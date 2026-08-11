"""Core algorithm tests for lulc-classification-ml."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ml


class TestNDVI:
    def test_vegetation_high(self):
        red = np.full((8, 8), 0.04, dtype=np.float32)
        nir = np.full((8, 8), 0.48, dtype=np.float32)
        ndvi = ml.compute_ndvi(red, nir)
        assert ndvi.mean() > 0.8  # (0.48-0.04)/(0.48+0.04)=0.846

    def test_water_low(self):
        red = np.full((8, 8), 0.03, dtype=np.float32)
        nir = np.full((8, 8), 0.01, dtype=np.float32)
        ndvi = ml.compute_ndvi(red, nir)
        assert ndvi.mean() < 0.0

    def test_zero_denominator(self):
        red = np.zeros((4, 4), dtype=np.float32)
        nir = np.zeros((4, 4), dtype=np.float32)
        ndvi = ml.compute_ndvi(red, nir)
        assert np.all(np.isfinite(ndvi))
        assert np.all(ndvi == 0.0)


class TestLocalVariance:
    def test_constant_is_zero(self):
        a = np.full((16, 16), 0.5, dtype=np.float32)
        var = ml.local_variance(a)
        assert var.max() < 1e-9

    def test_random_positive(self):
        rng = np.random.default_rng(0)
        a = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        var = ml.local_variance(a)
        assert var.mean() > 0.0


class TestBuildFeatures:
    def test_shape_and_names(self):
        cube = np.random.uniform(0, 1, (6, 12, 10)).astype(np.float32)
        feats, names = ml.build_features(cube)
        assert feats.shape == (120, 8)
        assert names == ["band0", "band1", "band2", "band3", "band4", "band5",
                         "ndvi", "texture_nir"]

    def test_too_few_bands_raises(self):
        cube = np.random.uniform(0, 1, (2, 8, 8)).astype(np.float32)
        with pytest.raises(ml.ValidationError):
            ml.build_features(cube)

    def test_pads_short_cube(self):
        cube = np.random.uniform(0, 1, (4, 6, 6)).astype(np.float32)
        feats, _ = ml.build_features(cube)
        assert feats.shape == (36, 8)
        # padded bands 4,5 are zero
        assert np.all(feats[:, 4] == 0.0)
        assert np.all(feats[:, 5] == 0.0)


class TestConfusionAccuracy:
    def test_perfect_accuracy(self):
        cm = np.array([[10, 0], [0, 10]], dtype=np.int64)
        acc = ml.accuracy_from_confusion(cm)
        assert acc["overall_accuracy"] == pytest.approx(1.0)
        assert acc["kappa"] == pytest.approx(1.0)

    def test_known_accuracy(self):
        # 4x4 with 6 correct of 8 → OA=0.75
        cm = np.array([[3, 1], [1, 3]], dtype=np.int64)
        acc = ml.accuracy_from_confusion(cm)
        assert acc["overall_accuracy"] == pytest.approx(0.75)
        assert acc["total_samples"] == 8

    def test_empty_confusion(self):
        cm = np.zeros((2, 2), dtype=np.int64)
        acc = ml.accuracy_from_confusion(cm)
        assert acc["overall_accuracy"] == 0.0
        assert acc["total_samples"] == 0


class TestMajorityFilter:
    def test_removes_salt_pixel(self):
        lab = np.full((9, 9), 1, dtype=np.int32)
        lab[4, 4] = 2  # isolated salt
        out = ml.majority_filter(lab)
        assert out[4, 4] == 1

    def test_preserves_block(self):
        lab = np.zeros((10, 10), dtype=np.int32)
        lab[:5, :] = 3
        out = ml.majority_filter(lab)
        # interior of each block stays the same
        assert out[1, 1] == 3
        assert out[8, 8] == 0


class TestClassifyPixels:
    def test_synthetic_accuracy_above_threshold(self):
        cube, labels, info = ml.generate_synthetic_scene(
            [116, 39, 117, 40], n_classes=5, width=64, height=64, seed=1)
        label_map, acc = ml.classify_pixels(
            cube, labels, method="rf", apply_filter=True, seed=1)
        assert label_map.shape == (64, 64)
        assert acc["overall_accuracy"] > 0.75

    def test_xgboost_method_runs(self):
        cube, labels, _ = ml.generate_synthetic_scene(
            [116, 39, 117, 40], n_classes=3, width=48, height=48, seed=2)
        _, acc = ml.classify_pixels(cube, labels, method="xgboost",
                                    apply_filter=False, seed=2)
        assert acc["method"] == "xgboost"
        assert 0.0 <= acc["overall_accuracy"] <= 1.0

    def test_unknown_method_raises(self):
        cube, labels, _ = ml.generate_synthetic_scene(
            [116, 39, 117, 40], n_classes=3, width=32, height=32)
        with pytest.raises(ml.UsageError):
            ml.classify_pixels(cube, labels, method="svm")

    def test_shape_mismatch_raises(self):
        cube = np.random.uniform(0, 1, (6, 16, 16)).astype(np.float32)
        labels = np.zeros((8, 8), dtype=np.int32)
        with pytest.raises(ml.ValidationError):
            ml.classify_pixels(cube, labels)

    def test_single_class_raises(self):
        cube = np.random.uniform(0, 1, (6, 16, 16)).astype(np.float32)
        labels = np.zeros((16, 16), dtype=np.int32)  # only class 0
        with pytest.raises(ml.ValidationError):
            ml.classify_pixels(cube, labels)


class TestAreaStats:
    def test_fractions_sum_to_one(self):
        lab = np.zeros((20, 20), dtype=np.int32)
        lab[:10, :] = 1
        stats = ml.class_area_stats(lab, [116, 39, 117, 40])
        total_frac = sum(c["fraction"] for c in stats["classes"])
        assert total_frac == pytest.approx(1.0)
        assert stats["total_pixels"] == 400
        assert len(stats["classes"]) == 2

    def test_area_positive(self):
        lab = np.ones((10, 10), dtype=np.int32)
        stats = ml.class_area_stats(lab, [116, 39, 117, 40])
        assert stats["total_area_km2"] > 0
        assert stats["classes"][0]["area_km2"] > 0


class TestSyntheticScene:
    def test_shape_and_labels(self):
        cube, labels, info = ml.generate_synthetic_scene(
            [116, 39, 117, 40], n_classes=5, width=48, height=40)
        assert cube.shape == (6, 40, 48)
        assert labels.shape == (40, 48)
        assert set(np.unique(labels).tolist()) <= set(range(5))
        assert info["n_classes"] == 5

    def test_n_classes_clamped(self):
        _, labels, info = ml.generate_synthetic_scene(
            [116, 39, 117, 40], n_classes=9, width=32, height=32)
        assert info["n_classes"] == 5  # clamped to len(CLASS_NAMES)
        assert labels.max() <= 4


class TestGeoTiffIO:
    def test_int_roundtrip(self, tmp_path):
        lab = np.random.randint(0, 5, (16, 16)).astype(np.int32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "lab.tif")
        ml.write_geotiff(path, lab, bbox, dtype="int32", nodata=-1)
        assert os.path.exists(path)
        back, rbbox = ml.read_geotiff(path)
        assert back.shape == (1, 16, 16)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_array_equal(back[0].astype(np.int32), lab)

    def test_read_missing_raises(self):
        with pytest.raises(ml.UsageError):
            ml.read_geotiff("/nonexistent/none.tif")
