"""Core algorithm tests for irrigation-efficiency."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestEffectivePrecip:
    def test_fixed_ratio(self):
        P = np.array([100.0, 200.0, 400.0])
        pe = mod.effective_precipitation(P, method="fixed", coeff=0.75)
        np.testing.assert_allclose(pe, 0.75 * P)

    def test_pe_le_precip(self):
        P = np.array([0.0, 50.0, 300.0, 800.0])
        for m in ("fixed", "usda"):
            pe = mod.effective_precipitation(P, method=m)
            assert np.all(pe >= 0)
            assert np.all(pe <= P + 1e-9)

    def test_usda_high_rain_lower_fraction(self):
        """强降雨的有效利用比例应低于小雨（USDA 经验式）。"""
        low = mod.effective_precipitation(np.array([50.0]), method="usda")[0]
        high = mod.effective_precipitation(np.array([500.0]), method="usda")[0]
        assert low / 50.0 > high / 500.0

    def test_bad_method_raises(self):
        with pytest.raises(mod.UsageError):
            mod.effective_precipitation(np.array([10.0]), method="nope")

    def test_bad_coeff_raises(self):
        with pytest.raises(mod.UsageError):
            mod.effective_precipitation(np.array([10.0]), method="fixed", coeff=1.5)


class TestCropET:
    def test_et_equals_pet_times_kc(self):
        pet = np.array([500.0, 600.0])
        kc = np.array([1.0, 1.2])
        et = mod.crop_evapotranspiration(pet, kc)
        np.testing.assert_allclose(et, [500.0, 720.0])

    def test_higher_kc_higher_et(self):
        pet = np.full(3, 500.0)
        kc = np.array([0.8, 1.0, 1.2])
        et = mod.crop_evapotranspiration(pet, kc)
        assert np.all(np.diff(et) > 0)

    def test_kc_lookup(self):
        crop = np.array([[1, 2, 3], [0, 4, 6]])
        kc = mod.kc_from_crop(crop)
        assert kc[0, 0] == 1.15   # wheat
        assert kc[1, 0] == 0.30   # fallow
        assert kc[0, 2] == 1.20   # rice


class TestDemand:
    def test_demand_formula(self):
        et = np.array([500.0, 300.0, 700.0])
        pe = np.array([200.0, 400.0, 100.0])
        d = mod.irrigation_demand(et, pe)
        np.testing.assert_allclose(d, [300.0, 0.0, 600.0])

    def test_demand_nonnegative(self):
        d = mod.irrigation_demand(np.array([100.0]), np.array([500.0]))
        assert d[0] == 0.0

    def test_higher_et_higher_demand(self):
        pe = np.full(3, 200.0)
        et = np.array([300.0, 400.0, 500.0])
        d = mod.irrigation_demand(et, pe)
        assert np.all(np.diff(d) > 0)


class TestEfficiency:
    def test_range_0_1(self):
        rng = np.random.default_rng(0)
        demand = rng.uniform(0, 500, 100)
        applied = rng.uniform(0, 800, 100)
        eff = mod.irrigation_efficiency(demand, applied)
        assert eff.min() >= 0.0
        assert eff.max() <= 1.0

    def test_demand_over_applied(self):
        """实灌量 ≥ 需水量时效率 = demand/applied。"""
        demand = np.array([100.0, 200.0])
        applied = np.array([200.0, 500.0])
        eff = mod.irrigation_efficiency(demand, applied)
        np.testing.assert_allclose(eff, [0.5, 0.4])

    def test_under_irrigation_caps_at_1(self):
        demand = np.array([500.0])
        applied = np.array([300.0])
        eff = mod.irrigation_efficiency(demand, applied)
        assert eff[0] == 1.0

    def test_zero_applied_is_zero(self):
        eff = mod.irrigation_efficiency(np.array([100.0]), np.array([0.0]))
        assert eff[0] == 0.0

    def test_deficit(self):
        d = mod.water_deficit(np.array([500.0, 100.0]), np.array([300.0, 400.0]))
        np.testing.assert_allclose(d, [200.0, 0.0])


class TestSyntheticAndIO:
    def test_shapes(self):
        info = mod.generate_synthetic([116, 39, 117, 40], grid_shape=(24, 24))
        assert info["et"].shape == (24, 24)
        assert info["precip"].shape == (24, 24)
        assert info["applied"].shape == (24, 24)
        assert np.all(info["et"] >= 0)

    def test_geotiff_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 500, (3, 12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back, arr, atol=1e-3)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
