"""Core algorithm tests for cloud-shadow-detection."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBrightness:
    def test_mean_over_bands(self):
        cube = np.stack([np.full((4, 4), 0.2), np.full((4, 4), 0.4)])
        b = mod.brightness(cube)
        assert b.shape == (4, 4)
        np.testing.assert_allclose(b, 0.3, atol=1e-6)


class TestShadowOffset:
    def test_north_sun_shadow_south(self):
        # 太阳在正北 (azimuth 0) → 阴影投向正南 → 行增大 (dy>0)
        dy, dx = mod.shadow_offset(0.0, 10.0)
        assert dy > 0
        assert dx == 0

    def test_offset_magnitude(self):
        dy, dx = mod.shadow_offset(90.0, 10.0)
        assert abs(dx) == 10 or abs(dy) == 10  # 东/西向为主


class TestDetectCloud:
    def test_bright_detected(self):
        cube = np.full((4, 16, 16), 0.2, dtype=np.float32)
        cube[:, 0:4, 0:4] = 0.85  # 亮云块
        cloud = mod.detect_cloud(cube, cloud_threshold=0.3)
        assert cloud[0:4, 0:4].all()
        assert not cloud[8:16, 8:16].any()


class TestDetectCloudShadow:
    def test_synthetic_recovers_cloud_and_shadow(self):
        bbox = [116, 39, 117, 40]
        cube, info, truth = mod.generate_synthetic(
            bbox, solar_azimuth_deg=160.0, shift_pixels=10.0,
        )
        mask, stats = mod.detect_cloud_shadow(
            cube, cloud_threshold=0.3, shadow_threshold=0.1,
            solar_azimuth_deg=160.0, shift_pixels=10.0,
        )
        # 云与影都应被检出
        assert stats["cloud_pixels"] > 0
        assert stats["shadow_pixels"] > 0
        # 检出云区与真值云区高度重合
        truth_cloud = truth == mod.CLOUD
        detected_cloud = mask == mod.CLOUD
        inter = np.count_nonzero(truth_cloud & detected_cloud)
        assert inter / np.count_nonzero(truth_cloud) > 0.9

    def test_mask_values_only_012(self):
        cube = np.random.uniform(0, 1, (4, 32, 32)).astype(np.float32)
        mask, _ = mod.detect_cloud_shadow(cube)
        assert set(np.unique(mask)).issubset({0, 1, 2})

    def test_fractions_sum_to_one(self):
        cube = np.random.uniform(0, 1, (4, 32, 32)).astype(np.float32)
        _, stats = mod.detect_cloud_shadow(cube)
        total = (stats["cloud_fraction"] + stats["shadow_fraction"]
                 + stats["clear_pixels"] / stats["total_pixels"])
        assert abs(total - 1.0) < 1e-3

    def test_empty_cube_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.detect_cloud_shadow(np.zeros((0,)))


class TestSynthetic:
    def test_shape_and_range(self):
        cube, info, truth = mod.generate_synthetic([116, 39, 117, 40])
        assert cube.ndim == 3
        assert cube.shape[0] == 4
        assert cube.min() >= 0.0 and cube.max() <= 1.0
        assert truth.shape == cube.shape[1:]
