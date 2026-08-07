"""Core algorithm tests for evapotranspiration-estimation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as et


class TestSlopeVaporPressure:
    def test_value_at_20C(self):
        """20 °C 时 Δ ≈ 0.145 kPa/°C（FAO-56 标准值）。"""
        delta = et.slope_vapor_pressure(np.array([20.0]))
        assert np.isclose(delta[0], 0.1448, atol=0.002)

    def test_increases_with_temp(self):
        """Δ 随气温单调递增。"""
        delta = et.slope_vapor_pressure(np.array([5.0, 15.0, 25.0, 35.0]))
        assert np.all(np.diff(delta) > 0)


class TestPriestleyTaylor:
    def test_typical_value(self):
        """Rn=15 MJ/m²/day, T=20 °C → ET ≈ 5.3 mm/day。"""
        e = et.priestley_taylor_et(np.array([15.0]), np.array([20.0]))
        assert 4.0 < e[0] < 7.0

    def test_increases_with_Rn(self):
        """固定气温，ET 随净辐射单调递增（正相关）。"""
        Rn = np.array([5.0, 10.0, 15.0, 20.0])
        T = np.full(4, 20.0)
        e = et.priestley_taylor_et(Rn, T)
        assert np.all(np.diff(e) > 0)

    def test_nonnegative(self):
        Rn = np.random.uniform(0, 25, (16, 16))
        T = np.random.uniform(0, 35, (16, 16))
        e = et.priestley_taylor_et(Rn, T)
        assert (e >= 0).all()

    def test_higher_alpha_higher_et(self):
        Rn = np.full((4, 4), 15.0)
        T = np.full((4, 4), 20.0)
        e1 = et.priestley_taylor_et(Rn, T, alpha=1.0)
        e2 = et.priestley_taylor_et(Rn, T, alpha=1.5)
        assert np.mean(e2) > np.mean(e1)


class TestSebal:
    def test_increases_with_Rn(self):
        """简化 SEBAL：ET 随净辐射正相关。"""
        NDVI = np.full((1, 4), 0.6)
        LST = np.full((1, 4), 300.0)
        Rn = np.array([[5.0, 10.0, 15.0, 20.0]])
        e = et.sebal_et(LST, NDVI, Rn)
        assert np.all(np.diff(e[0]) > 0)

    def test_vegetation_vs_bare(self):
        """同辐射下，高 NDVI + 低 LST（植被）ET 高于低 NDVI + 高 LST（裸地）。"""
        Rn = np.full((2, 2), 15.0)
        NDVI = np.array([[0.85, 0.85], [0.1, 0.1]])
        LST = np.array([[288.0, 288.0], [312.0, 312.0]])
        e = et.sebal_et(LST, NDVI, Rn)
        assert np.mean(e[0]) > np.mean(e[1])

    def test_physical_range(self):
        rng = np.random.default_rng(0)
        Rn = rng.uniform(5, 22, (32, 32))
        NDVI = rng.uniform(0.1, 0.9, (32, 32))
        LST = rng.uniform(285, 315, (32, 32))
        e = et.sebal_et(LST, NDVI, Rn)
        assert e.min() >= 0.0
        assert e.max() <= 10.0


class TestRunET:
    def test_unknown_method_raises(self):
        Rn = np.full((8, 8), 15.0)
        with pytest.raises(et.UsageError):
            et.run_et("bogus", Rn, np.full((8, 8), 20.0),
                      np.full((8, 8), 300.0), np.full((8, 8), 0.5))

    def test_non2d_raises(self):
        with pytest.raises(et.ValidationError):
            et.run_et("pt", np.zeros(8), np.zeros(8), np.zeros(8), np.zeros(8))

    def test_pt_and_sebal_both_work(self):
        Rn, T, LST, NDVI, _ = et.generate_synthetic([116, 39, 117, 40], seed=3)
        e_pt, p_pt = et.run_et("pt", Rn, T, LST, NDVI)
        e_se, p_se = et.run_et("sebal", Rn, T, LST, NDVI)
        assert e_pt.shape == Rn.shape
        assert e_se.shape == Rn.shape
        assert p_pt["method"] == "pt"
        assert p_se["method"] == "sebal"


class TestSynthetic:
    def test_shapes(self):
        Rn, T, LST, NDVI, info = et.generate_synthetic([116, 39, 117, 40])
        for arr in (Rn, T, LST, NDVI):
            assert arr.shape == (128, 128)
        assert (Rn > 0).all()
        assert (NDVI >= 0).all() and (NDVI <= 1).all()

    def test_et_physical_range(self):
        """合成数据估算的 ET 应落在物理合理区间（0–10 mm/day）。"""
        Rn, T, LST, NDVI, _ = et.generate_synthetic([116, 39, 117, 40], seed=7)
        e_pt, _ = et.run_et("pt", Rn, T, LST, NDVI)
        e_se, _ = et.run_et("sebal", Rn, T, LST, NDVI)
        for e in (e_pt, e_se):
            assert e.min() >= 0.0
            assert e.max() <= 10.0
            assert e.mean() > 0.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 8, (20, 20)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "et.tif")
        et.write_geotiff(path, arr, bbox)
        assert os.path.exists(path)
        back, rbbox = et.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, arr, atol=1e-4)

    def test_read_missing_raises(self):
        with pytest.raises(et.UsageError):
            et.read_geotiff("/nonexistent/nope.tif")
