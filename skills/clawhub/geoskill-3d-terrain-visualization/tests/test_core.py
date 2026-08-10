"""Core algorithm tests for 3d-terrain-visualization."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestNormals:
    def test_planar_surface_normals(self):
        # 平面 z = 2x（沿列方向），梯度 gx=2, gy=0
        # 单位法向量 = (-2, 0, 1)/sqrt(5)
        h = w = 20
        jj = np.arange(w, dtype=np.float32)
        dem = np.tile(2.0 * jj, (h, 1))
        nx, ny, nz = mod.dem_normals(dem, cellsize=1.0, zfactor=1.0)
        exp_nx = -2.0 / np.sqrt(5.0)
        exp_nz = 1.0 / np.sqrt(5.0)
        # 取内部像元避开边界差分误差
        assert np.allclose(nx[5:15, 5:15], exp_nx, atol=1e-3)
        assert np.allclose(ny[5:15, 5:15], 0.0, atol=1e-3)
        assert np.allclose(nz[5:15, 5:15], exp_nz, atol=1e-3)

    def test_normals_are_unit_vectors(self):
        dem = np.random.uniform(0, 100, (32, 32)).astype(np.float32)
        nx, ny, nz = mod.dem_normals(dem)
        mag = np.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
        np.testing.assert_allclose(mag, 1.0, atol=1e-5)

    def test_flat_surface_normal_up(self):
        dem = np.full((16, 16), 50.0, dtype=np.float32)
        nx, ny, nz = mod.dem_normals(dem)
        assert np.allclose(nx, 0.0, atol=1e-6)
        assert np.allclose(ny, 0.0, atol=1e-6)
        assert np.allclose(nz, 1.0, atol=1e-6)


class TestLighting:
    def test_light_vector_zenith(self):
        lx, ly, lz = mod.light_vector(0.0, 90.0)
        assert abs(lx) < 1e-6 and abs(ly) < 1e-6
        assert abs(lz - 1.0) < 1e-6

    def test_light_vector_east_horizon(self):
        lx, ly, lz = mod.light_vector(90.0, 0.0)
        assert abs(lx - 1.0) < 1e-6
        assert abs(ly) < 1e-6 and abs(lz) < 1e-6

    def test_lambertian_full_and_zero(self):
        # 法向 (0,0,1)：正上方光 → 1；水平光 → 0
        nx = ny = np.zeros((4, 4)); nz = np.ones((4, 4))
        assert np.allclose(mod.lambertian_shade(nx, ny, nz, 0, 0, 1), 1.0)
        assert np.allclose(mod.lambertian_shade(nx, ny, nz, 1, 0, 0), 0.0)

    def test_lambertian_45deg(self):
        # 法向 (0,0,1)，光 45° 高 → cos(45)=0.707
        nx = ny = np.zeros((2, 2)); nz = np.ones((2, 2))
        shade = mod.lambertian_shade(nx, ny, nz, 0.0, 1 / np.sqrt(2), 1 / np.sqrt(2))
        np.testing.assert_allclose(shade, 1 / np.sqrt(2), atol=1e-6)

    def test_shade_color_overlay_extremes(self):
        rgb = np.ones((4, 4, 3), dtype=np.float32)
        full = mod.shade_color_overlay(rgb, np.ones((4, 4)), ambient=0.2)
        dark = mod.shade_color_overlay(rgb, np.zeros((4, 4)), ambient=0.2)
        np.testing.assert_allclose(full, 1.0, atol=1e-6)
        np.testing.assert_allclose(dark, 0.2, atol=1e-6)


class TestRender:
    def test_png_magic(self):
        rgb = np.random.randint(0, 255, (8, 8, 3), dtype=np.uint8)
        assert mod.encode_png_bytes(rgb)[:8] == b"\x89PNG\r\n\x1a\n"

    def test_viewer_html_contains_image(self):
        html = mod.build_viewer_html("QUJD", {"title": "T", "exaggeration": 3.0})
        assert "QUJD" in html
        assert "perspective" in html
        assert "exag" in html


class TestSynthetic:
    def test_shape_and_relief(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dem.shape == (128, 128)
        assert info["max_elev"] > info["min_elev"]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb, res = mod.read_geotiff(path)
        assert back.shape == (1, 16, 16)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        assert res > 0

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
