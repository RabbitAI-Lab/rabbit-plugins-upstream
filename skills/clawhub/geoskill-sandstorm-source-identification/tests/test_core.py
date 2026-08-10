"""Core algorithm tests for sandstorm-source-identification."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ss


class TestVegetationProtection:
    def test_low_ndvi_unprotected(self):
        v = ss.vegetation_protection(np.array([0.0, 0.2, 0.4, 0.8]))
        assert abs(v[0] - 1.0) < 1e-6      # 裸地无保护
        assert abs(v[2] - 0.0) < 1e-6      # NDVI≥0.4 完全保护
        assert v[3] == 0.0
        assert v[0] > v[1] > v[2]          # 随 NDVI 递减


class TestWindExcessFactor:
    def test_zero_below_threshold(self):
        """风速≤阈值 → 不起沙，因子为 0。"""
        f = ss.wind_excess_factor(np.array([0.0, 3.0, 6.0]), threshold=6.0)
        assert np.allclose(f, 0.0)

    def test_increases_and_saturates(self):
        f = ss.wind_excess_factor(np.array([6.0, 11.0, 16.0, 100.0]), threshold=6.0, scale=10.0)
        assert f[0] == 0.0
        assert abs(f[1] - 0.5) < 1e-6       # 超 5 = 半饱和
        assert abs(f[2] - 1.0) < 1e-6       # 超 10 = 饱和
        assert f[3] == 1.0


class TestDustEmissionPotential:
    def test_bounded(self):
        rng = np.random.default_rng(0)
        ndvi = rng.uniform(0, 1, (16, 16))
        bare = rng.uniform(0, 1, (16, 16))
        wind = rng.uniform(0, 20, (16, 16))
        p = ss.dust_emission_potential(ndvi, bare, wind, threshold=6.0)
        assert p.min() >= 0.0 and p.max() <= 1.0

    def test_increases_with_wind_above_threshold(self):
        ndvi = np.full((8, 8), 0.05); bare = np.full((8, 8), 0.8)
        p_lo = ss.dust_emission_potential(ndvi, bare, np.full((8, 8), 8.0), 6.0).mean()
        p_hi = ss.dust_emission_potential(ndvi, bare, np.full((8, 8), 14.0), 6.0).mean()
        assert p_hi > p_lo > 0.0

    def test_zero_below_threshold(self):
        ndvi = np.full((8, 8), 0.05); bare = np.full((8, 8), 0.9)
        p = ss.dust_emission_potential(ndvi, bare, np.full((8, 8), 3.0), 6.0)
        assert np.allclose(p, 0.0)

    def test_decreases_with_ndvi(self):
        bare = np.full((8, 8), 0.8); wind = np.full((8, 8), 12.0)
        p_bare = ss.dust_emission_potential(np.full((8, 8), 0.0), bare, wind, 6.0).mean()
        p_veg = ss.dust_emission_potential(np.full((8, 8), 0.3), bare, wind, 6.0).mean()
        assert p_bare > p_veg

    def test_increases_with_bare_soil(self):
        ndvi = np.full((8, 8), 0.05); wind = np.full((8, 8), 12.0)
        p_low = ss.dust_emission_potential(ndvi, np.full((8, 8), 0.2), wind, 6.0).mean()
        p_high = ss.dust_emission_potential(ndvi, np.full((8, 8), 0.9), wind, 6.0).mean()
        assert p_high > p_low

    def test_shape_mismatch_raises(self):
        with pytest.raises(ss.ValidationError):
            ss.dust_emission_potential(np.zeros((4, 4)), np.zeros((4, 5)), np.zeros((4, 4)), 6.0)


class TestIdentifySources:
    def test_requires_all_conditions(self):
        ndvi = np.array([[0.05, 0.05, 0.30]])
        bare = np.array([[0.90, 0.20, 0.90]])
        wind = np.array([[10.0, 10.0, 10.0]])
        src = ss.identify_sources(ndvi, bare, wind, threshold=6.0, ndvi_thresh=0.15, bare_thresh=0.5)
        # 只有第一像元同时满足：低 NDVI + 高裸土 + 大风
        assert src[0, 0] == True
        assert src[0, 1] == False   # 裸土不足
        assert src[0, 2] == False   # NDVI 过高

    def test_no_sources_without_wind(self):
        ndvi = np.full((8, 8), 0.05); bare = np.full((8, 8), 0.9)
        src = ss.identify_sources(ndvi, bare, np.full((8, 8), 2.0), threshold=6.0)
        assert not src.any()


class TestTrajectoryWeight:
    def test_upwind_greater_than_downwind(self):
        """向东输送(90°)：受体西侧(上风方)权重高，东侧(下风方)为 0。"""
        shape = (20, 20)
        receptor = (10.0, 10.0)
        w = ss.trajectory_weight(shape, receptor, wind_dir_deg=90.0)
        upwind = w[10, 3]    # 西侧
        downwind = w[10, 17] # 东侧
        assert abs(upwind - 1.0) < 1e-6
        assert downwind == 0.0

    def test_bounded(self):
        w = ss.trajectory_weight((16, 16), (8.0, 8.0), wind_dir_deg=270.0)
        assert w.min() >= 0.0 and w.max() <= 1.0


class TestSynthetic:
    def test_shapes(self):
        layers, info = ss.generate_synthetic([80, 40, 81, 41])
        for k in ("ndvi", "bare_soil", "wind_speed"):
            assert layers[k].shape == (64, 64)
        assert info["max_wind"] > 6.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [80.0, 40.0, 81.0, 41.0]
        p = str(tmp_path / "s.tif")
        ss.write_geotiff(p, cube, bbox)
        back, bb = ss.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ss.UsageError):
            ss.read_geotiff("/nonexistent/s.tif")
