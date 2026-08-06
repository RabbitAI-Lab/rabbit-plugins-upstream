"""Core algorithm tests for network-routing."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def square_graph():
    """4 节点正方形 + 一条对角捷径。
    0(0,0) 1(1,0) 2(1,1) 3(0,1)，边权=欧氏，外加 0-2 对角=1.41。
    """
    coords = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
    def e(u, v):
        d = float(np.linalg.norm(coords[u] - coords[v]))
        return (u, v, d, d)
    edges = [e(0, 1), e(1, 2), e(2, 3), e(3, 0), e(0, 2)]
    return coords, edges


class TestBuildGraph:
    def test_undirected(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0]])
        adj_d, adj_t = mod.build_graph(coords, [(0, 1, 1.0, 2.0)])
        assert (1, 1.0) in adj_d[0]
        assert (0, 1.0) in adj_d[1]
        assert (1, 2.0) in adj_t[0]

    def test_negative_weight_raises(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0]])
        with pytest.raises(mod.ValidationError):
            mod.build_graph(coords, [(0, 1, -1.0, 1.0)])

    def test_invalid_node_raises(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0]])
        with pytest.raises(mod.ValidationError):
            mod.build_graph(coords, [(0, 5, 1.0, 1.0)])


class TestDijkstra:
    def test_shortest_uses_diagonal(self):
        """0→2：走对角捷径(1.41) 比 0-1-2(2.0) 短。"""
        coords, edges = square_graph()
        adj_d, _ = mod.build_graph(coords, edges)
        path, cost = mod.dijkstra_path(adj_d, 0, 2)
        assert path == [0, 2]
        np.testing.assert_allclose(cost, np.sqrt(2), atol=1e-9)

    def test_path_valid_chain(self):
        coords, edges = square_graph()
        adj_d, _ = mod.build_graph(coords, edges)
        path, _ = mod.dijkstra_path(adj_d, 0, 3)
        assert path[0] == 0 and path[-1] == 3

    def test_unreachable(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0], [5.0, 5.0]])
        adj_d, _ = mod.build_graph(coords, [(0, 1, 1.0, 1.0)])
        path, cost = mod.dijkstra_path(adj_d, 0, 2)
        assert path == []
        assert cost == float("inf")

    def test_out_of_range_raises(self):
        coords, edges = square_graph()
        adj_d, _ = mod.build_graph(coords, edges)
        with pytest.raises(mod.ValidationError):
            mod.dijkstra_path(adj_d, 0, 99)


class TestAstar:
    def test_matches_dijkstra(self):
        """可采纳启发式下 A* 代价必须等于 Dijkstra。"""
        coords, edges, _ = mod.generate_synthetic([116, 39, 117, 40], grid_n=8)
        adj_d, _ = mod.build_graph(coords, edges)
        scale = mod.admissible_heuristic_scale(coords, edges, "distance")
        for src, dst in [(0, 63), (5, 40), (10, 55)]:
            p_d, c_d = mod.dijkstra_path(adj_d, src, dst)
            p_a, c_a = mod.astar_path(adj_d, coords, src, dst, heuristic_scale=scale)
            np.testing.assert_allclose(c_a, c_d, rtol=1e-9)

    def test_zero_scale_equals_dijkstra(self):
        """heuristic_scale=0 的 A* 退化为 Dijkstra，代价相同。"""
        coords, edges = square_graph()
        adj_d, _ = mod.build_graph(coords, edges)
        _, c_d = mod.dijkstra_path(adj_d, 0, 2)
        _, c_a = mod.astar_path(adj_d, coords, 0, 2, heuristic_scale=0.0)
        np.testing.assert_allclose(c_a, c_d, atol=1e-9)


class TestAdmissibleScale:
    def test_distance_scale_is_one(self):
        """distance 权重下边权=欧氏 → min ratio = 1。"""
        coords, edges, _ = mod.generate_synthetic([116, 39, 117, 40], grid_n=6)
        scale = mod.admissible_heuristic_scale(coords, edges, "distance")
        np.testing.assert_allclose(scale, 1.0, atol=1e-6)

    def test_time_scale_leq_distance(self):
        """主干道更快 → time 权重的可采纳 scale < distance 的 scale。"""
        coords, edges, _ = mod.generate_synthetic([116, 39, 117, 40], grid_n=8)
        s_d = mod.admissible_heuristic_scale(coords, edges, "distance")
        s_t = mod.admissible_heuristic_scale(coords, edges, "time")
        assert s_t < s_d


class TestMultiConstraint:
    def test_time_route_prefers_trunk(self):
        """time 权重路径可能不同于 distance 权重路径（走主干道）。"""
        coords, edges, _ = mod.generate_synthetic([116, 39, 117, 40], grid_n=10)
        adj_d, adj_t = mod.build_graph(coords, edges)
        src, dst = 0, 99
        p_d, _ = mod.dijkstra_path(adj_d, src, dst)
        p_t, _ = mod.dijkstra_path(adj_t, src, dst)
        # 两条路径都有效，且 time 路径代价(time) 不高于 distance 路径的 time 代价
        # 直接验证：time 路径确实是 time 图的最短
        def path_cost_time(path):
            tot = 0.0
            for i in range(1, len(path)):
                for v, wgt in adj_t[path[i - 1]]:
                    if v == path[i]:
                        tot += wgt
                        break
            return tot
        assert path_cost_time(p_t) <= path_cost_time(p_d) + 1e-9


class TestRouteOD:
    def test_batch_multiple_pairs(self):
        coords, edges, _ = mod.generate_synthetic([116, 39, 117, 40], grid_n=6)
        adj_d, adj_t = mod.build_graph(coords, edges)
        pairs = [(0, 35), (1, 30), (5, 34)]
        results = mod.route_od(coords, adj_d, adj_t, pairs, weight="distance",
                               algorithm="dijkstra")
        assert len(results) == 3
        assert all(r["reachable"] for r in results)


class TestSynthetic:
    def test_shapes(self):
        coords, edges, info = mod.generate_synthetic([116, 39, 117, 40], grid_n=6)
        assert coords.shape == (36, 2)
        assert info["n_edges"] > 0

    def test_connected(self):
        coords, edges, info = mod.generate_synthetic([116, 39, 117, 40], grid_n=6)
        adj_d, _ = mod.build_graph(coords, edges)
        p, c = mod.dijkstra_path(adj_d, 0, 35)
        assert len(p) > 0
