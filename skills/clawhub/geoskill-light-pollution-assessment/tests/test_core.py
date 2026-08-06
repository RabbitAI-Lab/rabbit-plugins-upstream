"""Core algorithm tests for light-pollution-assessment (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestRadianceToGrade:
    def test_zero_radiance_grade_zero(self):
        grade = M.radiance_to_grade(np.zeros((4, 4), dtype=np.float32))
        assert np.all(grade == 0)

    def test_grade_increases_with_radiance(self):
        rads = np.array([0.0, 0.3, 1.5, 5.0, 20.0, 60.0], dtype=np.float32)
        grade = M.radiance_to_grade(rads.reshape(1, -1))
        # 应严格非递减
        assert np.all(np.diff(grade[0]) >= 0)
        # 6 个不同辐射值应覆盖 0-5 级
        assert set(grade[0].tolist()) == {0, 1, 2, 3, 4, 5}

    def test_threshold_boundaries(self):
        rads = np.array([0.24, 0.25, 0.99, 1.0, 3.99, 4.0], dtype=np.float32)
        grade = M.radiance_to_grade(rads.reshape(1, -1))
        assert grade[0, 0] == 0  # < 0.25
        assert grade[0, 1] == 1  # >= 0.25
        assert grade[0, 2] == 1  # < 1.0
        assert grade[0, 3] == 2  # >= 1.0
        assert grade[0, 4] == 2  # < 4.0
        assert grade[0, 5] == 3  # >= 4.0


class TestEcologicalImpact:
    def test_zero_radiance_zero_impact(self):
        eco = M.ecological_impact_index(np.zeros((4, 4)))
        np.testing.assert_allclose(eco, 0.0, atol=1e-5)

    def test_bounded_0_1(self):
        rng = np.random.default_rng(0)
        rad = rng.uniform(0, 300, (32, 32)).astype(np.float32)
        eco = M.ecological_impact_index(rad)
        assert eco.min() >= 0.0
        assert eco.max() <= 1.0 + 1e-5

    def test_monotonic_with_radiance(self):
        lo = M.ecological_impact_index(np.full((4, 4), 5.0))
        hi = M.ecological_impact_index(np.full((4, 4), 50.0))
        assert float(hi.mean()) > float(lo.mean())

    def test_logarithmic_saturation(self):
        """对数模型：等加性步长下增量递减（凹函数饱和特性）。"""
        r10 = M.ecological_impact_index(np.full((1,), 10.0))[0]
        r20 = M.ecological_impact_index(np.full((1,), 20.0))[0]
        r30 = M.ecological_impact_index(np.full((1,), 30.0))[0]
        # 等步长 10：(r20-r10) > (r30-r20)
        assert (r20 - r10) > (r30 - r20)


class TestSkyglow:
    def test_linear_scaling(self):
        s1 = M.skyglow_proxy(np.full((4, 4), 10.0), scatter_coeff=0.05)
        s2 = M.skyglow_proxy(np.full((4, 4), 10.0), scatter_coeff=0.10)
        np.testing.assert_allclose(s2, s1 * 2.0, rtol=1e-5)

    def test_proportional_to_radiance(self):
        s = M.skyglow_proxy(np.full((4, 4), 20.0), scatter_coeff=0.05)
        np.testing.assert_allclose(s, 1.0, rtol=1e-5)


class TestSynthetic:
    def test_center_brighter_than_edge(self):
        rad, _ = M.generate_synthetic_light([116, 39, 117, 40])
        h, w = rad.shape
        center = rad[h // 2, w // 2]
        corner = rad[0, 0]
        assert center > corner

    def test_positive_radiance(self):
        rad, _ = M.generate_synthetic_light([116, 39, 117, 40])
        assert rad.min() >= 0.0
