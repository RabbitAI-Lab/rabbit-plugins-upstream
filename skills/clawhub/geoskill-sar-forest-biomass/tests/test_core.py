"""Core algorithm tests for sar-forest-biomass."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestDefaults:
    def test_all_band_model_combos_present(self):
        for band in ("c", "l"):
            for model in ("linear", "saturation"):
                coefs = mod.DEFAULT_COEFS[(band, model)]
                assert coefs
                if model == "linear":
                    assert coefs["m"] > 0
                else:
                    assert coefs["agb_sat"] > 0 and coefs["k"] > 0

    def test_l_band_saturates_higher(self):
        # L 波段穿透性更强，饱和生物量应高于 C 波段
        assert (mod.DEFAULT_COEFS[("l", "saturation")]["agb_sat"]
                > mod.DEFAULT_COEFS[("c", "saturation")]["agb_sat"])


class TestLinearModel:
    def test_roundtrip(self):
        coefs = mod.DEFAULT_COEFS[("c", "linear")]
        truth = np.array([[10.0, 50.0, 120.0, 200.0]])
        sigma0 = mod.forward_sigma0_db(truth, "linear", coefs)
        back = mod.invert_biomass(sigma0, "linear", coefs)
        np.testing.assert_allclose(back, truth, atol=1e-4)

    def test_monotonic(self):
        coefs = mod.DEFAULT_COEFS[("c", "linear")]
        agb = np.array([10.0, 100.0, 200.0])
        s = mod.forward_sigma0_db(agb, "linear", coefs)
        assert np.all(np.diff(s) > 0)

    def test_clip_negative(self):
        coefs = mod.DEFAULT_COEFS[("c", "linear")]
        back = mod.invert_biomass(np.array([[-40.0]]), "linear", coefs)
        assert back[0, 0] == 0.0

    def test_clip_above_max(self):
        coefs = mod.DEFAULT_COEFS[("c", "linear")]
        back = mod.invert_biomass(np.array([[5.0]]), "linear", coefs)  # → ~606
        assert back[0, 0] == pytest.approx(mod.AGB_MAX, abs=1e-6)


class TestSaturationModel:
    def test_roundtrip(self):
        coefs = mod.DEFAULT_COEFS[("c", "saturation")]
        truth = np.array([[10.0, 50.0, 120.0, 180.0]])
        sigma0 = mod.forward_sigma0_db(truth, "saturation", coefs)
        back = mod.invert_biomass(sigma0, "saturation", coefs)
        np.testing.assert_allclose(back, truth, atol=1e-3)

    def test_saturation_increments_shrink(self):
        """等量 AGB 增量引起的 σ⁰ 增量应随生物量升高而减小（饱和）。"""
        coefs = mod.DEFAULT_COEFS[("c", "saturation")]
        lo = mod.forward_sigma0_db(np.array([20.0]), "saturation", coefs)
        mid = mod.forward_sigma0_db(np.array([70.0]), "saturation", coefs)
        hi = mod.forward_sigma0_db(np.array([120.0]), "saturation", coefs)
        hi2 = mod.forward_sigma0_db(np.array([170.0]), "saturation", coefs)
        inc_low = mid - lo
        inc_high = hi2 - hi
        assert inc_low > inc_high > 0

    def test_bounded_by_agb_sat(self):
        coefs = mod.DEFAULT_COEFS[("c", "saturation")]
        back = mod.invert_biomass(np.array([[20.0]]), "saturation", coefs)
        assert back[0, 0] <= coefs["agb_sat"] + 1e-6


class TestCalibration:
    def test_calibrate_linear_recovers(self):
        rng = np.random.default_rng(3)
        m, c = 0.04, -16.0
        agb = rng.uniform(10, 220, 120)
        sigma0 = m * agb + c + rng.normal(0, 0.05, 120)
        coefs = mod.calibrate_linear(sigma0, agb)
        assert coefs["m"] == pytest.approx(m, rel=0.05)
        assert coefs["c"] == pytest.approx(c, rel=0.05)

    def test_calibrate_saturation_recovers(self):
        rng = np.random.default_rng(5)
        agb_sat, k = 250.0, 1.5
        agb = rng.uniform(10, 230, 120)
        sigma0_lin = -(1.0 / k) * np.log(1.0 - agb / agb_sat)
        sigma0_db = 10.0 * np.log10(sigma0_lin) + rng.normal(0, 0.02, 120)
        coefs = mod.calibrate_saturation(sigma0_db, agb)
        assert coefs["agb_sat"] == pytest.approx(agb_sat, rel=0.10)
        assert coefs["k"] == pytest.approx(k, rel=0.10)

    def test_calibrated_retrieval_improves(self):
        """标定后的线性模型应能还原样本关系（残差小）。"""
        rng = np.random.default_rng(1)
        agb = rng.uniform(10, 200, 100)
        sigma0 = 0.033 * agb - 15.0 + rng.normal(0, 0.1, 100)
        coefs = mod.calibrate_linear(sigma0, agb)
        est = mod.invert_biomass(sigma0, "linear", coefs)
        rmse = np.sqrt(np.mean((est - agb) ** 2))
        assert rmse < 6.0


class TestLoadCalibration:
    def test_load_ok(self, tmp_path):
        p = tmp_path / "c.csv"
        p.write_text("sigma0,agb\n-14,30\n-12,90\n-10,150\n-8,210\n", encoding="utf-8")
        s, a = mod.load_calibration_csv(str(p))
        assert len(s) == 4
        assert a[0] == 30

    def test_missing_file(self):
        with pytest.raises(mod.UsageError):
            mod.load_calibration_csv("/no/such/file.csv")

    def test_bad_columns(self, tmp_path):
        p = tmp_path / "bad.csv"
        p.write_text("x,y\n1,2\n3,4\n5,6\n", encoding="utf-8")
        with pytest.raises(mod.ValidationError):
            mod.load_calibration_csv(str(p))


class TestSynthetic:
    def test_shape_and_truth(self):
        sigma0, info = mod.generate_synthetic([110, 22, 111, 23], width=32, height=32,
                                              band="c", model="saturation", seed=2)
        assert sigma0.shape == (32, 32)
        assert info["agb_truth"].shape == (32, 32)
        assert info["agb_truth"].min() >= 5.0

    def test_retrieval_accuracy_saturation(self):
        bbox = [110, 22, 111, 23]
        coefs = mod.DEFAULT_COEFS[("c", "saturation")]
        sigma0, info = mod.generate_synthetic(bbox, width=48, height=48, band="c",
                                              model="saturation", noise_db=0.3, seed=8)
        est = mod.invert_biomass(sigma0, "saturation", coefs)
        truth = info["agb_truth"]
        corr = np.corrcoef(est.ravel(), truth.ravel())[0, 1]
        rmse = np.sqrt(np.mean((est - truth) ** 2))
        assert corr > 0.9
        assert rmse < 15.0

    def test_retrieval_accuracy_linear(self):
        bbox = [110, 22, 111, 23]
        coefs = mod.DEFAULT_COEFS[("c", "linear")]
        sigma0, info = mod.generate_synthetic(bbox, width=48, height=48, band="c",
                                              model="linear", noise_db=0.2, seed=11)
        est = mod.invert_biomass(sigma0, "linear", coefs)
        truth = info["agb_truth"]
        corr = np.corrcoef(est.ravel(), truth.ravel())[0, 1]
        assert corr > 0.9


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(5, 200, (16, 16)).astype(np.float32)
        bbox = [110.0, 22.0, 111.0, 23.0]
        path = str(tmp_path / "x.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == arr.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, arr, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/no.tif")
