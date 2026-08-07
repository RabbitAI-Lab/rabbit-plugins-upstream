"""Core algorithm tests for environmental-impact-assessment (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestNormalize:
    def test_bounds(self):
        rng = np.random.default_rng(0)
        a = rng.uniform(-10, 10, (16, 16)).astype(np.float32)
        n = M.normalize_factor(a)
        assert n.min() >= 0.0
        assert n.max() <= 1.0

    def test_constant_zero(self):
        n = M.normalize_factor(np.full((8, 8), 5.0))
        assert np.all(n == 0.0)


class TestWeightedOverlay:
    def test_exact_weighted_mean(self):
        """I = Σ(wi×fi)/Σwi：单像元手算验证。"""
        f1 = np.full((4, 4), 0.2, dtype=np.float32)
        f2 = np.full((4, 4), 0.6, dtype=np.float32)
        factors = np.stack([f1, f2], axis=0)
        out = M.weighted_overlay(factors, [0.3, 0.7])
        expected = (0.3 * 0.2 + 0.7 * 0.6) / 1.0  # = 0.48
        np.testing.assert_allclose(out, expected, rtol=1e-5)

    def test_equal_weights_is_mean(self):
        rng = np.random.default_rng(1)
        factors = rng.uniform(0, 1, (3, 8, 8)).astype(np.float32)
        out = M.weighted_overlay(factors, [1.0, 1.0, 1.0])
        np.testing.assert_allclose(out, factors.mean(axis=0), rtol=1e-5)

    def test_output_bounded(self):
        rng = np.random.default_rng(2)
        factors = rng.uniform(0, 1, (4, 16, 16)).astype(np.float32)
        out = M.weighted_overlay(factors, M.DEFAULT_WEIGHTS)
        assert out.min() >= 0.0
        assert out.max() <= 1.0

    def test_zero_weights_raises(self):
        factors = np.zeros((2, 4, 4), dtype=np.float32)
        with pytest.raises(M.UsageError):
            M.weighted_overlay(factors, [0.0, 0.0])


class TestCumulativeImpact:
    def test_single_project_identity(self):
        """单项目累积 = 该项目本身。"""
        imp = np.full((1, 4, 4), 0.3, dtype=np.float32)
        c = M.cumulative_impact(imp)
        np.testing.assert_allclose(c, 0.3, rtol=1e-5)

    def test_cumulative_geq_each(self):
        """累积效应 ≥ 任一单独项目。"""
        rng = np.random.default_rng(3)
        impacts = rng.uniform(0, 0.5, (3, 8, 8)).astype(np.float32)
        c = M.cumulative_impact(impacts)
        for i in range(3):
            assert np.all(c >= impacts[i] - 1e-6)

    def test_probability_formula(self):
        """两个 0.5 项目：C = 1-(1-0.5)² = 0.75。"""
        imp = np.full((2, 4, 4), 0.5, dtype=np.float32)
        c = M.cumulative_impact(imp)
        np.testing.assert_allclose(c, 0.75, rtol=1e-5)

    def test_bounded_below_one(self):
        """多项目叠加也不超过 1（概率叠加特性）。"""
        imp = np.full((5, 4, 4), 0.9, dtype=np.float32)
        c = M.cumulative_impact(imp)
        assert c.max() <= 1.0


class TestImpactGrade:
    def test_grading_thresholds(self):
        idx = np.array([[0.05, 0.15, 0.35, 0.55, 0.75]], dtype=np.float32)
        grade = M.impact_grade(idx)
        assert grade[0, 0] == 0  # negligible
        assert grade[0, 1] == 1  # minor
        assert grade[0, 2] == 2  # moderate
        assert grade[0, 3] == 3  # significant
        assert grade[0, 4] == 4  # severe

    def test_monotonic(self):
        rng = np.random.default_rng(4)
        idx = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        grade = M.impact_grade(idx)
        assert grade.min() >= 0
        assert grade.max() <= 4
        # 指数越高，平均等级越高
        lo = M.impact_grade(np.full((4, 4), 0.05)).mean()
        hi = M.impact_grade(np.full((4, 4), 0.9)).mean()
        assert hi > lo
