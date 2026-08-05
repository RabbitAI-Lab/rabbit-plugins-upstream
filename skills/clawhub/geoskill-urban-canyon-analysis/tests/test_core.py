"""Core algorithm tests for urban-canyon-analysis.

验证物理正确性：
- H/W 比与建筑高度/街道宽度的解析解一致
- SVF 范围 [0,1]，且 SVF = 1/sqrt(1+(H/W)²)
- 开阔地 (H=0) → SVF=1；深峡谷 → SVF→0
- 街道宽度估计与注入的街道宽度一致（距离变换）
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBuildingHeight:
    def test_height_nonnegative(self):
        dsm = np.array([[100.0, 90.0], [80.0, 70.0]], dtype=np.float32)
        dtm = np.array([[95.0, 95.0], [95.0, 95.0]], dtype=np.float32)
        h = mod.building_height(dsm, dtm)
        assert h.min() >= 0.0

    def test_height_analytic(self):
        dsm = np.array([[60.0]], dtype=np.float32)
        dtm = np.array([[50.0]], dtype=np.float32)
        h = mod.building_height(dsm, dtm)
        np.testing.assert_allclose(h[0, 0], 10.0, atol=1e-5)


class TestStreetWidth:
    def test_straight_street_width(self):
        """两建筑块之间宽 10 像元的直街道 → 中心线宽度 ≈ 10。"""
        mask = np.zeros((40, 40), dtype=bool)
        mask[:, :15] = True   # 左建筑块
        mask[:, 25:] = True   # 右建筑块，中间 cols 15-24 为街道（宽 10）
        width = mod.estimate_street_width(mask, pixel_size=1.0)
        # 街道中心线 col=19 或 20，到最近建筑距离 ≈ 5，2×5 = 10
        center = width[20, 19]
        np.testing.assert_allclose(center, 10.0, atol=1.0)

    def test_building_interior_zero_width(self):
        mask = np.ones((20, 20), dtype=bool)
        width = mod.estimate_street_width(mask)
        np.testing.assert_allclose(width, 0.0, atol=1e-7)


class TestHeightWidthRatio:
    def test_hw_analytic(self):
        height = np.array([[20.0]], dtype=np.float32)
        width = np.array([[10.0]], dtype=np.float32)
        hw = mod.height_width_ratio(height, width)
        np.testing.assert_allclose(hw[0, 0], 2.0, atol=1e-5)

    def test_hw_zero_width(self):
        height = np.array([[20.0]], dtype=np.float32)
        width = np.array([[0.0]], dtype=np.float32)
        hw = mod.height_width_ratio(height, width)
        np.testing.assert_allclose(hw[0, 0], 0.0, atol=1e-7)


class TestSkyViewFactor:
    def test_svf_range_01(self):
        hw = np.linspace(0, 10, 100).astype(np.float32).reshape(10, 10)
        svf = mod.sky_view_factor(hw)
        assert svf.min() >= 0.0
        assert svf.max() <= 1.0

    def test_open_terrain_svf_one(self):
        """H/W = 0（开阔地）→ SVF = 1"""
        hw = np.array([[0.0]], dtype=np.float32)
        svf = mod.sky_view_factor(hw)
        np.testing.assert_allclose(svf[0, 0], 1.0, atol=1e-6)

    def test_svf_analytic(self):
        """SVF = 1/sqrt(1+(H/W)²)，H/W=1 → 1/sqrt(2)"""
        hw = np.array([[1.0]], dtype=np.float32)
        svf = mod.sky_view_factor(hw)
        np.testing.assert_allclose(svf[0, 0], 1.0 / np.sqrt(2.0), atol=1e-6)

    def test_deep_canyon_low_svf(self):
        """H/W = 10（深峡谷）→ SVF 很小"""
        hw = np.array([[10.0]], dtype=np.float32)
        svf = mod.sky_view_factor(hw)
        assert svf[0, 0] < 0.12

    def test_svf_monotonic_decreasing(self):
        hw = np.array([[0.5, 1.0, 2.0, 5.0]], dtype=np.float32)
        svf = mod.sky_view_factor(hw)
        assert svf[0, 0] > svf[0, 1] > svf[0, 2] > svf[0, 3]


class TestSynthetic:
    def test_synthetic_shapes(self):
        dsm, dtm, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dsm.shape == (128, 128)
        assert dtm.shape == (128, 128)
        assert info["building_height_m"] == 20.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb, _ = mod.read_geotiff(path)
        np.testing.assert_allclose(back, cube, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/file.tif")
