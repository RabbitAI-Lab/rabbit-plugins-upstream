"""Core algorithm tests for pasture-quality-assessment — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestFractionalCover:
    def test_soil_endpoint_zero(self):
        fvc = mod.fractional_cover(np.array([[0.10]]), ndvi_soil=0.10, ndvi_veg=0.70)
        assert fvc[0, 0] == pytest.approx(0.0, abs=1e-6)

    def test_veg_endpoint_one(self):
        fvc = mod.fractional_cover(np.array([[0.70]]), ndvi_soil=0.10, ndvi_veg=0.70)
        assert fvc[0, 0] == pytest.approx(1.0, abs=1e-6)

    def test_monotonic(self):
        ndvi = np.array([[0.1, 0.3, 0.5, 0.7]], dtype=np.float32)
        fvc = mod.fractional_cover(ndvi)
        assert np.all(np.diff(fvc[0]) > 0)

    def test_clipped_01(self):
        ndvi = np.array([[0.0, 1.0]], dtype=np.float32)
        fvc = mod.fractional_cover(ndvi)
        assert fvc.min() >= 0.0 and fvc.max() <= 1.0

    def test_invalid_endpoints_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.fractional_cover(np.array([[0.5]]), ndvi_soil=0.7, ndvi_veg=0.1)


class TestPhenology:
    def test_peak_at_gaussian_center(self):
        t = np.linspace(0, 1, 21)
        series = 0.15 + 0.6 * np.exp(-((t - 0.5) ** 2) / (2 * 0.12 ** 2))
        phen = mod.phenology_metrics(series.astype(np.float32))
        # 21 steps, center at index 10
        assert phen["peak_index"] == 10
        assert phen["peak_value"] == pytest.approx(0.75, abs=0.02)

    def test_season_length_positive(self):
        t = np.linspace(0, 1, 12)
        series = (0.1 + 0.5 * np.exp(-((t - 0.5) ** 2) / (2 * 0.15 ** 2))).astype(np.float32)
        phen = mod.phenology_metrics(series)
        assert phen["season_length"] > 0
        assert phen["season_start"] <= phen["peak_index"] <= phen["season_end"]
        # amplitude must equal the realized (discrete) max - min of the series
        expected_amp = float(series.max() - series.min())
        assert phen["amplitude"] == pytest.approx(expected_amp, abs=1e-4)

    def test_flat_series_zero_amplitude(self):
        phen = mod.phenology_metrics(np.full(10, 0.4, dtype=np.float32))
        assert phen["amplitude"] == 0.0

    def test_too_short_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.phenology_metrics(np.array([0.1, 0.2], dtype=np.float32))


class TestDegradationSlope:
    def test_increasing_trend_positive(self):
        # annual NDVI rises +0.02/yr at every pixel
        years, h, w = 8, 3, 3
        annual = np.zeros((years, h, w), dtype=np.float32)
        for y in range(years):
            annual[y] = 0.3 + 0.02 * y
        slope = mod.degradation_slope(annual)
        np.testing.assert_allclose(slope, 0.02, atol=1e-5)

    def test_decreasing_trend_negative(self):
        years, h, w = 8, 3, 3
        annual = np.zeros((years, h, w), dtype=np.float32)
        for y in range(years):
            annual[y] = 0.6 - 0.03 * y
        slope = mod.degradation_slope(annual)
        np.testing.assert_allclose(slope, -0.03, atol=1e-5)

    def test_stable_trend_zero(self):
        annual = np.full((6, 4, 4), 0.4, dtype=np.float32)
        slope = mod.degradation_slope(annual)
        np.testing.assert_allclose(slope, 0.0, atol=1e-6)

    def test_too_few_years_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.degradation_slope(np.zeros((1, 4, 4), dtype=np.float32))


class TestQuality:
    def test_high_cover_improving_is_best(self):
        cover = np.array([[0.9]], dtype=np.float32)
        slope = np.array([[0.02]], dtype=np.float32)  # improving
        q = mod.quality_index(cover, slope)
        assert q[0, 0] > 0.7

    def test_low_cover_degrading_is_worst(self):
        cover = np.array([[0.05]], dtype=np.float32)
        slope = np.array([[-0.05]], dtype=np.float32)  # degrading
        q = mod.quality_index(cover, slope)
        assert q[0, 0] < 0.2

    def test_quality_range(self):
        rng = np.random.default_rng(0)
        cover = rng.uniform(0, 1, (8, 8)).astype(np.float32)
        slope = rng.uniform(-0.1, 0.1, (8, 8)).astype(np.float32)
        q = mod.quality_index(cover, slope)
        assert q.min() >= 0.0 and q.max() <= 1.0

    def test_grade_thresholds(self):
        q = np.array([[0.2, 0.5, 0.7, 0.9]], dtype=np.float32)
        g = mod.grade_quality(q)
        assert list(g[0]) == [0, 1, 2, 3]


class TestPipeline:
    def test_good_side_higher_quality(self):
        _, packed = mod.generate_synthetic([116, 39, 117, 40])
        aux = packed["aux"]
        res = mod.assess_pasture(aux["current_ndvi"], aux["annual"],
                                 phenology_series=aux["phenology"])
        q = res["quality_index"]
        h, w = q.shape
        left = q[:, :int(w * 0.2)].mean()    # good pasture
        right = q[:, int(w * 0.8):].mean()   # degraded
        assert left > right
        assert res["stats"]["degrading_fraction"] > 0.0  # right side degrades

    def test_2d_required(self):
        with pytest.raises(mod.ValidationError):
            mod.assess_pasture(np.zeros((2, 8, 8)), np.zeros((3, 8, 8)))
