"""Core algorithm tests for education-resource-allocation."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ed


class TestDistanceMatrix:
    def test_shape_and_value(self):
        a = np.array([[0.0, 0.0], [3.0, 4.0]])
        b = np.array([[0.0, 0.0]])
        d = ed.euclid_distance_matrix(a, b)
        assert d.shape == (2, 1)
        assert d[0, 0] == 0.0
        assert d[1, 0] == pytest.approx(5.0)


class TestAssignStudents:
    def test_capacity_respected(self):
        zones = np.array([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0], [3.0, 0.0]])
        demand = np.array([10.0, 10.0, 10.0, 10.0])
        schools = np.array([[0.0, 0.0], [3.0, 0.0]])
        capacity = np.array([20.0, 20.0])
        res = ed.assign_students(demand, zones, schools, capacity)
        assert all(l <= c + 1e-9 for l, c in zip(res["load"], capacity))
        assert res["served"] == pytest.approx(40.0)
        assert res["unserved"] == pytest.approx(0.0)

    def test_insufficient_capacity_unserved(self):
        zones = np.array([[0.0, 0.0], [1.0, 0.0]])
        demand = np.array([30.0, 30.0])
        schools = np.array([[0.0, 0.0]])
        capacity = np.array([20.0])
        res = ed.assign_students(demand, zones, schools, capacity)
        assert res["load"][0] == pytest.approx(20.0)
        assert res["unserved"] == pytest.approx(40.0)

    def test_zero_demand_all_served(self):
        zones = np.array([[0.0, 0.0]])
        demand = np.array([0.0])
        schools = np.array([[0.0, 0.0]])
        capacity = np.array([10.0])
        res = ed.assign_students(demand, zones, schools, capacity)
        assert res["unserved"] == 0.0


class TestCoverage:
    def test_full_coverage(self):
        demand = np.array([10.0, 20.0])
        assignment = np.array([0, 1])
        assert ed.coverage_fraction(demand, assignment) == pytest.approx(1.0)

    def test_partial_coverage(self):
        demand = np.array([10.0, 30.0])
        assignment = np.array([0, -1])
        assert ed.coverage_fraction(demand, assignment) == pytest.approx(0.25)


class TestEquity:
    def test_gini_equal_is_zero(self):
        assert ed.gini(np.array([5.0, 5.0, 5.0, 5.0])) == pytest.approx(0.0, abs=1e-9)

    def test_equity_equal_is_one(self):
        assert ed.equity_index(np.array([3.0, 3.0, 3.0]), "gini") == pytest.approx(1.0, abs=1e-9)
        assert ed.equity_index(np.array([3.0, 3.0, 3.0]), "cv") == pytest.approx(1.0, abs=1e-9)

    def test_equity_bounds(self):
        rng = np.random.default_rng(0)
        a = rng.uniform(0.1, 10, 50)
        for m in ("gini", "cv"):
            e = ed.equity_index(a, m)
            assert 0.0 <= e <= 1.0

    def test_more_unequal_lower_equity(self):
        equal = np.array([5.0, 5.0, 5.0, 5.0])
        unequal = np.array([0.1, 0.1, 0.1, 20.0])
        assert ed.equity_index(equal, "gini") > ed.equity_index(unequal, "gini")


class TestWeightedAccess:
    def test_nearest_distance(self):
        zones = np.array([[0.0, 0.0], [10.0, 0.0]])
        schools = np.array([[1.0, 0.0]])
        acc = ed.weighted_access(zones, schools)
        assert acc[0] == pytest.approx(1.0)
        assert acc[1] == pytest.approx(9.0)

    def test_no_school_inf(self):
        zones = np.array([[0.0, 0.0]])
        acc = ed.weighted_access(zones, np.zeros((0, 2)))
        assert np.isinf(acc[0])


class TestSiteSelection:
    def test_selection_reduces_cost(self):
        zones = np.array([[0.0, 0.0], [10.0, 0.0], [0.0, 10.0], [10.0, 10.0]])
        demand = np.array([1.0, 1.0, 1.0, 1.0])
        existing = np.array([[0.0, 0.0]])
        candidates = np.array([[10.0, 10.0], [5.0, 5.0]])
        before = float((demand * ed.weighted_access(zones, existing)).sum())
        selected, after = ed.select_new_sites(candidates, zones, demand, k=1, existing=existing)
        assert len(selected) == 1
        assert after <= before
        # 选 (10,10) 能服务三个远区，优于中心点
        assert selected[0] == 0

    def test_k_larger_than_candidates(self):
        zones = np.array([[0.0, 0.0], [10.0, 0.0]])
        demand = np.array([1.0, 1.0])
        candidates = np.array([[0.0, 0.0]])
        selected, _ = ed.select_new_sites(candidates, zones, demand, k=5)
        assert selected == [0]

    def test_no_candidates(self):
        zones = np.array([[0.0, 0.0]])
        demand = np.array([1.0])
        selected, cost = ed.select_new_sites(np.zeros((0, 2)), zones, demand, k=2,
                                             existing=np.array([[0.0, 0.0]]))
        assert selected == []
        assert cost == pytest.approx(0.0)


class TestAggregate:
    def test_zone_demand_sum(self):
        pop = np.ones((16, 16), dtype=np.float32)  # 每区 4x4=16 像元
        demand = ed.aggregate_zone_demand(pop, 4, 4)
        assert demand.shape == (16,)
        assert demand[0] == pytest.approx(16 * 0.12)


class TestSyntheticAndIO:
    def test_synthetic_shapes(self):
        cube, info = ed.generate_synthetic_scene([116, 39, 117, 40], seed=1)
        assert cube.shape == (1, 128, 128)
        assert len(info["schools_rc"]) == 2

    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (1, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "e.tif")
        ed.write_geotiff(path, cube, bbox)
        back, rb = ed.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ed.UsageError):
            ed.read_geotiff("/nonexistent/e.tif")
