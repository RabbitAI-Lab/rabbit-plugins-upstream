"""Core algorithm tests for temperature-anomaly-mapping."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestClimatology:
    def test_phase_mean_exact(self):
        """period=2：clim 应为同相位帧的逐像元平均。"""
        cube = np.zeros((4, 2, 2), dtype=np.float32)
        cube[0] = 1.0; cube[2] = 3.0     # phase 0 -> mean 2
        cube[1] = 10.0; cube[3] = 20.0   # phase 1 -> mean 15
        clim = mod.compute_climatology(cube, period=2)
        np.testing.assert_allclose(clim[0], 2.0)
        np.testing.assert_allclose(clim[2], 2.0)
        np.testing.assert_allclose(clim[1], 15.0)
        np.testing.assert_allclose(clim[3], 15.0)

    def test_period_ge_n_uses_overall_mean(self):
        cube = np.arange(4 * 2 * 2, dtype=np.float32).reshape(4, 2, 2)
        clim = mod.compute_climatology(cube, period=10)
        overall = cube.mean(axis=0)
        for k in range(4):
            np.testing.assert_allclose(clim[k], overall)

    def test_wrong_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.compute_climatology(np.zeros((4, 4)), period=2)

    def test_invalid_period_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.compute_climatology(np.zeros((4, 2, 2)), period=0)


class TestAnomaly:
    def test_anomaly_is_current_minus_clim(self):
        rng = np.random.default_rng(0)
        cube = rng.normal(15, 3, (24, 8, 8)).astype(np.float32)
        anom, clim = mod.anomaly_cube(cube, period=12)
        np.testing.assert_allclose(anom, cube - clim, atol=1e-4)

    def test_anomaly_phase_mean_near_zero(self):
        """同一相位各年的距平之和应接近 0（气候态是组内均值）。"""
        rng = np.random.default_rng(1)
        cube = rng.normal(15, 3, (36, 4, 4)).astype(np.float32)
        anom, _ = mod.anomaly_cube(cube, period=12)
        for phase in range(12):
            idx = np.arange(phase, 36, 12)
            np.testing.assert_allclose(anom[idx].sum(axis=0), 0.0, atol=1e-3)


class TestStandardizedAnomaly:
    def test_exact_z(self):
        """phase std=1/5 → z 可精确推算。"""
        cube = np.zeros((4, 2, 2), dtype=np.float32)
        cube[0] = 1.0; cube[2] = 3.0     # phase 0: mean 2, std 1
        cube[1] = 10.0; cube[3] = 20.0   # phase 1: mean 15, std 5
        z = mod.standardized_anomaly(cube, period=2)
        np.testing.assert_allclose(z[0], -1.0, atol=1e-4)
        np.testing.assert_allclose(z[2], 1.0, atol=1e-4)
        np.testing.assert_allclose(z[1], -1.0, atol=1e-4)
        np.testing.assert_allclose(z[3], 1.0, atol=1e-4)


class TestClassifyAnomaly:
    def test_boundaries(self):
        z = np.array([2.5, 2.0, 1.5, 1.0, 0.5, 0.0,
                      -0.5, -1.0, -1.5, -2.0, -2.5], dtype=np.float32)
        cls = mod.classify_anomaly(z)
        assert cls.tolist() == [2, 2, 1, 1, 0, 0, 0, -1, -1, -2, -2]

    def test_all_normal(self):
        z = np.random.uniform(-0.9, 0.9, (10, 10)).astype(np.float32)
        assert np.all(mod.classify_anomaly(z) == 0)

    def test_class_codes_complete(self):
        assert set(mod.ANOMALY_CLASSES.keys()) == {2, 1, 0, -1, -2}


class TestSyntheticDetection:
    def test_injected_warm_anomaly_detected(self):
        """注入暖异常区应被判为暖/严重暖，区外基本正常。"""
        cube, info = mod.generate_synthetic_cube(
            [116, 39, 117, 40], n_dates=12, n_years=5)
        z = mod.standardized_anomaly(cube, period=12)
        last_z = z[-1]
        last_cls = mod.classify_anomaly(last_z)
        inj = info["injected"]
        y0, y1 = inj["y_range"]; x0, x1 = inj["x_range"]
        region = last_cls[y0:y1, x0:x1]
        outside_mask = np.ones(last_cls.shape, dtype=bool)
        outside_mask[y0:y1, x0:x1] = False
        # 注入区大部分被判为暖异常（>=1）
        assert np.mean(region >= 1) > 0.8
        # 区外绝大部分正常
        assert np.mean(last_cls[outside_mask] == 0) > 0.6

    def test_warm_fraction_matches_region(self):
        cube, info = mod.generate_synthetic_cube(
            [116, 39, 117, 40], n_dates=12, n_years=5)
        z = mod.standardized_anomaly(cube, period=12)
        cls = mod.classify_anomaly(z[-1])
        warm_frac = float(np.mean(cls >= 1))
        # 注入区占画面 1/3，暖占比应接近该量级
        assert 0.2 < warm_frac < 0.6

    def test_cube_shape_and_total(self):
        cube, info = mod.generate_synthetic_cube(
            [116, 39, 117, 40], n_dates=12, n_years=4)
        assert cube.shape == (48, 64, 64)
        assert info["total_frames"] == 48


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(-2, 2, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
