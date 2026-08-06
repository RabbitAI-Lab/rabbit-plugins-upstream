"""Core algorithm tests for soil-erosion-modeling (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestRFactor:
    def test_zero_precip_zero_R(self):
        r = M.r_factor(np.zeros((4, 4)))
        assert np.all(r == 0.0)

    def test_scales_with_precip(self):
        r1 = M.r_factor(np.full((4, 4), 500.0))
        r2 = M.r_factor(np.full((4, 4), 1000.0))
        np.testing.assert_allclose(r2, r1 * 2.0, rtol=1e-5)


class TestKFactor:
    def test_lookup_values(self):
        codes = np.array([[0, 1, 2, 3]], dtype=np.int8)
        k = M.k_factor(codes)
        np.testing.assert_allclose(k[0], [0.05, 0.32, 0.25, 0.42], rtol=1e-5)

    def test_silt_most_erodible(self):
        # 粉砂（code 3）应最高
        codes = np.array([[0, 1, 2, 3]], dtype=np.int8)
        k = M.k_factor(codes)
        assert k[0, 3] == k[0].max()


class TestLSFactor:
    def test_flat_low_ls(self):
        slope = np.zeros((4, 4), dtype=np.float32)
        flow = np.ones((4, 4), dtype=np.float32)
        ls = M.ls_factor(slope, flow)
        assert ls.max() < 0.5  # 平地 LS 很小

    def test_ls_increases_with_slope(self):
        flow = np.ones((4, 4), dtype=np.float32)
        ls_lo = M.ls_factor(np.full((4, 4), 5.0), flow)
        ls_hi = M.ls_factor(np.full((4, 4), 30.0), flow)
        assert float(ls_hi.mean()) > float(ls_lo.mean())

    def test_ls_increases_with_flow_accum(self):
        slope = np.full((4, 4), 15.0, dtype=np.float32)
        ls_lo = M.ls_factor(slope, np.ones((4, 4)))
        ls_hi = M.ls_factor(slope, np.full((4, 4), 100.0))
        assert float(ls_hi.mean()) > float(ls_lo.mean())


class TestCFactor:
    def test_range_0_1(self):
        rng = np.random.default_rng(0)
        ndvi = rng.uniform(-0.2, 1.0, (32, 32)).astype(np.float32)
        c = M.c_factor(ndvi)
        assert c.min() >= 0.0
        assert c.max() <= 1.0

    def test_high_ndvi_low_C(self):
        """植被覆盖好 → C 小。"""
        c_veg = M.c_factor(np.full((4, 4), 0.8))
        c_bare = M.c_factor(np.full((4, 4), 0.05))
        assert float(c_veg.mean()) < float(c_bare.mean())

    def test_bare_near_one(self):
        c = M.c_factor(np.zeros((4, 4)))
        np.testing.assert_allclose(c, 1.0, atol=0.02)


class TestPFactor:
    def test_lookup_values(self):
        codes = np.array([[0, 1, 2]], dtype=np.int8)
        p = M.p_factor(codes)
        np.testing.assert_allclose(p[0], [1.0, 0.55, 0.25], rtol=1e-5)

    def test_terracing_lowest(self):
        codes = np.array([[0, 1, 2]], dtype=np.int8)
        p = M.p_factor(codes)
        assert p[0, 2] == p[0].min()


class TestRUSLE:
    def test_product_of_factors(self):
        """侵蚀模数 = R×K×LS×C×P，物理乘积。"""
        r = np.full((4, 4), 100.0, dtype=np.float32)
        k = np.full((4, 4), 0.3, dtype=np.float32)
        ls = np.full((4, 4), 2.0, dtype=np.float32)
        c = np.full((4, 4), 0.5, dtype=np.float32)
        p = np.full((4, 4), 0.8, dtype=np.float32)
        a = M.rusle(r, k, ls, c, p)
        np.testing.assert_allclose(a, 100 * 0.3 * 2 * 0.5 * 0.8, rtol=1e-5)

    def test_zero_C_zero_erosion(self):
        r = np.full((4, 4), 100.0)
        k = np.full((4, 4), 0.3)
        ls = np.full((4, 4), 2.0)
        c = np.zeros((4, 4))
        p = np.full((4, 4), 1.0)
        a = M.rusle(r, k, ls, c, p)
        assert np.all(a == 0.0)

    def test_proportional_to_R(self):
        k = np.full((4, 4), 0.3)
        ls = np.full((4, 4), 2.0)
        c = np.full((4, 4), 0.5)
        p = np.full((4, 4), 1.0)
        a1 = M.rusle(np.full((4, 4), 100.0), k, ls, c, p)
        a2 = M.rusle(np.full((4, 4), 200.0), k, ls, c, p)
        np.testing.assert_allclose(a2, a1 * 2.0, rtol=1e-5)


class TestErosionGrade:
    def test_grading(self):
        a = np.array([[100, 600, 3000, 6000, 9000]], dtype=np.float32)
        grade = M.erosion_grade(a)
        assert grade[0, 0] == 0  # < 500
        assert grade[0, 1] == 1  # >= 500
        assert grade[0, 2] == 2  # >= 2500
        assert grade[0, 3] == 3  # >= 5000
        assert grade[0, 4] == 4  # >= 8000
