"""Core algorithm tests for edge-detection-lineament."""
import sys
import os
import json

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestNormalize:
    def test_range_01(self):
        band = np.linspace(10, 500, 256).reshape(16, 16).astype(np.float32)
        out = mod.normalize01(band)
        assert out.min() >= 0.0
        assert out.max() <= 1.0
        np.testing.assert_allclose(out.min(), 0.0, atol=1e-9)
        np.testing.assert_allclose(out.max(), 1.0, atol=1e-9)

    def test_constant_band_zeros(self):
        band = np.full((8, 8), 3.0, dtype=np.float32)
        out = mod.normalize01(band)
        assert (out == 0).all()


class TestDetectEdges:
    def test_canny_binary(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        edges = mod.detect_edges(cube[0], method="canny", threshold=0.1)
        assert set(np.unique(edges)).issubset({0.0, 1.0})
        # 合成影像有清晰边缘，应有可观边缘像元
        assert edges.mean() > 0.01

    def test_sobel_binary(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        edges = mod.detect_edges(cube[0], method="sobel", threshold=0.3)
        assert set(np.unique(edges)).issubset({0.0, 1.0})
        assert edges.mean() > 0.0

    def test_flat_image_no_edges(self):
        band = np.full((32, 32), 0.5, dtype=np.float32)
        edges = mod.detect_edges(band, method="canny", threshold=0.1)
        assert edges.sum() == 0

    def test_bad_method_raises(self):
        band = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.detect_edges(band, method="bogus")


class TestExtractLineaments:
    def test_finds_lines_on_synthetic(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        edges = mod.detect_edges(cube[0], method="canny", threshold=0.1)
        lines = mod.extract_lineaments(edges, min_length=15)
        assert len(lines) >= 1
        # 每条线段是两个二元组
        for ln in lines:
            assert len(ln) == 2
            assert len(ln[0]) == 2

    def test_empty_mask_no_lines(self):
        mask = np.zeros((32, 32), dtype=np.float32)
        lines = mod.extract_lineaments(mask)
        assert lines == []


class TestPixelToGeo:
    def test_corner_mapping(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        lon, lat = mod.pixel_to_geo(0, 0, width=10, height=10, bbox=bbox)
        np.testing.assert_allclose(lon, 116.05, atol=1e-6)
        np.testing.assert_allclose(lat, 39.95, atol=1e-6)
        lon2, lat2 = mod.pixel_to_geo(9, 9, width=10, height=10, bbox=bbox)
        np.testing.assert_allclose(lon2, 116.95, atol=1e-6)
        np.testing.assert_allclose(lat2, 39.05, atol=1e-6)


class TestBuildGdf:
    def test_gdf_structure(self):
        lines = [((0, 0), (10, 10)), ((0, 5), (10, 5))]
        gdf = mod.build_lineaments_gdf(lines, width=20, height=20,
                                        bbox=[116, 39, 117, 40])
        assert len(gdf) == 2
        assert gdf.crs.to_epsg() == 4326
        assert (gdf.geometry.geom_type == "LineString").all()

    def test_empty_gdf(self):
        gdf = mod.build_lineaments_gdf([], width=20, height=20,
                                        bbox=[116, 39, 117, 40])
        assert len(gdf) == 0
        assert gdf.crs.to_epsg() == 4326


class TestWriteGeojson:
    def test_roundtrip_readable(self, tmp_path):
        lines = [((0, 0), (10, 10)), ((0, 5), (10, 5))]
        gdf = mod.build_lineaments_gdf(lines, width=20, height=20,
                                        bbox=[116, 39, 117, 40])
        path = str(tmp_path / "lines.geojson")
        n = mod.write_lineaments_geojson(path, gdf)
        assert n == 2
        assert os.path.exists(path)
        with open(path, encoding="utf-8") as f:
            doc = json.load(f)
        assert doc["type"] == "FeatureCollection"
        assert len(doc["features"]) == 2

    def test_empty_write(self, tmp_path):
        gdf = mod.build_lineaments_gdf([], width=20, height=20,
                                        bbox=[116, 39, 117, 40])
        path = str(tmp_path / "empty.geojson")
        n = mod.write_lineaments_geojson(path, gdf)
        assert n == 0
        assert os.path.exists(path)


class TestEdgeStats:
    def test_density(self):
        mask = np.zeros((10, 10), dtype=np.float32)
        mask[0:5, :] = 1.0
        st = mod.edge_stats(mask)
        assert st["n_edge_pixels"] == 50
        np.testing.assert_allclose(st["edge_density"], 0.5, atol=1e-9)


class TestSynthetic:
    def test_cube_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert cube.shape == (1, 96, 96)
        assert info["n_true_lines"] == 3


class TestGeoTiffIO:
    def test_write_read_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        back, rbbox = mod.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/path/file.tif")
