"""Core algorithm tests for urban-drainage-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ud


class TestSlopeAndFlow:
    def test_flat_zero_slope(self):
        dem = np.full((24, 24), 10.0)
        assert np.allclose(ud.compute_slope_rad(dem, 5.0), 0.0, atol=1e-6)

    def test_flow_converges_to_low(self):
        # 漏斗：中心最低 → 中心汇流最大
        yy, xx = np.mgrid[0:24, 0:24]
        dem = ((xx - 11.5) ** 2 + (yy - 11.5) ** 2).astype(float)
        acc, down = ud.d8_flow_accumulation(dem, 1.0)
        assert acc[11:13, 11:13].sum() > 0.8 * acc.size


class TestTWI:
    def test_flat_high_acc_highest_twi(self):
        # 平坦（tanβ 小）+ 高汇流 → TWI 高
        acc = np.array([[1.0, 100.0]])
        slope = np.array([[np.deg2rad(20.0), np.deg2rad(1.0)]])
        twi = ud.topographic_wetness_index(acc, slope, cellsize=10.0)
        assert twi[0, 1] > twi[0, 0]


class TestRunoffCoefficient:
    def test_endpoints(self):
        C = ud.runoff_coefficient(np.array([0.0, 1.0]))
        assert C[0] == pytest.approx(0.15)
        assert C[1] == pytest.approx(0.90)

    def test_monotonic(self):
        isa = np.linspace(0, 1, 11)
        C = ud.runoff_coefficient(isa)
        assert np.all(np.diff(C) > 0)


class TestWaterloggingRisk:
    def test_low_flat_impervious_is_high_risk(self):
        n = 16
        twi = np.zeros((n, n)); twi[5:10, 5:10] = 12.0   # 高 TWI 块
        acc = np.ones((n, n)); acc[5:10, 5:10] = 200.0     # 高汇流
        isa = np.full((n, n), 0.1); isa[5:10, 5:10] = 0.9  # 高不透水
        risk = ud.waterlogging_risk(twi, acc, isa)
        block = risk[5:10, 5:10].mean()
        edge = risk[0:3, 0:3].mean()
        assert block > edge
        assert risk.max() <= 1.0


class TestClassify:
    def test_levels(self):
        risk = np.array([[0.2, 0.5], [0.8, 0.95]])
        cls = ud.classify_risk(risk)
        assert cls[0, 0] == 0
        assert cls[0, 1] == 1
        assert cls[1, 0] == 2


class TestDepth:
    def test_bounded_by_rainfall(self):
        C = np.full((10, 10), 0.9)
        acc = np.linspace(1, 500, 100).reshape(10, 10)
        depth = ud.waterlogging_depth_mm(50.0, C, acc)
        assert depth.max() <= 50.0
        assert depth.min() >= 0.0
        # 高汇流处深度更大
        assert depth.ravel()[-1] > depth.ravel()[0]


class TestFlowPaths:
    def test_paths_are_linestrings(self):
        yy, xx = np.mgrid[0:32, 0:32]
        dem = (xx + yy).astype(float)  # 向一角倾斜
        acc, down = ud.d8_flow_accumulation(dem, 1.0)
        bbox = [116.0, 39.0, 117.0, 40.0]
        paths = ud.trace_flow_paths(down, acc, bbox, n_paths=3)
        assert len(paths) >= 1
        for f in paths:
            assert f["geometry"]["type"] == "LineString"
            assert len(f["geometry"]["coordinates"]) >= 2


class TestEndToEndSynthetic:
    def test_depression_flagged_high_risk(self):
        """低洼 + 高汇流 + 高 ISA 的盆地应被识别为高风险，最高风险落在盆地附近。"""
        bbox = [116.0, 39.0, 117.0, 40.0]
        layers, info = ud.generate_synthetic(bbox, width=64, height=64, seed=5)
        risk, cls, depth, paths, summary = ud.run_model(
            layers["dem"], layers["isa"], info["cellsize_m"], bbox, rainfall_mm=50.0,
        )
        truth = info["truth"]
        h, w = risk.shape
        r_idx, c_idx = np.unravel_index(np.argmax(risk), risk.shape)
        xn, yn = c_idx / w, r_idx / h
        dist = np.hypot(xn - truth["cx"], yn - truth["cy"])
        assert dist < truth["r"] + 0.08
        assert summary["high_risk_fraction"] > 0.0
        assert summary["depth_max_mm"] > 0
        assert summary["n_flow_paths"] >= 1

    def test_no_depression_runs(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        layers, info = ud.generate_synthetic(bbox, width=48, height=48,
                                             seed=2, inject_depression=False)
        assert info["truth"] is None
        risk, cls, depth, paths, summary = ud.run_model(
            layers["dem"], layers["isa"], info["cellsize_m"], bbox, rainfall_mm=30.0,
        )
        assert 0.0 <= risk.min() and risk.max() <= 1.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "r.tif")
        ud.write_geotiff(path, arr, bbox)
        back, rbbox, cs = ud.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-4)
        assert cs > 0

    def test_read_missing_raises(self):
        with pytest.raises(ud.UsageError):
            ud.read_geotiff("/nonexistent/x.tif")
