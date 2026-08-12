"""Core algorithm tests for hyperspectral-classification."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as hc


class TestClassSpectra:
    def test_shape_and_range(self):
        spec = hc.class_spectra(4, 30, seed=1)
        assert spec.shape == (4, 30)
        assert spec.min() >= 0.01
        assert spec.max() <= 1.0

    def test_curves_distinct(self):
        """不同类别的光谱曲线应有明显差异（L2 距离 > 0）。"""
        spec = hc.class_spectra(4, 30, seed=1)
        for i in range(4):
            for j in range(i + 1, 4):
                dist = np.linalg.norm(spec[i] - spec[j])
                assert dist > 0.05

    def test_bad_args_raise(self):
        with pytest.raises(hc.UsageError):
            hc.class_spectra(0, 10)
        with pytest.raises(hc.UsageError):
            hc.class_spectra(3, 1)


class TestLabelMap:
    def test_all_classes_present(self):
        rng = np.random.default_rng(0)
        labels = hc.generate_label_map(64, 64, 4, rng)
        assert labels.shape == (64, 64)
        assert set(np.unique(labels).tolist()) == {0, 1, 2, 3}


class TestSynthetic:
    def test_cube_shape(self):
        cube, labels, info = hc.generate_synthetic([116, 39, 117, 40], n_bands=30, n_classes=4)
        assert cube.shape == (30, 64, 64)
        assert labels.shape == (64, 64)
        assert cube.min() >= 0.0 and cube.max() <= 1.0
        assert info["n_classes"] == 4


class TestSampling:
    def test_split_sizes(self):
        cube, labels, _ = hc.generate_synthetic([116, 39, 117, 40], n_bands=10, n_classes=3)
        Xtr, ytr, Xte, yte = hc.sample_pixels(cube, labels, n_per_class=100, seed=1)
        assert Xtr.shape[1] == 10
        assert Xte.shape[0] == yte.shape[0]
        assert Xtr.shape[0] > 0 and Xte.shape[0] > 0
        # 分层：每类都有训练样本
        assert set(np.unique(ytr).tolist()) == {0, 1, 2}


class TestClassifier:
    @pytest.mark.parametrize("method", ["rf", "svm"])
    def test_classification_accuracy(self, method):
        """端到端：合成数据分类总体精度 > 0.75。"""
        cube, labels, _ = hc.generate_synthetic([116, 39, 117, 40],
                                                n_bands=30, n_classes=4, seed=11)
        Xtr, ytr, Xte, yte = hc.sample_pixels(cube, labels, seed=3)
        model, pca = hc.train_classifier(Xtr, ytr, method=method)
        cmap = hc.classify_cube(cube, model, pca)
        assert cmap.shape == (64, 64)
        pred_te = model.predict(pca.transform(Xte))
        cm, _ = hc.confusion_matrix(yte, pred_te)
        oa = hc.overall_accuracy(cm)
        assert oa > 0.75, f"method={method} OA={oa}"

    def test_unknown_method_raises(self):
        X = np.random.rand(20, 5)
        y = np.array([0] * 10 + [1] * 10)
        with pytest.raises(hc.UsageError):
            hc.train_classifier(X, y, method="xgboost")

    def test_too_few_samples_raises(self):
        X = np.random.rand(1, 5)
        y = np.array([0])
        with pytest.raises(hc.ValidationError):
            hc.train_classifier(X, y, method="rf")


class TestPseudoLabels:
    def test_kmeans_labels(self):
        cube, labels, _ = hc.generate_synthetic([116, 39, 117, 40],
                                                n_bands=10, n_classes=3, seed=5)
        pl = hc.pseudo_labels(cube, 3)
        assert pl.shape == (64, 64)
        assert np.unique(pl).size >= 2


class TestConfusion:
    def test_perfect_accuracy(self):
        y = np.array([0, 0, 1, 1, 2])
        cm, classes = hc.confusion_matrix(y, y)
        assert hc.overall_accuracy(cm) == 1.0
        assert list(classes) == [0, 1, 2]

    def test_partial_accuracy(self):
        y_true = np.array([0, 0, 1, 1])
        y_pred = np.array([0, 1, 1, 1])
        cm, _ = hc.confusion_matrix(y_true, y_pred)
        assert hc.overall_accuracy(cm) == 0.75

    def test_empty_accuracy_zero(self):
        cm = np.zeros((2, 2), dtype=np.int64)
        assert hc.overall_accuracy(cm) == 0.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        hc.write_geotiff(path, cube, bbox)
        read_back, read_bbox = hc.read_geotiff(path)
        assert read_back.shape == cube.shape
        np.testing.assert_allclose(read_bbox, bbox, atol=1e-6)
        np.testing.assert_allclose(read_back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(hc.UsageError):
            hc.read_geotiff("/nonexistent/file.tif")
