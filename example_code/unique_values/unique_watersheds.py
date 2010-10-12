#!/usr/bin/env python

import mapnik
import random

if not mapnik.mapnik_version() > 700:
    raise SystemExit('At least Mapnik 0.7.0 is required for this script')

def random_rgb():
  return int(random.random() * 255)

def generate_unique_values(features):
    s = mapnik.Style()
    for feat in range(1,features+1):
        r = mapnik.Rule('%s' % feat)
        condition = '[ID]=%s' % (feat)
        r.filter = mapnik.Filter(condition)
        rgb = '%s%s,%s%s,%s%s' % (random_rgb(),'%',random_rgb(),'%',random_rgb(),'%')
        p = mapnik.PolygonSymbolizer(mapnik.Color('rgb(%s)' % rgb))
        p.gamma = .65
        r.symbols.append(p)
        #r.symbols.append(LineSymbolizer(Color('black'),.1))
        s.rules.append(r)
    return s

if __name__ == '__main__':

    # http://spatialreference.org/ref/user/north-pacific-albers-conic-equal-area/
    north_pacific_albers = '+proj=aea +lat_1=30 +lat_2=70 +lat_0=52 +lon_0=-170 +x_0=0 +y_0=0 +ellps=GRS80 +datum=NAD83 +units=m +no_defs'

    m = mapnik.Map(1000, 550, north_pacific_albers)
    
    lyr = mapnik.Layer('shape',north_pacific_albers)
    lyr.datasource = mapnik.Shapefile(file='../../data/north_pacific_ecoregions.shp')
    num_features = len(lyr.datasource.all_features())
    
    # Attach random RGB values to PolygonSymbolizer
    m.append_style('Random RGB values',generate_unique_values(num_features))
    lyr.styles.append('Random RGB values')
    
    # text styles, placed in separate style so text is always on top
    s,r = mapnik.Style(),mapnik.Rule()
    t = mapnik.TextSymbolizer('ECOREGION', 'DejaVu Sans Bold', 10, mapnik.Color('black'))
    t.wrap_width = 40
    t.halo_fill = mapnik.Color('white')
    t.halo_radius = 1
    r.symbols.append(t)
    s.rules.append(r)  
    m.append_style('Labels',s)
    lyr.styles.append('Labels')

    m.layers.append(lyr)
    m.zoom_to_box(lyr.envelope())
    
    mapnik.render_to_file(m,'map/unique_values.png')
