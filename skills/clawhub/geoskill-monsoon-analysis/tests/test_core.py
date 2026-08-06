"""Core algorithm tests for monsoon-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ma


class TestWindDirection:
    def test_westerly(self):
        """u>0 (向东吹) = 来自西方 = 270°。"""
        d = ma.wind_direction_deg(np.array([1.0]), np.array([0.0]))
        assert abs(float(d[0]) - 270.0) < 1e-6

    def test_southerly(self):
        """v>0 (向北吹) = 来自南方 = 180°。"""
        d = ma.wind_direction_deg(np.array([0.0]), np.array([1.0]))
        assert abs(float(d[0]) - 180.0) < 1e-6

    def test_range_0_360(self):
        u = np.random.uniform(-10, 10, (32, 32))
        v = np.random.uniform(-10, 10, (32, 32))
        d = ma.wind_direction_deg(u, v)
        assert d.min() >= 0.0
        assert d.max() < 360.0


class TestReversal:
    def test_opposite_winds_180(self):
        rev = ma.direction_reversal(
            np.array([-5.0]), np.array([0.0]),   # 冬：东风
            np.array([5.0]), np.array([0.0]))     # 夏：西风
        assert abs(rev - 180.0) < 1e-6

    def test_same_winds_near_0(self):
        rev = ma.direction_reversal(
            np.array([5.0]), np.array([3.0]),
            np.array([5.0]), np.array([3.0]))
        assert rev < 1e-6

    def test_perpendicular_90(self):
        rev = ma.direction_reversal(
            np.array([5.0]), np.array([0.0]),
            np.array([0.0]), np.array([5.0]))
        assert abs(rev - 90.0) < 1e-6


class TestMonsoonIndex:
    def test_positive_when_summer_u_larger(self):
        n, H, W = 12, 4, 4
        u = np.zeros((n, H, W))
        u[5:8] = 8.0   # 夏季（6-8 月，索引 5-7）正 u
        u[0:2] = -6.0  # 冬季负 u
        mi = ma.monsoon_index(u, summer_idx=[5, 6, 7], winter_idx=[0, 1])
        assert np.all(mi > 0)

    def test_shape(self):
        u = np.random.randn(12, 8, 8)
        mi = ma.monsoon_index(u, summer_idx=[5, 6, 7], winter_idx=[0, 1, 11])
        assert mi.shape == (8, 8)


class TestConcentration:
    def test_all_in_monsoon(self):
        precip = np.zeros(12)
        precip[5:8] = 100.0
        r = ma.precipitation_concentration(precip, monsoon_idx=[5, 6, 7])
        assert abs(r["concentration"] - 1.0) < 1e-9
        assert r["seasonality"] > 0.3

    def test_uniform_low_concentration(self):
        precip = np.full(12, 50.0)
        r = ma.precipitation_concentration(precip, monsoon_idx=[5, 6, 7])
        assert abs(r["concentration"] - 0.25) < 1e-9
        assert r["seasonality"] < 1e-9

    def test_zero_precip(self):
        r = ma.precipitation_concentration(np.zeros(12), monsoon_idx=[5, 6])
        assert r["concentration"] == 0.0
        assert r["annual_total"] == 0.0


class TestOnsetRetreat:
    def test_ordered(self):
        # 季风型逐日降水：前段干、中段湿、后段干
        daily = np.zeros(365)
        daily[120:270] = np.linspace(0, 20, 150)
        daily[200:230] = 25.0
        r = ma.detect_onset_retreat(daily)
        assert r["onset_index"] < r["peak_index"] < r["retreat_index"]

    def test_empty_raises(self):
        with pytest.raises(ma.ValidationError):
            ma.detect_onset_retreat(np.array([]))

    def test_zero_precip_fallback(self):
        r = ma.detect_onset_retreat(np.zeros(100))
        assert r["onset_index"] == 0
        assert r["retreat_index"] == 99


class TestAnalyze:
    def test_east_asia_synthetic(self):
        met = ma.generate_synthetic([110, 20, 122, 40], region="east_asia", n_dates=24)
        res = ma.analyze_monsoon(met["u"], met["v"], met["precip_monthly"],
                                 met["precip_daily"], met["months"], "east_asia")
        # 风场强反转（接近 180°）
        assert res["reversal_angle_deg"] > 90.0
        # 季风期降水集中（占比 > 0.4）
        assert res["concentration"] > 0.4
        # 东亚夏季 u 为正 → 季风指数为正
        assert res["monsoon_index_mean"] > 0.0

    def test_south_asia_u_negative(self):
        met = ma.generate_synthetic([70, 8, 90, 30], region="south_asia", n_dates=24)
        res = ma.analyze_monsoon(met["u"], met["v"], met["precip_monthly"],
                                 met["precip_daily"], met["months"], "south_asia")
        # 南亚夏季西南风 → u 为负 → 季风指数为负
        assert res["monsoon_index_mean"] < 0.0
        assert res["reversal_angle_deg"] > 90.0

    def test_unknown_region_raises(self):
        met = ma.generate_synthetic([110, 20, 122, 40], region="east_asia", n_dates=24)
        with pytest.raises(ma.UsageError):
            ma.analyze_monsoon(met["u"], met["v"], met["precip_monthly"],
                               met["precip_daily"], met["months"], "antarctica")


class TestSynthetic:
    def test_shapes(self):
        met = ma.generate_synthetic([110, 20, 122, 40], n_dates=24)
        assert met["u"].shape == (24, 64, 64)
        assert met["precip_daily"].shape == (365,)
        assert len(met["months"]) == 24

    def test_bad_region_raises(self):
        with pytest.raises(ma.UsageError):
            ma.generate_synthetic([110, 20, 122, 40], region="mars")


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(-5, 5, (2, 16, 16)).astype(np.float32)
        bbox = [110.0, 20.0, 122.0, 40.0]
        path = str(tmp_path / "w.tif")
        ma.write_geotiff(path, cube, bbox)
        back, rb = ma.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(ma.UsageError):
            ma.read_geotiff("/nonexistent/w.tif")
