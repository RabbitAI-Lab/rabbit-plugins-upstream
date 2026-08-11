"""Core algorithm tests for desertification-monitoring."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as dm


class TestTrendSlope:
    def test_sens_slope_recovers_linear(self):
        # perfect linear decline 0.8 -> 0.2 over 6 dates, slope = -0.12
        n = 6
        ts = np.linspace(0.8, 0.2, n)
        cube = np.zeros((n, 4, 4), dtype=np.float32)
        for k in range(n):
            cube[k] = ts[k]
        slope = dm.sens_slope(cube)
        assert np.allclose(slope, -0.12, atol=1e-4)

    def test_linear_slope_recovers_linear(self):
        n = 6
        ts = np.linspace(0.8, 0.2, n)
        cube = np.zeros((n, 4, 4), dtype=np.float32)
        for k in range(n):
            cube[k] = ts[k]
        slope = dm.linear_slope(cube)
        assert np.allclose(slope, -0.12, atol=1e-4)

    def test_sens_robust_to_outlier(self):
        n = 6
        ts = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.9], dtype=np.float32)  # one spike
        cube = np.zeros((n, 3, 3), dtype=np.float32)
        for k in range(n):
            cube[k] = ts[k]
        sens = dm.sens_slope(cube)[0, 0]
        lin = dm.linear_slope(cube)[0, 0]
        # Sen's should be closer to 0 (robust) than least squares
        assert abs(sens) < abs(lin)

    def test_flat_series_zero_slope(self):
        cube = np.full((5, 3, 3), 0.4, dtype=np.float32)
        assert np.allclose(dm.sens_slope(cube), 0.0, atol=1e-6)

    def test_too_few_dates_raises(self):
        cube = np.full((1, 3, 3), 0.4, dtype=np.float32)
        with pytest.raises(dm.ValidationError):
            dm.sens_slope(cube)

    def test_unknown_method_raises(self):
        cube = np.full((3, 2, 2), 0.4, dtype=np.float32)
        with pytest.raises(dm.UsageError):
            dm.trend_slope(cube, method="bogus")


class TestClassify:
    def test_grade_thresholds(self):
        score = np.array([[0.1, 0.35, 0.55, 0.8]], dtype=np.float32)
        grade = dm.classify_desertification(score)
        assert grade[0, 0] == 0
        assert grade[0, 1] == 1
        assert grade[0, 2] == 2
        assert grade[0, 3] == 3


class TestScore:
    def test_degrading_scores_high_stable_low(self):
        n = 6
        # degrading pixel 0.55 -> 0.10
        deg = np.linspace(0.55, 0.10, n).astype(np.float32)
        # stable pixel 0.60
        stb = np.full(n, 0.60, dtype=np.float32)
        ndvi = np.zeros((n, 1, 2), dtype=np.float32)
        ndvi[:, 0, 0] = deg
        ndvi[:, 0, 1] = stb
        albedo = np.array([[0.34, 0.12]], dtype=np.float32)
        score, slope, comp = dm.desertification_score(ndvi, albedo)
        assert score[0, 0] > score[0, 1]
        assert slope[0, 0] < -0.05
        grade = dm.classify_desertification(score)
        assert grade[0, 0] >= 2     # degrading -> moderate/severe
        assert grade[0, 1] == 0     # stable -> stable


class TestSplitInputs:
    def test_explicit_albedo(self):
        cube = np.random.uniform(0, 1, (7, 8, 8)).astype(np.float32)
        ndvi, alb, explicit = dm.split_inputs(cube, n_dates=6)
        assert ndvi.shape == (6, 8, 8)
        assert alb.shape == (8, 8)
        assert explicit is True
        np.testing.assert_allclose(alb, cube[6])

    def test_proxy_albedo(self):
        cube = np.random.uniform(0, 1, (6, 8, 8)).astype(np.float32)
        ndvi, alb, explicit = dm.split_inputs(cube, n_dates=6)
        assert explicit is False
        np.testing.assert_allclose(alb, 1.0 - cube[:6].mean(axis=0), atol=1e-5)

    def test_too_few_bands_raises(self):
        cube = np.random.uniform(0, 1, (3, 8, 8)).astype(np.float32)
        with pytest.raises(dm.ValidationError):
            dm.split_inputs(cube, n_dates=6)


class TestSynthetic:
    def test_shape_and_truth(self):
        ndvi, alb, truth, info = dm.generate_synthetic_series([100, 40, 101, 41], n_dates=6)
        assert ndvi.shape == (6, 128, 128)
        assert alb.shape == (128, 128)
        assert truth.sum() > 0

    def test_degrading_trend_detected(self):
        ndvi, alb, truth, info = dm.generate_synthetic_series([100, 40, 101, 41], n_dates=6)
        score, slope, comp = dm.desertification_score(ndvi, alb)
        mean_deg = float(slope[truth.astype(bool)].mean())
        assert mean_deg < -0.05, f"degrading region slope not negative: {mean_deg}"
        grade = dm.classify_desertification(score)
        # most of the degrading region should be moderate or severe
        assert (grade[truth.astype(bool)] >= 2).mean() > 0.8

    def test_build_cube_roundtrip(self):
        ndvi, alb, truth, info = dm.generate_synthetic_series([100, 40, 101, 41], n_dates=4)
        cube = dm.build_cube(ndvi, alb)
        assert cube.shape == (5, 128, 128)
        n2, a2, explicit = dm.split_inputs(cube, n_dates=4)
        assert explicit is True
        np.testing.assert_allclose(a2, alb, atol=1e-5)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (7, 16, 16)).astype(np.float32)
        bbox = [100.0, 40.0, 101.0, 41.0]
        path = str(tmp_path / "t.tif")
        dm.write_geotiff(path, cube, bbox)
        back, rb = dm.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(dm.UsageError):
            dm.read_geotiff("/nonexistent/x.tif")
