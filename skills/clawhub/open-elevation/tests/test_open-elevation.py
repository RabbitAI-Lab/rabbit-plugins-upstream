#!/usr/bin/env python3
"""Tests for open-elevation CLI."""

import sys
import os
import json
import csv
import importlib.util
import unittest
from unittest.mock import patch, MagicMock

# Load the module from scripts/open-elevation.py (hyphenated filename)
_script_path = os.path.join(os.path.dirname(__file__), "..", "scripts", "open-elevation.py")
_spec = importlib.util.spec_from_file_location("open_elevation", _script_path)
oe = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(oe)


class TestValidation(unittest.TestCase):
    def test_valid_lat(self):
        self.assertTrue(oe.validate_lat(0))
        self.assertTrue(oe.validate_lat(90))
        self.assertTrue(oe.validate_lat(-90))
        self.assertTrue(oe.validate_lat(39.9042))

    def test_invalid_lat(self):
        self.assertFalse(oe.validate_lat(91))
        self.assertFalse(oe.validate_lat(-91))

    def test_valid_lon(self):
        self.assertTrue(oe.validate_lon(0))
        self.assertTrue(oe.validate_lon(180))
        self.assertTrue(oe.validate_lon(-180))
        self.assertTrue(oe.validate_lon(116.4074))

    def test_invalid_lon(self):
        self.assertFalse(oe.validate_lon(181))
        self.assertFalse(oe.validate_lon(-181))


class TestDetectColumns(unittest.TestCase):
    def test_standard_names(self):
        lat, lon = oe.detect_columns(["id", "lat", "lon", "name"])
        self.assertEqual(lat, "lat")
        self.assertEqual(lon, "lon")

    def test_full_names(self):
        lat, lon = oe.detect_columns(["latitude", "longitude", "elevation"])
        self.assertEqual(lat, "latitude")
        self.assertEqual(lon, "longitude")

    def test_no_match(self):
        lat, lon = oe.detect_columns(["a", "b", "c"])
        self.assertIsNone(lat)
        self.assertIsNone(lon)


class TestQueryElevation(unittest.TestCase):
    @patch("requests.post")
    def test_success(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "results": [{"latitude": 39.9, "longitude": 116.4, "elevation": 43.5}]
        }
        mock_resp.raise_for_status = MagicMock()
        mock_post.return_value = mock_resp

        result = oe.query_elevation([{"latitude": 39.9, "longitude": 116.4}])
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1)
        self.assertAlmostEqual(result[0]["elevation"], 43.5)

    @patch("requests.post")
    def test_timeout(self, mock_post):
        import requests as req
        mock_post.side_effect = req.exceptions.Timeout()
        result = oe.query_elevation([{"latitude": 0, "longitude": 0}])
        self.assertIsNone(result)


class TestCLI(unittest.TestCase):
    @patch("requests.post")
    def test_lookup_valid(self, mock_post):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "results": [{"latitude": 39.9, "longitude": 116.4, "elevation": 43.5}]
        }
        mock_resp.raise_for_status = MagicMock()
        mock_post.return_value = mock_resp
        args = oe.argparse.Namespace(lat=39.9, lon=116.4, json=False, place=None,
                                     qa=False, output=None, fmt=None)
        rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 0)

    def test_lookup_invalid_lat(self):
        args = oe.argparse.Namespace(lat=999, lon=116.4, json=False, place=None,
                                     qa=False, output=None, fmt=None)
        rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 1)

    def test_lookup_invalid_lon(self):
        args = oe.argparse.Namespace(lat=39.9, lon=999, json=False, place=None,
                                     qa=False, output=None, fmt=None)
        rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 1)

    def test_lookup_no_args_errors(self):
        args = oe.argparse.Namespace(lat=None, lon=None, json=False, place=None,
                                     qa=False, output=None, fmt=None)
        rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 1)


class TestFormat(unittest.TestCase):
    """Tests for --format (csv / json) flag on lookup and batch subcommands."""

    @patch("requests.post")
    def test_lookup_format_csv_default(self, mock_post, capsys=None):
        """Default --format (csv) should emit comma-separated lat,lon,elevation."""
        import io
        from contextlib import redirect_stdout
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "results": [{"latitude": 39.9, "longitude": 116.4, "elevation": 43.5}]
        }
        mock_resp.raise_for_status = MagicMock()
        mock_post.return_value = mock_resp
        args = oe.argparse.Namespace(lat=39.9, lon=116.4, json=False, place=None,
                                     qa=False, output=None, fmt=None)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 0)
        out = buf.getvalue().strip()
        parts = out.split(",")
        self.assertEqual(len(parts), 3)
        self.assertAlmostEqual(float(parts[0]), 39.9, places=4)
        self.assertAlmostEqual(float(parts[1]), 116.4, places=4)
        self.assertAlmostEqual(float(parts[2]), 43.5, places=4)

    @patch("requests.post")
    def test_lookup_format_csv_explicit(self, mock_post):
        """--format csv should emit CSV-style 'lat,lon,elevation'."""
        import io
        from contextlib import redirect_stdout
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "results": [{"latitude": 39.9, "longitude": 116.4, "elevation": 43.5}]
        }
        mock_resp.raise_for_status = MagicMock()
        mock_post.return_value = mock_resp
        args = oe.argparse.Namespace(lat=39.9, lon=116.4, json=False, place=None,
                                     qa=False, output=None, fmt="csv")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 0)
        out = buf.getvalue().strip()
        parts = out.split(",")
        self.assertEqual(len(parts), 3)

    @patch("requests.post")
    def test_lookup_format_json(self, mock_post):
        """--format json should emit JSON object with lat/lon/elevation."""
        import io
        from contextlib import redirect_stdout
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "results": [{"latitude": 39.9, "longitude": 116.4, "elevation": 43.5}]
        }
        mock_resp.raise_for_status = MagicMock()
        mock_post.return_value = mock_resp
        args = oe.argparse.Namespace(lat=39.9, lon=116.4, json=False, place=None,
                                     qa=False, output=None, fmt="json")
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 0)
        out = buf.getvalue().strip()
        data = json.loads(out)
        self.assertIn("latitude", data)
        self.assertIn("longitude", data)
        self.assertIn("elevation", data)
        self.assertAlmostEqual(data["elevation"], 43.5)

    @patch("requests.post")
    def test_lookup_format_json_legacy_alias(self, mock_post):
        """Legacy --json flag should still emit JSON (backward compat)."""
        import io
        from contextlib import redirect_stdout
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = {
            "results": [{"latitude": 39.9, "longitude": 116.4, "elevation": 43.5}]
        }
        mock_resp.raise_for_status = MagicMock()
        mock_post.return_value = mock_resp
        args = oe.argparse.Namespace(lat=39.9, lon=116.4, json=True, place=None,
                                     qa=False, output=None, fmt=None)
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = oe.cmd_lookup(args)
        self.assertEqual(rc, 0)
        out = buf.getvalue().strip()
        data = json.loads(out)
        self.assertIn("elevation", data)

    def test_resolve_format_default(self):
        """_resolve_format should default to 'csv' when neither --format nor --json is set."""
        args = oe.argparse.Namespace(fmt=None, json=False)
        self.assertEqual(oe._resolve_format(args, default="csv"), "csv")

    def test_resolve_format_explicit_json(self):
        args = oe.argparse.Namespace(fmt="json", json=False)
        self.assertEqual(oe._resolve_format(args, default="csv"), "json")

    def test_resolve_format_legacy_json_alias(self):
        """Legacy --json should map to 'json' format."""
        args = oe.argparse.Namespace(fmt=None, json=True)
        self.assertEqual(oe._resolve_format(args, default="csv"), "json")

    def test_resolve_format_explicit_overrides_legacy(self):
        """--format should win over legacy --json."""
        args = oe.argparse.Namespace(fmt="csv", json=True)
        self.assertEqual(oe._resolve_format(args, default="csv"), "csv")

    def test_lookup_subcommand_help_shows_format(self):
        """`lookup --help` should mention the new --format flag."""
        import subprocess
        import sys as _sys
        result = subprocess.run(
            [_sys.executable, _script_path, "lookup", "--help"],
            capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--format", result.stdout)
        self.assertIn("csv", result.stdout)
        self.assertIn("json", result.stdout)

    def test_batch_subcommand_help_shows_format(self):
        """`batch --help` should mention the new --format flag."""
        import subprocess
        import sys as _sys
        result = subprocess.run(
            [_sys.executable, _script_path, "batch", "--help"],
            capture_output=True, text=True, timeout=15,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("--format", result.stdout)
        self.assertIn("csv", result.stdout)
        self.assertIn("json", result.stdout)


if __name__ == "__main__":
    unittest.main()
