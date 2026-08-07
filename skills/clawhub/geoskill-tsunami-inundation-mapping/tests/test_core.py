"""Core algorithm tests for tsunami-inundation-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ts


class TestBathtub:
    def test_below_water_is_wet(self):
        dem = np.array([[0.0, 5.0], [20.0, 30.0]])
        m = ts.bathtub_mask(dem, 10.0)
        assert m.tolist() == [[True, True], [False, False]]


class TestConnectivity:
    def test_isolated_inland_pit_not_flooded(self):
        """孤立内陆洼地虽低于水位，但与海不连通 → 不被淹没。"""
        dem = np.full((32, 32), 50.0)
        dem[:, :6] = np.linspace(0, 8, 6)  # 海岸缓坡，全部 <10
        dem[14:18, 20:24] = 2.0            # 孤立洼地，<10 但被高地包围
        seed = np.zeros((32, 32), dtype=bool); seed[:, 0] = True
        inund = ts.inundation(dem, 10.0, seed)
        assert inund[16, 2] == True          # 海岸被淹
        assert inund[16, 22] == False        # 孤立洼地不被淹
        # 但 bathtub 本身会认为洼地是湿的（对照）
        assert ts.bathtub_mask(dem, 10.0)[16, 22] == True

    def test_no_seed_no_inundation(self):
        dem = np.zeros((8, 8))
        seed = np.zeros((8, 8), dtype=bool)  # 无海岸种子
        inund = ts.inundation(dem, 10.0, seed)
        assert not inund.any()


class TestDepth:
    def test_depth_non_negative(self):
        dem, _ = ts.generate_synthetic([120, 30, 121, 31])
        inund = ts.inundation(dem, 10.0)
        d = ts.water_depth(dem, 10.0, inund)
        assert d.min() >= 0.0

    def test_depth_equals_level_minus_dem_inside(self):
        dem = np.array([[2.0, 100.0]])
        inund = np.array([[True, False]])
        d = ts.water_depth(dem, 10.0, inund)
        assert abs(d[0, 0] - 8.0) < 1e-6
        assert d[0, 1] == 0.0

    def test_depth_monotonic_with_water_level(self):
        """水位升高 → 总淹没水深与最大水深单调不减。"""
        dem, _ = ts.generate_synthetic([120, 30, 121, 31], seed=3)
        prev_sum, prev_max = -1.0, -1.0
        for wl in (5, 10, 15, 20, 25):
            inund = ts.inundation(dem, wl)
            d = ts.water_depth(dem, wl, inund)
            assert d.sum() >= prev_sum - 1e-6
            assert d.max() >= prev_max - 1e-6
            prev_sum, prev_max = float(d.sum()), float(d.max())


class TestInundationArea:
    def test_area_monotonic_with_water_level(self):
        dem, _ = ts.generate_synthetic([120, 30, 121, 31])
        areas = [int(ts.inundation(dem, wl).sum()) for wl in (3, 8, 13, 18, 23)]
        assert all(areas[i] <= areas[i + 1] for i in range(len(areas) - 1))
        assert areas[-1] > areas[0]  # 确实随水位扩张


class TestArrival:
    def test_arrival_increases_with_distance(self):
        inund = np.zeros((32, 32), dtype=bool)
        inund[:, :20] = True
        seed = np.zeros((32, 32), dtype=bool); seed[:, 0] = True
        arr = ts.arrival_time(inund, seed, cell_size=10.0, wave_speed=5.0)
        assert arr.min() >= 0.0
        row = arr[16, :20]
        assert row[0] == 0.0
        assert np.all(np.diff(row) >= -1e-6)  # 随距离非减
        assert row[-1] > row[0]
        # 定量：距离 = 列号×像元，时间 = 距离/速度
        assert abs(row[5] - (5 * 10.0 / 5.0)) < 1e-4

    def test_arrival_zero_outside_inundation(self):
        inund = np.zeros((8, 8), dtype=bool); inund[:, :4] = True
        seed = np.zeros((8, 8), dtype=bool); seed[:, 0] = True
        arr = ts.arrival_time(inund, seed)
        assert np.allclose(arr[:, 4:], 0.0)


class TestEvacuation:
    def test_disjoint_from_inundation(self):
        dem, _ = ts.generate_synthetic([120, 30, 121, 31])
        inund = ts.inundation(dem, 10.0)
        evac = ts.evacuation_zone(dem, inund, 10.0, margin=5.0)
        assert not (evac & inund).any()

    def test_only_low_dry_ground(self):
        dem = np.array([[2.0, 12.0, 100.0]])
        inund = np.array([[True, False, False]])
        evac = ts.evacuation_zone(dem, inund, 10.0, margin=5.0)
        assert evac[0, 1] == True    # 干地但 12 < 15 临界
        assert evac[0, 2] == False   # 100 > 15 安全
        assert evac[0, 0] == False   # 已淹没


class TestSynthetic:
    def test_shape_and_dtype(self):
        dem, info = ts.generate_synthetic([120, 30, 121, 31])
        assert dem.shape == (64, 64)
        assert dem.dtype == np.float32
        assert info["max_elev"] > info["min_elev"]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        dem = np.random.uniform(0, 50, (16, 16)).astype(np.float32)
        bbox = [120.0, 30.0, 121.0, 31.0]
        p = str(tmp_path / "dem.tif")
        ts.write_geotiff(p, dem, bbox)
        back, bb, _res = ts.read_geotiff(p)
        assert back.shape == (1,) + dem.shape
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], dem, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ts.UsageError):
            ts.read_geotiff("/nonexistent/dem.tif")
