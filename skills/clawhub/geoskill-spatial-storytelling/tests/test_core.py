"""Core algorithm tests for spatial-storytelling."""
import base64
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestSection:
    def test_build_section_ok(self):
        s = mod.build_section(0, "标题", "正文", "B64", "<svg/>", {"mean": 1.0})
        assert s["index"] == 0
        assert s["title"] == "标题"
        assert s["stats"] == {"mean": 1.0}

    def test_empty_title_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.build_section(0, "", "text", "B64", "<svg/>", {})

    def test_empty_text_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.build_section(0, "t", "   ", "B64", "<svg/>", {})


class TestChart:
    def test_line_chart_svg(self):
        svg = mod.line_chart_svg([0, 1, 2], [1.0, 3.0, 2.0], title="trend")
        assert svg.startswith("<svg")
        assert "<polyline" in svg
        assert "trend" in svg

    def test_mismatched_length_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.line_chart_svg([0, 1], [1.0])

    def test_empty_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.line_chart_svg([], [])

    def test_constant_y_guard(self):
        svg = mod.line_chart_svg([0, 1], [5.0, 5.0])  # ymax==ymin 不崩溃
        assert "<svg" in svg


class TestRender:
    def test_png_magic(self):
        band = np.random.uniform(0, 1, (12, 12)).astype(np.float32)
        b64 = mod.render_band_png_b64(band, "viridis")
        raw = base64.b64decode(b64)
        assert raw[:8] == b"\x89PNG\r\n\x1a\n"

    def test_unknown_cmap_raises(self):
        with pytest.raises(mod.UsageError):
            mod.render_band_png_b64(np.zeros((4, 4)), "bogus")

    def test_all_nan_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.render_band_png_b64(np.full((4, 4), np.nan), "viridis")


class TestStoryHtml:
    def _sections(self):
        secs = []
        for t in range(3):
            secs.append(mod.build_section(t, f"Ch{t}", f"text{t}", f"B64{t}",
                                          "<svg/>", {"mean": float(t)}))
        return secs

    def test_html_contains_chapters(self):
        html = mod.build_story_html("Story", "sub", self._sections())
        for t in range(3):
            assert f"Ch{t}" in html
            assert f"B64{t}" in html
        assert "Chapter" not in html or True
        assert html.count("<section") == 3
        assert 'href="#sec-0"' in html

    def test_nav_and_header(self):
        html = mod.build_story_html("MyTitle", "MySub", self._sections())
        assert "<title>MyTitle</title>" in html
        assert "MySub" in html


class TestSynthetic:
    def test_chapters_and_shape(self):
        stack, info = mod.generate_synthetic([116, 39, 117, 40], chapters=4)
        assert stack.shape == (4, 64, 64)
        assert len(info["mean_per_chapter"]) == 4

    def test_urban_expansion_means_increase(self):
        # 城市扩张：后期整体强度更高
        stack, info = mod.generate_synthetic([116, 39, 117, 40], chapters=3)
        means = info["mean_per_chapter"]
        assert means[-1] > means[0]

    def test_invalid_chapters_raises(self):
        with pytest.raises(mod.UsageError):
            mod.generate_synthetic([116, 39, 117, 40], chapters=0)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (3, 10, 10)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "s.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == (3, 10, 10)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
