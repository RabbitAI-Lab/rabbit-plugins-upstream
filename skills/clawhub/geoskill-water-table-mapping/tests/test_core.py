"""Core algorithm tests for water-table-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestIDW:
    def test_exact_at_points(self):
        pts = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0]])
        vals = np.array([10.0, 20.0, 30.0])
        out = mod.idw_interpolate(pts, vals, pts)
        np.testing.assert_allclose(out, vals, atol=1e-6)

    def test_within_range_convex(self):
        rng = np.random.default_rng(0)
        pts = rng.uniform(0, 1, (12, 2))
        vals = rng.uniform(5, 15, 12)
        targets = rng.uniform(0, 1, (50, 2))
        out = mod.idw_interpolate(pts, vals, targets)
        assert out.min() >= vals.min() - 1e-6
        assert out.max() <= vals.max() + 1e-6

    def test_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.idw_interpolate(np.zeros((3, 2)), np.zeros(2), np.zeros((5, 2)))


class TestVariogram:
    def test_zero_at_origin(self):
        g = mod.exponential_variogram(np.array([0.0]), sill=1.0, range_a=1.0, nugget=0.0)
        assert abs(g[0]) < 1e-12

    def test_monotonic_to_sill(self):
        h = np.linspace(0, 10, 50)
        g = mod.exponential_variogram(h, sill=2.0, range_a=2.0, nugget=0.0)
        assert np.all(np.diff(g) >= -1e-9)
        assert g[-1] < 2.0 + 1e-6
        assert g[-1] > 1.5  # 接近 sill

    def test_fit_params_positive(self):
        rng = np.random.default_rng(1)
        pts = rng.uniform(0, 10, (20, 2))
        vals = pts[:, 0] * 2 + rng.normal(0, 0.5, 20)  # 空间相关
        sill, range_a = mod.fit_variogram_params(pts, vals)
        assert sill > 0
        assert range_a > 0


class TestKriging:
    def test_exact_at_points(self):
        """普通克里金（nugget=0）在数据点处应精确复现观测值。"""
        pts = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.5, 0.5]])
        vals = np.array([10.0, 12.0, 11.0, 13.0, 11.5])
        sill, range_a = mod.fit_variogram_params(pts, vals)
        out = mod.ordinary_kriging(pts, vals, pts, sill, range_a, nugget=0.0)
        np.testing.assert_allclose(out, vals, atol=1e-3)

    def test_smooth_prediction_in_range(self):
        rng = np.random.default_rng(2)
        pts = rng.uniform(0, 1, (15, 2))
        vals = 20 - 5 * pts[:, 0] + rng.normal(0, 0.2, 15)
        sill, range_a = mod.fit_variogram_params(pts, vals)
        targets = rng.uniform(0, 1, (30, 2))
        out = mod.ordinary_kriging(pts, vals, targets, sill, range_a)
        assert np.all(np.isfinite(out))
        # 预测应在观测范围附近（克里金可轻微外推，放宽边界）
        assert out.min() > vals.min() - 3
        assert out.max() < vals.max() + 3


class TestCrossValidation:
    def test_cv_metrics(self):
        rng = np.random.default_rng(3)
        pts = rng.uniform(0, 1, (20, 2))
        vals = 30 - 8 * pts[:, 0] - 4 * pts[:, 1] + rng.normal(0, 0.2, 20)
        cv = mod.leave_one_out_cv(pts, vals, "idw")
        assert cv["rmse"] >= 0
        assert cv["r2"] > 0.5  # 强空间趋势，IDW 应拟合良好

    def test_cv_too_few_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.leave_one_out_cv(np.zeros((2, 2)), np.zeros(2), "idw")

    def test_unknown_method_raises(self):
        with pytest.raises(mod.UsageError):
            mod.interpolate_at(np.zeros((3, 2)), np.zeros(3), np.zeros((1, 2)), "bad", 1.0, 1.0)


class TestSynthetic:
    def test_shapes_and_constraint(self):
        info = mod.generate_synthetic([116, 39, 117, 40], n_wells=30, grid_shape=(24, 24))
        assert info["points"].shape == (30, 2)
        assert info["levels"].shape == (30,)
        assert info["level_field"].shape == (24, 24)
        # 真值水位必须低于 DEM
        assert np.all(info["level_field"] < info["dem"])

    def test_interpolation_recovers_truth(self):
        """合成 + IDW 插值应高度还原真值场。"""
        info = mod.generate_synthetic([116, 39, 117, 40], n_wells=60, grid_shape=(32, 32), noise=0.1, seed=9)
        targets = mod._grid_targets(info["bbox"], (32, 32))
        grid = mod.idw_interpolate(info["points"], info["levels"], targets).reshape(32, 32)
        corr = np.corrcoef(grid.ravel(), info["level_field"].ravel())[0, 1]
        assert corr > 0.95
        rmse = np.sqrt(np.mean((grid - info["level_field"]) ** 2))
        assert rmse < 1.5


class TestCSVAndIO:
    def test_read_wells_csv(self, tmp_path):
        p = str(tmp_path / "w.csv")
        with open(p, "w", newline="", encoding="utf-8") as f:
            f.write("lon,lat,water_level\n116.1,39.1,42.0\n116.5,39.5,40.0\n116.9,39.9,38.0\n")
        pts, vals = mod.read_wells_csv(p)
        assert pts.shape == (3, 2)
        np.testing.assert_allclose(vals, [42.0, 40.0, 38.0])

    def test_read_wells_missing_columns_raises(self, tmp_path):
        p = str(tmp_path / "bad.csv")
        with open(p, "w", newline="", encoding="utf-8") as f:
            f.write("a,b,c\n1,2,3\n")
        with pytest.raises(mod.ValidationError):
            mod.read_wells_csv(p)

    def test_read_wells_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_wells_csv("/nonexistent/w.csv")

    def test_geotiff_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 50, (1, 12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back, arr, atol=1e-4)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_tif_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
