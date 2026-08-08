"""Core algorithm tests for sar-soil-moisture."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestWavenumber:
    def test_c_band_value(self):
        k = mod.radar_wavenumber(0.056)
        assert k == pytest.approx(2 * np.pi / 0.056, rel=1e-6)
        assert 110 < k < 115  # C 波段约 112 rad/m

    def test_invalid_wavelength(self):
        with pytest.raises(mod.ValidationError):
            mod.radar_wavenumber(0.0)


class TestModelTerms:
    def test_moisture_sensitivity_decreases_with_incidence(self):
        _, _, C30 = mod._model_terms(30.0, "dubois")
        _, _, C50 = mod._model_terms(50.0, "dubois")
        assert C30 > C50  # cos²θ 随入射角增大而减小

    def test_unknown_model(self):
        with pytest.raises(mod.UsageError):
            mod._model_terms(40.0, "xx")

    def test_bad_incidence(self):
        with pytest.raises(mod.ValidationError):
            mod._model_terms(80.0, "dubois")


class TestBackscatter:
    def test_increases_with_moisture(self):
        s10 = mod.backscatter_db(0.10, 1.5, 40.0, "dubois")
        s30 = mod.backscatter_db(0.30, 1.5, 40.0, "dubois")
        assert s30 > s10

    def test_increases_with_roughness(self):
        s_lo = mod.backscatter_db(0.2, 0.5, 40.0, "dubois")
        s_hi = mod.backscatter_db(0.2, 3.0, 40.0, "dubois")
        assert s_hi > s_lo

    def test_vectorized(self):
        mv = np.array([0.05, 0.2, 0.4])
        s = mod.backscatter_db(mv, 1.5, 40.0, "dubois")
        assert s.shape == (3,)
        assert np.all(np.diff(s) > 0)


class TestInvert:
    def test_roundtrip(self):
        truth = np.array([[0.05, 0.15, 0.30, 0.45]])
        ks = np.array([[1.2, 1.2, 1.2, 1.2]])
        sigma0 = mod.backscatter_db(truth, ks, 40.0, "dubois")
        back = mod.invert_soil_moisture(sigma0, ks, 40.0, "dubois")
        np.testing.assert_allclose(back, truth, atol=1e-6)

    def test_clip_below_min(self):
        # 极低 σ⁰ → 反演为负 → 裁剪到 MV_MIN
        sigma0 = np.array([[-60.0]])
        back = mod.invert_soil_moisture(sigma0, 1.5, 40.0, "dubois")
        assert back[0, 0] == pytest.approx(mod.MV_MIN, abs=1e-9)

    def test_clip_above_max(self):
        sigma0 = np.array([[20.0]])
        back = mod.invert_soil_moisture(sigma0, 1.5, 40.0, "dubois")
        assert back[0, 0] == pytest.approx(mod.MV_MAX, abs=1e-9)

    def test_bad_range(self):
        with pytest.raises(mod.ValidationError):
            mod.invert_soil_moisture(np.array([[0.0]]), 1.5, 40.0, mv_min=0.5, mv_max=0.1)

    def test_both_models_roundtrip(self):
        for model in ("dubois", "oh"):
            truth = np.array([[0.12, 0.35]])
            ks = np.array([[1.8, 1.8]])
            s = mod.backscatter_db(truth, ks, 45.0, model)
            back = mod.invert_soil_moisture(s, ks, 45.0, model)
            np.testing.assert_allclose(back, truth, atol=1e-6)


class TestSynthetic:
    def test_shape_and_truth(self):
        sigma0, info = mod.generate_synthetic([116, 39, 117, 40], width=32, height=32, seed=1)
        assert sigma0.shape == (32, 32)
        assert info["mv_truth"].shape == (32, 32)
        assert info["ks_truth"].shape == (32, 32)
        assert info["mv_truth"].min() >= 0.03
        assert info["mv_truth"].max() <= 0.50

    def test_retrieval_accuracy(self):
        """合成场景反演：高相关 + 低 RMSE（m³/m³）。"""
        bbox = [116, 39, 117, 40]
        sigma0, info = mod.generate_synthetic(bbox, width=48, height=48,
                                              incidence_deg=40.0, model="dubois",
                                              noise_db=0.2, seed=9)
        est = mod.invert_soil_moisture(sigma0, info["ks_truth"], 40.0, "dubois")
        truth = info["mv_truth"]
        corr = np.corrcoef(est.ravel(), truth.ravel())[0, 1]
        rmse = np.sqrt(np.mean((est - truth) ** 2))
        assert corr > 0.95
        assert rmse < 0.05
        assert est.min() >= mod.MV_MIN - 1e-6
        assert est.max() <= mod.MV_MAX + 1e-6


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0.05, 0.4, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == arr.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, arr, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/no.tif")
