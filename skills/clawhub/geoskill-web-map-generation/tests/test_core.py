"""Core algorithm tests for web-map-generation."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestStretch:
    def test_percentile_stretch_range(self):
        band = np.linspace(0, 1000, 64 * 64).reshape(64, 64).astype(np.float32)
        out, lo, hi = mod.percentile_stretch(band, 2.0, 98.0)
        assert out.min() >= 0.0
        assert out.max() <= 1.0
        assert lo < hi

    def test_percentile_stretch_constant(self):
        band = np.full((16, 16), 5.0, dtype=np.float32)
        out, lo, hi = mod.percentile_stretch(band)
        assert np.all(out == 0.0)
        assert lo == hi == 5.0

    def test_percentile_stretch_known_endpoints(self):
        # 0..99 -> p2≈1.98, p98≈97.02；端点外被裁剪到 0/1
        band = np.arange(100, dtype=np.float32).reshape(10, 10)
        out, lo, hi = mod.percentile_stretch(band, 2.0, 98.0)
        assert out[0, 0] == 0.0          # min clipped
        assert out[-1, -1] == 1.0        # max clipped
        assert abs(lo - np.percentile(band, 2)) < 1e-3

    def test_minmax_stretch_endpoints(self):
        band = np.array([[0, 5], [10, 15]], dtype=np.float32)
        out, lo, hi = mod.minmax_stretch(band)
        assert lo == 0.0 and hi == 15.0
        assert out[0, 0] == 0.0 and out[1, 1] == 1.0
        assert abs(out[0, 1] - 5 / 15) < 1e-6

    def test_minmax_stretch_empty(self):
        band = np.full((4, 4), np.nan, dtype=np.float32)
        out, lo, hi = mod.minmax_stretch(band)
        assert np.all(out == 0.0)


class TestColormap:
    def test_apply_colormap_shape_dtype(self):
        gray = np.random.uniform(0, 1, (20, 30)).astype(np.float32)
        rgb = mod.apply_colormap(gray, "viridis")
        assert rgb.shape == (20, 30, 3)
        assert rgb.dtype == np.uint8

    def test_colormap_monotonic_for_gray(self):
        # gray colormap：越亮值越大
        gray = np.array([[0.0, 1.0]], dtype=np.float32)
        rgb = mod.apply_colormap(gray, "gray")
        assert rgb[0, 1, 0] > rgb[0, 0, 0]

    def test_unknown_cmap_raises(self):
        gray = np.zeros((4, 4), dtype=np.float32)
        with pytest.raises(mod.UsageError):
            mod.apply_colormap(gray, "not_a_cmap")


class TestPngAndHtml:
    def test_png_magic_bytes(self):
        rgb = np.random.randint(0, 255, (8, 8, 3), dtype=np.uint8)
        png = mod.encode_png_bytes(rgb)
        assert png[:8] == b"\x89PNG\r\n\x1a\n"

    def test_encode_png_bad_shape_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.encode_png_bytes(np.zeros((8, 8), dtype=np.uint8))

    def test_leaflet_bounds_order(self):
        s = mod.leaflet_bounds([116.0, 39.0, 117.0, 40.0])
        assert s == "[[39.0, 116.0], [40.0, 117.0]]"

    def test_build_html_contains_parts(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        html = mod.build_leaflet_html(bbox, "QUJD", "MyTitle", 0.7, "terrain",
                                      {"a": 1})
        assert "QUJD" in html
        assert "[[39.0, 116.0], [40.0, 117.0]]" in html
        assert "MyTitle" in html
        assert "L.imageOverlay" in html


class TestSynthetic:
    def test_synthetic_shape_and_relief(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dem.shape == (128, 128)
        assert info["max_elev"] > info["min_elev"]
        # 有显著地形起伏（山丘）
        assert info["max_elev"] - info["min_elev"] > 500.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == (1, 16, 16)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
