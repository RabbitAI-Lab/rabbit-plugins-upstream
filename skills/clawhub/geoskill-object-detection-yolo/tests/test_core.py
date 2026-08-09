"""Core algorithm tests for object-detection-yolo."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestIoU:
    def test_identical_boxes(self):
        b = [0, 0, 10, 10]
        assert abs(mod.iou(b, b) - 1.0) < 1e-9

    def test_disjoint_boxes(self):
        assert mod.iou([0, 0, 5, 5], [10, 10, 20, 20]) == 0.0

    def test_partial_overlap(self):
        # intersection 5x5=25, union 100+100-25=175
        v = mod.iou([0, 0, 10, 10], [5, 5, 15, 15])
        assert abs(v - 25.0 / 175.0) < 1e-9

    def test_zero_area_box(self):
        assert mod.iou([0, 0, 0, 0], [0, 0, 10, 10]) == 0.0


class TestNMS:
    def test_removes_overlapping_lower_score(self):
        boxes = np.array([
            [0, 0, 10, 10],
            [1, 1, 11, 11],   # 与框0高度重叠
            [50, 50, 60, 60],  # 独立目标
        ], dtype=np.float64)
        scores = np.array([0.9, 0.8, 0.7])
        keep = mod.nms(boxes, scores, iou_thresh=0.5)
        kept = set(int(i) for i in keep)
        assert 0 in kept            # 最高分保留
        assert 1 not in kept        # 重叠低分被抑制
        assert 2 in kept            # 独立目标保留
        assert len(keep) == 2

    def test_keeps_all_when_no_overlap(self):
        boxes = np.array([[0, 0, 5, 5], [20, 20, 25, 25], [40, 40, 45, 45]], dtype=np.float64)
        scores = np.array([0.5, 0.6, 0.7])
        keep = mod.nms(boxes, scores, iou_thresh=0.5)
        assert len(keep) == 3

    def test_empty_input(self):
        keep = mod.nms(np.empty((0, 4)), np.empty((0,)), iou_thresh=0.5)
        assert keep.size == 0

    def test_sorted_by_score_desc(self):
        boxes = np.array([[0, 0, 5, 5], [60, 60, 65, 65]], dtype=np.float64)
        scores = np.array([0.3, 0.9])
        keep = mod.nms(boxes, scores, iou_thresh=0.5)
        assert int(keep[0]) == 1  # 0.9 排第一


class TestWindowScore:
    def test_bright_patch_high_zscore(self):
        patch = np.full((8, 8), 100.0)
        s = mod.window_score(patch, global_mean=20.0, global_std=10.0)
        assert abs(s - 8.0) < 1e-9

    def test_hog_energy_zero_on_flat(self):
        flat = np.full((16, 16), 50.0)
        assert mod.hog_energy(flat) < 1e-6

    def test_hog_energy_high_on_edges(self):
        patch = np.zeros((16, 16))
        patch[:, 8:] = 100.0  # 竖直边缘
        assert mod.hog_energy(patch) > 10.0


class TestSlidingWindow:
    def test_detects_bright_target(self):
        img = np.zeros((64, 64))
        img[20:36, 20:36] = 100.0  # 一个明亮方块
        boxes, scores = mod.sliding_window_detect(
            img, win_size=16, step=4, score_thresh=1.5
        )
        assert len(boxes) > 0
        # 至少有一个候选框覆盖目标中心 (28,28)
        covered = any(
            b[0] <= 28 <= b[2] and b[1] <= 28 <= b[3] for b in boxes
        )
        assert covered

    def test_no_detection_on_flat(self):
        img = np.full((64, 64), 50.0)
        boxes, scores = mod.sliding_window_detect(
            img, win_size=16, step=4, score_thresh=1.5
        )
        assert len(boxes) == 0

    def test_window_too_large_raises(self):
        img = np.zeros((8, 8))
        with pytest.raises(mod.ValidationError):
            mod.sliding_window_detect(img, win_size=16, step=4)

    def test_rejects_3d(self):
        with pytest.raises(mod.ValidationError):
            mod.sliding_window_detect(np.zeros((3, 8, 8)))


class TestDetectPipeline:
    def test_nms_reduces_candidates(self):
        img = np.zeros((64, 64))
        img[20:36, 20:36] = 100.0
        raw_boxes, _ = mod.sliding_window_detect(img, win_size=16, step=4, score_thresh=1.5)
        boxes, scores = mod.detect_objects(
            img, win_size=16, step=4, score_thresh=1.5, iou_thresh=0.5
        )
        assert len(boxes) <= len(raw_boxes)
        assert len(boxes) >= 1


class TestGeocoding:
    def test_pixel_box_to_geo_corners(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        # 整幅影像框 -> 应还原为整个 bbox
        full = mod.pixel_box_to_geo([0, 0, 100, 100], bbox, 100, 100)
        np.testing.assert_allclose(full, [116.0, 39.0, 117.0, 40.0], atol=1e-9)

    def test_pixel_box_to_geo_subwindow(self):
        bbox = [0.0, 0.0, 10.0, 10.0]
        g = mod.pixel_box_to_geo([0, 0, 50, 50], bbox, 100, 100)
        np.testing.assert_allclose(g, [0.0, 5.0, 5.0, 10.0], atol=1e-9)

    def test_geojson_structure(self):
        boxes = np.array([[0, 0, 10, 10]], dtype=np.float64)
        scores = np.array([0.95])
        gj = mod.boxes_to_geojson(boxes, scores, [116, 39, 117, 40], 100, 100)
        assert gj["type"] == "FeatureCollection"
        assert len(gj["features"]) == 1
        feat = gj["features"][0]
        assert feat["geometry"]["type"] == "Polygon"
        assert feat["properties"]["score"] == pytest.approx(0.95)
        ring = feat["geometry"]["coordinates"][0]
        assert ring[0] == ring[-1]  # 闭合环


class TestSynthetic:
    def test_synthetic_shape_and_targets(self):
        img, info = mod.generate_synthetic([116, 39, 117, 40], n_targets=4)
        assert img.shape == (128, 128)
        assert info["n_targets"] == 4
        assert len(info["truth_boxes"]) == 4

    def test_detect_finds_synthetic_targets(self):
        bbox = [116, 39, 117, 40]
        img, info = mod.generate_synthetic(bbox, n_targets=4, seed=1)
        boxes, scores = mod.detect_objects(
            img, win_size=16, step=4, score_thresh=2.0, iou_thresh=0.4
        )
        # 4 个目标至少检出 3 个（允许个别边界漏检）
        assert len(boxes) >= 3


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        assert os.path.exists(path)
        back, rb = mod.read_geotiff(path)
        assert back.shape == (1, 16, 16)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
