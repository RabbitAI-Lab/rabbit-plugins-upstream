"""Core algorithm tests for farmland-productivity — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestNdviIntegral:
    def test_constant_series_exact(self):
        # constant NDVI 0.5 over 10 steps, dt=16 -> integral = 0.5 * 9 * 16 = 72
        series = np.full((10, 4, 4), 0.5, dtype=np.float32)
        integ = mod.ndvi_integral(series, dt_days=16.0)
        assert integ.shape == (4, 4)
        np.testing.assert_allclose(integ, 72.0, atol=1e-3)

    def test_higher_ndvi_higher_integral(self):
        low = np.full((12, 3, 3), 0.3, dtype=np.float32)
        high = np.full((12, 3, 3), 0.7, dtype=np.float32)
        assert mod.ndvi_integral(high).mean() > mod.ndvi_integral(low).mean()

    def test_integral_proportional_to_biomass(self):
        # double the vegetation amplitude -> double the integral (biomass proxy)
        t = np.linspace(0, 1, 12)
        phen = np.exp(-((t - 0.5) ** 2) / (2 * 0.15 ** 2))
        s1 = (0.1 + 0.3 * phen)[:, None, None] * np.ones((1, 2, 2))
        s2 = (0.1 + 0.6 * phen)[:, None, None] * np.ones((1, 2, 2))
        i1 = mod.ndvi_integral(s1).mean()
        i2 = mod.ndvi_integral(s2).mean()
        assert i2 > i1

    def test_single_step_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.ndvi_integral(np.zeros((1, 4, 4), dtype=np.float32))

    def test_wrong_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.ndvi_integral(np.zeros((4, 4), dtype=np.float32))


class TestClimateCorrection:
    def test_normal_is_unity(self):
        assert mod.climate_correction_factor(0.0, 0.0) == pytest.approx(1.0)

    def test_wet_year_boosts(self):
        f = mod.climate_correction_factor(precip_anomaly_pct=20.0, temp_anomaly_c=0.0)
        assert f > 1.0

    def test_hot_year_reduces(self):
        f = mod.climate_correction_factor(precip_anomaly_pct=0.0, temp_anomaly_c=3.0)
        assert f < 1.0

    def test_clipped_range(self):
        f_hi = mod.climate_correction_factor(precip_anomaly_pct=500.0, temp_anomaly_c=-50.0)
        f_lo = mod.climate_correction_factor(precip_anomaly_pct=-500.0, temp_anomaly_c=50.0)
        assert f_hi <= 1.5
        assert f_lo >= 0.5


class TestProductivityIndex:
    def test_range_01(self):
        integ = np.random.default_rng(0).uniform(0, 100, (8, 8)).astype(np.float32)
        pi = mod.productivity_index(integ, climate_factor=1.0)
        assert pi.min() >= 0.0 and pi.max() <= 1.0

    def test_climate_factor_scales(self):
        integ = np.full((4, 4), 50.0, dtype=np.float32)
        pi_normal = mod.productivity_index(integ, climate_factor=1.0, ref_integral=100.0)
        pi_wet = mod.productivity_index(integ, climate_factor=1.3, ref_integral=100.0)
        assert pi_wet.mean() > pi_normal.mean()

    def test_invalid_ref_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.productivity_index(np.ones((2, 2)), ref_integral=0.0)


class TestGrade:
    def test_thresholds(self):
        pi = np.array([[0.2, 0.5, 0.7, 0.9]], dtype=np.float32)
        g = mod.grade_productivity(pi)
        assert g[0, 0] == 0
        assert g[0, 1] == 1
        assert g[0, 2] == 2
        assert g[0, 3] == 3


class TestPipeline:
    def test_high_yield_side_higher_pi(self):
        series, info = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.assess_productivity(series, dt_days=info["dt_days"])
        pi = res["productivity_index"]
        h, w = pi.shape
        left = pi[:, :int(w * 0.2)].mean()    # high yield
        right = pi[:, int(w * 0.8):].mean()   # low yield
        assert left > right
        assert 0.0 <= pi.min() and pi.max() <= 1.0

    def test_hot_anomaly_lowers_pi(self):
        series, info = mod.generate_synthetic([116, 39, 117, 40])
        normal = mod.assess_productivity(series, dt_days=info["dt_days"])
        hot = mod.assess_productivity(series, dt_days=info["dt_days"], temp_anomaly_c=4.0)
        assert hot["stats"]["mean_pi"] <= normal["stats"]["mean_pi"]
