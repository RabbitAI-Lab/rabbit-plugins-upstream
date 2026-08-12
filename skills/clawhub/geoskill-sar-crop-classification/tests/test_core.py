"""Core algorithm tests for sar-crop-classification."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as scc


class TestTemporalFeatures:
    def test_shape_and_exact_stats(self):
        # t=[0,1,2,3] → mean=1.5, std=sqrt(1.25), amp=3, cv=std/mean, peak=1.0 (idx3)
        t = np.arange(4, dtype=np.float32)
        cube = np.broadcast_to(t[:, None, None], (4, 2, 3)).astype(np.float32).copy()
        feats, names = scc.temporal_features(cube)
        assert feats.shape == (6, 4 + 5)
        assert names[-5:] == ["mean", "std", "amplitude", "cv", "peak_time"]
        row = feats[0]
        np.testing.assert_allclose(row[4], 1.5, atol=1e-5)          # mean
        np.testing.assert_allclose(row[5], np.sqrt(1.25), atol=1e-5)  # std
        np.testing.assert_allclose(row[6], 3.0, atol=1e-5)          # amplitude
        np.testing.assert_allclose(row[7], np.sqrt(1.25) / 1.5, atol=1e-5)  # cv
        np.testing.assert_allclose(row[8], 1.0, atol=1e-5)          # peak_time

    def test_bad_ndim_raises(self):
        with pytest.raises(scc.ValidationError):
            scc.temporal_features(np.ones((4, 4), dtype=np.float32))


class TestConfusion:
    def test_matrix_and_accuracy(self):
        y_true = np.array([0, 0, 1, 1, 2])
        y_pred = np.array([0, 1, 1, 1, 2])
        cm = scc.confusion_matrix(y_true, y_pred, 3)
        assert cm[0, 0] == 1 and cm[0, 1] == 1
        assert cm[1, 1] == 2
        assert cm[2, 2] == 1
        assert scc.overall_accuracy(cm) == pytest.approx(4 / 5)

    def test_empty_accuracy_zero(self):
        cm = np.zeros((3, 3), dtype=np.int64)
        assert scc.overall_accuracy(cm) == 0.0


class TestClassCurves:
    def test_shapes(self):
        curves = scc._class_curves(6)
        assert curves.shape == (3, 6)

    def test_rice_rises(self):
        rice = scc._class_curves(8)[0]
        assert rice[-1] > rice[0] * 3  # 插秧低 → 生长高

    def test_wheat_declines(self):
        wheat = scc._class_curves(8)[1]
        assert wheat[0] > wheat[-1]

    def test_corn_mid_peak(self):
        corn = scc._class_curves(9)[2]
        peak = int(np.argmax(corn))
        assert 2 <= peak <= 6  # 峰值在中段


class TestSynthetic:
    def test_shapes_and_labels(self):
        cube, truth, info = scc.generate_synthetic([116, 39, 117, 40], n_dates=6)
        assert cube.shape == (6, 64, 64)
        assert truth.shape == (64, 64)
        assert set(np.unique(truth).tolist()) == {0, 1, 2}
        assert len(info["truth_class_fractions"]) == 3

    def test_class_separability(self):
        """各类区域均值时序应符合注入曲线特征。"""
        cube, truth, _ = scc.generate_synthetic([116, 39, 117, 40], n_dates=6, seed=3)
        rice_mean = cube[:, truth == 0].mean(axis=1)
        wheat_mean = cube[:, truth == 1].mean(axis=1)
        # 水稻早期低于小麦，晚期高于小麦（曲线交叉）
        assert rice_mean[0] < wheat_mean[0]
        assert rice_mean[-1] > wheat_mean[-1]

    def test_n_dates_too_small_raises(self):
        with pytest.raises(scc.UsageError):
            scc.generate_synthetic([116, 39, 117, 40], n_dates=2)


class TestClassify:
    def test_supervised_accuracy_above_threshold(self):
        cube, truth, _ = scc.generate_synthetic([116, 39, 117, 40], n_dates=6, seed=7)
        feats, _ = scc.temporal_features(cube)
        rng = np.random.default_rng(0)
        train_mask = rng.random(feats.shape[0]) < 0.35
        pred, cm, report = scc.classify_supervised(
            feats, truth.ravel(), train_mask, n_classes=3, n_estimators=40,
        )
        assert pred.shape == (feats.shape[0],)
        assert report["overall_accuracy"] > 0.7
        # 混淆矩阵对角占优
        assert np.trace(cm) > cm.sum() * 0.7

    def test_supervised_bad_split_raises(self):
        feats = np.random.default_rng(1).normal(size=(20, 5)).astype(np.float32)
        labels = np.zeros(20, dtype=np.int64)
        with pytest.raises(scc.ValidationError):
            scc.classify_supervised(feats, labels, np.zeros(20, dtype=bool), 3)

    def test_unsupervised_runs(self):
        cube, truth, _ = scc.generate_synthetic([116, 39, 117, 40], n_dates=6)
        feats, _ = scc.temporal_features(cube)
        pred, cm, report = scc.classify_unsupervised(feats, n_classes=3, n_estimators=30)
        assert pred.shape == (feats.shape[0],)
        assert report["mode"] == "unsupervised_kmeans"
        # RF 自训练对伪标签一致性很高
        assert report["overall_accuracy"] > 0.9


class TestAreaStats:
    def test_fractions_sum_to_one(self):
        labels = np.array([[0, 0, 1], [1, 2, 2]], dtype=np.int64)
        stats = scc.class_area_stats(labels, ["a", "b", "c"], [116.0, 39.0, 117.0, 40.0])
        total_frac = sum(s["fraction"] for s in stats)
        assert total_frac == pytest.approx(1.0)
        assert stats[0]["pixels"] == 2
        assert stats[2]["pixels"] == 2
        assert all(s["area_km2"] >= 0 for s in stats)


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(2).uniform(0, 2, (1, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        scc.write_geotiff(path, cube, bbox)
        back, rbbox = scc.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_read_missing_file_raises(self):
        with pytest.raises(scc.UsageError):
            scc.read_geotiff("/nonexistent/path/file.tif")
