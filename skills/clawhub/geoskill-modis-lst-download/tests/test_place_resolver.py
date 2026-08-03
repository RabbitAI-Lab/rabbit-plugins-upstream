"""test_place_resolver.py — Unit tests for the place_resolver module."""

import sys
import unittest
from pathlib import Path

# Add scripts/ to path
SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from place_resolver import (  # noqa: E402
    HARDCODED_BBOXES,
    PRESETS,
    PlaceNotFoundError,
    format_bbox,
    get_preset,
    list_presets,
    resolve_place,
)


class TestHardcodedBboxes(unittest.TestCase):
    def test_china_bbox(self):
        bbox = resolve_place("中国")
        self.assertEqual(bbox, (73.0, 18.0, 135.0, 54.0))

    def test_china_alias(self):
        # '中国' and 'china' should give the same bbox
        b1 = resolve_place("中国")
        b2 = resolve_place("china")
        self.assertEqual(b1, b2)

    def test_beijing(self):
        bbox = resolve_place("北京")
        self.assertEqual(bbox, (115.7, 39.4, 116.8, 40.3))

    def test_yangtze(self):
        bbox = resolve_place("长江流域")
        self.assertAlmostEqual(bbox[0], 90.0, places=2)
        self.assertAlmostEqual(bbox[2], 122.0, places=2)

    def test_case_insensitive(self):
        b1 = resolve_place("China")
        b2 = resolve_place("china")
        self.assertEqual(b1, b2)

    def test_alias_resolution(self):
        # 北京市 -> 北京
        b1 = resolve_place("北京市")
        b2 = resolve_place("北京")
        self.assertEqual(b1, b2)

    def test_chaoyang_district(self):
        bbox = resolve_place("朝阳区")
        self.assertAlmostEqual(bbox[0], 116.35, places=2)
        self.assertAlmostEqual(bbox[2], 116.65, places=2)


class TestPlaceNotFound(unittest.TestCase):
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            resolve_place("")

    def test_unknown_offline_only(self):
        # Without Nominatim, the unknown name should raise
        with self.assertRaises(PlaceNotFoundError):
            resolve_place("马尔代夫某无人岛xyz", use_nominatim=False)

    def test_error_message_includes_query(self):
        try:
            resolve_place("不存在的地点xyz", use_nominatim=False)
        except PlaceNotFoundError as exc:
            self.assertIn("不存在的地点xyz", str(exc))


class TestPresets(unittest.TestCase):
    def test_list_presets_returns_text(self):
        text = list_presets()
        self.assertIn("city-uhi", text)
        self.assertIn("china-lst", text)

    def test_get_preset_returns_dict(self):
        p = get_preset("city-uhi")
        self.assertEqual(p["product"], "MOD11A2")
        self.assertIn("bbox", p)
        # bbox is a 4-tuple
        self.assertEqual(len(p["bbox"]), 4)

    def test_get_preset_unknown_raises(self):
        with self.assertRaises(ValueError):
            get_preset("does-not-exist")

    def test_presets_have_valid_bbox(self):
        for name, p in PRESETS.items():
            self.assertEqual(len(p["bbox"]), 4, f"preset {name}")
            w, s, e, n = p["bbox"]
            self.assertLess(w, e, f"preset {name} west >= east")
            self.assertLess(s, n, f"preset {name} south >= north")
            self.assertGreaterEqual(s, -90)
            self.assertLessEqual(n, 90)
            self.assertGreaterEqual(w, -180)
            self.assertLessEqual(e, 180)


class TestFormatBbox(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(format_bbox((1.0, 2.0, 3.0, 4.0)), "1.0 2.0 3.0 4.0")

    def test_negative(self):
        self.assertEqual(format_bbox((-122.5, 37.5, -122.0, 38.0)), "-122.5 37.5 -122.0 38.0")


class TestAllHardcodedBboxesValid(unittest.TestCase):
    """Smoke test: every entry in HARDCODED_BBOXES is a valid 4-tuple bbox."""

    def test_all_entries_valid(self):
        for key, bbox in HARDCODED_BBOXES.items():
            self.assertEqual(len(bbox), 4, f"key={key}")
            w, s, e, n = bbox
            self.assertLess(w, e, f"key={key}")
            self.assertLess(s, n, f"key={key}")
            self.assertGreaterEqual(s, -90)
            self.assertLessEqual(n, 90)
            self.assertGreaterEqual(w, -180)
            self.assertLessEqual(e, 180)


if __name__ == "__main__":
    unittest.main(verbosity=2)
