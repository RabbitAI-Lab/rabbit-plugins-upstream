"""Unit tests for geometry helpers (bbox, area, clipping)."""

from __future__ import annotations

import math

import pytest

from core import geometry


class TestExpandBbox:
    def test_zero_km(self):
        bb = (10.0, 20.0, 30.0, 40.0)
        assert geometry.expand_bbox(bb, 0) == bb
        assert geometry.expand_bbox(bb, -1) == bb

    def test_1km_at_equator(self):
        bb = (0.0, 0.0, 1.0, 1.0)
        bb2 = geometry.expand_bbox(bb, 1.0)
        # 1° lat ≈ 110.574 km, so 1 km ≈ 0.00904°
        dlat = 1.0 / 110.574
        dlon = 1.0 / 111.320
        assert math.isclose(bb2[0], -dlon, abs_tol=1e-4)
        assert math.isclose(bb2[1], -dlat, abs_tol=1e-4)
        assert math.isclose(bb2[2], 1.0 + dlon, abs_tol=1e-4)
        assert math.isclose(bb2[3], 1.0 + dlat, abs_tol=1e-4)

    def test_1km_at_high_lat(self):
        # At 60° lat, 1° lon is half as wide in km.
        bb = (0.0, 60.0, 1.0, 61.0)
        bb2 = geometry.expand_bbox(bb, 1.0)
        # Lon expansion at lat 60.5 should be ~2x the equator value.
        dlon_eq = 1.0 / 111.320
        dlon_60 = 1.0 / (111.320 * math.cos(math.radians(60.5)))
        assert dlon_60 > dlon_eq
        assert math.isclose(bb2[0], -dlon_60, abs_tol=1e-4)


class TestParseBbox:
    def test_valid(self):
        bb = geometry.parse_bbox("100,20,125,40")
        assert bb == (100.0, 20.0, 125.0, 40.0)

    def test_with_spaces(self):
        bb = geometry.parse_bbox(" 100 , 20 , 125 , 40 ")
        assert bb == (100.0, 20.0, 125.0, 40.0)

    def test_wrong_count(self):
        with pytest.raises(ValueError):
            geometry.parse_bbox("1,2,3")

    def test_nan(self):
        with pytest.raises(ValueError):
            geometry.parse_bbox("foo,bar,baz,qux")

    def test_invalid_order(self):
        with pytest.raises(ValueError):
            geometry.parse_bbox("125,40,100,20")  # W > E

    def test_oob_lat(self):
        with pytest.raises(ValueError):
            geometry.parse_bbox("0,100,1,101")


class TestKmPerDegLon:
    def test_equator(self):
        assert math.isclose(geometry.km_per_deg_lon(0), 111.320, rel_tol=1e-3)

    def test_pole(self):
        # At lat 90, cos(90) ≈ 0, the clamp prevents divide-by-zero.
        v = geometry.km_per_deg_lon(90)
        assert v >= 0


class TestBboxStr:
    def test_round_trip(self):
        bb = (10.123456, 20.654321, 30.0, 40.0)
        s = geometry.bbox_str(bb)
        bb2 = geometry.parse_bbox(s)
        for a, b in zip(bb, bb2):
            assert math.isclose(a, b, abs_tol=1e-4)
