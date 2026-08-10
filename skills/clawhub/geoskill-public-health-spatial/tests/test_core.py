"""Core algorithm tests for public-health-spatial."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ph


class TestKDE:
    def test_peak_at_dense_cluster(self):
        rng = np.random.default_rng(0)
        cluster = np.column_stack([rng.normal(30, 1.0, 80), rng.normal(40, 1.0, 80)])
        bg = np.column_stack([rng.uniform(0, 64, 20), rng.uniform(0, 64, 20)])
        pts = np.vstack([cluster, bg])
        grid = ph.kde_grid(pts, 64, 64, bandwidth=2.0)
        peak = np.unravel_index(np.argmax(grid), grid.shape)
        assert abs(peak[0] - 30) <= 3
        assert abs(peak[1] - 40) <= 3

    def test_empty_points_zero(self):
        grid = ph.kde_grid(np.zeros((0, 2)), 16, 16)
        assert grid.shape == (16, 16)
        assert grid.sum() == 0.0

    def test_density_positive_near_point(self):
        pts = np.array([[10.0, 10.0]])
        grid = ph.kde_grid(pts, 20, 20, bandwidth=1.5)
        assert grid[10, 10] > grid[0, 0]


class TestScanStatistic:
    def test_llr_zero_when_uniform_rate(self):
        # 病例与人口成比例 -> 内外发病率相等 -> LLR=0
        population = np.array([100.0, 100.0, 100.0, 100.0])
        cases = np.array([10.0, 10.0, 10.0, 10.0])
        centroids = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
        res = ph.spatial_scan(cases, population, centroids, max_frac=0.5)
        assert res["llr"] == pytest.approx(0.0, abs=1e-6)

    def test_llr_positive_with_cluster(self):
        population = np.full(16, 100.0)
        cases = np.full(16, 2.0)
        cases[0] = 40.0  # 一个区域病例暴增
        ys, xs = np.mgrid[0:4, 0:4]
        centroids = np.column_stack([ys.ravel(), xs.ravel()]).astype(float)
        res = ph.spatial_scan(cases, population, centroids, max_frac=0.5)
        assert res["llr"] > 0.0
        assert res["rr"] > 1.0
        assert res["center_idx"] == 0  # 最可能聚集中心即高病例区

    def test_llr_function_nonnegative(self):
        # 内部发病率低于外部 -> LLR 取 0
        assert ph.kulldorff_llr(1, 100, 50, 1000) == 0.0


class TestCorrelation:
    def test_perfect_positive(self):
        a = np.arange(100, dtype=float).reshape(10, 10)
        b = a * 3.0 + 5.0
        assert ph.pearson_corr(a, b) == pytest.approx(1.0, abs=1e-9)

    def test_perfect_negative(self):
        a = np.arange(100, dtype=float)
        b = -a
        assert ph.pearson_corr(a, b) == pytest.approx(-1.0, abs=1e-9)

    def test_constant_zero(self):
        a = np.ones((10, 10))
        b = np.arange(100, dtype=float).reshape(10, 10)
        assert ph.pearson_corr(a, b) == 0.0


class TestAccessibility:
    def test_zero_at_facility_increases_away(self):
        mask = np.zeros((20, 20), dtype=bool)
        mask[10, 10] = True
        d = ph.accessibility_distance(mask, pixel_size=1.0)
        assert d[10, 10] == pytest.approx(0.0)
        assert d[0, 0] > d[9, 9]
        # 距离变换精确值：(10,10)->(10,13) = 3
        assert d[10, 13] == pytest.approx(3.0, abs=1e-5)

    def test_pixel_size_scaling(self):
        mask = np.zeros((10, 10), dtype=bool)
        mask[5, 5] = True
        d1 = ph.accessibility_distance(mask, pixel_size=1.0)
        d2 = ph.accessibility_distance(mask, pixel_size=2.0)
        assert d2[0, 0] == pytest.approx(2.0 * d1[0, 0], rel=1e-5)

    def test_no_facility_inf(self):
        mask = np.zeros((8, 8), dtype=bool)
        d = ph.accessibility_distance(mask)
        assert np.all(np.isinf(d))


class TestSynthetic:
    def test_scene_shapes(self):
        cube, cases, info = ph.generate_synthetic_scene([116, 39, 117, 40], seed=1)
        assert cube.shape == (2, 128, 128)
        assert cases.shape[1] == 2
        cr, cc = info["cluster_center_rc"]
        # KDE 峰值应接近注入聚集中心
        grid = ph.kde_grid(cases, 128, 128, bandwidth=4.0)
        peak = np.unravel_index(np.argmax(grid), grid.shape)
        assert abs(peak[0] - cr) <= 10 and abs(peak[1] - cc) <= 10


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "p.tif")
        ph.write_geotiff(path, cube, bbox)
        back, rb = ph.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ph.UsageError):
            ph.read_geotiff("/nonexistent/p.tif")
