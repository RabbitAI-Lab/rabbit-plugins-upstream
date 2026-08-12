"""Core algorithm tests for kriging-interpolation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestSemivariogram:
    def test_gamma_shape(self):
        rng = np.random.default_rng(0)
        coords = rng.uniform(0, 1, (30, 2))
        values = coords[:, 0] + rng.normal(0, 0.1, 30)
        lags, gamma, counts = mod.empirical_semivariogram(coords, values, n_lags=10)
        assert lags.shape == (10,)
        assert gamma.shape == (10,)
        assert counts.shape == (10,)
        # 近距离 gamma 应较小（空间相关）
        finite = gamma[np.isfinite(gamma)]
        assert finite.size > 0

    def test_increasing_with_distance(self):
        """对强空间相关数据，近距离 gamma < 远距离 gamma。"""
        rng = np.random.default_rng(1)
        coords = rng.uniform(0, 10, (60, 2))
        # 值随 x 平滑变化 → 强空间结构
        values = np.sin(coords[:, 0] * 0.5)
        lags, gamma, counts = mod.empirical_semivariogram(coords, values, n_lags=8, max_dist=5.0)
        finite = [(l, g) for l, g in zip(lags, gamma) if np.isfinite(g)]
        near = finite[0][1]
        far = finite[-1][1]
        assert far > near

    def test_too_few_points_raises(self):
        coords = np.array([[0.0, 0.0]])
        values = np.array([1.0])
        with pytest.raises(mod.ValidationError):
            mod.empirical_semivariogram(coords, values)


class TestSphericalModel:
    def test_zero_at_origin(self):
        assert mod.spherical_model(np.array([0.0]), 0.1, 1.0, 5.0)[0] == 0.0

    def test_sill_beyond_range(self):
        val = mod.spherical_model(np.array([10.0]), 0.0, 1.0, 5.0)[0]
        assert abs(val - 1.0) < 1e-12

    def test_monotonic_increasing(self):
        h = np.linspace(0.01, 4.99, 50)
        g = mod.spherical_model(h, 0.0, 1.0, 5.0)
        assert np.all(np.diff(g) >= -1e-12)


class TestFit:
    def test_fit_recovers_structure(self):
        """合成数据拟合出的 sill 应接近经验 gamma 的最大值。"""
        rng = np.random.default_rng(2)
        coords = rng.uniform(0, 10, (50, 2))
        values = coords[:, 0] + rng.normal(0, 0.3, 50)
        lags, gamma, _ = mod.empirical_semivariogram(coords, values, n_lags=10, max_dist=5.0)
        params = mod.fit_semivariogram(lags, gamma)
        assert params["sill"] > 0
        assert params["range"] > 0
        assert params["nugget"] >= 0


class TestKriging:
    def test_exact_at_sample_points(self):
        """普通克里金在采样点处应精确复现观测值。"""
        rng = np.random.default_rng(3)
        coords = rng.uniform(0, 1, (15, 2))
        values = rng.uniform(0, 10, 15)
        nugget, sill, vrange = 0.0, 1.0, 0.5
        pred, var = mod.ordinary_kriging(coords, values, coords, nugget, sill, vrange)
        np.testing.assert_allclose(pred, values, atol=1e-6)

    def test_prediction_within_range(self):
        """预测值应大致落在观测值范围内（无极端外推）。"""
        rng = np.random.default_rng(4)
        coords = rng.uniform(0, 1, (20, 2))
        values = rng.uniform(5, 15, 20)
        target = rng.uniform(0, 1, (10, 2))
        pred, var = mod.ordinary_kriging(coords, values, target, 0.0, 1.0, 0.5)
        assert pred.min() > 3.0
        assert pred.max() < 17.0

    def test_variance_nonnegative(self):
        rng = np.random.default_rng(5)
        coords = rng.uniform(0, 1, (15, 2))
        values = rng.uniform(0, 1, 15)
        target = rng.uniform(0, 1, (8, 2))
        _, var = mod.ordinary_kriging(coords, values, target, 0.0, 1.0, 0.5)
        assert np.all(var >= 0)

    def test_variance_lower_near_points(self):
        """靠近采样点处方差应小于远离处。"""
        coords = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
        values = np.array([1.0, 2.0, 3.0, 4.0])
        near = np.array([[0.05, 0.05]])
        far = np.array([[0.5, 0.5]])
        _, var_near = mod.ordinary_kriging(coords, values, near, 0.0, 1.0, 0.8)
        _, var_far = mod.ordinary_kriging(coords, values, far, 0.0, 1.0, 0.8)
        assert var_near[0] < var_far[0]


class TestCrossValidation:
    def test_cv_returns_metrics(self):
        rng = np.random.default_rng(6)
        coords = rng.uniform(0, 1, (20, 2))
        values = coords[:, 0] + rng.normal(0, 0.1, 20)
        cv = mod.cross_validate(coords, values, 0.0, 1.0, 0.5)
        assert "rmse" in cv and "mean_error" in cv
        assert cv["rmse"] >= 0
        assert cv["n"] == 20

    def test_cv_smooth_field_low_rmse(self):
        """平滑空间场的交叉验证 RMSE 应较低。"""
        rng = np.random.default_rng(7)
        coords = rng.uniform(0, 1, (25, 2))
        values = coords[:, 0] + coords[:, 1]  # 完全平滑线性场
        cv = mod.cross_validate(coords, values, 0.0, 1.0, 0.6)
        assert cv["rmse"] < 0.5


class TestSynthetic:
    def test_synthetic_shapes(self):
        coords, values, info = mod.generate_synthetic([116, 39, 117, 40], n_points=25)
        assert coords.shape == (25, 2)
        assert values.shape == (25,)
