"""Core algorithm tests for dinsar-coherence-analysis."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as dc


def _make_pair(seed=0, height=64, width=64, noise=0.05):
    """完全相关主从对：slave = master * exp(iφ) + 小噪声。"""
    rng = np.random.default_rng(seed)
    amp = rng.rayleigh(1.0, (height, width))
    master = (amp * np.exp(1j * rng.uniform(-np.pi, np.pi, (height, width)))).astype(np.complex64)
    phi = np.linspace(0, np.pi, width)[None, :].repeat(height, axis=0)
    slave = master * np.exp(1j * phi)
    slave = slave + (rng.normal(0, noise, master.shape) + 1j * rng.normal(0, noise, master.shape))
    return master, slave.astype(np.complex64)


class TestCoherence:
    def test_identical_high_coherence(self):
        m, s = _make_pair(seed=1)
        gamma, phase = dc.complex_coherence(m, s, looks_r=8, looks_a=4)
        assert gamma.shape == m.shape
        assert gamma.mean() > 0.85
        assert gamma.min() >= 0.0
        assert gamma.max() <= 1.0

    def test_independent_low_coherence(self):
        rng = np.random.default_rng(2)
        m = (rng.rayleigh(1.0, (64, 64)) * np.exp(1j * rng.uniform(-np.pi, np.pi, (64, 64)))).astype(np.complex64)
        s = (rng.rayleigh(1.0, (64, 64)) * np.exp(1j * rng.uniform(-np.pi, np.pi, (64, 64)))).astype(np.complex64)
        gamma, _ = dc.complex_coherence(m, s, looks_r=8, looks_a=8)
        # 完全去相关：相干性应显著低于相关对
        assert gamma.mean() < 0.4

    def test_separation_stable_vs_change(self):
        """变化区相干性显著低于稳定区。"""
        m, s, truth, info = dc.generate_synthetic([116, 39, 117, 40], seed=3)
        gamma, phase = dc.complex_coherence(m, s, looks_r=4, looks_a=4)
        stable = gamma[truth == 0]
        change = gamma[truth == 1]
        assert stable.mean() - change.mean() > 0.35
        assert stable.mean() > 0.7
        assert change.mean() < 0.6

    def test_phase_finite_wrapped(self):
        m, s = _make_pair(seed=4)
        _, phase = dc.complex_coherence(m, s, looks_r=4, looks_a=2)
        assert np.all(np.isfinite(phase))
        assert phase.min() >= -np.pi - 1e-3
        assert phase.max() <= np.pi + 1e-3

    def test_shape_mismatch_raises(self):
        m = np.ones((16, 16), dtype=np.complex64)
        s = np.ones((16, 8), dtype=np.complex64)
        with pytest.raises(dc.ValidationError):
            dc.complex_coherence(m, s)

    def test_zero_slave_no_nan(self):
        m = np.ones((16, 16), dtype=np.complex64)
        s = np.zeros((16, 16), dtype=np.complex64)
        gamma, phase = dc.complex_coherence(m, s)
        assert np.all(np.isfinite(gamma))
        assert np.all(np.isfinite(phase))


class TestStatistics:
    def test_stats_fields(self):
        gamma = np.random.uniform(0, 1, (32, 32)).astype(np.float32)
        stats = dc.coherence_statistics(gamma, [116, 39, 117, 40], coh_threshold=0.3)
        assert 0 <= stats["mean_coherence"] <= 1
        assert 0 <= stats["low_coherence_fraction"] <= 1
        assert stats["total_pixels"] == 1024
        assert stats["scene_area_km2"] > 0
        assert stats["low_coherence_area_km2"] >= 0

    def test_all_low_coherence(self):
        gamma = np.full((10, 10), 0.1, dtype=np.float32)
        stats = dc.coherence_statistics(gamma, [116, 39, 117, 40], coh_threshold=0.3)
        assert stats["low_coherence_fraction"] == pytest.approx(1.0)


class TestSynthetic:
    def test_shapes_and_types(self):
        m, s, truth, info = dc.generate_synthetic([116, 39, 117, 40])
        assert m.shape == (64, 64)
        assert s.shape == (64, 64)
        assert np.iscomplexobj(m)
        assert truth.sum() > 0
        assert 0 < info["change_fraction"] < 1

    def test_reproducible(self):
        m1, s1, _, _ = dc.generate_synthetic([116, 39, 117, 40], seed=9)
        m2, s2, _, _ = dc.generate_synthetic([116, 39, 117, 40], seed=9)
        np.testing.assert_array_equal(m1, m2)
        np.testing.assert_array_equal(s1, s2)


class TestIO:
    def test_complex_roundtrip(self, tmp_path):
        # 写一个 2 波段（实部/虚部）复 SLC
        c = (np.random.uniform(-1, 1, (16, 16)) + 1j * np.random.uniform(-1, 1, (16, 16)))
        cube = np.stack([c.real, c.imag]).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "slc.tif")
        dc.write_geotiff(path, cube, bbox)
        back, rbbox = dc.read_complex_geotiff(path)
        np.testing.assert_allclose(back.real, c.real, atol=1e-5)
        np.testing.assert_allclose(back.imag, c.imag, atol=1e-5)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(dc.UsageError):
            dc.read_complex_geotiff("/nonexistent/x.tif")
