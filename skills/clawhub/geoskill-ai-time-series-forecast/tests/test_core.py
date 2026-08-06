"""Core algorithm tests for ai-time-series-forecast."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestFitLinear:
    def test_exact_line(self):
        t = np.arange(10, dtype=float)
        y = 3.0 * t + 7.0
        slope, intercept = mod.fit_linear(t, y)
        assert slope == pytest.approx(3.0)
        assert intercept == pytest.approx(7.0)

    def test_too_few_points(self):
        with pytest.raises(mod.ValidationError):
            mod.fit_linear(np.array([0.0]), np.array([1.0]))

    def test_degenerate_t(self):
        with pytest.raises(mod.ValidationError):
            mod.fit_linear(np.array([5.0, 5.0]), np.array([1.0, 2.0]))


class TestFitPolynomial:
    def test_exact_quadratic(self):
        t = np.arange(20, dtype=float)
        y = 2.0 * t ** 2 - 3.0 * t + 1.0
        coeffs = mod.fit_polynomial(t, y, degree=2)
        np.testing.assert_allclose(coeffs, [2.0, -3.0, 1.0], atol=1e-6)
        np.testing.assert_allclose(mod.eval_polynomial(coeffs, t), y, atol=1e-6)

    def test_bad_degree(self):
        with pytest.raises(mod.UsageError):
            mod.fit_polynomial(np.arange(5.0), np.arange(5.0), degree=0)

    def test_too_few_for_degree(self):
        with pytest.raises(mod.ValidationError):
            mod.fit_polynomial(np.arange(2.0), np.arange(2.0), degree=2)


class TestFitAR:
    def test_recovers_ar1(self):
        rng = np.random.default_rng(0)
        n = 2000
        y = np.zeros(n)
        for i in range(1, n):
            y[i] = 0.8 * y[i - 1] + rng.normal(0, 0.1)
        coefs = mod.fit_ar(y, order=1)
        assert coefs[0] == pytest.approx(0.8, abs=0.05)

    def test_bad_order(self):
        with pytest.raises(mod.UsageError):
            mod.fit_ar(np.arange(10.0), order=0)

    def test_too_short(self):
        with pytest.raises(mod.ValidationError):
            mod.fit_ar(np.array([1.0, 2.0]), order=2)


class TestForecastAR:
    def test_constant_series_stays_constant(self):
        y = np.full(10, 5.0)
        coefs = mod.fit_ar(y, order=2)  # 常数序列：系数和应 ≈ 1
        fc = mod.forecast_ar(y, coefs, steps=5)
        np.testing.assert_allclose(fc, 5.0, atol=1e-6)

    def test_ar1_decays_toward_zero(self):
        y = np.array([1.0])
        coefs = np.array([0.5])
        fc = mod.forecast_ar(y, coefs, steps=3)
        np.testing.assert_allclose(fc, [0.5, 0.25, 0.125], atol=1e-9)

    def test_history_too_short(self):
        with pytest.raises(mod.ValidationError):
            mod.forecast_ar(np.array([1.0]), np.array([0.5, 0.3]), steps=2)

    def test_bad_steps(self):
        with pytest.raises(mod.UsageError):
            mod.forecast_ar(np.arange(5.0), np.array([0.5]), steps=0)


class TestEvaluateForecast:
    def test_hand_computed(self):
        fc = np.array([1.0, 2.0, 3.0])
        actual = np.array([2.0, 2.0, 5.0])  # 误差 [-1, 0, -2]
        m = mod.evaluate_forecast(fc, actual)
        assert m["mae"] == pytest.approx(1.0)
        assert m["rmse"] == pytest.approx(np.sqrt(5.0 / 3.0))
        assert m["n"] == 3

    def test_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.evaluate_forecast(np.array([1.0]), np.array([1.0, 2.0]))


class TestForecastSeries:
    def test_linear_trend_holdout(self):
        t = np.arange(30, dtype=float)
        y = 2.0 * t + 5.0 + np.random.default_rng(1).normal(0, 0.01, 30)
        res = mod.forecast_series(y, method="linear", horizon=5)
        assert res["metrics"]["rmse"] < 0.05
        assert res["forecast"].size == 5
        assert res["train_len"] == 25

    def test_poly_method(self):
        t = np.arange(30, dtype=float)
        y = 0.05 * t ** 2 + 1.0
        res = mod.forecast_series(y, method="poly", degree=2, horizon=5)
        assert res["metrics"]["rmse"] < 1e-3

    def test_ar_method(self):
        rng = np.random.default_rng(2)
        y = np.zeros(100)
        for i in range(1, 100):
            y[i] = 0.7 * y[i - 1] + rng.normal(0, 0.1)
        res = mod.forecast_series(y, method="ar", order=1, horizon=3)
        assert res["forecast"].size == 3
        assert "ar_coefficients" in res["model_params"]

    def test_unknown_method(self):
        with pytest.raises(mod.UsageError):
            mod.forecast_series(np.arange(20.0), method="prophet")

    def test_series_too_short(self):
        with pytest.raises(mod.ValidationError):
            mod.forecast_series(np.arange(5.0), horizon=4)


class TestForecastCube:
    def test_shapes(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40], n_steps=20, seed=3)
        fc, rmse = mod.forecast_cube(cube, method="linear", horizon=4)
        assert fc.shape == (4, 48, 48)
        assert rmse.shape == (48, 48)

    def test_linear_low_error_on_trend(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40], n_steps=20, seed=5)
        fc, rmse = mod.forecast_cube(cube, method="linear", horizon=4)
        # 趋势+季节+噪声：线性拟合留出 RMSE 应较小
        assert np.mean(rmse) < 0.1

    def test_ar_cube_runs(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40], n_steps=16, seed=6)
        fc, rmse = mod.forecast_cube(cube, method="ar", horizon=3, order=2)
        assert fc.shape == (3, 48, 48)
        assert np.isfinite(fc).all()

    def test_bad_shape_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.forecast_cube(np.zeros((10, 10)), horizon=2)

    def test_short_series_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.forecast_cube(np.zeros((5, 4, 4)), horizon=4)


class TestSynthetic:
    def test_shape_and_range(self):
        cube, info = mod.generate_synthetic([116, 39, 117, 40], n_steps=24)
        assert cube.shape == (24, 48, 48)
        assert cube.min() >= 0.0 and cube.max() <= 1.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "fc.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == (3, 16, 16)
        np.testing.assert_allclose(back, arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
