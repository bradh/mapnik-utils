@charset "UTF-8"; /* -*- mode: css; coding: utf-8 -*- */

/*

http://wiki.openstreetmap.org/index.php/Dresdner_Heide
http://commons.wikimedia.org/wiki/Category:Footpath_signs_in_Dresdner_Heide

*/


.route.hiking_heide_a_h empty,
.route.hiking_heide_k_n empty,
.route.hiking_heide_o_s empty,
.route.hiking_heide_t_z empty
{
    shield-fontset-name: "book-fonts";
    shield-size: 0;
    shield-fill: #777;
}

.route.hiking_heide_a_h[zoom>=12],
.route.hiking_heide_k_n[zoom>=12],
.route.hiking_heide_o_s[zoom>=12],
.route.hiking_heide_t_z[zoom>=12]
{
    shield-min-distance: 2;
    shield-spacing: 22;
}
.route.hiking_heide_a_h[zoom>=14],
.route.hiking_heide_k_n[zoom>=14],
.route.hiking_heide_o_s[zoom>=14],
.route.hiking_heide_t_z[zoom>=14]
{
    shield-min-distance: 5;
    shield-spacing: 55;
}
.route.hiking_heide_a_h[zoom>=15],
.route.hiking_heide_k_n[zoom>=15],
.route.hiking_heide_o_s[zoom>=15],
.route.hiking_heide_t_z[zoom>=15]
{
    shield-min-distance: 8;
    shield-spacing: 88;
}

/*

missing:

Alter Kannenhenkel
Bluempenweg
Fensterchen
Kreuz 4

*/


.route.hiking_heide_a_h[route_name="Dresdner Heide, Anker"][zoom>=14]                     { shield-file: url('img/symbols/dresdner_heide/anker1.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Bischofsweg"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/bischofsweg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Brille"][zoom>=14]                    { shield-file: url('img/symbols/dresdner_heide/brille.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Diebsteig"][zoom>=14]                 { shield-file: url('img/symbols/dresdner_heide/diebsteig.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Doppel-E"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/doppel-e.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Flügelweg"][zoom>=14]                 { shield-file: url('img/symbols/dresdner_heide/fluegelweg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Gabel"][zoom>=14]                     { shield-file: url('img/symbols/dresdner_heide/gabel.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Gänsefuß"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/gaensefuss.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, HG-Weg"][zoom>=14]                    { shield-file: url('img/symbols/dresdner_heide/hg-weg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hakenweg"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/hakenweg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hirschstängel"][zoom>=14]             { shield-file: url('img/symbols/dresdner_heide/hirschstaengel.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hämmerchen"][zoom>=14]                { shield-file: url('img/symbols/dresdner_heide/haemmerchen.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hütchen"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/huetchen.16.png'); }

.route.hiking_heide_k_n[route_name="Dresdner Heide, Kannenhenkel"][zoom>=14]              { shield-file: url('img/symbols/dresdner_heide/kannenhenkel.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz 5"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/kreuz_5.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz 6"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/kreuz_6.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz 7"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/kreuz_7.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz R"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Kreuz-R.10.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Krumme Neun"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/krumme_9.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Krumme 9"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/krumme_9.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kuhschwanz"][zoom>=14]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Kuhschwanz.10.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Mehlflußweg"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/mehlflussweg.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Mittelweg"][zoom>=14]                 { shield-file: url('img/symbols/dresdner_heide/mittelweg.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Mühlweg"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/muehlweg.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Nachtflügel"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Nachtfluegel.10.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Neuer Flügel"][zoom>=14]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Neuer_Fluegel.10.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Neuer Weg"][zoom>=14]                 { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Neuer_Weg.10.png'); }

.route.hiking_heide_o_s[route_name="Dresdner Heide, Oberringel"][zoom>=14]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Oberringel.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Ochsenkopf"][zoom>=14]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Ochsenkopf.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Ochsensteig"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Ochsensteig.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Pillnitz-Moritzburger-Weg"][zoom>=14] { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Pillnitz-Moritzburger_Weg.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Reichsapfel"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Reichsapfel.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Rennsteig"][zoom>=14]                 { shield-file: url('img/symbols/dresdner_heide/rennsteig.16.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Runde 4"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Runde_Vier.10.png'); }
/*Wegzeichen_Dresdner_Heide_Schwarzer_Bildweg*/
.route.hiking_heide_o_s[route_name="Dresdner Heide, Sandbrückenweg"][zoom>=14]            { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Sandbrueckenweg.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Saugartenweg"][zoom>=14]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Saugartenweg.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Schere"][zoom>=14]                    { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Schere.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Schwerterweg"][zoom>=14]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Schwerterweg.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Schwesternsteig"][zoom>=14]           { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Schwestersteig.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Semmelweg"][zoom>=14]                 { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Saugartenweg_Semmelweg.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Stallweg"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Stallweg.10.png'); }
/*Wegzeichen_Dresdner_Heide_Stallweg2*/
.route.hiking_heide_o_s[route_name="Dresdner Heide, Steingründchenweg"][zoom>=14]         { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Steingruendchenweg.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Steinweg"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Steinweg.10.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Stuhlweg"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Stuhlweg.10.png'); }

.route.hiking_heide_t_z[route_name="Dresdner Heide, Todweg"][zoom>=14]                    { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_O-_oder_Todweg.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Topfweg"][zoom>=14]                   { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Topfweg.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Traubelweg"][zoom>=14]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Traubelweg.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Türmchen"][zoom>=14]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Tuermchen.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Unterringel"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Unterringel.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Verkehrte Gabel"][zoom>=14]           { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Verkehrte_Gabel.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Verkehrter Anker"][zoom>=14]          { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Verkehrter_Anker.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Vogelzipfel"][zoom>=14]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Vogelzipfel.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Weißiger Gänsefuß"][zoom>=14]         { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Weissiger_Gaensefuss.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Weißiger Weg"][zoom>=14]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Weissiger_Weg.10.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Wiesenweg"][zoom>=14]                 { shield-file: url('img/symbols/dresdner_heide/wiesenweg.16.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Zirkel"][zoom>=14]                    { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Zirkel.10.png'); }

/* -------------------------------------------------- */

.route.hiking_heide_a_h[route_name="Dresdner Heide, Anker"][zoom>=15]                     { shield-file: url('img/symbols/dresdner_heide/anker1.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Bischofsweg"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/bischofsweg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Brille"][zoom>=15]                    { shield-file: url('img/symbols/dresdner_heide/brille.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Diebsteig"][zoom>=15]                 { shield-file: url('img/symbols/dresdner_heide/diebsteig.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Doppel-E"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/doppel-e.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Flügelweg"][zoom>=15]                 { shield-file: url('img/symbols/dresdner_heide/fluegelweg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Gabel"][zoom>=15]                     { shield-file: url('img/symbols/dresdner_heide/gabel.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Gänsefuß"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/gaensefuss.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, HG-Weg"][zoom>=15]                    { shield-file: url('img/symbols/dresdner_heide/hg-weg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hakenweg"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/hakenweg.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hirschstängel"][zoom>=15]             { shield-file: url('img/symbols/dresdner_heide/hirschstaengel.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hämmerchen"][zoom>=15]                { shield-file: url('img/symbols/dresdner_heide/haemmerchen.16.png'); }
.route.hiking_heide_a_h[route_name="Dresdner Heide, Hütchen"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/huetchen.16.png'); }

.route.hiking_heide_k_n[route_name="Dresdner Heide, Kannenhenkel"][zoom>=15]              { shield-file: url('img/symbols/dresdner_heide/kannenhenkel.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz 5"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/kreuz_5.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz 6"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/kreuz_6.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz 7"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/kreuz_7.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kreuz R"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Kreuz-R.12.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Krumme Neun"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/krumme_9.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Krumme 9"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/krumme_9.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Kuhschwanz"][zoom>=15]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Kuhschwanz.12.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Mehlflußweg"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/mehlflussweg.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Mittelweg"][zoom>=15]                 { shield-file: url('img/symbols/dresdner_heide/mittelweg.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Mühlweg"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/muehlweg.16.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Nachtflügel"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Nachtfluegel.12.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Neuer Flügel"][zoom>=15]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Neuer_Fluegel.12.png'); }
.route.hiking_heide_k_n[route_name="Dresdner Heide, Neuer Weg"][zoom>=15]                 { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Neuer_Weg.12.png'); }

.route.hiking_heide_o_s[route_name="Dresdner Heide, Oberringel"][zoom>=15]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Oberringel.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Ochsenkopf"][zoom>=15]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Ochsenkopf.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Ochsensteig"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Ochsensteig.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Pillnitz-Moritzburger-Weg"][zoom>=15] { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Pillnitz-Moritzburger_Weg.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Reichsapfel"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Reichsapfel.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Rennsteig"][zoom>=15]                 { shield-file: url('img/symbols/dresdner_heide/rennsteig.16.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Runde 4"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Runde_Vier.12.png'); }
/*Wegzeichen_Dresdner_Heide_Schwarzer_Bildweg*/
.route.hiking_heide_o_s[route_name="Dresdner Heide, Sandbrückenweg"][zoom>=15]            { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Sandbrueckenweg.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Saugartenweg"][zoom>=15]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Saugartenweg.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Schere"][zoom>=15]                    { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Schere.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Schwerterweg"][zoom>=15]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Schwerterweg.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Schwesternsteig"][zoom>=15]           { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Schwestersteig.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Semmelweg"][zoom>=15]                 { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Saugartenweg_Semmelweg.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Stallweg"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Stallweg.12.png'); }
/*Wegzeichen_Dresdner_Heide_Stallweg2*/
.route.hiking_heide_o_s[route_name="Dresdner Heide, Steingründchenweg"][zoom>=15]         { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Steingruendchenweg.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Steinweg"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Steinweg.12.png'); }
.route.hiking_heide_o_s[route_name="Dresdner Heide, Stuhlweg"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Stuhlweg.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Todweg"][zoom>=15]                    { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_O-_oder_Todweg.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Topfweg"][zoom>=15]                   { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Topfweg.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Traubelweg"][zoom>=15]                { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Traubelweg.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Türmchen"][zoom>=15]                  { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Tuermchen.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Unterringel"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Unterringel.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Verkehrte Gabel"][zoom>=15]           { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Verkehrte_Gabel.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Verkehrter Anker"][zoom>=15]          { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Verkehrter_Anker.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Vogelzipfel"][zoom>=15]               { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Vogelzipfel.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Weißiger Gänsefuß"][zoom>=15]         { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Weissiger_Gaensefuss.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Weißiger Weg"][zoom>=15]              { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Weissiger_Weg.12.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Wiesenweg"][zoom>=15]                 { shield-file: url('img/symbols/dresdner_heide/wiesenweg.16.png'); }
.route.hiking_heide_t_z[route_name="Dresdner Heide, Zirkel"][zoom>=15]                    { shield-file: url('img/symbols/dresdner_heide/Wegzeichen_Dresdner_Heide_Zirkel.12.png'); }
