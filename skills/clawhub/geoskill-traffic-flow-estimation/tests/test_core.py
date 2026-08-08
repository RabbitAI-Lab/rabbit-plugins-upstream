"""Core algorithm tests for traffic-flow-estimation.

验证物理正确性：
- 车辆计数与注入的独立亮目标数一致
- 流量 = 车辆数 / 时间间隔（解析解）
- 速度 = 位移 × 像元大小 / 时间（解析解）
- 相位互相关精确恢复已知的循环位移
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestCountVehicles:
    def test_count_matches_injected_blobs(self):
        """注入 5 个独立的 2×2 亮目标 → 计数 = 5"""
        img = np.full((64, 64), 0.05, dtype=np.float32)
        positions = [(5, 5), (10, 30), (25, 15), (40, 50), (55, 40)]
        for r, c in positions:
            img[r:r + 2, c:c + 2] = 0.9
        n = mod.count_vehicles(img, threshold=0.5, min_size=1, max_size=10)
        assert n == 5

    def test_count_zero_on_empty(self):
        img = np.full((32, 32), 0.1, dtype=np.float32)
        assert mod.count_vehicles(img, threshold=0.5) == 0

    def test_max_size_filter(self):
        """超大连通区（>max_size）被过滤掉"""
        img = np.full((32, 32), 0.05, dtype=np.float32)
        img[5:25, 5:25] = 0.9  # 20×20 = 400 像元的大块
        assert mod.count_vehicles(img, threshold=0.5, min_size=1, max_size=50) == 0


class TestEstimateFlow:
    def test_flow_analytic(self):
        """100 辆 / 0.5 h = 200 veh/h"""
        np.testing.assert_allclose(mod.estimate_flow(100, 0.5), 200.0, atol=1e-6)

    def test_flow_zero_dt(self):
        assert mod.estimate_flow(10, 0.0) == 0.0


class TestEstimateSpeed:
    def test_speed_analytic(self):
        """位移 10 px × 1 m/px / 2 s = 5 m/s"""
        np.testing.assert_allclose(
            mod.estimate_speed_mps(10.0, 1.0, 2.0), 5.0, atol=1e-6)

    def test_speed_zero_dt(self):
        assert mod.estimate_speed_mps(10.0, 1.0, 0.0) == 0.0


class TestEstimateShift:
    def test_recover_x_shift(self):
        """np.roll 沿 x 位移 7 → 互相关恢复 dx=7"""
        rng = np.random.default_rng(0)
        im1 = rng.uniform(0, 1, (64, 64))
        im2 = np.roll(im1, shift=7, axis=1)
        dy, dx = mod.estimate_shift(im1, im2)
        assert abs(dx - 7.0) < 1.0
        assert abs(dy) < 1.0

    def test_recover_negative_shift(self):
        rng = np.random.default_rng(1)
        im1 = rng.uniform(0, 1, (64, 64))
        im2 = np.roll(im1, shift=-5, axis=0)
        dy, dx = mod.estimate_shift(im1, im2)
        assert abs(dy + 5.0) < 1.0

    def test_zero_shift(self):
        rng = np.random.default_rng(2)
        im1 = rng.uniform(0, 1, (64, 64))
        dy, dx = mod.estimate_shift(im1, im1.copy())
        assert abs(dy) < 1.0
        assert abs(dx) < 1.0


class TestSynthetic:
    def test_shapes_and_shift(self):
        t1, t2, info = mod.generate_synthetic([116, 39, 117, 40])
        assert t1.shape == (128, 128)
        assert t2.shape == (128, 128)
        assert info["n_cars"] == 20
        assert info["shift_px"] == 6


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb, _ = mod.read_geotiff(path)
        np.testing.assert_allclose(back, cube, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/file.tif")
