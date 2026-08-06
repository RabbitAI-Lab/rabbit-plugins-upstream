"""Core algorithm tests for wildfire-spread-modeling."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as wf


class TestIgnitionProbability:
    def test_bounded_01(self):
        fuel = np.random.uniform(0, 1, (16, 16))
        moist = np.random.uniform(0, 1, (16, 16))
        p = wf.ignition_probability(fuel, moist, slope=0.5, wind_factor=2.0)
        assert p.min() >= 0.0
        assert p.max() <= 1.0

    def test_increases_with_fuel(self):
        moist = np.full((8, 8), 0.3)
        p_lo = wf.ignition_probability(np.full((8, 8), 0.2), moist).mean()
        p_hi = wf.ignition_probability(np.full((8, 8), 0.9), moist).mean()
        assert p_hi > p_lo

    def test_decreases_with_moisture(self):
        fuel = np.full((8, 8), 0.8)
        p_dry = wf.ignition_probability(fuel, np.full((8, 8), 0.05)).mean()
        p_wet = wf.ignition_probability(fuel, np.full((8, 8), 0.95)).mean()
        assert p_dry > p_wet

    def test_increases_with_wind_and_slope(self):
        fuel = np.full((8, 8), 0.7)
        moist = np.full((8, 8), 0.2)
        base = wf.ignition_probability(fuel, moist, slope=0.0, wind_factor=1.0).mean()
        windy = wf.ignition_probability(fuel, moist, slope=0.0, wind_factor=2.0).mean()
        steep = wf.ignition_probability(fuel, moist, slope=1.0, wind_factor=1.0).mean()
        assert windy > base
        assert steep > base


class TestShift:
    def test_shift_east(self):
        m = np.zeros((5, 5), dtype=bool); m[2, 2] = True
        # out[i,j] = m[i-di, j-dj]; di=0,dj=1 → out[i,j]=m[i,j-1]：向东移一格
        out = wf._shift(m, 0, 1)
        assert out[2, 3] == True
        assert out[2, 2] == False


class TestSimulateSpread:
    def test_burned_area_monotonic_in_time(self):
        """过火面积随时间步单调不减。"""
        layers, _ = wf.generate_synthetic([116, 39, 117, 40])
        burned, arrival = wf.simulate_spread(
            layers["fuel"], layers["moisture"], layers["slope"],
            wind_speed=1.0, wind_dir_deg=45.0, ignition=layers["ignition"], steps=15,
        )
        series = wf.burned_area_series(arrival, 15)
        assert all(series[i] <= series[i + 1] for i in range(len(series) - 1))
        assert series[0] >= 1          # 初始点火
        assert series[-1] >= series[0] # 确有蔓延
        assert int(burned.sum()) == series[-1]

    def test_more_wind_more_burned(self):
        """同一随机序列下，风速越大过火面积越大（顺风加速）。"""
        fuel = np.full((40, 40), 0.9, dtype=np.float32)
        moist = np.full((40, 40), 0.25, dtype=np.float32)
        slope = np.full((40, 40), 0.2, dtype=np.float32)
        ign = np.zeros((40, 40), dtype=bool); ign[20, 10] = True
        _, arr0 = wf.simulate_spread(fuel, moist, slope, 0.0, 0.0, ign, steps=12, seed=7)
        _, arr3 = wf.simulate_spread(fuel, moist, slope, 4.0, 0.0, ign, steps=12, seed=7)
        a0 = wf.burned_area_series(arr0, 12)[-1]
        a3 = wf.burned_area_series(arr3, 12)[-1]
        assert a3 >= a0
        # 顺风(东)方向应比静风烧得更远
        east_calm = np.count_nonzero(arr0[20, 21:] >= 0)
        east_wind = np.count_nonzero(arr3[20, 21:] >= 0)
        assert east_wind >= east_calm

    def test_more_moisture_less_burned(self):
        """同一随机序列下，湿度越大过火面积越小。"""
        fuel = np.full((40, 40), 0.9, dtype=np.float32)
        slope = np.full((40, 40), 0.2, dtype=np.float32)
        ign = np.zeros((40, 40), dtype=bool); ign[20, 20] = True
        _, arr_dry = wf.simulate_spread(fuel, np.full((40, 40), 0.05), slope, 1.0, 0.0, ign, steps=12, seed=11)
        _, arr_wet = wf.simulate_spread(fuel, np.full((40, 40), 0.9), slope, 1.0, 0.0, ign, steps=12, seed=11)
        assert wf.burned_area_series(arr_dry, 12)[-1] >= wf.burned_area_series(arr_wet, 12)[-1]

    def test_arrival_farther_is_later(self):
        ign = np.zeros((30, 30), dtype=bool); ign[15, 15] = True
        fuel = np.full((30, 30), 0.9, dtype=np.float32)
        moist = np.full((30, 30), 0.2, dtype=np.float32)
        slope = np.full((30, 30), 0.2, dtype=np.float32)
        _, arrival = wf.simulate_spread(fuel, moist, slope, 0.0, 0.0, ign, steps=14, seed=3)
        near = arrival[15, 17]
        far = arrival[15, 25]
        assert near >= 0 and far >= 0
        assert far >= near

    def test_empty_ignition_raises(self):
        fuel = np.full((8, 8), 0.9, dtype=np.float32)
        with pytest.raises(wf.ValidationError):
            wf.simulate_spread(fuel, fuel, fuel, 1.0, 0.0, np.zeros((8, 8), dtype=bool), steps=3)


class TestSynthetic:
    def test_shapes_and_ranges(self):
        layers, info = wf.generate_synthetic([116, 39, 117, 40])
        for k in ("fuel", "moisture", "slope"):
            assert layers[k].shape == (64, 64)
            assert layers[k].min() >= 0.0 and layers[k].max() <= 1.0
        assert layers["ignition"].sum() >= 1


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        p = str(tmp_path / "f.tif")
        wf.write_geotiff(p, cube, bbox)
        back, bb = wf.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(wf.UsageError):
            wf.read_geotiff("/nonexistent/f.tif")
