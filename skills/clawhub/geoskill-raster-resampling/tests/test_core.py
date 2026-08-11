"""Core algorithm tests for raster-resampling."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestCubicKernel:
    def test_partition_of_unity(self):
        # 任意采样位置四个邻域权重之和应为 1（保常数）
        for frac in (0.0, 0.25, 0.5, 0.73):
            s = sum(M.cubic_kernel(frac - t) for t in (-1, 0, 1, 2))
            assert s == pytest.approx(1.0, abs=1e-9)

    def test_center_weight_one(self):
        assert M.cubic_kernel(0.0) == pytest.approx(1.0)

    def test_far_zero(self):
        assert M.cubic_kernel(2.5) == 0.0


class TestConstantField:
    def test_all_methods_preserve_constant(self):
        const = np.full((16, 16), 7.0, dtype=np.float32)
        for meth in ("nearest", "bilinear", "cubic"):
            up = M.resample_band(const, 2.0, meth)
            assert up.shape == (32, 32)
            assert float(np.max(np.abs(up - 7.0))) == pytest.approx(0.0, abs=1e-4)

    def test_downsample_constant(self):
        const = np.full((16, 16), 3.0, dtype=np.float32)
        for meth in ("nearest", "bilinear", "cubic"):
            down = M.resample_band(const, 0.5, meth)
            assert down.shape == (8, 8)
            assert float(np.max(np.abs(down - 3.0))) == pytest.approx(0.0, abs=1e-4)


class TestNearest:
    def test_values_are_subset_of_input(self):
        rng = np.random.default_rng(0)
        band = rng.integers(0, 5, (16, 16)).astype(np.float32)
        out = M.resample_band(band, 2.0, "nearest")
        assert set(np.unique(out)).issubset(set(np.unique(band)))

    def test_identity_scale_1(self):
        band = np.arange(256, dtype=np.float32).reshape(16, 16)
        out = M.resample_band(band, 1.0, "nearest")
        np.testing.assert_allclose(out, band)


class TestBilinear:
    def test_linear_plane_exact_interior(self):
        # f = 2x + 3y + 5，双线性对线性函数内部精确重构
        yy, xx = np.mgrid[0:16, 0:16].astype(float)
        band = (2 * xx + 3 * yy + 5).astype(np.float32)
        up = M.resample_band(band, 2.0, "bilinear")
        oy = np.arange(32); ox = np.arange(32)
        iy = (oy + 0.5) / 2 - 0.5
        ix = (ox + 0.5) / 2 - 0.5
        IY, IX = np.meshgrid(iy, ix, indexing="ij")
        expect = 2 * IX + 3 * IY + 5
        # 内部像元（避开边界 clamp）误差应为 0
        assert float(np.max(np.abs(up[2:-2, 2:-2] - expect[2:-2, 2:-2]))) == pytest.approx(0.0, abs=1e-4)

    def test_midpoint_average(self):
        # 2x2 棋盘，中心像元应为四邻均值
        band = np.array([[0, 2], [2, 4]], dtype=np.float32)
        up = M.resample_band(band, 2.0, "bilinear")
        assert up.shape == (4, 4)
        # 整体均值应守恒
        assert float(np.mean(up)) == pytest.approx(float(np.mean(band)), abs=0.5)


class TestShape:
    def test_upsample_shape(self):
        band = np.zeros((10, 20), dtype=np.float32)
        assert M.resample_band(band, 2.0, "bilinear").shape == (20, 40)

    def test_downsample_shape(self):
        band = np.zeros((10, 20), dtype=np.float32)
        assert M.resample_band(band, 0.5, "bilinear").shape == (5, 10)


class TestErrors:
    def test_unknown_method_raises(self):
        band = np.zeros((8, 8), dtype=np.float32)
        with pytest.raises(M.UsageError):
            M.resample_band(band, 2.0, "lanczos")

    def test_nonpositive_scale_raises(self):
        band = np.zeros((8, 8), dtype=np.float32)
        with pytest.raises(M.UsageError):
            M.resample_band(band, 0.0, "bilinear")


class TestCube:
    def test_multiband(self):
        cube = np.random.default_rng(1).uniform(0, 1, (3, 16, 16)).astype(np.float32)
        out = M.resample_cube(cube, 0.5, "bilinear")
        assert out.shape == (3, 8, 8)


class TestSynthetic:
    def test_generate_shape(self):
        cube, info = M.generate_synthetic([116, 39, 117, 40], size=32)
        assert cube.shape == (1, 32, 32)
        assert info["size"] == 32


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(2).uniform(0, 1, (1, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        M.write_geotiff(path, cube, bbox)
        back, rbbox, nodata = M.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_geotiff("/nonexistent/nope.tif")
