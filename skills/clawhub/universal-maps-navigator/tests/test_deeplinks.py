#!/usr/bin/env python3
"""Offline tests for universal-maps-navigator (no network, sandboxed HOME).

Run:  python3 tests/test_deeplinks.py      (or: bash scripts/selftest.sh)
"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import parse_qs, urlsplit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SCRIPTS = os.path.join(ROOT, "scripts")
sys.path.insert(0, SCRIPTS)

TMP = tempfile.mkdtemp(prefix="umn-test-")
os.environ.update({"HOME": TMP, "UMN_CONFIG_DIR": os.path.join(TMP, "cfg"), "UMN_CACHE_DIR": os.path.join(TMP, "cache"), "UMN_OFFLINE": "1"})

import deeplinks  # noqa: E402
import umn  # noqa: E402

EIFFEL = (48.858370, 2.294481, "Eiffel Tower")
LOUVRE = (48.860611, 2.337644, "Louvre")


def q(url):
    return {k: v[0] for k, v in parse_qs(urlsplit(url).query).items()}


class DeepLinks(unittest.TestCase):
    def test_all_seven_apps_present(self):
        links = deeplinks.navigate_links(EIFFEL)
        for app in ("google", "apple", "waze", "organic", "comaps", "here", "sygic", "osm", "geo", "android"):
            self.assertIn(app, links)
            self.assertTrue(links[app]["url"])

    def test_google_maps_urls_spec(self):
        u = deeplinks.navigate_links(EIFFEL, LOUVRE, [(48.8606, 2.3376)], "bike", ("google",), avoid=["tolls", "ferries"])["google"]
        p = q(u["url"])
        self.assertTrue(u["url"].startswith("https://www.google.com/maps/dir/?"))
        self.assertEqual(p["api"], "1")
        self.assertEqual(p["travelmode"], "bicycling")
        self.assertEqual(p["dir_action"], "navigate")
        self.assertEqual(p["destination"], "48.858370,2.294481")
        self.assertEqual(p["origin"], "48.860611,2.337644")
        self.assertEqual(p["avoid"], "tolls,ferries")
        self.assertIn("%7C", u["url"]) if "waypoints" in u["url"] and "|" in p.get("waypoints", "") else None
        self.assertEqual(u["android_intent"], "google.navigation:q=48.858370,2.294481&mode=b")
        self.assertTrue(u["ios_scheme"].startswith("comgooglemaps://?"))

    def test_apple_maplinks(self):
        u = deeplinks.navigate_links(EIFFEL, None, [], "transit", ("apple",))["apple"]
        p = q(u["url"])
        self.assertTrue(u["url"].startswith("https://maps.apple.com/?"))
        self.assertEqual(p["daddr"], "48.858370,2.294481")
        self.assertEqual(p["dirflg"], "r")
        self.assertNotIn("saddr", p)
        self.assertTrue(u["ios_scheme"].startswith("maps://?"))

    def test_waze(self):
        u = deeplinks.navigate_links(EIFFEL, None, [], "car", ("waze",))["waze"]
        p = q(u["url"])
        self.assertTrue(u["url"].startswith("https://waze.com/ul?"))
        self.assertEqual(p["ll"], "48.858370,2.294481")
        self.assertEqual(p["navigate"], "yes")
        self.assertTrue(u["app_scheme"].startswith("waze://?"))

    def test_organic_and_comaps(self):
        l = deeplinks.navigate_links(EIFFEL, LOUVRE, [(48.86, 2.33, "Via")], "foot", ("organic", "comaps"))
        o = q(l["organic"]["url"])
        self.assertTrue(l["organic"]["url"].startswith("https://omaps.app/route?"))
        self.assertEqual(o["type"], "pedestrian")
        self.assertEqual(o["dll"], "48.858370,2.294481")
        self.assertEqual(o["sll"], "48.860611,2.337644")
        self.assertTrue(l["organic"]["app_scheme"].startswith("om://route?"))
        v2 = l["organic"]["app_scheme_v2_nav"]
        self.assertTrue(v2.startswith("om://v2/nav?"))
        self.assertIn("mode=walk", v2)
        self.assertIn("waypoints=48.860000,2.330000", v2)
        self.assertTrue(l["comaps"]["url"].startswith("https://comaps.at/route?"))
        self.assertTrue(l["comaps"]["app_scheme"].startswith("cm://route?"))

    def test_here_share_route(self):
        u = deeplinks.navigate_links(EIFFEL, None, [(48.86, 2.33, "Stop 1")], "truck", ("here",), avoid=["highways"],
                                     truck={"height": 4.0, "weight": 40, "hazmat": ["flammable"]})["here"]
        self.assertTrue(u["url"].startswith("https://share.here.com/r/mylocation/48.860000,2.330000,Stop%201,p/48.858370,2.294481,Eiffel%20Tower?"))
        p = q(u["url"])
        self.assertEqual(p["m"], "tr")
        self.assertEqual(p["a"], "motorway")
        self.assertEqual(p["vdh"], "400")
        self.assertEqual(p["vw"], "40000")
        self.assertEqual(p["hmr"], "flammable")

    def test_sygic_lon_before_lat(self):
        u = deeplinks.navigate_links(EIFFEL, None, [(48.86, 2.33)], "foot", ("sygic",))["sygic"]
        self.assertEqual(u["url"], "com.sygic.aura://coordinate|2.330000|48.860000|2.294481|48.858370|walk")
        self.assertEqual(u["ios_url"], "com.sygic.aura://coordinate%7C2.330000%7C48.860000%7C2.294481%7C48.858370%7Cwalk")

    def test_place_and_search_links(self):
        pl = deeplinks.place_links(*EIFFEL)
        self.assertIn("layer=traffic", pl["google"]["traffic_url"])
        self.assertIn("map_action=pano", pl["google"]["streetview_url"])
        self.assertTrue(pl["here"]["url"].startswith("https://share.here.com/l/48.858370,2.294481,Eiffel%20Tower?"))
        self.assertTrue(pl["organic"]["app_scheme"].startswith("om://map?v=1&ll=48.858370,2.294481"))
        self.assertTrue(pl["geo"]["url"].startswith("geo:48.858370,2.294481"))
        sl = deeplinks.search_links("vegan restaurant", (48.85, 2.35))
        self.assertEqual(q(sl["google"]["url"])["query"], "vegan restaurant")
        self.assertEqual(q(sl["apple"]["url"])["sll"], "48.850000,2.350000")
        self.assertTrue(sl["organic"]["app_scheme"].startswith("om://search?"))

    def test_unknown_mode_rejected(self):
        with self.assertRaises(ValueError):
            deeplinks.navigate_links(EIFFEL, mode="teleport")

    def test_cli_json(self):
        out = subprocess.run([sys.executable, os.path.join(SCRIPTS, "deeplinks.py"), "navigate", "48.858370", "2.294481", "--name", "Eiffel", "--app", "waze,sygic"],
                             capture_output=True, text=True, check=True).stdout
        d = json.loads(out)
        self.assertEqual(set(d), {"waze", "sygic"})


class Helpers(unittest.TestCase):
    def test_plus_code_known_values(self):
        self.assertEqual(umn.plus_code(48.858370, 2.294481), "8FW4V75V+8Q")
        self.assertEqual(umn.plus_code(20.3700625, 2.7821875), "7FG49QCJ+2V")

    def test_polyline_decode(self):
        self.assertEqual(umn.decode_polyline("_p~iF~ps|U_ulLnnqC_mqNvxq`@", 5), [(38.5, -120.2), (40.7, -120.95), (43.252, -126.453)])

    def test_haversine_and_bearing(self):
        self.assertAlmostEqual(umn.haversine((0, 0), (0, 1)) / 1000, 111.19, places=1)
        self.assertEqual(umn.compass(umn.bearing((0, 0), (1, 0))), "N")

    def test_parse_place_coordinates_and_saved(self):
        p = umn.parse_place("44.4268, 26.1025")
        self.assertEqual((p["lat"], p["lon"], p["source"]), (44.4268, 26.1025, "coordinates"))
        umn.CFG["places"] = {"home": {"lat": 1.5, "lon": 2.5, "name": "Home"}}
        self.assertEqual(umn.parse_place("HOME")["source"], "saved")
        with self.assertRaises(umn.UmnError):  # geocoding requires network → UMN_OFFLINE makes it fail fast
            umn.parse_place("Somewhere far away")

    def test_config_roundtrip_sandboxed(self):
        umn.CFG["units"] = "imperial"
        umn.save_config(umn.CFG)
        self.assertTrue(umn.CONFIG_PATH.startswith(TMP))
        self.assertEqual(json.load(open(umn.CONFIG_PATH))["units"], "imperial")
        self.assertEqual(umn.fmt_dist(1609.344), "1.0 mi")
        umn.CFG.pop("units")
        self.assertEqual(umn.fmt_dist(1500), "1.5 km")
        self.assertEqual(umn.fmt_dur(3725), "1 h 02 min")

    def test_sample_line(self):
        line = [(0, i / 100) for i in range(101)]
        s = umn.sample_line(line, 5)
        self.assertEqual(len(s), 5)
        self.assertEqual(s[0], line[0]); self.assertEqual(s[-1], line[-1])

    def test_gpx_kml_writers(self):
        gpx = os.path.join(TMP, "r.gpx"); kml = os.path.join(TMP, "b.kml")
        umn.write_gpx(gpx, [(1, 2), (3, 4)], "t<est>", [{"lat": 1, "lon": 2, "name": "A&B"}])
        umn.write_kml(kml, [{"lat": 1, "lon": 2, "name": "A&B"}])
        self.assertIn("<trkpt lat=\"1.000000\" lon=\"2.000000\"/>", open(gpx).read())
        self.assertIn("A&amp;B", open(kml).read())

    def test_category_selectors(self):
        self.assertEqual(umn.category_selectors("fuel"), ['["amenity"="fuel"]'])
        self.assertEqual(umn.category_selectors("shop=bakery"), ['["shop"="bakery"]'])
        self.assertIsNone(umn.category_selectors("random words"))

    def test_human_maxspeed(self):
        self.assertEqual(umn.human_maxspeed("50"), "50 km/h")
        self.assertIn("urban", umn.human_maxspeed("RO:urban"))
        self.assertEqual(umn.human_maxspeed("30 mph"), "30 mph")

    def test_cli_help_and_offline_error(self):
        h = subprocess.run([sys.executable, os.path.join(SCRIPTS, "umn.py"), "--help"], capture_output=True, text=True)
        self.assertEqual(h.returncode, 0); self.assertIn("navigate", h.stdout)
        r = subprocess.run([sys.executable, os.path.join(SCRIPTS, "umn.py"), "geocode", "Berlin"], capture_output=True, text=True, env=os.environ)
        self.assertEqual(r.returncode, 3); self.assertIn("network disabled", r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=1)
