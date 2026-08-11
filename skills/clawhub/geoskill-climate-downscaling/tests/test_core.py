"""Core algorithm tests for climate-downscaling."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as cd


class TestSlope:
    def test_flat_zero(self):
        dem = np.full((16, 16), 100.0)
        slope = cd.slope_from_dem(dem)
        assert slope.max() < 1e-6

    def test_ramp_positive(self):
        dem = np.tile(np.arange(16, dtype=np.float64) * 10.0, (16, 1))
        slope = cd.slope_from_dem(dem, res_m=10.0)
        assert slope.mean() > 0.0


class TestBlockAverage:
    def test_shape_and_value(self):
        arr = np.ones((16, 16))
        out = cd.block_average(arr, 4, 4)
        assert out.shape == (4, 4)
        np.testing.assert_allclose(out, 1.0)

    def test_known_values(self):
        arr = np.arange(16, dtype=np.float64).reshape(4, 4)
        out = cd.block_average(arr, 2, 2)
        assert out.shape == (2, 2)
        assert out[0, 0] == np.mean([0, 1, 4, 5])

    def test_ndim_raises(self):
        with pytest.raises(cd.ValidationError):
            cd.block_average(np.ones((4, 4, 4)), 2, 2)

    def test_too_large_block_raises(self):
        with pytest.raises(cd.ValidationError):
            cd.block_average(np.ones((4, 4)), 8, 8)


class TestRegression:
    def test_recovers_linear(self):
        rng = np.random.default_rng(0)
        elev = rng.uniform(0, 3000, 200)
        slope = rng.uniform(0, 30, 200)
        y = 25.0 - 0.006 * elev + 0.01 * slope
        X = np.column_stack([elev, slope])
        model, coefs, intercept = cd.fit_downscaling_regression(X, y)
        assert abs(coefs[0] - (-0.006)) < 1e-6
        assert abs(intercept - 25.0) < 1e-4

    def test_shape_mismatch_raises(self):
        with pytest.raises(cd.ValidationError):
            cd.fit_downscaling_regression(np.ones((10, 2)), np.ones(5))

    def test_too_few_samples_raises(self):
        with pytest.raises(cd.ValidationError):
            cd.fit_downscaling_regression(np.ones((2, 2)), np.ones(2))


class TestInterpolateResidual:
    def test_constant_preserved(self):
        resid = np.full((4, 4), 3.0)
        out = cd.interpolate_residual(resid, (16, 16))
        assert out.shape == (16, 16)
        np.testing.assert_allclose(out, 3.0, atol=1e-6)

    def test_too_coarse_returns_mean(self):
        resid = np.array([[5.0]])
        out = cd.interpolate_residual(resid, (8, 8))
        np.testing.assert_allclose(out, 5.0)


class TestDownscale:
    def test_end_to_end_captures_truth(self):
        met = cd.generate_synthetic([100, 26, 104, 30], target_size=64, coarse=8, seed=1)
        res = cd.downscale(met["dem"], met["slope"], met["truth"], coarse=8)
        # 与真值高相关
        assert res["correlation"] > 0.85
        # 高程递减率为负（温度随高程递减）
        assert res["lapse_rate_per_m"] < 0.0
        # 降尺度 RMSE 应优于粗分辨率基线
        assert res["rmse"] < res["rmse_coarse_baseline"]
        assert res["coefs"]["elevation"] < 0.0

    def test_shape_mismatch_raises(self):
        with pytest.raises(cd.ValidationError):
            cd.downscale(np.ones((16, 16)), np.ones((16, 16)), np.ones((8, 8)), coarse=4)


class TestSynthetic:
    def test_shapes(self):
        met = cd.generate_synthetic([100, 26, 104, 30], target_size=64, coarse=8)
        assert met["dem"].shape == (64, 64)
        assert met["slope"].shape == (64, 64)
        assert met["truth"].shape == (64, 64)
        assert met["truth_coarse"].shape == (8, 8)

    def test_truth_decreases_with_elevation(self):
        met = cd.generate_synthetic([100, 26, 104, 30], target_size=64, seed=5)
        # 忽略异常项，高程与温度总体负相关
        corr = np.corrcoef(met["dem"].ravel(), met["truth"].ravel())[0, 1]
        assert corr < -0.5


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 30, (1, 16, 16)).astype(np.float32)
        bbox = [100.0, 26.0, 104.0, 30.0]
        path = str(tmp_path / "d.tif")
        cd.write_geotiff(path, cube, bbox)
        back, rb = cd.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(cd.UsageError):
            cd.read_geotiff("/nonexistent/d.tif")
