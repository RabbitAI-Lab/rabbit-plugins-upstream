"""Core algorithm tests for image-fusion-pan-sharpening."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBrovey:
    def test_brovey_band_sum_equals_pan(self):
        """Brovey 性质：融合后各波段之和等于 PAN（注入的能量守恒）。"""
        ms_lr = np.random.uniform(0.1, 0.5, (3, 16, 16)).astype(np.float32)
        pan = np.random.uniform(0.1, 0.6, (1, 32, 32)).astype(np.float32)
        fused, params = mod.pansharpen(ms_lr, pan, method="brovey", scale=2)
        assert fused.shape == (3, 32, 32)
        band_sum = fused.sum(axis=0)
        np.testing.assert_allclose(band_sum, pan[0], rtol=1e-3, atol=1e-3)

    def test_brovey_nonnegative(self):
        ms_lr = np.random.uniform(0.05, 0.4, (3, 8, 8)).astype(np.float32)
        pan = np.random.uniform(0.05, 0.5, (1, 16, 16)).astype(np.float32)
        fused, _ = mod.pansharpen(ms_lr, pan, method="brovey", scale=2)
        assert fused.min() >= 0.0


class TestIHS:
    def test_ihs_mean_equals_pan(self):
        """IHS 性质：融合后各波段均值等于 PAN（强度被 PAN 替换）。"""
        ms_lr = np.random.uniform(0.1, 0.5, (3, 16, 16)).astype(np.float32)
        pan = np.random.uniform(0.2, 0.6, (1, 32, 32)).astype(np.float32)
        fused, params = mod.pansharpen(ms_lr, pan, method="ihs", scale=2)
        assert fused.shape == (3, 32, 32)
        band_mean = fused.mean(axis=0)
        # clip 到 >=0 会引入小偏差，但绝大多数像元不受影响
        np.testing.assert_allclose(band_mean, pan[0], rtol=1e-2, atol=1e-2)

    def test_ihs_shape_scale4(self):
        ms_lr = np.random.uniform(0.1, 0.5, (3, 8, 8)).astype(np.float32)
        pan = np.random.uniform(0.2, 0.6, (1, 32, 32)).astype(np.float32)
        fused, params = mod.pansharpen(ms_lr, pan, method="ihs", scale=4)
        assert fused.shape == (3, 32, 32)
        assert params["scale"] == 4


class TestValidation:
    def test_bad_method_raises(self):
        ms_lr = np.random.uniform(0.1, 0.5, (3, 8, 8)).astype(np.float32)
        pan = np.random.uniform(0.1, 0.5, (1, 16, 16)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.pansharpen(ms_lr, pan, method="bogus", scale=2)

    def test_bad_ms_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.pansharpen(np.ones((8, 8), dtype=np.float32),
                           np.ones((1, 16, 16), dtype=np.float32), scale=2)

    def test_2d_pan_accepted(self):
        ms_lr = np.random.uniform(0.1, 0.5, (3, 8, 8)).astype(np.float32)
        pan2d = np.random.uniform(0.1, 0.5, (16, 16)).astype(np.float32)
        fused, _ = mod.pansharpen(ms_lr, pan2d, method="brovey", scale=2)
        assert fused.shape == (3, 16, 16)


class TestSynthetic:
    def test_shapes(self):
        ms_lr, pan_hr, info = mod.generate_synthetic([116, 39, 117, 40], scale=2, bands=3)
        assert ms_lr.shape == (3, 64, 64)
        assert pan_hr.shape == (1, 128, 128)

    def test_fusion_runs_on_synthetic(self):
        ms_lr, pan_hr, info = mod.generate_synthetic([116, 39, 117, 40], scale=2, seed=7)
        fused, params = mod.pansharpen(ms_lr, pan_hr, method="brovey", scale=2)
        assert fused.shape[1:] == pan_hr.shape[1:]
        assert float(np.mean(fused)) > 0.0


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
