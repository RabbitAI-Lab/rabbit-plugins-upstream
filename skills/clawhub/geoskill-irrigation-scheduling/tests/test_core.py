"""Core algorithm tests for irrigation-scheduling — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestVaporPressure:
    def test_es_at_25c(self):
        # Tetens: es(25C) ~ 3.17 kPa
        es = mod.saturation_vapor_pressure(25.0)
        assert es == pytest.approx(3.17, abs=0.05)

    def test_es_monotonic_with_temperature(self):
        es10 = mod.saturation_vapor_pressure(10.0)
        es30 = mod.saturation_vapor_pressure(30.0)
        assert es30 > es10

    def test_slope_positive(self):
        assert mod.slope_vapor_curve(20.0) > 0

    def test_gamma_range(self):
        g = mod.psychrometric_constant(0.0)
        assert 0.05 < g < 0.08  # ~0.067 kPa/C at sea level


class TestPenmanMonteith:
    def test_et0_realistic_range(self):
        et0 = mod.penman_monteith_et0(tmean=25.0, wind2=2.0, rh=50.0, rs=20.0,
                                      lat_deg=40.0, doy=190)
        assert 1.0 < et0 < 12.0

    def test_et0_increases_with_temperature(self):
        cool = mod.penman_monteith_et0(15.0, 2.0, 50.0, 20.0, 40.0, 190)
        warm = mod.penman_monteith_et0(30.0, 2.0, 50.0, 20.0, 40.0, 190)
        assert warm > cool

    def test_et0_increases_with_radiation(self):
        low = mod.penman_monteith_et0(25.0, 2.0, 50.0, 8.0, 40.0, 190)
        high = mod.penman_monteith_et0(25.0, 2.0, 50.0, 28.0, 40.0, 190)
        assert high > low

    def test_et0_nonnegative(self):
        et0 = mod.penman_monteith_et0(5.0, 0.5, 90.0, 5.0, 40.0, 30)
        assert et0 >= 0.0

    def test_crop_et_scales_with_kc(self):
        assert mod.crop_et(5.0, 1.2) == pytest.approx(6.0)
        assert mod.crop_et(5.0, 0.0) == 0.0


class TestWaterBalance:
    def _setup(self):
        n = 60
        et0 = np.full(n, 5.0, dtype=np.float32)
        precip = np.zeros(n, dtype=np.float32)  # no rain -> irrigation needed
        kc = np.full(n, 1.0, dtype=np.float32)
        return et0, precip, kc

    def test_taw_formula(self):
        taw = mod.total_available_water(0.30, 0.15, 600.0)
        assert taw == pytest.approx((0.30 - 0.15) * 600.0)

    def test_taw_invalid_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.total_available_water(0.15, 0.30, 600.0)

    def test_irrigation_triggered_without_rain(self):
        et0, precip, kc = self._setup()
        res = mod.soil_water_balance(et0, precip, kc, 0.30, 0.15, 600.0, mad=0.5)
        assert res["n_events"] > 0
        assert res["total_irrigation_mm"] > 0
        # depletion never exceeds threshold after refill (bounded by one step ETc)
        assert res["depletion"].max() <= res["threshold_mm"] + 5.0 + 1e-3

    def test_more_events_when_mad_smaller(self):
        et0, precip, kc = self._setup()
        res_loose = mod.soil_water_balance(et0, precip, kc, 0.30, 0.15, 600.0, mad=0.8)
        res_tight = mod.soil_water_balance(et0, precip, kc, 0.30, 0.15, 600.0, mad=0.2)
        assert res_tight["n_events"] >= res_loose["n_events"]

    def test_rain_reduces_irrigation(self):
        et0, _, kc = self._setup()
        dry = mod.soil_water_balance(et0, np.zeros(60), kc, 0.30, 0.15, 600.0)
        rainy = mod.soil_water_balance(et0, np.full(60, 6.0), kc, 0.30, 0.15, 600.0)
        assert rainy["total_irrigation_mm"] < dry["total_irrigation_mm"]

    def test_length_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.soil_water_balance(np.ones(10), np.ones(5), np.ones(10), 0.3, 0.15, 600.0)


class TestSeasonalGrid:
    def test_dry_soil_needs_more_irrigation(self):
        weather = mod.generate_season_weather(n_days=60, seed=1)
        # wet soil (left) vs sandy dry soil (right)
        fc = np.array([[0.42, 0.25]], dtype=np.float32)
        wp = np.array([[0.20, 0.12]], dtype=np.float32)
        rd = np.array([[600.0, 600.0]], dtype=np.float32)
        soil = np.stack([np.tile(fc, (4, 1)), np.tile(wp, (4, 1)), np.tile(rd, (4, 1))], 0)
        req = mod.seasonal_requirement_grid(soil, weather["et0"], weather["precip"], weather["kc"])
        assert req.shape == (4, 2)
        # sandy (lower TAW) column needs more frequent irrigation -> >= water holding column
        assert req[:, 1].mean() >= req[:, 0].mean()

    def test_wrong_bands_raises(self):
        weather = mod.generate_season_weather(n_days=10)
        with pytest.raises(mod.ValidationError):
            mod.seasonal_requirement_grid(np.zeros((2, 4, 4)), weather["et0"],
                                          weather["precip"], weather["kc"])


class TestWeather:
    def test_et0_series_positive(self):
        w = mod.generate_season_weather(n_days=90, seed=7)
        assert w["et0"].shape == (90,)
        assert (w["et0"] >= 0).all()
        assert w["et0"].mean() > 0
