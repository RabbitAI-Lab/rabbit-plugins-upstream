"""Core algorithm tests for wind-resource-assessment."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestFitWeibull:
    def test_recovers_known_k_c_moment(self):
        """矩估计应能近似恢复已知 Weibull 参数。"""
        from scipy.stats import weibull_min
        rng = np.random.default_rng(0)
        true_k, true_c = 2.0, 8.0
        samples = weibull_min.rvs(true_k, scale=true_c, size=20000, random_state=rng)
        k, c = mod.fit_weibull(samples, method="moment")
        assert abs(k - true_k) < 0.3, f"k={k}, expected ~{true_k}"
        assert abs(c - true_c) / true_c < 0.1, f"c={c}, expected ~{true_c}"

    def test_recovers_known_k_c_mle(self):
        """MLE 应更精确地恢复已知 Weibull 参数。"""
        from scipy.stats import weibull_min
        rng = np.random.default_rng(1)
        true_k, true_c = 2.5, 6.0
        samples = weibull_min.rvs(true_k, scale=true_c, size=20000, random_state=rng)
        k, c = mod.fit_weibull(samples, method="mle")
        assert abs(k - true_k) < 0.2, f"k={k}, expected ~{true_k}"
        assert abs(c - true_c) / true_c < 0.05, f"c={c}, expected ~{true_c}"

    def test_empty_returns_zero(self):
        k, c = mod.fit_weibull(np.array([]))
        assert k == 0.0
        assert c == 0.0

    def test_negative_clipped(self):
        """负风速被截断后仍能拟合。"""
        rng = np.random.default_rng(2)
        samples = rng.uniform(-2, 10, size=5000)
        k, c = mod.fit_weibull(samples, method="moment")
        assert k > 0
        assert c > 0


class TestWindPowerDensity:
    def test_known_value(self):
        """WPD = 0.5 * rho * mean(v^3)。"""
        v = np.array([10.0, 10.0, 10.0])
        wpd = mod.wind_power_density(v, rho=1.225)
        expected = 0.5 * 1.225 * 1000.0
        assert abs(wpd - expected) < 1e-6

    def test_zero_wind(self):
        wpd = mod.wind_power_density(np.array([0.0, 0.0]))
        assert wpd == 0.0

    def test_positive_for_positive_wind(self):
        v = np.array([3.0, 5.0, 8.0, 12.0])
        wpd = mod.wind_power_density(v)
        assert wpd > 0.0


class TestExtrapolateWind:
    def test_higher_altitude_stronger(self):
        """目标高度 > 参考高度 → 风速增大。"""
        v_ref = np.array([5.0, 7.0, 9.0])
        v_100 = mod.extrapolate_wind(v_ref, z_ref=10.0, z_target=100.0, roughness=0.14)
        assert np.all(v_100 > v_ref)

    def test_lower_altitude_weaker(self):
        """目标高度 < 参考高度 → 风速减小。"""
        v_ref = np.array([5.0, 7.0, 9.0])
        v_5 = mod.extrapolate_wind(v_ref, z_ref=10.0, z_target=5.0, roughness=0.14)
        assert np.all(v_5 < v_ref)

    def test_same_height_unchanged(self):
        v_ref = np.array([5.0, 7.0, 9.0])
        v_same = mod.extrapolate_wind(v_ref, z_ref=10.0, z_target=10.0)
        np.testing.assert_allclose(v_same, v_ref, rtol=1e-6)


class TestWeibullMeanV3:
    def test_consistent_with_samples(self):
        """解析 E[v^3] 应与大样本均值一致。"""
        from scipy.stats import weibull_min
        rng = np.random.default_rng(3)
        true_k, true_c = 2.0, 7.0
        samples = weibull_min.rvs(true_k, scale=true_c, size=100000, random_state=rng)
        empirical = float(np.mean(samples ** 3))
        analytical = mod.weibull_mean_v3(true_k, true_c)
        assert abs(analytical - empirical) / empirical < 0.05

    def test_invalid_params_zero(self):
        assert mod.weibull_mean_v3(0.0, 5.0) == 0.0
        assert mod.weibull_mean_v3(2.0, 0.0) == 0.0


class TestAnnualEnergy:
    def test_positive_for_good_wind(self):
        mwh = mod.annual_energy_mwh(wpd=500.0)
        assert mwh > 0.0

    def test_zero_for_zero_wpd(self):
        mwh = mod.annual_energy_mwh(wpd=0.0)
        assert mwh == 0.0

    def test_capped_at_rated(self):
        """WPD 远超额定值时发电量不超上限。"""
        mwh_low = mod.annual_energy_mwh(wpd=400.0)
        mwh_high = mod.annual_energy_mwh(wpd=800.0)
        assert abs(mwh_high - mwh_low) < 1e-6  # 都被 cap 到 1.0


class TestAssessWindField:
    def test_output_shapes(self):
        cube = np.random.default_rng(4).uniform(2, 12, (20, 16, 16)).astype(np.float32)
        rasters, params = mod.assess_wind_field(cube, height=100.0, method="moment")
        assert rasters["mean_wind"].shape == (16, 16)
        assert rasters["wpd"].shape == (16, 16)
        assert rasters["weibull_k"].shape == (16, 16)
        assert rasters["weibull_c"].shape == (16, 16)
        assert params["n_dates"] == 20

    def test_wpd_positive(self):
        cube = np.random.default_rng(5).uniform(3, 15, (30, 8, 8)).astype(np.float32)
        rasters, params = mod.assess_wind_field(cube)
        assert np.all(rasters["wpd"] > 0)

    def test_too_few_dates_raises(self):
        cube = np.random.default_rng(6).uniform(3, 10, (1, 8, 8)).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.assess_wind_field(cube)

    def test_wrong_ndim_raises(self):
        cube = np.random.default_rng(7).uniform(3, 10, (8, 8)).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.assess_wind_field(cube)


class TestSynthetic:
    def test_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=30)
        assert cube.ndim == 3
        assert cube.shape[0] == 30
        assert cube.shape[1] == 64
        assert cube.shape[2] == 64

    def test_weibull_recovery(self):
        """合成数据的 Weibull 参数应接近真值。"""
        cube, info = mod.generate_synthetic_cube(
            [116, 39, 117, 40], n_dates=200, true_k=2.0, true_c=7.0, seed=99,
        )
        # 取中心像元时序
        series = cube[:, 32, 32]
        k, c = mod.fit_weibull(series, method="mle")
        assert abs(k - 2.0) < 0.5, f"k={k}"
        assert abs(c - 7.0) / 7.0 < 0.2, f"c={c}"


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(8).uniform(0, 10, (3, 16, 16)).astype(np.float32)
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
