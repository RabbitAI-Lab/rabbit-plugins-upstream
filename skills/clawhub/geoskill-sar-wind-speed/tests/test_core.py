"""Core algorithm tests for sar-wind-speed."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestAzimuthModulation:
    def test_upwind_greater_than_cross_greater_than_down(self):
        m1, m2 = 0.25, 0.10
        up = mod.azimuth_modulation(0.0, m1, m2)      # 迎风
        cross = mod.azimuth_modulation(90.0, m1, m2)  # 侧风
        down = mod.azimuth_modulation(180.0, m1, m2)  # 顺风
        assert up > cross > down

    def test_value_at_zero(self):
        # M(0) = 1 + m1 + m2
        assert mod.azimuth_modulation(0.0, 0.25, 0.10) == pytest.approx(1.35)


class TestCmodForward:
    def test_monotonic_in_wind(self):
        s5 = mod.cmod_sigma0_db(5.0, 45.0, 40.0, "cmod5")
        s10 = mod.cmod_sigma0_db(10.0, 45.0, 40.0, "cmod5")
        s20 = mod.cmod_sigma0_db(20.0, 45.0, 40.0, "cmod5")
        assert s5 < s10 < s20

    def test_typical_magnitude(self):
        # θ=40°, U=10 m/s 的 C 波段 σ⁰ 典型量级约 -8 dB
        s = mod.cmod_sigma0_db(10.0, 0.0, 40.0, "cmod5")
        assert -15.0 < s < 0.0

    def test_incidence_reduces_backscatter(self):
        # 入射角增大 → 后向散射降低（基线项）
        s30 = mod.cmod_sigma0_db(10.0, 45.0, 30.0, "cmod5")
        s50 = mod.cmod_sigma0_db(10.0, 45.0, 50.0, "cmod5")
        assert s30 > s50

    def test_unknown_model(self):
        with pytest.raises(mod.UsageError):
            mod.cmod_sigma0_db(10.0, 45.0, 40.0, "cmodX")

    def test_bad_incidence(self):
        with pytest.raises(mod.ValidationError):
            mod.cmod_sigma0_db(10.0, 45.0, 80.0, "cmod5")

    def test_vectorized(self):
        u = np.array([2.0, 10.0, 25.0])
        s = mod.cmod_sigma0_db(u, 45.0, 40.0, "cmod5")
        assert s.shape == (3,)
        assert np.all(np.diff(s) > 0)


class TestCmodInvert:
    def test_roundtrip_scalar_grid(self):
        """反演(正演(U)) 应还原 U。"""
        truth = np.array([[2.0, 5.0, 10.0, 20.0, 30.0]])
        sigma0 = mod.cmod_sigma0_db(truth, 45.0, 40.0, "cmod5")
        back = mod.cmod_invert_wind(sigma0, 45.0, 40.0, "cmod5")
        np.testing.assert_allclose(back, truth, atol=1e-3)

    def test_clipping_below_range(self):
        # 极低 σ⁰（对应负风速）应截断到 u_min=0
        very_low = np.array([[-40.0]])
        back = mod.cmod_invert_wind(very_low, 45.0, 40.0, "cmod5")
        assert back[0, 0] == pytest.approx(mod.U_MIN, abs=1e-3)

    def test_clipping_above_range(self):
        very_high = np.array([[30.0]])  # 远超 U_MAX=45 对应的 σ⁰
        back = mod.cmod_invert_wind(very_high, 45.0, 40.0, "cmod5")
        assert back[0, 0] == pytest.approx(mod.U_MAX, abs=1e-3)

    def test_bad_range(self):
        with pytest.raises(mod.ValidationError):
            mod.cmod_invert_wind(np.array([[0.0]]), 45.0, 40.0, u_min=10.0, u_max=5.0)

    def test_both_models_roundtrip(self):
        for model in ("cmod5", "cmod7"):
            truth = np.array([[8.0, 15.0]])
            s = mod.cmod_sigma0_db(truth, 30.0, 45.0, model)
            back = mod.cmod_invert_wind(s, 30.0, 45.0, model)
            np.testing.assert_allclose(back, truth, atol=1e-3)


class TestSynthetic:
    def test_shape_and_truth(self):
        sigma0, info = mod.generate_synthetic([121, 30, 122, 31], width=32, height=32,
                                              wind_dir=45.0, seed=1)
        assert sigma0.shape == (32, 32)
        assert "wind_truth" in info
        assert info["wind_truth"].shape == (32, 32)

    def test_retrieval_accuracy(self):
        """合成风场反演：高相关 + 低 RMSE。"""
        bbox = [121, 30, 122, 31]
        sigma0, info = mod.generate_synthetic(bbox, width=48, height=48,
                                              wind_dir=45.0, incidence_deg=40.0,
                                              model="cmod5", noise_db=0.2, seed=7)
        truth = info["wind_truth"]
        est = mod.cmod_invert_wind(sigma0, 45.0, 40.0, "cmod5")
        corr = np.corrcoef(est.ravel(), truth.ravel())[0, 1]
        rmse = np.sqrt(np.mean((est - truth) ** 2))
        assert corr > 0.95
        assert rmse < 1.5


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(-15, -5, (16, 16)).astype(np.float32)
        bbox = [121.0, 30.0, 122.0, 31.0]
        path = str(tmp_path / "x.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == arr.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, arr, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/no.tif")
