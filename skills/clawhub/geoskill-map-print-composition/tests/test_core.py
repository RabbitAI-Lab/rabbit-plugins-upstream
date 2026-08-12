"""Core algorithm tests for map-print-composition."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestAlphaComposite:
    def test_alpha_zero_returns_base(self):
        base = np.full((4, 4, 3), 0.2, dtype=np.float32)
        overlay = np.full((4, 4, 3), 0.9, dtype=np.float32)
        out = mod.alpha_composite(base, overlay, 0.0)
        np.testing.assert_allclose(out, base, atol=1e-6)

    def test_alpha_one_returns_overlay(self):
        base = np.full((4, 4, 3), 0.2, dtype=np.float32)
        overlay = np.full((4, 4, 3), 0.9, dtype=np.float32)
        out = mod.alpha_composite(base, overlay, 1.0)
        np.testing.assert_allclose(out, overlay, atol=1e-6)

    def test_alpha_half_is_mean(self):
        base = np.full((3, 3, 3), 0.2, dtype=np.float32)
        overlay = np.full((3, 3, 3), 0.8, dtype=np.float32)
        out = mod.alpha_composite(base, overlay, 0.5)
        np.testing.assert_allclose(out, 0.5, atol=1e-6)

    def test_alpha_clipped(self):
        base = np.zeros((2, 2, 3), dtype=np.float32)
        overlay = np.ones((2, 2, 3), dtype=np.float32)
        np.testing.assert_allclose(mod.alpha_composite(base, overlay, 5.0), 1.0)
        np.testing.assert_allclose(mod.alpha_composite(base, overlay, -5.0), 0.0)


class TestHillshadeBlend:
    def test_full_light_returns_color(self):
        rgb = np.full((4, 4, 3), 0.7, dtype=np.float32)
        hs = np.ones((4, 4), dtype=np.float32)
        out = mod.hillshade_blend(rgb, hs, ambient=0.0)
        np.testing.assert_allclose(out, 0.7, atol=1e-6)

    def test_zero_light_returns_ambient(self):
        rgb = np.full((4, 4, 3), 0.7, dtype=np.float32)
        hs = np.zeros((4, 4), dtype=np.float32)
        out = mod.hillshade_blend(rgb, hs, ambient=0.3)
        np.testing.assert_allclose(out, 0.7 * 0.3, atol=1e-6)

    def test_blend_darkens_shadow(self):
        rgb = np.full((2, 2, 3), 0.8, dtype=np.float32)
        bright = mod.hillshade_blend(rgb, np.ones((2, 2)))
        dark = mod.hillshade_blend(rgb, np.zeros((2, 2)))
        assert bright.mean() > dark.mean()


class TestHillshade:
    def test_flat_plane(self):
        dem = np.full((12, 12), 50.0, dtype=np.float32)
        hs = mod.horn_hillshade(dem, altitude=45.0)
        np.testing.assert_allclose(hs, np.sin(np.deg2rad(45.0)), atol=1e-5)

    def test_range(self):
        rng = np.random.default_rng(0)
        dem = rng.uniform(0, 300, (24, 24)).astype(np.float32)
        hs = mod.horn_hillshade(dem)
        assert hs.min() >= 0.0 and hs.max() <= 1.0


class TestColorAndIO:
    def test_dem_to_color_range(self):
        dem = np.random.uniform(0, 500, (16, 16)).astype(np.float32)
        rgb = mod.dem_to_color(dem, "terrain")
        assert rgb.shape == (16, 16, 3)
        assert rgb.min() >= 0.0 and rgb.max() <= 1.0

    def test_unknown_cmap_raises(self):
        with pytest.raises(mod.UsageError):
            mod.dem_to_color(np.zeros((4, 4)), "bogus")

    def test_rgb_geotiff_roundtrip(self, tmp_path):
        rgb = np.random.randint(0, 255, (10, 12, 3), dtype=np.uint8)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "rgb.tif")
        mod.write_geotiff_rgb(path, rgb, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == (3, 10, 12)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        # 各通道值读回一致
        for i in range(3):
            np.testing.assert_allclose(back[i], rgb[..., i], atol=1)

    def test_rgb_geotiff_bad_shape_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.write_geotiff_rgb("x.tif", np.zeros((4, 4)), [0, 0, 1, 1])


class TestPdfAndSynthetic:
    def test_render_pdf_magic(self, tmp_path):
        rgb = np.random.randint(0, 255, (8, 8, 3), dtype=np.uint8)
        path = str(tmp_path / "t.pdf")
        mod.render_pdf(path, rgb, [0, 0, 1, 1], "T", dpi=72)
        with open(path, "rb") as f:
            assert f.read(4) == b"%PDF"

    def test_synthetic_shape(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dem.shape == (128, 128)
        assert info["max_elev"] > info["min_elev"]
