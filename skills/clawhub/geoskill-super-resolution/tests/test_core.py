"""Core algorithm tests for super-resolution."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBicubic:
    def test_scale2_shape(self):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        out = mod.bicubic_upscale(cube, 2)
        assert out.shape == (3, 32, 32)

    def test_scale4_shape(self):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        out = mod.bicubic_upscale(cube, 4)
        assert out.shape == (3, 64, 64)

    def test_constant_stays_constant(self):
        cube = np.full((3, 16, 16), 0.4, dtype=np.float32)
        out = mod.bicubic_upscale(cube, 2)
        np.testing.assert_allclose(out, 0.4, atol=1e-4)

    def test_bad_scale_raises(self):
        with pytest.raises(mod.UsageError):
            mod.bicubic_upscale(np.ones((1, 8, 8), dtype=np.float32), 3)


class TestDownsample:
    def test_shape(self):
        cube = np.random.uniform(0, 1, (3, 32, 32)).astype(np.float32)
        out = mod.downsample(cube, 2)
        assert out.shape == (3, 16, 16)


class TestPSNR:
    def test_identical_is_inf(self):
        a = np.full((4, 4), 0.5, dtype=np.float32)
        assert mod.psnr(a, a) == float("inf")

    def test_known_value(self):
        a = np.array([0.5, 0.5], dtype=np.float64)
        b = np.array([0.5, 0.6], dtype=np.float64)
        # mse = 0.005 -> psnr = 10*log10(1/0.005) = 23.01 dB
        assert abs(mod.psnr(a, b) - 23.0103) < 0.01

    def test_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.psnr(np.ones((4, 4)), np.ones((4, 5)))


class TestSuperResolve:
    def test_shape_and_params(self):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        out, params = mod.super_resolve(cube, scale=2, method="bicubic")
        assert out.shape == (3, 32, 32)
        assert params["scale"] == 2
        assert params["method"] == "bicubic"

    def test_bad_method_raises(self):
        with pytest.raises(mod.UsageError):
            mod.super_resolve(np.ones((1, 8, 8), dtype=np.float32), scale=2, method="espcn")


class TestSynthetic:
    def test_shapes_scale2(self):
        lowres, truth, info = mod.generate_synthetic([116, 39, 117, 40], scale=2)
        assert truth.shape == (3, 128, 128)
        assert lowres.shape == (3, 64, 64)
        assert info["scale"] == 2

    def test_shapes_scale4(self):
        lowres, truth, info = mod.generate_synthetic([116, 39, 117, 40], scale=4)
        assert truth.shape == (3, 128, 128)
        assert lowres.shape == (3, 32, 32)

    def test_super_resolve_psnr_reasonable(self):
        lowres, truth, info = mod.generate_synthetic([116, 39, 117, 40], scale=2, seed=7)
        upscaled, _ = mod.super_resolve(lowres, scale=2)
        assert upscaled.shape == truth.shape
        p = mod.psnr(upscaled, truth, max_val=1.0)
        assert p > 20.0


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        read_back, read_bbox = mod.read_geotiff(path)
        assert read_back.shape == cube.shape
        np.testing.assert_allclose(read_bbox, bbox, atol=1e-6)
        np.testing.assert_allclose(read_back, cube, atol=1e-5)

    def test_read_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/path/file.tif")
