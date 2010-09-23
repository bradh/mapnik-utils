import itertools

ids = itertools.count(0)

wkt = 'POLYGON((39.0234375 62.578125,20.0390625 58.359375,15.1171875 45.703125,15.8203125 35.15625,24.2578125 30.9375,35.5078125 30.234375,55.1953125 38.671875,58.7109375 46.40625,54.4921875 53.4375,51.6796875 58.359375,49.5703125 61.171875,39.0234375 62.578125))'

wkt2 = 'POLYGON((67.1484375 66.09375,53.0859375 55.546875,46.0546875 44.296875,48.8671875 35.15625,61.5234375 28.828125,73.4765625 33.75,78.3984375 40.78125,80.5078125 54.140625,77.6953125 61.171875,67.1484375 66.09375))'
import mapnik2

# Features
f = mapnik2.Feature(ids.next())
f.add_geometry(wkt)
f['name'] = 'one'
f2 = mapnik2.Feature(ids.next())
f2.add_geometry(wkt2)
f2['name'] = 'two'    

# Datasource
ds = mapnik2.MemoryDatasource()
ds.add_feature(f)
ds.add_feature(f2)

# Map
m = mapnik2.Map(600,300,'+init=epsg:4326')
m.background = mapnik2.Color('steelblue')

# Styles
poly = mapnik2.PolygonSymbolizer()
line = mapnik2.LineSymbolizer()
text = mapnik2.TextSymbolizer(mapnik2.Expression('[name]'), 'DejaVu Sans Book', 10, mapnik2.Color('black'))
s,r = mapnik2.Style(), mapnik2.Rule()
r.symbols.extend([poly,line,text])
s.rules.append(r)
m.append_style('My Style',s)

# Layer
lyr = mapnik2.Layer('test','+init=epsg:4326')
lyr.datasource = ds
lyr.styles.append('My Style')
m.layers.append(lyr)

# Render
m.zoom_to_box(lyr.envelope())
mapnik2.render_to_file(m, 'test.png')
