"""Core algorithm tests for texture-feature-extraction."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _smooth_vs_rough(h=24, w=24, seed=0):
    """左半平滑渐变，右半高频噪声。"""
    rng = np.random.default_rng(seed)
    yy, xx = np.mgrid[0:h, 0:w]
    xx = xx.astype(np.float32) / max(w - 1, 1)
    smooth = 0.5 + 0.3 * xx
    rough = rng.uniform(0, 1, (h, w)).astype(np.float32)
    band = np.empty((h, w), dtype=np.float32)
    half = w // 2
    band[:, :half] = smooth[:, :half]
    band[:, half:] = rough[:, half:]
    return band, half


class TestQuantize:
    def test_range(self):
        band = np.linspace(0, 100, 256).reshape(16, 16).astype(np.float32)
        q = mod.quantize_band(band, levels=32)
        assert q.dtype == np.uint8
        assert q.min() == 0
        assert q.max() == 31

    def test_constant_band(self):
        band = np.full((8, 8), 5.0, dtype=np.float32)
        q = mod.quantize_band(band, levels=32)
        assert (q == 0).all()


class TestComputeTexture:
    def test_returns_requested_features(self):
        band = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        tex = mod.compute_texture(band, window=5,
                                  features=["contrast", "energy", "homogeneity"])
        assert set(tex.keys()) == {"contrast", "energy", "homogeneity"}
        for f in tex:
            assert tex[f].shape == (16, 16)

    def test_contrast_higher_in_rough(self):
        """粗糙区 contrast 应显著高于平滑区。"""
        band, half = _smooth_vs_rough()
        tex = mod.compute_texture(band, window=5, features=["contrast"])
        c = tex["contrast"]
        smooth_mean = float(np.mean(c[:, 2:half - 2]))
        rough_mean = float(np.mean(c[:, half + 2:-2]))
        assert rough_mean > smooth_mean * 1.5

    def test_homogeneity_higher_in_smooth(self):
        """平滑区 homogeneity 应高于粗糙区。"""
        band, half = _smooth_vs_rough()
        tex = mod.compute_texture(band, window=5, features=["homogeneity"])
        hmap = tex["homogeneity"]
        smooth_mean = float(np.mean(hmap[:, 2:half - 2]))
        rough_mean = float(np.mean(hmap[:, half + 2:-2]))
        assert smooth_mean > rough_mean

    def test_bad_feature_raises(self):
        band = np.random.uniform(0, 1, (10, 10)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.compute_texture(band, window=5, features=["bogus"])

    def test_even_window_raises(self):
        band = np.random.uniform(0, 1, (10, 10)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.compute_texture(band, window=4, features=["contrast"])

    def test_asm_geq_energy_squared(self):
        """ASM 与 energy 逐角度满足 energy²=ASM；多方向平均后由 Jensen
        不等式有 mean(ASM) >= mean(energy)²。"""
        band = np.random.uniform(0, 1, (12, 12)).astype(np.float32)
        tex = mod.compute_texture(band, window=5, features=["energy", "ASM"])
        assert (tex["ASM"] >= tex["energy"] ** 2 - 1e-6).all()
        # 两者高度相关（同源 GLCM）
        corr = np.corrcoef(tex["ASM"].ravel(), (tex["energy"] ** 2).ravel())[0, 1]
        assert corr > 0.99


class TestFeatureStats:
    def test_stats_values(self):
        arr = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
        st = mod.feature_stats(arr)
        assert st["min"] == 1.0
        assert st["max"] == 4.0
        np.testing.assert_allclose(st["mean"], 2.5, atol=1e-6)


class TestSynthetic:
    def test_cube_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert cube.shape == (1, 64, 64)
        assert info["smooth_region"][1] == info["rough_region"][0]


class TestGeoTiffIO:
    def test_write_read_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
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
