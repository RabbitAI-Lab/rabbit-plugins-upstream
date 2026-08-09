"""Core algorithm tests for data-catalog-generator."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


@pytest.fixture
def source_dir(tmp_path):
    d = str(tmp_path / "src")
    M.generate_synthetic([116, 39, 117, 40], d, size=8)
    return d


class TestScan:
    def test_scan_finds_all(self, source_dir):
        files = M.scan_directory(source_dir, recursive=True)
        # 2 tif + 1 geojson + 1 shp + 1 gpkg（不含 .shx/.dbf/.prj）
        assert len(files) == 5
        assert all(M.is_geodata(f) for f in files)

    def test_scan_skips_aux_files(self, source_dir):
        files = M.scan_directory(source_dir, recursive=True)
        exts = {os.path.splitext(f)[1].lower() for f in files}
        assert ".shx" not in exts and ".dbf" not in exts and ".prj" not in exts

    def test_scan_single_file(self, source_dir):
        one = os.path.join(source_dir, "dem.tif")
        assert M.scan_directory(one) == [one]

    def test_scan_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.scan_directory("/nonexistent/dir_xyz")


class TestMetadata:
    def test_raster_metadata(self, source_dir):
        e = M.extract_metadata(os.path.join(source_dir, "dem.tif"))
        assert e["status"] == "ok"
        assert e["kind"] == "raster"
        assert e["band_count"] == 1
        assert e["width"] == 8 and e["height"] == 8
        assert e["crs_epsg"] == 4326

    def test_multiband_raster(self, source_dir):
        e = M.extract_metadata(os.path.join(source_dir, "rgb.tif"))
        assert e["band_count"] == 3

    def test_vector_metadata_points(self, source_dir):
        e = M.extract_metadata(os.path.join(source_dir, "pois.geojson"))
        assert e["kind"] == "vector"
        assert e["feature_count"] == 8
        assert "Point" in e["geometry_types"]
        assert "id" in e["fields"]

    def test_vector_metadata_lines(self, source_dir):
        e = M.extract_metadata(os.path.join(source_dir, "roads.gpkg"))
        assert e["feature_count"] == 2
        assert any("Line" in g for g in e["geometry_types"])

    def test_unreadable_file_error(self, tmp_path):
        bad = tmp_path / "corrupt.tif"
        bad.write_bytes(b"not a real tiff")
        e = M.extract_metadata(str(bad))
        assert e["status"] == "error"
        assert e["error"]

    def test_unsupported_ext(self, tmp_path):
        f = tmp_path / "x.txt"
        f.write_text("hi", encoding="utf-8")
        e = M.extract_metadata(str(f))
        assert e["status"] == "error"


class TestClassify:
    def test_raster_categories(self):
        assert M.classify({"status": "ok", "kind": "raster", "band_count": 1}) == "Single-band raster"
        assert M.classify({"status": "ok", "kind": "raster", "band_count": 3}) == "Multispectral raster"
        assert M.classify({"status": "ok", "kind": "raster", "band_count": 200}) == "Hyperspectral raster"

    def test_vector_categories(self):
        assert M.classify({"status": "ok", "kind": "vector", "geometry_types": ["Point", "MultiPoint"]}) == "Point vector"
        assert M.classify({"status": "ok", "kind": "vector", "geometry_types": ["Polygon"]}) == "Polygon vector"
        assert M.classify({"status": "ok", "kind": "vector", "geometry_types": ["Point", "Polygon"]}) == "Mixed vector"

    def test_error_category(self):
        assert M.classify({"status": "error"}) == "Unreadable"


class TestCrsFamily:
    def test_families(self):
        assert M.crs_family(4326) == "Geographic (WGS 84)"
        assert M.crs_family(3857) == "Web Mercator"
        assert M.crs_family(32650).startswith("Projected")
        assert M.crs_family(None) == "Unknown CRS"


class TestCatalog:
    def test_build_summary(self, source_dir):
        files = M.scan_directory(source_dir, recursive=True)
        entries = [M.extract_metadata(f) for f in files]
        summ = M.build_catalog(entries)
        assert summ["n_files"] == 5
        assert summ["n_readable"] == 5
        assert summ["n_errors"] == 0
        # 8 点 + 1 面 + 2 线
        assert summ["total_vector_features"] == 11
        assert summ["categories"]["Point vector"] == 1
        assert summ["formats"]["GeoTIFF"] == 2

    def test_csv_written(self, source_dir, tmp_path):
        files = M.scan_directory(source_dir, recursive=True)
        entries = [M.extract_metadata(f) for f in files]
        csv_path = str(tmp_path / "catalog.csv")
        M.write_catalog_csv(entries, csv_path)
        with open(csv_path, encoding="utf-8") as f:
            lines = f.read().strip().splitlines()
        assert len(lines) == len(entries) + 1  # 表头 + 数据行
        assert lines[0].startswith("name,")

    def test_html_written(self, source_dir, tmp_path):
        files = M.scan_directory(source_dir, recursive=True)
        entries = [M.extract_metadata(f) for f in files]
        summ = M.build_catalog(entries)
        html_path = str(tmp_path / "catalog.html")
        M.write_catalog_html(entries, summ, html_path)
        content = open(html_path, encoding="utf-8").read()
        assert "<table" in content
        assert "dem.tif" in content
        assert "Data Catalog" in content
