"""Core algorithm tests for format-batch-converter."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestDetectKind:
    @pytest.mark.parametrize("name,kind", [
        ("a.tif", "raster"), ("b.TIFF", "raster"),
        ("c.geojson", "vector"), ("d.shp", "vector"),
        ("e.gpkg", "vector"), ("f.txt", None), ("g", None),
    ])
    def test_detect(self, name, kind):
        assert M.detect_kind(name) == kind


class TestVectorConvert:
    def test_geojson_to_gpkg_preserves_count(self, tmp_path):
        src = str(tmp_path / "src")
        M.generate_synthetic([116, 39, 117, 40], src, size=8)
        points_gj = os.path.join(src, "synthetic_points.geojson")
        dst = str(tmp_path / "points.gpkg")
        M.convert_vector(points_gj, dst, "gpkg")
        import geopandas as gpd
        assert len(gpd.read_file(dst)) == 10

    def test_geojson_to_shp_preserves_count(self, tmp_path):
        src = str(tmp_path / "src")
        M.generate_synthetic([116, 39, 117, 40], src, size=8)
        points_gj = os.path.join(src, "synthetic_points.geojson")
        dst = str(tmp_path / "points.shp")
        M.convert_vector(points_gj, dst, "shp")
        assert os.path.exists(dst)
        import geopandas as gpd
        assert len(gpd.read_file(dst)) == 10

    def test_unknown_target_raises(self, tmp_path):
        src = str(tmp_path / "src")
        M.generate_synthetic([116, 39, 117, 40], src, size=8)
        with pytest.raises(M.UsageError):
            M.convert_vector(os.path.join(src, "synthetic_points.geojson"),
                             str(tmp_path / "x.dxf"), "dxf")


class TestRasterConvert:
    def test_tif_to_tif_preserves_data(self, tmp_path):
        src = str(tmp_path / "src")
        M.generate_synthetic([116, 39, 117, 40], src, size=16)
        tif = os.path.join(src, "synthetic_raster.tif")
        dst = str(tmp_path / "out.tif")
        M.convert_raster(tif, dst)
        import rasterio
        with rasterio.open(tif) as a, rasterio.open(dst) as b:
            assert a.shape == b.shape
            assert a.count == b.count
            np.testing.assert_allclose(a.read(1), b.read(1), atol=1e-4)


class TestBatchConvert:
    def test_batch_all_converted(self, tmp_path):
        src = str(tmp_path / "src")
        M.generate_synthetic([116, 39, 117, 40], src, size=8)
        out = str(tmp_path / "out")
        res = M.batch_convert(src, out, raster_target="tif", vector_target="gpkg")
        assert res["summary"]["n_inputs"] == 3
        assert res["summary"]["n_converted"] == 3
        assert res["summary"]["n_errors"] == 0
        for e in res["entries"]:
            assert e["status"] == "ok"
            assert os.path.exists(e["target"])
            assert e["bytes"] > 0

    def test_unknown_ext_skipped(self, tmp_path):
        src = tmp_path / "src"
        src.mkdir()
        (src / "readme.txt").write_text("not geodata", encoding="utf-8")
        # 加一个有效文件，确保目录非空
        M.generate_synthetic([116, 39, 117, 40], str(src), size=8)
        out = str(tmp_path / "out")
        res = M.batch_convert(str(src), out)
        # txt 被 collect_inputs 直接过滤（不识别），因此不会出现在 entries
        kinds = {e["kind"] for e in res["entries"]}
        assert None not in kinds
        assert res["summary"]["n_converted"] == 3

    def test_missing_source_error_entry(self, tmp_path):
        # 直接对不存在的 .tif 调 convert_file → error 条目
        entry = M.convert_file(str(tmp_path / "ghost.tif"), str(tmp_path))
        assert entry["status"] == "error"
        assert entry["kind"] == "raster"

    def test_recursive_collect(self, tmp_path):
        root = tmp_path / "root"
        (root / "sub").mkdir(parents=True)
        M.generate_synthetic([116, 39, 117, 40], str(root / "sub"), size=8)
        files = M.collect_inputs(str(root), recursive=True)
        assert len(files) == 3
        files_flat = M.collect_inputs(str(root), recursive=False)
        assert len(files_flat) == 0  # 顶层无文件


class TestSynthetic:
    def test_generates_three_files(self, tmp_path):
        src = str(tmp_path / "src")
        paths = M.generate_synthetic([116, 39, 117, 40], src, size=8)
        assert len(paths) == 3
        for p in paths:
            assert os.path.exists(p)

    def test_collect_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.collect_inputs("/nonexistent/dir", recursive=False)
