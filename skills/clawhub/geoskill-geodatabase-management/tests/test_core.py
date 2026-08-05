"""Core algorithm tests for geodatabase-management."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


@pytest.fixture
def gpkg(tmp_path):
    path = str(tmp_path / "test.gpkg")
    gdf = M.generate_synthetic([116, 39, 117, 40], n=120)
    layer = M.create_geodatabase(path, gdf, "cities")
    return path, layer, gdf


class TestSanitizeLayer:
    def test_digit_prefix(self):
        assert not M._sanitize_layer("123abc")[0].isdigit()

    def test_special_chars(self):
        assert M._sanitize_layer("my-layer.name") == "my_layer_name"


class TestCreateAndList:
    def test_create_and_count(self, gpkg):
        path, layer, gdf = gpkg
        layers = M.list_layers(path)
        names = {l["layer"] for l in layers}
        assert layer in names
        lyr = next(l for l in layers if l["layer"] == layer)
        assert lyr["feature_count"] == len(gdf)
        assert lyr["data_type"] == "features"

    def test_create_missing_db_list_raises(self):
        with pytest.raises(M.UsageError):
            M.list_layers("/nonexistent/nope.gpkg")


class TestImport:
    def test_append_features(self, tmp_path):
        path = str(tmp_path / "imp.gpkg")
        gdf1 = M.generate_synthetic([116, 39, 117, 40], n=50, seed=1)
        M.create_geodatabase(path, gdf1, "pts")
        gdf2 = M.generate_synthetic([116, 39, 117, 40], n=30, seed=2)
        added = M.import_features(path, gdf2, "pts")
        assert added == 30
        lyr = next(l for l in M.list_layers(path) if l["layer"] == "pts")
        assert lyr["feature_count"] == 80

    def test_import_missing_db_raises(self, tmp_path):
        gdf = M.generate_synthetic([116, 39, 117, 40], n=5)
        with pytest.raises(M.UsageError):
            M.import_features(str(tmp_path / "no.gpkg"), gdf, "x")


class TestSpatialIndex:
    def test_index_exists_after_build(self, gpkg):
        path, layer, gdf = gpkg
        assert M.spatial_index_exists(path, layer) is False
        n = M.build_spatial_index(path, layer, gdf)
        assert n == len(gdf)
        assert M.spatial_index_exists(path, layer) is True

    def test_index_table_name(self):
        assert M.spatial_index_table("cities") == "idx_cities_geom"


class TestQuery:
    def test_index_matches_brute_force(self, gpkg):
        path, layer, gdf = gpkg
        M.build_spatial_index(path, layer, gdf)
        win = [116.2, 39.2, 116.6, 39.6]
        qi = M.query_bbox_indexed(path, layer, win)
        qb = M.query_bbox_brute(path, layer, win)
        assert qi == qb

    def test_query_all_inside_window(self, gpkg):
        import geopandas as gpd
        from shapely.geometry import box
        path, layer, gdf = gpkg
        M.build_spatial_index(path, layer, gdf)
        win = [116.1, 39.1, 116.5, 39.5]
        qi = M.query_bbox_indexed(path, layer, win)
        g2 = gpd.read_file(path, layer=layer)
        wb = box(*win)
        for fid in qi:
            assert wb.intersects(g2.geometry.iloc[fid - 1].envelope)

    def test_full_extent_returns_all(self, gpkg):
        path, layer, gdf = gpkg
        M.build_spatial_index(path, layer, gdf)
        b = gdf.total_bounds
        win = [b[0] - 1, b[1] - 1, b[2] + 1, b[3] + 1]
        qi = M.query_bbox_indexed(path, layer, win)
        assert len(qi) == len(gdf)

    def test_query_without_index_raises(self, gpkg):
        path, layer, gdf = gpkg
        with pytest.raises(M.ValidationError):
            M.query_bbox_indexed(path, layer, [116, 39, 117, 40])

    def test_many_random_windows_match(self, gpkg):
        path, layer, gdf = gpkg
        M.build_spatial_index(path, layer, gdf)
        rng = np.random.default_rng(7)
        for _ in range(8):
            x0 = rng.uniform(116, 116.7)
            y0 = rng.uniform(39, 39.7)
            win = [x0, y0, x0 + rng.uniform(0.05, 0.3), y0 + rng.uniform(0.05, 0.3)]
            assert M.query_bbox_indexed(path, layer, win) == \
                M.query_bbox_brute(path, layer, win)


class TestDatabaseInfo:
    def test_info_structure(self, gpkg):
        path, layer, gdf = gpkg
        M.build_spatial_index(path, layer, gdf)
        info = M.database_info(path)
        assert info["path"] == path
        lyr = next(l for l in info["layers"] if l["layer"] == layer)
        assert lyr["has_spatial_index"] is True
        assert "gpkg_contents" in info["sqlite_tables"]


class TestSynthetic:
    def test_generate(self):
        gdf = M.generate_synthetic([116, 39, 117, 40], n=20)
        assert len(gdf) == 20
        assert gdf.crs.to_epsg() == 4326

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_vector("/nonexistent/nope.shp")
