"""Core algorithm tests for few-shot-classification."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestPixelFeatures:
    def test_shape(self):
        cube = np.random.uniform(0, 1, (4, 10, 12)).astype(np.float32)
        feats, nb, h, w = mod.pixel_features(cube)
        assert feats.shape == (120, 4)
        assert (nb, h, w) == (4, 10, 12)

    def test_rejects_1d(self):
        with pytest.raises(mod.ValidationError):
            mod.pixel_features(np.zeros((5,)))


class TestComputePrototypes:
    def test_exact_means(self):
        feats = np.array([[0.0, 0.0], [2.0, 2.0], [10.0, 0.0], [12.0, 0.0]])
        labels = np.array([0, 0, 1, 1])
        protos, classes = mod.compute_prototypes(feats, labels)
        np.testing.assert_array_equal(classes, [0, 1])
        np.testing.assert_allclose(protos[0], [1.0, 1.0])
        np.testing.assert_allclose(protos[1], [11.0, 0.0])

    def test_missing_class_raises(self):
        feats = np.array([[0.0, 0.0], [1.0, 1.0]])
        labels = np.array([0, 0])
        with pytest.raises(mod.UsageError):
            mod.compute_prototypes(feats, labels, classes=np.array([0, 1]))

    def test_length_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.compute_prototypes(np.zeros((3, 2)), np.array([0, 1]))


class TestDistances:
    def test_hand_computed(self):
        x = np.array([[0.0, 0.0]])
        protos = np.array([[3.0, 4.0], [0.0, 0.0]])
        d = mod.euclidean_distances(x, protos)
        np.testing.assert_allclose(d, [[5.0, 0.0]], atol=1e-9)

    def test_symmetric_zero_self(self):
        protos = np.array([[1.0, 2.0]])
        d = mod.euclidean_distances(protos, protos)
        assert d[0, 0] == pytest.approx(0.0)


class TestPrototypeProbabilities:
    def test_rows_sum_to_one(self):
        d = np.array([[0.0, 1.0, 2.0], [5.0, 5.0, 0.1]])
        probs = mod.prototype_probabilities(d)
        np.testing.assert_allclose(probs.sum(axis=1), [1.0, 1.0], atol=1e-9)

    def test_closer_higher_prob(self):
        d = np.array([[0.0, 1.0]])
        probs = mod.prototype_probabilities(d)
        # softmax([0, -1]) -> [0.731, 0.269]
        assert probs[0, 0] == pytest.approx(0.7310586, abs=1e-6)
        assert probs[0, 0] > probs[0, 1]

    def test_numerically_stable_large_dist(self):
        d = np.array([[1000.0, 1001.0]])
        probs = mod.prototype_probabilities(d)
        assert np.isfinite(probs).all()
        assert probs.sum() == pytest.approx(1.0)


class TestClassify:
    def test_nearest_prototype(self):
        protos = np.array([[0.0, 0.0], [10.0, 10.0]])
        classes = np.array([0, 1])
        query = np.array([[0.5, 0.5], [9.0, 9.5], [100.0, 100.0]])
        pred, probs = mod.classify(query, protos, classes)
        np.testing.assert_array_equal(pred, [0, 1, 1])
        assert probs.shape == (3, 2)


class TestStandardize:
    def test_support_centered(self):
        rng = np.random.default_rng(0)
        feats = rng.normal(10, 2, (100, 3))
        sup_idx = np.arange(30)
        std, mu, sigma = mod.standardize_fit_transform(feats, sup_idx)
        np.testing.assert_allclose(std[sup_idx].mean(axis=0), 0.0, atol=1e-9)


class TestFewShotEpisode:
    def test_synthetic_high_accuracy(self):
        cube, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=4)
        feats, _, _, _ = mod.pixel_features(cube)
        result = mod.few_shot_episode(feats, truth.ravel(), n_shot=3, seed=4)
        assert result["accuracy"] > 0.9
        assert result["n_shot"] == 3
        assert result["n_classes"] == 3
        assert result["n_support"] == 9

    def test_one_shot_works(self):
        cube, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=6)
        feats, _, _, _ = mod.pixel_features(cube)
        result = mod.few_shot_episode(feats, truth.ravel(), n_shot=1, seed=6)
        assert result["accuracy"] > 0.85

    def test_too_few_samples_raises(self):
        feats = np.zeros((4, 2))
        labels = np.array([0, 0, 1, 1])
        with pytest.raises(mod.ValidationError):
            mod.few_shot_episode(feats, labels, n_shot=2)  # 每类只有 2 个，需 >= 3

    def test_bad_n_shot_raises(self):
        with pytest.raises(mod.UsageError):
            mod.few_shot_episode(np.zeros((10, 2)), np.array([0] * 5 + [1] * 5), n_shot=0)


class TestClassifyImage:
    def test_map_matches_truth(self):
        cube, truth, _ = mod.generate_synthetic([116, 39, 117, 40], seed=8)
        feats, _, h, w = mod.pixel_features(cube)
        rng = np.random.default_rng(8)
        sup_idx = []
        for c in np.unique(truth):
            idx_c = np.where(truth.ravel() == c)[0]
            sup_idx.extend(rng.permutation(idx_c)[:3].tolist())
        sup_idx = np.array(sup_idx)
        label_map = mod.classify_image(cube, feats[sup_idx], truth.ravel()[sup_idx])
        assert label_map.shape == (h, w)
        assert np.mean(label_map == truth) > 0.95


class TestPseudoSupport:
    def test_support_size(self):
        cube, _, _ = mod.generate_synthetic([116, 39, 117, 40], seed=2)
        feats, _, _, _ = mod.pixel_features(cube)
        sup_idx, sup_labels = mod._pseudo_support(feats, n_classes=3, n_shot=5, seed=2)
        assert sup_idx.size == 15
        assert sup_labels.size == 15


class TestSynthetic:
    def test_shapes(self):
        cube, truth, info = mod.generate_synthetic([116, 39, 117, 40])
        assert cube.shape == (4, 64, 64)
        assert truth.shape == (64, 64)
        assert set(np.unique(truth)) == {0, 1, 2}


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "fs.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
