"""Core algorithm tests for interactive-webgis."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _gdf():
    import geopandas as gpd
    from shapely.geometry import Point
    rows = [
        {"name": "A", "category": "school", "value": 10, "geometry": Point(0.1, 0.1)},
        {"name": "B", "category": "hospital", "value": 55, "geometry": Point(0.5, 0.5)},
        {"name": "C", "category": "school", "value": 90, "geometry": Point(0.9, 0.9)},
    ]
    return gpd.GeoDataFrame(rows, crs="EPSG:4326")


class TestQueryEngine:
    def test_gt(self):
        out = mod.query_features(_gdf(), "value", "gt", "50")
        assert sorted(out["name"].tolist()) == ["B", "C"]

    def test_le(self):
        out = mod.query_features(_gdf(), "value", "le", "55")
        assert sorted(out["name"].tolist()) == ["A", "B"]

    def test_eq_numeric(self):
        out = mod.query_features(_gdf(), "value", "eq", "90")
        assert out["name"].tolist() == ["C"]

    def test_eq_string(self):
        out = mod.query_features(_gdf(), "category", "eq", "school")
        assert sorted(out["name"].tolist()) == ["A", "C"]

    def test_contains(self):
        out = mod.query_features(_gdf(), "category", "contains", "hos")
        assert out["name"].tolist() == ["B"]

    def test_unknown_field_raises(self):
        with pytest.raises(mod.UsageError):
            mod.query_features(_gdf(), "nope", "gt", "1")

    def test_unknown_op_raises(self):
        with pytest.raises(mod.UsageError):
            mod.query_features(_gdf(), "value", "like", "1")

    def test_numeric_op_nonnumeric_value_raises(self):
        with pytest.raises(mod.UsageError):
            mod.query_features(_gdf(), "value", "gt", "abc")


class TestDensityRaster:
    def test_total_equals_npoints(self):
        pts = np.array([[0.1, 0.1], [0.5, 0.5], [0.9, 0.9], [0.9, 0.9]])
        grid = mod.point_density_raster(pts, [0, 0, 1, 1], 16, 16)
        assert grid.sum() == 4  # 每点计一次

    def test_outside_points_ignored(self):
        pts = np.array([[0.5, 0.5], [5.0, 5.0]])
        grid = mod.point_density_raster(pts, [0, 0, 1, 1], 10, 10)
        assert grid.sum() == 1

    def test_empty_points(self):
        grid = mod.point_density_raster(np.zeros((0, 2)), [0, 0, 1, 1], 8, 8)
        assert grid.sum() == 0


class TestConfigAndHtml:
    def test_config_requires_name_type(self):
        with pytest.raises(mod.ValidationError):
            mod.build_webgis_config("T", [{"name": "x"}], [0, 0, 1, 1])

    def test_config_defaults(self):
        cfg = mod.build_webgis_config("T", [{"name": "l", "type": "circle"}], [0, 0, 1, 1])
        assert cfg["layers"][0]["visible"] is True
        assert cfg["bbox"] == [0, 0, 1, 1]

    def test_html_contains_query_ui(self):
        cfg = mod.build_webgis_config("MyGIS", [{"name": "l", "type": "circle",
                                                 "color": "#ff0000"}], [0, 0, 1, 1])
        gj = {"type": "FeatureCollection", "features": []}
        html = mod.build_webgis_html(cfg, gj, ["value", "category"])
        assert "applyQuery" in html
        assert "circleMarker" in html
        assert "#ff0000" in html
        assert "value" in html and "category" in html


class TestSynthetic:
    def test_synthetic_features(self):
        gdf = mod.generate_synthetic([116, 39, 117, 40], n=50)
        assert len(gdf) == 50
        assert set(["name", "category", "value"]).issubset(gdf.columns)
        assert gdf.crs is not None


class TestGeoTiff:
    def test_write(self, tmp_path):
        arr = np.ones((8, 8), dtype=np.float32)
        path = str(tmp_path / "d.tif")
        mod.write_geotiff(path, arr, [0, 0, 1, 1])
        assert os.path.exists(path)
