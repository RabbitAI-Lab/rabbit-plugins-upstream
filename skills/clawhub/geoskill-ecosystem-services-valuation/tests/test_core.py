"""Core algorithm tests for ecosystem-services-valuation (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestClassifyLULC:
    def test_forest_high_ndvi(self):
        codes = M.classify_lulc(np.full((8, 8), 0.70, dtype=np.float32))
        assert np.all(codes == 0)  # forest

    def test_water_negative_ndvi(self):
        codes = M.classify_lulc(np.full((8, 8), -0.10, dtype=np.float32))
        assert np.all(codes == 3)  # water

    def test_built_low_positive(self):
        codes = M.classify_lulc(np.full((8, 8), 0.05, dtype=np.float32))
        assert np.all(codes == 4)  # built/bare

    def test_mixed_scene(self):
        ndvi = np.array([[-0.1, 0.05, 0.20, 0.45, 0.70]], dtype=np.float32)
        codes = M.classify_lulc(ndvi)
        assert codes[0, 0] == 3
        assert codes[0, 1] == 4
        assert codes[0, 2] == 2
        assert codes[0, 3] == 1
        assert codes[0, 4] == 0


class TestServiceValues:
    def test_shape(self):
        vals = M.compute_service_values(np.zeros((16, 16), dtype=np.int8), 1.0)
        assert vals.shape == (4, 16, 16)

    def test_forest_regulating_highest(self):
        vals = M.compute_service_values(np.zeros((8, 8), dtype=np.int8), 1.0)
        # forest (2.01, 6.30, 3.02, 0.78) → regulating 最大
        assert float(vals[1].mean()) > float(vals[0].mean())
        assert float(vals[1].mean()) > float(vals[2].mean())

    def test_built_much_lower_than_forest(self):
        built = M.compute_service_values(np.full((8, 8), 4, dtype=np.int8), 1.0)
        forest = M.compute_service_values(np.zeros((8, 8), dtype=np.int8), 1.0)
        # built (0, 0.10, 0.05, 0.01) << forest (2.01, 6.30, 3.02, 0.78)
        assert float(built.sum()) < 0.05 * float(forest.sum())

    def test_scales_with_area(self):
        codes = np.zeros((8, 8), dtype=np.int8)
        v1 = M.compute_service_values(codes, 1.0)
        v2 = M.compute_service_values(codes, 2.0)
        np.testing.assert_allclose(v2, v1 * 2.0, rtol=1e-5)

    def test_scales_with_unit_value(self):
        codes = np.full((4, 4), 1, dtype=np.int8)
        v1 = M.compute_service_values(codes, 1.0, unit_value=3000)
        v2 = M.compute_service_values(codes, 1.0, unit_value=6000)
        np.testing.assert_allclose(v2, v1 * 2.0, rtol=1e-5)

    def test_total_conservation(self):
        """总价值 = 各像元价值之和（能量守恒式校验）。"""
        codes = np.zeros((4, 4), dtype=np.int8)
        vals = M.compute_service_values(codes, 2.0)
        for si in range(4):
            expected = M.EQUIV_FACTOR_TABLE["forest"][si] * M.EQUIV_UNIT_VALUE * 2.0 * 16
            np.testing.assert_allclose(float(np.sum(vals[si])), expected, rtol=1e-4)


class TestSynthetic:
    def test_ndvi_range(self):
        ndvi, info = M.generate_synthetic_esv([116, 39, 117, 40])
        assert ndvi.min() >= -0.5
        assert ndvi.max() <= 1.0
        assert ndvi.shape == (128, 128)
