"""Core algorithm tests for spatial-index-builder."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


def _mixed_geoms(n_points=120, n_polys=60, seed=0):
    from shapely.geometry import Point, Polygon
    rng = np.random.default_rng(seed)
    geoms = []
    for _ in range(n_points):
        geoms.append(Point(rng.uniform(116, 117), rng.uniform(39, 40)))
    for _ in range(n_polys):
        x = rng.uniform(116, 117)
        y = rng.uniform(39, 40)
        d = rng.uniform(0.001, 0.03)
        geoms.append(Polygon([(x, y), (x + d, y), (x + d, y + d), (x, y + d), (x, y)]))
    return geoms


class TestGeoHash:
    def test_encode_length(self):
        for p in (1, 5, 8):
            assert len(M.geohash_encode(116.4, 39.9, p)) == p

    def test_encode_deterministic(self):
        assert M.geohash_encode(116.4, 39.9, 6) == M.geohash_encode(116.4, 39.9, 6)

    def test_nearby_share_prefix(self):
        a = M.geohash_encode(116.4000, 39.9000, 6)
        b = M.geohash_encode(116.4001, 39.9000, 6)
        assert a[:4] == b[:4]  # 极近点共享较长前缀

    def test_far_apart_differ(self):
        a = M.geohash_encode(116.4, 39.9, 6)
        b = M.geohash_encode(-73.9, 40.7, 6)
        assert a != b

    def test_cell_size_decreases(self):
        lw5, lh5 = M.geohash_cell_size(5)
        lw7, lh7 = M.geohash_cell_size(7)
        assert lw7 < lw5 and lh7 < lh5

    def test_cells_in_bbox_covers_corners(self):
        bbox = [116.40, 39.90, 116.45, 39.95]
        cells = set(M.geohash_cells_in_bbox(bbox, 6))
        for lon, lat in [(116.40, 39.90), (116.45, 39.95), (116.425, 39.925)]:
            assert M.geohash_encode(lon, lat, 6) in cells


class TestQuadTree:
    def test_insert_and_query(self):
        from shapely.geometry import Point
        geoms = [Point(0.5, 0.5), Point(5.0, 5.0), Point(0.6, 0.6)]
        qt = M.build_quadtree(geoms, bounds=(0, 0, 10, 10))
        hits = M.refine(geoms, qt.query((0, 0, 1, 1)), (0, 0, 1, 1))
        assert set(hits) == {0, 2}

    def test_empty_query(self):
        from shapely.geometry import Point
        geoms = [Point(0.5, 0.5)]
        qt = M.build_quadtree(geoms, bounds=(0, 0, 10, 10))
        assert M.refine(geoms, qt.query((8, 8, 9, 9)), (8, 8, 9, 9)) == []


class TestRTree:
    def test_query_matches_geometry(self):
        from shapely.geometry import Point
        geoms = [Point(0.5, 0.5), Point(5.0, 5.0)]
        tree = M.build_rtree(geoms)
        assert M.query_rtree(tree, geoms, (0, 0, 1, 1)) == [0]
        assert M.query_rtree(tree, geoms, (4, 4, 6, 6)) == [1]


class TestConsistency:
    def test_all_indexes_match_brute_force(self):
        geoms = _mixed_geoms(120, 60, seed=0)
        rt = M.build_rtree(geoms)
        qt = M.build_quadtree(geoms)
        gh = M.build_geohash(geoms, 6)
        rng = np.random.default_rng(1)
        for _ in range(50):
            x0 = rng.uniform(116, 116.8)
            y0 = rng.uniform(39, 39.8)
            w = [x0, y0, x0 + rng.uniform(0.02, 0.3), y0 + rng.uniform(0.02, 0.3)]
            brute = M.query_brute(geoms, w)
            assert M.query_rtree(rt, geoms, w) == brute
            assert M.refine(geoms, qt.query(tuple(w)), w) == brute
            assert M.query_geohash(gh, geoms, w, 6) == brute

    def test_polygon_centroid_outside_window_no_false_negative(self):
        # 细长多边形：代表点在窗口外，但几何与窗口相交
        from shapely.geometry import Polygon
        poly = Polygon([(0, 0), (10, 0), (10, 0.1), (0, 0.1), (0, 0)])
        geoms = [poly]
        gh = M.build_geohash(geoms, 4)
        # 窗口只覆盖多边形左端一小段
        w = [0.0, 0.0, 0.5, 0.05]
        assert M.query_geohash(gh, geoms, w, 4) == M.query_brute(geoms, w) == [0]


class TestBenchmark:
    def test_benchmark_consistent(self):
        geoms = _mixed_geoms(80, 30, seed=2)
        windows = M.random_windows([116, 39, 117, 40], k=10, seed=3)
        res = M.benchmark(geoms, windows, precision=6)
        assert res["all_consistent"] is True
        assert res["n_features"] == 110
        assert res["n_queries"] == 10
        names = {ix["index"] for ix in res["indexes"]}
        assert names == {"rtree", "quadtree", "geohash", "brute_force"}
        for ix in res["indexes"]:
            assert ix["consistent_with_brute"] is True
            assert ix["avg_hits"] >= 0


class TestSynthetic:
    def test_generate_points(self):
        gdf = M.generate_synthetic([116, 39, 117, 40], n=50)
        assert len(gdf) == 50
        assert gdf.crs.to_epsg() == 4326

    def test_random_windows_inside(self):
        wins = M.random_windows([116, 39, 117, 40], k=8, seed=1)
        assert len(wins) == 8
        for w in wins:
            assert w[0] <= w[2] and w[1] <= w[3]
            assert 116 <= w[0] and w[2] <= 117

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_vector("/nonexistent/nope.shp")
