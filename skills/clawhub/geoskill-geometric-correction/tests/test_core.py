"""Core algorithm tests for geometric-correction."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestPolyFit:
    def test_recovers_known_affine(self):
        rng = np.random.default_rng(0)
        src = rng.uniform(0, 100, (10, 2))  # pixel (col, row)
        dst = np.column_stack([
            116.0 + 0.01 * src[:, 0] + 0.002 * src[:, 1],
            40.0 - 0.002 * src[:, 0] - 0.01 * src[:, 1],
        ])
        coeffs = mod.fit_poly(src, dst, order=1)
        pred = mod.eval_poly(coeffs, src)
        np.testing.assert_allclose(pred, dst, atol=1e-8)
        rms = mod.gcp_rms(coeffs, src, dst)
        assert rms["rms_total"] < 1e-8

    def test_eval_poly_order1_values(self):
        coeffs = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
        pts = np.array([[1, 1], [2, 0]], dtype=np.float64)
        out = mod.eval_poly(coeffs, pts)
        np.testing.assert_allclose(out, [[6, 15], [5, 14]])

    def test_order2_insufficient_gcps_raises(self):
        src = np.array([[0, 0], [1, 0], [0, 1], [1, 1]], dtype=np.float64)
        dst = src.copy()
        with pytest.raises(mod.ValidationError):
            mod.fit_poly(src, dst, order=2)  # needs >= 6

    def test_bad_order_raises(self):
        with pytest.raises(mod.UsageError):
            mod.poly_design(np.array([[0.0, 0.0]]), order=3)

    def test_min_gcp_table(self):
        assert mod.MIN_GCPS[1] == 3
        assert mod.MIN_GCPS[2] == 6


class TestResample:
    def test_constant_image_stays_constant(self):
        cube = np.full((2, 30, 30), 0.7, dtype=np.float32)
        g = np.array([[0, 0], [20, 0], [0, 20], [20, 20], [10, 10]], dtype=np.float64)
        inv = mod.fit_poly(g, g, order=1)  # geo -> pixel identity
        out = mod.resample_cube(cube, inv, [0, 0, 20, 20], out_h=20, out_w=20)
        assert out.shape == (2, 20, 20)
        np.testing.assert_allclose(out, 0.7, atol=1e-5)


class TestCorrectGeometry:
    def test_synthetic_order1_reconstructs(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, gcp_pix, gcp_geo, info = mod.generate_synthetic(bbox, order=1, seed=7)
        corrected, report = mod.correct_geometry(cube, gcp_pix, gcp_geo, bbox, order=1)
        assert corrected.shape == cube.shape
        assert report["rms"]["rms_total"] >= 0
        ideal = info["_ideal"]
        band0 = corrected[0]
        valid = band0 > -9000
        rmse = float(np.sqrt(np.mean((band0[valid] - ideal[valid]) ** 2)))
        assert rmse < 0.05

    def test_synthetic_order2(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, gcp_pix, gcp_geo, info = mod.generate_synthetic(bbox, order=2, seed=7)
        corrected, report = mod.correct_geometry(cube, gcp_pix, gcp_geo, bbox, order=2)
        assert report["n_gcp"] >= 6
        assert corrected.shape == cube.shape


class TestSynthetic:
    def test_shapes(self):
        bbox = [116, 39, 117, 40]
        cube, gp, gg, info = mod.generate_synthetic(bbox)
        assert cube.shape == (3, 128, 128)
        assert gp.shape[0] == 16  # 4x4 grid
        assert gp.shape == gg.shape
        assert info["n_gcp"] == 16


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
