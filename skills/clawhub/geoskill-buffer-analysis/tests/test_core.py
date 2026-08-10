"""Core algorithm tests for buffer-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod

from shapely.geometry import Point, LineString, box


class TestMakeBuffers:
    def test_point_buffer_area_pi_r2(self):
        """平面坐标下点缓冲面积 ≈ πr²。"""
        r = 5.0
        buffers = mod.make_buffers([Point(0, 0)], r, quad_segs=128)
        area = buffers[0].area
        assert area == pytest.approx(np.pi * r * r, rel=1e-3)

    def test_buffer_grows_with_distance(self):
        b1 = mod.make_buffers([Point(0, 0)], 1.0)[0]
        b2 = mod.make_buffers([Point(0, 0)], 2.0)[0]
        assert b2.area > b1.area

    def test_line_buffer_stadium(self):
        """线段缓冲 = 矩形 + 两端半圆（stadium）。"""
        line = LineString([(0, 0), (10, 0)])
        r = 1.0
        buf = mod.make_buffers([line], r, quad_segs=128)[0]
        expected = 10 * 2 * r + np.pi * r * r  # 矩形 + 整圆
        assert buf.area == pytest.approx(expected, rel=1e-3)

    def test_zero_distance_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.make_buffers([Point(0, 0)], 0.0)


class TestDissolve:
    def test_overlapping_buffers_merged(self):
        """两个重叠缓冲融合后面积 < 各自面积之和。"""
        b = mod.make_buffers([Point(0, 0), Point(1, 0)], 2.0, quad_segs=64)
        individual_sum = b[0].area + b[1].area
        dissolved = mod.dissolve_buffers(b)
        assert dissolved.area < individual_sum
        assert dissolved.area > b[0].area  # 大于单个

    def test_disjoint_buffers_area_sum(self):
        """不相交的缓冲融合后面积 = 各自之和。"""
        b = mod.make_buffers([Point(0, 0), Point(100, 0)], 1.0, quad_segs=64)
        dissolved = mod.dissolve_buffers(b)
        assert dissolved.area == pytest.approx(b[0].area + b[1].area, rel=1e-6)

    def test_empty_raises(self):
        from shapely.geometry import Point as P
        with pytest.raises(mod.ValidationError):
            mod.dissolve_buffers([P().buffer(0)])


class TestOverlayCount:
    def test_counts_targets_inside(self):
        buf = mod.make_buffers([Point(0, 0)], 5.0, quad_segs=64)[0]
        targets = [Point(0, 0), Point(1, 1), Point(100, 100)]
        n, hits = mod.overlay_count(buf, targets)
        assert n == 2
        assert set(hits) == {0, 1}

    def test_no_hits(self):
        buf = mod.make_buffers([Point(0, 0)], 1.0)[0]
        targets = [Point(50, 50), Point(60, 60)]
        n, hits = mod.overlay_count(buf, targets)
        assert n == 0
        assert hits == []


class TestPlanarArea:
    def test_area_positive_and_reasonable(self):
        """1°x1° 方框在赤道附近 ≈ 111km x 111km ≈ 12300 km²。"""
        g = box(0, 0, 1, 1)
        area = mod.planar_area_km2(g, lon0=0.5, lat0=0.5)
        assert 12000 < area < 12600

    def test_area_shrinks_with_latitude(self):
        """同 1°x1° 方框在高纬面积更小（经度收敛）。"""
        a_eq = mod.planar_area_km2(box(0, 0, 1, 1), 0.5, 0.5)
        a_hi = mod.planar_area_km2(box(0, 60, 1, 61), 0.5, 60.5)
        assert a_hi < a_eq


class TestSynthetic:
    def test_shapes(self):
        src, tgt, info = mod.generate_synthetic([116, 39, 117, 40], n_sources=8, n_targets=30)
        assert len(src) == 8
        assert len(tgt) == 30
