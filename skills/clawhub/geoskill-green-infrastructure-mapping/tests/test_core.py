"""Core algorithm tests for green-infrastructure-mapping.

验证物理正确性：
- NDVI 解析解与值域 [−1,1]
- 绿地分类阈值行为
- 树木计数与注入的分离树冠数一致
- 连通性指数：单一连通块=1，碎片化<1，值域[0,1]
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestNDVI:
    def test_analytic(self):
        nir = np.array([[0.5]], dtype=np.float32)
        red = np.array([[0.1]], dtype=np.float32)
        n = mod.ndvi(nir, red)
        np.testing.assert_allclose(n[0, 0], 0.4 / 0.6, atol=1e-5)

    def test_range(self):
        rng = np.random.default_rng(0)
        nir = rng.uniform(0.01, 0.9, (32, 32)).astype(np.float32)
        red = rng.uniform(0.01, 0.9, (32, 32)).astype(np.float32)
        n = mod.ndvi(nir, red)
        assert n.min() >= -1.0
        assert n.max() <= 1.0


class TestClassifyGreen:
    def test_threshold(self):
        ndvi_arr = np.array([[0.2, 0.35, 0.6]], dtype=np.float32)
        green = mod.classify_green(ndvi_arr, threshold=0.3)
        assert green[0, 0] == 0
        assert green[0, 1] == 1
        assert green[0, 2] == 1


class TestTreeCount:
    def test_count_matches_injected_peaks(self):
        """注入 4 个分离的高斯树冠 → 计数 ≈ 4"""
        ndvi_arr = np.full((64, 64), 0.1, dtype=np.float32)
        centers = [(12, 12), (12, 48), (48, 12), (48, 48)]
        yy, xx = np.mgrid[0:64, 0:64]
        for r, c in centers:
            g = 0.6 * np.exp(-((yy - r) ** 2 + (xx - c) ** 2) / (2 * 3.0 ** 2))
            ndvi_arr += g.astype(np.float32)
        n = mod.tree_count(ndvi_arr, min_ndvi=0.4, neighborhood=5)
        assert n == 4

    def test_count_zero_on_bare(self):
        ndvi_arr = np.full((32, 32), 0.1, dtype=np.float32)
        assert mod.tree_count(ndvi_arr, min_ndvi=0.4) == 0


class TestConnectivityIndex:
    def test_single_block_connectivity_one(self):
        """单一连通绿地块 → 连通性 = 1"""
        mask = np.zeros((32, 32), dtype=np.uint8)
        mask[8:24, 8:24] = 1
        conn, n_patches = mod.connectivity_index(mask)
        np.testing.assert_allclose(conn, 1.0, atol=1e-6)
        assert n_patches == 1

    def test_fragmented_connectivity_less_than_one(self):
        """多个等大小碎片 → 连通性 = 1/n_patches < 1"""
        mask = np.zeros((40, 40), dtype=np.uint8)
        mask[5:10, 5:10] = 1
        mask[5:10, 30:35] = 1
        mask[30:35, 5:10] = 1
        mask[30:35, 30:35] = 1
        conn, n_patches = mod.connectivity_index(mask)
        assert n_patches == 4
        np.testing.assert_allclose(conn, 0.25, atol=1e-6)

    def test_empty_returns_zero(self):
        mask = np.zeros((16, 16), dtype=np.uint8)
        conn, n_patches = mod.connectivity_index(mask)
        assert conn == 0.0
        assert n_patches == 0

    def test_connectivity_range(self):
        rng = np.random.default_rng(1)
        mask = (rng.random((32, 32)) > 0.6).astype(np.uint8)
        conn, _ = mod.connectivity_index(mask)
        assert 0.0 <= conn <= 1.0


class TestSynthetic:
    def test_shapes(self):
        red, nir, info = mod.generate_synthetic([116, 39, 117, 40])
        assert red.shape == (128, 128)
        assert nir.shape == (128, 128)
        assert info["n_trees_injected"] == 25


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
