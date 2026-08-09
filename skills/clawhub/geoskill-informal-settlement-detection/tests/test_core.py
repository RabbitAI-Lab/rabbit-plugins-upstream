"""Core algorithm tests for informal-settlement-detection.

验证物理正确性：
- 局部标准差：噪声区 > 平滑区
- NDVI：植被(NIR高Red低) → 正值；裸地(NIR≈Red) → 近零
- 非正规评分：高纹理+高密度+低NDVI → 高分
- 评分值域 [0,1]
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestLocalStd:
    def test_noise_higher_than_smooth(self):
        rng = np.random.default_rng(0)
        noisy = rng.uniform(0, 1, (64, 64)).astype(np.float32)
        smooth = np.full((64, 64), 0.5, dtype=np.float32)
        std_n = mod.local_std(noisy, size=5)
        std_s = mod.local_std(smooth, size=5)
        assert np.mean(std_n) > np.mean(std_s) + 0.01

    def test_constant_zero_std(self):
        c = np.full((32, 32), 0.7, dtype=np.float32)
        std = mod.local_std(c, size=3)
        np.testing.assert_allclose(std, 0.0, atol=1e-5)


class TestNDVI:
    def test_vegetation_positive(self):
        nir = np.array([[0.5]], dtype=np.float32)
        red = np.array([[0.1]], dtype=np.float32)
        n = mod.ndvi(nir, red)
        np.testing.assert_allclose(n[0, 0], 0.4 / 0.6, atol=1e-5)

    def test_bare_soil_near_zero(self):
        nir = np.array([[0.2]], dtype=np.float32)
        red = np.array([[0.2]], dtype=np.float32)
        n = mod.ndvi(nir, red)
        np.testing.assert_allclose(n[0, 0], 0.0, atol=1e-5)

    def test_range(self):
        rng = np.random.default_rng(1)
        nir = rng.uniform(0.01, 0.9, (32, 32)).astype(np.float32)
        red = rng.uniform(0.01, 0.9, (32, 32)).astype(np.float32)
        n = mod.ndvi(nir, red)
        assert n.min() >= -1.0
        assert n.max() <= 1.0


class TestInformalScore:
    def test_score_range_01(self):
        rng = np.random.default_rng(2)
        tex = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        den = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        ndvi_arr = rng.uniform(-1, 1, (32, 32)).astype(np.float32)
        score = mod.informal_score(tex, den, ndvi_arr)
        assert score.min() >= 0.0
        assert score.max() <= 1.0

    def test_high_texture_high_density_low_ndvi_scores_high(self):
        n = 32
        tex = np.full((n, n), 0.9, dtype=np.float32)
        den = np.full((n, n), 0.9, dtype=np.float32)
        ndvi_arr = np.full((n, n), -0.8, dtype=np.float32)  # very low vegetation
        score = mod.informal_score(tex, den, ndvi_arr)
        assert np.mean(score) > 0.5

    def test_low_texture_low_density_high_ndvi_scores_low(self):
        n = 32
        tex = np.full((n, n), 0.1, dtype=np.float32)
        den = np.full((n, n), 0.1, dtype=np.float32)
        ndvi_arr = np.full((n, n), 0.8, dtype=np.float32)  # dense vegetation
        score = mod.informal_score(tex, den, ndvi_arr)
        assert np.mean(score) < 0.5


class TestClassify:
    def test_threshold_split(self):
        score = np.array([[0.3, 0.7]], dtype=np.float32)
        mask = mod.classify_informal(score, threshold=0.5)
        assert mask[0, 0] == 0
        assert mask[0, 1] == 1


class TestSynthetic:
    def test_synthetic_shapes(self):
        red, nir, fp, info = mod.generate_synthetic([116, 39, 117, 40])
        assert red.shape == (128, 128)
        assert nir.shape == (128, 128)
        assert fp.shape == (128, 128)
        assert info["informal_fraction"] == 0.5


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
