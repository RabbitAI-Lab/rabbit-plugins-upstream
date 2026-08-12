"""Core algorithm tests for impervious-surface-trend."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ist


class TestLinearTrend:
    def test_recovers_known_slope(self):
        times = np.arange(5, dtype=float)
        # y = 3*t + 5 逐像元
        cube = np.zeros((5, 4, 4))
        for t in range(5):
            cube[t] = 3.0 * t + 5.0
        slope, intercept = ist.linear_trend(cube, times)
        np.testing.assert_allclose(slope, 3.0, atol=1e-9)
        np.testing.assert_allclose(intercept, 5.0, atol=1e-9)

    def test_flat_zero_slope(self):
        times = np.arange(6, dtype=float)
        cube = np.full((6, 3, 3), 0.4)
        slope, _ = ist.linear_trend(cube, times)
        np.testing.assert_allclose(slope, 0.0, atol=1e-12)

    def test_shape_mismatch_raises(self):
        with pytest.raises(ist.ValidationError):
            ist.linear_trend(np.zeros((5, 2, 2)), np.arange(4))

    def test_too_few_dates_raises(self):
        with pytest.raises(ist.ValidationError):
            ist.linear_trend(np.zeros((1, 2, 2)), np.arange(1))

    def test_identical_times_raises(self):
        with pytest.raises(ist.ValidationError):
            ist.linear_trend(np.zeros((3, 2, 2)), np.array([1.0, 1.0, 1.0]))


class TestExponentialTrend:
    def test_recovers_rate(self):
        times = np.arange(5, dtype=float)
        # y = 0.1 * exp(0.4 t)，均 < 1
        cube = np.zeros((5, 3, 3))
        for t in range(5):
            cube[t] = 0.1 * np.exp(0.4 * t)
        b, a = ist.exponential_trend(cube, times)
        np.testing.assert_allclose(b, 0.4, atol=1e-6)
        np.testing.assert_allclose(a, np.log(0.1), atol=1e-6)


class TestHotspots:
    def test_high_value_flagged(self):
        slope = np.zeros((10, 10))
        slope[5, 5] = 10.0
        hot, thr = ist.detect_hotspots(slope, k=1.0)
        assert hot[5, 5]
        assert thr > 0

    def test_positive_only(self):
        slope = np.full((4, 4), -1.0)
        slope[0, 0] = -0.5  # 最高但仍为负
        hot, _ = ist.detect_hotspots(slope, k=1.0, positive_only=True)
        assert not hot.any()

    def test_all_same_no_hotspot(self):
        slope = np.full((5, 5), 2.0)
        hot, _ = ist.detect_hotspots(slope)
        assert not hot.any()  # std=0, thr=mean, 无严格大于


class TestFitTrend:
    def test_unknown_method_raises(self):
        cube = np.random.uniform(0, 1, (4, 4, 4))
        with pytest.raises(ist.UsageError):
            ist.fit_trend(cube, np.arange(4), method="cubic")

    def test_stats_keys(self):
        cube = np.random.uniform(0, 1, (5, 8, 8))
        res = ist.fit_trend(cube, np.arange(5), method="linear")
        for key in ("mean_slope", "hotspot_fraction", "positive_fraction"):
            assert key in res["stats"]


class TestSyntheticRecovery:
    def test_linear_recovers_injected(self):
        """线性合成：强增长块斜率应接近注入值 0.05，热点应覆盖它。"""
        synth = ist.generate_synthetic([116, 39, 117, 40], n_dates=5,
                                       trend="linear", seed=11)
        res = ist.fit_trend(synth["cube"], synth["times"], method="linear")
        slope = res["slope"]
        grow = synth["grow_mask"]
        np.testing.assert_allclose(slope[grow].mean(), 0.05, atol=0.01)
        assert res["hotspots"][grow].mean() > 0.95
        assert res["stats"]["hotspot_fraction"] < 0.3

    def test_exponential_recovers_injected(self):
        """指数合成：强增长块相对增长率应接近注入值 0.15。"""
        synth = ist.generate_synthetic([116, 39, 117, 40], n_dates=6,
                                       trend="exponential", seed=11)
        res = ist.fit_trend(synth["cube"], synth["times"], method="exponential")
        b = res["slope"]
        grow = synth["grow_mask"]
        np.testing.assert_allclose(b[grow].mean(), 0.15, atol=0.03)
        # 大多数像元正增长（背景增长率弱、含噪声，允许少量为负）
        assert res["stats"]["positive_fraction"] > 0.7


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        ist.write_geotiff(path, arr, bbox)
        back, rb = ist.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(ist.UsageError):
            ist.read_geotiff("/no/such/file.tif")
