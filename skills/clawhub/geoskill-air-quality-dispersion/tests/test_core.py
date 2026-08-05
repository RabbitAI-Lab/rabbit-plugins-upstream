"""Core algorithm tests for air-quality-dispersion (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestDispersionParams:
    def test_sigma_grows_with_distance(self):
        x = np.array([0.1, 1.0, 10.0], dtype=np.float32)
        sy, sz = M.dispersion_params(x, "D")
        assert sy[0] < sy[1] < sy[2]
        assert sz[0] < sz[1] < sz[2]

    def test_stable_less_dispersion(self):
        """F 类（稳定）比 A 类（不稳定）扩散弱 → σ 更小。"""
        x = np.array([1.0], dtype=np.float32)
        sy_a, sz_a = M.dispersion_params(x, "A")
        sy_f, sz_f = M.dispersion_params(x, "F")
        assert float(sy_f[0]) < float(sy_a[0])
        assert float(sz_f[0]) < float(sz_a[0])

    def test_unknown_stability_raises(self):
        with pytest.raises(M.UsageError):
            M.dispersion_params(np.array([1.0]), "X")


class TestGaussianPlume:
    def _make(self):
        x = np.full((1, 100), 1000.0, dtype=np.float32)
        y = np.linspace(-500, 500, 100).astype(np.float32)[np.newaxis, :]
        sy = np.full_like(x, 80.0)
        sz = np.full_like(x, 40.0)
        return x, y, sy, sz

    def test_centerline_maximum(self):
        x, y, sy, sz = self._make()
        conc = M.gaussian_plume(100.0, 3.0, x, y, 50.0, sy, sz)
        center = conc.shape[1] // 2
        assert conc[0, center] > conc[0, 0]
        assert conc[0, center] > conc[0, -1]

    def test_decays_with_distance(self):
        """下风向浓度随距离衰减。"""
        y = np.zeros((1, 1), dtype=np.float32)
        x1 = np.full((1, 1), 500.0, dtype=np.float32)
        x2 = np.full((1, 1), 5000.0, dtype=np.float32)
        sy1, sz1 = M.dispersion_params(x1 / 1000.0, "D")
        sy2, sz2 = M.dispersion_params(x2 / 1000.0, "D")
        c1 = M.gaussian_plume(100.0, 3.0, x1, y, 50.0, sy1, sz1)
        c2 = M.gaussian_plume(100.0, 3.0, x2, y, 50.0, sy2, sz2)
        assert float(c1[0, 0]) > float(c2[0, 0])

    def test_higher_Q_higher_conc(self):
        x, y, sy, sz = self._make()
        c1 = M.gaussian_plume(100.0, 3.0, x, y, 50.0, sy, sz)
        c2 = M.gaussian_plume(200.0, 3.0, x, y, 50.0, sy, sz)
        np.testing.assert_allclose(c2, c1 * 2.0, rtol=1e-5)

    def test_higher_wind_lower_conc(self):
        x, y, sy, sz = self._make()
        c_slow = M.gaussian_plume(100.0, 2.0, x, y, 50.0, sy, sz)
        c_fast = M.gaussian_plume(100.0, 6.0, x, y, 50.0, sy, sz)
        assert float(c_slow.mean()) > float(c_fast.mean())

    def test_nonnegative(self):
        x, y, sy, sz = self._make()
        conc = M.gaussian_plume(100.0, 3.0, x, y, 50.0, sy, sz)
        assert conc.min() >= 0.0


class TestTerrainCorrection:
    def test_flat_factor_one(self):
        tcf = M.terrain_correction(np.full((8, 8), 100.0), source_elev=100.0, base_H=50.0)
        np.testing.assert_allclose(tcf, 1.0, atol=1e-5)

    def test_higher_terrain_higher_factor(self):
        tcf = M.terrain_correction(np.full((4, 4), 200.0), source_elev=100.0, base_H=50.0)
        assert float(tcf.mean()) > 1.0

    def test_lower_terrain_lower_factor(self):
        tcf = M.terrain_correction(np.full((4, 4), 50.0), source_elev=100.0, base_H=50.0)
        assert float(tcf.mean()) < 1.0

    def test_clipped(self):
        tcf = M.terrain_correction(np.full((4, 4), 10000.0), source_elev=0.0, base_H=50.0)
        assert tcf.max() <= 3.0
