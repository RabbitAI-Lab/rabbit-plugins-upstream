"""Core algorithm tests for soil-moisture-mapping — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestThermalInertia:
    def test_ati_higher_when_wet(self):
        # wet soil: low albedo, small diurnal range -> high ATI
        wet = mod.apparent_thermal_inertia(np.array([[0.1]]), np.array([[295.0]]), np.array([[292.0]]))
        dry = mod.apparent_thermal_inertia(np.array([[0.3]]), np.array([[310.0]]), np.array([[290.0]]))
        assert wet[0, 0] > dry[0, 0]

    def test_moisture_monotonic_with_ati(self):
        ati = np.array([[0.02, 0.1, 0.5]], dtype=np.float32)
        mv = mod.thermal_inertia_moisture(ati)
        assert mv[0, 0] < mv[0, 1] < mv[0, 2]

    def test_moisture_bounded(self):
        ati = np.linspace(0, 5, 50).astype(np.float32).reshape(1, -1)
        mv = mod.thermal_inertia_moisture(ati, mv_max=0.45)
        assert mv.min() >= 0.0 and mv.max() <= 0.45

    def test_zero_amp_guard(self):
        ati = mod.apparent_thermal_inertia(np.array([[0.2]]), np.array([[300.0]]), np.array([[300.0]]))
        assert np.isfinite(ati).all()


class TestDubois:
    def test_forward_monotonic_with_moisture(self):
        mv = np.array([[0.05, 0.2, 0.4]], dtype=np.float32)
        sigma = mod.dubois_forward(mv)
        assert sigma[0, 0] < sigma[0, 1] < sigma[0, 2]  # wetter -> stronger backscatter

    def test_invert_recovers_forward(self):
        mv_in = np.array([[0.05, 0.15, 0.30]], dtype=np.float32)
        sigma = mod.dubois_forward(mv_in)
        mv_out = mod.dubois_invert(sigma)
        np.testing.assert_allclose(mv_out, mv_in, atol=1e-3)

    def test_invert_monotonic_with_backscatter(self):
        sigma = np.array([[1e-4, 1e-3, 1e-2]], dtype=np.float32)
        mv = mod.dubois_invert(sigma)
        assert mv[0, 0] < mv[0, 1] < mv[0, 2]

    def test_linear_db_roundtrip(self):
        sigma = np.array([[0.01, 0.001]], dtype=np.float32)
        db = mod.linear_to_db(sigma)
        np.testing.assert_allclose(db[0, 0], -20.0, atol=1e-3)
        np.testing.assert_allclose(db[0, 1], -30.0, atol=1e-3)


class TestDroughtGrade:
    def test_grade_thresholds(self):
        mv = np.array([[0.35, 0.25, 0.15, 0.05]], dtype=np.float32)
        grade = mod.drought_grade(mv)
        assert grade[0, 0] == 0  # wet
        assert grade[0, 1] == 1  # mild
        assert grade[0, 2] == 2  # moderate
        assert grade[0, 3] == 3  # severe


class TestEstimatePipeline:
    def _data(self):
        cube, packed = mod.generate_synthetic([116, 39, 117, 40])
        return cube, packed

    def test_wet_side_moister_than_dry(self):
        cube, packed = self._data()
        albedo, t_day, t_night, sigma_vv = cube[0], cube[1], cube[2], cube[3]
        res = mod.estimate_moisture(albedo, t_day, t_night, sigma_vv, method="combined")
        mv = res["mv"]
        h, w = mv.shape
        wet_col = mv[:, :int(w * 0.2)].mean()   # left = wet
        dry_col = mv[:, int(w * 0.8):].mean()    # right = dry
        assert wet_col > dry_col
        assert mv.min() >= 0.0

    def test_dubois_matches_truth_trend(self):
        cube, packed = self._data()
        sigma_vv = cube[3]
        mv_sar = mod.dubois_invert(sigma_vv)
        mv_true = packed["mv_true"]
        # correlation between SAR-retrieved and truth should be strongly positive
        corr = np.corrcoef(mv_sar.ravel(), mv_true.ravel())[0, 1]
        assert corr > 0.8

    def test_method_choice(self):
        cube, _ = self._data()
        a, td, tn, sv = cube[0], cube[1], cube[2], cube[3]
        ti = mod.estimate_moisture(a, td, tn, sv, method="thermal-inertia")
        sar = mod.estimate_moisture(a, td, tn, sv, method="dubois-sar")
        comb = mod.estimate_moisture(a, td, tn, sv, method="combined")
        # combined is the mean of the two
        np.testing.assert_allclose(comb["mv"], 0.5 * ti["mv"] + 0.5 * sar["mv"], atol=1e-5)

    def test_unknown_method_raises(self):
        cube, _ = self._data()
        with pytest.raises(mod.UsageError):
            mod.estimate_moisture(cube[0], cube[1], cube[2], cube[3], method="bogus")
