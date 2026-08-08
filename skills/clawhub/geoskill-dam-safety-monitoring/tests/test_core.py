"""Core algorithm tests for dam-safety-monitoring."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as dm


class TestNormalize:
    def test_range_01(self):
        arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        out = dm.normalize_minmax(arr)
        assert out.min() == pytest.approx(0.0)
        assert out.max() == pytest.approx(1.0)

    def test_constant_array_returns_zero(self):
        arr = np.full((5, 5), 3.0)
        out = dm.normalize_minmax(arr)
        assert np.allclose(out, 0.0)


class TestAnomalyMagnitude:
    def test_center_is_zero_anomaly(self):
        arr = np.full((10, 10), 5.0)
        arr[5, 5] = 100.0  # 一个离群高值
        anom = dm.anomaly_magnitude(arr)
        assert anom[5, 5] == anom.max()
        assert anom[0, 0] < anom[5, 5]


class TestCompositeRisk:
    def test_high_deformation_higher_risk(self):
        n = 32
        deformation = np.zeros((n, n))
        deformation[10:20, 10:20] = -50.0  # 强沉降块
        ndvi = np.full((n, n), 0.4)
        thermal = np.full((n, n), 25.0)
        water = np.zeros((n, n))
        risk = dm.composite_risk(deformation, ndvi, thermal, water)
        block = risk[10:20, 10:20].mean()
        corner = risk[0:5, 0:5].mean()
        assert block > corner
        assert risk.max() <= 1.0 and risk.min() >= 0.0

    def test_zero_weights_raises(self):
        z = np.zeros((4, 4))
        with pytest.raises(dm.UsageError):
            dm.composite_risk(z, z, z, z,
                              weights={"deformation": 0, "ndvi_anomaly": 0,
                                       "thermal_anomaly": 0, "water_change": 0})


class TestClassify:
    def test_levels(self):
        risk = np.array([[0.1, 0.4], [0.7, 0.9]])
        cls = dm.classify_risk(risk)
        assert cls[0, 0] == 0  # low
        assert cls[0, 1] == 1  # medium
        assert cls[1, 0] == 2  # high
        assert cls[1, 1] == 2


class TestDetectAnomalies:
    def test_two_blobs(self):
        risk = np.zeros((40, 40))
        risk[5:12, 5:12] = 0.8
        risk[25:33, 25:33] = 0.9
        labels, n = dm.detect_anomalies(risk, threshold=0.5)
        assert n == 2


class TestPolygonize:
    def test_returns_features_with_props(self):
        risk = np.zeros((40, 40))
        risk[10:20, 10:20] = 0.85
        bbox = [116.0, 39.0, 117.0, 40.0]
        feats = dm.polygonize_anomalies(risk, threshold=0.5, bbox=bbox)
        assert len(feats) >= 1
        f = feats[0]
        assert f["type"] == "Feature"
        assert f["geometry"]["type"] in ("Polygon", "MultiPolygon")
        assert "risk_mean" in f["properties"]
        assert f["properties"]["risk_max"] >= 0.5


class TestEndToEndSynthetic:
    def test_injected_anomaly_detected(self):
        """注入的沉降/渗流异常区应被识别，且最高风险位置落在注入区附近。"""
        bbox = [116.0, 39.0, 117.0, 40.0]
        layers, info = dm.generate_synthetic(bbox, width=64, height=64, seed=7)
        risk, cls, feats, summary = dm.run_model(
            layers["deformation"], layers["ndvi"], layers["thermal"],
            layers["water_change"], bbox, threshold=0.5,
        )
        assert summary["n_anomaly_polygons"] >= 1
        # 最高风险像元应落在注入区附近
        truth = info["truth"]
        h, w = risk.shape
        r_idx, c_idx = np.unravel_index(np.argmax(risk), risk.shape)
        xn = c_idx / w
        yn = r_idx / h
        dist = np.hypot(xn - truth["cx"], yn - truth["cy"])
        assert dist < truth["r"] + 0.05
        # 高风险占比应较小（异常是局部的）但非零
        assert 0.0 < summary["level_fraction"]["high"] < 0.5

    def test_no_anomaly_baseline_low_risk(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        layers, info = dm.generate_synthetic(bbox, width=48, height=48,
                                             seed=3, inject_anomaly=False)
        assert info["truth"] is None
        risk, cls, feats, summary = dm.run_model(
            layers["deformation"], layers["ndvi"], layers["thermal"],
            layers["water_change"], bbox, threshold=0.5,
        )
        # 无注入异常时高风险占比应很低
        assert summary["level_fraction"]["high"] < 0.05


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(-30, 30, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "d.tif")
        dm.write_geotiff(path, arr, bbox)
        back, rbbox = dm.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-4)

    def test_read_missing_raises(self):
        with pytest.raises(dm.UsageError):
            dm.read_geotiff("/nonexistent/x.tif")
