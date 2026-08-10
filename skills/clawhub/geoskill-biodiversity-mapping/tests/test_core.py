"""Core algorithm tests for biodiversity-mapping (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestNDVI:
    def test_vegetation_high_positive(self):
        red = np.full((8, 8), 0.04, dtype=np.float32)
        nir = np.full((8, 8), 0.45, dtype=np.float32)
        v = M.ndvi(red, nir)
        assert float(np.mean(v)) > 0.8  # (0.45-0.04)/(0.45+0.04) ~ 0.837

    def test_water_negative(self):
        red = np.full((8, 8), 0.11, dtype=np.float32)
        nir = np.full((8, 8), 0.02, dtype=np.float32)
        v = M.ndvi(red, nir)
        assert float(np.mean(v)) < 0.0

    def test_range_clipped(self):
        rng = np.random.default_rng(0)
        red = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        nir = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        v = M.ndvi(red, nir)
        assert v.min() >= -1.0
        assert v.max() <= 1.0

    def test_zero_denominator_safe(self):
        red = np.zeros((4, 4), dtype=np.float32)
        nir = np.zeros((4, 4), dtype=np.float32)
        v = M.ndvi(red, nir)
        assert np.all(v == 0.0)


class TestHeterogeneity:
    def test_constant_surface_zero(self):
        a = np.full((32, 32), 0.5, dtype=np.float32)
        h = M.local_heterogeneity(a, window=5)
        assert float(np.max(h)) < 1e-5

    def test_noisy_surface_positive(self):
        rng = np.random.default_rng(1)
        a = rng.uniform(0, 1, (64, 64)).astype(np.float32)
        h = M.local_heterogeneity(a, window=5)
        assert float(np.mean(h)) > 0.05

    def test_more_noise_more_hetero(self):
        rng = np.random.default_rng(2)
        base = np.full((64, 64), 0.5, dtype=np.float32)
        low = base + rng.normal(0, 0.01, base.shape).astype(np.float32)
        high = base + rng.normal(0, 0.3, base.shape).astype(np.float32)
        assert float(np.mean(M.local_heterogeneity(high))) > float(
            np.mean(M.local_heterogeneity(low)))


class TestTerrainRoughness:
    def test_flat_zero(self):
        dem = np.full((32, 32), 100.0, dtype=np.float32)
        r = M.terrain_roughness(dem)
        assert float(np.max(r)) < 1e-4

    def test_tilted_positive(self):
        yy, xx = np.mgrid[0:32, 0:32].astype(np.float32)
        dem = 10.0 * xx  # plane sloping in x
        r = M.terrain_roughness(dem)
        assert float(np.mean(r)) > 5.0  # gradient magnitude ~ 10


class TestNormalize:
    def test_bounds(self):
        rng = np.random.default_rng(3)
        a = rng.uniform(-5, 5, (16, 16)).astype(np.float32)
        n = M.normalize01(a)
        assert n.min() >= 0.0
        assert n.max() <= 1.0
        assert abs(float(n.max()) - 1.0) < 1e-6

    def test_constant_returns_zero(self):
        a = np.full((8, 8), 3.14, dtype=np.float32)
        n = M.normalize01(a)
        assert np.all(n == 0.0)


class TestSpeciesRichness:
    def _proxies(self, val):
        a = np.full((16, 16), val, dtype=np.float32)
        return a, a, a

    def test_bounded_by_smax(self):
        rng = np.random.default_rng(4)
        ndvi_a = rng.uniform(-1, 1, (32, 32)).astype(np.float32)
        tex = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        rough = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        rich, q = M.species_richness(ndvi_a, tex, rough, s_max=200.0)
        assert rich.min() >= 0.0
        assert rich.max() <= 200.0 + 1e-3
        assert q.min() >= 0.0
        assert q.max() <= 1.0 + 1e-6

    def test_monotonic_in_quality(self):
        # 单一代理从低到高，丰富度应单调上升（其余代理恒定 -> 归一化为 0）
        rng = np.random.default_rng(5)
        ndvi_low = rng.uniform(0.0, 0.2, (32, 32)).astype(np.float32)
        ndvi_high = rng.uniform(0.7, 1.0, (32, 32)).astype(np.float32)
        tex = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        rough = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        rich_low, _ = M.species_richness(ndvi_low, tex, rough, method="productivity")
        rich_high, _ = M.species_richness(ndvi_high, tex, rough, method="productivity")
        assert float(np.mean(rich_high)) > float(np.mean(rich_low))

    def test_unknown_method_raises(self):
        a = np.zeros((4, 4), dtype=np.float32)
        with pytest.raises(M.UsageError):
            M.species_richness(a, a, a, method="bogus")


class TestSynthetic:
    def test_shape_and_bands(self):
        cube, info = M.generate_synthetic([116, 39, 117, 40])
        assert cube.shape[0] == 3
        assert cube.shape[1] == 128 and cube.shape[2] == 128
        assert info["bands"] == ["red", "nir", "dem"]

    def test_vegetation_ndvi_positive_in_scene(self):
        cube, info = M.generate_synthetic([116, 39, 117, 40], seed=7)
        v = M.ndvi(cube[0], cube[1])
        # 场景含植被区，NDVI 最大值应明显为正
        assert float(np.max(v)) > 0.7
        assert float(np.min(v)) < 0.2  # 水体区低/负


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(8).uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        M.write_geotiff(path, cube, bbox)
        back, rb = M.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_geotiff("/nonexistent/file.tif")
