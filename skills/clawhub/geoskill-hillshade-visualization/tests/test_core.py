"""Core algorithm tests for hillshade-visualization (Horn 解析解)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestHornAnalytic:
    def test_flat_plane_equals_sin_altitude(self):
        # 平面：坡度=0 → hs = sin(altitude)
        dem = np.full((20, 20), 100.0, dtype=np.float32)
        for alt in (30.0, 45.0, 60.0):
            hs = mod.horn_hillshade(dem, azimuth=315.0, altitude=alt)
            np.testing.assert_allclose(hs, np.sin(np.deg2rad(alt)), atol=1e-5)

    def test_west_rising_plane_fully_lit_from_west(self):
        # 平面 z = col（向东升高，坡面朝西）。光从西边来(azimuth=270)
        # 且 altitude=45 时，入射角=0 → hs=1
        jj = np.arange(24, dtype=np.float32)
        dem = np.tile(jj, (24, 1))
        hs = mod.horn_hillshade(dem, azimuth=270.0, altitude=45.0, cellsize=1.0)
        np.testing.assert_allclose(hs[4:-4, 4:-4], 1.0, atol=1e-4)

    def test_west_rising_plane_in_shadow_from_east(self):
        # 同样的平面，光从东边来(azimuth=90) → 背光面 hs=0
        jj = np.arange(24, dtype=np.float32)
        dem = np.tile(jj, (24, 1))
        hs = mod.horn_hillshade(dem, azimuth=90.0, altitude=45.0, cellsize=1.0)
        np.testing.assert_allclose(hs[4:-4, 4:-4], 0.0, atol=1e-4)

    def test_range_01(self):
        rng = np.random.default_rng(0)
        dem = rng.uniform(0, 500, (32, 32)).astype(np.float32)
        hs = mod.horn_hillshade(dem, azimuth=315.0, altitude=45.0)
        assert hs.min() >= 0.0 and hs.max() <= 1.0

    def test_invalid_altitude_raises(self):
        dem = np.ones((8, 8), dtype=np.float32)
        with pytest.raises(mod.UsageError):
            mod.horn_hillshade(dem, altitude=120.0)

    def test_zfactor_changes_relief(self):
        rng = np.random.default_rng(1)
        dem = rng.uniform(0, 100, (32, 32)).astype(np.float32)
        hs1 = mod.horn_hillshade(dem, z_factor=1.0)
        hs5 = mod.horn_hillshade(dem, z_factor=5.0)
        # 垂直夸张改变纹理（不完全相同）
        assert not np.allclose(hs1, hs5)


class TestMultiDirectional:
    def test_flat_plane_invariant_to_azimuths(self):
        dem = np.full((16, 16), 50.0, dtype=np.float32)
        hs, w = mod.multidirectional_hillshade(dem, azimuths=(0, 90, 180, 270), altitude=45.0)
        np.testing.assert_allclose(hs, np.sin(np.deg2rad(45.0)), atol=1e-5)
        np.testing.assert_allclose(w, [0.25, 0.25, 0.25, 0.25])

    def test_weights_normalize(self):
        dem = np.full((8, 8), 1.0, dtype=np.float32)
        _, w = mod.multidirectional_hillshade(dem, azimuths=(0, 90), weights=(1, 3))
        np.testing.assert_allclose(w, [0.25, 0.75])

    def test_weighted_sum_equals_manual(self):
        rng = np.random.default_rng(2)
        dem = rng.uniform(0, 200, (20, 20)).astype(np.float32)
        combined, w = mod.multidirectional_hillshade(
            dem, azimuths=(270, 315), weights=(2, 1), altitude=40.0)
        manual = (2 / 3) * mod.horn_hillshade(dem, 270, 40) \
            + (1 / 3) * mod.horn_hillshade(dem, 315, 40)
        np.testing.assert_allclose(combined, manual, atol=1e-6)

    def test_weight_length_mismatch_raises(self):
        dem = np.ones((8, 8), dtype=np.float32)
        with pytest.raises(mod.UsageError):
            mod.multidirectional_hillshade(dem, azimuths=(0, 90), weights=(1,))

    def test_empty_azimuths_raises(self):
        dem = np.ones((8, 8), dtype=np.float32)
        with pytest.raises(mod.UsageError):
            mod.multidirectional_hillshade(dem, azimuths=())


class TestColorOverlay:
    def test_full_light_returns_base_color(self):
        dem_norm = np.full((4, 4), 0.5, dtype=np.float32)
        hs = np.ones((4, 4), dtype=np.float32)
        rgb = mod.color_overlay(dem_norm, hs, "gray", ambient=0.2)
        # hs=1 → factor=1 → rgb = cmap(0.5)*255（gray cmap → ~128）
        assert rgb.shape == (4, 4, 3)
        assert abs(int(rgb[0, 0, 0]) - 128) <= 2

    def test_zero_light_gives_ambient(self):
        dem_norm = np.full((4, 4), 1.0, dtype=np.float32)
        hs = np.zeros((4, 4), dtype=np.float32)
        rgb = mod.color_overlay(dem_norm, hs, "gray", ambient=0.25)
        # hs=0 → factor=ambient=0.25 → 255*0.25 ≈ 64
        assert abs(int(rgb[0, 0, 0]) - 64) <= 2

    def test_unknown_cmap_raises(self):
        with pytest.raises(mod.UsageError):
            mod.color_overlay(np.zeros((2, 2)), np.ones((2, 2)), "bogus")


class TestSynthetic:
    def test_shape_and_relief(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dem.shape == (128, 128)
        assert info["max_elev"] - info["min_elev"] > 400.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (14, 14)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "h.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
