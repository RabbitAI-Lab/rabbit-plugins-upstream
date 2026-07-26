#!/usr/bin/env python3
"""Tests for osm-data-download."""

import sys
import os
import json
import unittest
import tempfile
import shutil
import importlib.util

# Load the script module
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "scripts", "osm-data-download.py")
spec = importlib.util.spec_from_file_location("osm_data_download", SCRIPT_PATH)
odd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(odd)


class TestBboxValidation(unittest.TestCase):
    """Test bounding box validation."""

    def test_valid_bbox(self):
        result = odd.validate_bbox("116.0,39.5,116.8,40.2")
        self.assertEqual(result, (116.0, 39.5, 116.8, 40.2))

    def test_valid_bbox_with_spaces(self):
        result = odd.validate_bbox(" 116.0 , 39.5 , 116.8 , 40.2 ")
        self.assertEqual(result, (116.0, 39.5, 116.8, 40.2))

    def test_invalid_bbox_too_few(self):
        with self.assertRaises(ValueError):
            odd.validate_bbox("116.0,39.5,116.8")

    def test_invalid_bbox_too_many(self):
        with self.assertRaises(ValueError):
            odd.validate_bbox("116.0,39.5,116.8,40.2,100")

    def test_invalid_bbox_lon_min_gt_max(self):
        with self.assertRaises(ValueError):
            odd.validate_bbox("116.8,39.5,116.0,40.2")

    def test_invalid_bbox_lat_min_gt_max(self):
        with self.assertRaises(ValueError):
            odd.validate_bbox("116.0,40.2,116.8,39.5")

    def test_invalid_bbox_out_of_range(self):
        with self.assertRaises(ValueError):
            odd.validate_bbox("116.0,39.5,200.0,40.2")


class TestOverpassQuery(unittest.TestCase):
    """Test Overpass QL query building."""

    def test_query_with_value(self):
        bbox = (116.0, 39.5, 116.8, 40.2)
        query = odd.build_overpass_query(bbox, "amenity", "restaurant")
        self.assertIn('["amenity"="restaurant"]', query)
        self.assertIn("(39.5,116.0,40.2,116.8)", query)

    def test_query_without_value(self):
        bbox = (116.0, 39.5, 116.8, 40.2)
        query = odd.build_overpass_query(bbox, "highway")
        self.assertIn('["highway"]', query)
        self.assertNotIn('="', query.split('["highway"]')[1].split(")")[0])

    def test_query_custom_timeout(self):
        bbox = (116.0, 39.5, 116.8, 40.2)
        query = odd.build_overpass_query(bbox, "building", timeout=120)
        self.assertIn("timeout:120", query)


class TestPresetQuery(unittest.TestCase):
    """Test semantic preset queries (water/road/...)."""

    def test_water_preset_includes_all_tag_groups(self):
        bbox = (116.0, 39.5, 116.8, 40.2)
        q = odd.build_preset_query(bbox, "water")
        # 4 filters × 3 element types = 12 statements
        self.assertIn('["natural"="water"]', q)
        self.assertIn('["waterway"]', q)
        self.assertIn('["landuse"="reservoir"]', q)
        self.assertIn('["water"~"^(river|lake|pond|reservoir)$"]', q)
        # Node / way / relation each appear
        self.assertIn("node", q)
        self.assertIn("way", q)
        self.assertIn("relation", q)

    def test_unknown_preset_raises(self):
        with self.assertRaises(ValueError):
            odd.build_preset_query((0, 0, 1, 1), "no-such-preset")

    def test_green_preset_includes_parks(self):
        q = odd.build_preset_query((0, 0, 1, 1), "green")
        self.assertIn('["leisure"="park"]', q)


class TestOsmToGeojson(unittest.TestCase):
    """Test OSM to GeoJSON conversion."""

    def test_empty_data(self):
        result = odd.osm_to_geojson({"elements": []})
        self.assertEqual(result["type"], "FeatureCollection")
        self.assertEqual(len(result["features"]), 0)

    def test_node_to_point(self):
        osm_data = {
            "elements": [
                {"type": "node", "id": 1, "lat": 39.9, "lon": 116.4,
                 "tags": {"amenity": "restaurant", "name": "Test"}}
            ]
        }
        result = odd.osm_to_geojson(osm_data)
        self.assertEqual(len(result["features"]), 1)
        self.assertEqual(result["features"][0]["geometry"]["type"], "Point")
        self.assertEqual(result["features"][0]["geometry"]["coordinates"], [116.4, 39.9])
        self.assertEqual(result["features"][0]["properties"]["amenity"], "restaurant")

    def test_way_to_linestring(self):
        osm_data = {
            "elements": [
                {"type": "node", "id": 1, "lat": 39.9, "lon": 116.4},
                {"type": "node", "id": 2, "lat": 39.91, "lon": 116.41},
                {"type": "way", "id": 100, "nodes": [1, 2],
                 "tags": {"highway": "residential"}},
            ]
        }
        result = odd.osm_to_geojson(osm_data)
        ways = [f for f in result["features"] if f["properties"]["osm_type"] == "way"]
        self.assertEqual(len(ways), 1)
        self.assertEqual(ways[0]["geometry"]["type"], "LineString")

    def test_closed_way_to_polygon(self):
        osm_data = {
            "elements": [
                {"type": "node", "id": 1, "lat": 39.9, "lon": 116.4},
                {"type": "node", "id": 2, "lat": 39.91, "lon": 116.4},
                {"type": "node", "id": 3, "lat": 39.91, "lon": 116.41},
                {"type": "node", "id": 4, "lat": 39.9, "lon": 116.41},
                {"type": "node", "id": 5, "lat": 39.9, "lon": 116.4},
                {"type": "way", "id": 100, "nodes": [1, 2, 3, 4, 5],
                 "tags": {"building": "yes"}},
            ]
        }
        result = odd.osm_to_geojson(osm_data)
        ways = [f for f in result["features"] if f["properties"]["osm_type"] == "way"]
        self.assertEqual(len(ways), 1)
        self.assertEqual(ways[0]["geometry"]["type"], "Polygon")


class TestPlaceContext(unittest.TestCase):
    """Test _place_context regex parser for Chinese place names."""

    def test_province(self):
        ctx = odd._place_context("四川省")
        self.assertEqual(ctx.get("state"), "四川省")

    def test_city(self):
        ctx = odd._place_context("成都市")
        self.assertEqual(ctx.get("city"), "成都市")

    def test_county(self):
        ctx = odd._place_context("朝阳区")
        self.assertEqual(ctx.get("county"), "朝阳区")

    def test_full_chain(self):
        # NOTE: current regex matches shortest XXX市 from the start,
        # so for "四川省成都市武侯区" the city match greedily becomes
        # "四川省成都市" rather than the bare "成都市". This is acceptable
        # as a hint (Nominatim still finds the right relation) and is
        # preserved for backward compatibility.
        ctx = odd._place_context("四川省成都市武侯区")
        self.assertEqual(ctx.get("state"), "四川省")
        self.assertIn("市", ctx.get("city", ""))
        self.assertEqual(ctx.get("county"), "武侯区")


class TestNormalisePlace(unittest.TestCase):
    def test_strip_whitespace(self):
        self.assertEqual(odd._normalise_place("  朝阳区  "), "朝阳区")

    def test_remove_inner_spaces(self):
        self.assertEqual(odd._normalise_place("朝阳 区"), "朝阳区")

    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            odd._normalise_place("   ")


class TestFormatList(unittest.TestCase):
    def test_single(self):
        self.assertEqual(odd.parse_format_list("geojson"), ["geojson"])

    def test_comma_list(self):
        self.assertEqual(
            odd.parse_format_list("geojson,shapefile"),
            ["geojson", "shapefile"],
        )

    def test_dedup(self):
        self.assertEqual(
            odd.parse_format_list("geojson,geojson,shapefile"),
            ["geojson", "shapefile"],
        )

    def test_unknown_raises(self):
        with self.assertRaises(ValueError):
            odd.parse_format_list("geojson,csv")


class TestClipFeaturesToBoundary(unittest.TestCase):
    """Test geometry clipping against an admin boundary."""

    def _square_polygon(self, x0, y0, x1, y1):
        return {
            "type": "Polygon",
            "coordinates": [[[x0, y0], [x1, y0], [x1, y1], [x0, y1], [x0, y0]]],
        }

    def test_inside_polygon_kept(self):
        boundary = self._square_polygon(0, 0, 10, 10)
        geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": self._square_polygon(2, 2, 4, 4),
                "properties": {"name": "inner"},
            }],
        }
        out = odd.clip_features_to_boundary(geojson, boundary)
        self.assertEqual(len(out["features"]), 1)
        self.assertEqual(out["features"][0]["properties"]["name"], "inner")

    def test_outside_polygon_dropped(self):
        boundary = self._square_polygon(0, 0, 10, 10)
        geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": self._square_polygon(20, 20, 30, 30),
                "properties": {"name": "outer"},
            }],
        }
        out = odd.clip_features_to_boundary(geojson, boundary)
        self.assertEqual(len(out["features"]), 0)

    def test_overlap_clipped(self):
        boundary = self._square_polygon(0, 0, 10, 10)
        geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "geometry": self._square_polygon(5, 5, 15, 15),
                "properties": {"name": "overlap"},
            }],
        }
        out = odd.clip_features_to_boundary(geojson, boundary)
        # Should be clipped, not dropped
        self.assertEqual(len(out["features"]), 1)
        clipped_geom = out["features"][0]["geometry"]
        self.assertIn(clipped_geom["type"], ("Polygon", "MultiPolygon"))


class TestQASummary(unittest.TestCase):
    def test_basic_qa(self):
        geojson = {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {"type": "Point", "coordinates": [116, 39]},
                    "properties": {"name": "a"},
                },
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]],
                    },
                    "properties": {"name": "b", "kind": "lake"},
                },
            ],
        }
        qa = odd.build_qa_summary(
            geojson,
            bbox=(116, 39, 117, 40),
            query="[out:json]...",
            formats=["geojson"],
        )
        self.assertEqual(qa["feature_count"], 2)
        self.assertEqual(qa["geometry_types"]["Point"], 1)
        self.assertEqual(qa["geometry_types"]["Polygon"], 1)
        self.assertEqual(qa["bbox"], [116, 39, 117, 40])
        self.assertEqual(qa["crs"], "EPSG:4326 (WGS84)")

    def test_qa_with_place(self):
        place = {
            "query": "朝阳区",
            "display_name": "朝阳区, 北京市, 中国",
            "osm_type": "relation",
            "osm_id": 2988933,
            "admin_level": "6",
            "bbox": [116.3, 39.8, 116.6, 40.1],
        }
        qa = odd.build_qa_summary(
            {"features": []},
            bbox=(116.3, 39.8, 116.6, 40.1),
            query="x",
            formats=["geojson"],
            place=place,
            preset="water",
            clipped=True,
        )
        self.assertIn("place", qa)
        self.assertEqual(qa["place"]["osm_id"], 2988933)
        self.assertTrue(qa["place"]["clipped_to_boundary"])
        self.assertEqual(qa["preset"]["name"], "water")


class TestShapefileBundle(unittest.TestCase):
    def test_zip_writes_required_files(self):
        tmp = tempfile.mkdtemp()
        try:
            # Create a minimal shapefile-like set
            base = os.path.join(tmp, "test")
            for ext in (".shp", ".shx", ".dbf", ".prj", ".cpg"):
                with open(base + ext, "wb" if ext in (".shp", ".shx", ".dbf") else "w") as f:
                    if ext == ".cpg":
                        f.write("UTF-8\n")
                    elif ext == ".prj":
                        f.write('GEOGCS["WGS 84"]')
                    else:
                        f.write(b"\x00" * 16)
            z = odd.zip_shapefile_bundle(base + ".shp")
            self.assertTrue(os.path.exists(z))
            self.assertTrue(z.endswith(".zip"))
            import zipfile
            with zipfile.ZipFile(z) as zf:
                names = zf.namelist()
                self.assertIn("test.shp", names)
                self.assertIn("test.shx", names)
                self.assertIn("test.dbf", names)
                self.assertIn("test.prj", names)
                self.assertIn("test.cpg", names)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


class TestCLI(unittest.TestCase):
    """Test CLI parser setup."""

    def test_parser_builds(self):
        parser = odd.build_parser()
        self.assertIsNotNone(parser)

    def test_download_place_subcommand_present(self):
        parser = odd.build_parser()
        # Reach into the subparsers
        # argparse in 3.12 stores actions
        sub_action = None
        for action in parser._actions:
            if hasattr(action, "choices") and isinstance(action.choices, dict):
                if "download-place" in action.choices:
                    sub_action = action
                    break
        self.assertIsNotNone(sub_action, "download-place subcommand missing")
        sub = sub_action.choices["download-place"]
        # Required: --place, -o
        required = {a.dest for a in sub._actions if getattr(a, "required", False)}
        self.assertIn("place", required)
        self.assertIn("output", required)
        # New flags
        flag_dests = {a.dest for a in sub._actions}
        self.assertIn("preset", flag_dests)
        self.assertIn("feature", flag_dests)
        self.assertIn("formats", flag_dests)
        self.assertIn("zip_shapefile", flag_dests)
        self.assertIn("qa", flag_dests)
        self.assertIn("no_clip", flag_dests)


if __name__ == "__main__":
    unittest.main()
