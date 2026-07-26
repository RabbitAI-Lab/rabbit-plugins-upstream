#!/usr/bin/env python3
"""Tests for forest-carbon-estimate: carbon calculation methods."""

import sys
import os
import csv
import json
import tempfile
import unittest
import importlib.util

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "..", "scripts", "forest-carbon-estimate.py")
spec = importlib.util.spec_from_file_location("forest_estimate", SCRIPT_PATH)
fce = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fce)


class TestBEFMethod(unittest.TestCase):
    """Test Biomass Expansion Factor method."""

    def test_bef_basic(self):
        result = fce.estimate_carbon_bef(agb=100, bef=1.3, carbon_fraction=0.47)
        self.assertAlmostEqual(result["agb"], 100.0)
        self.assertAlmostEqual(result["total_biomass"], 130.0)
        self.assertAlmostEqual(result["carbon_stock"], 130.0 * 0.47)
        self.assertEqual(result["method"], "BEF")

    def test_bef_default_params(self):
        result = fce.estimate_carbon_bef(agb=200)
        self.assertAlmostEqual(result["total_biomass"], 200 * 1.3)
        self.assertAlmostEqual(result["carbon_stock"], 200 * 1.3 * 0.47)

    def test_bef_zero_agb(self):
        result = fce.estimate_carbon_bef(agb=0)
        self.assertAlmostEqual(result["carbon_stock"], 0.0)


class TestAllometricMethod(unittest.TestCase):
    """Test allometric equation method."""

    def test_allometric_basic(self):
        result = fce.estimate_carbon_allometric(height=10, forest_type="default")
        self.assertIn("agb", result)
        self.assertIn("bgb", result)
        self.assertIn("total_biomass", result)
        self.assertIn("carbon_stock", result)
        self.assertEqual(result["method"], "allometric")
        self.assertEqual(result["height"], 10)

    def test_allometric_tropical(self):
        # tropical_rainforest falls back to "default" coeffs (a=0.60, b=1.9)
        result = fce.estimate_carbon_allometric(height=20, forest_type="tropical_rainforest")
        expected_agb = 0.60 * (20 ** 1.9)
        self.assertAlmostEqual(result["agb"], expected_agb, places=1)
        # root_shoot for tropical_rainforest = 0.20
        self.assertAlmostEqual(result["bgb"], result["agb"] * 0.20, places=1)

    def test_allometric_increases_with_height(self):
        r1 = fce.estimate_carbon_allometric(height=10, forest_type="default")
        r2 = fce.estimate_carbon_allometric(height=20, forest_type="default")
        self.assertGreater(r2["carbon_stock"], r1["carbon_stock"])


class TestIPCCMethod(unittest.TestCase):
    """Test IPCC Tier 1 method."""

    def test_ipcc_basic(self):
        result = fce.estimate_carbon_ipcc(forest_type="default", area_ha=10.0)
        self.assertIn("agb", result)
        self.assertIn("total_carbon_t", result)
        self.assertEqual(result["method"], "IPCC_Tier1")
        self.assertEqual(result["area_ha"], 10.0)

    def test_ipcc_tropical(self):
        result = fce.estimate_carbon_ipcc(forest_type="tropical_rainforest")
        self.assertAlmostEqual(result["agb"], 200.0)

    def test_ipcc_area_scaling(self):
        r1 = fce.estimate_carbon_ipcc(forest_type="default", area_ha=1.0)
        r2 = fce.estimate_carbon_ipcc(forest_type="default", area_ha=10.0)
        self.assertAlmostEqual(r2["total_carbon_t"], r1["total_carbon_t"] * 10, places=1)


class TestMonteCarloUncertainty(unittest.TestCase):
    """Test Monte Carlo uncertainty analysis."""

    def test_monte_carlo_allometric(self):
        result = fce.monte_carlo_uncertainty(
            method="allometric",
            n_iterations=500,
            height=15,
            forest_type="default",
        )
        self.assertIn("mean", result)
        self.assertIn("std", result)
        self.assertIn("percentile_5", result)
        self.assertIn("percentile_95", result)
        self.assertEqual(result["n_iterations"], 500)
        self.assertGreater(result["mean"], 0)
        self.assertGreater(result["std"], 0)

    def test_monte_carlo_bef(self):
        result = fce.monte_carlo_uncertainty(
            method="bef",
            n_iterations=500,
            agb=150,
            forest_type="temperate",
        )
        self.assertIn("mean", result)
        self.assertGreater(result["mean"], 0)

    def test_monte_carlo_ci_width(self):
        result = fce.monte_carlo_uncertainty(
            method="allometric",
            n_iterations=1000,
            height=15,
        )
        ci_low = result["confidence_interval_95"][0]
        ci_high = result["confidence_interval_95"][1]
        self.assertLess(ci_low, ci_high)
        self.assertGreater(ci_high, 0)


class TestCalculationChain(unittest.TestCase):
    """Test the full calculation chain consistency."""

    def test_bef_chain(self):
        agb = 100
        bef = 1.3
        cf = 0.47
        result = fce.estimate_carbon_bef(agb, bef, cf)
        expected_total = agb * bef
        expected_carbon = expected_total * cf
        self.assertAlmostEqual(result["total_biomass"], expected_total)
        self.assertAlmostEqual(result["carbon_stock"], expected_carbon)

    def test_allometric_chain(self):
        result = fce.estimate_carbon_allometric(height=10, forest_type="default")
        expected_total = result["agb"] + result["bgb"]
        expected_carbon = expected_total * fce.CARBON_FRACTION
        self.assertAlmostEqual(result["total_biomass"], expected_total)
        self.assertAlmostEqual(result["carbon_stock"], expected_carbon)


class TestDefaultFactors(unittest.TestCase):
    """Test IPCC default factor tables."""

    def test_root_shoot_ratios_positive(self):
        for forest_type, ratio in fce.ROOT_SHOOT_RATIOS.items():
            self.assertGreater(ratio, 0, f"{forest_type} ratio should be positive")

    def test_bef_factors_greater_than_one(self):
        for forest_type, bef in fce.BEF_FACTORS.items():
            self.assertGreater(bef, 1.0, f"{forest_type} BEF should be > 1")

    def test_carbon_fraction(self):
        self.assertEqual(fce.CARBON_FRACTION, 0.47)


class TestFormatArgParser(unittest.TestCase):
    """Test --format argument on the 'estimate' subcommand (batch-D)."""

    def _parse(self, argv):
        parser = fce.argparse.ArgumentParser(prog="forest-carbon-estimate")
        sub = parser.add_subparsers(dest="command")
        est = sub.add_parser("estimate")
        est.add_argument("--format", choices=["auto", "geojson", "geotiff", "csv", "json"],
                          default="auto")
        return parser.parse_args(argv)

    def test_default_format(self):
        args = self._parse(["estimate"])
        self.assertEqual(args.format, "auto")

    def test_geojson_format(self):
        args = self._parse(["estimate", "--format", "geojson"])
        self.assertEqual(args.format, "geojson")

    def test_csv_format(self):
        args = self._parse(["estimate", "--format", "csv"])
        self.assertEqual(args.format, "csv")

    def test_json_format(self):
        args = self._parse(["estimate", "--format", "json"])
        self.assertEqual(args.format, "json")

    def test_geotiff_format(self):
        args = self._parse(["estimate", "--format", "geotiff"])
        self.assertEqual(args.format, "geotiff")

    def test_rejects_unknown_format(self):
        with self.assertRaises(SystemExit):
            self._parse(["estimate", "--format", "xml"])


class TestEstimateSinglePointFormat(unittest.TestCase):
    """Test --format dispatch for the single-point estimation branch."""

    def _run(self, fmt, suffix):
        out_path = tempfile.NamedTemporaryFile(mode="w", suffix=suffix, delete=False).name
        args = fce.argparse.Namespace(
            input=None, method="allometric", forest_type="default",
            height=15, agb=None, area_ha=1.0, agb_band=1,
            place=None, preset=None, qa=False, output=out_path, format=fmt,
        )
        try:
            fce.cmd_estimate(args)
            self.assertTrue(os.path.exists(out_path))
            if fmt == "csv":
                with open(out_path, "r", encoding="utf-8", newline="") as f:
                    rows = list(csv.DictReader(f))
                self.assertEqual(len(rows), 1)
                self.assertIn("carbon_stock", rows[0])
            else:  # json (default for single-point when format not csv)
                with open(out_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.assertIn("carbon_stock", data)
                self.assertIn("method", data)
        finally:
            if os.path.exists(out_path):
                os.unlink(out_path)

    def test_single_point_to_json(self):
        self._run("json", ".json")

    def test_single_point_to_csv(self):
        self._run("csv", ".csv")


class TestEstimateCSVInputFormat(unittest.TestCase):
    """Test --format dispatch for the CSV-input branch."""

    def _write_csv(self, path):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["height"])
            w.writeheader()
            for h in (10, 12, 14, 16, 18):
                w.writerow({"height": h})

    def _run(self, fmt, suffix):
        in_path = tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False).name
        out_path = tempfile.NamedTemporaryFile(mode="w", suffix=suffix, delete=False).name
        self._write_csv(in_path)
        args = fce.argparse.Namespace(
            input=in_path, method="allometric", forest_type="default",
            height=None, agb=None, area_ha=1.0, agb_band=1,
            place=None, preset=None, qa=False, output=out_path, format=fmt,
        )
        try:
            fce.cmd_estimate(args)
            self.assertTrue(os.path.exists(out_path))
            if fmt == "json":
                with open(out_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                self.assertIsInstance(data, list)
                self.assertEqual(len(data), 5)
            else:
                with open(out_path, "r", encoding="utf-8", newline="") as f:
                    rows = list(csv.DictReader(f))
                self.assertEqual(len(rows), 5)
        finally:
            for p in (in_path, out_path):
                if os.path.exists(p):
                    os.unlink(p)

    def test_csv_input_default_writes_csv(self):
        self._run("auto", ".csv")

    def test_csv_input_to_json(self):
        self._run("json", ".json")


if __name__ == "__main__":
    unittest.main()
