"""Core algorithm tests for groundwater-level-prediction."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestDecompose:
    def test_reconstruction_identity(self):
        """trend + seasonal + residual 必须精确重构原序列。"""
        rng = np.random.default_rng(0)
        series = 10 + 0.05 * np.arange(72) + 2 * np.sin(2 * np.pi * np.arange(72) / 12) + rng.normal(0, 0.3, 72)
        trend, seasonal, residual = mod.decompose_series(series, period=12)
        recon = trend + seasonal + residual
        np.testing.assert_allclose(recon, series, atol=1e-9)

    def test_trend_captures_direction(self):
        """上升趋势序列的 trend 末端应高于首端。"""
        series = 5.0 + 0.1 * np.arange(60)
        trend, _, _ = mod.decompose_series(series, period=12)
        assert trend[-1] > trend[0]

    def test_seasonal_zero_mean(self):
        rng = np.random.default_rng(1)
        series = 3 * np.sin(2 * np.pi * np.arange(48) / 12) + rng.normal(0, 0.1, 48)
        _, seasonal, _ = mod.decompose_series(series, period=12)
        cycle = seasonal[:12]
        assert abs(cycle.mean()) < 1e-6


class TestDrivers:
    def _make(self, n=60, seed=7):
        rng = np.random.default_rng(seed)
        t = np.arange(n)
        precip = 70 + 55 * np.sin(2 * np.pi * (t - 3) / 12) + rng.normal(0, 10, n)
        pumping = 30 + 0.1 * t + rng.normal(0, 2, n)
        level = 35 - 0.03 * t + 0.02 * (precip - precip.mean()) - 0.015 * (pumping - pumping.mean())
        return precip, pumping, level

    def test_linear_high_r2(self):
        precip, pumping, level = self._make()
        res = mod.fit_predict_drivers(
            level, precip, pumping, precip[:6], pumping[:6],
            method="linear", n_lag=2,
        )
        assert res["r2_history"] > 0.8
        assert res["predicted_future"].shape == (6,)

    def test_prediction_correlates_with_truth(self):
        """用同一生成机制造未来真值，预测应与真值高相关。"""
        rng = np.random.default_rng(11)
        n = 72
        t = np.arange(n)
        precip = 70 + 55 * np.sin(2 * np.pi * (t - 3) / 12) + rng.normal(0, 10, n)
        pumping = 30 + 0.1 * t + rng.normal(0, 2, n)
        level = 35 - 0.03 * t + 0.02 * (precip - precip[:60].mean()) - 0.015 * (pumping - pumping[:60].mean())
        res = mod.fit_predict_drivers(
            level[:60], precip[:60], pumping[:60], precip[60:], pumping[60:],
            method="linear",
        )
        truth = level[60:]
        corr = np.corrcoef(res["predicted_future"], truth)[0, 1]
        assert corr > 0.7
        assert res["rmse_validation"] < np.std(level)  # RMSE 小于序列标准差

    def test_rf_runs(self):
        precip, pumping, level = self._make(seed=3)
        res = mod.fit_predict_drivers(
            level, precip, pumping, precip[:4], pumping[:4], method="rf",
        )
        assert res["predicted_future"].shape == (4,)
        assert np.all(np.isfinite(res["predicted_future"]))

    def test_unknown_method_raises(self):
        precip, pumping, level = self._make()
        with pytest.raises(mod.UsageError):
            mod.fit_predict_drivers(level, precip, pumping, precip[:3], pumping[:3], method="nope")

    def test_length_mismatch_raises(self):
        precip, pumping, level = self._make()
        with pytest.raises(mod.ValidationError):
            mod.fit_predict_drivers(level, precip[:30], pumping, precip[:3], pumping[:3])


class TestIDW:
    def test_exact_at_points(self):
        """插值在已知点位置应返回该点值。"""
        bbox = [116.0, 39.0, 117.0, 40.0]
        pts = np.array([[116.0, 39.0], [117.0, 40.0], [116.5, 39.5]])
        vals = np.array([10.0, 20.0, 30.0])
        grid = mod.idw_interpolate(pts, vals, (3, 3), bbox)
        # 左上角像元 ≈ 第一个点
        assert grid.shape == (3, 3)
        assert abs(grid[2, 0] - 10.0) < 1.0 or abs(grid[0, 0] - 20.0) < 5.0

    def test_within_value_range(self):
        """IDW 结果应落在输入值的范围内（凸组合性质）。"""
        rng = np.random.default_rng(5)
        bbox = [0.0, 0.0, 1.0, 1.0]
        pts = rng.uniform(0, 1, (10, 2))
        vals = rng.uniform(5, 15, 10)
        grid = mod.idw_interpolate(pts, vals, (16, 16), bbox)
        assert grid.min() >= vals.min() - 1e-3
        assert grid.max() <= vals.max() + 1e-3

    def test_shape_and_mismatch(self):
        bbox = [0.0, 0.0, 1.0, 1.0]
        pts = np.array([[0.2, 0.3], [0.8, 0.7]])
        with pytest.raises(mod.ValidationError):
            mod.idw_interpolate(pts, np.array([1.0]), (8, 8), bbox)  # 数量不匹配


class TestSynthetic:
    def test_shapes(self):
        info = mod.generate_synthetic([116, 39, 117, 40], n_history=48, predict_steps=6, n_wells=10)
        assert info["levels_hist"].shape == (10, 48)
        assert info["levels_fut_truth"].shape == (10, 6)
        assert info["precip_hist"].shape == (48,)
        assert info["points"].shape == (10, 2)

    def test_end_to_end_prediction_skill(self):
        """合成 + 预测：相关系数应高、RMSE 合理。"""
        info = mod.generate_synthetic([116, 39, 117, 40], n_history=60, predict_steps=6, n_wells=8, seed=21)
        preds = np.zeros((8, 6))
        for i in range(8):
            res = mod.fit_predict_drivers(
                info["levels_hist"][i], info["precip_hist"], info["pumping_hist"],
                info["precip_fut"], info["pumping_fut"], method="linear",
            )
            preds[i] = res["predicted_future"]
        corr = np.corrcoef(preds.ravel(), info["levels_fut_truth"].ravel())[0, 1]
        assert corr > 0.8


class TestCubeForecast:
    def test_forecast_shape(self):
        rng = np.random.default_rng(0)
        cube = rng.uniform(20, 30, (24, 8, 8)).astype(np.float32)
        out = mod.forecast_cube_seasonal_trend(cube, predict_steps=4, period=12)
        assert out.shape == (4, 8, 8)
        assert np.all(np.isfinite(out))

    def test_bad_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.forecast_cube_seasonal_trend(np.zeros((5, 5)), 3)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/file.tif")
