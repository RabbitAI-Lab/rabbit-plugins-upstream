"""Core algorithm tests for viewshed-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestCurvature:
    def test_zero_at_origin(self):
        assert mod.curvature_correction(np.array([0.0]))[0] == 0.0

    def test_increases_with_distance(self):
        d = np.array([100.0, 1000.0, 10000.0])
        c = mod.curvature_correction(d)
        assert np.all(np.diff(c) > 0)

    def test_magnitude_reasonable(self):
        # 10km 处曲率下降约 d^2/(2R) ≈ 10000^2/(2*6371000) ≈ 7.85 m
        c = mod.curvature_correction(np.array([10000.0]), k=0.0)[0]
        assert abs(c - 7.85) < 0.5


class TestViewshedSingle:
    def test_observer_sees_itself(self):
        dem = np.zeros((10, 10), dtype=np.float32)
        vis = mod.viewshed_single(dem, (5, 5))
        assert vis[5, 5]

    def test_flat_terrain_full_visible(self):
        """完全平坦地形上观察点应看到所有像元。"""
        dem = np.zeros((15, 15), dtype=np.float32)
        vis = mod.viewshed_single(dem, (7, 7), curvature=False)
        assert vis.all()

    def test_wall_blocks_behind(self):
        """观察点一侧有高墙，墙后像元应不可见。"""
        dem = np.zeros((21, 21), dtype=np.float32)
        # 在 col=11 建一堵高墙
        dem[:, 11] = 500.0
        obs = (10, 5)  # 观察点在墙左侧
        vis = mod.viewshed_single(dem, obs, curvature=False)
        # 墙本身可见
        assert vis[10, 11]
        # 墙右侧远处（同排）应被遮挡
        assert not vis[10, 18]

    def test_high_peak_sees_more(self):
        """站在高处比站在低处看到更多。"""
        dem = np.zeros((21, 21), dtype=np.float32)
        dem[5:16, 5:16] = 50.0  # 中央台地
        vis_low = mod.viewshed_single(dem, (0, 0), observer_height=0.0, curvature=False)
        vis_high = mod.viewshed_single(dem, (0, 0), observer_height=200.0, curvature=False)
        assert vis_high.sum() >= vis_low.sum()

    def test_out_of_bounds_raises(self):
        dem = np.zeros((5, 5), dtype=np.float32)
        with pytest.raises(mod.ValidationError):
            mod.viewshed_single(dem, (99, 99))


class TestViewshedMulti:
    def test_count_accumulates(self):
        dem = np.zeros((15, 15), dtype=np.float32)
        observers = [(7, 7), (3, 3)]
        count, any_vis = mod.viewshed_multi(dem, observers, curvature=False)
        # 平坦地形每个观察点看到全部 → count 全为 2
        assert count.max() == 2
        assert any_vis.all()

    def test_any_visible_union(self):
        dem = np.zeros((10, 10), dtype=np.float32)
        _, any_vis = mod.viewshed_multi(dem, [(5, 5)], curvature=False)
        assert any_vis.dtype == bool


class TestSynthetic:
    def test_shapes(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40], grid_size=32)
        assert dem.shape == (32, 32)
        assert "elev_range" in info

    def test_has_peak(self):
        dem, _ = mod.generate_synthetic([116, 39, 117, 40], grid_size=32)
        assert dem.max() > 500  # 中央山峰


class TestParseObservers:
    def test_default(self):
        obs = mod._parse_observers(None, 20, 20)
        assert len(obs) == 3

    def test_custom(self):
        obs = mod._parse_observers("5,5;10,10", 20, 20)
        assert obs == [(5, 5), (10, 10)]

    def test_out_of_bounds_raises(self):
        with pytest.raises(mod.UsageError):
            mod._parse_observers("99,99", 10, 10)
