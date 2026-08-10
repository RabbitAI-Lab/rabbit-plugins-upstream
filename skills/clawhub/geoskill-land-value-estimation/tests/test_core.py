"""Core algorithm tests for land-value-estimation.

验证物理正确性：
- 可达性 = exp(-distance/decay)，distance=0→1，单调递减
- Hedonic 价值 = 截距 + Σ系数×特征（线性解析解）
- 价值随可达性递增（正系数）
- 最小二乘标定精确恢复已知系数
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestAccessibility:
    def test_zero_distance_one(self):
        d = np.array([[0.0]], dtype=np.float32)
        a = mod.accessibility(d, decay=1000.0)
        np.testing.assert_allclose(a[0, 0], 1.0, atol=1e-6)

    def test_exp_analytic(self):
        """distance=1000, decay=1000 → exp(-1)"""
        d = np.array([[1000.0]], dtype=np.float32)
        a = mod.accessibility(d, decay=1000.0)
        np.testing.assert_allclose(a[0, 0], np.exp(-1.0), atol=1e-6)

    def test_monotonic_decreasing(self):
        d = np.array([[0.0, 10.0, 50.0, 100.0]], dtype=np.float32)
        a = mod.accessibility(d, decay=30.0)
        assert a[0, 0] > a[0, 1] > a[0, 2] > a[0, 3]

    def test_range(self):
        rng = np.random.default_rng(0)
        d = rng.uniform(0, 1000, (16, 16)).astype(np.float32)
        a = mod.accessibility(d, decay=100.0)
        assert a.min() > 0.0
        assert a.max() <= 1.0


class TestHedonicValue:
    def test_linear_analytic(self):
        """value = 1000 + 5000×0.8 + 2000×0.5 + 1500×0.4 = 1000+4000+1000+600 = 6600"""
        a = np.array([[0.8]], dtype=np.float32)
        p = np.array([[0.5]], dtype=np.float32)
        g = np.array([[0.4]], dtype=np.float32)
        v = mod.hedonic_value(a, p, g, intercept=1000.0,
                              coef_acc=5000.0, coef_poi=2000.0, coef_green=1500.0)
        np.testing.assert_allclose(v[0, 0], 6600.0, atol=1e-2)

    def test_higher_accessibility_higher_value(self):
        p = np.array([[0.5, 0.5]], dtype=np.float32)
        g = np.array([[0.5, 0.5]], dtype=np.float32)
        a = np.array([[0.2, 0.9]], dtype=np.float32)
        v = mod.hedonic_value(a, p, g)
        assert v[0, 1] > v[0, 0]

    def test_nonnegative(self):
        rng = np.random.default_rng(1)
        a = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        p = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        g = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        v = mod.hedonic_value(a, p, g)
        assert v.min() >= 0.0


class TestCalibrateCoefficients:
    def test_recovers_known_coefficients(self):
        """用已知系数生成样本 → lstsq 精确恢复"""
        rng = np.random.default_rng(2)
        n = 200
        X = rng.uniform(0, 1, (n, 3))
        true = np.array([100.0, 50.0, -20.0, 30.0])  # intercept + 3 coefs
        y = true[0] + X @ true[1:]
        recovered = mod.calibrate_coefficients(X, y)
        np.testing.assert_allclose(recovered, true, atol=1e-6)


class TestSynthetic:
    def test_shapes(self):
        dc, poi, dg, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dc.shape == (128, 128)
        assert poi.shape == (128, 128)
        assert dg.shape == (128, 128)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back, cube, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/file.tif")
