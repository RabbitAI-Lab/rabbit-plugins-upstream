"""Core algorithm tests for bathymetry-estimation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestStumpf:
    def test_ratio_monotonic_with_depth(self):
        """蓝光衰减慢 → 蓝/绿比值随水深增大，Stumpf 水深单调增。"""
        blue = np.array([0.40, 0.30, 0.20], dtype=np.float32)
        green = np.array([0.30, 0.15, 0.05], dtype=np.float32)
        depth = mod.stumpf_depth(blue, green, m0=0.0, m1=10.0)
        assert depth[0] < depth[1] < depth[2]

    def test_invalid_reflectance_nodata(self):
        blue = np.array([0.0, 0.5], dtype=np.float32)
        green = np.array([0.5, 0.5], dtype=np.float32)
        depth = mod.stumpf_depth(blue, green, 0.0, 10.0)
        assert depth[0] == mod.NODATA
        assert depth[1] != mod.NODATA


class TestFitStumpf:
    def test_recovers_linear_coeffs(self):
        """对 Stumpf 生成的数据反拟合，应恢复 m0/m1。"""
        rng = np.random.default_rng(0)
        ratio = rng.uniform(0.5, 5.0, 200)
        blue = ratio
        green = np.ones_like(ratio)
        true_m0, true_m1 = 1.5, 8.0
        depth = true_m0 + true_m1 * np.log(ratio)
        m0, m1 = mod.fit_stumpf(blue, green, depth)
        assert abs(m0 - true_m0) < 1e-6
        assert abs(m1 - true_m1) < 1e-6

    def test_too_few_samples_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.fit_stumpf(np.array([0.5]), np.array([0.3]), np.array([3.0]))


class TestLyzenga:
    def test_fit_and_apply(self):
        rng = np.random.default_rng(1)
        blue = rng.uniform(0.05, 0.5, 300)
        green = rng.uniform(0.05, 0.5, 300)
        true = (2.0, -5.0, 3.0)
        depth = true[0] + true[1] * np.log(blue) + true[2] * np.log(green)
        c0, c1, c2 = mod.fit_lyzenga(blue, green, depth)
        assert abs(c0 - true[0]) < 1e-4
        assert abs(c1 - true[1]) < 1e-4
        assert abs(c2 - true[2]) < 1e-4


class TestAccuracy:
    def test_perfect_prediction(self):
        t = np.arange(10, dtype=np.float32)
        m = mod.accuracy_metrics(t.copy(), t)
        assert m["rmse"] == 0.0
        assert abs(m["r2"] - 1.0) < 1e-6

    def test_ignores_nodata(self):
        est = np.array([1.0, 2.0, mod.NODATA], dtype=np.float32)
        truth = np.array([1.0, 2.0, 3.0], dtype=np.float32)
        m = mod.accuracy_metrics(est, truth)
        assert m["n_valid"] == 2


class TestEstimateBathymetry:
    def test_synthetic_stumpf_accurate(self):
        cube, truth, info = mod.generate_synthetic([116, 39, 117, 40])
        cb, cg, cd = mod.sample_calibration(cube, truth, 0, 1)
        depth, params = mod.estimate_bathymetry(
            cube, method="stumpf", calib_blue=cb, calib_green=cg, calib_depth=cd,
        )
        acc = mod.accuracy_metrics(depth, truth)
        # Stumpf 对 Beer–Lambert 数据应高度准确
        assert acc["r2"] > 0.95
        assert acc["rmse"] < 1.5

    def test_synthetic_lyzenga_accurate(self):
        cube, truth, info = mod.generate_synthetic([116, 39, 117, 40])
        cb, cg, cd = mod.sample_calibration(cube, truth, 0, 1)
        depth, _ = mod.estimate_bathymetry(
            cube, method="lyzenga", calib_blue=cb, calib_green=cg, calib_depth=cd,
        )
        acc = mod.accuracy_metrics(depth, truth)
        assert acc["r2"] > 0.95

    def test_unknown_method_raises(self):
        cube = np.random.rand(4, 8, 8).astype(np.float32) + 0.1
        with pytest.raises(mod.UsageError):
            mod.estimate_bathymetry(cube, method="bogus")

    def test_depth_clipped(self):
        cube, truth, info = mod.generate_synthetic([116, 39, 117, 40])
        depth, params = mod.estimate_bathymetry(cube, method="stumpf", max_depth=40.0)
        valid = depth > mod.NODATA / 2
        assert depth[valid].max() <= 40.0
        assert depth[valid].min() >= 0.0


class TestCalibrationCSV:
    def test_read_csv(self, tmp_path):
        p = tmp_path / "calib.csv"
        p.write_text("blue,green,depth\n0.4,0.3,1.0\n0.3,0.2,3.0\n0.2,0.1,6.0\n",
                     encoding="utf-8")
        b, g, d = mod.read_calibration_csv(str(p))
        assert len(b) == 3
        assert d[2] == 6.0

    def test_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_calibration_csv("/nonexistent/calib.csv")


class TestSynthetic:
    def test_shape_and_depth_range(self):
        cube, truth, info = mod.generate_synthetic([116, 39, 117, 40], max_depth=20.0)
        assert cube.shape[0] == 4
        assert truth.shape == cube.shape[1:]
        assert truth.min() >= 0.0
        assert truth.max() <= 20.0
