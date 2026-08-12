"""Core algorithm tests for snowmelt-runoff-modeling."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as sm


class TestDegreeDayMelt:
    def test_zero_below_threshold(self):
        """气温低于 T_base 时融雪为 0。"""
        temp = np.array([-5.0, -1.0, 0.0])
        melt = sm.degree_day_melt(temp, ddf=4.0, t_base=0.0)
        assert np.allclose(melt, 0.0)

    def test_linear_above_threshold(self):
        """M = DDF × (T − T_base)。"""
        melt = sm.degree_day_melt(np.array([5.0]), ddf=4.0, t_base=0.0)
        assert np.isclose(melt[0], 20.0)
        melt2 = sm.degree_day_melt(np.array([3.0]), ddf=4.0, t_base=1.0)
        assert np.isclose(melt2[0], 8.0)

    def test_increases_with_temp(self):
        temps = np.array([0.0, 2.0, 5.0, 10.0])
        melt = sm.degree_day_melt(temps, ddf=4.0)
        assert np.all(np.diff(melt) > 0)


class TestAirTempLapse:
    def test_higher_elevation_colder(self):
        dem = np.array([[500.0, 3000.0]], dtype=np.float32)
        t = sm.air_temp_at_elevation(10.0, dem, elev_ref=500.0, lapse=0.006)
        assert t[0, 0] > t[0, 1]
        # 2500 m 高差 → 15 °C 降幅
        assert np.isclose(t[0, 0] - t[0, 1], 15.0)


class TestSimulateSnowmelt:
    def test_water_conservation(self):
        """流域平均累积径流 == 平均径流深（水量守恒）。"""
        rng = np.random.default_rng(0)
        dem = rng.uniform(500, 3000, (16, 16))
        swe_init = rng.uniform(0, 200, (16, 16))
        temp_series = np.linspace(5, 15, 30)  # 足够暖，全部融化
        runoff_daily, snow_area, runoff_depth = sm.simulate_snowmelt(
            dem, temp_series, swe_init, ddf=4.0
        )
        assert np.isclose(np.sum(runoff_daily), np.mean(runoff_depth), rtol=1e-6)

    def test_full_melt_conserves_swe(self):
        """充分融化后，总径流 ≈ 初始总雪量。"""
        dem = np.full((8, 8), 1000.0)
        swe_init = np.full((8, 8), 100.0)
        temp_series = np.full(40, 20.0)  # 高温确保融尽
        runoff_daily, snow_area, runoff_depth = sm.simulate_snowmelt(
            dem, temp_series, swe_init, ddf=4.0
        )
        assert np.isclose(np.sum(runoff_daily), 100.0, rtol=1e-6)
        assert snow_area[-1] == 0.0
        assert np.allclose(runoff_depth, 100.0)

    def test_snow_area_nonincreasing(self):
        rng = np.random.default_rng(1)
        dem = rng.uniform(500, 3000, (16, 16))
        swe_init = rng.uniform(0, 300, (16, 16))
        temp_series = np.linspace(-2, 12, 40)
        _, snow_area, _ = sm.simulate_snowmelt(dem, temp_series, swe_init)
        assert np.all(np.diff(snow_area) <= 1e-9)

    def test_warmer_more_runoff(self):
        """更暖的气温序列 → 更大累积径流。"""
        rng = np.random.default_rng(2)
        dem = rng.uniform(500, 3000, (16, 16))
        swe_init = rng.uniform(50, 250, (16, 16))
        cold = np.linspace(-5, 3, 30)
        warm = np.linspace(0, 12, 30)
        r_cold, _, _ = sm.simulate_snowmelt(dem, cold, swe_init)
        r_warm, _, _ = sm.simulate_snowmelt(dem, warm, swe_init)
        assert np.sum(r_warm) > np.sum(r_cold)

    def test_no_melt_when_cold(self):
        """全程低于冰点 → 无径流，积雪面积不变。"""
        dem = np.full((8, 8), 1000.0)
        swe_init = np.full((8, 8), 100.0)
        temp_series = np.full(10, -10.0)
        runoff_daily, snow_area, runoff_depth = sm.simulate_snowmelt(
            dem, temp_series, swe_init
        )
        assert np.allclose(runoff_daily, 0.0)
        assert np.allclose(snow_area, 1.0)
        assert np.allclose(runoff_depth, 0.0)

    def test_shape_mismatch_raises(self):
        with pytest.raises(sm.ValidationError):
            sm.simulate_snowmelt(np.zeros((4, 4)), np.zeros(5), np.zeros((3, 3)))


class TestSnowmeltStats:
    def test_peak_and_totals(self):
        runoff = np.array([0.0, 1.0, 5.0, 2.0, 0.5])
        snow_area = np.array([1.0, 0.9, 0.6, 0.3, 0.1])
        depth = np.full((4, 4), 8.5 / 16 * 16)  # 任意
        swe_init = np.full((4, 4), 10.0)
        stats = sm.snowmelt_stats(runoff, snow_area, depth, swe_init)
        assert stats["n_days"] == 5
        assert stats["peak_day"] == 2
        assert np.isclose(stats["peak_runoff_mm_day"], 5.0)
        assert np.isclose(stats["total_runoff_mm"], 8.5)


class TestSynthetic:
    def test_shapes(self):
        dem, temp, swe, info = sm.generate_synthetic([116, 39, 117, 40], n_days=30)
        assert dem.shape == (128, 128)
        assert swe.shape == (128, 128)
        assert temp.size == 30
        assert info["n_days"] == 30

    def test_warming_drives_melt(self):
        """合成升温序列下，模拟应产生径流且积雪面积下降。"""
        dem, temp, swe, _ = sm.generate_synthetic([116, 39, 117, 40], n_days=60, seed=5)
        runoff_daily, snow_area, depth = sm.simulate_snowmelt(dem, temp, swe, ddf=4.0)
        assert np.sum(runoff_daily) > 0
        assert snow_area[-1] <= snow_area[0]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 100, (20, 20)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "depth.tif")
        sm.write_geotiff(path, arr, bbox)
        assert os.path.exists(path)
        back, rbbox = sm.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, arr, atol=1e-4)

    def test_read_missing_raises(self):
        with pytest.raises(sm.UsageError):
            sm.read_geotiff("/nonexistent/nope.tif")
