"""Core algorithm tests for spatial-data-dashboard."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestStats:
    def test_histogram_counts_sum(self):
        rng = np.random.default_rng(0)
        vals = rng.normal(100, 20, (50, 50))
        edges, counts = mod.raster_histogram(vals, bins=15)
        assert len(edges) == 16
        assert len(counts) == 15
        assert sum(counts) == 2500  # 全部有效像元

    def test_histogram_ignores_nan(self):
        vals = np.array([1.0, 2.0, np.nan, 4.0, np.inf])
        edges, counts = mod.raster_histogram(vals, bins=4)
        assert sum(counts) == 3  # 只有 1,2,4 有效

    def test_histogram_empty(self):
        edges, counts = mod.raster_histogram(np.array([np.nan, np.nan]), bins=5)
        assert sum(counts) == 0

    def test_descriptive_stats_known(self):
        vals = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        s = mod.descriptive_stats(vals)
        assert s["count"] == 5
        assert abs(s["mean"] - 3.0) < 1e-9
        assert s["min"] == 1.0 and s["max"] == 5.0
        assert abs(s["p50"] - 3.0) < 1e-9

    def test_descriptive_stats_empty(self):
        s = mod.descriptive_stats(np.array([np.nan]))
        assert s["count"] == 0


class TestZonal:
    def test_zonal_means(self):
        values = np.array([[1, 1, 5], [1, 1, 5], [9, 9, 5]], dtype=float)
        labels = np.array([[0, 0, 1], [0, 0, 1], [2, 2, 1]], dtype=int)
        z = mod.zonal_statistics(values, labels)
        assert abs(z[0]["mean"] - 1.0) < 1e-9
        assert z[0]["count"] == 4
        assert abs(z[1]["mean"] - 5.0) < 1e-9
        assert abs(z[2]["mean"] - 9.0) < 1e-9

    def test_zonal_ignores_negative_label(self):
        values = np.ones((3, 3))
        labels = np.full((3, 3), -1, dtype=int)
        assert mod.zonal_statistics(values, labels) == {}

    def test_zonal_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.zonal_statistics(np.ones((3, 3)), np.ones((2, 2), dtype=int))


class TestSvg:
    def test_histogram_rect_count(self):
        edges = [0.0, 1.0, 2.0, 3.0]
        counts = [5, 8, 2]
        svg = mod.svg_histogram(edges, counts, title="H")
        assert svg.count("<rect") == 3
        assert "<svg" in svg and "</svg>" in svg

    def test_line_polyline_points(self):
        svg = mod.svg_line([0, 1, 2, 3], [10, 20, 15, 30])
        assert "<polyline" in svg
        # 4 个点 → 3 个逗号分隔的空格段（points 里有 4 组 x,y）
        assert svg.count(",") >= 4

    def test_line_constant_y_guard(self):
        svg = mod.svg_line([1, 2], [5, 5])  # ymax==ymin 不崩溃
        assert "<svg" in svg


class TestSyntheticAndAssembly:
    def test_synthetic_shapes(self):
        dem, labels, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dem.shape == (64, 64)
        assert labels.shape == (64, 64)
        assert info["zones"] == 16

    def test_dashboard_html_parts(self):
        bbox = [116, 39, 117, 40]
        html = mod.build_dashboard_html(
            bbox, "QUJD", "MyDash", {"count": 10, "mean": 1.0, "std": 0.5,
                                      "min": 0.0, "max": 2.0},
            "<svg>H</svg>", "<svg>L</svg>", {0: {"mean": 1.0, "min": 0.0,
                                                  "max": 2.0, "count": 10}})
        assert "QUJD" in html
        assert "MyDash" in html
        assert "[[39, 116], [40, 117]]" in html
        assert "L.imageOverlay" in html

    def test_overlay_b64_is_png(self):
        dem, _, _ = mod.generate_synthetic([116, 39, 117, 40])
        b64, lo, hi = mod.render_overlay_b64(dem)
        import base64
        raw = base64.b64decode(b64)
        assert raw[:8] == b"\x89PNG\r\n\x1a\n"
        assert hi > lo


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == (1, 16, 16)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
