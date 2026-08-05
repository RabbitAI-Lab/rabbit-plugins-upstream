"""Core algorithm tests for sar-ship-detection."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestCfarAlpha:
    def test_alpha_positive(self):
        a = mod.ca_cfar_alpha(1e-4, 200)
        assert a > 1.0

    def test_roundtrip_pfa(self):
        """α 由 Pfa 推得，反解 (1+α/N)^(−N) 应回到 Pfa。"""
        for pfa in (1e-3, 1e-4, 1e-6):
            n = 150
            a = mod.ca_cfar_alpha(pfa, n)
            pfa_back = (1.0 + a / n) ** (-n)
            assert pfa_back == pytest.approx(pfa, rel=1e-9)

    def test_smaller_pfa_larger_alpha(self):
        assert mod.ca_cfar_alpha(1e-6, 200) > mod.ca_cfar_alpha(1e-3, 200)

    def test_invalid_pfa(self):
        with pytest.raises(mod.ValidationError):
            mod.ca_cfar_alpha(1.5, 100)

    def test_invalid_n(self):
        with pytest.raises(mod.ValidationError):
            mod.ca_cfar_alpha(1e-4, 0)


class TestCfarDetect:
    def _scene(self, val=1.0, size=40):
        img = np.full((size, size), val, dtype=np.float32)
        return img

    def test_constant_no_detection(self):
        img = self._scene()
        res = mod.cfar_detect(img, guard=2, background=5, pfa=1e-4, method="ca")
        assert res["detections"].sum() == 0

    def test_bright_point_detected(self):
        img = self._scene()
        img[20, 20] = 100.0
        res = mod.cfar_detect(img, guard=2, background=5, pfa=1e-4, method="ca")
        assert res["detections"][20, 20]
        # 背景像元不应被误检
        assert res["detections"].sum() == 1

    def test_os_detects_bright_point(self):
        img = self._scene()
        img[20, 20] = 100.0
        res = mod.cfar_detect(img, guard=2, background=5, pfa=1e-4, method="os")
        assert res["detections"][20, 20]

    def test_margin_not_detected(self):
        img = self._scene()
        img[0, 0] = 1000.0  # 角点在边界 margin 内，不参与检测
        res = mod.cfar_detect(img, guard=2, background=5, pfa=1e-4, method="ca")
        assert not res["detections"][0, 0]

    def test_image_too_small(self):
        img = np.ones((10, 10), dtype=np.float32)
        with pytest.raises(mod.ValidationError):
            mod.cfar_detect(img, guard=2, background=5)

    def test_bad_method(self):
        img = self._scene()
        with pytest.raises(mod.UsageError):
            mod.cfar_detect(img, method="xx")

    def test_threshold_shape(self):
        img = self._scene()
        res = mod.cfar_detect(img, guard=2, background=5)
        assert res["threshold"].shape == img.shape
        assert res["noise_estimate"].shape == img.shape


class TestCluster:
    def test_two_clusters(self):
        det = np.zeros((40, 40), dtype=bool)
        det[10:12, 10:12] = True
        det[30:33, 30:33] = True
        img = np.ones((40, 40), dtype=np.float32)
        img[10, 10] = 50.0
        img[31, 31] = 80.0
        targets = mod.cluster_detections(det, img)
        assert len(targets) == 2
        # 按峰值降序：31,31 那个（80）排第一
        assert targets[0]["peak_intensity"] == 80.0
        assert targets[0]["rank"] == 0

    def test_min_area_filter(self):
        det = np.zeros((30, 30), dtype=bool)
        det[5, 5] = True          # area 1
        det[20:23, 20:23] = True  # area 9
        img = np.ones((30, 30), dtype=np.float32)
        targets = mod.cluster_detections(det, img, min_area=4)
        assert len(targets) == 1
        assert targets[0]["area_px"] == 9

    def test_centroid_and_bbox(self):
        det = np.zeros((20, 20), dtype=bool)
        det[8:12, 8:12] = True
        img = np.ones((20, 20), dtype=np.float32)
        t = mod.cluster_detections(det, img)[0]
        assert t["area_px"] == 16
        assert t["centroid_row"] == pytest.approx(9.5)
        assert t["centroid_col"] == pytest.approx(9.5)
        assert t["bbox_px"] == [8, 8, 11, 11]

    def test_bad_shape(self):
        with pytest.raises(mod.ValidationError):
            mod.cluster_detections(np.zeros((4, 4, 4), dtype=bool), np.zeros((4, 4)))


class TestPixelToLonlat:
    def test_center_of_topleft_pixel(self):
        bbox = [120.0, 30.0, 121.0, 31.0]  # W,S,E,N
        lon, lat = mod.pixel_to_lonlat(0, 0, bbox, h=100, w=100)
        assert lon == pytest.approx(120.005)
        assert lat == pytest.approx(30.995)

    def test_bottom_right(self):
        bbox = [120.0, 30.0, 121.0, 31.0]
        lon, lat = mod.pixel_to_lonlat(99, 99, bbox, h=100, w=100)
        assert lon == pytest.approx(120.995)
        assert lat == pytest.approx(30.005)


class TestSynthetic:
    def test_shape_and_truth(self):
        img, info = mod.generate_synthetic([121, 30, 122, 31], width=64, height=64,
                                           n_ships=4, seed=7)
        assert img.shape == (64, 64)
        assert info["n_ships_injected"] == len(info["ships_truth_px"])
        assert info["n_ships_injected"] <= 4

    def test_detection_recovers_ships(self):
        """合成场景：CFAR 检测到的目标数应接近注入船数。"""
        bbox = [121, 30, 122, 31]
        img, info = mod.generate_synthetic(bbox, width=96, height=96, n_ships=6,
                                           seed=3)
        res = mod.cfar_detect(img, guard=2, background=5, pfa=1e-4, method="ca")
        targets = mod.cluster_detections(res["detections"], img)
        injected = info["n_ships_injected"]
        assert injected >= 4
        assert abs(len(targets) - injected) <= 2

    def test_detection_locations_match_truth(self):
        """每个注入船附近都应有一个检测目标。"""
        bbox = [121, 30, 122, 31]
        img, info = mod.generate_synthetic(bbox, width=96, height=96, n_ships=5,
                                           ship_contrast=80.0, seed=11)
        res = mod.cfar_detect(img, guard=2, background=5, pfa=1e-4, method="ca")
        targets = mod.cluster_detections(res["detections"], img)
        matched = 0
        for truth in info["ships_truth_px"]:
            for t in targets:
                if (abs(t["centroid_row"] - truth["row"]) < 3
                        and abs(t["centroid_col"] - truth["col"]) < 3):
                    matched += 1
                    break
        assert matched == info["n_ships_injected"]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [121.0, 30.0, 122.0, 31.0]
        path = str(tmp_path / "x.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == arr.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, arr, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/no.tif")
