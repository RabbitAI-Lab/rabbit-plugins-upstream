"""Core algorithm tests for building-density-mapping.

验证物理正确性：
- 建筑密度与注入足迹一致（核密度守恒、纯建筑区=1、纯空地=0）
- FAR 与建筑高度/层高的解析解一致
- 密度值域 [0,1]
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestComputeDensity:
    def test_all_built_density_one(self):
        """纯建筑区 → 中心密度 = 1.0"""
        fp = np.ones((64, 64), dtype=np.float32)
        d = mod.compute_density(fp, kernel_size=5)
        # 中心区域完全被建筑覆盖，密度应为 1
        np.testing.assert_allclose(d[20:44, 20:44], 1.0, atol=1e-5)

    def test_empty_density_zero(self):
        """纯空地 → 密度 = 0"""
        fp = np.zeros((64, 64), dtype=np.float32)
        d = mod.compute_density(fp, kernel_size=5)
        np.testing.assert_allclose(d, 0.0, atol=1e-7)

    def test_density_range_01(self):
        rng = np.random.default_rng(0)
        fp = (rng.random((64, 64)) > 0.5).astype(np.float32)
        d = mod.compute_density(fp, kernel_size=7)
        assert d.min() >= 0.0
        assert d.max() <= 1.0

    def test_density_matches_injected_fraction(self):
        """注入 50% 覆盖率的棋盘格足迹 → 内部均值密度 ≈ 0.5"""
        fp = np.zeros((128, 128), dtype=np.float32)
        yy, xx = np.mgrid[0:128, 0:128]
        fp[(yy + xx) % 2 == 0] = 1.0  # 精确 50% 覆盖
        d = mod.compute_density(fp, kernel_size=5)
        # 内部（避免边界零填充影响）均值应接近 0.5
        interior = d[20:108, 20:108]
        np.testing.assert_allclose(np.mean(interior), 0.5, atol=0.02)

    def test_half_block_center_density(self):
        """左半区建筑 → 建筑区中心密度=1，空地中心密度=0"""
        fp = np.zeros((64, 64), dtype=np.float32)
        fp[:, :32] = 1.0
        d = mod.compute_density(fp, kernel_size=3)
        assert d[32, 10] > 0.99   # 建筑区深处
        assert d[32, 55] < 0.01   # 空地深处


class TestComputeFAR:
    def test_far_analytic(self):
        """FAR = density × height / floor_height，解析验证"""
        density = np.array([[0.5]], dtype=np.float32)
        height = np.array([[15.0]], dtype=np.float32)
        far = mod.compute_far(density, height, floor_height=3.0)
        np.testing.assert_allclose(far[0, 0], 2.5, atol=1e-5)  # 0.5 × 5 = 2.5

    def test_far_zero_height(self):
        density = np.array([[0.8]], dtype=np.float32)
        height = np.array([[0.0]], dtype=np.float32)
        far = mod.compute_far(density, height, floor_height=3.0)
        np.testing.assert_allclose(far[0, 0], 0.0, atol=1e-7)

    def test_far_proportional_to_density(self):
        height = np.full((1, 2), 12.0, dtype=np.float32)
        density = np.array([[0.2, 0.6]], dtype=np.float32)
        far = mod.compute_far(density, height, floor_height=3.0)
        np.testing.assert_allclose(far[0, 1] / far[0, 0], 3.0, atol=1e-5)

    def test_far_nonnegative(self):
        rng = np.random.default_rng(1)
        density = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        height = rng.uniform(0, 60, (32, 32)).astype(np.float32)
        far = mod.compute_far(density, height)
        assert far.min() >= 0.0


class TestSynthetic:
    def test_synthetic_shapes(self):
        fp, h, info = mod.generate_synthetic([116, 39, 117, 40])
        assert fp.shape == (128, 128)
        assert h.shape == (128, 128)
        assert set(np.unique(fp)).issubset({0.0, 1.0})

    def test_synthetic_heights_consistent(self):
        """建筑足迹处高度 > 0，非建筑处高度 = 0"""
        fp, h, info = mod.generate_synthetic([116, 39, 117, 40], seed=7)
        assert np.all(h[fp == 0] == 0.0)
        assert np.all(h[fp == 1] > 0.0)
        assert info["footprint_fraction"] > 0.0


class TestGeoTiffIO:
    def test_write_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        read_back, read_bbox = mod.read_geotiff(path)
        assert read_back.shape == cube.shape
        np.testing.assert_allclose(read_bbox, bbox, atol=1e-6)
        np.testing.assert_allclose(read_back, cube, atol=1e-5)

    def test_read_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/path/file.tif")
