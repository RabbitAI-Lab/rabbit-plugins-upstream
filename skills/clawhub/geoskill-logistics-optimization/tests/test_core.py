"""Core algorithm tests for logistics-optimization."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as lo


class TestDistance:
    def test_matrix_symmetric_zero_diag(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
        d = lo.distance_matrix(coords, metric="euclidean")
        assert np.allclose(d, d.T)
        assert np.allclose(np.diag(d), 0.0)

    def test_euclidean_value(self):
        coords = np.array([[0.0, 0.0], [3.0, 4.0]])
        d = lo.distance_matrix(coords, metric="euclidean")
        assert d[0, 1] == pytest.approx(5.0)

    def test_haversine_known(self):
        # 北京 (116.4,39.9) -> 天津 (117.2,39.1) 约 110-130 km
        d = lo.haversine_km(116.4, 39.9, 117.2, 39.1)
        assert 90.0 < d < 150.0


class TestTSP:
    def test_square_optimal_perimeter(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
        d = lo.distance_matrix(coords, metric="euclidean")
        tour, length = lo.solve_tsp(d, start=0, use_2opt=True)
        # 访问所有节点并回到起点，长度=周长 4
        assert tour[0] == 0 and tour[-1] == 0
        assert sorted(tour[:-1]) == [0, 1, 2, 3]
        assert length == pytest.approx(4.0, abs=1e-6)

    def test_nn_visits_all_once(self):
        rng = np.random.default_rng(0)
        coords = rng.uniform(0, 10, (12, 2))
        d = lo.distance_matrix(coords, metric="euclidean")
        tour = lo.tsp_nearest_neighbor(d, start=0)
        assert tour[0] == 0 and tour[-1] == 0
        assert sorted(tour[:-1]) == list(range(12))

    def test_two_opt_no_worse(self):
        rng = np.random.default_rng(1)
        coords = rng.uniform(0, 100, (20, 2))
        d = lo.distance_matrix(coords, metric="euclidean")
        nn = lo.tsp_nearest_neighbor(d, 0)
        nn_len = lo.tour_length(nn, d)
        opt = lo.two_opt(nn, d)
        assert lo.tour_length(opt, d) <= nn_len + 1e-6
        assert sorted(opt[:-1]) == list(range(20))


class TestVRP:
    def test_capacity_respected_all_served(self):
        rng = np.random.default_rng(2)
        coords = rng.uniform(0, 20, (11, 2))  # 1 depot + 10 customers
        demands = np.concatenate([[0.0], rng.integers(1, 5, 10).astype(float)])
        d = lo.distance_matrix(coords, metric="euclidean")
        capacity = 8.0
        sol = lo.solve_vrp(d, demands, capacity=capacity, use_2opt=True)
        served = []
        for r in sol["routes"]:
            assert r["load"] <= capacity + 1e-6
            served.extend(r["customers"])
        assert sorted(served) == list(range(1, 11))  # 全部客户被服务
        assert sol["total_demand"] == pytest.approx(demands.sum())

    def test_over_capacity_single_raises(self):
        coords = np.array([[0.0, 0.0], [1.0, 1.0]])
        demands = np.array([0.0, 100.0])
        d = lo.distance_matrix(coords, metric="euclidean")
        with pytest.raises(lo.ValidationError):
            lo.solve_vrp(d, demands, capacity=10.0)

    def test_length_mismatch_raises(self):
        d = lo.distance_matrix(np.array([[0.0, 0.0], [1.0, 1.0]]), "euclidean")
        with pytest.raises(lo.ValidationError):
            lo.solve_vrp(d, np.array([0.0, 1.0, 2.0]), capacity=5.0)


class TestTimeWindows:
    def test_feasible_when_wide_windows(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0]])
        d = lo.distance_matrix(coords, metric="euclidean")
        tw_open = np.array([0.0, 0.0, 0.0])
        tw_close = np.array([1e6, 1e6, 1e6])
        feasible, arr = lo.check_time_windows([0, 1, 2, 0], d, tw_open, tw_close, speed=60.0)
        assert feasible is True
        assert len(arr) == 3

    def test_infeasible_when_tight(self):
        coords = np.array([[0.0, 0.0], [100.0, 0.0]])  # 100 km
        d = lo.distance_matrix(coords, metric="euclidean")
        tw_open = np.array([0.0, 0.0])
        tw_close = np.array([1e6, 1.0])  # 节点1须在 1 min 内到达，实际 100km/40kmh=150min
        feasible, _ = lo.check_time_windows([0, 1, 0], d, tw_open, tw_close, speed=40.0)
        assert feasible is False


class TestSynthetic:
    def test_generates_nodes(self):
        coords, demands, info = lo.generate_synthetic_nodes([116, 39, 117, 40], n_customers=10)
        assert coords.shape == (11, 2)
        assert demands[0] == 0.0
        assert (demands[1:] > 0).all()


class TestIO:
    def test_read_geojson_roundtrip(self, tmp_path):
        gj = {"type": "FeatureCollection", "features": [
            {"type": "Feature", "geometry": {"type": "Point", "coordinates": [116.0, 39.0]},
             "properties": {"demand": 0}},
            {"type": "Feature", "geometry": {"type": "Point", "coordinates": [116.5, 39.5]},
             "properties": {"demand": 3}},
            {"type": "Feature", "geometry": {"type": "Point", "coordinates": [117.0, 40.0]},
             "properties": {"demand": 2}},
        ]}
        path = str(tmp_path / "n.geojson")
        import json as _json
        with open(path, "w", encoding="utf-8") as f:
            _json.dump(gj, f)
        coords, demands, bbox = lo.read_nodes_geojson(path)
        assert coords.shape == (3, 2)
        assert list(demands) == [0.0, 3.0, 2.0]
        assert bbox == [116.0, 39.0, 117.0, 40.0]

    def test_missing_raises(self):
        with pytest.raises(lo.UsageError):
            lo.read_nodes_geojson("/nonexistent/n.geojson")
