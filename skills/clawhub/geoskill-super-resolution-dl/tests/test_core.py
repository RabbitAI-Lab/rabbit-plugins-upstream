"""Core algorithm tests for super-resolution-dl."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBicubicUpscale:
    def test_output_size(self):
        img = np.random.uniform(0, 1, (16, 16))
        out = mod.bicubic_upscale(img, scale=2)
        assert out.shape == (32, 32)

    def test_scale_3(self):
        img = np.random.uniform(0, 1, (10, 20))
        out = mod.bicubic_upscale(img, scale=3)
        assert out.shape == (30, 60)

    def test_scale_1_identity(self):
        img = np.random.uniform(0, 1, (8, 8))
        out = mod.bicubic_upscale(img, scale=1)
        np.testing.assert_array_equal(out, img)

    def test_constant_preserved(self):
        img = np.full((12, 12), 0.7)
        out = mod.bicubic_upscale(img, scale=2)
        np.testing.assert_allclose(out, 0.7, atol=1e-6)

    def test_rejects_3d(self):
        with pytest.raises(mod.ValidationError):
            mod.bicubic_upscale(np.zeros((2, 8, 8)), scale=2)

    def test_bad_scale_raises(self):
        with pytest.raises(mod.UsageError):
            mod.bicubic_upscale(np.zeros((8, 8)), scale=0)


class TestLaplacianSharpen:
    def test_flat_unchanged(self):
        img = np.full((16, 16), 0.5)
        out = mod.laplacian_sharpen(img, amount=0.5)
        np.testing.assert_allclose(out, 0.5, atol=1e-9)

    def test_edge_contrast_increased(self):
        """锐化应增大边缘处的对比（overshoot）。"""
        img = np.zeros((1, 20))
        img[0, 10:] = 1.0
        out = mod.laplacian_sharpen(img, amount=0.5)
        # 边缘附近：暗侧更暗、亮侧更亮
        assert out[0, 9] < img[0, 9]    # 暗侧下冲
        assert out[0, 10] > img[0, 10]  # 亮侧上冲


class TestSuperResolve:
    def test_shape_and_dtype(self):
        img = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        out = mod.super_resolve(img, scale=2, amount=0.5)
        assert out.shape == (32, 32)
        assert out.dtype == np.float32


class TestPSNR:
    def test_identical_high(self):
        img = np.random.uniform(0, 1, (16, 16))
        assert mod.psnr(img, img, data_range=1.0) >= 99.0

    def test_noisy_lower_than_clean(self):
        rng = np.random.default_rng(0)
        ref = rng.uniform(0, 1, (32, 32))
        noisy_small = ref + rng.normal(0, 0.01, ref.shape)
        noisy_big = ref + rng.normal(0, 0.1, ref.shape)
        p_small = mod.psnr(ref, noisy_small, data_range=1.0)
        p_big = mod.psnr(ref, noisy_big, data_range=1.0)
        assert p_small > p_big

    def test_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.psnr(np.zeros((4, 4)), np.zeros((5, 5)))


class TestSSIM:
    def test_identical_near_one(self):
        img = np.random.uniform(0, 1, (32, 32))
        s = mod.structural_similarity(img, img, data_range=1.0)
        assert s > 0.99

    def test_degrades_with_noise(self):
        rng = np.random.default_rng(1)
        ref = rng.uniform(0, 1, (32, 32))
        clean = mod.structural_similarity(ref, ref, data_range=1.0)
        noisy = mod.structural_similarity(ref, ref + rng.normal(0, 0.2, ref.shape), data_range=1.0)
        assert noisy < clean

    def test_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.structural_similarity(np.zeros((4, 4)), np.zeros((6, 6)))


class TestSynthetic:
    def test_shapes(self):
        low, high, info = mod.generate_synthetic([116, 39, 117, 40], scale=2)
        assert high.shape == (64, 64)
        assert low.shape == (32, 32)
        assert info["scale"] == 2

    def test_sr_output_matches_truth_size(self):
        low, high, _ = mod.generate_synthetic([116, 39, 117, 40], scale=2, seed=7)
        sr = mod.super_resolve(low, scale=2)
        assert sr.shape == high.shape


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "sr.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
