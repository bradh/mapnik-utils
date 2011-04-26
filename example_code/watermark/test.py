import mapnik

osm = mapnik.Image.open('osm.png')
watermark = mapnik.Image.open('watermark.png')
y_offset = 0
x_offset = 0
opacity = 1
osm.blend(x_offset,y_offset,watermark,opacity)
osm.save('osm_new.png')