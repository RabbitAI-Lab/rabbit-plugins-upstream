"""Core algorithm tests for lidar-terrain-modeling."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestTerrain:
    def test_bounded(self):
        x = np.linspace(0, 1000, 50)
        y = np.linspace(0, 1000, 50)
        z = mod.terrain_z(x, y, 1000.0, 1000.0)
        assert z.min() > 50
        assert z.max() < 160

    def test_grid_dims_cap(self):
        # 1 degree bbox (~111km) with 1m resolution must be capped
        n_cols, n_rows, rx, ry = mod.grid_dims([116, 39, 117, 40], 1.0)
        assert n_cols <= mod.MAX_DIM
        assert n_rows <= mod.MAX_DIM
        assert rx > 1.0  # resolution enlarged to fit cap


class TestInterpolation:
    def _plane_points(self, n=400):
        rng = np.random.default_rng(0)
        x = rng.uniform(0, 100, n)
        y = rng.uniform(0, 100, n)
        z = 2.0 * x + 3.0 * y + 10.0   # plane
        return np.column_stack([x, y, z])

    def test_idw_recovers_plane(self):
        pts = self._plane_points()
        # 用内部节点（角点邻域不对称，IDW 无法精确复现平面，属正常现象）
        nodes = np.array([[50.0, 50.0], [40.0, 60.0], [70.0, 30.0]])
        out = mod.idw_interpolate(pts, nodes, k=12)
        expected = 2.0 * nodes[:, 0] + 3.0 * nodes[:, 1] + 10.0
        np.testing.assert_allclose(out, expected, rtol=0.08)

    def test_tin_recovers_plane(self):
        pts = self._plane_points()
        nodes = np.array([[50.0, 50.0], [30.0, 60.0]])
        out = mod.tin_interpolate(pts, nodes)
        expected = 2.0 * nodes[:, 0] + 3.0 * nodes[:, 1] + 10.0
        np.testing.assert_allclose(out, expected, atol=1e-3)


class TestSlopeAspect:
    def test_flat_zero_slope(self):
        dem = np.full((10, 10), 50.0, dtype=np.float32)
        slope, aspect = mod.slope_aspect(dem, 1.0, 1.0)
        assert np.allclose(slope, 0.0, atol=1e-3)
        assert np.all(aspect == -1.0)   # flat → nodata aspect

    def test_plane_tilt_east(self):
        # 高程随东(列)减小 → 下坡朝东，坡向≈90°
        cols = np.arange(20, dtype=float)
        dem = np.tile(-cols, (20, 1)).astype(np.float32)  # z = -x
        slope, aspect = mod.slope_aspect(dem, 1.0, 1.0)
        # 内部像元坡度≈45°
        assert 44.0 < slope[10, 10] < 46.0
        assert 85.0 < aspect[10, 10] < 95.0

    def test_plane_tilt_north(self):
        # z = -row：北(row0)高、南低 → 下坡朝南，坡向≈180°
        rows = np.arange(20, dtype=float)
        dem = np.tile(-rows[:, None], (1, 20)).astype(np.float32)
        slope, aspect = mod.slope_aspect(dem, 1.0, 1.0)
        assert 170.0 < aspect[10, 10] < 190.0


class TestRasterize:
    def test_rasterize_shape(self):
        rng = np.random.default_rng(1)
        pts = np.column_stack([rng.uniform(0, 100, 500),
                               rng.uniform(0, 100, 500),
                               rng.uniform(0, 50, 500)])
        dem, nc, nr, rx, ry = mod.rasterize(pts, [0, 0, 1, 1], 1.0, method="idw")
        assert dem.shape == (nr, nc)
        assert np.isfinite(dem).all()

    def test_unknown_method_raises(self):
        pts = np.random.uniform(0, 10, (20, 3))
        with pytest.raises(mod.UsageError):
            mod.rasterize(pts, [0, 0, 1, 1], 1.0, method="spline")


class TestSyntheticIntegration:
    def test_dem_matches_truth(self):
        bbox = [116.0, 39.0, 116.02, 39.01]
        points, info = mod.generate_synthetic(bbox, 1.0, seed=7)
        dem, nc, nr, rx, ry = mod.rasterize(points, bbox, 1.0, method="idw")
        xs, ys, _, _ = mod.grid_nodes(bbox, nc, nr)
        XX, YY = np.meshgrid(xs, ys)
        truth = mod.terrain_z(XX, YY, info["width_m"], info["height_m"])
        rmse = float(np.sqrt(np.mean((dem - truth) ** 2)))
        assert rmse < 1.0   # 平滑地形，IDW 重建精度高
        slope, aspect = mod.slope_aspect(dem, rx, ry)
        assert slope.mean() > 0
        assert slope.max() < 60   # 合理坡度范围

    def test_tin_matches_truth(self):
        bbox = [116.0, 39.0, 116.02, 39.01]
        points, info = mod.generate_synthetic(bbox, 1.0, seed=9)
        dem, nc, nr, rx, ry = mod.rasterize(points, bbox, 1.0, method="tin")
        xs, ys, _, _ = mod.grid_nodes(bbox, nc, nr)
        XX, YY = np.meshgrid(xs, ys)
        truth = mod.terrain_z(XX, YY, info["width_m"], info["height_m"])
        rmse = float(np.sqrt(np.mean((dem - truth) ** 2)))
        assert rmse < 1.5
