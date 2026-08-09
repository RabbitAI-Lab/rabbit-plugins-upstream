"""Core algorithm tests for profile-chart-generator."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestPathGeometry:
    def test_path_length_one_degree_equator(self):
        # 赤道处 1 个经度 ≈ 111320 m
        verts = np.array([[0.0, 0.0], [1.0, 0.0]])
        L = mod.path_length_m(verts)
        assert abs(L - 111320.0) < 1.0

    def test_segment_lengths_count(self):
        verts = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0]])
        seg = mod.segment_lengths_m(verts)
        assert seg.shape == (2,)
        assert np.all(seg > 0)

    def test_samples_from_interval(self):
        assert mod.samples_from_interval(1000.0, 100.0) == 11  # 0..1000
        assert mod.samples_from_interval(1000.0, 300.0) == 5   # ceil(3.33)+1
        assert mod.samples_from_interval(0.0, 100.0) == 2      # 最少 2 点

    def test_samples_interval_invalid_raises(self):
        with pytest.raises(mod.UsageError):
            mod.samples_from_interval(1000.0, 0.0)

    def test_resample_endpoints_exact(self):
        verts = np.array([[116.0, 39.0], [117.0, 40.0]])
        pts, total = mod.resample_path(verts, 5)
        assert pts.shape == (5, 2)
        np.testing.assert_allclose(pts[0], verts[0], atol=1e-9)
        np.testing.assert_allclose(pts[-1], verts[-1], atol=1e-9)

    def test_resample_equal_spacing(self):
        # 直线重采样：相邻点地面间距一致
        verts = np.array([[0.0, 0.0], [1.0, 0.0]])
        pts, total = mod.resample_path(verts, 11)
        seg = mod.segment_lengths_m(pts)
        np.testing.assert_allclose(seg, total / 10.0, rtol=1e-6)

    def test_resample_too_few_raises(self):
        with pytest.raises(mod.UsageError):
            mod.resample_path(np.array([[0.0, 0.0]]), 5)


class TestBilinear:
    def _linear_raster(self, bbox, h, w, a, b, c):
        # z = a*x + b*y + c（在像元中心取值）
        W, S, E, N = bbox
        pw = (E - W) / w; ph = (N - S) / h
        cols = W + (np.arange(w) + 0.5) * pw
        rows = N - (np.arange(h) + 0.5) * ph
        xx, yy = np.meshgrid(cols, rows)
        return (a * xx + b * yy + c).astype(np.float32)

    def test_plane_exact_interior(self):
        # 双线性内插对平面精确
        bbox = [0.0, 0.0, 1.0, 1.0]
        a, b, c = 2.0, -3.0, 5.0
        raster = self._linear_raster(bbox, 50, 50, a, b, c)
        for x, y in [(0.3, 0.7), (0.5, 0.5), (0.123, 0.888), (0.9, 0.2)]:
            got = mod.bilinear_sample(raster, bbox, x, y)
            assert abs(got - (a * x + b * y + c)) < 1e-3

    def test_extract_profile_length_matches(self):
        bbox = [0.0, 0.0, 1.0, 1.0]
        raster = self._linear_raster(bbox, 30, 30, 1.0, 1.0, 0.0)
        pts = np.array([[0.1, 0.1], [0.5, 0.5], [0.9, 0.9]])
        vals = mod.extract_profile(raster, bbox, pts)
        assert vals.shape == (3,)
        # 沿对角线 x=y，z = x+y，故值递增
        assert vals[0] < vals[1] < vals[2]

    def test_profile_samples_consistent_with_path(self):
        # 验收点：采样点数与路径长度一致（interval 决定，等距且步长<=interval）
        verts = np.array([[0.0, 0.0], [1.0, 0.0]])  # 赤道 111320 m
        L = mod.path_length_m(verts)
        interval = 10000.0
        n = mod.samples_from_interval(L, interval)
        pts, _ = mod.resample_path(verts, n)
        seg = mod.segment_lengths_m(pts)
        spacing = L / (n - 1)
        # 相邻点等距，且步长不超过 interval（密度保证）
        np.testing.assert_allclose(seg, spacing, rtol=1e-6)
        assert 0 < spacing <= interval + 1e-6
        # 总长 = (n-1)*spacing 精确闭合到路径长度
        np.testing.assert_allclose((n - 1) * spacing, L, rtol=1e-9)
        assert len(pts) == n


class TestRenderAndCsv:
    def test_png_magic(self):
        png = mod.render_profile_png(np.array([0, 100, 200.0]),
                                     np.array([10, 30, 20.0]), "T")
        assert png[:8] == b"\x89PNG\r\n\x1a\n"

    def test_csv_format(self, tmp_path):
        dist = np.array([0.0, 100.0, 200.0])
        pts = np.array([[116.0, 39.0], [116.5, 39.5], [117.0, 40.0]])
        vals = np.array([10.0, 20.0, 15.0])
        path = str(tmp_path / "p.csv")
        mod.write_profile_csv(path, dist, pts, vals)
        with open(path, encoding="utf-8") as f:
            lines = f.read().strip().split("\n")
        assert lines[0] == "index,distance_m,lon,lat,value"
        assert len(lines) == 4  # header + 3 rows
        assert lines[1].split(",")[0] == "0"


class TestSynthetic:
    def test_shape(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dem.shape == (64, 64)
        assert info["max_elev"] > info["min_elev"]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "d.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
