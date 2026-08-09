"""Core algorithm tests for spatial-etl-pipeline."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestOps:
    def test_filter_bbox_only_inside(self):
        from shapely.geometry import box
        gdf = M.extract_synthetic([116, 39, 117, 40], n=100)
        win = [116.2, 39.2, 116.8, 39.8]
        sub = M.op_filter_bbox(gdf, {"bbox": win})
        wb = box(*win)
        assert len(sub) < len(gdf)
        assert bool(sub.geometry.apply(lambda g: wb.intersects(g)).all())

    def test_filter_attribute_predicate(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=100)
        sub = M.op_filter_attribute(gdf, {"field": "value", "cmp": ">", "value": 50})
        assert bool((sub["value"] > 50).all())

    def test_filter_attribute_comparators(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=100)
        lt = M.op_filter_attribute(gdf, {"field": "value", "cmp": "<", "value": 50})
        assert bool((lt["value"] < 50).all())

    def test_filter_attribute_missing_field_raises(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=10)
        with pytest.raises(M.ValidationError):
            M.op_filter_attribute(gdf, {"field": "nope", "value": 1})

    def test_filter_attribute_bad_cmp_raises(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=10)
        with pytest.raises(M.UsageError):
            M.op_filter_attribute(gdf, {"field": "value", "cmp": "~", "value": 1})

    def test_reproject(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=10)
        out = M.op_reproject(gdf, {"to_crs": "EPSG:3857"})
        assert out.crs.to_epsg() == 3857

    def test_add_field_area(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=10)
        out = M.op_add_field(gdf, {"name": "area", "source": "area"})
        assert "area" in out.columns
        assert bool((out["area"] > 0).all())

    def test_add_field_index(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=10)
        out = M.op_add_field(gdf, {"name": "seq", "source": "index"})
        assert list(out["seq"]) == list(range(1, 11))

    def test_add_field_unknown_source_raises(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=5)
        with pytest.raises(M.UsageError):
            M.op_add_field(gdf, {"name": "x", "source": "bogus"})

    def test_rename(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=5)
        out = M.op_rename(gdf, {"mapping": {"id": "fid"}})
        assert "fid" in out.columns and "id" not in out.columns

    def test_buffer(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=5)
        before = gdf.geometry.area.sum()
        out = M.op_buffer(gdf, {"distance": 0.01})
        assert out.geometry.area.sum() > before


class TestPipeline:
    def test_full_run_logs_and_counts(self, tmp_path):
        ctx = M.PipelineContext()
        cfg = M.default_config([116, 39, 117, 40], str(tmp_path), n=40)
        M.run_pipeline(cfg, ctx)
        # 至少 extract + 4 transform + load
        assert len(ctx.logs) >= 6
        assert all(l["status"] == "ok" for l in ctx.logs)
        assert ctx.logs[0]["op"] == "extract"
        # 要素单调不增（过滤只减不增）
        counts = [l["features_out"] for l in ctx.logs if l["op"] != "extract"]
        assert ctx.initial_count == 40
        assert counts[-1] <= 40

    def test_unknown_op_raises(self, tmp_path):
        ctx = M.PipelineContext()
        cfg = {
            "source": {"type": "synthetic", "bbox": [116, 39, 117, 40], "n": 5},
            "steps": [{"op": "explode"}],
        }
        with pytest.raises(M.UsageError):
            M.run_pipeline(cfg, ctx)

    def test_load_writes_file(self, tmp_path):
        ctx = M.PipelineContext()
        out_geojson = str(tmp_path / "etl_output.geojson")
        cfg = {
            "source": {"type": "synthetic", "bbox": [116, 39, 117, 40], "n": 10},
            "steps": [],
            "load": {"format": "geojson", "path": out_geojson},
        }
        M.run_pipeline(cfg, ctx)
        assert os.path.exists(out_geojson)


class TestQualityReport:
    def test_report_fields(self, tmp_path):
        ctx = M.PipelineContext()
        cfg = M.default_config([116, 39, 117, 40], str(tmp_path), n=40)
        M.run_pipeline(cfg, ctx)
        rep = M.quality_report(ctx)
        assert rep["initial_features"] == 40
        assert rep["final_features"] <= 40
        assert rep["dropped_features"] == 40 - rep["final_features"]
        assert 0 <= rep["retention"] <= 1
        assert rep["crs"] is not None
        assert "null_fractions" in rep


class TestLoadFormats:
    def test_load_geojson_empty(self, tmp_path):
        import geopandas as gpd
        from pyproj import CRS
        from shapely.geometry import Point
        gdf = gpd.GeoDataFrame({"a": []}, geometry=[], crs=CRS.from_epsg(4326))
        path = str(tmp_path / "empty.geojson")
        M.load_vector(gdf, path, "geojson")
        assert os.path.exists(path)

    def test_load_gpkg(self, tmp_path):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=5)
        path = str(tmp_path / "out.gpkg")
        M.load_vector(gdf, path, "gpkg")
        assert os.path.exists(path)

    def test_load_unknown_format_raises(self, tmp_path):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=5)
        with pytest.raises(M.UsageError):
            M.load_vector(gdf, str(tmp_path / "x.xyz"), "shapefile")


class TestExtract:
    def test_extract_synthetic(self):
        gdf = M.extract_synthetic([116, 39, 117, 40], n=20)
        assert len(gdf) == 20
        assert gdf.crs.to_epsg() == 4326

    def test_extract_file_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.extract_file("/nonexistent/nope.shp")
