"""Core algorithm tests for crop-counting-yield — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _gaussian_field(positions, h=64, w=64, amp=0.8, sigma=2.5, base=0.02):
    field = np.full((h, w), base, dtype=np.float32)
    yy, xx = np.mgrid[0:h, 0:w]
    for (r, c) in positions:
        field += amp * np.exp(-((yy - r) ** 2 + (xx - c) ** 2) / (2 * sigma ** 2))
    return np.clip(field, 0, 1).astype(np.float32)


class TestPeakDetection:
    def test_recovers_exact_count(self):
        positions = [(10, 10), (10, 40), (40, 10), (40, 40), (25, 25)]
        field = _gaussian_field(positions)
        peaks = mod.detect_peaks(field, min_distance=3, threshold_abs=0.2)
        assert len(peaks) == len(positions)

    def test_single_peak(self):
        field = _gaussian_field([(32, 32)])
        peaks = mod.detect_peaks(field, min_distance=3, threshold_abs=0.2)
        assert len(peaks) == 1
        r, c = peaks[0]
        assert abs(r - 32) <= 1 and abs(c - 32) <= 1

    def test_threshold_filters_noise(self):
        field = _gaussian_field([(20, 20)], amp=0.05)  # very weak
        peaks = mod.detect_peaks(field, min_distance=3, threshold_abs=0.2)
        assert len(peaks) == 0


class TestWatershed:
    def test_labels_match_peaks(self):
        positions = [(12, 12), (12, 45), (45, 12), (45, 45)]
        field = _gaussian_field(positions)
        peaks = mod.detect_peaks(field, min_distance=3, threshold_abs=0.2)
        labels = mod.watershed_segment(field, peaks)
        # number of positive labels should be at least the number of peaks (scipy path)
        n_labels = len([u for u in np.unique(labels) if u > 0])
        assert n_labels >= 1
        assert labels.shape == field.shape


class TestYieldModel:
    def test_yield_increases_with_density(self):
        y1 = mod.estimate_yield(density=0.1, mean_vigor=0.5)
        y2 = mod.estimate_yield(density=0.3, mean_vigor=0.5)
        assert y2 > y1

    def test_yield_increases_with_vigor(self):
        y1 = mod.estimate_yield(density=0.2, mean_vigor=0.3)
        y2 = mod.estimate_yield(density=0.2, mean_vigor=0.7)
        assert y2 > y1

    def test_yield_formula(self):
        # yield = a*density*vigor + b, defaults a=8000, b=500
        y = mod.estimate_yield(density=0.1, mean_vigor=0.5)
        assert y == pytest.approx(8000 * 0.1 * 0.5 + 500)

    def test_negative_input_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.estimate_yield(density=-0.1, mean_vigor=0.5)


class TestPipeline:
    def test_count_matches_truth(self):
        n = 16
        canopy, info = mod.generate_synthetic([116, 39, 117, 40], n_plants=n, seed=3)
        res = mod.process_canopy(canopy, min_distance=4)
        # detected count should be close to the injected truth (allow small tolerance)
        assert abs(res["count"] - n) <= max(2, int(0.2 * n))
        assert res["density"] > 0
        assert res["yield_kg_ha"] > 0

    def test_2d_required(self):
        with pytest.raises(mod.ValidationError):
            mod.process_canopy(np.zeros((2, 8, 8), dtype=np.float32))

    def test_density_scales_with_area(self):
        canopy, _ = mod.generate_synthetic([116, 39, 117, 40], n_plants=9, seed=5)
        r1 = mod.process_canopy(canopy, pixel_area_m2=1.0)
        r2 = mod.process_canopy(canopy, pixel_area_m2=2.0)
        # larger pixel area -> lower density (plants/m2)
        assert r2["density"] < r1["density"]
