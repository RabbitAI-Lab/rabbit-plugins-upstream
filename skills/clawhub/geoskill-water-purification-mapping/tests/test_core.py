"""Core algorithm tests for water-purification-mapping (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestWaterYield:
    def test_water_balance_closes(self):
        """水量平衡：Y = P - AET，且 0 ≤ AET ≤ P。"""
        rng = np.random.default_rng(0)
        p = rng.uniform(400, 1200, (32, 32)).astype(np.float32)
        et0 = rng.uniform(400, 1200, (32, 32)).astype(np.float32)
        awc = rng.uniform(0.1, 0.3, (32, 32)).astype(np.float32)
        y = M.water_yield(p, et0, awc)
        assert y.min() >= 0.0
        assert y.max() <= p.max() + 1.0
        # AET = P - Y ≥ 0
        aet = p - y
        assert aet.min() >= -1e-3

    def test_yield_increases_with_precip(self):
        """更多降雨 → 更多产水（ET0 固定）。"""
        et0 = np.full((4, 4), 600.0, dtype=np.float32)
        awc = np.full((4, 4), 0.2, dtype=np.float32)
        y_lo = M.water_yield(np.full((4, 4), 500.0), et0, awc)
        y_hi = M.water_yield(np.full((4, 4), 1200.0), et0, awc)
        assert float(y_hi.mean()) > float(y_lo.mean())

    def test_yield_decreases_with_et0(self):
        """更高蒸发需求 → 更少产水（P 固定）。"""
        p = np.full((4, 4), 800.0, dtype=np.float32)
        awc = np.full((4, 4), 0.2, dtype=np.float32)
        y_lo = M.water_yield(p, np.full((4, 4), 400.0), awc)
        y_hi = M.water_yield(p, np.full((4, 4), 1200.0), awc)
        assert float(y_hi.mean()) < float(y_lo.mean())

    def test_dry_limit_low_yield(self):
        """极端干燥（ET0 >> P）→ 产水远小于湿润条件（Budyko 特性）。"""
        awc = np.full((4, 4), 0.1, dtype=np.float32)
        y_dry = M.water_yield(np.full((4, 4), 300.0), np.full((4, 4), 3000.0), awc)
        y_wet = M.water_yield(np.full((4, 4), 800.0), np.full((4, 4), 400.0), awc)
        # 干燥条件产水应远小于湿润条件（至少 5 倍差距）
        assert float(y_dry.mean()) < float(y_wet.mean()) / 5.0


class TestRetention:
    def test_high_ndvi_higher_retention(self):
        wy = np.full((4, 4), 100.0, dtype=np.float32)
        r_veg = M.water_retention(wy, np.full((4, 4), 0.8))
        r_bare = M.water_retention(wy, np.full((4, 4), 0.05))
        assert float(r_veg.mean()) > float(r_bare.mean())

    def test_retention_le_yield(self):
        """涵养量 ≤ 产水量（截留系数 ≤ 1）。"""
        wy = np.full((8, 8), 200.0, dtype=np.float32)
        r = M.water_retention(wy, np.full((8, 8), 0.9))
        assert float(r.max()) <= float(wy.max()) + 1e-3

    def test_retention_factor_bounded(self):
        rng = np.random.default_rng(1)
        ndvi = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        f = M.retention_factor(ndvi)
        assert f.min() >= 0.0
        assert f.max() <= 0.85 + 1e-5


class TestNutrientRetention:
    def test_scales_with_load(self):
        ndvi = np.full((4, 4), 0.6, dtype=np.float32)
        n1 = M.nutrient_retention(np.full((4, 4), 50.0), ndvi)
        n2 = M.nutrient_retention(np.full((4, 4), 100.0), ndvi)
        np.testing.assert_allclose(n2, n1 * 2.0, rtol=1e-5)

    def test_vegetation_retains_more(self):
        load = np.full((4, 4), 80.0, dtype=np.float32)
        n_veg = M.nutrient_retention(load, np.full((4, 4), 0.8))
        n_bare = M.nutrient_retention(load, np.full((4, 4), 0.05))
        assert float(n_veg.mean()) > float(n_bare.mean())

    def test_zero_load_zero_retention(self):
        n = M.nutrient_retention(np.zeros((4, 4)), np.full((4, 4), 0.8))
        assert np.all(n == 0.0)
