"""Core algorithm tests for orchard-tree-counting — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestPeakDetection:
    def test_recovers_known_trees(self):
        chm, info = mod.generate_synthetic([116, 39, 117, 40])
        peaks = mod.detect_tree_peaks(chm, min_distance=5, threshold_abs=1.0)
        # should recover all true trees
        assert len(peaks) == info["n_trees_true"]

    def test_threshold_filters_noise(self):
        chm = np.random.default_rng(0).uniform(0, 0.5, (32, 32)).astype(np.float32)
        peaks = mod.detect_tree_peaks(chm, min_distance=3, threshold_abs=1.0)
        assert len(peaks) == 0

    def test_min_distance_suppresses_duplicates(self):
        chm, _ = mod.generate_synthetic([116, 39, 117, 40], spacing=12)
        peaks_close = mod.detect_tree_peaks(chm, min_distance=2, threshold_abs=1.0)
        peaks_far = mod.detect_tree_peaks(chm, min_distance=10, threshold_abs=1.0)
        assert len(peaks_far) <= len(peaks_close)


class TestCrownTemplate:
    def test_template_shape_odd(self):
        tmpl = mod.crown_template(radius_px=3.0)
        assert tmpl.shape[0] == tmpl.shape[1]
        assert tmpl.shape[0] % 2 == 1

    def test_peak_at_center(self):
        tmpl = mod.crown_template(radius_px=4.0, size=15)
        c = 15 // 2
        assert tmpl[c, c] == pytest.approx(1.0, abs=1e-5)
        assert tmpl[0, 0] < 0.01

    def test_invalid_radius_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.crown_template(radius_px=0.0)


class TestTemplateMatch:
    def test_high_score_for_orchard(self):
        chm, _ = mod.generate_synthetic([116, 39, 117, 40], crown_radius_px=3.0)
        tmpl = mod.crown_template(radius_px=3.0)
        score = mod.template_match_score(chm, tmpl)
        assert 0.0 <= score <= 1.0

    def test_low_score_for_flat(self):
        flat = np.full((32, 32), 5.0, dtype=np.float32)
        tmpl = mod.crown_template(radius_px=3.0)
        score = mod.template_match_score(flat, tmpl)
        assert score < 0.1  # flat has no crown pattern


class TestCrownWidth:
    def test_recovers_injected_width(self):
        chm, info = mod.generate_synthetic([116, 39, 117, 40],
                                           crown_radius_px=3.0, spacing=20)
        peaks = mod.detect_tree_peaks(chm, min_distance=5, threshold_abs=1.0)
        assert len(peaks) > 0
        widths = [mod.crown_width_fwhm(chm, (p[0], p[1]), pixel_size_m=1.0) for p in peaks]
        widths = np.array(widths)
        assert widths.size > 0
        assert np.all(widths > 0)
        # FWHM should be roughly proportional to crown radius
        mean_w = np.mean(widths)
        assert 2.0 < mean_w < 10.0  # reasonable range for radius=3px

    def test_zero_height_returns_zero(self):
        chm = np.zeros((20, 20), dtype=np.float32)
        width = mod.crown_width_fwhm(chm, (10, 10), pixel_size_m=1.0)
        assert width == 0.0

    def test_pixel_size_scales_width(self):
        chm, _ = mod.generate_synthetic([116, 39, 117, 40], crown_radius_px=3.0, spacing=20)
        peaks = mod.detect_tree_peaks(chm, min_distance=5, threshold_abs=1.0)
        p = peaks[0]
        w1 = mod.crown_width_fwhm(chm, (p[0], p[1]), pixel_size_m=1.0)
        w2 = mod.crown_width_fwhm(chm, (p[0], p[1]), pixel_size_m=2.0)
        assert w2 == pytest.approx(2.0 * w1, abs=1e-4)


class TestCountAndCrowns:
    def test_full_pipeline(self):
        chm, info = mod.generate_synthetic([116, 39, 117, 40], spacing=12)
        res = mod.count_and_crowns(chm, min_distance=5, threshold_abs=1.0, pixel_size_m=1.0)
        assert res["count"] == info["n_trees_true"]
        assert res["mean_crown_width_m"] > 0
        assert 0.0 <= res["template_score"] <= 1.0
        assert res["density_per_ha"] > 0

    def test_2d_required(self):
        with pytest.raises(mod.ValidationError):
            mod.count_and_crowns(np.zeros((2, 8, 8), dtype=np.float32))
