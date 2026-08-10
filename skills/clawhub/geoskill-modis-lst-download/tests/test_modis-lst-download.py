#!/usr/bin/env python3
"""
Tests for modis-lst-download CLI.
Run with: python -m pytest tests/ -v
"""

import sys
import os
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

try:
    import modis_lst_download as mld
except ImportError:
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "modis_lst_download",
        str(Path(__file__).parent.parent / "scripts" / "modis_lst_download.py"),
    )
    mld = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mld)


class TestValidation(unittest.TestCase):
    """Test input validation functions."""

    def test_validate_bbox_valid(self):
        """Test valid bounding box."""
        result = mld.validate_bbox([73, 18, 135, 54])
        self.assertEqual(result, (73, 18, 135, 54))

    def test_validate_bbox_invalid_order(self):
        """Test invalid bbox (south >= north)."""
        with self.assertRaises(ValueError):
            mld.validate_bbox([73, 54, 135, 18])

    def test_validate_bbox_invalid_lat(self):
        """Test invalid latitude in bbox."""
        with self.assertRaises(ValueError):
            mld.validate_bbox([73, 91, 135, 54])

    def test_validate_date_range_valid(self):
        """Test valid date range."""
        start, end = mld.validate_date_range("2023-01-01", "2023-12-31")
        self.assertEqual(start.year, 2023)
        self.assertEqual(end.year, 2023)

    def test_validate_date_range_invalid_format(self):
        """Test invalid date format."""
        with self.assertRaises(ValueError):
            mld.validate_date_range("2023/01/01", "2023/12/31")

    def test_validate_date_range_end_before_start(self):
        """Test end date before start date."""
        with self.assertRaises(ValueError):
            mld.validate_date_range("2023-12-31", "2023-01-01")

    def test_validate_date_range_nrt_too_long(self):
        """Test NRT date range > 7 days."""
        with self.assertRaises(ValueError):
            mld.validate_date_range("2023-01-01", "2023-01-15", "NRT")

    def test_validate_product_valid(self):
        """Test valid product names."""
        self.assertEqual(mld.validate_product("MOD11A1"), "MOD11A1")
        self.assertEqual(mld.validate_product("mod11a1"), "MOD11A1")
        self.assertEqual(mld.validate_product("MYD11A2"), "MYD11A2")

    def test_validate_product_invalid(self):
        """Test invalid product name."""
        with self.assertRaises(ValueError):
            mld.validate_product("INVALID")


class TestConfig(unittest.TestCase):
    """Test configuration management."""

    def test_load_config_nonexistent(self):
        """Test loading config when file doesn't exist."""
        with patch("modis_lst_download.CONFIG_FILE") as mock_path:
            mock_path.exists.return_value = False
            config = mld.load_config()
            self.assertEqual(config, {})

    def test_save_and_load_config(self):
        """Test saving and loading config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            config_file = Path(tmpdir) / "config.json"
            with patch("modis_lst_download.CONFIG_FILE", config_file):
                with patch("modis_lst_download.CONFIG_DIR", Path(tmpdir)):
                    test_config = {"earthdata_username": "testuser"}
                    mld.save_config(test_config)
                    loaded = mld.load_config()
                    self.assertEqual(loaded["earthdata_username"], "testuser")


class TestProducts(unittest.TestCase):
    """Test product definitions."""

    def test_all_products_have_required_fields(self):
        """Test that all products have required metadata fields."""
        required_fields = ["name", "satellite", "temporal", "resolution", "collection", "daynight"]
        for product_name, product_info in mld.PRODUCTS.items():
            for field in required_fields:
                self.assertIn(field, product_info,
                              f"Product {product_name} missing field: {field}")

    def test_products_count(self):
        """Test that we have 4 products defined."""
        self.assertEqual(len(mld.PRODUCTS), 4)


class TestCLI(unittest.TestCase):
    """Test CLI argument parsing."""

    def test_help_message(self):
        """Test that help message can be displayed."""
        with self.assertRaises(SystemExit) as cm:
            with patch("sys.argv", ["modis-lst-download", "--help"]):
                mld.main()
        self.assertEqual(cm.exception.code, 0)

    def test_search_help(self):
        """Test search subcommand help."""
        with self.assertRaises(SystemExit) as cm:
            with patch("sys.argv", ["modis-lst-download", "search", "--help"]):
                mld.main()
        self.assertEqual(cm.exception.code, 0)

    def test_download_help(self):
        """Test download subcommand help."""
        with self.assertRaises(SystemExit) as cm:
            with patch("sys.argv", ["modis-lst-download", "download", "--help"]):
                mld.main()
        self.assertEqual(cm.exception.code, 0)

    def test_configure_help(self):
        """Test configure subcommand help."""
        with self.assertRaises(SystemExit) as cm:
            with patch("sys.argv", ["modis-lst-download", "configure", "--help"]):
                mld.main()
        self.assertEqual(cm.exception.code, 0)


if __name__ == "__main__":
    unittest.main()
