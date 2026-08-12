"""Core algorithm tests for map-symbology-optimizer."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestWcag:
    def test_luminance_extremes(self):
        assert mod.relative_luminance((255, 255, 255)) == pytest.approx(1.0, abs=1e-6)
        assert mod.relative_luminance((0, 0, 0)) == pytest.approx(0.0, abs=1e-6)

    def test_contrast_black_white_is_21(self):
        assert mod.contrast_ratio((0, 0, 0), (255, 255, 255)) == pytest.approx(21.0, abs=1e-6)

    def test_contrast_same_is_1(self):
        assert mod.contrast_ratio((120, 60, 200), (120, 60, 200)) == pytest.approx(1.0)

    def test_contrast_symmetric(self):
        a = (30, 60, 90); b = (200, 220, 240)
        assert mod.contrast_ratio(a, b) == pytest.approx(mod.contrast_ratio(b, a))

    def test_contrast_range(self):
        rng = np.random.default_rng(0)
        for _ in range(20):
            c1 = tuple(int(x) for x in rng.integers(0, 256, 3))
            c2 = tuple(int(x) for x in rng.integers(0, 256, 3))
            r = mod.contrast_ratio(c1, c2)
            assert 1.0 <= r <= 21.0

    def test_best_text_white_bg(self):
        assert mod.best_text_color((255, 255, 255)) == (0, 0, 0)

    def test_best_text_black_bg(self):
        assert mod.best_text_color((0, 0, 0)) == (255, 255, 255)

    def test_best_text_picks_higher_contrast(self):
        bg = (100, 120, 180)
        txt = mod.best_text_color(bg)
        other = (0, 0, 0) if txt == (255, 255, 255) else (255, 255, 255)
        assert mod.contrast_ratio(bg, txt) >= mod.contrast_ratio(bg, other)


class TestColorblind:
    def test_gray_invariant_under_simulation(self):
        # 灰度 (v,v,v) 经矩阵后仍为 (v,v,v)（矩阵每行和为 1）
        out = mod.simulate_deuteranopia((128, 128, 128))
        np.testing.assert_allclose(out, (128, 128, 128), atol=1e-9)

    def test_okabe_ito_is_safe(self):
        assert mod.is_colorblind_safe(mod.PALETTES["okabe-ito"]) is True

    def test_near_identical_colors_not_safe(self):
        bad = [(119, 119, 0), (136, 136, 0), (127, 128, 0)]
        assert mod.is_colorblind_safe(bad) is False

    def test_separation_decreases_with_similar_colors(self):
        distinct = [(230, 159, 0), (0, 114, 178)]
        similar = [(119, 119, 0), (136, 136, 0)]
        assert mod.min_pairwise_separation(distinct) > mod.min_pairwise_separation(similar)

    def test_single_color_infinite_separation(self):
        assert mod.min_pairwise_separation([(1, 2, 3)]) == float("inf")


class TestSymbology:
    def test_classify_breaks_quantile(self):
        vals = np.arange(0, 101, dtype=float)
        edges = mod.classify_breaks(vals, "quantile", 4)
        assert len(edges) == 5
        assert edges[0] == 0.0 and edges[-1] == 100.0
        assert abs(edges[2] - 50.0) < 1e-6

    def test_classify_breaks_equal_interval(self):
        vals = np.arange(0, 101, dtype=float)
        edges = mod.classify_breaks(vals, "equal_interval", 4)
        np.testing.assert_allclose(edges, [0, 25, 50, 75, 100], atol=1e-6)

    def test_classify_invalid_method(self):
        with pytest.raises(mod.UsageError):
            mod.classify_breaks(np.arange(10.0), "bogus", 4)

    def test_classify_too_few_classes(self):
        with pytest.raises(mod.UsageError):
            mod.classify_breaks(np.arange(10.0), "quantile", 1)

    def test_pick_colors_cycles(self):
        colors = mod.pick_colors("okabe-ito", 10)
        assert len(colors) == 10
        assert colors[0] == colors[8]  # 8 色循环

    def test_pick_colors_unknown_palette(self):
        with pytest.raises(mod.UsageError):
            mod.pick_colors("bogus", 3)

    def test_optimize_symbology_complete(self):
        rng = np.random.default_rng(1)
        vals = rng.uniform(0, 100, (32, 32))
        plan = mod.optimize_symbology(vals, n_classes=5, method="quantile",
                                      palette="okabe-ito")
        assert len(plan["breaks"]) == 6
        assert len(plan["classes"]) == 5
        for c in plan["classes"]:
            assert c["fill_hex"].startswith("#")
            assert c["text_hex"] in ("#000000", "#ffffff")
            assert c["text_contrast"] >= 1.0
        assert plan["qa"]["cvd_safe"] is True
        assert plan["qa"]["min_text_contrast"] >= 1.0

    def test_rgb_to_hex(self):
        assert mod.rgb_to_hex((0, 0, 0)) == "#000000"
        assert mod.rgb_to_hex((255, 255, 255)) == "#ffffff"
        assert mod.rgb_to_hex((230, 159, 0)) == "#e69f00"


class TestRenderAndIO:
    def test_png_magic(self):
        vals = np.random.uniform(0, 10, (16, 16)).astype(np.float32)
        plan = mod.optimize_symbology(vals, n_classes=3, palette="tol-muted")
        png = mod.render_symbology_png(vals, plan)
        assert png[:8] == b"\x89PNG\r\n\x1a\n"

    def test_synthetic_shape(self):
        r, info = mod.generate_synthetic([116, 39, 117, 40])
        assert r.shape == (64, 64)
        assert info["max"] > info["min"]

    def test_geotiff_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (10, 10)).astype(np.float32)
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, [0, 0, 1, 1])
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
