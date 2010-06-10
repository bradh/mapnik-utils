/* -*- mode: css -*- */


/* catch-all - FIXME: remove this at some point */
/*
.poi.point[zoom>=13]
{
    point-file: url('sjjb-mapicons/png/poi_point_of_interest.glow.12.png');
    text-dy: 14;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 500;
    text-halo-fill: #ff3333;
    text-halo-radius: 1;
}
*/

/* ---------------------------------------------------------------------- */

.poi_natural.point[natural=tree][zoom>=14] name
{
    point-file: url('img/mapnik-symbols/tree.png');
    text-fill: #239c45;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_tourism.point[tourism=viewpoint][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/tourist_view_point.glow.8.png');
    text-fill: #734a08;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_tourism.point[tourism=viewpoint][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/tourist_view_point.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_tourism.point[man_made=tower][zoom>=13] name
{
    point-file: url('img/svg-twotone-png/tourist_tower.p.10.png');
/*    point-file: url('sjjb-mapicons/png/tourist_tower.glow.10.png'); */
    text-fill: #734a08;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;

}

.poi_tourism.point[man_made=tower][zoom>=15] name
{
    point-file: url('img/svg-twotone-png/tourist_tower.p.14.png');
/*    point-file: url('sjjb-mapicons/png/tourist_tower.glow.14.png');*/
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_historic.point[historic=ruins][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/tourist_ruin.glow.10.png');
    text-fill: #734a08;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;

}

.poi_historic.point[historic=ruins][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/tourist_ruin.glow.14.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_historic.point[historic=castle][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/tourist_castle.glow.8.png');
    text-fill: #734a08;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_historic.point[historic=castle][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/tourist_castle.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_tourism.point[tourism=information][information=guidepost][zoom>=15] name
{
    point-file: url('img/svg-twotone-png/tourist_guidepost.p.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_tourism.point[tourism=information][information!=guidepost][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/amenity_information.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_tourism.point[tourism=information][information!=guidepost][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/amenity_information.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_tourism.point[tourism=attraction][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/poi_point_of_interest.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_tourism.point[tourism=attraction][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/poi_point_of_interest.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=bench][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/amenity_bench.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=toilets][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/amenity_toilets.glow.8.png');
    text-fill: #734a08;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=toilets][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/amenity_toilets.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=shelter][zoom>=12] name
{
    point-file: url('sjjb-mapicons/png/accommodation_shelter.glow.8.png');
    text-fill: #0092da;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=shelter][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/accommodation_shelter.glow.12.png');
    text-fill: #0092da;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=shelter][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/accommodation_shelter.glow.16.png');
    text-fill: #0092da;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_tourism.point[tourism=picnic_site][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/tourist_picnic.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_tourism.point[tourism=picnic_site][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/tourist_picnic.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=telephone][zoom>=14] name
{
    point-file: url('sjjb-mapicons/png/amenity_telephone.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=telephone][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/amenity_telephone.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

/*
.poi.point[amenity=rescue_box][zoom>=14] name
{
    point-file: url('sjjb-mapicons/png/health_hospital_emergency.glow.10.png');
    text-fill: #da0092;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 500;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}
*/
.poi.point[amenity=rescue_box][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/health_hospital_emergency.glow.12.png');
    text-fill: #da0092;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=restaurant][zoom>=14] name
{
    point-file: url('sjjb-mapicons/png/food_restaurant.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=restaurant][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/food_restaurant.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=fast_food][zoom>=14] name
{
    point-file: url('sjjb-mapicons/png/food_fastfood.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=fast_food][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/food_fastfood.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=pub][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/food_pub.glow.8.png');
    text-fill: #734a08;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=pub][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/food_pub.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=drinking_water][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/food_drinkingtap.glow.12.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=drinking_water][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/food_drinkingtap.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=parking][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/transport_parking.glow.8.png');
    text-fill: #0092da;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 50;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=parking][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/transport_parking.glow.12.png');
    text-fill: #0092da;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 50;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=parking][zoom>=13][fee=yes] name
{
    point-file: url('sjjb-mapicons/png/transport_parking_car_paid.glow.8.png');
    text-fill: #0092da;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 50;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=parking][zoom>=15][fee=yes] name
{
    point-file: url('sjjb-mapicons/png/transport_parking_car_paid.glow.12.png');
    text-fill: #0092da;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 50;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[amenity=place_of_worship][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/place_of_worship.glow.8.png');
    text-fill: #0092da;
    text-dy: 9;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 50;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi.point[amenity=place_of_worship][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/place_of_worship.glow.12.png');
    text-fill: #0092da;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 50;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

/* .poi.label[zoom>=17][amenity=police], */
/* .poi.label[zoom>=17][amenity=police] */
/* { */
/*     point-file: url('img/icons/24x24/symbol/emergency/amenity=police.png'); */
/*     text-dy: 20; */

/* } */

/* TODO: parking, gate, cave, halt, survey_point, pow */

.poi_natural.point[natural=cave_entrance][zoom>=13] name
{
    point-file: url('img/svg-twotone-png/tourist_cave.p.8.png');
/*    point-file: url('sjjb-mapicons/png/poi_cave.glow.8.png');*/
    text-fill: #734a08;
    text-dy: 10;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_natural.point[natural=cave_entrance][zoom>=15] name
{
    point-file: url('img/svg-twotone-png/tourist_cave.p.12.png');
/*    point-file: url('sjjb-mapicons/png/poi_cave.glow.12.png');*/
    text-fill: #734a08;
    text-dy: 14;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_natural.point[natural=cave_entrance][zoom>=16]
{
    point-allow-overlap: true;
}

.poi_tourism.point[tourism=summit_cross][zoom>=13] name,
.poi_historic.point[historic=wayside_cross][zoom>=14] name
{
/*    point-file: url('sjjb-mapicons/png/tourist_cross.glow.12.png'); */
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_tourism.point[tourism=summit_cross][zoom>=15] name,
.poi_historic.point[historic=wayside_cross][zoom>=16] name
{
/*    point-file: url('sjjb-mapicons/png/tourist_cross.glow.16.png'); */
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_tourism.point[tourism=camp_site][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/accommodation_camping.glow.14.png');
    text-fill: #0092da;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_tourism.point[tourism=camp_site][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/accommodation_camping.glow.16.png');
    text-fill: #0092da;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi_boundary.point[boundary=marker][zoom>=16] ref
{
    text-fill: #cf9700;
    text-fontset-name: "oblique-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}


.poi_shop.point[shop=bicycle][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/shopping_bicycle.glow.14.png');
    text-fill: #ac39ac;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

.poi_shop.point[shop=bicycle][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/shopping_bicycle.glow.16.png');
    text-fill: #ac39ac;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}


/*.poi_historic.point[historic=ruins][ruins=bunker][zoom>=13] name,*/
.poi.point[military=bunker][zoom>=13] name
{
    point-file: url('img/svg-twotone-png/military_bunker.p.14.png');
/*    point-file: url('sjjb-mapicons/png/poi_military_bunker.glow.14.png');*/
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}

/*.poi_historic.point[historic=ruins][ruins=bunker][zoom>=15] name,*/
.poi.point[military=bunker][zoom>=15] name
{
    point-file: url('img/svg-twotone-png/military_bunker.p.16.png');
/*    point-file: url('sjjb-mapicons/png/poi_military_bunker.glow.16.png');*/
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}


.poi.point[amenity=hunting_stand][zoom>=13]
{
    point-file: url('img/svg-twotone-png/poi_hunting_stand.p.14.png');
/*    point-file: url('sjjb-mapicons/png/poi_hunting_stand.glow.14.png');*/
}
.poi.point[amenity=hunting_stand][zoom>=15]
{
    point-file: url('img/svg-twotone-png/poi_hunting_stand.p.16.png');
/*    point-file: url('sjjb-mapicons/png/poi_hunting_stand.glow.16.png');*/
    point-allow-overlap: true;
}

.poi.point[man_made=mast][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/poi_tower_communications.glow.14.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}
.poi.point[man_made=mast][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/poi_tower_communications.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}

.poi.point[man_made=mineshaft][zoom>=13] name
{
    point-file: url('sjjb-mapicons/png/poi_mine.glow.14.png');
    text-fill: #734a08;
    text-dy: 13;
    text-fontset-name: "book-fonts";
    text-size: 8;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
}
.poi.point[man_made=mineshaft][zoom>=15] name
{
    point-file: url('sjjb-mapicons/png/poi_mine.glow.16.png');
    text-fill: #734a08;
    text-dy: 17;
    text-fontset-name: "book-fonts";
    text-size: 10;
    text-placement: point;
    text-wrap-width: 77;
    text-halo-fill: #fbfbfb;
    text-halo-radius: 1;
    point-allow-overlap: true;
}
