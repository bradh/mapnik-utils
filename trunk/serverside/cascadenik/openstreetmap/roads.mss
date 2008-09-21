/** Path Weights **/

.path[highway!=steps]
{
    line-cap: butt;
    line-join: round;
}

.path[highway=steps]
{
    line-cap: butt;
    line-join: miter;
}

.path.outline[highway!=steps][zoom>=16] { line-width: 4; }
.path.inline[highway!=steps][zoom>=16]
{
    line-width: 2;
    line-dasharray: 3, 3;
}

.path.outline[highway=steps][zoom>=16] { line-width: 7; }
.path.inline[highway=steps][zoom>=16]
{
    line-width: 5;
    line-dasharray: 2, 3;
}

.path.outline[highway!=steps][zoom>=14][zoom<=15] { line-width: 3; }
.path.inline[highway!=steps][zoom>=14][zoom<=15]
{
    line-width: 2;
    line-dasharray: 2, 2;
}

.path.outline[highway=steps][zoom>=14][zoom<=15] { line-width: 5; }
.path.inline[highway=steps][zoom>=14][zoom<=15]
{
    line-width: 3;
    line-dasharray: 1, 2;
}

/** Path Colors **/

.path.inline
{
    line-color: #000;
    line-opacity: 0.5;
}

.path.outline
{
    line-color: #fff;
    line-opacity: 0.2;
}



/** Roads **/

.road
{
    line-cap: round;
    line-join: miter;
    outline-cap: butt;
    outline-join: miter;
}

.road.outline[tunnel=yes],
.road.outline[tunnel=true]
{
    line-cap: butt;
    line-dasharray: 4,6;
}

/*
.road.major.inline[bridge=yes][zoom>=13],
.road.major.inline[bridge=true][zoom>=13]
{
    outline-width: 1;
    outline-color: #888;
}
*/

/** Road Weights **/

.motorway.inline[zoom>=7][zoom<=11] { line-width: 2; }
.motorway.outline[zoom>=7][zoom<=11] { line-width: 4; }

.road.inline[highway!=motorway][highway!=motorway_link][zoom>=7][zoom<=10] { line-width: 1; } /* general background fuzz */

.road.major.inline[highway=motorway][zoom>=7][zoom<=10] { line-width: 2; }
.road.major.inline[highway!=motorway_link][zoom>=11][zoom<=12] { line-width: 2; }
.road.major.outline[highway!=motorway_link][zoom>=11][zoom<=12] { line-width: 4; }

.road.minor.inline[zoom>=11][zoom<=12] { line-width: 1; }

.road.major.inline[zoom=13] { line-width: 5; }
.road.major.outline[zoom=13] { line-width: 7; }
.road.major.inline[highway=motorway_link][zoom=13] { line-width: 2; }
.road.major.outline[highway=motorway_link][zoom=13] { line-width: 4; }

.road.minor.inline[zoom=13] { line-width: 1; }

.road.major.inline[zoom=14] { line-width: 7; }
.road.major.outline[zoom=14] { line-width: 9; }
.road.major.inline[highway=motorway_link][zoom=14] { line-width: 2; }
.road.major.outline[highway=motorway_link][zoom=14] { line-width: 4; }

.road.minor.inline[zoom=14] { line-width: 2; }

.road.major.inline[zoom=15] { line-width: 11; }
.road.major.outline[zoom=15] { line-width: 13; }
.road.major.inline[highway=motorway_link][zoom=15] { line-width: 4; }
.road.major.outline[highway=motorway_link][zoom=15] { line-width: 6; }

.road.minor.inline[highway!=service][zoom=15] { line-width: 4; }
.road.minor.outline[highway!=service][zoom=15] { line-width: 6; }
.road.minor.inline[highway=service][zoom=15] { line-width: 2; }
.road.minor.outline[highway=service][zoom=15] { line-width: 4; }

.road.major.inline[zoom=16] { line-width: 13; }
.road.major.outline[zoom=16] { line-width: 15; }
.road.major.outline[highway=motorway][zoom=16] { line-width: 17; }
.road.major.inline[highway=motorway_link][zoom=16] { line-width: 8; }
.road.major.outline[highway=motorway_link][zoom=16] { line-width: 10; }

.road.minor.inline[highway!=service][zoom=16] { line-width: 8; }
.road.minor.outline[highway!=service][zoom=16] { line-width: 10; }
.road.minor.inline[highway=service][zoom=16] { line-width: 6; }
.road.minor.outline[highway=service][zoom=16] { line-width: 8; }

.road.inline[zoom>=17] { line-width: 15; }
.road.outline[zoom>=17] { line-width: 17; }
.road.outline[highway=motorway][zoom>=17] { line-width: 19; }
.road.inline[highway=motorway_link][zoom>=17] { line-width: 10; }
.road.outline[highway=motorway_link][zoom>=17] { line-width: 12; }



.road.label[oneway=1][highway!=motorway][zoom>=15],
.road.label[oneway=yes][highway!=motorway][zoom>=15],
.road.label[oneway=true][highway!=motorway][zoom>=15]
{
    line-pattern-file: url('img/oneway-arrow.png');
}

.motorway.inline[highway=motorway][zoom>=15]
{
    line-width: 1;
    line-color: #ff9460;
    line-dasharray: 12, 12;
}

.motorway.inline[highway=motorway][zoom=16]
{
    line-color: #ffad78;
}

.motorway.inline[highway=motorway][zoom>=17]
{
    line-color: #f9c38d;
}



/** Road Labels **/

.road.label.major[highway=trunk][zoom=12] name,
.road.label.major[highway=primary][zoom=12] name,
.road.label.major[highway=secondary][zoom=12] name,
.road.label.major[highway!=motorway][highway!=motorway_link][zoom>=13][zoom<=14] name,
.road.label.minor[highway=tertiary][zoom=13] name,
.road.label[highway!=motorway][highway!=motorway_link][zoom>=14] name
{
    text-face-name: "DejaVu Sans Book";
    text-size: 9;
    text-fill: #000;
    text-placement: line;
    text-halo-radius: 1;
    text-halo-fill: #fff;
    text-max-char-angle-delta: 20;
    text-min-distance: 50;
    text-spacing: 400;
}

.road.label.minor[zoom>=13][zoom<=14] name
{
    text-halo-fill: #dceee9 !important;
}

.road.label[highway!=motorway][highway!=motorway_link][zoom>=17] name 
{
    text-size: 12 !important;
}

.road.label.major[highway=motorway][zoom>=7] ref_content
{
    shield-face-name: "DejaVu Sans Bold";
    shield-min-distance: 100;
    shield-size: 9;
    shield-fill: #000;
}

.road.label.major[highway=motorway][zoom>=7][ref_length=2] ref_content { shield-file: url('img/horizontal-shield-2.png'); }
.road.label.major[highway=motorway][zoom>=7][ref_length=3] ref_content { shield-file: url('img/horizontal-shield-3.png'); }
.road.label.major[highway=motorway][zoom>=7][ref_length=4] ref_content { shield-file: url('img/horizontal-shield-4.png'); }
.road.label.major[highway=motorway][zoom>=7][ref_length=5] ref_content { shield-file: url('img/horizontal-shield-5.png'); }
.road.label.major[highway=motorway][zoom>=7][ref_length=6] ref_content { shield-file: url('img/horizontal-shield-6.png'); }
.road.label.major[highway=motorway][zoom>=7][ref_length=7] ref_content { shield-file: url('img/horizontal-shield-7.png'); }
.road.label.major[highway=motorway][zoom>=7][ref_length=8] ref_content { shield-file: url('img/horizontal-shield-8.png'); }
.road.label.major[highway=motorway][zoom>=7][ref_length=9] ref_content { shield-file: url('img/horizontal-shield-9.png'); }



/** Road Colors **/

.road.inline
{
    line-color: #f8f8f8;
    line-opacity: 1;
}

.road.outline
{
    line-color: #d2d2d2;
    line-opacity: 1;
}

.road.inline[highway=tertiary]
{
    line-color: #ffffff;
}

.road.outline[highway=tertiary]
{
    line-color: #c3c3c3;
}

.road.inline[highway=secondary]
{
    line-color: #fdffdd;
}

.road.outline[highway=secondary]
{
    line-color: #b5b880;
}

.road.inline[highway=trunk],
.road.inline[highway=primary]
{
    line-color: #ffec9f;
}

.road.outline[highway=trunk],
.road.outline[highway=primary]
{
    line-color: #b1a67b;
}

.road.inline[highway=motorway_link]
{
    line-color: #ff9460;
}

.road.outline[highway=motorway_link]
{
    line-color: #6d8aa7;
}

.motorway.inline,
.road.inline[highway=motorway]
{
    line-color: #ff5559;
}

.motorway.outline,
.road.outline[highway=motorway]
{
    line-color: #03317d;
}

/* lighten the motorways up a bit at higher zoom levels */
.road.inline[highway=motorway][zoom=16] { line-color: #ff7775; }
.road.inline[highway=motorway][zoom>=17] { line-color: #ff9d98; }
.road.outline[highway=motorway][zoom>=16] { line-color: #6c7dd5; }
.road.inline[highway=motorway_link][zoom=16] { line-color: #ffad78; }
.road.inline[highway=motorway_link][zoom>=17] { line-color: #f9c38d; }

.road.inline.minor[zoom>=12][zoom<=14]
{
    line-color: #5f6e6d;
    line-opacity: 0.37;
}

.road.inline.minor[zoom>=7][zoom<=11],
.road.inline.major[highway!=motorway][zoom>=7][zoom<=10]
{
    line-color: #b6cccb;
    line-opacity: 1;
}
