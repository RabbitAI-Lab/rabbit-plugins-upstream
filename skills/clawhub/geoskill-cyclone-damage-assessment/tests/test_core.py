"""Core algorithm tests for cyclone-damage-assessment."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as cy


class TestHollandWind:
    def test_peak_at_rmax(self):
        """最大风速出现在 r=Rmax 处，且等于 Vmax。"""
        vmax, rmax = 50.0, 30000.0
        r = np.array([rmax])
        v = cy.holland_wind_speed(r, vmax, rmax, b=1.5)
        assert abs(v[0] - vmax) < 1e-3
        # 邻近半径处都低于 Vmax
        rs = np.linspace(2000, 120000, 200)
        vs = cy.holland_wind_speed(rs, vmax, rmax, b=1.5)
        assert vs.max() <= vmax + 1e-3
        assert abs(vs.max() - vmax) < 1.0

    def test_eye_is_calm(self):
        """风眼内部风速迅速衰减到接近 0。"""
        v_eye = cy.holland_wind_speed(np.array([500.0]), 50.0, 30000.0)[0]
        assert v_eye < 1.0

    def test_decays_outward(self):
        v_near = cy.holland_wind_speed(np.array([30000.0]), 50.0, 30000.0)[0]
        v_far = cy.holland_wind_speed(np.array([120000.0]), 50.0, 30000.0)[0]
        assert v_far < v_near

    def test_monotonic_in_vmax(self):
        r = np.array([30000.0, 60000.0])
        v50 = cy.holland_wind_speed(r, 50.0, 30000.0)
        v70 = cy.holland_wind_speed(r, 70.0, 30000.0)
        assert np.all(v70 > v50)

    def test_invalid_params_raise(self):
        with pytest.raises(cy.ValidationError):
            cy.holland_wind_speed(np.array([1000.0]), -5.0, 30000.0)
        with pytest.raises(cy.ValidationError):
            cy.holland_wind_speed(np.array([1000.0]), 50.0, 0.0)


class TestVulnerability:
    def test_half_at_v50(self):
        dr = cy.vulnerability_curve(np.array([40.0]), v50=40.0)
        assert abs(dr[0] - 0.5) < 1e-6

    def test_monotonic_and_bounded(self):
        w = np.linspace(0, 100, 50)
        dr = cy.vulnerability_curve(w, v50=40.0, k=0.12)
        assert dr.min() >= 0.0 and dr.max() <= 1.0
        assert np.all(np.diff(dr) >= -1e-9)
        assert dr[0] < 0.1 and dr[-1] > 0.9


class TestSurge:
    def test_increases_with_wind(self):
        s = cy.storm_surge(np.array([0.0, 20.0, 50.0]))
        assert s[0] == 0.0
        assert s[2] > s[1] > s[0]


class TestCombinedDamage:
    def test_bounded_and_monotonic(self):
        rng = np.random.default_rng(0)
        dw = rng.uniform(0, 1, (16, 16))
        pr = rng.uniform(0, 100, (16, 16))
        sg = rng.uniform(0, 5, (16, 16))
        base = cy.combined_damage(dw, pr, sg)
        assert base.min() >= 0.0 and base.max() <= 1.0
        more_wind = cy.combined_damage(np.clip(dw + 0.5, 0, 1), pr, sg)
        assert more_wind.mean() >= base.mean() - 1e-9

    def test_bad_weights_raise(self):
        z = np.zeros((4, 4))
        with pytest.raises(cy.ValidationError):
            cy.combined_damage(z, z, z, weights=(0.0, 0.0, 0.0))


class TestLoss:
    def test_loss_equals_dr_times_exposure(self):
        dr = np.full((10, 10), 0.3, dtype=np.float32)
        ex = np.full((10, 10), 1000.0, dtype=np.float32)
        loss = cy.estimate_loss(dr, ex)
        assert abs(float(loss.sum()) - 0.3 * 1000.0 * 100) < 1e-2

    def test_loss_monotonic_in_exposure(self):
        dr = np.full((8, 8), 0.5, dtype=np.float32)
        l1 = cy.estimate_loss(dr, np.full((8, 8), 100.0)).sum()
        l2 = cy.estimate_loss(dr, np.full((8, 8), 200.0)).sum()
        assert l2 > l1

    def test_shape_mismatch_raises(self):
        with pytest.raises(cy.ValidationError):
            cy.estimate_loss(np.zeros((4, 4)), np.zeros((4, 5)))


class TestSynthetic:
    def test_shapes_nonneg(self):
        layers, info = cy.generate_synthetic([120, 25, 121, 26])
        assert layers["exposure"].shape == (64, 64)
        assert layers["exposure"].min() >= 0.0
        assert layers["precip"].min() >= 0.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [120.0, 25.0, 121.0, 26.0]
        p = str(tmp_path / "c.tif")
        cy.write_geotiff(p, cube, bbox)
        back, bb = cy.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(cy.UsageError):
            cy.read_geotiff("/nonexistent/c.tif")
