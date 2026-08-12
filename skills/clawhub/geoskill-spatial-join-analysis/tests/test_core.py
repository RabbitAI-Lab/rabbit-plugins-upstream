"""Core algorithm tests for spatial-join-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod

from shapely.geometry import Point, box


class TestSpatialJoin:
    def test_intersects_assigns_points_to_boxes(self):
        """两个 box + 三个点，验证 intersects 配对正确。"""
        boxes = [box(0, 0, 1, 1), box(2, 0, 3, 1)]
        points = [Point(0.5, 0.5), Point(2.5, 0.5), Point(0.5, 0.5)]
        pairs = mod.spatial_join(boxes, points, "intersects")
        pair_set = set(pairs)
        assert (0, 0) in pair_set  # box0 含 point0
        assert (0, 2) in pair_set  # box0 含 point2
        assert (1, 1) in pair_set  # box1 含 point1
        assert (1, 0) not in pair_set

    def test_intersects_count(self):
        """一个 box 含全部 5 个点 → 5 对。"""
        boxes = [box(0, 0, 10, 10)]
        points = [Point(i, i) for i in range(5)]
        pairs = mod.spatial_join(boxes, points, "intersects")
        assert len(pairs) == 5

    def test_within_predicate(self):
        """点 within box。"""
        points = [Point(0.5, 0.5), Point(5.0, 5.0)]
        boxes = [box(0, 0, 1, 1)]
        pairs = mod.spatial_join(points, boxes, "within")
        assert (0, 0) in set(pairs)
        assert (1, 0) not in set(pairs)

    def test_unknown_predicate_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.spatial_join([box(0, 0, 1, 1)], [Point(0.5, 0.5)], "bogus")


class TestNearestJoin:
    def test_nearest_correct(self):
        """每个点连到最近 box。"""
        boxes = [box(0, 0, 1, 1), box(10, 10, 11, 11)]
        points = [Point(0.5, 0.5), Point(9.0, 9.0)]
        pairs = mod.nearest_join(points, boxes)
        d = dict(pairs)
        assert d[0] == 0  # 点0 最近 box0
        assert d[1] == 1  # 点1 最近 box1


class TestAggregate:
    def test_sum(self):
        pairs = [(0, 0), (0, 1), (1, 2)]
        values = np.array([10.0, 20.0, 30.0])
        out = mod.aggregate_join(pairs, values, n_left=3, agg="sum")
        assert out[0] == 30.0
        assert out[1] == 30.0
        assert np.isnan(out[2])

    def test_count(self):
        pairs = [(0, 0), (0, 1), (0, 2), (1, 0)]
        values = np.array([1.0, 1.0, 1.0])
        out = mod.aggregate_join(pairs, values, n_left=2, agg="count")
        assert out[0] == 3
        assert out[1] == 1

    def test_mean(self):
        pairs = [(0, 0), (0, 1)]
        values = np.array([10.0, 30.0])
        out = mod.aggregate_join(pairs, values, n_left=1, agg="mean")
        assert out[0] == 20.0

    def test_max_min(self):
        pairs = [(0, 0), (0, 1), (0, 2)]
        values = np.array([5.0, 1.0, 9.0])
        assert mod.aggregate_join(pairs, values, 1, "max")[0] == 9.0
        assert mod.aggregate_join(pairs, values, 1, "min")[0] == 1.0

    def test_unknown_agg_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.aggregate_join([(0, 0)], np.array([1.0]), 1, "median")

    def test_count_empty_zero(self):
        """无连接的 left count 为 0。"""
        out = mod.aggregate_join([], np.array([1.0]), n_left=2, agg="count")
        assert out[0] == 0 and out[1] == 0


class TestSynthetic:
    def test_shapes(self):
        pts, polys, info = mod.generate_synthetic([116, 39, 117, 40], n_points=50, grid_cells=3)
        assert len(pts) == 50
        assert len(polys) == 9
        assert info["n_zones"] == 9

    def test_zones_cover_bbox(self):
        """网格面层应覆盖整个 bbox。"""
        pts, polys, info = mod.generate_synthetic([0, 0, 1, 1], grid_cells=4)
        union = polys.geometry.union_all()
        assert union.area == pytest.approx(1.0, abs=1e-6)
