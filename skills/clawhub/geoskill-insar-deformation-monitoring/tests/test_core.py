"""Core algorithm tests for insar-deformation-monitoring."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as insar


class TestInterferogram:
    def test_identical_slcs_zero_phase(self):
        rng = np.random.default_rng(0)
        amp = rng.uniform(0.5, 1.5, (32, 32))
        phi = rng.uniform(-np.pi, np.pi, (32, 32))
        slc = (amp * np.exp(1j * phi)).astype(np.complex64)
        ifg = insar.interferogram(slc, slc)
        # m·conj(m) 为正实数 → 相位=0
        np.testing.assert_allclose(ifg, 0.0, atol=1e-5)

    def test_known_phase_difference(self):
        amp = np.ones((16, 16), dtype=np.float32)
        master = amp * np.exp(1j * 0.0)
        slave = amp * np.exp(1j * 0.5)  # φ2 = 0.5
        ifg = insar.interferogram(master, slave)
        # angle(m·conj(s)) = φ1 - φ2 = -0.5
        np.testing.assert_allclose(ifg, -0.5, atol=1e-5)

    def test_shape_mismatch_raises(self):
        a = np.ones((8, 8), dtype=np.complex64)
        b = np.ones((8, 9), dtype=np.complex64)
        with pytest.raises(insar.ValidationError):
            insar.interferogram(a, b)


class TestCoherence:
    def test_identical_slcs_coherence_one(self):
        rng = np.random.default_rng(1)
        slc = (rng.uniform(0.5, 1.5, (32, 32))
               * np.exp(1j * rng.uniform(-np.pi, np.pi, (32, 32)))).astype(np.complex64)
        coh = insar.coherence(slc, slc, window=5)
        assert coh.min() >= 0.0
        assert coh.max() <= 1.0 + 1e-6
        np.testing.assert_allclose(coh.mean(), 1.0, atol=1e-4)

    def test_independent_slcs_low_coherence(self):
        rng = np.random.default_rng(2)
        m = (rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))).astype(np.complex64)
        s = (rng.normal(size=(64, 64)) + 1j * rng.normal(size=(64, 64))).astype(np.complex64)
        coh = insar.coherence(m, s, window=7)
        # 不相干噪声对的相干性应接近 0
        assert coh.mean() < 0.35

    def test_coherence_range(self):
        rng = np.random.default_rng(3)
        m = (rng.normal(size=(32, 32)) + 1j * rng.normal(size=(32, 32))).astype(np.complex64)
        s = m + 0.3 * (rng.normal(size=(32, 32)) + 1j * rng.normal(size=(32, 32)))
        coh = insar.coherence(m, s.astype(np.complex64), window=5)
        assert coh.min() >= 0.0
        assert coh.max() <= 1.0 + 1e-6


class TestPhaseToDeformation:
    def test_linear_relation(self):
        phase = np.array([0.0, np.pi, -np.pi, 2 * np.pi], dtype=np.float32)
        wl = 0.0555
        d = insar.phase_to_deformation(phase, wl)
        expected = phase * wl / (4 * np.pi)
        np.testing.assert_allclose(d, expected, atol=1e-7)

    def test_full_cycle_is_half_wavelength(self):
        # 2π 相位 → λ/2 形变
        d = insar.phase_to_deformation(np.array([2 * np.pi], dtype=np.float32), 0.0555)
        np.testing.assert_allclose(d[0], 0.0555 / 2.0, atol=1e-6)

    def test_bad_wavelength_raises(self):
        with pytest.raises(insar.UsageError):
            insar.phase_to_deformation(np.zeros((4, 4)), 0.0)


class TestSyntheticRecovery:
    def test_recovered_deformation_correlates_with_truth(self):
        master, slave, info = insar.generate_synthetic(
            [116, 39, 117, 40], wavelength=0.0555, noise_level=0.25, seed=7,
        )
        deform, coh, params = insar.insar_process(
            master, slave, wavelength=0.0555, window=5,
        )
        truth = info["deformation_truth"]
        corr = np.corrcoef(deform.ravel(), truth.ravel())[0, 1]
        # ifg = -(φ_def) → 符号相反，取绝对值
        assert abs(corr) > 0.85

    def test_deformation_magnitude_consistent(self):
        master, slave, info = insar.generate_synthetic(
            [116, 39, 117, 40], wavelength=0.0555, noise_level=0.2, seed=11,
        )
        deform, coh, params = insar.insar_process(master, slave, 0.0555, window=5)
        truth = info["deformation_truth"]
        # 形变量级一致（同数量级，cm 级）
        assert abs(np.std(deform) - np.std(truth)) < np.std(truth) * 1.5

    def test_shapes(self):
        master, slave, info = insar.generate_synthetic([116, 39, 117, 40])
        assert master.shape == (64, 64)
        assert slave.shape == (64, 64)
        assert info["deformation_truth"].shape == (64, 64)


class TestSlcFromCube:
    def test_four_bands_complex(self):
        cube = np.random.default_rng(4).normal(size=(4, 8, 8)).astype(np.float32)
        m, s = insar.slc_from_cube(cube)
        assert m.dtype == np.complex64
        np.testing.assert_allclose(m.real, cube[0])
        np.testing.assert_allclose(m.imag, cube[1])
        np.testing.assert_allclose(s.real, cube[2])
        np.testing.assert_allclose(s.imag, cube[3])

    def test_two_bands_real_pair(self):
        cube = np.ones((2, 4, 4), dtype=np.float32)
        m, s = insar.slc_from_cube(cube)
        np.testing.assert_allclose(m.imag, 0.0)

    def test_one_band_raises(self):
        cube = np.ones((1, 4, 4), dtype=np.float32)
        with pytest.raises(insar.ValidationError):
            insar.slc_from_cube(cube)


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(5).uniform(-0.01, 0.01, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        insar.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        back, rbbox = insar.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_file_raises(self):
        with pytest.raises(insar.UsageError):
            insar.read_geotiff("/nonexistent/path/file.tif")
