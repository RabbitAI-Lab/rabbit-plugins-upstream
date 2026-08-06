"""Core algorithm tests for wetland-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as wm


class TestNormalizeDem:
    def test_range_01(self):
        dem = np.array([[100.0, 20.0], [60.0, 20.0]], dtype=np.float32)
        n = wm.normalize_dem(dem)
        assert n.min() == pytest.approx(0.0)
        assert n.max() == pytest.approx(1.0)
        # 20 -> 0, 100 -> 1
        assert n[0, 0] == pytest.approx(1.0)
        assert n[0, 1] == pytest.approx(0.0)
        assert n[1, 0] == pytest.approx(0.5)

    def test_constant_zero(self):
        dem = np.full((4, 4), 55.0, dtype=np.float32)
        n = wm.normalize_dem(dem)
        assert np.all(n == 0.0)


class TestClassifyHandcrafted:
    def test_four_pixels(self):
        # pixel columns: water, swamp, mudflat, non_wetland
        cube = np.zeros((4, 1, 4), dtype=np.float32)
        cube[wm.BAND_NDWI] = [[0.60, 0.15, 0.05, -0.20]]
        cube[wm.BAND_NDVI] = [[0.05, 0.55, 0.10, 0.35]]
        cube[wm.BAND_DEM] = [[0.10, 0.25, 0.20, 0.80]]
        cube[wm.BAND_SAR] = [[-20.0, -12.0, -15.0, -6.0]]
        cls, info = wm.classify_wetland(cube)
        assert cls[0].tolist() == [1, 2, 3, 0]
        assert set(info["masks"].keys()) == {"water", "swamp", "mudflat", "non_wetland"}

    def test_water_priority(self):
        # a pixel satisfying water AND swamp conditions -> water wins
        cube = np.array([[[0.60]], [[0.60]], [[0.10]], [[-20.0]]], dtype=np.float32)
        cls, _ = wm.classify_wetland(cube)
        assert cls[0, 0] == 1

    def test_high_elevation_excludes_swamp(self):
        # veg present but high elevation + high SAR -> non_wetland
        cube = np.array([[[0.10]], [[0.60]], [[0.80]], [[-6.0]]], dtype=np.float32)
        cls, _ = wm.classify_wetland(cube)
        assert cls[0, 0] == 0

    def test_bad_band_count_raises(self):
        cube = np.zeros((2, 4, 4), dtype=np.float32)
        with pytest.raises(wm.ValidationError):
            wm.classify_wetland(cube)

    def test_bad_ndim_raises(self):
        with pytest.raises(wm.ValidationError):
            wm.classify_wetland(np.zeros((4, 4), dtype=np.float32))


class TestSynthetic:
    def test_shape_and_codes(self):
        cube, truth, info = wm.generate_synthetic(
            [116, 39, 117, 40], width=64, height=48, seed=1)
        assert cube.shape == (4, 48, 64)
        assert truth.shape == (48, 64)
        assert set(np.unique(truth).tolist()) <= {0, 1, 2, 3}
        counts = info["truth_pixel_counts"]
        assert all(counts[k] > 0 for k in ["water", "swamp", "mudflat", "non_wetland"])

    def test_classification_matches_injection(self):
        cube, truth, info = wm.generate_synthetic(
            [116, 39, 117, 40], width=80, height=80, seed=2)
        cls, _ = wm.classify_wetland(cube)
        acc = wm.classification_accuracy(cls, truth)
        assert acc["overall_accuracy"] > 0.95
        for name in ["water", "swamp", "mudflat"]:
            assert acc["per_class_recall"][name] > 0.9

    def test_dem_band_normalized(self):
        cube, _, _ = wm.generate_synthetic(
            [116, 39, 117, 40], width=40, height=40, seed=3)
        assert cube[wm.BAND_DEM].min() >= -0.1
        assert cube[wm.BAND_DEM].max() <= 1.1


class TestAreaStats:
    def test_fractions_sum_to_one(self):
        cube, truth, _ = wm.generate_synthetic(
            [116, 39, 117, 40], width=48, height=48, seed=4)
        cls, _ = wm.classify_wetland(cube)
        stats = wm.wetland_area_stats(cls, [116, 39, 117, 40])
        total_frac = sum(c["fraction"] for c in stats["classes"])
        assert total_frac == pytest.approx(1.0)
        assert len(stats["classes"]) == 4
        assert 0.0 < stats["wetland_fraction"] < 1.0
        assert stats["wetland_area_km2"] > 0


class TestAccuracy:
    def test_perfect(self):
        a = np.array([0, 1, 2, 3])
        acc = wm.classification_accuracy(a, a)
        assert acc["overall_accuracy"] == 1.0

    def test_known(self):
        pred = np.array([1, 1, 0, 0])
        truth = np.array([1, 0, 0, 0])
        acc = wm.classification_accuracy(pred, truth)
        assert acc["overall_accuracy"] == pytest.approx(0.75)


class TestGeoTiffIO:
    def test_cube_roundtrip(self, tmp_path):
        cube = np.random.uniform(-1, 1, (4, 12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "layers.tif")
        wm.write_geotiff(path, cube, bbox, dtype="float32")
        back, rbbox = wm.read_cube(path)
        assert back.shape == (4, 12, 12)
        np.testing.assert_allclose(back, cube, atol=1e-6)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(wm.UsageError):
            wm.read_cube("/nonexistent/none.tif")
