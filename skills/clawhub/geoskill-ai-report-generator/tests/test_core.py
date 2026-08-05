"""Core algorithm tests for ai-report-generator."""
import sys
import os
import json

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestHtmlEscape:
    def test_escapes_special_chars(self):
        assert mod.html_escape("<script>") == "&lt;script&gt;"
        assert mod.html_escape("a & b") == "a &amp; b"
        assert mod.html_escape('"q"') == "&quot;q&quot;"

    def test_injection_neutralized(self):
        evil = "<img src=x onerror=alert(1)>"
        out = mod.html_escape(evil)
        assert "<img" not in out
        assert "&lt;img" in out


class TestLoadAnalysis:
    def test_dict_passthrough(self):
        d = {"a": 1}
        assert mod.load_analysis(d) is d

    def test_from_file(self, tmp_path):
        p = tmp_path / "r.json"
        p.write_text(json.dumps({"ndvi_mean": 0.5}), encoding="utf-8")
        d = mod.load_analysis(str(p))
        assert d["ndvi_mean"] == 0.5

    def test_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.load_analysis("/nonexistent/r.json")

    def test_non_dict_root_raises(self, tmp_path):
        p = tmp_path / "list.json"
        p.write_text(json.dumps([1, 2, 3]), encoding="utf-8")
        with pytest.raises(mod.ValidationError):
            mod.load_analysis(str(p))


class TestNumericMetrics:
    def test_excludes_strings_and_bool(self):
        res = {"a": 1.0, "b": "text", "c": True, "d": 3}
        m = mod.numeric_metrics(res)
        assert set(m.keys()) == {"a", "d"}
        assert m["d"] == 3.0

    def test_excludes_nan(self):
        m = mod.numeric_metrics({"a": float("nan"), "b": 2.0})
        assert set(m.keys()) == {"b"}


class TestComputeSummary:
    def test_stats(self):
        res = {"x": 1.0, "y": 5.0, "z": 3.0}
        s = mod.compute_summary(res)
        assert s["n_metrics"] == 3
        assert s["min"] == 1.0 and s["min_key"] == "x"
        assert s["max"] == 5.0 and s["max_key"] == "y"
        assert s["mean"] == pytest.approx(3.0)

    def test_empty(self):
        s = mod.compute_summary({"name": "abc"})
        assert s["n_metrics"] == 0
        assert s["min"] is None


class TestQualityFlags:
    def test_pass_warn_fail(self):
        res = {"cloud_cover_pct": 2.0, "ndvi_mean": 0.25, "valid_pixels": 100.0}
        th = {"cloud_cover_pct": (5.0, 15.0),   # >=15 PASS, >=5 WARN, <5 FAIL
              "ndvi_mean": (0.2, 0.35),
              "valid_pixels": (1000.0, 5000.0)}
        flags = mod.quality_flags(res, th)
        assert flags["cloud_cover_pct"] == "FAIL"   # 2 < 5
        assert flags["ndvi_mean"] == "WARN"          # 0.2 <= 0.25 < 0.35
        assert flags["valid_pixels"] == "FAIL"       # 100 < 1000

    def test_pass_boundary(self):
        flags = mod.quality_flags({"m": 15.0}, {"m": (5.0, 15.0)})
        assert flags["m"] == "PASS"  # >= high

    def test_missing_metric_skipped(self):
        flags = mod.quality_flags({"a": 1.0}, {"b": (0.0, 1.0)})
        assert flags == {}


class TestRenderMarkdown:
    def test_contains_title_and_table(self):
        res = {"ndvi_mean": 0.6, "cloud_cover_pct": 3.0}
        md = mod.render_markdown(res, "测试报告")
        assert "# 测试报告" in md
        assert "| 指标 | 数值 | 评级 |" in md
        assert "ndvi_mean" in md

    def test_conclusion_fail(self):
        res = {"ndvi_mean": 0.05}
        flags = {"ndvi_mean": "FAIL"}
        md = mod.render_markdown(res, "T", flags=flags)
        assert "FAIL" in md
        assert "不达标" in md


class TestRenderHTML:
    def test_structure(self):
        res = {"ndvi_mean": 0.6}
        html = mod.render_html(res, "报告")
        assert html.startswith("<!DOCTYPE html>")
        assert "<h1>报告</h1>" in html
        assert "<table>" in html
        assert html.rstrip().endswith("</html>")

    def test_escaping_in_title(self):
        html = mod.render_html({"a": 1.0}, "<b>X</b>")
        assert "<b>X</b>" not in html
        assert "&lt;b&gt;X&lt;/b&gt;" in html


class TestRasterBandStats:
    def test_per_band(self):
        cube = np.array([[[1.0, 2.0], [3.0, 4.0]],
                         [[10.0, 20.0], [30.0, 40.0]]], dtype=np.float32)
        stats = mod.raster_band_stats(cube)
        assert stats["n_bands"] == 2
        assert stats["band_0_min"] == 1.0
        assert stats["band_0_max"] == 4.0
        assert stats["band_0_mean"] == pytest.approx(2.5)
        assert stats["band_1_mean"] == pytest.approx(25.0)
        assert stats["overall_mean"] == pytest.approx(13.75)


class TestSynthetic:
    def test_has_expected_keys(self):
        res = mod.generate_synthetic([116, 39, 117, 40], seed=1)
        assert "ndvi_mean" in res
        assert "cloud_cover_pct" in res
        assert res["bbox"] == [116, 39, 117, 40]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "r.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
