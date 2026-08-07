"""Core algorithm tests for time-series-classification."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ts


class TestClassTemplates:
    def test_all_classes_present(self):
        t = ts.class_templates(12)
        assert set(t.keys()) == {1, 2, 3, 4}
        for curve in t.values():
            assert curve.shape == (12,)
            assert curve.min() >= 0.0
            assert curve.max() <= 1.0

    def test_double_rice_has_two_humps(self):
        """双季稻曲线应有两个明显高峰。"""
        curve = ts.class_templates(12)[1]
        # 上半年和下半年各有一个高点
        assert curve[2:6].max() > 0.6
        assert curve[7:11].max() > 0.6


class TestExtractFeatures:
    def test_known_values(self):
        # 单像元已知曲线
        curve = np.array([0.1, 0.3, 0.8, 0.5, 0.2])[:, None]
        feats = ts.extract_features(curve)
        # max, min, amp, mean, peak_time, gsl, n_peaks
        assert feats.shape == (1, len(ts.FEATURE_NAMES))
        np.testing.assert_allclose(feats[0, 0], 0.8)   # max
        np.testing.assert_allclose(feats[0, 1], 0.1)   # min
        np.testing.assert_allclose(feats[0, 2], 0.7)   # amplitude
        np.testing.assert_allclose(feats[0, 4], 2.0)   # peak_time (index 2)

    def test_bimodal_two_peaks(self):
        series = ts.class_templates(12)[1][:, None]
        feats = ts.extract_features(series)
        assert feats[0, 6] == 2.0  # n_peaks

    def test_single_peak_one(self):
        series = ts.class_templates(12)[2][:, None]
        feats = ts.extract_features(series)
        assert feats[0, 6] == 1.0

    def test_requires_2d(self):
        with pytest.raises(ts.ValidationError):
            ts.extract_features(np.zeros((5, 4, 4)))

    def test_too_few_dates(self):
        with pytest.raises(ts.ValidationError):
            ts.extract_features(np.zeros((2, 10)))

    def test_vectorized_shape(self):
        series = np.random.uniform(0, 1, (12, 100))
        feats = ts.extract_features(series)
        assert feats.shape == (100, len(ts.FEATURE_NAMES))


class TestTrainingSet:
    def test_shape_and_labels(self):
        X, y = ts.make_training_set(12, n_per_class=50, seed=0)
        assert X.shape == (200, len(ts.FEATURE_NAMES))
        assert set(np.unique(y).tolist()) == {1, 2, 3, 4}

    def test_deterministic(self):
        X1, _ = ts.make_training_set(12, n_per_class=30, seed=5)
        X2, _ = ts.make_training_set(12, n_per_class=30, seed=5)
        np.testing.assert_array_equal(X1, X2)


class TestClassification:
    def test_accuracy_above_threshold(self):
        """合成场景整体分类精度应 > 0.7。"""
        synth = ts.generate_synthetic([116, 39, 117, 40], n_dates=12, seed=7)
        cube = synth["cube"]
        truth = synth["truth"]
        n_dates = cube.shape[0]
        X_train, y_train = ts.make_training_set(n_dates, seed=1)
        X_pred = ts.extract_features(cube.reshape(n_dates, -1))
        labels, imp = ts.train_and_classify(X_train, y_train, X_pred, seed=1)
        acc = float(np.mean(labels.reshape(truth.shape) == truth))
        assert acc > 0.7
        np.testing.assert_allclose(imp.sum(), 1.0, atol=1e-6)

    def test_feature_dim_mismatch_raises(self):
        with pytest.raises(ts.ValidationError):
            ts.train_and_classify(np.zeros((10, 7)), np.zeros(10), np.zeros((5, 6)))


class TestSynthetic:
    def test_cube_shape(self):
        synth = ts.generate_synthetic([116, 39, 117, 40], n_dates=8)
        assert synth["cube"].shape == (8, 64, 64)
        assert synth["truth"].shape == (64, 64)
        assert set(np.unique(synth["truth"]).tolist()) == {1, 2, 3, 4}


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 4, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        ts.write_geotiff(path, arr, bbox)
        back, rb = ts.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(ts.UsageError):
            ts.read_geotiff("/no/such/file.tif")
