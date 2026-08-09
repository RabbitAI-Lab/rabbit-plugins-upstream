"""Core algorithm tests for vector-simplification."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestDouglasPeucker:
    def test_straight_line_collapses(self):
        line = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
        out = M.douglas_peucker(line, 0.1)
        assert out == [(0, 0), (4, 0)]

    def test_keeps_far_spike(self):
        line = [(0, 0), (1, 5), (2, 0)]
        out = M.douglas_peucker(line, 0.5)
        assert (1, 5) in out

    def test_removes_small_spike(self):
        line = [(0, 0), (1, 0.001), (2, 0)]
        out = M.douglas_peucker(line, 0.1)
        assert (1, 0.001) not in out

    def test_epsilon_zero_identity(self):
        line = [(0, 0), (1, 1), (2, 0), (3, 1)]
        out = M.douglas_peucker(line, 0.0)
        assert out == line

    def test_endpoints_always_kept(self):
        line = [(0, 0), (1, 2), (2, -1), (3, 3), (4, 0)]
        out = M.douglas_peucker(line, 0.5)
        assert out[0] == line[0]
        assert out[-1] == line[-1]

    def test_output_subset_of_input(self):
        line = [(i, np.sin(i)) for i in range(30)]
        out = M.douglas_peucker(line, 0.1)
        assert set(out).issubset(set(line))
        assert len(out) <= len(line)


class TestVisvalingam:
    def test_count_target(self):
        pts = [(i, np.sin(i)) for i in range(20)]
        out = M.visvalingam_count(pts, 5)
        assert len(out) == 5
        assert out[0] == pts[0]
        assert out[-1] == pts[-1]

    def test_count_min_two(self):
        pts = [(i, i) for i in range(10)]
        assert len(M.visvalingam_count(pts, 1)) == 2

    def test_threshold_removes_small_area(self):
        # 中间点几乎共线 → 面积近 0，应被删除
        pts = [(0, 0), (1, 0.0001), (2, 0), (3, 0)]
        out = M.visvalingam_threshold(pts, 0.01)
        assert (1, 0.0001) not in out

    def test_threshold_keeps_large_area(self):
        pts = [(0, 0), (1, 10), (2, 0)]
        out = M.visvalingam_threshold(pts, 1.0)
        assert (1, 10) in out


class TestTriangleArea:
    def test_unit_right_triangle(self):
        assert M.triangle_area((0, 0), (1, 0), (0, 1)) == pytest.approx(0.5)

    def test_collinear_zero(self):
        assert M.triangle_area((0, 0), (1, 1), (2, 2)) == 0.0


class TestGeometry:
    def _circle(self, n=64):
        from shapely.geometry import Polygon
        ang = np.linspace(0, 2 * np.pi, n, endpoint=False)
        ring = [(np.cos(a), np.sin(a)) for a in ang]
        ring.append(ring[0])
        return Polygon(ring)

    def test_circle_reduces_vertices_high_area(self):
        poly = self._circle(64)
        simp = M.simplify_geometry(poly, "douglas-peucker", 0.05)
        assert M.vertex_count(simp) < M.vertex_count(poly)
        assert simp.area / poly.area > 0.9

    def test_polygon_stays_valid(self):
        poly = self._circle(64)
        simp = M.simplify_geometry(poly, "douglas-peucker", 0.02)
        assert simp.is_valid
        assert simp.geom_type == "Polygon"

    def test_linestring_simplified(self):
        from shapely.geometry import LineString
        line = LineString([(i, np.sin(i)) for i in range(40)])
        simp = M.simplify_geometry(line, "douglas-peucker", 0.1)
        assert M.vertex_count(simp) < M.vertex_count(line)

    def test_visvalingam_geometry(self):
        poly = self._circle(64)
        simp = M.simplify_geometry(poly, "visvalingam", 0.0, target=20)
        assert M.vertex_count(simp) <= 21  # 20 + 闭合点

    def test_unknown_method_raises(self):
        from shapely.geometry import LineString
        line = LineString([(0, 0), (1, 1), (2, 0)])
        with pytest.raises(M.UsageError):
            M.simplify_geometry(line, "chaikin", 0.1)


class TestVertexCount:
    def test_polygon_count(self):
        from shapely.geometry import Polygon
        poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
        assert M.vertex_count(poly) == 5

    def test_none_zero(self):
        assert M.vertex_count(None) == 0


class TestGeoDataFrame:
    def test_reduction_stats(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        out_gdf, stats = M.simplify_geodataframe(gdf, "douglas-peucker", 0.001)
        assert stats["input_vertices"] > stats["output_vertices"]
        assert stats["vertex_reduction_pct"] > 0
        assert 0 < stats["area_retention"] <= 1.0001
        assert len(out_gdf) == len(gdf)


class TestSynthetic:
    def test_generate(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        assert len(gdf) == 4  # 3 circles + 1 zigzag
        assert gdf.crs.to_epsg() == 4326


class TestIO:
    def test_roundtrip(self, tmp_path):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        path = str(tmp_path / "out.geojson")
        M.write_geojson(path, gdf)
        back = M.read_vector(path)
        assert len(back) == len(gdf)

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_vector("/nonexistent/nope.shp")
