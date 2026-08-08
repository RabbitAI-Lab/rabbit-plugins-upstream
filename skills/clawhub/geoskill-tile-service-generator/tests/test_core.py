"""Core algorithm tests for tile-service-generator."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestTileMath:
    def test_world_tile_z0(self):
        assert M.lon_to_tile_x(-180.0, 0) == 0
        assert M.lon_to_tile_x(180.0, 0) == 1

    def test_lon_roundtrip(self):
        lon = 116.4
        for z in (1, 5, 10):
            x = M.lon_to_tile_x(lon, z)
            assert M.tile_x_to_lon(x, z) == pytest.approx(lon, abs=1e-9)

    def test_lat_roundtrip(self):
        lat = 39.9
        for z in (1, 5, 10):
            y = M.lat_to_tile_y(lat, z)
            assert M.tile_y_to_lat(y, z) == pytest.approx(lat, abs=1e-9)

    def test_tile_bounds_monotonic(self):
        # 相邻瓦片边界应无缝拼接
        w1, s1, e1, n1 = M.tile_lonlat_bounds(210, 96, 8)
        w2, s2, e2, n2 = M.tile_lonlat_bounds(211, 96, 8)
        assert e1 == pytest.approx(w2, abs=1e-9)

    def test_tile_range_covers_bbox(self):
        bbox = [116, 39, 117, 40]
        x0, y0, x1, y1 = M.tile_range_for_bbox(bbox, 8)
        assert x0 <= x1 and y0 <= y1
        # bbox 中心应落在范围内
        cx = M.lon_to_tile_x(116.5, 8)
        cy = M.lat_to_tile_y(39.5, 8)
        assert x0 <= int(cx) <= x1
        assert y0 <= int(cy) <= y1


class TestQuadkey:
    def test_known_value(self):
        # Bing 文档经典示例：z=3, x=3, y=5 -> "213"
        assert M.quadkey(3, 5, 3) == "213"

    def test_length_equals_zoom(self):
        assert len(M.quadkey(3, 5, 3)) == 3
        assert len(M.quadkey(0, 0, 1)) == 1

    def test_z0_empty(self):
        assert M.quadkey(0, 0, 0) == ""

    def test_digits_in_03(self):
        key = M.quadkey(210, 96, 8)
        assert all(c in "0123" for c in key)


class TestMercator:
    def test_origin(self):
        x, y = M.lonlat_to_mercator(0, 0)
        assert x == pytest.approx(0.0, abs=1e-6)
        assert y == pytest.approx(0.0, abs=1e-6)

    def test_roundtrip(self):
        for lon, lat in [(116.4, 39.9), (-73.9, 40.7), (121.47, 31.23)]:
            mx, my = M.lonlat_to_mercator(lon, lat)
            rl, ra = M.mercator_to_lonlat(mx, my)
            assert rl == pytest.approx(lon, abs=1e-6)
            assert ra == pytest.approx(lat, abs=1e-6)


class TestPNG:
    def test_encode_decode_size(self, tmp_path):
        arr = (np.arange(16 * 16) % 256).reshape(16, 16).astype(np.uint8)
        path = str(tmp_path / "t.png")
        M.encode_png_grayscale(path, arr)
        assert M.decode_png_size(path) == (16, 16)

    def test_signature(self, tmp_path):
        arr = np.zeros((8, 8), dtype=np.uint8)
        path = str(tmp_path / "t.png")
        M.encode_png_grayscale(path, arr)
        with open(path, "rb") as f:
            assert f.read(8) == b"\x89PNG\r\n\x1a\n"

    def test_decode_invalid_raises(self, tmp_path):
        path = str(tmp_path / "bad.png")
        with open(path, "wb") as f:
            f.write(b"not a png")
        with pytest.raises(M.ValidationError):
            M.decode_png_size(path)


class TestNormalize:
    def test_nan_to_zero(self):
        tile = np.full((4, 4), np.nan)
        out = M.normalize_uint8(tile)
        assert out.dtype == np.uint8
        assert out.max() == 0

    def test_stretch_to_255(self):
        tile = np.linspace(0, 10, 16).reshape(4, 4)
        out = M.normalize_uint8(tile)
        assert out.min() == 0
        assert out.max() == 255

    def test_constant_tile_mid(self):
        tile = np.full((4, 4), 5.0)
        out = M.normalize_uint8(tile)
        assert out.min() == 128


class TestResampleTile:
    def test_tile_shape(self):
        band = np.random.default_rng(0).uniform(0, 100, (32, 32)).astype(np.float32)
        tile = M.resample_tile(band, [116, 39, 117, 40], 210, 96, 8, tile_size=32)
        assert tile.shape == (32, 32)

    def test_inside_bbox_finite(self):
        # 取完全覆盖栅格的瓦片级别（低级别可能跨界），这里直接用栅格中心采样
        band = np.ones((32, 32), dtype=np.float32) * 7.0
        x0, y0, _, _ = M.tile_range_for_bbox([116, 39, 117, 40], 8)
        tile = M.resample_tile(band, [116, 39, 117, 40], x0, y0, 8, tile_size=16)
        # 与栅格重叠的像元应为 7.0
        finite = tile[np.isfinite(tile)]
        assert finite.size > 0
        assert np.allclose(finite, 7.0)


class TestGenerateTiles:
    def test_generates_files_and_meta(self, tmp_path):
        band = np.random.default_rng(1).uniform(0, 100, (32, 32)).astype(np.float32)
        meta = M.generate_tiles(band, [116, 39, 117, 40], [6, 7],
                                str(tmp_path), tile_size=32)
        assert meta["total_tiles"] > 0
        for zkey, zval in meta["zooms"].items():
            assert zval["count"] == len(zval["tiles"])
            for t in zval["tiles"]:
                p = os.path.join(str(tmp_path), "tiles", t["path"])
                assert os.path.exists(p)
                w, h = M.decode_png_size(p)
                assert (w, h) == (32, 32)


class TestSynthetic:
    def test_generate(self):
        cube, info = M.generate_synthetic([116, 39, 117, 40], size=32)
        assert cube.shape == (1, 32, 32)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(2).uniform(0, 1, (1, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        M.write_geotiff(path, cube, bbox)
        back, rbbox = M.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_geotiff("/nonexistent/nope.tif")
