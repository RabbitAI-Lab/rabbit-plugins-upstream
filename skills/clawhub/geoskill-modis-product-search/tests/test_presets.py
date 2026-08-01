"""test_presets.py — Tests for the new preset / task commands in modis-product-search."""

import json
import sys
import unittest
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = SKILL_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import modis_products  # noqa: E402


class TestTaskPresets(unittest.TestCase):
    def test_lst_uhi(self):
        p = modis_products.TASK_PRESETS["lst-uhi"]
        self.assertIn("MOD11A2", p["products"])
        self.assertEqual(p["category"], "land_surface_temperature")

    def test_ndvi_250m(self):
        p = modis_products.TASK_PRESETS["ndvi-250m"]
        self.assertEqual(p["products"], ["MOD13Q1"])

    def test_all_presets_have_products_and_category(self):
        for name, p in modis_products.TASK_PRESETS.items():
            self.assertIn("products", p, name)
            self.assertIn("category", p, name)
            self.assertGreater(len(p["products"]), 0, name)
            self.assertIn(p["category"], modis_products.CATEGORY_MAP, name)

    def test_all_referenced_products_exist(self):
        for name, p in modis_products.TASK_PRESETS.items():
            for pid in p["products"]:
                prod = modis_products.get_product_by_id(pid, modis_products.load_data()[0])
                self.assertIsNotNone(prod, f"{name}: missing {pid}")


class TestTaskKeywords(unittest.TestCase):
    def test_known_tasks(self):
        for kw in ["fire", "ndvi", "lst", "uhi", "snow", "vegetation"]:
            self.assertIn(kw, modis_products.TASK_KEYWORDS, kw)

    def test_chinese_tasks(self):
        for kw in ["火灾", "热岛", "积雪", "土地覆盖", "反射率", "反照率"]:
            self.assertIn(kw, modis_products.TASK_KEYWORDS, kw)


class TestPresetCommand(unittest.TestCase):
    def test_preset_list(self):
        result = modis_products.main(["preset", "list"])
        self.assertIn("presets", result)
        self.assertIn("lst-uhi", result["presets"])

    def test_preset_lst_uhi(self):
        result = modis_products.main(["preset", "lst-uhi"])
        self.assertEqual(result["preset"], "lst-uhi")
        self.assertIn("MOD11A2", result["products"])

    def test_preset_unknown(self):
        result = modis_products.main(["preset", "unknown-preset"])
        self.assertIn("error", result)
        self.assertIn("available", result)

    def test_preset_no_args(self):
        result = modis_products.main(["preset"])
        self.assertIn("error", result)


class TestTaskCommand(unittest.TestCase):
    def test_task_fire(self):
        result = modis_products.main(["task", "fire"])
        self.assertEqual(result["category"], "thermal_anomalies")
        self.assertIn("MOD14A1", result["products"])

    def test_task_chinese(self):
        result = modis_products.main(["task", "火灾"])
        self.assertEqual(result["category"], "thermal_anomalies")

    def test_task_ndvi(self):
        result = modis_products.main(["task", "ndvi"])
        self.assertEqual(result["category"], "vegetation_indices")
        self.assertIn("MOD13Q1", result["products"])

    def test_task_unknown(self):
        result = modis_products.main(["task", "不存在的任务"])
        self.assertIn("error", result)
        self.assertIn("available", result)

    def test_task_no_args(self):
        result = modis_products.main(["task"])
        self.assertIn("error", result)

    def test_task_list(self):
        result = modis_products.main(["task-list"])
        self.assertIn("tasks", result)
        self.assertGreater(len(result["tasks"]), 5)


class TestHelpIncludesNewCommands(unittest.TestCase):
    def test_help_text_lists_preset_and_task(self):
        help_text = modis_products.show_help()
        self.assertIn("preset", help_text)
        self.assertIn("task <keyword>", help_text)

    def test_help_text_mentions_qa(self):
        """Phase 5: --qa should be documented in show_help()."""
        help_text = modis_products.show_help()
        self.assertIn("--qa PATH", help_text)


class TestQaSummary(unittest.TestCase):
    """Phase 5: --qa sidecar summary tests for modis-product-search."""

    def _run(self, *args):
        """Run main() and return the result dict."""
        return modis_products.main(list(args))

    def test_qa_search_writes_json(self):
        """search <kw> --qa PATH should write a JSON sidecar with the query."""
        import json as _json
        import os as _os
        import tempfile as _tf
        with _tf.TemporaryDirectory() as tmp:
            qa_path = _os.path.join(tmp, "search.qa.json")
            result = self._run("search", "NDVI", "--qa", qa_path)
            self.assertIn("results", result)
            self.assertTrue(_os.path.exists(qa_path), "QA sidecar not written")
            data = _json.load(open(qa_path, encoding="utf-8"))
            self.assertEqual(data["skill"], "modis-product-search")
            self.assertEqual(data["command"], "search")
            self.assertEqual(data["parsed"]["primary"], "NDVI")
            self.assertIn("timestamp", data)
            self.assertIn("version", data)

    def test_qa_show_writes_json(self):
        """show <id> --qa PATH should record the product id."""
        import json as _json
        import os as _os
        import tempfile as _tf
        with _tf.TemporaryDirectory() as tmp:
            qa_path = _os.path.join(tmp, "show.qa.json")
            result = self._run("show", "MOD13Q1", "--qa", qa_path)
            self.assertEqual(result["product_id"], "MOD13Q1")
            data = _json.load(open(qa_path, encoding="utf-8"))
            self.assertEqual(data["command"], "show")
            self.assertEqual(data["parsed"]["primary"], "MOD13Q1")

    def test_qa_preset_writes_matched_products(self):
        """preset <name> --qa PATH should record matched product ids."""
        import json as _json
        import os as _os
        import tempfile as _tf
        with _tf.TemporaryDirectory() as tmp:
            qa_path = _os.path.join(tmp, "preset.qa.json")
            result = self._run("preset", "ndvi-250m", "--qa", qa_path)
            self.assertEqual(result["preset"], "ndvi-250m")
            data = _json.load(open(qa_path, encoding="utf-8"))
            self.assertEqual(data["command"], "preset")
            self.assertEqual(data["parsed"]["primary"], "ndvi-250m")
            self.assertIn("MOD13Q1", data["parsed"]["matched_products"])

    def test_qa_task_writes_matched_products(self):
        """task <kw> --qa PATH should record the matched MODIS product ids."""
        import json as _json
        import os as _os
        import tempfile as _tf
        with _tf.TemporaryDirectory() as tmp:
            qa_path = _os.path.join(tmp, "task.qa.json")
            result = self._run("task", "fire", "--qa", qa_path)
            self.assertEqual(result["task"], "fire")
            data = _json.load(open(qa_path, encoding="utf-8"))
            self.assertEqual(data["command"], "task")
            self.assertEqual(data["parsed"]["primary"], "fire")
            self.assertIn("MOD14A1", data["parsed"]["matched_products"])

    def test_qa_without_path_returns_error(self):
        """--qa without a following PATH should return an error, not crash."""
        result = self._run("search", "NDVI", "--qa")
        self.assertIn("error", result)

    def test_no_qa_does_not_write_file(self):
        """Without --qa, no sidecar should be created."""
        import os as _os
        import tempfile as _tf
        with _tf.TemporaryDirectory() as tmp:
            # Just call with a known result-producing command and ensure no
            # qa file is created in the temp dir.
            before = set(_os.listdir(tmp))
            result = self._run("show", "MOD13Q1")
            self.assertNotIn("error", result)
            after = set(_os.listdir(tmp))
            self.assertEqual(before, after,
                             f"sidecar created unexpectedly: {after - before}")


class TestPlaceCommand(unittest.TestCase):
    """Phase 6: `place <name>` resolves a Chinese place to bbox + covered products."""

    def test_place_help_lists_command(self):
        self.assertIn("place <name>", modis_products.show_help())

    def test_place_no_args_returns_error(self):
        result = modis_products.main(["place"])
        self.assertIn("error", result)

    def test_place_known_chinese_place(self):
        """`place 北京市` should return bbox + covered_ids without network."""
        result = modis_products.main(["place", "北京市"])
        if "error" in result and "_geoskill_core" in result.get("error", ""):
            self.skipTest("_geoskill_core/aoi.py not vendored in this environment")
        self.assertIn("place", result)
        self.assertEqual(result["place"], "北京市")
        self.assertIn("bbox", result)
        w, s, e, n = result["bbox"]
        # Beijing's bbox should be roughly within (115, 39, 117, 41)
        self.assertTrue(115.0 < w < 117.0, f"W out of range: {w}")
        self.assertTrue(39.0 < s < 41.0, f"S out of range: {s}")
        self.assertTrue(115.0 < e < 117.0, f"E out of range: {e}")
        self.assertTrue(39.0 < n < 41.0, f"N out of range: {n}")
        # All global products should cover Beijing
        self.assertIn("covered_ids", result)
        self.assertGreater(result["n_covered"], 10,
                           "Beijing should be covered by most global products")
        # Output should mention the place
        self.assertIn("北京市", result["output"])

    def test_place_known_english_place(self):
        """`place beijing` (lowercase) should also resolve (HARDCODED)."""
        result = modis_products.main(["place", "beijing"])
        if "error" in result and "_geoskill_core" in result.get("error", ""):
            self.skipTest("_geoskill_core/aoi.py not vendored")
        self.assertIn("bbox", result)
        self.assertGreater(result["n_covered"], 0)

    def test_place_with_qa_sidecar(self):
        """`place 北京市 --qa PATH` should record bbox + n_covered in sidecar."""
        import json as _json
        import os as _os
        import tempfile as _tf
        with _tf.TemporaryDirectory() as tmp:
            qa_path = _os.path.join(tmp, "place.qa.json")
            result = modis_products.main(["place", "北京市", "--qa", qa_path])
            if "error" in result and "_geoskill_core" in result.get("error", ""):
                self.skipTest("_geoskill_core/aoi.py not vendored")
            self.assertIn("covered_ids", result)
            self.assertTrue(_os.path.exists(qa_path), "QA sidecar not written")
            data = _json.load(open(qa_path, encoding="utf-8"))
            self.assertEqual(data["command"], "place")
            self.assertEqual(data["parsed"]["primary"], "北京市")
            self.assertIn("bbox", data["parsed"])
            self.assertIn("n_covered", data["parsed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
