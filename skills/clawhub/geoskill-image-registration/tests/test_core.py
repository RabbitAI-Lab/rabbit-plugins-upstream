"""Core algorithm tests for image-registration."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestEstimateShift:
    def test_recovers_integer_shift(self):
        ref, target, info = mod.generate_synthetic(
            [116, 39, 117, 40], shift_y=4.0, shift_x=-6.0, seed=7,
        )
        dy, dx = mod.estimate_shift(ref, target)
        assert abs(dy - 4.0) < 0.15
        assert abs(dx - (-6.0)) < 0.15

    def test_recovers_subpixel_shift(self):
        ref, target, info = mod.generate_synthetic(
            [116, 39, 117, 40], shift_y=2.5, shift_x=-3.5, seed=11,
        )
        dy, dx = mod.estimate_shift(ref, target)
        assert abs(dy - 2.5) < 0.5
        assert abs(dx - (-3.5)) < 0.5

    def test_zero_shift(self):
        ref, _, _ = mod.generate_synthetic([116, 39, 117, 40], seed=3)
        dy, dx = mod.estimate_shift(ref, ref.copy())
        assert abs(dy) < 0.2
        assert abs(dx) < 0.2

    def test_shape_mismatch_raises(self):
        a = np.zeros((3, 32, 32), dtype=np.float32)
        b = np.zeros((3, 40, 40), dtype=np.float32)
        with pytest.raises(mod.ValidationError):
            mod.estimate_shift(a, b)


class TestApplyShift:
    def test_shape_preserved(self):
        cube = np.random.uniform(0, 1, (3, 32, 32)).astype(np.float32)
        out = mod.apply_shift(cube, 2.0, -3.0)
        assert out.shape == cube.shape

    def test_zero_shift_identity(self):
        cube = np.random.uniform(0, 1, (3, 32, 32)).astype(np.float32)
        out = mod.apply_shift(cube, 0.0, 0.0)
        np.testing.assert_allclose(out, cube, atol=1e-5)

    def test_2d_input(self):
        img = np.random.uniform(0, 1, (32, 32)).astype(np.float32)
        out = mod.apply_shift(img, 1.0, 1.0)
        assert out.shape == (32, 32)


class TestRegisterImage:
    def test_register_aligns_to_ref(self):
        ref, target, info = mod.generate_synthetic(
            [116, 39, 117, 40], shift_y=4.0, shift_x=-6.0, seed=7,
        )
        registered, report = mod.register_image(ref, target)
        assert registered.shape == ref.shape
        assert mod._interior_rmse(registered, ref) < 0.02

    def test_report_keys(self):
        ref, target, _ = mod.generate_synthetic([116, 39, 117, 40], seed=7)
        _, report = mod.register_image(ref, target)
        assert "estimated_shift_y" in report
        assert "estimated_shift_x" in report
        assert "shift_magnitude" in report
        assert report["shift_magnitude"] >= 0


class TestSynthetic:
    def test_shapes(self):
        ref, target, info = mod.generate_synthetic([116, 39, 117, 40])
        assert ref.shape == (3, 128, 128)
        assert target.shape == (3, 128, 128)
        assert info["true_shift"] == [4.0, -6.0]

    def test_target_differs_from_ref(self):
        ref, target, _ = mod.generate_synthetic([116, 39, 117, 40], seed=5)
        assert not np.allclose(ref, target)


class TestInteriorRmse:
    def test_identical_zero(self):
        a = np.random.uniform(0, 1, (3, 60, 60)).astype(np.float32)
        assert mod._interior_rmse(a, a) == 0.0


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
