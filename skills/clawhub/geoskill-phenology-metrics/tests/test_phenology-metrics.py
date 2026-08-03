#!/usr/bin/env python3
"""Tests for phenology-metrics."""

import sys
import os
import unittest
import json
import importlib.util
import tempfile

import numpy as np
import pandas as pd

# Load the script module
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "scripts", "phenology-metrics.py")
spec = importlib.util.spec_from_file_location("phenology_metrics", SCRIPT_PATH)
pm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pm)


class TestThreshold(unittest.TestCase):
    """Test threshold extraction method."""

    def setUp(self):
        """Create synthetic NDVI time series (one season)."""
        np.random.seed(42)
        self.dates = np.linspace(0, 365, 50)
        # Simulate seasonal NDVI: baseline 0.2, peak 0.8 at day 180
        self.values = 0.2 + 0.6 / (1 + np.exp(-0.05 * (self.dates - 120))) - \
                       0.6 / (1 + np.exp(-0.05 * (self.dates - 240)))
        self.values += np.random.normal(0, 0.02, len(self.values))
        self.values = np.clip(self.values, 0, 1)

    def test_threshold_sos_eos(self):
        result = pm.extract_threshold(self.dates, self.values, 0.5)
        self.assertIsNotNone(result["sos"])
        self.assertIsNotNone(result["eos"])
        self.assertGreater(result["eos"], result["sos"])

    def test_threshold_los(self):
        result = pm.extract_threshold(self.dates, self.values, 0.5)
        self.assertIsNotNone(result["los"])
        self.assertGreater(result["los"], 50)  # Season should be > 50 days
        self.assertLess(result["los"], 300)

    def test_threshold_ratio_10(self):
        result = pm.extract_threshold(self.dates, self.values, 0.1)
        self.assertIsNotNone(result["sos"])
        # Lower ratio should give earlier SOS
        result_50 = pm.extract_threshold(self.dates, self.values, 0.5)
        self.assertLessEqual(result["sos"], result_50["sos"])


class TestDerivative(unittest.TestCase):
    """Test derivative extraction method."""

    def setUp(self):
        np.random.seed(42)
        self.dates = np.linspace(0, 365, 50)
        self.values = 0.2 + 0.6 / (1 + np.exp(-0.05 * (self.dates - 120))) - \
                       0.6 / (1 + np.exp(-0.05 * (self.dates - 240)))
        self.values += np.random.normal(0, 0.02, len(self.values))
        self.values = np.clip(self.values, 0, 1)

    def test_derivative_sos_eos(self):
        result = pm.extract_derivative(self.dates, self.values)
        self.assertIsNotNone(result["sos"])
        self.assertIsNotNone(result["eos"])
        # SOS should be before EOS
        self.assertLess(result["sos"], result["eos"])


class TestLogisticFit(unittest.TestCase):
    """Test double logistic fitting."""

    def setUp(self):
        np.random.seed(42)
        self.dates = np.linspace(0, 365, 50)
        self.values = 0.2 + 0.6 / (1 + np.exp(-0.05 * (self.dates - 120))) - \
                       0.6 / (1 + np.exp(-0.05 * (self.dates - 240)))
        self.values += np.random.normal(0, 0.01, len(self.values))
        self.values = np.clip(self.values, 0, 1)

    def test_logistic_fit(self):
        result = pm.fit_logistic(self.dates, self.values)
        self.assertIn("r_squared", result)
        self.assertGreater(result["r_squared"], 0.5)  # Should fit well
        self.assertIsNotNone(result["sos"])
        self.assertIsNotNone(result["eos"])
        self.assertIsNotNone(result["peak_value"])

    def test_logistic_params(self):
        result = pm.fit_logistic(self.dates, self.values)
        self.assertIn("fitted_params", result)
        self.assertEqual(len(result["fitted_params"]), 6)


class TestDataLoading(unittest.TestCase):
    """Test CSV loading."""

    def setUp(self):
        """Create a temporary CSV file."""
        self.temp_dir = tempfile.mkdtemp()
        self.csv_path = os.path.join(self.temp_dir, "test_ndvi.csv")
        dates = pd.date_range("2023-01-01", periods=50, freq="7D")
        np.random.seed(42)
        values = 0.2 + 0.6 / (1 + np.exp(-0.05 * (np.arange(50) - 20))) - \
                  0.6 / (1 + np.exp(-0.05 * (np.arange(50) - 40)))
        values += np.random.normal(0, 0.02, 50)
        df = pd.DataFrame({"date": dates, "ndvi": np.clip(values, 0, 1)})
        df.to_csv(self.csv_path, index=False)

    def test_load_timeseries(self):
        df = pm.load_timeseries(self.csv_path, "date", "ndvi")
        self.assertEqual(len(df), 50)
        self.assertIn("date", df.columns)
        self.assertIn("ndvi", df.columns)

    def test_load_missing_column(self):
        with self.assertRaises(ValueError):
            pm.load_timeseries(self.csv_path, "date", "evi")


class TestCLI(unittest.TestCase):
    """Test CLI setup."""

    def test_parser_builds(self):
        parser = pm.build_parser()
        self.assertIsNotNone(parser)

    def test_extract_subcommand_help_shows_format(self):
        """`extract --help` should mention the new --format flag."""
        import subprocess
        import sys as _sys
        result = subprocess.run(
            [_sys.executable, SCRIPT_PATH, "extract", "--help"],
            capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--format", result.stdout)
        self.assertIn("csv", result.stdout)
        self.assertIn("json", result.stdout)

    def test_from_place_subcommand_help_shows_format(self):
        """`from-place --help` should mention the new --format flag."""
        import subprocess
        import sys as _sys
        result = subprocess.run(
            [_sys.executable, SCRIPT_PATH, "from-place", "--help"],
            capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--format", result.stdout)
        self.assertIn("csv", result.stdout)
        self.assertIn("json", result.stdout)


class TestFormat(unittest.TestCase):
    """Tests for --format (csv / json) flag on extract subcommand."""

    def setUp(self):
        """Create a temporary CSV file."""
        self.temp_dir = tempfile.mkdtemp()
        self.csv_path = os.path.join(self.temp_dir, "test_ndvi.csv")
        dates = pd.date_range("2023-01-01", periods=50, freq="7D")
        np.random.seed(42)
        values = 0.2 + 0.6 / (1 + np.exp(-0.05 * (np.arange(50) - 20))) - \
                  0.6 / (1 + np.exp(-0.05 * (np.arange(50) - 40)))
        values += np.random.normal(0, 0.02, 50)
        df = pd.DataFrame({"date": dates, "ndvi": np.clip(values, 0, 1)})
        df.to_csv(self.csv_path, index=False)

    def test_extract_format_csv(self):
        """--format csv should produce a CSV file with metrics in one row."""
        out_csv = os.path.join(self.temp_dir, "metrics.csv")
        args = pm.argparse.Namespace(
            input=self.csv_path, date_col="date", value_col="ndvi",
            method="threshold", threshold_ratio=0.5,
            place=None, preset=None, output=out_csv,
            fmt="csv", json=False, qa=False, place_info=None,
        )
        pm.cmd_extract(args)
        self.assertTrue(os.path.exists(out_csv))
        with open(out_csv, "r", encoding="utf-8") as f:
            text = f.read()
        # CSV header should contain sos / eos
        self.assertIn("sos", text)
        self.assertIn("eos", text)
        self.assertIn("los", text)

    def test_extract_format_json(self):
        """--format json should produce a JSON file with full metrics dict."""
        out_json = os.path.join(self.temp_dir, "metrics.json")
        args = pm.argparse.Namespace(
            input=self.csv_path, date_col="date", value_col="ndvi",
            method="threshold", threshold_ratio=0.5,
            place=None, preset=None, output=out_json,
            fmt="json", json=False, qa=False, place_info=None,
        )
        pm.cmd_extract(args)
        self.assertTrue(os.path.exists(out_json))
        with open(out_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("sos", data)
        self.assertIn("eos", data)
        self.assertIn("method", data)

    def test_extract_format_json_legacy_alias(self):
        """Legacy --json should still produce JSON (backward compat)."""
        out_json = os.path.join(self.temp_dir, "metrics_legacy.json")
        args = pm.argparse.Namespace(
            input=self.csv_path, date_col="date", value_col="ndvi",
            method="threshold", threshold_ratio=0.5,
            place=None, preset=None, output=out_json,
            fmt=None, json=True, qa=False, place_info=None,
        )
        pm.cmd_extract(args)
        self.assertTrue(os.path.exists(out_json))
        with open(out_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("sos", data)

    def test_extract_format_inferred_from_suffix_json(self):
        """When --format not given and output ends with .json, write JSON."""
        out_json = os.path.join(self.temp_dir, "inferred.json")
        args = pm.argparse.Namespace(
            input=self.csv_path, date_col="date", value_col="ndvi",
            method="threshold", threshold_ratio=0.5,
            place=None, preset=None, output=out_json,
            fmt=None, json=False, qa=False, place_info=None,
        )
        pm.cmd_extract(args)
        self.assertTrue(os.path.exists(out_json))
        with open(out_json, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.assertIn("sos", data)

    def test_extract_qa_records_format(self):
        """QA summary should record the chosen format."""
        out_json = os.path.join(self.temp_dir, "qa_test.json")
        qa_path = os.path.join(self.temp_dir, "qa_test.qa.json")
        args = pm.argparse.Namespace(
            input=self.csv_path, date_col="date", value_col="ndvi",
            method="threshold", threshold_ratio=0.5,
            place=None, preset=None, output=out_json,
            fmt="json", json=False, qa=True, place_info=None,
        )
        pm.cmd_extract(args)
        self.assertTrue(os.path.exists(qa_path))
        with open(qa_path, "r", encoding="utf-8") as f:
            qa = json.load(f)
        self.assertEqual(qa["format"], "json")


if __name__ == "__main__":
    unittest.main()
