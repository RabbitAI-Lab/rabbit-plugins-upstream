#!/usr/bin/env python3
"""Tests for change-detection."""

import sys
import os
import csv
import json
import tempfile
import unittest
import importlib.util
from unittest.mock import patch, MagicMock

import numpy as np

# Load the script module
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "scripts", "change-detection.py")
spec = importlib.util.spec_from_file_location("change_detection", SCRIPT_PATH)
cd = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cd)


class TestValidation(unittest.TestCase):
    """Test input validation."""

    def test_validate_sensor_valid(self):
        for s in ["landsat8", "landsat9", "sentinel2", "LANDSAT8"]:
            self.assertIn(cd.validate_sensor(s), cd.VALID_SENSORS)

    def test_validate_sensor_invalid(self):
        with self.assertRaises(ValueError):
            cd.validate_sensor("modis")

    def test_validate_method_valid(self):
        for m in ["ndvi-diff", "image-diff", "cva", "NDVI-DIFF"]:
            self.assertIn(cd.validate_method(m), cd.VALID_METHODS)

    def test_validate_method_invalid(self):
        with self.assertRaises(ValueError):
            cd.validate_method("random-forest")


class TestNDVI(unittest.TestCase):
    """Test NDVI computation."""

    def test_ndvi_basic(self):
        green = np.array([0.1, 0.2], dtype=np.float32)
        nir = np.array([0.5, 0.8], dtype=np.float32)
        red = np.array([0.1, 0.2], dtype=np.float32)
        result = cd.compute_ndvi(green, nir, red)
        # NDVI = (0.5-0.1)/(0.5+0.1) = 0.667
        self.assertAlmostEqual(result[0], 0.6667, places=3)

    def test_ndvi_zero_denominator(self):
        green = np.array([0.0], dtype=np.float32)
        nir = np.array([0.0], dtype=np.float32)
        red = np.array([0.0], dtype=np.float32)
        result = cd.compute_ndvi(green, nir, red)
        self.assertEqual(result[0], 0.0)


class TestOtsu(unittest.TestCase):
    """Test Otsu threshold."""

    def test_otsu_bimodal(self):
        np.random.seed(42)
        d1 = np.random.normal(0.0, 0.02, 5000)
        d2 = np.random.normal(0.5, 0.05, 5000)
        data = np.concatenate([d1, d2]).astype(np.float32)
        thresh = cd.otsu_threshold(data)
        # Threshold should separate the two peaks (centers at 0.0 and 0.5)
        self.assertGreater(thresh, 0.0)
        self.assertLess(thresh, 0.5)

    def test_otsu_empty(self):
        data = np.array([np.nan], dtype=np.float32)
        thresh = cd.otsu_threshold(data)
        self.assertEqual(thresh, 0.1)


class TestDetectionMethods(unittest.TestCase):
    """Test detection method functions."""

    def test_image_diff(self):
        data1 = [np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)]
        data2 = [np.array([[1.5, 2.5], [3.5, 4.5]], dtype=np.float32)]
        bands = {"all": data1}
        bands2 = {"all": data2}
        result = cd.method_image_diff(bands, bands2, bands=[1])
        expected = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=np.float32)
        np.testing.assert_array_almost_equal(result, expected)

    def test_cva(self):
        data1 = [np.array([[1.0, 2.0]], dtype=np.float32)]
        data2 = [np.array([[4.0, 6.0]], dtype=np.float32)]
        bands = {"all": data1}
        bands2 = {"all": data2}
        result = cd.method_cva(bands, bands2, bands=[1])
        expected = np.array([[3.0, 4.0]], dtype=np.float32)
        np.testing.assert_array_almost_equal(result, expected)


class TestCLI(unittest.TestCase):
    """Test CLI setup."""

    def test_parser_builds(self):
        parser = cd.build_parser()
        self.assertIsNotNone(parser)


class TestFormatArgParser(unittest.TestCase):
    """Test --format argument on the 'detect' subcommand (batch-D)."""

    def _parse(self, argv):
        return cd.build_parser().parse_args(argv)

    def test_default_format(self):
        args = self._parse([
            "detect", "--image-t1", "t1.tif", "--image-t2", "t2.tif",
        ])
        self.assertEqual(args.format, "auto")

    def test_geojson_format(self):
        args = self._parse([
            "detect", "--image-t1", "t1.tif", "--image-t2", "t2.tif",
            "--format", "geojson",
        ])
        self.assertEqual(args.format, "geojson")

    def test_csv_format(self):
        args = self._parse([
            "detect", "--image-t1", "t1.tif", "--image-t2", "t2.tif",
            "--format", "csv",
        ])
        self.assertEqual(args.format, "csv")

    def test_json_format(self):
        args = self._parse([
            "detect", "--image-t1", "t1.tif", "--image-t2", "t2.tif",
            "--format", "json",
        ])
        self.assertEqual(args.format, "json")

    def test_rejects_unknown_format(self):
        with self.assertRaises(SystemExit):
            self._parse([
                "detect", "--image-t1", "t1.tif", "--image-t2", "t2.tif",
                "--format", "xml",
            ])


class TestDetectFormatDispatch(unittest.TestCase):
    """End-to-end: run detect with --format on synthetic rasters and assert output."""

    def _make_raster(self, path, data, transform=None, nodata=-9999.0):
        import rasterio as rio
        from rasterio.transform import Affine
        # data shape is (bands, rows, cols)
        if data.ndim != 3:
            raise ValueError("data must be 3D (bands, rows, cols)")
        n_bands, height, width = data.shape
        if transform is None:
            transform = Affine(1.0, 0.0, 0.0, 0.0, -1.0, float(height))
        with rio.open(
            path, "w", driver="GTiff",
            height=height, width=width,
            count=n_bands,
            dtype="float32", crs="EPSG:4326",
            transform=transform, nodata=nodata,
        ) as dst:
            for i in range(n_bands):
                dst.write(data[i], i + 1)
        return path

    def _synthetic_inputs(self, tmp):
        # Two small 7-band rasters matching Landsat 8 (Coastal, Blue, Green,
        # Red, NIR, SWIR1, SWIR2). Bands 4 (Red) and 5 (NIR) are used by
        # the ndvi-diff method.
        t1 = tmp / "t1.tif"
        t2 = tmp / "t2.tif"
        data1 = np.zeros((7, 2, 2), dtype="float32")
        data1[0] = 0.05  # Coastal
        data1[1] = 0.07  # Blue
        data1[2] = 0.10  # Green
        data1[3] = 0.20  # Red
        data1[4] = 0.40  # NIR
        data1[5] = 0.30  # SWIR1
        data1[6] = 0.25  # SWIR2
        data2 = data1.copy()
        # Modify some pixels to force a real change
        data2[3, 0, 0] = 0.50  # Red increases
        data2[4, 1, 1] = 0.05  # NIR drops
        self._make_raster(str(t1), data1)
        self._make_raster(str(t2), data2)
        return str(t1), str(t2)

    def test_detect_qa_geojson(self):
        with tempfile.TemporaryDirectory() as d:
            t1, t2 = self._synthetic_inputs(__import__("pathlib").Path(d))
            out = os.path.join(d, "change.tif")
            args = cd.argparse.Namespace(
                image_t1=t1, image_t2=t2,
                sensor="landsat8", method="ndvi-diff",
                output=out, mask=None,  # avoid pre-existing uint8/nodata bug
                threshold=None, bands=None,
                place=None, preset=None, json=False,
                qa=True, format="geojson",
            )
            cd.cmd_detect(args)
            qa_path = os.path.splitext(out)[0] + ".qa.geojson"
            self.assertTrue(os.path.exists(qa_path))
            with open(qa_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertEqual(data["type"], "FeatureCollection")
            self.assertGreater(len(data["features"]), 0)
            self.assertIn("method", data["features"][0]["properties"])

    def test_detect_qa_csv(self):
        with tempfile.TemporaryDirectory() as d:
            t1, t2 = self._synthetic_inputs(__import__("pathlib").Path(d))
            out = os.path.join(d, "change.tif")
            args = cd.argparse.Namespace(
                image_t1=t1, image_t2=t2,
                sensor="landsat8", method="ndvi-diff",
                output=out, mask=None,
                threshold=None, bands=None,
                place=None, preset=None, json=False,
                qa=True, format="csv",
            )
            cd.cmd_detect(args)
            qa_path = os.path.splitext(out)[0] + ".qa.csv"
            self.assertTrue(os.path.exists(qa_path))
            with open(qa_path, "r", encoding="utf-8", newline="") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), 1)
            self.assertIn("change_pixels", rows[0])

    def test_detect_qa_json_default(self):
        with tempfile.TemporaryDirectory() as d:
            t1, t2 = self._synthetic_inputs(__import__("pathlib").Path(d))
            out = os.path.join(d, "change.tif")
            args = cd.argparse.Namespace(
                image_t1=t1, image_t2=t2,
                sensor="landsat8", method="ndvi-diff",
                output=out, mask=None,
                threshold=None, bands=None,
                place=None, preset=None, json=False,
                qa=True, format="auto",
            )
            cd.cmd_detect(args)
            qa_path = os.path.splitext(out)[0] + ".qa.json"
            self.assertTrue(os.path.exists(qa_path))
            with open(qa_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIn("change_pixels", data)

    def test_detect_json_stdout_csv(self):
        with tempfile.TemporaryDirectory() as d:
            t1, t2 = self._synthetic_inputs(__import__("pathlib").Path(d))
            out = os.path.join(d, "change.tif")
            args = cd.argparse.Namespace(
                image_t1=t1, image_t2=t2,
                sensor="landsat8", method="ndvi-diff",
                output=out, mask=None,
                threshold=None, bands=None,
                place=None, preset=None, json=True,
                qa=False, format="csv",
            )
            import io, contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                cd.cmd_detect(args)
            text = buf.getvalue()
            # The CSV stats are emitted after the run; verify the header and
            # the change_pixels column appear somewhere in the output.
            self.assertIn("change_pixels", text)

    def test_detect_json_stdout_geojson(self):
        with tempfile.TemporaryDirectory() as d:
            t1, t2 = self._synthetic_inputs(__import__("pathlib").Path(d))
            out = os.path.join(d, "change.tif")
            args = cd.argparse.Namespace(
                image_t1=t1, image_t2=t2,
                sensor="landsat8", method="ndvi-diff",
                output=out, mask=None,
                threshold=None, bands=None,
                place=None, preset=None, json=True,
                qa=False, format="geojson",
            )
            import io, contextlib, re
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                cd.cmd_detect(args)
            text = buf.getvalue()
            # The FeatureCollection JSON is the last balanced JSON object in
            # the buffer — extract it by scanning for the closing brace.
            start = text.find('{\n  "type": "FeatureCollection"')
            self.assertGreaterEqual(start, 0,
                msg=f"Expected FeatureCollection in output, got: {text[-300:]}")
            data = json.loads(text[start:])
            self.assertEqual(data["type"], "FeatureCollection")
            self.assertGreater(len(data["features"]), 0)


if __name__ == "__main__":
    unittest.main()
