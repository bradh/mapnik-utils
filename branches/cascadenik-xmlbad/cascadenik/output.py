import style

try:
    import mapnik
except ImportError:
    # Map.to_mapnik won't work, maybe that's okay?
    pass

class Map:
    def __init__(self, srs=None, layers=None, bgcolor=None):
        assert srs is None or type(srs) is str
        assert layers is None or type(layers) in (list, tuple)
        assert bgcolor is None or bgcolor.__class__ is style.color or bgcolor == 'transparent'
        
        self.srs = srs
        self.layers = layers or []
        self.bgcolor = bgcolor

    def __repr__(self):
        return 'Map(%s %s)' % (self.bgcolor, repr(self.layers))

    def to_mapnik(self, mmap):
        """
        """
        mmap.srs = self.srs or mmap.srs
        mmap.bgcolor = str(self.bgcolor) or mmap.bgcolor
        
        ids = (i for i in xrange(1, 999999))
        
        for layer in self.layers:
            for style in layer.styles:

                sty = mapnik.Style()
                
                for rule in style.rules:
                    rul = mapnik.Rule('rule %d' % ids.next())
                    rul.filter = rule.filter and mapnik.Filter(rule.filter.text) or rul.filter
                    rul.min_scale = rule.minscale and rule.minscale.value or rul.min_scale
                    rul.max_scale = rule.maxscale and rule.maxscale.value or rul.max_scale
                    
                    for symbolizer in rule.symbolizers:
                    
                        if symbolizer.__class__ is PolygonSymbolizer:
                            sym = mapnik.PolygonSymbolizer(mapnik.Color(str(symbolizer.color)))
                            sym.fill_opacity = symbolizer.opacity

                        elif symbolizer.__class__ is LineSymbolizer:
                            stroke = mapnik.Stroke(mapnik.Color(str(symbolizer.color)), symbolizer.width)
                            stroke.opacity = symbolizer.opacity or stroke.opacity
                            stroke.line_cap = symbolizer.cap or stroke.line_cap
                            stroke.line_join = symbolizer.join or stroke.line_join
                            sym = mapnik.LineSymbolizer(stroke)

                        elif symbolizer.__class__ is TextSymbolizer:
                            sym = mapnik.TextSymbolizer(symbolizer.name, symbolizer.face_name, symbolizer.size,
                                                        mapnik.Color(str(symbolizer.color)))

                            sym.wrap_width = symbolizer.wrap_width or sym.wrap_width
                            sym.label_spacing = symbolizer.spacing or sym.label_spacing
                            sym.label_position_tolerance = symbolizer.label_position_tolerance or sym.label_position_tolerance
                            sym.max_char_angle_delta = symbolizer.max_char_angle_delta or sym.max_char_angle_delta
                            sym.halo_fill = symbolizer.halo_color or sym.halo_fill
                            sym.halo_radius = symbolizer.halo_radius or sym.halo_radius
                            sym.avoid_edges = symbolizer.avoid_edges or sym.avoid_edges
                            sym.minimum_distance = symbolizer.min_distance or sym.minimum_distance
                            sym.allow_overlap = symbolizer.allow_overlap or sym.allow_overlap
                            
                            sym.displacement(symbolizer.dx or 0, symbolizer.dy or 0)

                        else:
                            continue
                        
                        rul.symbols.append(sym)
                    sty.rules.append(rul)
                mmap.append_style(style.name, sty)

            lay = mapnik.Layer(layer.name)
            lay.srs = layer.srs or lay.srs
            lay.minzoom = layer.minzoom or lay.minzoom
            lay.maxzoom = layer.maxzoom or lay.maxzoom
            
            for style in layer.styles:
                lay.styles.append(style.name)

            mmap.layers.append(lay)
                    
                    
        

class Style:
    def __init__(self, name, rules):
        assert name is None or type(name) is str
        assert rules is None or type(rules) in (list, tuple)
        
        self.name = name
        self.rules = rules or []

    def __repr__(self):
        return 'Style(%s: %s)' % (self.name, repr(self.rules))

class Rule:
    def __init__(self, minscale, maxscale, filter, symbolizers):
        assert minscale is None or minscale.__class__ is MinScaleDenominator
        assert maxscale is None or maxscale.__class__ is MaxScaleDenominator
        assert filter is None or filter.__class__ is Filter

        self.minscale = minscale
        self.maxscale = maxscale
        self.filter = filter
        self.symbolizers = symbolizers

    def __repr__(self):
        return 'Rule(%s:%s, %s, %s)' % (repr(self.minscale), repr(self.maxscale), repr(self.filter), repr(self.symbolizers))

class Layer:
    def __init__(self, name, datasource, styles=None, srs=None, minzoom=None, maxzoom=None):
        assert type(name) is str
        assert styles is None or type(styles) in (list, tuple)
        assert srs is None or type(srs) is str
        assert minzoom is None or type(minzoom) in (int, float)
        assert maxzoom is None or type(maxzoom) in (int, float)
        
        self.name = name
        self.datasource = datasource
        self.styles = styles or []
        self.srs = srs
        self.minzoom = minzoom
        self.maxzoom = maxzoom

    def __repr__(self):
        return 'Layer(%s: %s)' % (self.name, repr(self.styles))

class Datasource:
    def __init__(self, plugin_name, **parameters):
        self.parameters = dict([('plugin_name', plugin_name)] + parameters.items())

class MinScaleDenominator:
    def __init__(self, value):
        assert type(value) is int
        self.value = value

    def __repr__(self):
        return str(self.value)

class MaxScaleDenominator:
    def __init__(self, value):
        assert type(value) is int
        self.value = value

    def __repr__(self):
        return str(self.value)

class Filter:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return str(self.text)

class PolygonSymbolizer:
    def __init__(self, color, opacity=None):
        assert color.__class__ is style.color
        assert opacity is None or type(opacity) in (int, float)

        self.color = color
        self.opacity = opacity or 1.0

    def __repr__(self):
        return 'Polygon(%s, %s)' % (self.color, self.opacity)

class LineSymbolizer:
    def __init__(self, color, width, opacity=None, join=None, cap=None, dashes=None):
        assert color.__class__ is style.color
        assert type(width) in (int, float)
        assert opacity is None or type(opacity) in (int, float)
        assert join is None or type(join) is str
        assert cap is None or type(cap) is str
        assert dashes is None or dashes.__class__ is style.numbers

        self.color = color
        self.width = width
        self.opacity = opacity
        self.join = join
        self.cap = cap
        self.dashes = dashes

    def __repr__(self):
        return 'Line(%s, %s)' % (self.color, self.width)

class TextSymbolizer:
    def __init__(self, name, face_name, size, color, wrap_width=None, \
        spacing=None, label_position_tolerance=None, max_char_angle_delta=None, \
        halo_color=None, halo_radius=None, dx=None, dy=None, avoid_edges=None, \
        min_distance=None, allow_overlap=None, placement=None):

        assert type(name) is str
        assert type(face_name) is str
        assert type(size) is int
        assert color.__class__ is style.color
        assert wrap_width is None or type(wrap_width) is int
        assert spacing is None or type(spacing) is int
        assert label_position_tolerance is None or type(label_position_tolerance) is int
        assert max_char_angle_delta is None or type(max_char_angle_delta) is int
        assert halo_color is None or halo_color.__class__ is style.color
        assert halo_radius is None or type(halo_radius) is int
        assert dx is None or type(dx) is int
        assert dy is None or type(dy) is int
        assert avoid_edges is None or avoid_edges.__class__ is style.boolean
        assert min_distance is None or type(min_distance) is int
        assert allow_overlap is None or allow_overlap.__class__ is style.boolean
        assert placement is None or type(placement) is str

        self.name = name
        self.face_name = face_name
        self.size = size
        self.color = color

        self.wrap_width = wrap_width
        self.spacing = spacing
        self.label_position_tolerance = label_position_tolerance
        self.max_char_angle_delta = max_char_angle_delta
        self.halo_color = halo_color
        self.halo_radius = halo_radius
        self.dx = dx
        self.dy = dy
        self.avoid_edges = avoid_edges
        self.min_distance = min_distance
        self.allow_overlap = allow_overlap
        self.placement = placement

    def __repr__(self):
        return 'Text(%s, %s)' % (self.face_name, self.size)

class ShieldSymbolizer:
    def __init__(self, face_name=None, size=None, file=None, filetype=None, width=None, height=None, color=None, min_distance=None):
        assert face_name and size or file
        
        assert face_name is None or type(face_name) is str
        assert size is None or type(size) is int
        assert width is None or type(width) is int
        assert height is None or type(height) is int

        assert color is None or color.__class__ is style.color
        assert min_distance is None or type(min_distance) is int

        self.face_name = face_name
        self.size = size
        self.file = file
        self.type = filetype
        self.width = width
        self.height = height

        self.color = color
        self.min_distance = min_distance

    def __repr__(self):
        return 'Shield(%s, %s, %s)' % (self.face_name, self.size, self.file)

class PointSymbolizer:
    def __init__(self, file, filetype, width, height, allow_overlap=None):
        assert type(file) is str
        assert type(filetype) is str
        assert type(width) is int
        assert type(height) is int
        assert allow_overlap is None or allow_overlap.__class__ is style.boolean

        self.file = file
        self.type = filetype
        self.width = width
        self.height = height
        self.allow_overlap = allow_overlap

    def __repr__(self):
        return 'Point(%s)' % self.file

class PolygonPatternSymbolizer(PointSymbolizer):
    def __init__(self, file, filetype, width, height):
        PointSymbolizer.__init__(self, file, filetype, width, height)
    
    def __repr__(self):
        return 'PolyPat(%s)' % self.file

class LinePatternSymbolizer(PointSymbolizer):
    def __init__(self, file, filetype, width, height):
        PointSymbolizer.__init__(self, file, filetype, width, height)
    
    def __repr__(self):
        return 'LinePat(%s)' % self.file
