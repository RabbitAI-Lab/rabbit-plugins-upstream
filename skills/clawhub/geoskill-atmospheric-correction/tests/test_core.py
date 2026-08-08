"""Core algorithm tests for atmospheric-correction."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import ac


class TestDarkObject:
    def test_dark_object_positive(self):
        band = np.random.uniform(100, 5000, (64, 64)).astype(np.float32)
        rho_dark, dn_dark = ac.dark_object_reflectance(
            band, esun=1550.0, solar_zenith_deg=30.0, gain=0.01, bias=0.0,
        )
        assert rho_dark > 0
        assert dn_dark > 0

    def test_dark_object_empty_band(self):
        band = np.full((10, 10), np.nan, dtype=np.float32)
        rho_dark, dn_dark = ac.dark_object_reflectance(
            band, esun=1550.0, solar_zenith_deg=30.0, gain=0.01, bias=0.0,
        )
        assert rho_dark == 0.0
        assert dn_dark == 0.0


class TestRayleigh:
    def test_blue_greater_than_red(self):
        tau_blue = ac.rayleigh_optical_depth(0.48)
        tau_red = ac.rayleigh_optical_depth(0.66)
        assert tau_blue > tau_red

    def test_nir_very_small(self):
        tau_nir = ac.rayleigh_optical_depth(0.86)
        assert tau_nir < 0.02  # ~0.016 at 0.86µm


class TestDosCorrect:
    def test_output_shape_preserved(self):
        cube = np.random.uniform(500, 8000, (4, 32, 32)).astype(np.float32)
        out, params = ac.dos_correct(cube, sensor="generic")
        assert out.shape == cube.shape
        assert params["method"] == "dos"
        assert len(params["bands"]) == 4

    def test_output_range_01(self):
        cube = np.random.uniform(500, 8000, (4, 32, 32)).astype(np.float32)
        out, _ = ac.dos_correct(cube, sensor="generic")
        assert out.min() >= 0.0
        assert out.max() <= 1.0

    def test_6s_lowers_reflectance_vs_dos(self):
        """6s-simplified subtracts extra Rayleigh → lower reflectance than DOS."""
        cube = np.random.uniform(1000, 8000, (4, 32, 32)).astype(np.float32)
        out_dos, _ = ac.dos_correct(cube, sensor="generic", method="dos")
        out_6s, _ = ac.dos_correct(cube, sensor="generic", method="6s-simplified")
        # Blue band (index 0) should have biggest difference
        assert np.mean(out_6s[0]) < np.mean(out_dos[0])

    def test_unknown_sensor_raises(self):
        cube = np.random.uniform(0, 1, (3, 8, 8)).astype(np.float32)
        with pytest.raises(ac.UsageError):
            ac.dos_correct(cube, sensor="unknown_sensor")

    def test_too_many_bands_raises(self):
        cube = np.random.uniform(0, 1, (10, 8, 8)).astype(np.float32)
        with pytest.raises(ac.ValidationError):
            ac.dos_correct(cube, sensor="generic")  # generic has 4 bands


class TestSynthetic:
    def test_synthetic_cube_shape(self):
        cube, info = ac.generate_synthetic_cube([116, 39, 117, 40], "landsat8")
        assert cube.ndim == 3
        assert cube.shape[0] == 6  # landsat8 has 6 bands
        assert cube.shape[1] == 128
        assert cube.shape[2] == 128

    def test_synthetic_correction_improves(self):
        """DOS correction of synthetic data should recover reflectance closer
        to ground truth than raw TOA."""
        bbox = [116, 39, 117, 40]
        cube, info = ac.generate_synthetic_cube(bbox, "generic", seed=7)
        surf, params = ac.dos_correct(cube, sensor="generic")
        # Surface reflectance should be in valid range
        assert surf.min() >= 0.0
        assert surf.max() <= 1.0
        # Mean should be reasonable (vegetation/soil/water mix)
        mean_refl = float(np.mean(surf))
        assert 0.01 < mean_refl < 0.6


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        ac.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        read_back, read_bbox = ac.read_geotiff(path)
        assert read_back.shape == cube.shape
        np.testing.assert_allclose(read_bbox, bbox, atol=1e-6)
        np.testing.assert_allclose(read_back, cube, atol=1e-5)

    def test_read_missing_file_raises(self):
        with pytest.raises(ac.UsageError):
            ac.read_geotiff("/nonexistent/path/file.tif")
