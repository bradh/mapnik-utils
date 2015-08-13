# Nikweb: a Mapnik GeoJSON web service #

Submit some GeoJSON feature data via a HTTP request and receive your [Mapnik](http://mapnik.org/) map rendered with the features in the appropriate places.


## Licensing ##

Copyright (C) 2009 [Alpstein Tourismus GmbH & Co. KG](http://www.alpstein.de), and others.
See [AUTHORS](http://mapnik-utils.googlecode.com/svn/trunk/nikweb/AUTHORS) for details.

> This program is free software: you can redistribute it and/or modify it under the terms of the **GNU Lesser General Public License** as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.


## Requirements ##

  * Linux or OS X (might work on windows, patches welcome!)
  * [Python](http://www.python.org) >= 2.4
  * [GDAL](http://www.gdal.org) >= 1.5.0, compiled with GeoJSON support
  * [Cairo](http://cairographics.org/) 1.8 & python-cairo (optional, for PDF/SVG output)
  * [Mapnik](http://www.mapnik.org) >= 0.6.0, compiled with GDAL support (& other sources you want), and optionally Cairo support.
  * Python [SimpleJSON](http://undefined.org/python/#simplejson) (for Python < 2.6)
  * [WebOb](http://pythonpaste.org/webob/) >= 0.9 or [Django](http://www.djangoproject.com) >= 1.0 (for the web framework bits)

## Installing ##

To install it, run the following command inside this directory:

```
$ sudo python setup.py install
```

If you have the Python `easy_install` utility available, you can also type the following to download and install in one step:

```
$ sudo easy_install nikweb
$ sudo easy_install --upgrade nikweb    # to force upgrading
```

Or if you are using `pip`:

```
$ pip install nikweb
```

## Demos / Getting Started ##

See [examples/README](http://mapnik-utils.googlecode.com/svn/trunk/nikweb/examples/README)

| **Input Feature Data** | **Map File** | **Output Image** |
|:-----------------------|:-------------|:-----------------|
|[JSON](http://code.google.com/p/mapnik-utils/source/browse/trunk/nikweb/examples/example_0.json)|[Map XML](http://code.google.com/p/mapnik-utils/source/browse/trunk/nikweb/examples/example_0.xml)|<a href='http://mapnik-utils.googlecode.com/svn/wiki/nikweb_images/example_0.png'><img src='http://mapnik-utils.googlecode.com/svn/wiki/nikweb_images/example_0.png' /></a>|
|[JSON](http://code.google.com/p/mapnik-utils/source/browse/trunk/nikweb/examples/example_1.json)|[Map XML](http://code.google.com/p/mapnik-utils/source/browse/trunk/nikweb/examples/example_1.xml)|<a href='http://mapnik-utils.googlecode.com/svn/wiki/nikweb_images/example_1.png'><img src='http://mapnik-utils.googlecode.com/svn/wiki/nikweb_images/example_1.png' height='200' /></a>|
|[JSON](http://code.google.com/p/mapnik-utils/source/browse/trunk/nikweb/examples/example_2.json)|[Map XML](http://code.google.com/p/mapnik-utils/source/browse/trunk/nikweb/examples/example_2.xml)|<a href='http://mapnik-utils.googlecode.com/svn/wiki/nikweb_images/example_2.jpg'><img src='http://mapnik-utils.googlecode.com/svn/wiki/nikweb_images/example_2.jpg' height='200' /></a>|

## Requests ##

The views available are (assuming the default setup):
  * `/` - being the root of the WSGI app. Will return a list of available maps.
  * `/<map>/` - renders the specified map.

The map names are the names of the xml files from the `NIKWEB_MAP_DEFINITIONS` directory, without the '.xml' at the end. Note that '.XML' files will not work.


### Rendering ###

Rendering requests can be made via GET or POST. Note that GET request URLs are limited to 2KB on MSIE, and similar sizes for other browsers.

GET requests use the '`q`' parameter for the JSON data (ala `/url/?q=...`), POST uses the request body without form encoding.

The format of the JSON is basically a [GeoJSON FeatureCollection object](http://geojson.org/geojson-spec.html) with some additional (optional) parameters.

The additional parameters are:
  * `width`: width of the output map image.
  * `height`: height of the output map image.
  * `bbox_image`: `[minx, miny, maxx, maxx]`. Default is the extent of the submitted data.
  * `bbox_image_buffer`: `[value, units]`. When bbox\_image is not specified, buffer the extent of the submitted data by the specified value. Units are one of "`px`" (pixels in the output image), or "`map`" (map units).
  * format: output image mime-type. Default is "`image/png`". Available formats are:
    * `image/png`: 32-bit PNG
    * `image/jpeg`: JPEG
    * `image/png256`: 8-bit PNG
    * `text/svg+xml`: SVG (only if Mapnik was built with Cairo support)
    * `application/pdf`: PDF (only if Mapnik was built with Cairo support)
    * `application/postscript`: PostScript (only if Mapnik was built with Cairo support)

If `width` and `height` are specified, the resulting image will be that size. If `bbox_image` is specified, and one of `width`/`height` are specified, then the unspecified width or height is calculated based on the bounding box proportions.

All input data should be in the projection specified in the map XML file `<layer>` definition. If the `<map>` projection differs, then `bbox_image` must be specified, and should be in the `<map>` projection coordinates.

For the PDF and PostScript output formats, the image dimensions are all in points (1/72.0 inch).

## Map definitions ##

The map XML files (specified by `NIKWEB_MAP_DEFINITIONS`) are just standard [Mapnik XML files](http://trac.mapnik.org/wiki/XMLGettingStarted). For each layer where you want data sourced from the request, make the layer name something beginning with "`NIKWEB`" and don't include any `<Datasource>` element.

Any attributes specified by the GeoJSON Feature element 'properties' collections are available for filtering using the normal Mapnik `<filter>` method.


## Integrating ##

The core functionality sits in the `nikweb.render.MapnikRenderRequest` class. The `nikweb.http.MapnikHttp` class is a helper for the web views implemented by `nikweb.http.webob_server` and the `nikweb.http.django_views` modules.

Notes:
  * While Mapnik is threadsafe, GDAL (which is used for GeoJSON processing) may not be. If you're running into problems, use to a multi-process web server (prefork MPM, mod-wsgi daemon mode with threads=1, etc.). For more information see: http://trac.osgeo.org/gdal/wiki/FAQMiscellaneous

### WebOb Standalone Server ###

Nikweb bundles a [WebOb](http://pythonpaste.org/webob/) WSGI application and a standalone server in the `nikweb.http.webob_server` module.

Run:
```
$ nikweb/http/webob_server.py /path/to/map/files/
```

Find out the applicable options & environment variables via --help

### WebOb, Apache & mod-wsgi ###

In [examples/nikweb\_webob.wsgi](http://code.google.com/p/mapnik-utils/source/browse/trunk/nikweb/examples/nikweb_webob.wsgi) there is a sample WSGI file for use by [mod-wsgi](http://www.modwsgi.org/) within Apache. Copy it to an empty directory and edit it to set your paths appropriately.

Then in your apache config, add the path to a `WSGIScriptAlias` directive:

```
WSGIScriptAlias / /path/to/nikweb_config/apache/nikweb_webob.wsgi
<Directory /path/to/nikweb_config/apache>
  Order deny,allow
  Allow from all
</Directory>    
```

### Django ###

Nikweb bundles two [Django](http://www.djangoproject.com) views in the `nikweb.http.django_views` module.

Specify the Nikweb settings in the Django settings module:
  * `NIKWEB_MAP_DEFINITIONS`: local path to your map definitions (required)
  * `NIKWEB_MAP_LAYER_PREFIX`: layer prefix to use in the map XML files (optional; "NIKWEB")
  * `NIKWEB_DEFAULT_SIZE`: default map size tuple (optional; (512,512))

Add the following lines to the appropriate part of your urls.py file:

```
(r'$',                   'nikweb.http.django_views.nikweb_index'),
(r'(?P<map>[\w\.-]+)/$', 'nikweb.http.django_views.nikweb_render'),
```

## Contributing ##

Bug reports, suggestions, feedback, and contributions are all very welcome.

  * [Issue Tracker](http://code.google.com/p/mapnik-utils/issues/list)
  * [Mapnik Mailing Lists](http://mapnik.org/contact/)