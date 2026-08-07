"""Core algorithm tests for ecological-corridor-design (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestResistance:
    def test_high_suitability_low_resistance(self):
        res_hi = M.resistance_from_suitability(np.full((4, 4), 0.9))
        res_lo = M.resistance_from_suitability(np.full((4, 4), 0.1))
        assert float(res_hi.mean()) < float(res_lo.mean())

    def test_bounded(self):
        rng = np.random.default_rng(0)
        suit = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        res = M.resistance_from_suitability(suit)
        assert res.min() >= 1.0
        assert res.max() <= 101.0


class TestLeastCostPath:
    def test_path_connects_src_dst(self):
        resistance = np.ones((10, 10), dtype=np.float32)
        src, dst = (0, 0), (9, 9)
        path, cost = M.least_cost_path(resistance, src, dst)
        assert path[0] == src
        assert path[-1] == dst
        assert cost > 0

    def test_avoids_high_cost_barrier(self):
        """路径应绕过高阻力带。"""
        resistance = np.ones((20, 20), dtype=np.float32)
        # 中间一列高阻力（留一个缺口）
        resistance[:, 10] = 100.0
        resistance[15, 10] = 1.0  # 缺口
        src, dst = (10, 0), (10, 19)
        path, _ = M.least_cost_path(resistance, src, dst)
        # 路径应经过缺口 (15, 10) 附近，而不是直接穿过高阻力列
        rows_at_col10 = [p[0] for p in path if p[1] == 10]
        assert len(rows_at_col10) > 0
        assert any(abs(r - 15) <= 3 for r in rows_at_col10)

    def test_uniform_cost_straight_path(self):
        """均匀阻力下，路径成本 = 曼哈顿距离 × 单位成本。"""
        resistance = np.ones((10, 10), dtype=np.float32) * 2.0
        src, dst = (0, 0), (9, 9)
        path, cost = M.least_cost_path(resistance, src, dst)
        # 曼哈顿距离 = 18 步，每步成本 ~2
        expected_cost = 18 * 2.0
        np.testing.assert_allclose(cost, expected_cost, rtol=0.1)


class TestCorridorRaster:
    def test_corridor_covers_path(self):
        resistance = np.ones((10, 10), dtype=np.float32)
        path = [(0, 0), (1, 1), (2, 2), (3, 3)]
        corridor = M.corridor_raster(resistance, path, buffer=1)
        for r, c in path:
            assert corridor[r, c] == 1

    def test_buffer_expands_corridor(self):
        resistance = np.ones((10, 10), dtype=np.float32)
        path = [(5, 5)]
        c0 = M.corridor_raster(resistance, path, buffer=0)
        c2 = M.corridor_raster(resistance, path, buffer=2)
        assert c2.sum() > c0.sum()


class TestConnectivity:
    def test_connected_higher_than_fragmented(self):
        """单一大斑块 PC > 多个小斑块 PC。"""
        suit_connected = np.zeros((20, 20), dtype=np.float32)
        suit_connected[5:15, 5:15] = 0.8  # 一个 10x10 斑块

        suit_fragmented = np.zeros((20, 20), dtype=np.float32)
        suit_fragmented[2:4, 2:4] = 0.8
        suit_fragmented[8:10, 8:10] = 0.8
        suit_fragmented[14:16, 14:16] = 0.8

        pc_conn = M.probability_of_connectivity(suit_connected, threshold=0.5)
        pc_frag = M.probability_of_connectivity(suit_fragmented, threshold=0.5)
        assert pc_conn > pc_frag

    def test_no_suitable_zero_pc(self):
        suit = np.zeros((10, 10), dtype=np.float32)
        pc = M.probability_of_connectivity(suit, threshold=0.5)
        assert pc == 0.0

    def test_bounded_0_1(self):
        rng = np.random.default_rng(1)
        suit = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        pc = M.probability_of_connectivity(suit, threshold=0.5)
        assert 0.0 <= pc <= 1.0
