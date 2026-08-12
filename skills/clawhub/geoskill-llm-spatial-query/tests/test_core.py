"""Core algorithm tests for llm-spatial-query."""
import sys
import os
import json

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _sample_gdf():
    import geopandas as gpd
    from shapely.geometry import box
    feats = [
        {"id": 0, "name": "a", "area_km2": 10.0, "value": 5.0,
         "population": 100, "geometry": box(0, 0, 1, 1)},
        {"id": 1, "name": "b", "area_km2": 60.0, "value": 90.0,
         "population": 4000, "geometry": box(2, 2, 3, 3)},
        {"id": 2, "name": "c", "area_km2": 80.0, "value": 50.0,
         "population": 200, "geometry": box(10, 10, 11, 11)},
    ]
    return gpd.GeoDataFrame(feats, crs="EPSG:4326")


class TestParseQuery:
    def test_attribute_filter_cn(self):
        plan = mod.parse_spatial_query("筛选面积大于50的地块")
        assert {"field": "area_km2", "op": ">", "value": 50.0} in plan["filters"]

    def test_attribute_filter_en_symbol(self):
        plan = mod.parse_spatial_query("value < 20")
        assert {"field": "value", "op": "<", "value": 20.0} in plan["filters"]

    def test_multiple_filters(self):
        plan = mod.parse_spatial_query("面积大于10 且 人口小于3000")
        fields = {(f["field"], f["op"]) for f in plan["filters"]}
        assert ("area_km2", ">") in fields
        assert ("population", "<") in fields

    def test_top_n(self):
        plan = mod.parse_spatial_query("取值最高的前3个")
        assert plan["top_n"] == 3
        assert plan["sort_field"] == "value"

    def test_top_n_english(self):
        plan = mod.parse_spatial_query("top 5 by value")
        assert plan["top_n"] == 5

    def test_spatial_bbox_intent(self):
        plan = mod.parse_spatial_query("在范围内的地块")
        assert plan["spatial"] == "bbox"

    def test_no_filter_all(self):
        plan = mod.parse_spatial_query("全部要素")
        assert plan["filters"] == []
        assert plan["spatial"] == "all"
        assert plan["top_n"] is None

    def test_empty_raises(self):
        with pytest.raises(mod.UsageError):
            mod.parse_spatial_query("  ")


class TestNormalizeOp:
    def test_aliases(self):
        assert mod.normalize_op("大于") == ">"
        assert mod.normalize_op("超过") == ">"
        assert mod.normalize_op("低于") == "<"
        assert mod.normalize_op("大于等于") == ">="
        assert mod.normalize_op("等于") == "=="


class TestApplyAttributeFilter:
    def test_greater_than(self):
        gdf = _sample_gdf()
        out = mod.apply_attribute_filter(gdf, "area_km2", ">", 50.0)
        assert set(out["id"]) == {1, 2}

    def test_less_equal(self):
        gdf = _sample_gdf()
        out = mod.apply_attribute_filter(gdf, "value", "<=", 50.0)
        assert set(out["id"]) == {0, 2}

    def test_equal(self):
        gdf = _sample_gdf()
        out = mod.apply_attribute_filter(gdf, "population", "==", 200.0)
        assert set(out["id"]) == {2}

    def test_missing_field_passthrough(self):
        gdf = _sample_gdf()
        out = mod.apply_attribute_filter(gdf, "nonexistent", ">", 0)
        assert len(out) == 3

    def test_bad_op_raises(self):
        gdf = _sample_gdf()
        with pytest.raises(mod.UsageError):
            mod.apply_attribute_filter(gdf, "value", "~", 0)


class TestQueryByBbox:
    def test_intersects_only(self):
        gdf = _sample_gdf()
        out = mod.query_by_bbox(gdf, [0, 0, 4, 4])
        assert set(out["id"]) == {0, 1}  # id2 在 (10,10)，不相交

    def test_no_crs_raises(self):
        import geopandas as gpd
        from shapely.geometry import box
        gdf = gpd.GeoDataFrame(
            [{"geometry": box(0, 0, 1, 1)}], crs=None)
        with pytest.raises(mod.ValidationError):
            mod.query_by_bbox(gdf, [0, 0, 2, 2])


class TestRunSpatialQuery:
    def test_filter_plus_topn(self):
        gdf = _sample_gdf()
        plan = {"filters": [{"field": "area_km2", "op": ">", "value": 50.0}],
                "spatial": "all", "top_n": 1, "sort_field": "value"}
        out = mod.run_spatial_query(gdf, plan)
        assert len(out) == 1
        assert out.iloc[0]["id"] == 1  # value 90 最高

    def test_bbox_filter_requires_bbox(self):
        gdf = _sample_gdf()
        plan = {"filters": [], "spatial": "bbox", "top_n": None, "sort_field": None}
        with pytest.raises(mod.UsageError):
            mod.run_spatial_query(gdf, plan, bbox=None)

    def test_bbox_filter_applies(self):
        gdf = _sample_gdf()
        plan = {"filters": [], "spatial": "bbox", "top_n": None, "sort_field": None}
        out = mod.run_spatial_query(gdf, plan, bbox=[0, 0, 4, 4])
        assert set(out["id"]) == {0, 1}


class TestBuildSynthetic:
    def test_grid_and_crs(self):
        gdf = mod.build_synthetic_dataset([116, 39, 117, 40], n=9, seed=1)
        assert len(gdf) == 9
        assert gdf.crs is not None
        assert gdf.geometry.is_valid.all()
        for col in ["id", "name", "area_km2", "value", "population", "category"]:
            assert col in gdf.columns

    def test_area_positive(self):
        gdf = mod.build_synthetic_dataset([116, 39, 117, 40], n=4, seed=2)
        assert (gdf["area_km2"] > 0).all()


class TestResultsToGeoJSON:
    def test_structure(self):
        gdf = _sample_gdf()
        gj = mod.results_to_geojson(gdf)
        assert gj["type"] == "FeatureCollection"
        assert len(gj["features"]) == 3
        assert gj["features"][0]["geometry"]["type"] == "Polygon"


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_vector_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_vector("/nonexistent/x.geojson")
