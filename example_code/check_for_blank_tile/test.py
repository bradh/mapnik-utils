#!/usr/bin/env python

# sample script and tests to show how
# image backgrounds work and some simple
# ways to detect blank tiles, e.g. images
# with background but no other data rendered

import mapnik

w,h = 256,256

# create a map
m = mapnik.Map(w,h)

# new maps have a transparent background
# and from python are None
assert m.background is None

# so if we render this blank map to an image
# the image should be fully transparent

# create a new, fresh tile
im = mapnik.Image(w,h)

# then render
mapnik.render(m,im)

# lets ensure this rendered image still looks the same as a new one!
# it should be since we have no data in our map yet
# create a new one
new_im = mapnik.Image(w,h)

# one way to compare image output is to compare png-encoded strings
# compare things
assert new_im.tostring('png') == im.tostring('png')

# we can set the map background, and this will apply to our rendered image
# which is (in final effect) the same as setting it to be transparent
m.background = mapnik.Color('green')

# recreate a new, fresh tile
im = mapnik.Image(w,h)

# render
mapnik.render(m,im)

# this should be equivalent to a new image with green background
green = mapnik.Image(w,h)
green.background = mapnik.Color('green')

# make sure this is the case
assert green.tostring('png') == im.tostring('png')

# now lets load some data
mapnik.load_map(m,"map.xml")

# this sets the background of the map
# to 'steelblue' so lets ensure that
assert mapnik.Color('steelblue') == m.background

# but we have not initialized our map bounds yet
assert m.envelope() == mapnik.Envelope(-1.0,-1.0,0.0,0.0)

# so if we render the tile should be perfectly blue
# recreate a new, fresh tile
im = mapnik.Image(w,h)

# render
mapnik.render(m,im)

# make sure this is the case
steelblue = mapnik.Image(w,h)
steelblue.background = mapnik.Color('steelblue')
assert steelblue.tostring('png') == im.tostring('png')

# now, if we actually zoom to an area with data
# then our map should no longer be purely 'steelblue'
m.zoom_all()
mapnik.render(m,im)
assert len(im.tostring('png')) > len(steelblue.tostring('png'))

# finally, save the two tiles to the filesystem to ensure, visually,
# that they are different
im.save('world.png','png')
steelblue.save('blue.png','png')

