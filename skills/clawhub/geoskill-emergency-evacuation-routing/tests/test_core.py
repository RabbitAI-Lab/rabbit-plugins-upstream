"""Core algorithm tests for emergency-evacuation-routing."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ev


def _adjacent(path):
    """路径相邻像元八连通且首尾正确性辅助检查。"""
    for (r0, c0), (r1, c1) in zip(path[:-1], path[1:]):
        if max(abs(r1 - r0), abs(c1 - c0)) != 1:
            return False
    return True


class TestShortestPath:
    def test_open_grid_optimal_is_euclidean(self):
        """无障碍均匀网格：对角最短路径代价 = 欧氏距离（10·√2）。"""
        cost = np.ones((11, 11))
        path, c = ev.shortest_path(cost, (0, 0), (10, 10))
        assert path is not None
        assert abs(c - 10 * np.sqrt(2)) < 1e-6
        assert path[0] == (0, 0) and path[-1] == (10, 10)
        assert len(path) == 11
        assert _adjacent(path)

    def test_avoids_blocked_cells(self):
        cost = np.ones((11, 11))
        blocked = np.zeros((11, 11), dtype=bool)
        blocked[:, 5] = True
        blocked[0, 5] = False  # 顶部留缺口
        path, c = ev.shortest_path(cost, (5, 0), (5, 10), blocked)
        assert path is not None
        # 绝不穿过阻断像元
        assert all(not blocked[r, c_] for (r, c_) in path)
        assert _adjacent(path)

    def test_detour_longer_than_open(self):
        cost = np.ones((11, 11))
        open_path, open_c = ev.shortest_path(cost, (5, 0), (5, 10))
        blocked = np.zeros((11, 11), dtype=bool)
        blocked[:, 5] = True; blocked[0, 5] = False
        _, detour_c = ev.shortest_path(cost, (5, 0), (5, 10), blocked)
        assert open_c == pytest.approx(10.0)
        assert detour_c > open_c

    def test_unreachable(self):
        cost = np.ones((11, 11))
        blocked = np.zeros((11, 11), dtype=bool)
        blocked[:, 5] = True  # 全长墙，无缺口
        path, c = ev.shortest_path(cost, (5, 0), (5, 10), blocked)
        assert path is None
        assert c == float("inf")

    def test_start_equals_end(self):
        cost = np.ones((5, 5))
        path, c = ev.shortest_path(cost, (2, 2), (2, 2))
        assert path == [(2, 2)]
        assert c == 0.0


class TestDijkstra:
    def test_start_out_of_bounds_raises(self):
        with pytest.raises(ev.ValidationError):
            ev.dijkstra(np.ones((5, 5)), (9, 9))

    def test_distance_increases_from_source(self):
        cost = np.ones((9, 9))
        dist, _ = ev.dijkstra(cost, (4, 4))
        assert dist[4, 4] == 0.0
        assert dist[4, 5] == pytest.approx(1.0)
        assert dist[5, 5] == pytest.approx(np.sqrt(2))


class TestAssignEvacuation:
    def test_all_origins_reach_shelter(self):
        cost = np.ones((20, 20))
        origins = [(2, 2), (17, 2), (2, 17)]
        shelters = [(10, 10)]
        res = ev.assign_evacuation(cost, origins, shelters)
        assert len(res) == 3
        for oi, r in res.items():
            assert r["path"][0] == tuple(origins[oi])
            assert r["path"][-1] == tuple(shelters[r["shelter"]])
            assert _adjacent(r["path"])

    def test_capacity_limits_assignment(self):
        """避难所容量 1，两个起点只能分配一个。"""
        cost = np.ones((20, 20))
        origins = [(0, 0), (19, 19)]
        shelters = [(10, 10)]
        res = ev.assign_evacuation(cost, origins, shelters, capacities=[1])
        assert len(res) == 1

    def test_capacity_two_assigns_both(self):
        cost = np.ones((20, 20))
        origins = [(0, 0), (19, 19)]
        shelters = [(10, 10)]
        res = ev.assign_evacuation(cost, origins, shelters, capacities=[2])
        assert len(res) == 2

    def test_no_shelters_raises(self):
        with pytest.raises(ev.ValidationError):
            ev.assign_evacuation(np.ones((5, 5)), [(0, 0)], [])

    def test_routes_avoid_blockage(self):
        cost = np.ones((20, 20))
        blocked = np.zeros((20, 20), dtype=bool)
        blocked[5:15, 10] = True  # 中段屏障
        origins = [(10, 2)]
        shelters = [(10, 17)]
        res = ev.assign_evacuation(cost, origins, shelters, blocked=blocked)
        assert len(res) == 1
        assert all(not blocked[r, c] for (r, c) in res[0]["path"])


class TestSynthetic:
    def test_shapes(self):
        layers, info = ev.generate_synthetic([116, 39, 117, 40])
        assert layers["cost"].shape == (48, 48)
        assert layers["hazard"].shape == (48, 48)
        assert info["n_origins"] == len(layers["origins"])


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        p = str(tmp_path / "r.tif")
        ev.write_geotiff(p, cube, bbox)
        back, bb = ev.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ev.UsageError):
            ev.read_geotiff("/nonexistent/r.tif")
