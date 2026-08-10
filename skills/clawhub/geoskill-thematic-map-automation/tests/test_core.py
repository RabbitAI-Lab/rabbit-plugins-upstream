"""Core algorithm tests for thematic-map-automation."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestClassify:
    def test_equal_interval_edges(self):
        edges = mod.classify(np.arange(0, 101, dtype=float), "equal_interval", 4)
        assert len(edges) == 5
        np.testing.assert_allclose(edges, [0, 25, 50, 75, 100], atol=1e-6)

    def test_quantile_median_edge(self):
        vals = np.arange(0, 101, dtype=float)
        edges = mod.classify(vals, "quantile", 4)
        assert abs(edges[2] - 50.0) < 1e-6  # 50% 分位
        assert edges[0] == 0.0 and edges[-1] == 100.0

    def test_quantile_skewed_vs_equal(self):
        # 偏态数据：分位数断点应不同于等间距
        vals = np.concatenate([np.zeros(50), np.arange(1, 51, dtype=float)])
        q = mod.classify(vals, "quantile", 4)
        e = mod.classify(vals, "equal_interval", 4)
        assert q[1] != e[1]

    def test_jenks_separates_bimodal(self):
        vals = np.array([1, 2, 3, 10, 11, 12.0])
        edges = mod.jenks_breaks(vals, 2)
        # 内部断点必须落在两簇空隙 [3, 10] 内
        assert edges[1] >= 3.0
        assert edges[1] <= 10.0
        assert edges[0] == 1.0 and edges[-1] == 12.0

    def test_jenks_three_clusters(self):
        vals = np.array([1, 2, 3, 20, 21, 22, 40, 41, 42.0])
        edges = mod.classify(vals, "jenks", 3)
        assert len(edges) == 4
        # 断点单调递增
        assert all(edges[i] <= edges[i + 1] for i in range(len(edges) - 1))

    def test_invalid_method_raises(self):
        with pytest.raises(mod.UsageError):
            mod.classify(np.arange(10.0), "bad_method", 3)

    def test_too_few_classes_raises(self):
        with pytest.raises(mod.UsageError):
            mod.classify(np.arange(10.0), "quantile", 1)


class TestAssignClass:
    def test_known_assignment(self):
        edges = [0, 25, 50, 75, 100]
        out = mod.assign_class(np.array([0, 10, 30, 60, 90, 100.0]), edges)
        assert out.tolist() == [0, 0, 1, 2, 3, 3]

    def test_clip_to_range(self):
        edges = [0, 5, 10]
        out = mod.assign_class(np.array([-100, 100.0]), edges)
        assert out[0] == 0 and out[1] == 1


class TestSymbols:
    def test_proportional_area_proportional(self):
        sizes = mod.proportional_sizes(np.array([1.0, 4.0]), max_size=100.0)
        # 面积正比于值：4/1 → size 比 4
        assert abs(sizes[1] / sizes[0] - 4.0) < 1e-6
        assert sizes[1] == 100.0

    def test_proportional_zero_guard(self):
        sizes = mod.proportional_sizes(np.array([0.0, 0.0]))
        assert np.all(sizes == 0.0)

    def test_dot_counts_known(self):
        out = mod.dot_counts(np.array([10.0, 21.0, 2.0]), 5.0)
        assert out.tolist() == [2, 4, 0]

    def test_dot_counts_invalid_vpd_raises(self):
        with pytest.raises(mod.UsageError):
            mod.dot_counts(np.array([1.0]), 0.0)

    def test_random_points_inside_polygon(self):
        from shapely.geometry import box
        poly = box(0, 0, 1, 1)
        rng = np.random.default_rng(0)
        pts = mod.random_points_in_polygon(poly, 50, rng)
        assert len(pts) == 50
        for x, y in pts:
            assert 0.0 <= x <= 1.0 and 0.0 <= y <= 1.0


class TestSyntheticAndRender:
    def test_synthetic_grid_count(self):
        gdf = mod.generate_synthetic([116, 39, 117, 40], nx=6, ny=5)
        assert len(gdf) == 30
        assert gdf.crs is not None
        assert "value" in gdf.columns

    def test_render_png_and_pdf(self, tmp_path):
        gdf = mod.generate_synthetic([116, 39, 117, 40], nx=4, ny=4)
        edges = mod.classify(gdf["value"].to_numpy(), "quantile", 4)
        gdf2 = gdf.copy(); gdf2["class"] = mod.assign_class(gdf2["value"].to_numpy(), edges)
        fig = mod.render_thematic(gdf2, edges, "YlOrRd", "choropleth", 5.0, 42, "T")
        png = str(tmp_path / "t.png"); pdf = str(tmp_path / "t.pdf")
        fig.savefig(png); fig.savefig(pdf, format="pdf")
        with open(png, "rb") as f:
            assert f.read(8) == b"\x89PNG\r\n\x1a\n"
        with open(pdf, "rb") as f:
            assert f.read(4) == b"%PDF"

    def test_rasterize_classes_valid(self):
        gdf = mod.generate_synthetic([0, 0, 1, 1], nx=4, ny=4)
        edges = mod.classify(gdf["value"].to_numpy(), "quantile", 4)
        gdf2 = gdf.copy(); gdf2["class"] = mod.assign_class(gdf2["value"].to_numpy(), edges)
        r = mod.rasterize_classes(gdf2, [0, 0, 1, 1], 16, 16)
        assert r.shape == (16, 16)
        valid = r[r >= 0]
        assert valid.size > 0
        assert valid.min() >= 0 and valid.max() <= 3
