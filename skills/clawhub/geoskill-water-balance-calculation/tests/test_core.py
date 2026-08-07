"""Core algorithm tests for water-balance-calculation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as wb


class TestClosureResidual:
    def test_exact_balance_zero_residual(self):
        P = np.array([[100.0, 200.0]], dtype=np.float32)
        ET = np.array([[40.0, 80.0]], dtype=np.float32)
        Q = np.array([[30.0, 60.0]], dtype=np.float32)
        dS = np.array([[30.0, 60.0]], dtype=np.float32)
        res = wb.closure_residual(P, ET, Q, dS)
        assert np.allclose(res, 0.0)

    def test_residual_formula(self):
        """residual = P − ET − Q − ΔS。"""
        P = np.full((4, 4), 100.0)
        ET = np.full((4, 4), 50.0)
        Q = np.full((4, 4), 30.0)
        dS = np.full((4, 4), 10.0)
        res = wb.closure_residual(P, ET, Q, dS)
        assert np.allclose(res, 10.0)  # 100-50-30-10


class TestWaterBalanceStats:
    def test_relative_closure_error(self):
        P = np.full((10, 10), 1000.0)
        ET = np.full((10, 10), 450.0)
        Q = np.full((10, 10), 300.0)
        dS = np.full((10, 10), 250.0)  # 闭合
        res = wb.closure_residual(P, ET, Q, dS)
        stats = wb.water_balance_stats(P, ET, Q, dS, res)
        assert stats["relative_closure_error"] == 0.0
        assert np.isclose(stats["mean_P_mm"], 1000.0)

    def test_error_with_residual(self):
        P = np.full((10, 10), 1000.0)
        res = np.full((10, 10), 50.0)  # 5% 误差
        stats = wb.water_balance_stats(P, P * 0.4, P * 0.3, P * 0.3, res)
        assert np.isclose(stats["relative_closure_error"], 0.05)


class TestSyntheticBalance:
    def test_closure_near_zero(self):
        """合成数据应物理闭合：相对闭合误差很小（< 2%）。"""
        P, ET, Q, dS, info = wb.generate_synthetic([116, 39, 117, 40], seed=3)
        res = wb.closure_residual(P, ET, Q, dS)
        stats = wb.water_balance_stats(P, ET, Q, dS, res)
        assert stats["relative_closure_error"] < 0.02
        assert abs(stats["residual_mean_mm"]) < 5.0

    def test_conservation(self):
        """mean(P) ≈ mean(ET) + mean(Q) + mean(dS)（扰动范围内）。"""
        P, ET, Q, dS, _ = wb.generate_synthetic([116, 39, 117, 40], seed=9)
        imbalance = np.mean(P) - (np.mean(ET) + np.mean(Q) + np.mean(dS))
        assert abs(imbalance) < 5.0  # 扰动 std=3mm，均值误差远小于此

    def test_shapes(self):
        P, ET, Q, dS, info = wb.generate_synthetic([116, 39, 117, 40])
        for arr in (P, ET, Q, dS):
            assert arr.shape == (128, 128)
        assert (P > 0).all()


class TestRunWaterBalance:
    def test_shape_mismatch_raises(self):
        P = np.zeros((8, 8))
        with pytest.raises(wb.ValidationError):
            wb.run_water_balance(P, np.zeros((8, 8)), np.zeros((8, 8)),
                                 np.zeros((4, 4)), [116, 39, 117, 40])

    def test_non2d_raises(self):
        with pytest.raises(wb.ValidationError):
            wb.run_water_balance(np.zeros(8), np.zeros(8), np.zeros(8),
                                 np.zeros(8), [116, 39, 117, 40])

    def test_returns_residual_and_report(self):
        P, ET, Q, dS, _ = wb.generate_synthetic([116, 39, 117, 40], seed=1)
        res, report = wb.run_water_balance(P, ET, Q, dS, [116, 39, 117, 40])
        assert res.shape == P.shape
        assert "relative_closure_error" in report


class TestGeoTiffIO:
    def test_multiband_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1000, (4, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "comp.tif")
        wb.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        import rasterio
        with rasterio.open(path) as src:
            assert src.count == 4
            back = src.read().astype(np.float32)
        np.testing.assert_allclose(back, cube, atol=1e-3)

    def test_read_missing_raises(self):
        with pytest.raises(wb.UsageError):
            wb.read_geotiff("/nonexistent/nope.tif")
