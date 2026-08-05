"""Core algorithm tests for instance-segmentation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestOtsu:
    def test_bimodal_threshold_between_modes(self):
        rng = np.random.default_rng(0)
        bg = rng.normal(10, 1, 5000)
        fg = rng.normal(100, 1, 5000)
        t = mod.otsu_threshold(np.concatenate([bg, fg]))
        assert 30 < t < 80

    def test_empty_returns_zero(self):
        assert mod.otsu_threshold(np.array([np.nan, np.nan])) == 0.0


class TestThresholdSegment:
    def test_explicit_threshold(self):
        img = np.array([[1, 2], [8, 9]], dtype=np.float64)
        mask = mod.threshold_segment(img, thresh=5.0)
        np.testing.assert_array_equal(mask, [[False, False], [True, True]])

    def test_auto_threshold(self):
        img = np.zeros((20, 20))
        img[:10] = 0.0
        img[10:] = 100.0
        mask = mod.threshold_segment(img)  # Otsu
        assert mask[0, 0] == False
        assert mask[15, 0] == True

    def test_rejects_3d(self):
        with pytest.raises(mod.ValidationError):
            mod.threshold_segment(np.zeros((2, 4, 4)))


class TestLabelInstances:
    def test_two_separate_blobs(self):
        mask = np.zeros((10, 10), dtype=bool)
        mask[1:3, 1:3] = True
        mask[6:9, 6:9] = True
        labels, n = mod.label_instances(mask, connectivity=8)
        assert n == 2
        assert labels[1, 1] != labels[7, 7]
        assert labels[0, 0] == 0

    def test_connectivity_4_vs_8_diagonal(self):
        """对角相邻的两个像元：8-连通算一个实例，4-连通算两个。"""
        mask = np.zeros((4, 4), dtype=bool)
        mask[0, 0] = True
        mask[1, 1] = True  # 与 (0,0) 对角相邻
        _, n8 = mod.label_instances(mask, connectivity=8)
        _, n4 = mod.label_instances(mask, connectivity=4)
        assert n8 == 1
        assert n4 == 2

    def test_bad_connectivity_raises(self):
        with pytest.raises(mod.UsageError):
            mod.label_instances(np.zeros((3, 3), dtype=bool), connectivity=6)


class TestInstanceProperties:
    def test_area_and_centroid(self):
        label_map = np.zeros((10, 10), dtype=np.int32)
        label_map[2:5, 3:7] = 1  # 3 行 x 4 列 = 12 像元
        image = np.ones((10, 10)) * 5.0
        props = mod.instance_properties(label_map, image)
        assert len(props) == 1
        p = props[0]
        assert p["area_px"] == 12
        assert abs(p["centroid_row"] - 3.0) < 1e-9   # (2+3+4)/3
        assert abs(p["centroid_col"] - 4.5) < 1e-9   # (3+4+5+6)/4
        assert p["bbox_px"] == [3, 2, 7, 5]
        assert p["mean_intensity"] == pytest.approx(5.0)

    def test_min_area_filter(self):
        label_map = np.zeros((10, 10), dtype=np.int32)
        label_map[0, 0] = 1          # 面积 1
        label_map[5:8, 5:8] = 2      # 面积 9
        props = mod.instance_properties(label_map, np.ones((10, 10)), min_area=5)
        assert len(props) == 1
        assert props[0]["area_px"] == 9

    def test_sorted_by_area_desc(self):
        label_map = np.zeros((12, 12), dtype=np.int32)
        label_map[0:2, 0:2] = 1      # 4
        label_map[4:9, 4:9] = 2      # 25
        props = mod.instance_properties(label_map, np.ones((12, 12)))
        assert props[0]["area_px"] == 25
        assert props[1]["area_px"] == 4


class TestSegmentPipeline:
    def test_counts_blobs(self):
        img = np.zeros((60, 60))
        img[5:15, 5:15] = 100.0
        img[40:50, 40:50] = 100.0
        label_map, props, info = mod.segment_instances(img, thresh=50.0)
        assert info["n_instances"] == 2
        assert label_map.max() == 2

    def test_relabels_sequentially(self):
        img = np.zeros((40, 40))
        img[2:5, 2:5] = 100.0      # 小实例
        img[20:35, 20:35] = 100.0  # 大实例
        label_map, props, info = mod.segment_instances(img, thresh=50.0)
        ids = sorted(p["instance_id"] for p in props)
        assert ids == [1, 2]  # 连续编号


class TestGeocoding:
    def test_geojson_features(self):
        img = np.zeros((100, 100))
        img[10:20, 10:20] = 100.0
        _, props, _ = mod.segment_instances(img, thresh=50.0)
        gj = mod.instances_to_geojson(props, [116, 39, 117, 40], 100, 100)
        assert gj["type"] == "FeatureCollection"
        assert len(gj["features"]) == 1
        feat = gj["features"][0]
        assert feat["properties"]["area_px"] == 100
        ring = feat["geometry"]["coordinates"][0]
        assert ring[0] == ring[-1]


class TestSynthetic:
    def test_synthetic_finds_all_blobs(self):
        img, info = mod.generate_synthetic([116, 39, 117, 40], n_blobs=5, seed=3)
        _, props, seg_info = mod.segment_instances(img, connectivity=8, min_area=3)
        assert seg_info["n_instances"] == 5
        assert len(info["truth_centers"]) == 5


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.arange(256, dtype=np.float32).reshape(16, 16)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "lab.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-3)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
