"""Core algorithm tests for carbon-stock-estimation (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestAGB:
    def test_zero_ndvi_zero_agb(self):
        agb = M.agb_from_ndvi(np.zeros((8, 8), dtype=np.float32))
        assert np.all(agb == 0.0)

    def test_exact_power_law(self):
        agb = M.agb_from_ndvi(np.full((8, 8), 0.5, dtype=np.float32), scale=200.0, power=2.0)
        np.testing.assert_allclose(agb, 200.0 * 0.25, rtol=1e-5)

    def test_monotonic_with_ndvi(self):
        lo = M.agb_from_ndvi(np.full((4, 4), 0.3))
        hi = M.agb_from_ndvi(np.full((4, 4), 0.7))
        assert float(hi.mean()) > float(lo.mean())


class TestCarbonConversion:
    def test_carbon_equals_biomass_times_fraction(self):
        biomass = np.full((8, 8), 100.0, dtype=np.float32)
        carbon = M.carbon_from_biomass(biomass, carbon_fraction=0.47)
        np.testing.assert_allclose(carbon, 47.0, rtol=1e-5)

    def test_linear_scaling(self):
        c1 = M.carbon_from_biomass(np.full((4, 4), 100.0))
        c2 = M.carbon_from_biomass(np.full((4, 4), 200.0))
        np.testing.assert_allclose(c2, c1 * 2.0, rtol=1e-5)


class TestSoilCarbon:
    def test_forest_higher_than_bare(self):
        soc_f = M.soil_carbon(np.zeros((8, 8), dtype=np.int8), 1.0)
        soc_b = M.soil_carbon(np.full((8, 8), 3, dtype=np.int8), 1.0)
        assert float(soc_f.mean()) > float(soc_b.mean())

    def test_water_zero(self):
        soc = M.soil_carbon(np.full((4, 4), 4, dtype=np.int8), 1.0)
        assert np.all(soc == 0.0)

    def test_scales_with_area(self):
        codes = np.zeros((4, 4), dtype=np.int8)
        s1 = M.soil_carbon(codes, 1.0)
        s2 = M.soil_carbon(codes, 3.0)
        np.testing.assert_allclose(s2, s1 * 3.0, rtol=1e-5)


class TestTotalCarbon:
    def test_root_shoot_ratio(self):
        agb_c = np.full((8, 8), 47.0, dtype=np.float32)
        tc = M.total_carbon(agb_c, root_shoot_ratio=0.3)
        np.testing.assert_allclose(tc, 47.0 * 1.3, rtol=1e-4)

    def test_adds_soc(self):
        agb_c = np.full((4, 4), 10.0, dtype=np.float32)
        soc = np.full((4, 4), 20.0, dtype=np.float32)
        tc = M.total_carbon(agb_c, root_shoot_ratio=0.0, soc=soc)
        np.testing.assert_allclose(tc, 30.0, rtol=1e-5)

    def test_total_is_sum_of_pools(self):
        """总碳 = 地上碳×(1+R/S) + 土壤碳，物理守恒。"""
        rng = np.random.default_rng(0)
        agb_c = rng.uniform(0, 50, (16, 16)).astype(np.float32)
        soc = rng.uniform(0, 30, (16, 16)).astype(np.float32)
        tc = M.total_carbon(agb_c, root_shoot_ratio=0.25, soc=soc)
        expected = agb_c * 1.25 + soc
        np.testing.assert_allclose(tc, expected, rtol=1e-5)
