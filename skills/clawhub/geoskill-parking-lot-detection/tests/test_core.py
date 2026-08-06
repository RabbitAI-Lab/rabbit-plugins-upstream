"""Core algorithm tests for parking-lot-detection.

验证物理正确性：
- NDVI 解析解
- 沥青分数：暗+无植被 → 高；亮或植被 → 低
- 标线密度：规则亮线区 > 均匀暗区
- 停车场评分值域 [0,1]，停车场特征组合 → 高分
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestNDVI:
    def test_analytic(self):
        nir = np.array([[0.6]], dtype=np.float32)
        red = np.array([[0.2]], dtype=np.float32)
        n = mod.ndvi(nir, red)
        np.testing.assert_allclose(n[0, 0], 0.4 / 0.8, atol=1e-5)


class TestAsphaltScore:
    def test_dark_bare_high_score(self):
        """暗 + 无植被 → 高沥青分数"""
        b = np.array([[0.05]], dtype=np.float32)  # 暗
        n = np.array([[0.0]], dtype=np.float32)   # 无植被
        s = mod.asphalt_score(b, n)
        assert s[0, 0] > 0.8

    def test_bright_low_score(self):
        b = np.array([[0.5]], dtype=np.float32)  # 亮
        n = np.array([[0.0]], dtype=np.float32)
        s = mod.asphalt_score(b, n)
        assert s[0, 0] < 0.1

    def test_vegetated_low_score(self):
        b = np.array([[0.1]], dtype=np.float32)
        n = np.array([[0.6]], dtype=np.float32)  # 高植被
        s = mod.asphalt_score(b, n)
        assert s[0, 0] < 0.1

    def test_range(self):
        rng = np.random.default_rng(0)
        b = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        n = rng.uniform(-1, 1, (32, 32)).astype(np.float32)
        s = mod.asphalt_score(b, n)
        assert s.min() >= 0.0
        assert s.max() <= 1.0


class TestMarkingDensity:
    def test_stripes_higher_than_uniform(self):
        """规则亮线区 → 标线密度高于均匀暗区"""
        uniform_dark = np.full((64, 64), 0.1, dtype=np.float32)
        striped = np.full((64, 64), 0.1, dtype=np.float32)
        striped[::8, :] = 0.9  # 规则亮线
        d_u = mod.marking_density(uniform_dark)
        d_s = mod.marking_density(striped)
        assert np.mean(d_s) > np.mean(d_u) + 0.001

    def test_marking_density_nonnegative(self):
        rng = np.random.default_rng(1)
        g = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        d = mod.marking_density(g)
        assert d.min() >= 0.0


class TestRegularity:
    def test_range_01(self):
        rng = np.random.default_rng(2)
        g = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        r = mod.regularity(g, block=8)
        assert r.min() >= 0.0
        assert r.max() <= 1.0 + 1e-6


class TestParkingScore:
    def test_range_01(self):
        rng = np.random.default_rng(3)
        a = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        m = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        r = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        s = mod.parking_score(a, m, r)
        assert s.min() >= 0.0
        assert s.max() <= 1.0

    def test_parking_features_high_score(self):
        a = np.full((8, 8), 0.9, dtype=np.float32)
        m = np.full((8, 8), 0.9, dtype=np.float32)
        r = np.full((8, 8), 0.9, dtype=np.float32)
        s = mod.parking_score(a, m, r)
        np.testing.assert_allclose(s, 0.9, atol=1e-5)

    def test_nonparking_low_score(self):
        a = np.full((8, 8), 0.0, dtype=np.float32)
        m = np.full((8, 8), 0.0, dtype=np.float32)
        r = np.full((8, 8), 0.0, dtype=np.float32)
        s = mod.parking_score(a, m, r)
        np.testing.assert_allclose(s, 0.0, atol=1e-7)


class TestSynthetic:
    def test_shapes(self):
        red, nir, info = mod.generate_synthetic([116, 39, 117, 40])
        assert red.shape == (128, 128)
        assert nir.shape == (128, 128)
        assert info["parking_fraction"] == 0.5


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back, cube, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/file.tif")
