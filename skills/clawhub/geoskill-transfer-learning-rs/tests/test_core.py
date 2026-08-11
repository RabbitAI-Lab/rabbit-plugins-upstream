"""Core algorithm tests for transfer-learning-rs."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBuildFeatures:
    def test_raw_vs_transfer_dims(self):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        raw = mod.build_features(cube, use_transfer=False)
        tr = mod.build_features(cube, use_transfer=True)
        assert raw.shape == (16 * 16, 3)
        assert tr.shape == (16 * 16, 9)  # 3 bands x (raw+grad+lmean)

    def test_deterministic(self):
        cube = np.random.uniform(0, 1, (2, 10, 10)).astype(np.float32)
        a = mod.build_features(cube, use_transfer=True)
        b = mod.build_features(cube, use_transfer=True)
        np.testing.assert_array_equal(a, b)

    def test_rejects_1d(self):
        with pytest.raises(mod.ValidationError):
            mod.build_features(np.zeros((5,)))

    def test_gradient_responds_to_edges(self):
        # 有边缘的波段梯度特征应大于平坦波段
        flat = np.zeros((1, 16, 16))
        edge = np.zeros((1, 16, 16))
        edge[0, :, 8:] = 1.0
        f_flat = mod.build_features(flat, use_transfer=True)
        f_edge = mod.build_features(edge, use_transfer=True)
        # 梯度通道索引：bands..2*bands -> 1..2
        assert f_edge[:, 1].mean() > f_flat[:, 1].mean()


class TestStandardize:
    def test_train_zero_mean_unit_std(self):
        rng = np.random.default_rng(0)
        x_tr = rng.normal(5, 3, (200, 4))
        x_te = rng.normal(5, 3, (50, 4))
        tr, te, mu, sigma = mod.standardize(x_tr, x_te)
        np.testing.assert_allclose(tr.mean(axis=0), 0.0, atol=1e-9)
        np.testing.assert_allclose(tr.std(axis=0), 1.0, atol=1e-6)
        # 测试集用训练集统计量变换
        np.testing.assert_allclose(te, (x_te - mu) / sigma, atol=1e-9)


class TestOverallAccuracy:
    def test_perfect(self):
        assert mod.overall_accuracy([0, 1, 2], [0, 1, 2]) == 1.0

    def test_partial(self):
        assert mod.overall_accuracy([0, 1, 1, 1], [0, 1, 0, 0]) == pytest.approx(0.5)

    def test_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.overall_accuracy([0, 1], [0, 1, 2])


class TestSplitIndices:
    def test_fractions(self):
        tr, te = mod.split_indices(100, 0.7, seed=1)
        assert tr.size == 70
        assert te.size == 30
        assert len(set(tr.tolist()) & set(te.tolist())) == 0

    def test_bad_frac_raises(self):
        with pytest.raises(mod.UsageError):
            mod.split_indices(10, 1.5)


class TestFinetune:
    def test_separable_high_acc(self):
        rng = np.random.default_rng(0)
        x = np.vstack([rng.normal(0, 0.2, (60, 3)), rng.normal(5, 0.2, (60, 3))])
        y = np.array([0] * 60 + [1] * 60)
        clf = mod.finetune_classifier(x, y, model="logreg")
        assert np.mean(clf.predict(x) == y) > 0.98

    def test_bad_model_raises(self):
        with pytest.raises(mod.UsageError):
            mod.finetune_classifier(np.zeros((10, 2)), np.zeros(10), model="xgb")


class TestTransferLearn:
    def test_synthetic_high_accuracy(self):
        cube, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=3)
        pred, info = mod.transfer_learn(cube, truth, train_frac=0.6,
                                        use_transfer=True, seed=3)
        assert pred.shape == truth.shape
        assert info["validation_accuracy"] > 0.85
        assert info["n_features"] == 12  # 4 bands x 3

    def test_truth_size_mismatch_raises(self):
        cube = np.zeros((3, 10, 10))
        with pytest.raises(mod.ValidationError):
            mod.transfer_learn(cube, np.zeros(50))

    def test_transfer_not_worse_than_raw(self):
        cube, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=7)
        _, info_tr = mod.transfer_learn(cube, truth, use_transfer=True, seed=7)
        _, info_raw = mod.transfer_learn(cube, truth, use_transfer=False, seed=7)
        assert info_tr["validation_accuracy"] >= info_raw["validation_accuracy"] - 0.05


class TestClusterFeatures:
    def test_labels_in_range(self):
        cube, _, _ = mod.generate_synthetic([116, 39, 117, 40], seed=1)
        labels, info = mod.cluster_features(cube, n_classes=3, seed=1)
        assert labels.shape == (64, 64)
        assert set(np.unique(labels)).issubset({0, 1, 2})


class TestSynthetic:
    def test_shapes(self):
        cube, truth, info = mod.generate_synthetic([116, 39, 117, 40], n_bands=4)
        assert cube.shape == (4, 64, 64)
        assert truth.shape == (64, 64)
        assert set(np.unique(truth)) == {0, 1, 2}


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
