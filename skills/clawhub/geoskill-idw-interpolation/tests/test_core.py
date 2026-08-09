"""Core algorithm tests for idw-interpolation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestIDWExact:
    def test_exact_at_known_points(self):
        """IDW must reproduce exact values at known sample locations."""
        pts = np.array([[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
        vals = np.array([10.0, 20.0, 30.0, 40.0])
        # Grid exactly at sample points
        grid_x, grid_y = np.meshgrid([0.0, 1.0], [1.0, 0.0])
        result = mod.idw_interpolate(pts, vals, grid_x, grid_y, power=2.0)
        # (0,0)->10, (1,0)->20, (0,1)->30, (1,1)->40
        expected = np.array([[30.0, 40.0], [10.0, 20.0]])
        np.testing.assert_allclose(result, expected, atol=1e-10)

    def test_exact_vectorized(self):
        """Vectorized version also exact at sample points."""
        pts = np.array([[0.0, 0.0], [2.0, 0.0], [0.0, 2.0]])
        vals = np.array([5.0, 15.0, 25.0])
        grid_x = np.array([[0.0, 2.0], [0.0, 2.0]])
        grid_y = np.array([[0.0, 0.0], [2.0, 2.0]])
        result = mod.idw_grid_vectorized(pts, vals, grid_x, grid_y, power=2.0)
        expected = np.array([[5.0, 15.0], [25.0, np.nan]])  # (2,2) not a sample
        # Only check the 3 exact points
        assert abs(result[0, 0] - 5.0) < 1e-10
        assert abs(result[0, 1] - 15.0) < 1e-10
        assert abs(result[1, 0] - 25.0) < 1e-10

    def test_midpoint_symmetry(self):
        """At midpoint of two equal-distance points, IDW = mean."""
        pts = np.array([[0.0, 0.0], [2.0, 0.0]])
        vals = np.array([10.0, 30.0])
        grid_x = np.array([[1.0]])
        grid_y = np.array([[0.0]])
        result = mod.idw_interpolate(pts, vals, grid_x, grid_y, power=2.0)
        assert abs(result[0, 0] - 20.0) < 1e-10

    def test_closer_point_dominates(self):
        """Closer point should have more influence."""
        pts = np.array([[0.0, 0.0], [10.0, 0.0]])
        vals = np.array([100.0, 0.0])
        grid_x = np.array([[1.0]])
        grid_y = np.array([[0.0]])
        result = mod.idw_interpolate(pts, vals, grid_x, grid_y, power=2.0)
        # At x=1: w0=1/1^2=1, w1=1/9^2=1/81 => result ≈ 100*1/(1+1/81) ≈ 98.78
        assert result[0, 0] > 90.0


class TestIDWPower:
    def test_higher_power_more_local(self):
        """Higher power → result closer to nearest point value."""
        pts = np.array([[0.0, 0.0], [1.0, 0.0]])
        vals = np.array([0.0, 100.0])
        gx = np.array([[0.25]])
        gy = np.array([[0.0]])
        r1 = mod.idw_interpolate(pts, vals, gx, gy, power=1.0)
        r4 = mod.idw_interpolate(pts, vals, gx, gy, power=4.0)
        # Higher power → closer to nearest (0.0)
        assert r4[0, 0] < r1[0, 0]


class TestIDWNeighbors:
    def test_n_neighbors_limits(self):
        """With n_neighbors=1, result = nearest point value."""
        pts = np.array([[0.0, 0.0], [1.0, 0.0], [2.0, 0.0]])
        vals = np.array([10.0, 20.0, 30.0])
        gx = np.array([[0.6]])
        gy = np.array([[0.0]])
        result = mod.idw_interpolate(pts, vals, gx, gy, power=2.0, n_neighbors=1)
        assert abs(result[0, 0] - 20.0) < 1e-10

    def test_vectorized_n_neighbors(self):
        """Vectorized with n_neighbors=1 matches nearest."""
        pts = np.array([[0.0, 0.0], [5.0, 0.0], [10.0, 0.0]])
        vals = np.array([100.0, 200.0, 300.0])
        gx = np.array([[4.0]])
        gy = np.array([[0.0]])
        result = mod.idw_grid_vectorized(pts, vals, gx, gy, power=2.0, n_neighbors=1)
        assert abs(result[0, 0] - 200.0) < 1e-10


class TestIDWSearchRadius:
    def test_max_distance_filter(self):
        """Points outside search radius are excluded."""
        pts = np.array([[0.0, 0.0], [100.0, 0.0]])
        vals = np.array([10.0, 99.0])
        gx = np.array([[1.0]])
        gy = np.array([[0.0]])
        result = mod.idw_interpolate(pts, vals, gx, gy, power=2.0, max_distance=5.0)
        # Only first point within radius → exact value
        assert abs(result[0, 0] - 10.0) < 1e-10


class TestIDWValidation:
    def test_empty_points_raises(self):
        pts = np.empty((0, 2))
        vals = np.empty(0)
        gx = np.array([[0.0]])
        gy = np.array([[0.0]])
        with pytest.raises(mod.ValidationError):
            mod.idw_interpolate(pts, vals, gx, gy)

    def test_length_mismatch_raises(self):
        pts = np.array([[0.0, 0.0]])
        vals = np.array([1.0, 2.0])
        gx = np.array([[0.0]])
        gy = np.array([[0.0]])
        with pytest.raises(mod.ValidationError):
            mod.idw_interpolate(pts, vals, gx, gy)


class TestSynthetic:
    def test_synthetic_shapes(self):
        pts, vals, gx, gy, info = mod.generate_synthetic([116, 39, 117, 40], n_points=30, grid_size=32)
        assert pts.shape == (30, 2)
        assert vals.shape == (30,)
        assert gx.shape == (32, 32)
        assert gy.shape == (32, 32)

    def test_synthetic_in_bbox(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        pts, vals, gx, gy, info = mod.generate_synthetic(bbox, seed=7)
        assert np.all(pts[:, 0] >= bbox[0]) and np.all(pts[:, 0] <= bbox[2])
        assert np.all(pts[:, 1] >= bbox[1]) and np.all(pts[:, 1] <= bbox[3])
