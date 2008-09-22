#!/usr/bin/env python

"""

nik2img.py - In Mapnik xml, out Map image

Summary:
  A command line tool for generating map images by pointing to an XML file.
  Mirrors the shp2img utility developed by the MapServer project.
  shp2img reference: http://mapserver.gis.umn.edu/docs/reference/utilityreference/shp2img
 
Source:
 http://code.google.com/p/mapnik-utils/

Dependencies:
  Requires Python and Mapnik installed with the python bindings

Usage:
  # Copy the script to your path then:
  $ nik2img.py -h # help on usage
  $ nik2img.py -m mapfile.xml -o yourmap.png
  $ nik2img.py -m mapfile.xml -o yourmapsfolder -i all --debug -p epsg:900913 -r 1003750,-1706377,10037508,2810502 -t 2

Limitations:
  Paths to file system datasources in the XML files loaded will be relative to your dir.
  Very sparse on the error handling so far.
 
ToDo
  * Add docstrings and code comments.
  * Use has_key rather than try statements throughout.
  * Add ability to set resolutions for ZOOM_LEVELS
  * Refactor into a single function when run as main.
  * Support cairo renderer and formats.
  * Add a verbose output setting with timing tests and mapfile debugging.
  * Refactor debug to shp2img setting of debug type: graphics, zooms, times, mapfile, layers, all, etc.
  * Support variable substitution.
  * Ability to turn layers on and off (enable).
  * Map draw looping
  * Cascadenik integration | ability to read in css.mml or css.mss.
  * Allow for setting the path to datasources.
  
"""

__author__ = "Dane Springmeyer (dbsgeo [ -a- ] gmail.com"
__copyright__ = "Copyright 2008, Dane Springmeyer"
__version__ = "0.1 $Rev: 1 $"
__license__ = "GPLv2"

def usage (name):
  print
  color_print(3, "===========================================================================")
  color_print(2,"Usage: %s -m <mapnik.xml> -o <image.png>" % name)
  color_print(4,"-option\tstatus\t\t\tdescription")
  print "-m\t<required>\t\tMapfile: Path to xml map file to load styles from."
  print "-o\t<required>\t\tImage: Set the output filename (use .ext) or directory name (no .ext)"
  print "-i\t[default: png]\t\tFormat: Choose the output format (all, png, png256, jpeg)"
  print "-e\t[default: max extent]\tMinx,Miny,Maxx,Maxy: Set map extent in geographic (lon/lat) coordinates"
  print "-r\t[default: max extent]\tMinx,Miny,Maxx,Maxy: Set map extent in projected coordinates of mapfile"
  print "-s\t[default: 600,300]\tWidth,Height: Set the image size in pixels"
  print "-p\t[default: srs of mapfile]\tproj4 string: Set map display projection using -p <epsg:code>, ie epsg:900913"
  #print "-l\t[default:all enabled in mapfile]\t\tSet layers to enable (quote and comma separate if several)"  
  #print "-v\t[default:off]\t\tRun with verbose output"
  #print "-c\t[default:1]\t\tDraw map n number of times" 
  print "-t\t[default:0]\t\tPause n seconds after reading the map"
  print "--debug\t[default:0]\t\tLoop through all formats and zoom levels generating map graphics (more opt later)" 
  #print "-d\tDatavalue[default: None]: Variable substitution, ie override the projection"
  print "-h\t[default:off]\t\tPrints this usage information"
  color_print(3, "===========================================================================")
  color_print(7,"Dane Springmeyer, dbsgeo a-t gmail.com")
  print
 
def color_print(color,text):
    """
    1:red, 2:green, 3:yellow, 4: dark blue, 5:pink, 6:teal blue, 7:white
    """
    print "\033[9%sm%s\033[0m" % (color,text)
    
def output_error(msg, E=None, yield_usage=False):
    if E:
      color_print(1, '// --> %s: \n\n %s' % (msg, E))
    else:
      color_print(1, '// --> %s' % msg)    
    if yield_usage:
      usage(sys.argv[0])
    sys.exit(1)

def is_file(name):
    if name.find('.') > -1 and name.count('.') == 1:
        return True
    elif name.rfind('.') - (len(name)+1) == -3:
        return True
    elif name.find('.') > -1 and name.count('.') <> 1:
        output_error("Unknown output type; cannot guess whether it's a file or directory")
    else:
        return False

if __name__ == "__main__":
  import os
  import sys
  import getopt
  import time
  
  WIDTH = 600
  HEIGHT = 300
  AGG_FORMATS = {'png':'.png','png256':'.png','jpeg':'.jpg'}
  ZOOM_LEVELS = [x*.1 for x in range(1,10)]
  ZOOM_LEVELS.reverse()
  FORMAT = 'png'
  run = False  
  run_verbose = False
  built_test_outputs = False
  var = {}        # In/Out paths

  try:
    opts, args = getopt.getopt(sys.argv[1:], "m:o:i:e:s:d:r:p:t:vh", ['debug'])
  except getopt.GetoptError, err:
    output_error(err,yield_usage=True)
  
  if len(sys.argv) <= 1:
    usage(sys.argv[0])
    sys.exit(1)
  
  for opt, arg in opts:
    if opt == "-m":
         var['m'] = arg
    elif opt == "-o":
        var['o'] = arg
    elif opt == "-i":
        var['i'] = arg
    elif opt == "-e":
        var['e'] = arg
    elif opt == "-p":
        var['p'] = arg
    elif opt == "-r":
        var['r'] = arg
    elif opt == "-t":
        var['t'] = arg
    elif opt == "-s":
        var['s'] = arg
    #elif opt == "-l":
        #var['l'] = arg   
    #elif opt == "-c":
        #var['c'] = arg   
    #elif opt == "-d":
        #var['d'] = arg        
    #elif opt == "-v":
        #run_verbose = True
    elif opt == "--debug":
        built_test_outputs = True
    elif opt == "-h":
        usage(sys.argv[0])
        sys.exit(1)
    
  if len(var) < 2:
    output_error('Make sure to specify the -m <input mapfile.xml> and -o <output image>',yield_usage=True)
  else:
    run = True
    import os
    
    try:
        import mapnik
        color_print (4,'Loading mapnik python bindings...')
    except:
        output_error('Could not load mapnik python bindings')

  try:
    xml = open(var['m'], "r");
    print "//-- Confirmed path to XML file: %s" % var['m']
    xml.close()
  except IOError:
    output_error("Cannot open XML file: %s" % var['m'])

  if not run:
    sys.exit(1)

  if var.has_key('s'):
    WIDTH,HEIGHT = var['s'].split(',')
  
  try:
    WIDTH = int(WIDTH)
  except Exception, E:
    output_error("Width must be an integer",E)

  try:
    HEIGHT = int(HEIGHT)
  except Exception, E:
    output_error("Height must be an integer",E)

  try:
    mapnik_map = mapnik.Map(WIDTH,HEIGHT)
  except Exception, E:
    output_error("Problem initiating map",E)
    
  try:    
    mapnik.load_map(mapnik_map, var['m'])  
  except Exception, E:
    output_error("Problem loading map",E)

  if var.has_key('t'):
    time.sleep(float(var['t']))

  if var.has_key('p'):
    if var['p'] == "epsg:900913":
      google_merc = '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +no_defs +over'
      epsg = mapnik.Projection(google_merc)
    else:
      epsg = mapnik.Projection("+init=%s" % var['p'])
    mapnik_map.srs = epsg.params()
       
  if var.has_key('e'):
    try:
      bbox = [float(x) for x in var['e'].split(",")]
      bbox = mapnik.Envelope(*bbox)
      p = mapnik.Projection("%s" % mapnik_map.srs)
      if not p.geographic:
        print '// -- Initialized projection: %s' % p.params()
        bbox = mapnik.forward_(bbox, p)
    except Exception, E:
       output_error("Problem setting geographic bounding box", E)
    mapnik_map.zoom_to_box(bbox)
  elif var.has_key('r'):
    try:
      bbox = [float(x) for x in var['r'].split(",")]
      bbox = mapnik.Envelope(*bbox)
    except Exception, E:
       output_error("Problem setting projected bounding box", E)
    mapnik_map.zoom_to_box(bbox)
  else:
    try:    
      mapnik_map.zoom_all()
    except Exception, E:
      output_error("Problem Zooming to all layers",E)
  
  o = var['o']
  if not is_file(o):
      try:
        os.mkdir(o)
      except OSError:
        color_print(1,'// -- Directory already exists, doing nothing...')
      o = '%s/%s.%s' % (o,o,FORMAT)
  if not built_test_outputs:    
    try:
      if var['i'] == 'all':
        o = o.split('.')[0]
        for k, v in AGG_FORMATS.iteritems():
          try:  
            mapnik.render_to_file(mapnik_map,'%s_%s%s' % (o,k,v), k)
          except Exception, E:
            output_error("Error when rendering to file",E)
      elif var['i']:
        mapnik.render_to_file(mapnik_map,o, var['i'])
    except KeyError:
      mapnik.render_to_file(mapnik_map,o,FORMAT)  
    except Exception, E:
      output_error("Error when rendering to file",E)
  else:
    for lev in ZOOM_LEVELS:
      mapnik_map.zoom(lev)
      print mapnik_map.scale()
      o_name = '%s_level-%s' % (o.split('.')[0],lev)
      try:
        if var['i'] == 'all':
          for k, v in AGG_FORMATS.iteritems():
            try:
              file = '%s_%s%s' % (o_name,k,v)
              color_print (1,file)
              mapnik.render_to_file(mapnik_map,file, k)
            except Exception, E:
              output_error("Error when rendering to file",E)
        elif var['i']:
            mapnik.render_to_file(mapnik_map,o_name, var['i'])
      except KeyError:
        mapnik.render_to_file(mapnik_map,'%s.%s' % (o_name,FORMAT),FORMAT)  
      except Exception, E:
        output_error("Error when rendering to file",E)