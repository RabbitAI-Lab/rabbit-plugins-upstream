"""Core algorithm tests for frost-risk-mapping."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestTerrainAttributes:
    def test_south_descending_plane_aspect(self):
        """向南下降的平面 → 坡向 ≈ 180°（南），坡度 = 倾角。"""
        plane = np.tile(np.arange(64, 0, -1, dtype=float)[:, None], (1, 64))
        slope, aspect = mod.terrain_attributes(plane, res_m=1.0)
        assert abs(float(aspect[32, 32]) - 180.0) < 1.0
        assert abs(float(slope[32, 32]) - 45.0) < 1.0

    def test_east_descending_plane_aspect(self):
        """向东下降的平面 → 坡向 ≈ 90°（东）。"""
        plane = np.tile(np.arange(64, 0, -1, dtype=float)[None, :], (64, 1))
        slope, aspect = mod.terrain_attributes(plane, res_m=1.0)
        assert abs(float(aspect[32, 32]) - 90.0) < 1.0

    def test_flat_zero_slope(self):
        flat = np.full((16, 16), 100.0)
        slope, aspect = mod.terrain_attributes(flat, res_m=1.0)
        assert float(np.max(slope)) < 1e-6

    def test_wrong_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.terrain_attributes(np.zeros((4, 4, 4)))


class TestAspectCorrection:
    def test_south_warmer_north_colder(self):
        south = float(mod.aspect_correction(np.array([180.0]), np.array([20.0]))[0])
        north = float(mod.aspect_correction(np.array([0.0]), np.array([20.0]))[0])
        assert south > 0
        assert north < 0
        assert south > north

    def test_zero_slope_zero_effect(self):
        corr = mod.aspect_correction(np.array([180.0, 0.0]), np.array([0.0, 0.0]))
        np.testing.assert_allclose(corr, [0.0, 0.0], atol=1e-9)


class TestColdAirPooling:
    def test_basin_negative_flat_zero(self):
        dem = np.full((21, 21), 500.0)
        dem[10, 10] = 100.0  # 单点洼地
        anomaly = mod.cold_air_pooling(dem, radius=3)
        assert float(anomaly[10, 10]) < 0
        # 远离洼地处无降温
        assert abs(float(anomaly[0, 0])) < 1e-6

    def test_capped(self):
        dem = np.full((21, 21), 1000.0)
        dem[10, 10] = 0.0
        anomaly = mod.cold_air_pooling(dem, radius=3, pool_factor=0.5, cap=-6.0)
        assert float(anomaly[10, 10]) >= -6.0


class TestApplyTerrainCorrection:
    def test_temperature_decreases_with_elevation(self):
        """单调斜坡（无洼地）上，高程越高最低温越低（递减率主导）。"""
        dem = np.tile(np.linspace(0.0, 1000.0, 64)[:, None], (1, 64))
        base = np.full((64, 64), 5.0)
        ts = apply(base, dem)
        # 同列内部两像元：高 elevation 更冷
        t_low = float(ts[0, 10, 32])
        t_high = float(ts[0, 50, 32])
        assert dem[10, 32] < dem[50, 32]
        assert t_high < t_low

    def test_basin_colder_than_surroundings(self):
        """洼地中心经冷池修正后比平坦背景更冷。"""
        dem = np.full((31, 31), 500.0)
        dem[15, 15] = 200.0  # 单点洼地
        base = np.full((31, 31), 5.0)
        ts = apply(base, dem)
        # 洼地中心应冷于远处平坦背景
        assert float(ts[0, 15, 15]) < float(ts[0, 3, 3])

    def test_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            apply(np.zeros((5, 4, 4)), np.zeros((3, 3)))


def apply(base, dem):
    """helper：把平坦参考温度包成 (1,H,W) 时序后做地形修正。"""
    return mod.apply_terrain_correction(base[np.newaxis, ...], dem)


class TestFrostFrequency:
    def test_known_frequency(self):
        ts = np.array([1.0, -1.0, -2.0, 3.0, -1.0]).reshape(5, 1, 1)
        freq = mod.frost_frequency(ts, threshold=0.0)
        assert abs(float(freq[0, 0]) - 0.6) < 1e-6

    def test_no_frost(self):
        ts = np.full((4, 2, 2), 5.0)
        freq = mod.frost_frequency(ts, threshold=0.0)
        assert np.all(freq == 0.0)

    def test_wrong_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.frost_frequency(np.zeros((4, 4)))


class TestFrostSeason:
    def test_known_season(self):
        series = np.array([5, 3, -1, -2, 4, 5, 6, -3], dtype=float).reshape(8, 1, 1)
        s = mod.frost_season(series, threshold=0.0)
        assert int(s["first_frost"][0, 0]) == 2
        assert int(s["last_frost"][0, 0]) == 7
        assert int(s["frost_days"][0, 0]) == 3
        assert int(s["frost_free_period"][0, 0]) == 3  # idx 4,5,6

    def test_no_frost(self):
        series = np.full((5, 1, 1), 10.0)
        s = mod.frost_season(series, threshold=0.0)
        assert int(s["first_frost"][0, 0]) == -1
        assert int(s["last_frost"][0, 0]) == -1
        assert int(s["frost_free_period"][0, 0]) == 5


class TestFrostRiskClass:
    def test_levels(self):
        freq = np.array([0.0, 0.05, 0.2, 0.5, 0.8])
        risk = mod.frost_risk_class(freq)
        np.testing.assert_array_equal(risk, [0, 1, 2, 3, 4])

    def test_boundaries(self):
        freq = np.array([0.1, 0.3, 0.6])
        risk = mod.frost_risk_class(freq)
        np.testing.assert_array_equal(risk, [1, 2, 3])


class TestSynthetic:
    def test_shapes(self):
        dem, tmin, info = mod.generate_synthetic([116, 39, 117, 40], n_dates=20)
        assert dem.shape == (64, 64)
        assert tmin.shape[0] == 20
        assert tmin.shape[1:] == dem.shape
        assert info["dem_max"] > info["dem_min"]

    def test_hilltop_and_basin_colder_than_plain(self):
        """山脊与洼地均比平原更冷、霜冻风险更高。"""
        dem, tmin, info = mod.generate_synthetic([116, 39, 117, 40], n_dates=30, seed=42)
        meant = tmin.mean(axis=0)
        freq = mod.frost_frequency(tmin, 0.0)
        risk = mod.frost_risk_class(freq)
        hill = np.unravel_index(int(np.argmax(dem)), dem.shape)
        plain = (5, 55)
        basin = (32, 32)
        assert float(meant[hill]) < float(meant[plain])
        assert float(meant[basin]) < float(meant[plain])
        assert int(risk[hill]) >= int(risk[plain])
        assert int(risk[basin]) >= int(risk[plain])

    def test_risk_has_diversity(self):
        """合成场景风险等级应有多样性（至少 3 个等级出现）。"""
        dem, tmin, info = mod.generate_synthetic([116, 39, 117, 40], n_dates=30, seed=7)
        freq = mod.frost_frequency(tmin, 0.0)
        risk = mod.frost_risk_class(freq)
        assert len(np.unique(risk)) >= 3


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(2).uniform(-5, 10, (5, 16, 16)).astype(np.float32)
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
