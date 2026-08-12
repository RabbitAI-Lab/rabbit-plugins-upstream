"""Core algorithm tests for least-cost-path."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestDijkstraUniform:
    def test_uniform_straight_cost(self):
        """单位成本面上，水平直线距离 N 的累积成本 = N。"""
        cost = np.ones((11, 21), dtype=np.float64)
        src = (5, 0)
        dist, back = mod.dijkstra_cost_distance(cost, src)
        # 沿同行到 (5,20)：20 步 * 单位成本，edge=0.5*(1+1)*1=1 → 总成本 20
        np.testing.assert_allclose(dist[5, 20], 20.0, atol=1e-9)

    def test_uniform_diagonal_cost(self):
        """对角线邻接成本 = √2。"""
        cost = np.ones((11, 11), dtype=np.float64)
        src = (0, 0)
        dist, _ = mod.dijkstra_cost_distance(cost, src)
        # 到 (10,10) 走对角线 10 步，每步 √2
        np.testing.assert_allclose(dist[10, 10], 10 * np.sqrt(2), atol=1e-6)

    def test_source_zero(self):
        cost = np.ones((5, 5))
        dist, back = mod.dijkstra_cost_distance(cost, (2, 2))
        assert dist[2, 2] == 0.0
        assert back[2, 2] == -1

    def test_distance_monotonic_along_path(self):
        cost = np.ones((9, 9))
        dist, back = mod.dijkstra_cost_distance(cost, (4, 4))
        path = mod.extract_path(back, (8, 8), (4, 4))
        dists = [dist[r, c] for r, c in path]
        assert all(dists[i] <= dists[i + 1] for i in range(len(dists) - 1))


class TestBarrier:
    def test_path_avoids_high_cost(self):
        """高成本墙应被绕开（缺口处通过）。"""
        cost = np.ones((20, 20), dtype=np.float64)
        mid = 10
        cost[:, mid] = 1000.0
        cost[3, mid] = 1.0  # 唯一缺口
        src = (10, 2)
        dst = (10, 18)
        dist, back = mod.dijkstra_cost_distance(cost, src)
        path = mod.extract_path(back, dst, src)
        # 路径应经过缺口行附近（row≈3），而非直穿 col=10 的高成本
        rows_at_wall = [r for r, c in path if c == mid]
        assert all(abs(r - 3) <= 1 for r in rows_at_wall)

    def test_barrier_increases_cost(self):
        """有障碍的成本距离 > 无障碍。"""
        cost_free = np.ones((15, 15))
        cost_wall = np.ones((15, 15))
        cost_wall[:, 7] = 100.0
        cost_wall[2, 7] = 1.0
        d_free, _ = mod.dijkstra_cost_distance(cost_free, (7, 1))
        d_wall, _ = mod.dijkstra_cost_distance(cost_wall, (7, 1))
        assert d_wall[7, 13] > d_free[7, 13]


class TestPathExtraction:
    def test_path_starts_ends(self):
        cost = np.ones((10, 10))
        src, dst = (1, 1), (8, 8)
        _, back = mod.dijkstra_cost_distance(cost, src)
        path = mod.extract_path(back, dst, src)
        assert path[0] == src
        assert path[-1] == dst

    def test_path_cost_matches_distance(self):
        """path_cost 应等于 dist[dest]。"""
        rng = np.random.default_rng(0)
        cost = rng.uniform(1, 5, (12, 12))
        src, dst = (0, 0), (11, 11)
        dist, back = mod.dijkstra_cost_distance(cost, src)
        path = mod.extract_path(back, dst, src)
        np.testing.assert_allclose(mod.path_cost(cost, path), dist[dst], rtol=1e-6)

    def test_path_adjacency(self):
        """路径中相邻像元必须是 8 邻域。"""
        cost = np.ones((10, 10))
        _, back = mod.dijkstra_cost_distance(cost, (0, 0))
        path = mod.extract_path(back, (9, 7), (0, 0))
        for i in range(1, len(path)):
            dr = abs(path[i][0] - path[i - 1][0])
            dc = abs(path[i][1] - path[i - 1][1])
            assert dr <= 1 and dc <= 1 and (dr + dc) > 0

    def test_unreachable_raises(self):
        cost = np.ones((5, 5))
        back = np.full((5, 5), -2, dtype=np.int32)
        back[0, 0] = -1
        with pytest.raises(mod.ValidationError):
            mod.extract_path(back, (4, 4), (0, 0))


class TestValidation:
    def test_negative_cost_raises(self):
        cost = np.ones((5, 5))
        cost[2, 2] = -1
        with pytest.raises(mod.ValidationError):
            mod.dijkstra_cost_distance(cost, (0, 0))

    def test_source_out_of_bounds_raises(self):
        cost = np.ones((5, 5))
        with pytest.raises(mod.ValidationError):
            mod.dijkstra_cost_distance(cost, (99, 99))


class TestSynthetic:
    def test_shapes(self):
        cost, info = mod.generate_synthetic([116, 39, 117, 40], grid_size=32)
        assert cost.shape == (32, 32)
        assert cost.max() > 10  # 障碍带
