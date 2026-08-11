"""Core algorithm tests for land-degradation-assessment."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ld


class TestSensSlope:
    def test_linear_ramp_recovers_slope(self):
        times = np.arange(6, dtype=float)
        # 斜率为 2.0 的线性序列
        series = np.zeros((6, 4, 4))
        for t in range(6):
            series[t] = 2.0 * t
        slope = ld.sens_slope(series, times)
        np.testing.assert_allclose(slope, 2.0, atol=1e-9)

    def test_decreasing_negative(self):
        times = np.arange(5, dtype=float)
        series = np.zeros((5, 3, 3))
        for t in range(5):
            series[t] = 1.0 - 0.05 * t
        slope = ld.sens_slope(series, times)
        assert np.all(slope < 0)
        np.testing.assert_allclose(slope, -0.05, atol=1e-9)

    def test_outlier_robust(self):
        """Sen's slope 用中位数，单个离群值不应主导结果。"""
        times = np.arange(6, dtype=float)
        series = np.zeros((6, 1, 1))
        for t in range(6):
            series[t, 0, 0] = 1.0 * t
        series[3, 0, 0] = 1000.0  # 注入离群
        slope = ld.sens_slope(series, times)[0, 0]
        assert 0.5 < slope < 1.5  # 仍接近真实斜率 1.0

    def test_too_few_dates_raises(self):
        with pytest.raises(ld.ValidationError):
            ld.sens_slope(np.zeros((1, 4, 4)), np.arange(1))

    def test_shape_mismatch_raises(self):
        with pytest.raises(ld.ValidationError):
            ld.sens_slope(np.zeros((5, 4, 4)), np.arange(6))


class TestClassifyIndicator:
    def test_thresholds(self):
        val = np.array([-0.2, -0.01, 0.0, 0.01, 0.3])
        out = ld.classify_indicator(val, degrade_thresh=-0.05, improve_thresh=0.05)
        assert list(out) == [-1, 0, 0, 0, 1]


class TestTransitionMatrix:
    def test_counts(self):
        l1 = np.array([[1, 1], [2, 2]])
        l2 = np.array([[1, 2], [2, 2]])
        mat = ld.transition_matrix(l1, l2, n_classes=3)
        assert mat[1, 1] == 1   # 1->1
        assert mat[1, 2] == 1   # 1->2
        assert mat[2, 2] == 2   # 2->2
        assert mat.sum() == 4

    def test_shape_mismatch_raises(self):
        with pytest.raises(ld.ValidationError):
            ld.transition_matrix(np.zeros((2, 2)), np.zeros((3, 3)), 3)

    def test_negative_code_raises(self):
        with pytest.raises(ld.ValidationError):
            ld.transition_matrix(np.array([[-1, 0]]), np.array([[0, 0]]), 2)


class TestCombine:
    def test_any_degraded_wins(self):
        prod = np.array([0, 0, 0])
        cover = np.array([-1, 0, 1])
        combined = ld.combine_sdg(prod, cover, None)
        assert combined[0] == -1
        assert combined[1] == 0
        assert combined[2] == 1

    def test_degraded_beats_improved(self):
        prod = np.array([-1])
        cover = np.array([1])
        combined = ld.combine_sdg(prod, cover, None)
        assert combined[0] == -1

    def test_optional_carbon_skipped(self):
        prod = np.array([0, 1])
        combined = ld.combine_sdg(prod, None, None)
        assert combined[0] == 0
        assert combined[1] == 1


class TestSOC:
    def test_relative_change(self):
        s1 = np.array([10.0, 5.0, 0.0])
        s2 = np.array([7.0, 6.25, 1.0])
        rel = ld.soc_relative_change(s1, s2)
        np.testing.assert_allclose(rel[0], -0.3)
        np.testing.assert_allclose(rel[1], 0.25)
        assert rel[2] == 0.0  # s1=0 → 记 0


class TestSyntheticDetection:
    def test_degradation_matches_injected(self):
        """合成场景里评估出的退化区应与注入真值高度一致。"""
        synth = ld.generate_synthetic([116, 39, 117, 40], n_dates=6, seed=7)
        res = ld.assess_degradation(
            synth["ndvi"], synth["times"],
            lulc1=synth["lulc1"], lulc2=synth["lulc2"],
            soc1=synth["soc1"], soc2=synth["soc2"],
        )
        agree = float(np.mean(res["degradation"] == synth["truth"]))
        assert agree > 0.98
        # 注入的退化块被识别为退化
        assert np.all(res["degradation"][synth["deg_mask"]] == ld.DEGRADED)
        assert np.all(res["degradation"][synth["imp_mask"]] == ld.IMPROVED)

    def test_productivity_only(self):
        """仅提供 NDVI 时序（无 LULC/SOC）也能产出分级。"""
        synth = ld.generate_synthetic([116, 39, 117, 40], n_dates=6)
        res = ld.assess_degradation(synth["ndvi"], synth["times"])
        assert res["cover_class"] is None
        assert res["carbon_class"] is None
        assert res["degradation"].shape == (64, 64)
        assert res["counts"]["degraded"] > 0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        ld.write_geotiff(path, arr, bbox)
        back, rb = ld.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(ld.UsageError):
            ld.read_geotiff("/no/such/file.tif")
