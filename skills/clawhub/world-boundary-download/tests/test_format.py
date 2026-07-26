"""Tests for format normalisation and conversions.

Pure-Python tests for the helper layer; the live conversions are
covered by the integration test in :mod:`test_geoboundaries`.
"""

from __future__ import annotations

import pytest

from core import format as fmt_mod
from core.exceptions import FormatError


class TestNormalizeFormat:
    @pytest.mark.parametrize(
        "raw,expected",
        [
            ("shp", "shp"),
            ("SHP", "shp"),
            ("shapefile", "shp"),
            ("esri shp", "shp"),
            ("geojson", "geojson"),
            ("gson", "geojson"),
            ("json", "geojson"),
            ("gpkg", "gpkg"),
            ("geopackage", "gpkg"),
            ("topojson", "topojson"),
            ("topo", "topojson"),
        ],
    )
    def test_aliases(self, raw, expected):
        assert fmt_mod.normalize_format(raw) == expected

    def test_invalid(self):
        with pytest.raises(FormatError):
            fmt_mod.normalize_format("xyz")


class TestOutputSuffix:
    def test_known_formats(self):
        assert fmt_mod.OUTPUT_SUFFIX["shp"] == ".zip"
        assert fmt_mod.OUTPUT_SUFFIX["geojson"] == ".geojson"
        assert fmt_mod.OUTPUT_SUFFIX["gpkg"] == ".gpkg"
        assert fmt_mod.OUTPUT_SUFFIX["topojson"] == ".topojson"

    def test_all_supported_have_suffix(self):
        for fmt in fmt_mod.SUPPORTED_OUTPUT_FORMATS:
            assert fmt in fmt_mod.OUTPUT_SUFFIX
