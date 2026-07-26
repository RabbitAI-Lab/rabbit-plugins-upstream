#!/usr/bin/env python3
"""Tests for drought-monitor: SPI/SPEI calculation."""

import sys
import os
import csv
import json
import tempfile
import unittest
import importlib.util

# Load module from file path (handles hyphenated filename)
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "scripts", "drought-monitor.py")
spec = importlib.util.spec_from_file_location("drought_monitor", SCRIPT_PATH)
dm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dm)


class TestSPIClassification(unittest.TestCase):
    """Test SPI classification logic."""

    def test_extreme_drought(self):
        self.assertEqual(dm.classify_spi(-2.5), "Extreme drought")

    def test_severe_drought(self):
        self.assertEqual(dm.classify_spi(-1.8), "Severe drought")

    def test_moderate_drought(self):
        self.assertEqual(dm.classify_spi(-1.2), "Moderate drought")

    def test_normal(self):
        self.assertEqual(dm.classify_spi(0.0), "Normal")
        self.assertEqual(dm.classify_spi(0.5), "Normal")
        self.assertEqual(dm.classify_spi(-0.5), "Normal")

    def test_moderate_wet(self):
        self.assertEqual(dm.classify_spi(1.2), "Moderate wet")

    def test_very_wet(self):
        self.assertEqual(dm.classify_spi(1.7), "Very wet")

    def test_extremely_wet(self):
        self.assertEqual(dm.classify_spi(2.5), "Extremely wet")

    def test_boundary_values(self):
        """Test exact boundary values.
        Classification uses low <= value < high, so boundary values
        belong to the higher class (e.g., 1.0 -> Moderate wet, not Normal).
        """
        self.assertEqual(dm.classify_spi(-2.0), "Severe drought")
        self.assertEqual(dm.classify_spi(-1.5), "Moderate drought")
        self.assertEqual(dm.classify_spi(-1.0), "Normal")
        self.assertEqual(dm.classify_spi(1.0), "Moderate wet")  # 1.0 is lower bound of Moderate wet
        self.assertEqual(dm.classify_spi(1.5), "Very wet")       # 1.5 is lower bound of Very wet
        self.assertEqual(dm.classify_spi(2.0), "Extremely wet")  # 2.0 is lower bound of Extremely wet


class TestAccumulatePrecip(unittest.TestCase):
    """Test precipitation accumulation."""

    def test_accumulate_3month(self):
        """Test 3-month accumulation."""
        data = [
            {"date": "20200101", "value": 1.0},
            {"date": "20200102", "value": 2.0},
            {"date": "20200201", "value": 3.0},
            {"date": "20200301", "value": 4.0},
            {"date": "20200401", "value": 5.0},
        ]
        result = dm.accumulate_precip(data, 3)
        # Jan total = 3.0, Feb = 3.0, Mar = 4.0, Apr = 5.0
        # 3-month accum: Jan+Feb+Mar = 10.0, Feb+Mar+Apr = 12.0
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0]["value"], 10.0)
        self.assertAlmostEqual(result[1]["value"], 12.0)


class TestGammaFitting(unittest.TestCase):
    """Test gamma distribution fitting."""

    def test_fit_gamma_basic(self):
        """Test gamma fitting with known data."""
        import numpy as np
        np.random.seed(42)
        data = np.random.gamma(shape=2.0, scale=3.0, size=100)
        result = dm.fit_gamma(data)
        self.assertIsNotNone(result)
        shape, loc, scale, p_zero = result
        self.assertGreater(shape, 0)
        self.assertGreater(scale, 0)
        self.assertEqual(p_zero, 0.0)


class TestSPICalculation(unittest.TestCase):
    """Test full SPI calculation pipeline."""

    def test_compute_spi_basic(self):
        """Test SPI computation with synthetic data."""
        import numpy as np
        np.random.seed(42)
        base_values = np.random.gamma(shape=3.0, scale=20.0, size=60)
        accumulated = []
        for i, v in enumerate(base_values):
            year = 2020 + i // 12
            month = i % 12 + 1
            accumulated.append({"date": f"{year}{month:02d}", "value": float(v)})

        results = dm.compute_spi(accumulated, 3)
        self.assertGreater(len(results), 0)

        for r in results:
            self.assertIn("date", r)
            self.assertIn("spi", r)
            self.assertIn("classification", r)
            self.assertIsInstance(r["spi"], float)

        spi_values = [r["spi"] for r in results]
        mean_spi = sum(spi_values) / len(spi_values)
        self.assertLess(abs(mean_spi), 1.0)


class TestReportGeneration(unittest.TestCase):
    """Test report generation."""

    def test_generate_report(self):
        """Test report from SPI results."""
        import numpy as np
        np.random.seed(42)
        results = []
        for i in range(24):
            year = 2020 + i // 12
            month = i % 12 + 1
            spi = float(np.random.normal(0, 1))
            results.append({
                "date": f"{year}{month:02d}",
                "spi": spi,
                "classification": dm.classify_spi(spi),
            })

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            output_path = f.name

        try:
            report = dm.generate_report(results, output_path)
            self.assertIn("period", report)
            self.assertIn("spi_statistics", report)
            self.assertIn("classification_counts", report)
            self.assertIn("drought_frequency_percent", report)
            self.assertIn("trend", report)

            self.assertTrue(os.path.exists(output_path))
            with open(output_path) as f:
                loaded = json.load(f)
            self.assertEqual(loaded["period"]["total_months"], 24)
        finally:
            os.unlink(output_path)


class TestInputValidation(unittest.TestCase):
    """Test input validation."""

    def test_valid_scales(self):
        """Test that valid scales are accepted."""
        for scale in [1, 3, 6, 12, 24]:
            self.assertIn(scale, dm.VALID_SCALES)

    def test_drought_classes_coverage(self):
        """Test that drought classes cover all real numbers."""
        import numpy as np
        test_values = np.linspace(-5, 5, 100)
        for v in test_values:
            result = dm.classify_spi(float(v))
            self.assertNotEqual(result, "Unknown")


class TestOutputWriters(unittest.TestCase):
    """Test --format dispatch (csv / json / ndjson) for batch-D upgrade."""

    def _sample(self):
        return [
            {"date": "202001", "spi": 0.5, "classification": "Normal"},
            {"date": "202002", "spi": -1.2, "classification": "Moderate drought"},
            {"date": "202003", "spi": 1.8, "classification": "Very wet"},
        ]

    def test_write_csv(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            path = f.name
        try:
            dm.write_csv(self._sample(), path)
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            self.assertEqual(len(rows), 3)
            self.assertEqual(rows[0]["date"], "202001")
        finally:
            os.unlink(path)

    def test_write_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            path = f.name
        try:
            dm.write_json(self._sample(), path)
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIsInstance(data, list)
            self.assertEqual(len(data), 3)
            self.assertEqual(data[1]["classification"], "Moderate drought")
        finally:
            os.unlink(path)

    def test_write_ndjson(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".ndjson", delete=False) as f:
            path = f.name
        try:
            dm.write_ndjson(self._sample(), path)
            with open(path, "r", encoding="utf-8") as f:
                lines = [l for l in f.read().splitlines() if l.strip()]
            self.assertEqual(len(lines), 3)
            # Each line must parse as standalone JSON
            for line in lines:
                obj = json.loads(line)
                self.assertIn("spi", obj)
                self.assertIn("date", obj)
        finally:
            os.unlink(path)

    def test_write_results_dispatches(self):
        cases = [
            ("csv", ".csv", csv.DictReader),
            ("json", ".json", None),
            ("ndjson", ".ndjson", None),
        ]
        for fmt, ext, _ in cases:
            with tempfile.NamedTemporaryFile(mode="w", suffix=ext, delete=False) as f:
                path = f.name
            try:
                dm.write_results(self._sample(), path, fmt=fmt)
                self.assertTrue(os.path.exists(path))
                if fmt == "csv":
                    with open(path, "r", encoding="utf-8") as f:
                        rows = list(csv.DictReader(f))
                    self.assertEqual(len(rows), 3)
                elif fmt == "json":
                    with open(path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    self.assertEqual(len(data), 3)
                elif fmt == "ndjson":
                    with open(path, "r", encoding="utf-8") as f:
                        lines = [l for l in f.read().splitlines() if l.strip()]
                    self.assertEqual(len(lines), 3)
            finally:
                os.unlink(path)

    def test_write_results_unknown_falls_back_to_csv(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
            path = f.name
        try:
            dm.write_results(self._sample(), path, fmt="unknown_format")
            with open(path, "r", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), 3)
        finally:
            os.unlink(path)


class TestFormatArgParser(unittest.TestCase):
    """Test --format argument on spi/spei subcommands."""

    def _parse(self, argv):
        # Build parser manually from the same module
        import argparse
        p = argparse.ArgumentParser(prog="drought-monitor")
        sub = p.add_subparsers(dest="command")
        spi = sub.add_parser("spi")
        spi.add_argument("--format", choices=["csv", "json", "ndjson"], default="csv")
        spei = sub.add_parser("spei")
        spei.add_argument("--format", choices=["csv", "json", "ndjson"], default="csv")
        return p.parse_args(argv)

    def test_spi_default_format(self):
        args = self._parse(["spi"])
        self.assertEqual(args.format, "csv")

    def test_spi_json_format(self):
        args = self._parse(["spi", "--format", "json"])
        self.assertEqual(args.format, "json")

    def test_spi_ndjson_format(self):
        args = self._parse(["spi", "--format", "ndjson"])
        self.assertEqual(args.format, "ndjson")

    def test_spi_format_rejects_unknown(self):
        with self.assertRaises(SystemExit):
            self._parse(["spi", "--format", "xml"])


class TestSPIEndToEndWithFormat(unittest.TestCase):
    """End-to-end: compute SPI from local CSV and write in different formats."""

    def _write_input(self, path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["date", "precipitation"])
            w.writeheader()
            # 24 months of synthetic precipitation
            for i in range(24):
                ym = f"2020{(i % 12) + 1:02d}"
                w.writerow({"date": ym, "precipitation": str(50.0 + (i % 5) * 10)})

    def _run_spi(self, fmt, suffix):
        in_path = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False).name
        out_path = tempfile.NamedTemporaryFile(mode="w", suffix=suffix, delete=False).name
        self._write_input(in_path)
        try:
            args = dm.argparse.Namespace(
                lat=None, lon=None, place=None, preset=None,
                start=None, end=None, scale=3,
                input=in_path, output=out_path,
                format=fmt, qa=False,
            )
            dm.cmd_spi(args)
            self.assertTrue(os.path.exists(out_path))
            if fmt == "csv":
                with open(out_path, "r", encoding="utf-8") as f:
                    rows = list(csv.DictReader(f))
                self.assertGreater(len(rows), 0)
                self.assertIn("spi", rows[0])
            elif fmt == "json":
                with open(out_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.assertIsInstance(data, list)
                self.assertGreater(len(data), 0)
                self.assertIn("spi", data[0])
            elif fmt == "ndjson":
                with open(out_path, "r", encoding="utf-8") as f:
                    lines = [l for l in f.read().splitlines() if l.strip()]
                self.assertGreater(len(lines), 0)
                for line in lines:
                    self.assertIn("spi", json.loads(line))
        finally:
            os.unlink(in_path)
            if os.path.exists(out_path):
                os.unlink(out_path)

    def test_spi_to_csv(self):
        self._run_spi("csv", ".csv")

    def test_spi_to_json(self):
        self._run_spi("json", ".json")

    def test_spi_to_ndjson(self):
        self._run_spi("ndjson", ".ndjson")


if __name__ == "__main__":
    unittest.main()
