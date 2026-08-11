"""Core algorithm tests for solar-radiation-modeling."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestSolarGeometry:
    def test_declination_summer_positive(self):
        """夏至附近赤纬应为正（北半球）。"""
        decl = mod.solar_declination(172)
        assert np.rad2deg(decl) > 20  # ~23.45

    def test_declination_winter_negative(self):
        decl = mod.solar_declination(355)
        assert np.rad2deg(decl) < -20

    def test_hour_angle_noon_zero(self):
        assert abs(mod.hour_angle(12.0)) < 1e-12

    def test_hour_angle_sign(self):
        assert mod.hour_angle(9.0) < 0   # 上午
        assert mod.hour_angle(15.0) > 0  # 下午

    def test_elevation_max_at_noon(self):
        """正午太阳高度角最大。"""
        lat = np.deg2rad(40.0)
        decl = mod.solar_declination(172)
        elevs = [mod.solar_elevation(lat, decl, mod.hour_angle(h)) for h in range(4, 21)]
        noon = mod.solar_elevation(lat, decl, mod.hour_angle(12.0))
        assert noon == max(elevs)

    def test_night_elevation_negative(self):
        lat = np.deg2rad(40.0)
        decl = mod.solar_declination(172)
        assert mod.solar_elevation(lat, decl, mod.hour_angle(0.0)) < 0

    def test_summer_noon_elevation_value(self):
        """40°N 夏至正午太阳高度角 ≈ 90 - 40 + 23.45 ≈ 73.45°。"""
        lat = np.deg2rad(40.0)
        decl = mod.solar_declination(172)
        elev = mod.solar_elevation(lat, decl, 0.0)
        assert abs(np.rad2deg(elev) - 73.45) < 1.5


class TestRadiation:
    def test_extraterrestrial_zero_at_night(self):
        assert mod.extraterrestrial_radiation(172, 0.0) == 0.0

    def test_extraterrestrial_near_constant(self):
        val = mod.extraterrestrial_radiation(172, np.deg2rad(45))
        assert 1300 < val < 1450

    def test_transmittance_higher_sun_more(self):
        """太阳越高，大气透过率越大。"""
        t_high = mod.atmospheric_transmittance(np.deg2rad(80))
        t_low = mod.atmospheric_transmittance(np.deg2rad(10))
        assert t_high > t_low

    def test_transmittance_range(self):
        t = mod.atmospheric_transmittance(np.deg2rad(45))
        assert 0 < t <= 1


class TestSlopeAspect:
    def test_flat_zero_slope(self):
        dem = np.full((20, 20), 100.0, dtype=np.float32)
        slope, aspect = mod.slope_aspect(dem, cell_size=30.0)
        np.testing.assert_allclose(slope, 0.0, atol=1e-6)

    def test_tilted_plane_slope(self):
        """均匀倾斜面坡度应一致。"""
        yy, xx = np.mgrid[0:20, 0:20]
        dem = (yy * 10.0).astype(np.float32)  # 每行升 10m，cell 30m → tan≈10/30
        slope, aspect = mod.slope_aspect(dem, cell_size=30.0)
        expected = np.arctan(10.0 / 30.0)
        # 内部像元坡度接近预期
        np.testing.assert_allclose(slope[5:15, 5:15], expected, atol=0.02)


class TestIncidence:
    def test_flat_surface_overhead_sun(self):
        """平地 + 太阳天顶 → cosθ=1。"""
        slope = np.zeros((3, 3))
        aspect = np.zeros((3, 3))
        cos_t = mod.incidence_angle_cos(slope, aspect, np.deg2rad(90), 0.0)
        np.testing.assert_allclose(cos_t, 1.0, atol=1e-6)

    def test_south_slope_more_than_north_summer_noon(self):
        """北半球夏季正午，南向坡入射余弦 > 北向坡。"""
        elev = np.deg2rad(70)
        azim = np.deg2rad(180)  # 太阳正南
        south = np.full((1,), np.deg2rad(180))  # 坡向朝南
        north = np.full((1,), np.deg2rad(0))    # 坡向朝北
        s30 = np.full((1,), np.deg2rad(30))
        cos_south = mod.incidence_angle_cos(s30, south, elev, azim)
        cos_north = mod.incidence_angle_cos(s30, north, elev, azim)
        assert cos_south[0] > cos_north[0]


class TestDailyModel:
    def test_radiation_positive(self):
        dem = np.full((16, 16), 100.0, dtype=np.float32)
        rad, info = mod.model_daily_radiation(dem, 40.0, 172, 30.0, time_step_h=1.0)
        assert rad.mean() > 0
        assert info["sun_up_steps"] > 0

    def test_south_slope_higher_daily(self):
        """南坡日总辐射应高于北坡。"""
        yy, xx = np.mgrid[0:16, 0:16]
        dem_south = (yy * 15.0).astype(np.float32)     # 南坡
        dem_north = ((15 - yy) * 15.0).astype(np.float32)  # 北坡
        rad_s, _ = mod.model_daily_radiation(dem_south, 40.0, 172, 30.0, time_step_h=1.0)
        rad_n, _ = mod.model_daily_radiation(dem_north, 40.0, 172, 30.0, time_step_h=1.0)
        assert rad_s.mean() > rad_n.mean()


class TestSynthetic:
    def test_shapes(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40], grid_size=32)
        assert dem.shape == (32, 32)
