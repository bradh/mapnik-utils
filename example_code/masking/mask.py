#!/usr/bin/env python

import os
import mapnik2 as mapnik

tile = 256
# great lakes region
bbox = mapnik.Box2d(-96.020508,39.943436,-71.850586,49.553726)

map1 = mapnik.Map(tile,tile)
mapnik.load_map(map1,'land.xml')
map1.zoom_to_box(bbox)
map1.background = mapnik.Color('transparent')
im1 = mapnik.Image(tile,tile)
mapnik.render(map1,im1)

map2 = mapnik.Map(tile,tile)
mapnik.load_map(map2,'lakes.xml')
map2.background = mapnik.Color('transparent')
map2.zoom_to_box(bbox)

ops = [mapnik.CompositeOp.dst_out,mapnik.CompositeOp.multiply,mapnik.CompositeOp.src_out]

for op in ops:
    im2 = mapnik.Image(tile,tile)
    mapnik.render(map2,im2)
    im1.composite(im2,op)
    name = '%s.png' % op
    im1.save(name)
    os.system('open %s' % name)