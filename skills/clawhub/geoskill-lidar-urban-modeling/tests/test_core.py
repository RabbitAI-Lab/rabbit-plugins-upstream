"""Core algorithm tests for lidar-urban-modeling."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as lu


class TestRasterSurfaces:
    def test_max_surface(self):
        points = np.array([[0.5, 0.5, 2.0],
                           [0.5, 0.5, 7.0],
                           [3.5, 3.5, 1.0]])
        extent = lu.grid_extent(points, 1.0)
        dsm = lu.rasterize_max_surface(points, extent, 1.0)
        assert np.nanmax(dsm) == 7.0

    def test_min_le_percentile_le_max(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=2)
        extent = lu.grid_extent(points, 1.0)
        smin = lu.rasterize_min_surface(points, extent, 1.0)
        spct = lu.rasterize_percentile_surface(points, extent, 1.0, pct=10.0)
        smax = lu.rasterize_max_surface(points, extent, 1.0)
        valid = np.isfinite(smin) & np.isfinite(spct) & np.isfinite(smax)
        assert valid.any()
        assert np.all(smin[valid] <= spct[valid] + 1e-9)
        assert np.all(spct[valid] <= smax[valid] + 1e-9)

    def test_ndsm_nonnegative(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=3)
        extent = lu.grid_extent(points, 1.0)
        ndsm, dsm, dtm = lu.compute_ndsm(points, extent, 1.0, "min")
        assert ndsm.min() >= 0.0
        assert ndsm.shape == dsm.shape == dtm.shape


class TestGroundSurface:
    def test_pmf_removes_square_bump(self):
        grid = np.zeros((32, 32), dtype=np.float64)
        grid[12:20, 12:20] = 12.0  # 8×8 建筑突起
        out = lu.pmf_ground_surface(grid, cell_size=1.0)
        assert out[16, 16] < 1.0       # 突起被削去
        assert abs(out[2, 2]) < 1e-9   # 远处地面不变

    def test_pmf_preserves_plane(self):
        yy, xx = np.mgrid[0:32, 0:32]
        grid = 0.02 * xx.astype(np.float64) + 0.01 * yy
        out = lu.pmf_ground_surface(grid, cell_size=1.0)
        assert np.abs(out - grid).max() < 1e-6

    def test_ground_method_percentile_close_to_min(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=4)
        extent = lu.grid_extent(points, 1.0)
        d1 = lu.estimate_ground_surface(points, extent, 1.0, "min")
        d2 = lu.estimate_ground_surface(points, extent, 1.0, "percentile")
        assert np.abs(d1 - d2).mean() < 1.0

    def test_unknown_ground_method_raises(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=4)
        extent = lu.grid_extent(points, 1.0)
        with pytest.raises(lu.UsageError):
            lu.estimate_ground_surface(points, extent, 1.0, "bogus")


class TestDtm:
    def test_dtm_follows_terrain_outside_buildings(self):
        """建筑外部 DTM 应贴近真值地形（0.015x + 0.01y）。"""
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=5)
        extent = lu.grid_extent(points, 1.0)
        xmin, ymax, w, h = extent
        dtm = lu.estimate_ground_surface(points, extent, 1.0, "min")
        row = h // 2
        y_mid = ymax - (row + 0.5)
        xs = xmin + (np.arange(w) + 0.5)
        truth = lu.synthetic_terrain(xs, np.full(w, y_mid))
        outside = np.ones(w, dtype=bool)
        for b in info["buildings"]:
            outside &= ~((xs >= b["x_min"]) & (xs <= b["x_max"])
                         & (y_mid >= b["y_min"]) & (y_mid <= b["y_max"]))
        assert outside.sum() > w // 2
        err = np.abs(dtm[row][outside] - truth[outside])
        assert err.mean() < 0.3


class TestExtractBuildings:
    def test_count_and_height_synthetic(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=42)
        extent = lu.grid_extent(points, 1.0)
        ndsm, _, _ = lu.compute_ndsm(points, extent, 1.0, "min")
        bld = lu.extract_buildings(ndsm, extent, 1.0,
                                   min_height=3.0, min_area_m2=15.0)
        n_true = info["n_buildings_true"]
        assert abs(len(bld) - n_true) <= 1
        pairs, h_rmse, a_rrmse = lu.match_buildings(bld, info["buildings"])
        assert len(pairs) >= n_true - 1
        assert h_rmse < 0.5, f"h_rmse={h_rmse}"
        assert a_rrmse < 0.3, f"a_rrmse={a_rrmse}"

    def test_second_seed_consistent(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=123)
        extent = lu.grid_extent(points, 1.0)
        ndsm, _, _ = lu.compute_ndsm(points, extent, 1.0, "min")
        bld = lu.extract_buildings(ndsm, extent, 1.0, 3.0, 15.0)
        assert abs(len(bld) - info["n_buildings_true"]) <= 1

    def test_min_height_filters_everything(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=7)
        extent = lu.grid_extent(points, 1.0)
        ndsm, _, _ = lu.compute_ndsm(points, extent, 1.0, "min")
        bld = lu.extract_buildings(ndsm, extent, 1.0, min_height=100.0)
        assert bld == []

    def test_min_area_filters_small_blobs(self):
        ndsm = np.zeros((16, 16), dtype=np.float64)
        ndsm[3, 4] = 8.0          # 1 m² 碎片
        ndsm[10:14, 10:14] = 6.0  # 16 m² 建筑
        extent = (0.0, 16.0, 16, 16)
        bld = lu.extract_buildings(ndsm, extent, 1.0,
                                   min_height=3.0, min_area_m2=10.0)
        assert len(bld) == 1
        assert bld[0]["area_m2"] == 16.0
        assert bld[0]["height_max"] == 6.0
        assert bld[0]["height_mean"] == 6.0
        assert bld[0]["volume_m3"] == pytest.approx(96.0)
        # 行 10..13、列 10..13 的质心 → 局部坐标 (12, 16−12)
        assert bld[0]["centroid_x"] == pytest.approx(12.0)
        assert bld[0]["centroid_y"] == pytest.approx(4.0)

    def test_two_rectangles_sorted_by_height(self):
        ndsm = np.zeros((32, 32), dtype=np.float64)
        ndsm[5:15, 5:15] = 10.0    # 100 m²，h=10
        ndsm[20:26, 20:26] = 6.0   # 36 m²，h=6
        extent = (0.0, 32.0, 32, 32)
        bld = lu.extract_buildings(ndsm, extent, 1.0,
                                   min_height=3.0, min_area_m2=15.0)
        assert len(bld) == 2
        assert bld[0]["height_max"] == 10.0  # 按高度降序
        assert bld[0]["building_id"] == 0
        assert bld[1]["height_max"] == 6.0

    def test_diagonal_cells_connected_8(self):
        """8 连通：对角相接的像元属于同一栋建筑。"""
        ndsm = np.zeros((16, 16), dtype=np.float64)
        ndsm[2:6, 2:6] = 8.0
        ndsm[6:10, 6:10] = 8.0  # 仅在角点 (5,5)/(6,6) 对角相接
        extent = (0.0, 16.0, 16, 16)
        bld = lu.extract_buildings(ndsm, extent, 1.0,
                                   min_height=3.0, min_area_m2=10.0)
        assert len(bld) == 1
        assert bld[0]["n_cells"] == 32


class TestVectorize:
    def test_polygon_valid_and_bounds(self):
        ndsm = np.zeros((32, 32), dtype=np.float64)
        ndsm[5:15, 5:15] = 10.0
        extent = (0.0, 32.0, 32, 32)
        bld = lu.extract_buildings(ndsm, extent, 1.0, 3.0, 15.0)
        geoms = lu.vectorize_buildings(bld, extent, 1.0)
        assert len(geoms) == 1
        g = geoms[0]
        assert g.is_valid
        assert g.area == pytest.approx(100.0)
        minx, miny, maxx, maxy = g.bounds
        assert minx >= 0.0 and maxx <= 32.0
        assert miny >= 0.0 and maxy <= 32.0

    def test_remap_to_geo(self):
        ndsm = np.zeros((32, 32), dtype=np.float64)
        ndsm[5:15, 5:15] = 10.0
        extent = (0.0, 32.0, 32, 32)
        bld = lu.extract_buildings(ndsm, extent, 1.0, 3.0, 15.0)
        geoms = lu.vectorize_buildings(bld, extent, 1.0)
        geo = lu.remap_geom_to_geo(geoms[0], [0.0, 0.0, 32.0, 32.0],
                                   [116.0, 39.0, 117.0, 40.0])
        minx, miny, maxx, maxy = geo.bounds
        assert minx >= 116.0 and maxx <= 117.0
        assert miny >= 39.0 and maxy <= 40.0
        assert geo.area > 0
        assert geo.is_valid


class TestMatchBuildings:
    def test_identity_match(self):
        det = [{"centroid_x": 10.0, "centroid_y": 10.0, "height_max": 9.0,
                "area_m2": 100.0, "volume_m3": 800.0},
               {"centroid_x": 50.0, "centroid_y": 50.0, "height_max": 15.0,
                "area_m2": 200.0, "volume_m3": 3000.0}]
        truth = [{"cx": 10.0, "cy": 10.0, "height": 9.0, "area_m2": 100.0},
                 {"cx": 50.0, "cy": 50.0, "height": 15.0, "area_m2": 200.0}]
        pairs, h_rmse, a_rrmse = lu.match_buildings(det, truth)
        assert len(pairs) == 2
        assert h_rmse == 0.0
        assert a_rrmse == 0.0

    def test_no_match_when_far(self):
        det = [{"centroid_x": 1.0, "centroid_y": 1.0, "height_max": 9.0,
                "area_m2": 100.0, "volume_m3": 800.0}]
        truth = [{"cx": 90.0, "cy": 90.0, "height": 9.0, "area_m2": 100.0}]
        pairs, h_rmse, a_rrmse = lu.match_buildings(det, truth)
        assert pairs == []
        assert np.isnan(h_rmse)
        assert np.isnan(a_rrmse)


class TestSynthetic:
    def test_info_and_points(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=8)
        assert points.ndim == 2 and points.shape[1] == 3
        assert info["n_buildings_true"] == 8
        assert len(info["buildings"]) == 8
        for b in info["buildings"]:
            assert b["area_m2"] == pytest.approx(b["width"] * b["depth"])
            assert 6.0 <= b["height"] <= 25.0

    def test_buildings_do_not_overlap(self):
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=9)
        bs = info["buildings"]
        for i in range(len(bs)):
            for j in range(i + 1, len(bs)):
                a, c = bs[i], bs[j]
                sep = (a["x_max"] < c["x_min"] or c["x_max"] < a["x_min"]
                       or a["y_max"] < c["y_min"] or c["y_max"] < a["y_min"])
                assert sep, f"buildings {i} and {j} overlap"

    def test_no_ground_inside_footprint(self):
        """建筑足迹中心附近不应有地面点（激光雷达遮挡）。"""
        points, info = lu.generate_synthetic([116, 39, 117, 40], seed=10)
        b = info["buildings"][0]
        cx, cy = b["cx"], b["cy"]
        near = (np.abs(points[:, 0] - cx) < 0.4) & (np.abs(points[:, 1] - cy) < 0.4)
        z = points[near, 2]
        terrain = lu.synthetic_terrain(np.array([cx]), np.array([cy]))[0]
        assert z.size > 0
        assert z.min() > terrain + 2.0  # 只有墙面/屋顶点


class TestReadPoints:
    def test_read_npy_roundtrip(self, tmp_path):
        arr = np.random.default_rng(0).uniform(0, 10, (50, 3))
        p = str(tmp_path / "pts.npy")
        np.save(p, arr)
        out = lu.read_points(p)
        np.testing.assert_allclose(out, arr)

    def test_read_csv(self, tmp_path):
        p = str(tmp_path / "pts.csv")
        with open(p, "w", encoding="utf-8") as f:
            f.write("1.0,2.0,3.0\n4.0,5.0,6.0\n")
        out = lu.read_points(p)
        assert out.shape == (2, 3)
        np.testing.assert_allclose(out[1], [4.0, 5.0, 6.0])

    def test_read_missing_raises(self):
        with pytest.raises(lu.UsageError):
            lu.read_points("/nonexistent/pts.npy")

    def test_read_two_columns_raises(self, tmp_path):
        p = str(tmp_path / "bad.csv")
        with open(p, "w", encoding="utf-8") as f:
            f.write("1.0,2.0\n3.0,4.0\n")
        with pytest.raises(lu.ValidationError):
            lu.read_points(p)


class TestGeoTiffIO:
    def test_write_roundtrip(self, tmp_path):
        import rasterio
        arr = np.random.default_rng(1).uniform(0, 5, (32, 32)).astype(np.float32)
        p = str(tmp_path / "ndsm.tif")
        lu.write_geotiff(p, arr, [116.0, 39.0, 117.0, 40.0], nodata=-1.0)
        with rasterio.open(p) as src:
            data = src.read(1)
            assert src.crs.to_epsg() == 4326
        np.testing.assert_allclose(data, arr, atol=1e-5)


class TestWriteGeoJSON:
    def test_write_and_read_back(self, tmp_path):
        import geopandas as gpd
        ndsm = np.zeros((32, 32), dtype=np.float64)
        ndsm[5:15, 5:15] = 10.0
        ndsm[20:26, 20:26] = 6.0
        extent = (0.0, 32.0, 32, 32)
        bld = lu.extract_buildings(ndsm, extent, 1.0, 3.0, 15.0)
        geoms = lu.vectorize_buildings(bld, extent, 1.0)
        p = str(tmp_path / "b.geojson")
        lu.write_buildings_geojson(p, bld, geoms)
        gdf = gpd.read_file(p)
        assert len(gdf) == 2
        assert {"building_id", "height_max_m", "height_mean_m",
                "area_m2", "volume_m3"}.issubset(set(gdf.columns))
        assert gdf.crs.to_epsg() == 4326
        assert bool((gdf.geometry.is_valid).all())

    def test_write_empty(self, tmp_path):
        import json as _json
        p = str(tmp_path / "empty.geojson")
        lu.write_buildings_geojson(p, [], [])
        with open(p, encoding="utf-8") as f:
            doc = _json.load(f)
        assert doc["type"] == "FeatureCollection"
        assert doc["features"] == []
