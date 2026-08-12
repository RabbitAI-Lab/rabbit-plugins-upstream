"""Core algorithm tests for location-allocation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def small_instance():
    """6 需求点 x 5 候选点，已知结构。"""
    demand = np.array([[0.0, 0.0], [0.1, 0.0], [1.0, 0.0],
                       [1.1, 0.0], [2.0, 0.0], [2.1, 0.0]])
    cand = np.array([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0],
                     [0.5, 0.5], [1.5, 0.5]])
    weights = np.array([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
    return demand, cand, weights


class TestDistanceMatrix:
    def test_shapes(self):
        d = np.zeros((4, 2))
        c = np.zeros((3, 2))
        dm = mod.distance_matrix(d, c)
        assert dm.shape == (4, 3)

    def test_self_zero(self):
        pts = np.array([[0.0, 0.0], [3.0, 4.0]])
        dm = mod.distance_matrix(pts, pts)
        np.testing.assert_allclose(np.diag(dm), 0.0, atol=1e-12)
        np.testing.assert_allclose(dm[0, 1], 5.0, atol=1e-9)

    def test_symmetric(self):
        rng = np.random.default_rng(0)
        pts = rng.uniform(0, 1, (8, 2))
        dm = mod.distance_matrix(pts, pts)
        np.testing.assert_allclose(dm, dm.T, atol=1e-12)


class TestPMedian:
    def test_matches_bruteforce_small(self):
        """贪心+交换解的目标值应等于暴力最优（小实例）。"""
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        for p in [1, 2, 3]:
            res = mod.p_median(dm, weights, p)
            bf_sel, bf_cost = mod.brute_force_p_median(dm, weights, p)
            np.testing.assert_allclose(res["cost"], bf_cost, rtol=1e-9,
                                       err_msg=f"p={p}")

    def test_cost_decreases_with_p(self):
        """增加设施数，总成本不增。"""
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        costs = [mod.p_median(dm, weights, p)["cost"] for p in [1, 2, 3, 4]]
        assert all(costs[i] >= costs[i + 1] - 1e-9 for i in range(len(costs) - 1))

    def test_p_equals_one_selects_best(self):
        """p=1 时选中使加权距离和最小的候选点。"""
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        res = mod.p_median(dm, weights, 1)
        bf_sel, _ = mod.brute_force_p_median(dm, weights, 1)
        assert res["selected"] == sorted(bf_sel)

    def test_assignment_valid(self):
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        res = mod.p_median(dm, weights, 2)
        for a in res["assignment"]:
            assert a in res["selected"]

    def test_p_out_of_range_raises(self):
        dm = np.ones((3, 2))
        with pytest.raises(mod.ValidationError):
            mod.p_median(dm, np.ones(3), p=5)

    def test_weight_mismatch_raises(self):
        dm = np.ones((3, 2))
        with pytest.raises(mod.ValidationError):
            mod.p_median(dm, np.ones(5), p=1)


class TestPCenter:
    def test_matches_bruteforce_small(self):
        """p-center 的最大距离应等于暴力最优。"""
        from itertools import combinations
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        for p in [1, 2, 3]:
            res = mod.p_center(dm, p)
            # 暴力
            best = np.inf
            for combo in combinations(range(dm.shape[1]), p):
                md = dm[:, list(combo)].min(axis=1).max()
                best = min(best, md)
            np.testing.assert_allclose(res["max_distance"], best, rtol=1e-9,
                                       err_msg=f"p={p}")

    def test_maxdist_decreases_with_p(self):
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        mds = [mod.p_center(dm, p)["max_distance"] for p in [1, 2, 3]]
        assert all(mds[i] >= mds[i + 1] - 1e-9 for i in range(len(mds) - 1))


class TestMaxCoverage:
    def test_full_coverage_large_threshold(self):
        """阈值足够大时覆盖全部需求。"""
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        res = mod.max_coverage(dm, weights, p=1, threshold=100.0)
        np.testing.assert_allclose(res["coverage_ratio"], 1.0, atol=1e-9)

    def test_coverage_monotonic_in_p(self):
        demand, cand, weights = small_instance()
        dm = mod.distance_matrix(demand, cand)
        ratios = [mod.max_coverage(dm, weights, p, threshold=0.3)["coverage_ratio"]
                  for p in [1, 2, 3]]
        assert all(ratios[i] <= ratios[i + 1] + 1e-9 for i in range(len(ratios) - 1))

    def test_weighted_coverage_value(self):
        """覆盖需求量 = 阈值内被覆盖需求权重之和。"""
        demand = np.array([[0.0, 0.0], [10.0, 10.0]])
        cand = np.array([[0.0, 0.0]])
        weights = np.array([5.0, 7.0])
        dm = mod.distance_matrix(demand, cand)
        res = mod.max_coverage(dm, weights, p=1, threshold=1.0)
        # 只有需求0在阈值内
        np.testing.assert_allclose(res["covered_demand"], 5.0, atol=1e-9)


class TestSynthetic:
    def test_shapes(self):
        demand, weights, cand, info = mod.generate_synthetic([116, 39, 117, 40])
        assert demand.shape == (60, 2)
        assert weights.shape == (60,)
        assert cand.shape == (20, 2)
