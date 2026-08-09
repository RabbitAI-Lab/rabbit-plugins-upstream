"""Core algorithm tests for ai-accuracy-assessment."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


# 手算基准案例：
# truth = [0,0,1,1,2,2], pred = [0,1,1,1,2,0]
# cm = [[1,1,0],[0,2,0],[1,0,1]]
TRUTH = np.array([0, 0, 1, 1, 2, 2])
PRED = np.array([0, 1, 1, 1, 2, 0])
EXPECTED_CM = np.array([[1, 1, 0], [0, 2, 0], [1, 0, 1]])


class TestConfusionMatrix:
    def test_exact(self):
        cm, labels = mod.confusion_matrix(PRED, TRUTH)
        np.testing.assert_array_equal(cm, EXPECTED_CM)
        np.testing.assert_array_equal(labels, [0, 1, 2])

    def test_subset_labels(self):
        cm, labels = mod.confusion_matrix(np.array([0, 1]), np.array([0, 1]))
        np.testing.assert_array_equal(cm, [[1, 0], [0, 1]])

    def test_size_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.confusion_matrix(np.array([0, 1]), np.array([0]))

    def test_empty_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.confusion_matrix(np.array([]), np.array([]))


class TestOverallAccuracy:
    def test_hand_computed(self):
        oa = mod.overall_accuracy(EXPECTED_CM)
        assert oa == pytest.approx(4.0 / 6.0)

    def test_perfect(self):
        assert mod.overall_accuracy(np.diag([5, 5, 5])) == 1.0

    def test_empty(self):
        assert mod.overall_accuracy(np.zeros((2, 2))) == 0.0


class TestPerClassMetrics:
    def test_hand_computed(self):
        metrics = mod.per_class_metrics(EXPECTED_CM)
        # 类别 0: TP=1, 列和=2, 行和=2 -> P=0.5, R=0.5, F1=0.5
        assert metrics[0]["precision"] == pytest.approx(0.5)
        assert metrics[0]["recall"] == pytest.approx(0.5)
        assert metrics[0]["f1"] == pytest.approx(0.5)
        # 类别 1: TP=2, 列和=3, 行和=2 -> P=2/3, R=1, F1=0.8
        assert metrics[1]["precision"] == pytest.approx(2.0 / 3.0)
        assert metrics[1]["recall"] == pytest.approx(1.0)
        assert metrics[1]["f1"] == pytest.approx(0.8)
        # 类别 2: TP=1, 列和=1, 行和=2 -> P=1, R=0.5, F1=2/3
        assert metrics[2]["precision"] == pytest.approx(1.0)
        assert metrics[2]["recall"] == pytest.approx(0.5)
        assert metrics[2]["f1"] == pytest.approx(2.0 / 3.0)

    def test_zero_column_safe(self):
        cm = np.array([[1, 0], [0, 0]])  # 类别 1 无样本
        metrics = mod.per_class_metrics(cm)
        assert metrics[1]["precision"] == 0.0
        assert metrics[1]["f1"] == 0.0


class TestMeanIoU:
    def test_hand_computed(self):
        # IoU: 1/3, 2/3, 1/2 -> 均值 0.5
        miou, ious = mod.mean_iou(EXPECTED_CM)
        assert ious[0] == pytest.approx(1.0 / 3.0)
        assert ious[1] == pytest.approx(2.0 / 3.0)
        assert ious[2] == pytest.approx(0.5)
        assert miou == pytest.approx(0.5)

    def test_perfect(self):
        miou, _ = mod.mean_iou(np.diag([4, 4]))
        assert miou == 1.0


class TestKappa:
    def test_hand_computed(self):
        # po=2/3, pe=1/3 -> kappa=0.5
        k = mod.cohens_kappa(EXPECTED_CM)
        assert k == pytest.approx(0.5)

    def test_perfect(self):
        assert mod.cohens_kappa(np.diag([10, 10, 10])) == pytest.approx(1.0)


class TestSpatialAccuracyMap:
    def test_perfect_all_ones(self):
        pred = np.zeros((10, 10), dtype=int)
        truth = pred.copy()
        acc = mod.spatial_accuracy_map(pred, truth, window=3)
        np.testing.assert_allclose(acc, 1.0, atol=1e-9)

    def test_localizes_errors(self):
        """注入误差块：块内局部精度低，块外高。"""
        truth = np.zeros((40, 40), dtype=int)
        pred = truth.copy()
        pred[15:25, 15:25] = 1  # 10x10 误差块
        acc = mod.spatial_accuracy_map(pred, truth, window=5)
        assert acc[20, 20] < 0.5     # 块中心精度低
        assert acc[2, 2] > 0.9       # 远离误差块精度高

    def test_window_1_is_pixelwise(self):
        pred = np.array([[0, 1], [1, 1]])
        truth = np.array([[0, 0], [1, 1]])
        acc = mod.spatial_accuracy_map(pred, truth, window=1)
        np.testing.assert_array_equal(acc, [[1, 0], [1, 1]])

    def test_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.spatial_accuracy_map(np.zeros((4, 4)), np.zeros((5, 5)))

    def test_bad_window_raises(self):
        with pytest.raises(mod.UsageError):
            mod.spatial_accuracy_map(np.zeros((4, 4)), np.zeros((4, 4)), window=0)


class TestAssess:
    def test_full_report_keys(self):
        report = mod.assess(PRED, TRUTH, window=3)
        for key in ["confusion_matrix", "overall_accuracy", "mean_iou",
                    "cohens_kappa", "macro_f1", "per_class", "accuracy_map"]:
            assert key in report
        assert report["overall_accuracy"] == pytest.approx(4.0 / 6.0)
        assert report["mean_iou"] == pytest.approx(0.5)
        assert report["accuracy_map"].shape == (6,) or report["accuracy_map"].size == 6

    def test_synthetic_accuracy_near_expected(self):
        pred, truth, _ = mod.generate_synthetic([116, 39, 117, 40], error_frac=0.05, seed=2)
        report = mod.assess(pred, truth)
        # 系统误差块 (32x32 中约 1/3 区域) + 5% 随机误差 -> OA 应明显小于 1
        assert 0.5 < report["overall_accuracy"] < 0.99


class TestSynthetic:
    def test_shapes_and_range(self):
        pred, truth, info = mod.generate_synthetic([116, 39, 117, 40], seed=1)
        assert pred.shape == truth.shape == (64, 64)
        assert set(np.unique(truth)) == {0, 1, 2}
        assert not np.array_equal(pred, truth)  # 有注入误差


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "acc.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
