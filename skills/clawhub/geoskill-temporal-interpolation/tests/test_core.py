"""Core algorithm tests for temporal-interpolation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestPhenologyCurve:
    def test_shape_and_range(self):
        curve = mod.phenology_curve(12)
        assert curve.shape == (12,)
        assert curve.min() >= 0.15
        assert curve.max() <= 0.85

    def test_summer_peak(self):
        """年中（夏季）应为峰值。"""
        curve = mod.phenology_curve(13)
        assert np.argmax(curve) == 6  # 中间点


class TestSavgolWindow:
    def test_odd_window(self):
        wl, po = mod._savgol_window(12, 5)
        assert wl == 5
        assert wl % 2 == 1
        assert po < wl

    def test_even_request_made_odd(self):
        wl, _ = mod._savgol_window(12, 6)
        assert wl % 2 == 1

    def test_window_capped_by_ndates(self):
        wl, po = mod._savgol_window(5, 99)
        assert wl <= 5
        assert po < wl


class TestSmoothTimeseries:
    def test_savgol_shape(self):
        cube = np.random.uniform(0.2, 0.8, (12, 8, 8)).astype(np.float32)
        sm, params = mod.smooth_timeseries(cube, method="savgol", window_length=5)
        assert sm.shape == cube.shape
        assert params["method"] == "savgol"

    def test_spline_shape(self):
        cube = np.random.uniform(0.2, 0.8, (10, 6, 6)).astype(np.float32)
        sm, params = mod.smooth_timeseries(cube, method="spline")
        assert sm.shape == cube.shape
        assert params["method"] == "spline"

    def test_savgol_reduces_noise(self):
        """平滑后相对真值的 RMSE 应低于含噪声观测。"""
        noisy, info = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=12)
        clean = info["clean"]
        sm, _ = mod.smooth_timeseries(noisy, method="savgol", window_length=5)
        rmse_noisy = mod.series_rmse(noisy, clean)
        rmse_smooth = mod.series_rmse(sm, clean)
        assert rmse_smooth < rmse_noisy

    def test_spline_reduces_noise(self):
        noisy, info = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=12)
        clean = info["clean"]
        sm, _ = mod.smooth_timeseries(noisy, method="spline", smoothing=1.2)
        rmse_noisy = mod.series_rmse(noisy, clean)
        rmse_smooth = mod.series_rmse(sm, clean)
        assert rmse_smooth < rmse_noisy

    def test_output_range(self):
        noisy, _ = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=12)
        sm, _ = mod.smooth_timeseries(noisy, method="savgol")
        assert sm.min() >= -1.0
        assert sm.max() <= 1.0

    def test_bad_method_raises(self):
        cube = np.random.uniform(0, 1, (6, 4, 4)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.smooth_timeseries(cube, method="bogus")

    def test_single_date_raises(self):
        cube = np.random.uniform(0, 1, (1, 4, 4)).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.smooth_timeseries(cube, method="savgol")

    def test_constant_series_spline(self):
        """常数序列不应让样条崩溃。"""
        cube = np.full((8, 4, 4), 0.5, dtype=np.float32)
        sm, _ = mod.smooth_timeseries(cube, method="spline")
        np.testing.assert_allclose(sm, 0.5, atol=1e-4)


class TestSeriesRmse:
    def test_zero_for_identical(self):
        a = np.random.uniform(0, 1, (5, 4, 4)).astype(np.float32)
        assert mod.series_rmse(a, a) == 0.0

    def test_known_value(self):
        a = np.zeros((2, 2, 2), dtype=np.float32)
        b = np.ones((2, 2, 2), dtype=np.float32)
        np.testing.assert_allclose(mod.series_rmse(a, b), 1.0, atol=1e-6)


class TestSynthetic:
    def test_cube_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=12)
        assert cube.shape == (12, 32, 32)
        assert info["clean"].shape == cube.shape

    def test_noisy_differs_from_clean(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=12)
        assert not np.allclose(cube, info["clean"])


class TestGeoTiffIO:
    def test_write_read_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (4, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        back, rbbox = mod.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/path/file.tif")
