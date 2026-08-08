"""Core algorithm tests for hotspot-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestDistanceWeights:
    def test_self_weight_present(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0], [5.0, 5.0]])
        W = mod.distance_band_weights(coords, bandwidth=1.5)
        # 对角线（自身）应为 1
        np.testing.assert_allclose(np.diag(W), 1.0)

    def test_neighbors_within_band(self):
        coords = np.array([[0.0, 0.0], [1.0, 0.0], [10.0, 10.0]])
        W = mod.distance_band_weights(coords, bandwidth=1.5)
        assert W[0, 1] == 1.0  # 距离 1 < 1.5
        assert W[0, 2] == 0.0  # 距离远


class TestGiStar:
    def test_hotspot_positive(self):
        """中心高值 → 正 z 得分。"""
        coords = np.array([[float(i), float(j)] for i in range(7) for j in range(7)])
        x = np.zeros(49)
        # 中心 (3,3) 及邻域高值
        for i in range(7):
            for j in range(7):
                if abs(i - 3) <= 1 and abs(j - 3) <= 1:
                    x[i * 7 + j] = 100.0
        W = mod.distance_band_weights(coords, bandwidth=1.5)
        z = mod.gi_star_zscores(x, W)
        center = z[3 * 7 + 3]
        assert center > 2.0

    def test_coldspot_negative(self):
        """高值背景中的低值中心 → 负 z 得分。"""
        coords = np.array([[float(i), float(j)] for i in range(7) for j in range(7)])
        x = np.full(49, 100.0)
        for i in range(7):
            for j in range(7):
                if abs(i - 3) <= 1 and abs(j - 3) <= 1:
                    x[i * 7 + j] = 0.0
        W = mod.distance_band_weights(coords, bandwidth=1.5)
        z = mod.gi_star_zscores(x, W)
        assert z[3 * 7 + 3] < -2.0

    def test_uniform_field_near_zero(self):
        """均匀场 z 得分应接近 0。"""
        coords = np.array([[float(i), float(j)] for i in range(6) for j in range(6)])
        x = np.full(36, 5.0)
        W = mod.distance_band_weights(coords, bandwidth=1.5)
        z = mod.gi_star_zscores(x, W)
        assert np.all(np.abs(z) < 1e-6)


class TestClassification:
    def test_thresholds(self):
        z = np.array([3.0, 2.0, 1.7, 0.0, -1.7, -2.0, -3.0])
        sig = mod.classify_significance(z)
        assert sig[0] == 3   # z>2.58
        assert sig[1] == 2   # z>1.96
        assert sig[2] == 1   # z>1.65
        assert sig[3] == 0
        assert sig[4] == -1
        assert sig[5] == -2
        assert sig[6] == -3


class TestKDE:
    def test_peak_at_point(self):
        """核密度峰值应出现在点位置附近。"""
        pts = np.array([[0.5, 0.5]])
        gx, gy = np.meshgrid(np.linspace(0, 1, 21), np.linspace(0, 1, 21))
        density = mod.kernel_density(pts, gx, gy, bandwidth=0.1)
        peak = np.unravel_index(np.argmax(density), density.shape)
        # 峰值对应坐标接近 (0.5, 0.5)
        assert abs(gy[peak] - 0.5) < 0.06
        assert abs(gx[peak] - 0.5) < 0.06

    def test_density_nonnegative(self):
        rng = np.random.default_rng(0)
        pts = rng.uniform(0, 1, (20, 2))
        gx, gy = np.meshgrid(np.linspace(0, 1, 15), np.linspace(0, 1, 15))
        density = mod.kernel_density(pts, gx, gy, bandwidth=0.1)
        assert np.all(density >= 0)

    def test_weights_scale_density(self):
        pts = np.array([[0.5, 0.5]])
        gx, gy = np.meshgrid(np.linspace(0, 1, 11), np.linspace(0, 1, 11))
        d1 = mod.kernel_density(pts, gx, gy, 0.1, weights=np.array([1.0]))
        d2 = mod.kernel_density(pts, gx, gy, 0.1, weights=np.array([2.0]))
        np.testing.assert_allclose(d2, d1 * 2.0, rtol=1e-10)

    def test_empty_points_raises(self):
        gx, gy = np.meshgrid(np.linspace(0, 1, 5), np.linspace(0, 1, 5))
        with pytest.raises(mod.ValidationError):
            mod.kernel_density(np.empty((0, 2)), gx, gy, 0.1)


class TestMultiscale:
    def test_multiple_scales(self):
        coords = np.array([[float(i), float(j)] for i in range(5) for j in range(5)])
        x = np.random.default_rng(1).uniform(0, 10, 25)
        result = mod.multiscale_gi(x, coords, [1.0, 2.0])
        assert "bw_1.0000" in result
        assert "bw_2.0000" in result
        assert result["bw_1.0000"].shape == (25,)


class TestSynthetic:
    def test_shapes(self):
        field, pts, info = mod.generate_synthetic([116, 39, 117, 40], grid_size=16, n_events=100)
        assert field.shape == (16, 16)
        assert pts.shape[1] == 2
