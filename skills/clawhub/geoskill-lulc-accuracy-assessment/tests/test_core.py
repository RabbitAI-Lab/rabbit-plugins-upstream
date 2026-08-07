"""Core algorithm tests for lulc-accuracy-assessment."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as acc


# 一个已知混淆矩阵（行=参考，列=预测）
KNOWN_CM = np.array([
    [50, 5, 0],
    [3, 40, 2],
    [0, 4, 46],
], dtype=np.int64)
LABELS = [1, 2, 3]


def _expand(cm, labels):
    """把混淆矩阵展开成 (reference, predicted) 样本对。"""
    ref, pred = [], []
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ref += [labels[i]] * int(cm[i, j])
            pred += [labels[j]] * int(cm[i, j])
    return np.array(ref), np.array(pred)


class TestConfusionMatrix:
    def test_builds_known_matrix(self):
        ref, pred = _expand(KNOWN_CM, LABELS)
        cm = acc.build_confusion_matrix(ref, pred, LABELS)
        np.testing.assert_array_equal(cm, KNOWN_CM)

    def test_length_mismatch_raises(self):
        with pytest.raises(acc.ValidationError):
            acc.build_confusion_matrix(np.array([1, 2]), np.array([1]), [1, 2])

    def test_unknown_labels_ignored(self):
        ref = np.array([1, 2, 99])
        pred = np.array([1, 2, 1])
        cm = acc.build_confusion_matrix(ref, pred, [1, 2])
        assert cm.sum() == 2  # 99 不在 labels，被忽略


class TestOverallAccuracy:
    def test_known_value(self):
        oa = acc.overall_accuracy(KNOWN_CM)
        np.testing.assert_allclose(oa, 136.0 / 150.0, atol=1e-9)

    def test_perfect(self):
        assert acc.overall_accuracy(np.eye(3, dtype=int)) == 1.0

    def test_empty(self):
        assert acc.overall_accuracy(np.zeros((2, 2), dtype=int)) == 0.0


class TestKappa:
    def test_known_value(self):
        # 手工计算：pe = (55*53 + 45*49 + 50*48) / 150^2
        po = 136.0 / 150.0
        pe = (55 * 53 + 45 * 49 + 50 * 48) / (150.0 ** 2)
        expected = (po - pe) / (1 - pe)
        np.testing.assert_allclose(acc.kappa_coefficient(KNOWN_CM), expected, atol=1e-9)

    def test_matches_sklearn(self):
        from sklearn.metrics import cohen_kappa_score
        ref, pred = _expand(KNOWN_CM, LABELS)
        expected = cohen_kappa_score(ref, pred)
        np.testing.assert_allclose(acc.kappa_coefficient(KNOWN_CM), expected, atol=1e-9)

    def test_perfect_agreement_kappa_1(self):
        cm = np.diag([10, 20, 30])
        assert abs(acc.kappa_coefficient(cm) - 1.0) < 1e-9


class TestProducerUser:
    def test_producers_accuracy(self):
        pa = acc.producers_accuracy(KNOWN_CM)
        np.testing.assert_allclose(pa, [50 / 55, 40 / 45, 46 / 50], atol=1e-9)

    def test_users_accuracy(self):
        ua = acc.users_accuracy(KNOWN_CM)
        np.testing.assert_allclose(ua, [50 / 53, 40 / 49, 46 / 48], atol=1e-9)

    def test_zero_row_no_nan(self):
        cm = np.array([[0, 0], [0, 5]], dtype=np.int64)
        pa = acc.producers_accuracy(cm)
        assert np.all(np.isfinite(pa))
        assert pa[0] == 0.0


class TestF1:
    def test_f1_formula(self):
        pa = np.array([0.9, 0.5])
        ua = np.array([0.8, 0.5])
        f1 = acc.f1_scores(pa, ua)
        np.testing.assert_allclose(f1[0], 2 * 0.9 * 0.8 / 1.7, atol=1e-9)
        np.testing.assert_allclose(f1[1], 0.5, atol=1e-9)

    def test_f1_zero_div(self):
        f1 = acc.f1_scores(np.array([0.0]), np.array([0.0]))
        assert f1[0] == 0.0


class TestAccuracyMetrics:
    def test_full_structure(self):
        m = acc.accuracy_metrics(KNOWN_CM, LABELS)
        assert "overall_accuracy" in m
        assert "kappa" in m
        assert len(m["per_class"]) == 3
        assert m["total_samples"] == 150


class TestStratifiedSample:
    def test_all_classes_represented(self):
        truth = np.zeros((20, 20), dtype=np.int64)
        truth[:10, :] = 1
        truth[10:, :] = 2
        rng = np.random.default_rng(0)
        rows, cols, labs = acc.stratified_sample(truth, 40, rng)
        assert set(labs.tolist()) == {1, 2}
        # 标签与真值一致
        assert np.all(truth[rows, cols] == labs)

    def test_empty_raises(self):
        rng = np.random.default_rng(0)
        with pytest.raises(acc.ValidationError):
            acc.stratified_sample(np.zeros((0, 0), dtype=np.int64), 10, rng)


class TestSynthetic:
    def test_oa_near_one_minus_error(self):
        synth = acc.generate_synthetic([116, 39, 117, 40], n_points=400,
                                       error_rate=0.18, seed=3)
        labels = sorted(set(np.unique(synth["reference"]).tolist()) |
                        set(np.unique(synth["predicted"]).tolist()))
        cm = acc.build_confusion_matrix(synth["reference"], synth["predicted"], labels)
        oa = acc.overall_accuracy(cm)
        assert 0.7 < oa < 0.95
        assert acc.kappa_coefficient(cm) > 0.3

    def test_n_points_respected(self):
        synth = acc.generate_synthetic([116, 39, 117, 40], n_points=100, seed=1)
        assert synth["reference"].size > 0
        assert synth["reference"].size <= 100 + 5  # 每类至少 1 个，可能略超


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 5, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        acc.write_geotiff(path, arr, bbox)
        back, rb = acc.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(acc.UsageError):
            acc.read_geotiff("/no/such/file.tif")
