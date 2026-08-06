"""Core algorithm tests for service-area-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def line_graph(n=5, w=1.0):
    """0-1-2-...(n-1) 线性图。"""
    edges = [(i, i + 1, w) for i in range(n - 1)]
    return mod.build_adjacency(edges, n)


class TestAdjacency:
    def test_undirected(self):
        adj = mod.build_adjacency([(0, 1, 2.0)], 2)
        assert (1, 2.0) in adj[0]
        assert (0, 2.0) in adj[1]

    def test_negative_weight_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.build_adjacency([(0, 1, -1.0)], 2)

    def test_invalid_node_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.build_adjacency([(0, 5, 1.0)], 3)


class TestDijkstra:
    def test_line_distances(self):
        adj = line_graph(5, w=1.0)
        d = mod.dijkstra(adj, 0)
        np.testing.assert_allclose(d, [0, 1, 2, 3, 4], atol=1e-12)

    def test_shortest_chooses_shortcut(self):
        """0->1->2->3 = 3，但 0->3 直达 = 1。"""
        edges = [(0, 1, 1.0), (1, 2, 1.0), (2, 3, 1.0), (0, 3, 1.0)]
        adj = mod.build_adjacency(edges, 4)
        d = mod.dijkstra(adj, 0)
        assert d[3] == 1.0

    def test_unreachable_inf(self):
        edges = [(0, 1, 1.0)]  # 节点 2 孤立
        adj = mod.build_adjacency(edges, 3)
        d = mod.dijkstra(adj, 0)
        assert np.isinf(d[2])

    def test_source_out_of_range_raises(self):
        adj = line_graph(3)
        with pytest.raises(mod.ValidationError):
            mod.dijkstra(adj, 99)


class TestServiceArea:
    def test_coverage_within_threshold(self):
        adj = line_graph(10, w=1.0)
        sa = mod.service_area(adj, [0], threshold=3.0)
        # 节点 0..3 可达（距离 0..3）
        assert sa["covered_count"] == 4
        assert sa["reachable_any"][:4].all()
        assert not sa["reachable_any"][4]

    def test_nearest_facility(self):
        adj = line_graph(10, w=1.0)
        sa = mod.service_area(adj, [0, 9], threshold=100.0)
        # 前半归设施0，后半归设施1
        assert sa["nearest_facility"][0] == 0
        assert sa["nearest_facility"][9] == 1
        assert sa["nearest_facility"][2] == 0
        assert sa["nearest_facility"][7] == 1

    def test_no_facilities_raises(self):
        adj = line_graph(5)
        with pytest.raises(mod.ValidationError):
            mod.service_area(adj, [], threshold=1.0)

    def test_threshold_excludes_far(self):
        adj = line_graph(10, w=1.0)
        sa = mod.service_area(adj, [0, 9], threshold=2.0)
        # 中间节点（4,5）距两设施都>2 → nearest=-1
        assert sa["nearest_facility"][4] == -1


class TestCoverageByThreshold:
    def test_monotonic_increasing(self):
        adj = line_graph(20, w=1.0)
        cov = mod.coverage_by_threshold(adj, [0], [1.0, 5.0, 10.0, 100.0])
        counts = [c["covered_nodes"] for c in cov]
        assert counts == sorted(counts)
        assert counts[-1] == 20

    def test_demand_weighted(self):
        adj = line_graph(5, w=1.0)
        demand = np.array([10.0, 10.0, 10.0, 10.0, 10.0])
        cov = mod.coverage_by_threshold(adj, [0], [2.0], demand=demand)
        assert cov[0]["covered_nodes"] == 3
        assert cov[0]["covered_demand"] == 30.0
        assert cov[0]["total_demand"] == 50.0


class TestSynthetic:
    def test_grid_shapes(self):
        coords, edges, info = mod.generate_synthetic([116, 39, 117, 40], grid_n=8)
        assert coords.shape == (64, 2)
        assert info["n_edges"] > 0

    def test_grid_connected(self):
        """格网应全连通：从 0 出发所有节点可达。"""
        coords, edges, info = mod.generate_synthetic([116, 39, 117, 40], grid_n=6)
        adj = mod.build_adjacency(edges, info["n_nodes"])
        d = mod.dijkstra(adj, 0)
        assert np.all(np.isfinite(d))
