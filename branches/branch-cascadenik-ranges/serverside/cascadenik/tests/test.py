import sys
import unittest
import xml.etree.ElementTree
from cascadenik.style import ParseException, stylesheet_rulesets, rulesets_declarations, stylesheet_declarations
from cascadenik.style import Selector, SelectorElement, SelectorAttributeTest
from cascadenik.style import postprocess_property, postprocess_value, Property
from cascadenik.compile import tests_filter_combinations, Filter, selectors_tests
from cascadenik.compile import filtered_property_declarations, is_applicable_selector
from cascadenik.compile import add_polygon_style, add_line_style, add_text_styles, add_shield_styles
from cascadenik.compile import add_point_style, add_polygon_pattern_style, add_line_pattern_style

class ParseTests(unittest.TestCase):
    
    def testBadSelector1(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Too Many Things { }')

    def testBadSelector2(self):
        self.assertRaises(ParseException, stylesheet_rulesets, '{ }')

    def testBadSelector3(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Illegal { }')

    def testBadSelector4(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer foo[this=that] { }')

    def testBadSelector5(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer[this>that] foo { }')

    def testBadSelector6(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer foo#bar { }')

    def testBadSelector7(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer foo.bar { }')

    def testBadSelectorTest1(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer[foo>] { }')

    def testBadSelectorTest2(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer[foo><bar] { }')

    def testBadSelectorTest3(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer[foo<<bar] { }')

    def testBadSelectorTest4(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer[<bar] { }')

    def testBadSelectorTest5(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer[<<bar] { }')

    def testBadProperty1(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer { unknown-property: none; }')

    def testBadProperty2(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer { extra thing: none; }')

    def testBadProperty3(self):
        self.assertRaises(ParseException, stylesheet_rulesets, 'Layer { "not an ident": none; }')

    def testRulesets1(self):
        self.assertEqual(0, len(stylesheet_rulesets('/* empty stylesheet */')))

    def testRulesets2(self):
        self.assertEqual(1, len(stylesheet_rulesets('Layer { }')))

    def testRulesets3(self):
        self.assertEqual(2, len(stylesheet_rulesets('Layer { } Layer { }')))

    def testRulesets4(self):
        self.assertEqual(3, len(stylesheet_rulesets('Layer { } /* something */ Layer { } /* extra */ Layer { }')))

    def testRulesets5(self):
        self.assertEqual(1, len(stylesheet_rulesets('Map { }')))

class SelectorTests(unittest.TestCase):
    
    def testSpecificity1(self):
        self.assertEqual((0, 1, 0), Selector(SelectorElement(['Layer'])).specificity())
    
    def testSpecificity2(self):
        self.assertEqual((0, 2, 0), Selector(SelectorElement(['Layer']), SelectorElement(['name'])).specificity())
    
    def testSpecificity3(self):
        self.assertEqual((0, 2, 0), Selector(SelectorElement(['Layer', '.class'])).specificity())
    
    def testSpecificity4(self):
        self.assertEqual((0, 3, 0), Selector(SelectorElement(['Layer', '.class']), SelectorElement(['name'])).specificity())
    
    def testSpecificity5(self):
        self.assertEqual((1, 2, 0), Selector(SelectorElement(['Layer', '#id']), SelectorElement(['name'])).specificity())
    
    def testSpecificity6(self):
        self.assertEqual((1, 0, 0), Selector(SelectorElement(['#id'])).specificity())
    
    def testSpecificity7(self):
        self.assertEqual((1, 0, 1), Selector(SelectorElement(['#id'], [SelectorAttributeTest('a', '>', 'b')])).specificity())
    
    def testSpecificity8(self):
        self.assertEqual((1, 0, 2), Selector(SelectorElement(['#id'], [SelectorAttributeTest('a', '>', 'b'), SelectorAttributeTest('a', '<', 'b')])).specificity())

    def testSpecificity9(self):
        self.assertEqual((1, 0, 2), Selector(SelectorElement(['#id'], [SelectorAttributeTest('a', '>', 100), SelectorAttributeTest('a', '<', 'b')])).specificity())

    def testMatch1(self):
        self.assertEqual(True, Selector(SelectorElement(['Layer'])).matches('Layer', 'foo', []))

    def testMatch2(self):
        self.assertEqual(True, Selector(SelectorElement(['#foo'])).matches('Layer', 'foo', []))

    def testMatch3(self):
        self.assertEqual(False, Selector(SelectorElement(['#foo'])).matches('Layer', 'bar', []))

    def testMatch4(self):
        self.assertEqual(True, Selector(SelectorElement(['.bar'])).matches('Layer', None, ['bar']))

    def testMatch5(self):
        self.assertEqual(True, Selector(SelectorElement(['.bar'])).matches('Layer', None, ['bar', 'baz']))

    def testMatch6(self):
        self.assertEqual(True, Selector(SelectorElement(['.bar', '.baz'])).matches('Layer', None, ['bar', 'baz']))

    def testMatch7(self):
        self.assertEqual(False, Selector(SelectorElement(['.bar', '.baz'])).matches('Layer', None, ['bar']))

    def testMatch8(self):
        self.assertEqual(False, Selector(SelectorElement(['Layer'])).matches('Map', None, []))

    def testMatch9(self):
        self.assertEqual(False, Selector(SelectorElement(['Map'])).matches('Layer', None, []))

    def testMatch10(self):
        self.assertEqual(True, Selector(SelectorElement(['*'])).matches('Layer', None, []))

    def testMatch10(self):
        self.assertEqual(True, Selector(SelectorElement(['*'])).matches('Map', None, []))

    def testRange1(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('scale-denominator', '>', 100)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(False, selector.inRange(99))
        self.assertEqual(False, selector.inRange(100))
        self.assertEqual(True, selector.inRange(1000))

    def testRange2(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('scale-denominator', '>=', 100)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(True, selector.isMapScaled())
        self.assertEqual(False, selector.inRange(99))
        self.assertEqual(True, selector.inRange(100))
        self.assertEqual(True, selector.inRange(1000))

    def testRange3(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('scale-denominator', '<', 100)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(True, selector.isMapScaled())
        self.assertEqual(True, selector.inRange(99))
        self.assertEqual(False, selector.inRange(100))
        self.assertEqual(False, selector.inRange(1000))

    def testRange4(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('scale-denominator', '<=', 100)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(True, selector.isMapScaled())
        self.assertEqual(True, selector.inRange(99))
        self.assertEqual(True, selector.inRange(100))
        self.assertEqual(False, selector.inRange(1000))

    def testRange5(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('nonsense', '<=', 100)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(False, selector.isMapScaled())
        self.assertEqual(True, selector.inRange(99))
        self.assertEqual(True, selector.inRange(100))
        self.assertEqual(False, selector.inRange(1000))

    def testRange6(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('scale-denominator', '>=', 100), SelectorAttributeTest('scale-denominator', '<', 1000)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(True, selector.isMapScaled())
        self.assertEqual(False, selector.inRange(99))
        self.assertEqual(True, selector.inRange(100))
        self.assertEqual(False, selector.inRange(1000))

    def testRange7(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('scale-denominator', '>', 100), SelectorAttributeTest('scale-denominator', '<=', 1000)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(True, selector.isMapScaled())
        self.assertEqual(False, selector.inRange(99))
        self.assertEqual(False, selector.inRange(100))
        self.assertEqual(True, selector.inRange(1000))

    def testRange8(self):
        selector = Selector(SelectorElement(['*'], [SelectorAttributeTest('scale-denominator', '<=', 100), SelectorAttributeTest('scale-denominator', '>=', 1000)]))
        self.assertEqual(True, selector.isRanged())
        self.assertEqual(True, selector.isMapScaled())
        self.assertEqual(False, selector.inRange(99))
        self.assertEqual(False, selector.inRange(100))
        self.assertEqual(False, selector.inRange(1000))

class PropertyTests(unittest.TestCase):

    def testProperty1(self):
        self.assertRaises(ParseException, postprocess_property, [('IDENT', 'too-many'), ('IDENT', 'properties')])

    def testProperty2(self):
        self.assertRaises(ParseException, postprocess_property, [])

    def testProperty3(self):
        self.assertRaises(ParseException, postprocess_property, [('IDENT', 'illegal-property')])

    def testProperty4(self):
        self.assertEqual('shield', postprocess_property([('IDENT', 'shield-fill')]).group())

    def testProperty5(self):
        self.assertEqual('shield', postprocess_property([('S', ' '), ('IDENT', 'shield-fill'), ('COMMENT', 'ignored comment')]).group())

class ValueTests(unittest.TestCase):

    def testBadValue1(self):
        self.assertRaises(ParseException, postprocess_value, [], Property('polygon-opacity'))

    def testBadValue2(self):
        self.assertRaises(ParseException, postprocess_value, [('IDENT', 'too'), ('IDENT', 'many')], Property('polygon-opacity'))

    def testBadValue3(self):
        self.assertRaises(ParseException, postprocess_value, [('IDENT', 'non-number')], Property('polygon-opacity'))

    def testBadValue4(self):
        self.assertRaises(ParseException, postprocess_value, [('IDENT', 'non-string')], Property('text-face-name'))

    def testBadValue5(self):
        self.assertRaises(ParseException, postprocess_value, [('IDENT', 'non-hash')], Property('polygon-fill'))

    def testBadValue6(self):
        self.assertRaises(ParseException, postprocess_value, [('HASH', '#badcolor')], Property('polygon-fill'))

    def testBadValue7(self):
        self.assertRaises(ParseException, postprocess_value, [('IDENT', 'non-URI')], Property('point-file'))

    def testBadValue8(self):
        self.assertRaises(ParseException, postprocess_value, [('IDENT', 'bad-boolean')], Property('text-avoid-edges'))

    def testBadValue9(self):
        self.assertRaises(ParseException, postprocess_value, [('STRING', 'not an IDENT')], Property('line-join'))

    def testBadValue10(self):
        self.assertRaises(ParseException, postprocess_value, [('IDENT', 'not-in-tuple')], Property('line-join'))

    def testBadValue11(self):
        self.assertRaises(ParseException, postprocess_value, [('NUMBER', '1'), ('CHAR', ','), ('CHAR', ','), ('NUMBER', '3')], Property('line-dasharray'))

    def testValue1(self):
        self.assertEqual(1.0, postprocess_value([('NUMBER', '1.0')], Property('polygon-opacity')).value)

    def testValue2(self):
        self.assertEqual(10, postprocess_value([('NUMBER', '10')], Property('line-width')).value)

    def testValue2b(self):
        self.assertEqual(-10, postprocess_value([('CHAR', '-'), ('NUMBER', '10')], Property('text-dx')).value)

    def testValue3(self):
        self.assertEqual('DejaVu', str(postprocess_value([('STRING', '"DejaVu"')], Property('text-face-name'))))

    def testValue4(self):
        self.assertEqual('#ff9900', str(postprocess_value([('HASH', '#ff9900')], Property('map-bgcolor'))))

    def testValue5(self):
        self.assertEqual('#ff9900', str(postprocess_value([('HASH', '#f90')], Property('map-bgcolor'))))

    def testValue6(self):
        self.assertEqual('http://example.com', str(postprocess_value([('URI', 'url("http://example.com")')], Property('point-file'))))

    def testValue7(self):
        self.assertEqual('true', str(postprocess_value([('IDENT', 'true')], Property('text-avoid-edges'))))

    def testValue8(self):
        self.assertEqual('false', str(postprocess_value([('IDENT', 'false')], Property('text-avoid-edges'))))

    def testValue9(self):
        self.assertEqual('bevel', str(postprocess_value([('IDENT', 'bevel')], Property('line-join'))))

    def testValue10(self):
        self.assertEqual('1,2,3', str(postprocess_value([('NUMBER', '1'), ('CHAR', ','), ('NUMBER', '2'), ('CHAR', ','), ('NUMBER', '3')], Property('line-dasharray'))))

    def testValue11(self):
        self.assertEqual('1,2.0,3', str(postprocess_value([('NUMBER', '1'), ('CHAR', ','), ('S', ' '), ('NUMBER', '2.0'), ('CHAR', ','), ('NUMBER', '3')], Property('line-dasharray'))))

class CascadeTests(unittest.TestCase):

    def testCascade1(self):
        s = """
            Layer
            {
                text-dx: -10;
                text-dy: -10;
            }
        """
        rulesets = stylesheet_rulesets(s)
        
        self.assertEqual(1, len(rulesets))
        self.assertEqual(1, len(rulesets[0]['selectors']))
        self.assertEqual(1, len(rulesets[0]['selectors'][0].elements))

        self.assertEqual(2, len(rulesets[0]['declarations']))
        self.assertEqual('text-dx', rulesets[0]['declarations'][0]['property'].name)
        self.assertEqual(-10, rulesets[0]['declarations'][0]['value'].value)
        
        declarations = rulesets_declarations(rulesets)
        
        self.assertEqual(2, len(declarations))
        self.assertEqual('text-dx', declarations[0].property.name)
        self.assertEqual('text-dy', declarations[1].property.name)

    def testCascade2(self):
        s = """
            * { text-fill: #ff9900 !important; }

            Layer#foo.foo[baz>10] bar,
            *
            {
                polygon-fill: #f90;
                text-face-name: /* boo yah */ "Helvetica Bold";
                text-size: 10;
                polygon-pattern-file: url('http://example.com');
                line-cap: square;
                text-allow-overlap: false;
                text-dx: -10;
            }
        """
        rulesets = stylesheet_rulesets(s)
        
        self.assertEqual(2, len(rulesets))
        self.assertEqual(1, len(rulesets[0]['selectors']))
        self.assertEqual(1, len(rulesets[0]['selectors'][0].elements))
        self.assertEqual(2, len(rulesets[1]['selectors']))
        self.assertEqual(2, len(rulesets[1]['selectors'][0].elements))
        self.assertEqual(1, len(rulesets[1]['selectors'][1].elements))
        
        declarations = rulesets_declarations(rulesets)

        self.assertEqual(15, len(declarations))

        self.assertEqual('*', str(declarations[0].selector))
        self.assertEqual('polygon-fill', declarations[0].property.name)
        self.assertEqual('#ff9900', str(declarations[0].value))

        self.assertEqual('*', str(declarations[1].selector))
        self.assertEqual('text-face-name', declarations[1].property.name)
        self.assertEqual('Helvetica Bold', str(declarations[1].value))

        self.assertEqual('*', str(declarations[2].selector))
        self.assertEqual('text-size', declarations[2].property.name)
        self.assertEqual('10', str(declarations[2].value))

        self.assertEqual('*', str(declarations[3].selector))
        self.assertEqual('polygon-pattern-file', declarations[3].property.name)
        self.assertEqual('http://example.com', str(declarations[3].value))

        self.assertEqual('*', str(declarations[4].selector))
        self.assertEqual('line-cap', declarations[4].property.name)
        self.assertEqual('square', str(declarations[4].value))

        self.assertEqual('*', str(declarations[5].selector))
        self.assertEqual('text-allow-overlap', declarations[5].property.name)
        self.assertEqual('false', str(declarations[5].value))

        self.assertEqual('*', str(declarations[6].selector))
        self.assertEqual('text-dx', declarations[6].property.name)
        self.assertEqual('-10', str(declarations[6].value))

        self.assertEqual('Layer#foo.foo[baz>10] bar', str(declarations[7].selector))
        self.assertEqual('polygon-fill', declarations[7].property.name)
        self.assertEqual('#ff9900', str(declarations[7].value))

        self.assertEqual('Layer#foo.foo[baz>10] bar', str(declarations[8].selector))
        self.assertEqual('text-face-name', declarations[8].property.name)
        self.assertEqual('Helvetica Bold', str(declarations[8].value))

        self.assertEqual('Layer#foo.foo[baz>10] bar', str(declarations[9].selector))
        self.assertEqual('text-size', declarations[9].property.name)
        self.assertEqual('10', str(declarations[9].value))

        self.assertEqual('Layer#foo.foo[baz>10] bar', str(declarations[10].selector))
        self.assertEqual('polygon-pattern-file', declarations[10].property.name)
        self.assertEqual('http://example.com', str(declarations[10].value))

        self.assertEqual('Layer#foo.foo[baz>10] bar', str(declarations[11].selector))
        self.assertEqual('line-cap', declarations[11].property.name)
        self.assertEqual('square', str(declarations[11].value))

        self.assertEqual('Layer#foo.foo[baz>10] bar', str(declarations[12].selector))
        self.assertEqual('text-allow-overlap', declarations[12].property.name)
        self.assertEqual('false', str(declarations[12].value))

        self.assertEqual('Layer#foo.foo[baz>10] bar', str(declarations[13].selector))
        self.assertEqual('text-dx', declarations[13].property.name)
        self.assertEqual('-10', str(declarations[13].value))

        self.assertEqual('*', str(declarations[14].selector))
        self.assertEqual('text-fill', declarations[14].property.name)
        self.assertEqual('#ff9900', str(declarations[14].value))

class FilterCombinationTests(unittest.TestCase):

    def testFilters1(self):
        s = """
            Layer[landuse=military]     { polygon-fill: #000; }
            Layer[landuse=civilian]     { polygon-fill: #001; }
            Layer[landuse=agriculture]  { polygon-fill: #010; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 4)
        self.assertEqual(str(sorted(filters)), '[[landuse!=agriculture][landuse!=civilian][landuse!=military], [landuse=agriculture], [landuse=civilian], [landuse=military]]')

    def testFilters2(self):
        s = """
            Layer[landuse=military]     { polygon-fill: #000; }
            Layer[landuse=civilian]     { polygon-fill: #001; }
            Layer[landuse=agriculture]  { polygon-fill: #010; }
            Layer[horse=yes]    { polygon-fill: #011; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 8)
        self.assertEqual(str(sorted(filters)), '[[horse!=yes][landuse!=agriculture][landuse!=civilian][landuse!=military], [horse!=yes][landuse=agriculture], [horse!=yes][landuse=civilian], [horse!=yes][landuse=military], [horse=yes][landuse!=agriculture][landuse!=civilian][landuse!=military], [horse=yes][landuse=agriculture], [horse=yes][landuse=civilian], [horse=yes][landuse=military]]')

    def testFilters3(self):
        s = """
            Layer[landuse=military]     { polygon-fill: #000; }
            Layer[landuse=civilian]     { polygon-fill: #001; }
            Layer[landuse=agriculture]  { polygon-fill: #010; }
            Layer[horse=yes]    { polygon-fill: #011; }
            Layer[horse=no]     { polygon-fill: #100; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 12)
        self.assertEqual(str(sorted(filters)), '[[horse!=no][horse!=yes][landuse!=agriculture][landuse!=civilian][landuse!=military], [horse!=no][horse!=yes][landuse=agriculture], [horse!=no][horse!=yes][landuse=civilian], [horse!=no][horse!=yes][landuse=military], [horse=no][landuse!=agriculture][landuse!=civilian][landuse!=military], [horse=no][landuse=agriculture], [horse=no][landuse=civilian], [horse=no][landuse=military], [horse=yes][landuse!=agriculture][landuse!=civilian][landuse!=military], [horse=yes][landuse=agriculture], [horse=yes][landuse=civilian], [horse=yes][landuse=military]]')

    def testFilters4(self):
        s = """
            Layer[landuse=military]     { polygon-fill: #000; }
            Layer[landuse=civilian]     { polygon-fill: #001; }
            Layer[landuse=agriculture]  { polygon-fill: #010; }
            Layer[horse=yes]    { polygon-fill: #011; }
            Layer[leisure=park] { polygon-fill: #100; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 16)
        self.assertEqual(str(sorted(filters)), '[[horse!=yes][landuse!=agriculture][landuse!=civilian][landuse!=military][leisure!=park], [horse!=yes][landuse!=agriculture][landuse!=civilian][landuse!=military][leisure=park], [horse!=yes][landuse=agriculture][leisure!=park], [horse!=yes][landuse=agriculture][leisure=park], [horse!=yes][landuse=civilian][leisure!=park], [horse!=yes][landuse=civilian][leisure=park], [horse!=yes][landuse=military][leisure!=park], [horse!=yes][landuse=military][leisure=park], [horse=yes][landuse!=agriculture][landuse!=civilian][landuse!=military][leisure!=park], [horse=yes][landuse!=agriculture][landuse!=civilian][landuse!=military][leisure=park], [horse=yes][landuse=agriculture][leisure!=park], [horse=yes][landuse=agriculture][leisure=park], [horse=yes][landuse=civilian][leisure!=park], [horse=yes][landuse=civilian][leisure=park], [horse=yes][landuse=military][leisure!=park], [horse=yes][landuse=military][leisure=park]]')

class SimpleRangeTests(unittest.TestCase):

    def testRanges1(self):
        s = """
            Layer[foo<1000] { polygon-fill: #000; }
            Layer[foo>1000] { polygon-fill: #001; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 3)
        self.assertEqual(str(sorted(filters)), '[[foo<1000], [foo=1000], [foo>1000]]')

    def testRanges2(self):
        s = """
            Layer[foo>1] { polygon-fill: #000; }
            Layer[foo<2] { polygon-fill: #001; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 3)
        self.assertEqual(str(sorted(filters)), '[[foo<2][foo>1], [foo<=1], [foo>=2]]')

    def testRanges3(self):
        s = """
            Layer[foo>1] { polygon-fill: #000; }
            Layer[foo<2] { polygon-fill: #001; }
            Layer[bar>4] { polygon-fill: #010; }
            Layer[bar<8] { polygon-fill: #011; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 9)
        self.assertEqual(str(sorted(filters)), '[[bar<8][bar>4][foo<2][foo>1], [bar<8][bar>4][foo<=1], [bar<8][bar>4][foo>=2], [bar<=4][foo<2][foo>1], [bar<=4][foo<=1], [bar<=4][foo>=2], [bar>=8][foo<2][foo>1], [bar>=8][foo<=1], [bar>=8][foo>=2]]')

    def testRanges4(self):
        s = """
            Layer[foo>1] { polygon-fill: #000; }
            Layer[foo<2] { polygon-fill: #001; }
            Layer[bar=this] { polygon-fill: #010; }
            Layer[bar=that] { polygon-fill: #011; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 9)
        self.assertEqual(str(sorted(filters)), '[[bar!=that][bar!=this][foo<2][foo>1], [bar!=that][bar!=this][foo<=1], [bar!=that][bar!=this][foo>=2], [bar=that][foo<2][foo>1], [bar=that][foo<=1], [bar=that][foo>=2], [bar=this][foo<2][foo>1], [bar=this][foo<=1], [bar=this][foo>=2]]')

    def testRanges5(self):
        s = """
            Layer[foo>1] { polygon-fill: #000; }
            Layer[foo<2] { polygon-fill: #001; }
            Layer[bar=this] { polygon-fill: #010; }
            Layer[bar=that] { polygon-fill: #011; }
            Layer[bar=blah] { polygon-fill: #100; }
        """
        rulesets = stylesheet_rulesets(s)
        selectors = [dec.selector for dec in rulesets_declarations(rulesets)]
        filters = tests_filter_combinations(selectors_tests(selectors))
        
        self.assertEqual(len(filters), 12)
        self.assertEqual(str(sorted(filters)), '[[bar!=blah][bar!=that][bar!=this][foo<2][foo>1], [bar!=blah][bar!=that][bar!=this][foo<=1], [bar!=blah][bar!=that][bar!=this][foo>=2], [bar=blah][foo<2][foo>1], [bar=blah][foo<=1], [bar=blah][foo>=2], [bar=that][foo<2][foo>1], [bar=that][foo<=1], [bar=that][foo>=2], [bar=this][foo<2][foo>1], [bar=this][foo<=1], [bar=this][foo>=2]]')

class CompatibilityTests(unittest.TestCase):

    def testCompatibility1(self):
        a = SelectorAttributeTest('foo', '=', 1)
        b = SelectorAttributeTest('foo', '=', 1)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility2(self):
        a = SelectorAttributeTest('foo', '=', 1)
        b = SelectorAttributeTest('bar', '=', 1)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility3(self):
        a = SelectorAttributeTest('foo', '=', 1)
        b = SelectorAttributeTest('foo', '!=', 1)
        assert not a.isCompatible([b])
        assert not b.isCompatible([a])

    def testCompatibility4(self):
        a = SelectorAttributeTest('foo', '!=', 1)
        b = SelectorAttributeTest('bar', '=', 1)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility5(self):
        a = SelectorAttributeTest('foo', '!=', 1)
        b = SelectorAttributeTest('foo', '!=', 2)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility6(self):
        a = SelectorAttributeTest('foo', '!=', 1)
        b = SelectorAttributeTest('foo', '!=', 1)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility7(self):
        a = SelectorAttributeTest('foo', '=', 1)
        b = SelectorAttributeTest('foo', '<', 1)
        assert not a.isCompatible([b])
        assert not b.isCompatible([a])

    def testCompatibility8(self):
        a = SelectorAttributeTest('foo', '>=', 1)
        b = SelectorAttributeTest('foo', '=', 1)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility9(self):
        a = SelectorAttributeTest('foo', '=', 1)
        b = SelectorAttributeTest('foo', '<=', 1)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility10(self):
        a = SelectorAttributeTest('foo', '>', 1)
        b = SelectorAttributeTest('foo', '=', 1)
        assert not a.isCompatible([b])
        assert not b.isCompatible([a])

    def testCompatibility11(self):
        a = SelectorAttributeTest('foo', '>', 2)
        b = SelectorAttributeTest('foo', '<=', 1)
        assert not a.isCompatible([b])
        assert not b.isCompatible([a])

    def testCompatibility12(self):
        a = SelectorAttributeTest('foo', '<=', 1)
        b = SelectorAttributeTest('foo', '>', 2)
        assert not a.isCompatible([b])
        assert not b.isCompatible([a])

    def testCompatibility13(self):
        a = SelectorAttributeTest('foo', '<', 1)
        b = SelectorAttributeTest('foo', '>', 1)
        assert not a.isCompatible([b])
        assert not b.isCompatible([a])

    def testCompatibility14(self):
        a = SelectorAttributeTest('foo', '<', 2)
        b = SelectorAttributeTest('foo', '>', 1)
        assert a.isCompatible([b])
        assert b.isCompatible([a])

    def testCompatibility15(self):
        # Layer[scale-denominator>1000][bar>1]
        s = Selector(SelectorElement(['Layer'], [SelectorAttributeTest('scale-denominator', '>', 1000), SelectorAttributeTest('bar', '<', 3)]))
        
        # [bar>=3][baz=quux][foo>1][scale-denominator>1000]
        f = Filter(SelectorAttributeTest('scale-denominator', '>', 1000), SelectorAttributeTest('bar', '>=', 3), SelectorAttributeTest('foo', '>', 1), SelectorAttributeTest('baz', '=', 'quux'))
        
        assert not is_applicable_selector(s, f)

    def testCompatibility16(self):
        # Layer[scale-denominator<1000][foo=1]
        s = Selector(SelectorElement(['Layer'], [SelectorAttributeTest('scale-denominator', '<', 1000), SelectorAttributeTest('foo', '=', 1)]))
        
        # [baz!=quux][foo=1][scale-denominator>1000]
        f = Filter(SelectorAttributeTest('baz', '!=', 'quux'), SelectorAttributeTest('foo', '=', 1), SelectorAttributeTest('scale-denominator', '>', 1000))
        
        assert not is_applicable_selector(s, f)

class StyleRuleTests(unittest.TestCase):

    def testStyleRules1(self):
        s = """
            Layer[zoom<=10][use=park] { polygon-fill: #0f0; }
            Layer[zoom<=10][use=cemetery] { polygon-fill: #999; }
            Layer[zoom>10][use=park] { polygon-fill: #6f6; }
            Layer[zoom>10][use=cemetery] { polygon-fill: #ccc; }
        """

        declarations = stylesheet_declarations(s, is_gym=True)
        
        layer = xml.etree.ElementTree.Element('Layer')
        layer.append(xml.etree.ElementTree.Element('Datasource'))
    
        map = xml.etree.ElementTree.Element('Map')
        map.append(layer)
        
        add_polygon_style(map, layer, declarations)
        
        assert map.find('Layer/StyleName') is not None
        
        stylename = map.find('Layer/StyleName').text
        
        style_el = map.find('Style')
        
        assert style_el is not None
        assert style_el.get('name') == stylename
        
        rule_els = style_el.findall('Rule')
        
        assert rule_els[0].find('MaxScaleDenominator').text == '399999'
        assert rule_els[0].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[0].find('PolygonSymbolizer/CssParameter').text == '#cccccc'
        assert rule_els[0].find('Filter').text == "[use] = 'cemetery'"
        
        assert rule_els[1].find('MaxScaleDenominator').text == '399999'
        assert rule_els[1].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[1].find('PolygonSymbolizer/CssParameter').text == '#66ff66'
        assert rule_els[1].find('Filter').text == "[use] = 'park'"
    
        assert rule_els[2].find('MinScaleDenominator').text == '400000'
        assert rule_els[2].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[2].find('PolygonSymbolizer/CssParameter').text == '#999999'
        assert rule_els[2].find('Filter').text == "[use] = 'cemetery'"
        
        assert rule_els[3].find('MinScaleDenominator').text == '400000'
        assert rule_els[3].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[3].find('PolygonSymbolizer/CssParameter').text == '#00ff00'
        assert rule_els[3].find('Filter').text == "[use] = 'park'"

    def testStyleRules2(self):
        s = """
            Layer[zoom<=10][foo<1] { polygon-fill: #000; }
            Layer[zoom<=10][foo>1] { polygon-fill: #00f; }
            Layer[zoom>10][foo<1] { polygon-fill: #0f0; }
            Layer[zoom>10][foo>1] { polygon-fill: #f00; }
        """
    
        declarations = stylesheet_declarations(s, is_gym=True)
        
        layer = xml.etree.ElementTree.Element('Layer')
        layer.append(xml.etree.ElementTree.Element('Datasource'))
    
        map = xml.etree.ElementTree.Element('Map')
        map.append(layer)
        
        add_polygon_style(map, layer, declarations)
        
        assert map.find('Layer/StyleName') is not None
        
        stylename = map.find('Layer/StyleName').text
        
        style_el = map.find('Style')
        
        assert style_el is not None
        assert style_el.get('name') == stylename
        
        rule_els = style_el.findall('Rule')
        
        assert rule_els[0].find('MaxScaleDenominator').text == '399999'
        assert rule_els[0].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[0].find('PolygonSymbolizer/CssParameter').text == '#00ff00'
        assert rule_els[0].find('Filter').text == '[foo] < 1'
        
        assert rule_els[1].find('MinScaleDenominator').text == '400000'
        assert rule_els[1].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[1].find('PolygonSymbolizer/CssParameter').text == '#000000'
        assert rule_els[1].find('Filter').text == '[foo] < 1'
        
        assert rule_els[2].find('MaxScaleDenominator').text == '399999'
        assert rule_els[2].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[2].find('PolygonSymbolizer/CssParameter').text == '#ff0000'
        assert rule_els[2].find('Filter').text == '[foo] > 1'
    
        assert rule_els[3].find('MinScaleDenominator').text == '400000'
        assert rule_els[3].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert rule_els[3].find('PolygonSymbolizer/CssParameter').text == '#0000ff'
        assert rule_els[3].find('Filter').text == '[foo] > 1'

    def testStyleRules3(self):
        s = """
            Layer[zoom<=10][foo<1] { polygon-fill: #000; }
            Layer[zoom<=10][foo>1] { polygon-fill: #00f; }
            Layer[zoom>10][foo<1] { polygon-fill: #0f0; }
            Layer[zoom>10][foo>1] { polygon-fill: #f00; }
    
            Layer[zoom<=10] { line-width: 1; }
            Layer[zoom>10] { line-width: 2; }
            Layer[foo<1] { line-color: #0ff; }
            Layer[foo=1] { line-color: #f0f; }
            Layer[foo>1] { line-color: #ff0; }
        """
    
        declarations = stylesheet_declarations(s, is_gym=True)
        
        layer = xml.etree.ElementTree.Element('Layer')
        layer.append(xml.etree.ElementTree.Element('Datasource'))
    
        map = xml.etree.ElementTree.Element('Map')
        map.append(layer)
        
        add_polygon_style(map, layer, declarations)
        add_line_style(map, layer, declarations)

        assert len(map.findall('Layer/StyleName')) == 2
        
        stylenames = [stylename.text for stylename in map.findall('Layer/StyleName')]
        
        style_els = map.findall('Style')
        
        assert len(style_els) == 2
    
        assert style_els[0].get('name') in (stylenames)
        poly_rule_els = style_els[0].findall('Rule')
        
        assert poly_rule_els[0].find('MaxScaleDenominator').text == '399999'
        assert poly_rule_els[0].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert poly_rule_els[0].find('PolygonSymbolizer/CssParameter').text == '#00ff00'
        assert poly_rule_els[0].find('Filter').text == '[foo] < 1'
        
        assert poly_rule_els[1].find('MinScaleDenominator').text == '400000'
        assert poly_rule_els[1].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert poly_rule_els[1].find('PolygonSymbolizer/CssParameter').text == '#000000'
        assert poly_rule_els[1].find('Filter').text == '[foo] < 1'
        
        assert poly_rule_els[2].find('MaxScaleDenominator').text == '399999'
        assert poly_rule_els[2].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert poly_rule_els[2].find('PolygonSymbolizer/CssParameter').text == '#ff0000'
        assert poly_rule_els[2].find('Filter').text == '[foo] > 1'
    
        assert poly_rule_els[3].find('MinScaleDenominator').text == '400000'
        assert poly_rule_els[3].find('PolygonSymbolizer/CssParameter').get('name') == 'fill'
        assert poly_rule_els[3].find('PolygonSymbolizer/CssParameter').text == '#0000ff'
        assert poly_rule_els[3].find('Filter').text == '[foo] > 1'
    
        assert style_els[1].get('name') in (stylenames)
        line_rule_els = style_els[1].findall('Rule')
        
        assert line_rule_els[0].find('MaxScaleDenominator').text == '399999'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[0].text == '2.0'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[1].text == '#00ffff'
        assert line_rule_els[0].find('Filter').text == '[foo] < 1'
        
        assert line_rule_els[1].find('MinScaleDenominator').text == '400000'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[0].text == '1.0'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[1].text == '#00ffff'
        assert line_rule_els[1].find('Filter').text == '[foo] < 1'
        
        assert line_rule_els[2].find('MaxScaleDenominator').text == '399999'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[0].text == '2.0'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[1].text == '#ff00ff'
        assert line_rule_els[2].find('Filter').text == '[foo] = 1'
    
        assert line_rule_els[3].find('MinScaleDenominator').text == '400000'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[0].text == '1.0'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[1].text == '#ff00ff'
        assert line_rule_els[3].find('Filter').text == '[foo] = 1'
        
        assert line_rule_els[4].find('MaxScaleDenominator').text == '399999'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[0].text == '2.0'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[1].text == '#ffff00'
        assert line_rule_els[4].find('Filter').text == '[foo] > 1'
    
        assert line_rule_els[5].find('MinScaleDenominator').text == '400000'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[0].text == '1.0'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[1].text == '#ffff00'
        assert line_rule_els[5].find('Filter').text == '[foo] > 1'

    def testStyleRules4(self):
        s = """
            Layer[zoom<=10] { line-width: 1; }
            Layer[zoom>10] { line-width: 2; }
            Layer[foo<1] { line-color: #0ff; }
            Layer[foo=1] { line-color: #f0f; }
            Layer[foo>1] { line-color: #ff0; }
            
            Layer label { text-face-name: 'Helvetica'; text-size: 12; }
            Layer[foo<1] label { text-face-name: 'Arial'; }
            Layer[zoom<=10] label { text-size: 10; }
        """
    
        declarations = stylesheet_declarations(s, is_gym=True)
        
        layer = xml.etree.ElementTree.Element('Layer')
        layer.append(xml.etree.ElementTree.Element('Datasource'))
    
        map = xml.etree.ElementTree.Element('Map')
        map.append(layer)
        
        add_line_style(map, layer, declarations)
        add_text_styles(map, layer, declarations)
        
        assert len(map.findall('Layer/StyleName')) == 2
        
        stylenames = [stylename.text for stylename in map.findall('Layer/StyleName')]
        
        style_els = map.findall('Style')
        
        assert len(style_els) == 2
    
        assert style_els[0].get('name') in (stylenames)
        line_rule_els = style_els[0].findall('Rule')
        
        assert line_rule_els[0].find('MaxScaleDenominator').text == '399999'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[0].text == '2.0'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[0].findall('LineSymbolizer/CssParameter')[1].text == '#00ffff'
        assert line_rule_els[0].find('Filter').text == '[foo] < 1'
        
        assert line_rule_els[1].find('MinScaleDenominator').text == '400000'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[0].text == '1.0'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[1].findall('LineSymbolizer/CssParameter')[1].text == '#00ffff'
        assert line_rule_els[1].find('Filter').text == '[foo] < 1'
        
        assert line_rule_els[2].find('MaxScaleDenominator').text == '399999'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[0].text == '2.0'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[2].findall('LineSymbolizer/CssParameter')[1].text == '#ff00ff'
        assert line_rule_els[2].find('Filter').text == '[foo] = 1'
    
        assert line_rule_els[3].find('MinScaleDenominator').text == '400000'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[0].text == '1.0'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[3].findall('LineSymbolizer/CssParameter')[1].text == '#ff00ff'
        assert line_rule_els[3].find('Filter').text == '[foo] = 1'
        
        assert line_rule_els[4].find('MaxScaleDenominator').text == '399999'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[0].text == '2.0'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[4].findall('LineSymbolizer/CssParameter')[1].text == '#ffff00'
        assert line_rule_els[4].find('Filter').text == '[foo] > 1'
    
        assert line_rule_els[5].find('MinScaleDenominator').text == '400000'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[0].get('name') == 'stroke-width'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[0].text == '1.0'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[1].get('name') == 'stroke'
        assert line_rule_els[5].findall('LineSymbolizer/CssParameter')[1].text == '#ffff00'
        assert line_rule_els[5].find('Filter').text == '[foo] > 1'
        
        assert style_els[1].get('name') in (stylenames)
        text_rule_els = style_els[1].findall('Rule')
        
        assert text_rule_els[0].find('MaxScaleDenominator').text == '399999'
        assert text_rule_els[0].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[0].find('TextSymbolizer').get('face_name') == 'Arial'
        assert text_rule_els[0].find('TextSymbolizer').get('size') == '12'
        assert text_rule_els[0].find('Filter').text == '[foo] < 1'
        
        assert text_rule_els[1].find('MinScaleDenominator').text == '400000'
        assert text_rule_els[1].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[1].find('TextSymbolizer').get('face_name') == 'Arial'
        assert text_rule_els[1].find('TextSymbolizer').get('size') == '10'
        assert text_rule_els[1].find('Filter').text == '[foo] < 1'
        
        assert text_rule_els[2].find('MaxScaleDenominator').text == '399999'
        assert text_rule_els[2].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[2].find('TextSymbolizer').get('face_name') == 'Helvetica'
        assert text_rule_els[2].find('TextSymbolizer').get('size') == '12'
        assert text_rule_els[2].find('Filter').text == '[foo] >= 1'
    
        assert text_rule_els[3].find('MinScaleDenominator').text == '400000'
        assert text_rule_els[3].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[3].find('TextSymbolizer').get('face_name') == 'Helvetica'
        assert text_rule_els[3].find('TextSymbolizer').get('size') == '10'
        assert text_rule_els[3].find('Filter').text == '[foo] >= 1'

    def testStyleRules5(self):
        s = """
            Layer label { text-face-name: 'Helvetica'; text-size: 12; text-fill: #000; }
            Layer[foo<1] label { text-face-name: 'Arial'; }
            Layer[zoom<=10] label { text-size: 10; }
            
            Layer label { shield-face-name: 'Helvetica'; shield-size: 12; shield-file: url('purple-point.png'); }
            Layer[foo>1] label { shield-size: 10; }
            Layer[bar=baz] label { shield-size: 14; }
            Layer[bar=quux] label { shield-size: 16; }
        """
    
        declarations = stylesheet_declarations(s, is_gym=True)
        
        layer = xml.etree.ElementTree.Element('Layer')
        layer.append(xml.etree.ElementTree.Element('Datasource'))
    
        map = xml.etree.ElementTree.Element('Map')
        map.append(layer)
        
        add_text_styles(map, layer, declarations)
        add_shield_styles(map, layer, declarations)
        
        assert len(map.findall('Layer/StyleName')) == 2
        
        stylenames = [stylename.text for stylename in map.findall('Layer/StyleName')]
        
        style_els = map.findall('Style')
        
        assert len(style_els) == 2
    
        assert style_els[0].get('name') in (stylenames)
        text_rule_els = style_els[0].findall('Rule')
        
        assert text_rule_els[0].find('MaxScaleDenominator').text == '399999'
        assert text_rule_els[0].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[0].find('TextSymbolizer').get('face_name') == 'Arial'
        assert text_rule_els[0].find('TextSymbolizer').get('size') == '12'
        assert text_rule_els[0].find('Filter').text == '[foo] < 1'
        
        assert text_rule_els[1].find('MinScaleDenominator').text == '400000'
        assert text_rule_els[1].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[1].find('TextSymbolizer').get('face_name') == 'Arial'
        assert text_rule_els[1].find('TextSymbolizer').get('size') == '10'
        assert text_rule_els[1].find('Filter').text == '[foo] < 1'
        
        assert text_rule_els[2].find('MaxScaleDenominator').text == '399999'
        assert text_rule_els[2].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[2].find('TextSymbolizer').get('face_name') == 'Helvetica'
        assert text_rule_els[2].find('TextSymbolizer').get('size') == '12'
        assert text_rule_els[2].find('Filter').text == '[foo] >= 1'
    
        assert text_rule_els[3].find('MinScaleDenominator').text == '400000'
        assert text_rule_els[3].find('TextSymbolizer').get('name') == 'label'
        assert text_rule_els[3].find('TextSymbolizer').get('face_name') == 'Helvetica'
        assert text_rule_els[3].find('TextSymbolizer').get('size') == '10'
        assert text_rule_els[3].find('Filter').text == '[foo] >= 1'
    
        assert style_els[1].get('name') in (stylenames)
        shield_rule_els = style_els[1].findall('Rule')
        
        assert shield_rule_els[0].find('MinScaleDenominator') is None
        assert shield_rule_els[0].find('MaxScaleDenominator') is None
        assert shield_rule_els[0].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('size') == '12'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[0].find('Filter').text == "not [bar] = 'baz' and not [bar] = 'quux' and [foo] <= 1"
        
        assert shield_rule_els[1].find('MinScaleDenominator') is None
        assert shield_rule_els[1].find('MaxScaleDenominator') is None
        assert shield_rule_els[1].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('size') == '10'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[1].find('Filter').text == "not [bar] = 'baz' and not [bar] = 'quux' and [foo] > 1"
        
        assert shield_rule_els[2].find('MinScaleDenominator') is None
        assert shield_rule_els[2].find('MaxScaleDenominator') is None
        assert shield_rule_els[2].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('size') == '14'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[2].find('Filter').text == "[bar] = 'baz' and [foo] <= 1"
        
        assert shield_rule_els[3].find('MinScaleDenominator') is None
        assert shield_rule_els[3].find('MaxScaleDenominator') is None
        assert shield_rule_els[3].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('size') == '14'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[3].find('Filter').text == "[bar] = 'baz' and [foo] > 1"
        
        assert shield_rule_els[4].find('MinScaleDenominator') is None
        assert shield_rule_els[4].find('MaxScaleDenominator') is None
        assert shield_rule_els[4].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('size') == '16'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[4].find('Filter').text == "[bar] = 'quux' and [foo] <= 1"
        
        assert shield_rule_els[5].find('MinScaleDenominator') is None
        assert shield_rule_els[5].find('MaxScaleDenominator') is None
        assert shield_rule_els[5].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('size') == '16'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[5].find('Filter').text == "[bar] = 'quux' and [foo] > 1"

    def testStyleRules6(self):
        s = """
            Layer label { shield-face-name: 'Helvetica'; shield-size: 12; shield-file: url('purple-point.png'); }
            Layer[foo>1] label { shield-size: 10; }
            Layer[bar=baz] label { shield-size: 14; }
            Layer[bar=quux] label { shield-size: 16; }
    
            Layer { point-file: url('purple-point.png'); }
        """
    
        declarations = stylesheet_declarations(s, is_gym=True)
        
        layer = xml.etree.ElementTree.Element('Layer')
        layer.append(xml.etree.ElementTree.Element('Datasource'))
    
        map = xml.etree.ElementTree.Element('Map')
        map.append(layer)
        
        add_shield_styles(map, layer, declarations)
        add_point_style(map, layer, declarations)
        
        assert len(map.findall('Layer/StyleName')) == 2
        
        stylenames = [stylename.text for stylename in map.findall('Layer/StyleName')]
        
        style_els = map.findall('Style')
        
        assert len(style_els) == 2
    
        assert style_els[0].get('name') in (stylenames)
        shield_rule_els = style_els[0].findall('Rule')
        
        assert shield_rule_els[0].find('MinScaleDenominator') is None
        assert shield_rule_els[0].find('MaxScaleDenominator') is None
        assert shield_rule_els[0].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('size') == '12'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[0].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[0].find('Filter').text == "not [bar] = 'baz' and not [bar] = 'quux' and [foo] <= 1"
        
        assert shield_rule_els[1].find('MinScaleDenominator') is None
        assert shield_rule_els[1].find('MaxScaleDenominator') is None
        assert shield_rule_els[1].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('size') == '10'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[1].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[1].find('Filter').text == "not [bar] = 'baz' and not [bar] = 'quux' and [foo] > 1"
        
        assert shield_rule_els[2].find('MinScaleDenominator') is None
        assert shield_rule_els[2].find('MaxScaleDenominator') is None
        assert shield_rule_els[2].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('size') == '14'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[2].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[2].find('Filter').text == "[bar] = 'baz' and [foo] <= 1"
        
        assert shield_rule_els[3].find('MinScaleDenominator') is None
        assert shield_rule_els[3].find('MaxScaleDenominator') is None
        assert shield_rule_els[3].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('size') == '14'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[3].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[3].find('Filter').text == "[bar] = 'baz' and [foo] > 1"
        
        assert shield_rule_els[4].find('MinScaleDenominator') is None
        assert shield_rule_els[4].find('MaxScaleDenominator') is None
        assert shield_rule_els[4].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('size') == '16'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[4].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[4].find('Filter').text == "[bar] = 'quux' and [foo] <= 1"
        
        assert shield_rule_els[5].find('MinScaleDenominator') is None
        assert shield_rule_els[5].find('MaxScaleDenominator') is None
        assert shield_rule_els[5].find('ShieldSymbolizer').get('name') == 'label'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('face_name') == 'Helvetica'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('size') == '16'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('height') == '8'
        assert shield_rule_els[5].find('ShieldSymbolizer').get('width') == '8'
        assert shield_rule_els[5].find('Filter').text == "[bar] = 'quux' and [foo] > 1"
    
        assert style_els[1].get('name') in (stylenames)
        point_rule_els = style_els[1].findall('Rule')
        
        assert point_rule_els[0].find('Filter') is None
        assert point_rule_els[0].find('MinScaleDenominator') is None
        assert point_rule_els[0].find('MaxScaleDenominator') is None
        assert point_rule_els[0].find('PointSymbolizer').get('type') == 'png'
        assert point_rule_els[0].find('PointSymbolizer').get('height') == '8'
        assert point_rule_els[0].find('PointSymbolizer').get('width') == '8'

    def testStyleRules7(self):
        s = """
            Layer { point-file: url('purple-point.png'); }
            Layer { polygon-pattern-file: url('purple-point.png'); }
            Layer { line-pattern-file: url('purple-point.png'); }
        """
    
        declarations = stylesheet_declarations(s, is_gym=True)
        
        layer = xml.etree.ElementTree.Element('Layer')
        layer.append(xml.etree.ElementTree.Element('Datasource'))
    
        map = xml.etree.ElementTree.Element('Map')
        map.append(layer)
        
        add_point_style(map, layer, declarations)
        add_polygon_pattern_style(map, layer, declarations)
        add_line_pattern_style(map, layer, declarations)
        
        assert len(map.findall('Layer/StyleName')) == 3
        
        stylenames = [stylename.text for stylename in map.findall('Layer/StyleName')]
        
        style_els = map.findall('Style')
        
        assert len(style_els) == 3
    
        assert style_els[0].get('name') in (stylenames)
        point_rule_els = style_els[0].findall('Rule')
        
        assert point_rule_els[0].find('Filter') is None
        assert point_rule_els[0].find('MinScaleDenominator') is None
        assert point_rule_els[0].find('MaxScaleDenominator') is None
        assert point_rule_els[0].find('PointSymbolizer').get('type') == 'png'
        assert point_rule_els[0].find('PointSymbolizer').get('height') == '8'
        assert point_rule_els[0].find('PointSymbolizer').get('width') == '8'
    
        assert style_els[1].get('name') in (stylenames)
        point_rule_els = style_els[1].findall('Rule')
        
        assert point_rule_els[0].find('Filter') is None
        assert point_rule_els[0].find('MinScaleDenominator') is None
        assert point_rule_els[0].find('MaxScaleDenominator') is None
        assert point_rule_els[0].find('PolygonPatternSymbolizer').get('type') == 'png'
        assert point_rule_els[0].find('PolygonPatternSymbolizer').get('height') == '8'
        assert point_rule_els[0].find('PolygonPatternSymbolizer').get('width') == '8'
    
        assert style_els[2].get('name') in (stylenames)
        point_rule_els = style_els[2].findall('Rule')
        
        assert point_rule_els[0].find('Filter') is None
        assert point_rule_els[0].find('MinScaleDenominator') is None
        assert point_rule_els[0].find('MaxScaleDenominator') is None
        assert point_rule_els[0].find('LinePatternSymbolizer').get('type') == 'png'
        assert point_rule_els[0].find('LinePatternSymbolizer').get('height') == '8'
        assert point_rule_els[0].find('LinePatternSymbolizer').get('width') == '8'

if __name__ == '__main__':
    unittest.main()
