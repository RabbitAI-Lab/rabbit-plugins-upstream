"""Core algorithm tests for slum-mapping.

验证物理正确性：
- 贫民窟指数 ∈ [0,1]
- 单调性：密度↑ → 指数↑；夜光↑ → 指数↓；纹理↑ → 指数↑；人口↑ → 指数↑
- 棚户区特征组合（高纹理/高密度/暗夜光/高人口）→ 高指数
- 正规规划区（平滑/中密度/亮夜光）→ 低指数
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
        assert np.mean(mod.local_std(noisy)) > np.mean(mod.local_std(smooth)) + 0.01

    def test_constant_zero(self):
        c = np.full((32, 32), 0.7, dtype=np.float32)
        np.testing.assert_allclose(mod.local_std(c), 0.0, atol=1e-5)


class TestSlumIndex:
    def test_range_01(self):
        rng = np.random.default_rng(1)
        tex = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        den = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        nl = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        pop = rng.uniform(0, 1000, (16, 16)).astype(np.float32)
        si = mod.slum_index(tex, den, nl, pop)
        assert si.min() >= 0.0
        assert si.max() <= 1.0

    def test_monotonic_in_density(self):
        tex = np.full((1, 2), 0.5, dtype=np.float32)
        nl = np.full((1, 2), 0.3, dtype=np.float32)
        pop = np.full((1, 2), 500.0, dtype=np.float32)
        den = np.array([[0.2, 0.9]], dtype=np.float32)
        si = mod.slum_index(tex, den, nl, pop)
        assert si[0, 1] > si[0, 0]

    def test_monotonic_decreasing_in_nightlight(self):
        tex = np.full((1, 2), 0.5, dtype=np.float32)
        den = np.full((1, 2), 0.7, dtype=np.float32)
        pop = np.full((1, 2), 800.0, dtype=np.float32)
        nl = np.array([[0.1, 0.9]], dtype=np.float32)
        si = mod.slum_index(tex, den, nl, pop)
        assert si[0, 0] > si[0, 1]  # 夜光低 → 指数高

    def test_monotonic_in_texture(self):
        den = np.full((1, 2), 0.7, dtype=np.float32)
        nl = np.full((1, 2), 0.2, dtype=np.float32)
        pop = np.full((1, 2), 800.0, dtype=np.float32)
        tex = np.array([[0.05, 0.5]], dtype=np.float32)
        si = mod.slum_index(tex, den, nl, pop)
        assert si[0, 1] > si[0, 0]

    def test_slum_combo_high_formal_low(self):
        """棚户区组合 → 高指数；正规区组合 → 低指数"""
        # 棚户区
        si_slum = mod.slum_index(
            np.array([[0.4]], dtype=np.float32),
            np.array([[0.9]], dtype=np.float32),
            np.array([[0.1]], dtype=np.float32),
            np.array([[1000.0]], dtype=np.float32),
        )
        # 正规区
        si_formal = mod.slum_index(
            np.array([[0.02]], dtype=np.float32),
            np.array([[0.4]], dtype=np.float32),
            np.array([[0.9]], dtype=np.float32),
            np.array([[400.0]], dtype=np.float32),
        )
        assert si_slum[0, 0] > 0.5
        assert si_formal[0, 0] < 0.3


class TestClassifySlum:
    def test_threshold(self):
        si = np.array([[0.3, 0.7]], dtype=np.float32)
        mask = mod.classify_slum(si, threshold=0.5)
        assert mask[0, 0] == 0
        assert mask[0, 1] == 1


class TestSynthetic:
    def test_shapes(self):
        g, d, nl, pop, info = mod.generate_synthetic([116, 39, 117, 40])
        assert g.shape == (128, 128)
        assert d.shape == (128, 128)
        assert nl.shape == (128, 128)
        assert pop.shape == (128, 128)


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
