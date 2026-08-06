"""Core algorithm tests for radiometric-calibration."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestDnToRadiance:
    def test_linear_relationship(self):
        dn = np.array([[0.0, 100.0, 1000.0]], dtype=np.float32)
        rad = mod.dn_to_radiance(dn, gain=0.01, bias=5.0)
        expected = np.clip(0.01 * dn + 5.0, 0.0, None)
        np.testing.assert_allclose(rad, expected, atol=1e-5)

    def test_clipped_nonnegative(self):
        dn = np.array([[0.0, 10.0]], dtype=np.float32)
        rad = mod.dn_to_radiance(dn, gain=0.01, bias=-100.0)
        assert rad.min() >= 0.0


class TestRadianceToReflectance:
    def test_range_01(self):
        rad = np.random.uniform(0, 500, (16, 16)).astype(np.float32)
        rho = mod.radiance_to_reflectance(rad, esun=1550.0, solar_zenith_deg=30.0)
        assert rho.min() >= 0.0
        assert rho.max() <= 1.0

    def test_monotonic_in_radiance(self):
        rho_low = mod.radiance_to_reflectance(np.array([[10.0]], dtype=np.float32), 1550.0, 30.0)
        rho_high = mod.radiance_to_reflectance(np.array([[100.0]], dtype=np.float32), 1550.0, 30.0)
        assert rho_high[0, 0] > rho_low[0, 0]

    def test_known_value(self):
        # rho = pi*L*d^2/(ESUN*cos(0)) = pi*ESUN/(ESUN*1) = pi -> clipped to 1
        rho = mod.radiance_to_reflectance(np.array([[1550.0]], dtype=np.float32), 1550.0, 0.0)
        np.testing.assert_allclose(rho[0, 0], 1.0, atol=1e-5)


class TestCalibrate:
    def test_radiance_shape_and_value(self):
        cube = np.random.uniform(500, 8000, (4, 32, 32)).astype(np.float32)
        out, params = mod.calibrate(cube, sensor="generic", output_type="toa_radiance")
        assert out.shape == cube.shape
        assert params["output_type"] == "toa_radiance"
        assert out.min() >= 0.0

    def test_reflectance_range_01(self):
        cube = np.random.uniform(500, 8000, (4, 32, 32)).astype(np.float32)
        out, _ = mod.calibrate(cube, sensor="generic", output_type="toa_reflectance")
        assert out.min() >= 0.0
        assert out.max() <= 1.0
        assert len(out.shape) == 3

    def test_unknown_sensor_raises(self):
        cube = np.random.uniform(0, 1, (3, 8, 8)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.calibrate(cube, sensor="unknown")

    def test_bad_output_type_raises(self):
        cube = np.random.uniform(0, 1, (3, 8, 8)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.calibrate(cube, sensor="generic", output_type="bogus")

    def test_too_many_bands_raises(self):
        cube = np.random.uniform(0, 1, (10, 8, 8)).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.calibrate(cube, sensor="generic")


class TestSynthetic:
    def test_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], "landsat8")
        assert cube.ndim == 3
        assert cube.shape[0] == 6
        assert cube.shape[1] == 128

    def test_calibration_recovers_truth(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], "generic", seed=7)
        out, _ = mod.calibrate(cube, sensor="generic", output_type="toa_reflectance")
        assert out.min() >= 0.0 and out.max() <= 1.0
        mean_refl = float(np.mean(out))
        assert 0.01 < mean_refl < 0.6


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
