"""Core algorithm tests for snow-ice-mapping."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestComputeNDSI:
    def test_high_green_low_swir_positive(self):
        green = np.full((8, 8), 0.80, dtype=np.float32)
        swir = np.full((8, 8), 0.10, dtype=np.float32)
        ndsi = mod.compute_ndsi(green, swir)
        # (0.8-0.1)/(0.8+0.1) = 0.7778
        np.testing.assert_allclose(ndsi, 0.7778, atol=1e-3)

    def test_equal_bands_zero(self):
        a = np.full((8, 8), 0.30, dtype=np.float32)
        ndsi = mod.compute_ndsi(a, a.copy())
        np.testing.assert_allclose(ndsi, 0.0, atol=1e-6)

    def test_zero_denominator_returns_zero(self):
        green = np.zeros((4, 4), dtype=np.float32)
        swir = np.zeros((4, 4), dtype=np.float32)
        ndsi = mod.compute_ndsi(green, swir)
        np.testing.assert_allclose(ndsi, 0.0, atol=1e-6)

    def test_output_range(self):
        rng = np.random.default_rng(0)
        green = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        swir = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        ndsi = mod.compute_ndsi(green, swir)
        assert ndsi.min() >= -1.0 and ndsi.max() <= 1.0


class TestDetectSnow:
    def test_synthetic_recovers_snow(self):
        cube, temperature, info, truth = mod.generate_synthetic(
            [116, 39, 117, 40], green_index=1, swir_index=4,
        )
        snow, ndsi = mod.detect_snow(cube, green_index=1, swir_index=4,
                                     ndsi_threshold=0.4)
        # 真值雪区应被高比例检出
        inter = np.count_nonzero((truth == 1) & snow)
        recall = inter / max(np.count_nonzero(truth == 1), 1)
        assert recall > 0.9

    def test_band_index_out_of_range_raises(self):
        cube = np.random.rand(3, 8, 8).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.detect_snow(cube, green_index=1, swir_index=4)  # only 3 bands

    def test_2d_cube_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.detect_snow(np.zeros((8, 8), dtype=np.float32))

    def test_temperature_constraint(self):
        """温度约束应排除"高 NDSI 但温暖"的像元。"""
        cube, temperature, info, truth = mod.generate_synthetic(
            [116, 39, 117, 40],
        )
        # 把雪区温度人为调高（> 阈值），应不再判为雪
        hot_temp = temperature.copy()
        hot_temp[truth == 1] = 300.0
        snow, _ = mod.detect_snow(cube, ndsi_threshold=0.4,
                                  temperature=hot_temp, temp_threshold=273.15)
        assert np.count_nonzero(snow) == 0


class TestPixelArea:
    def test_positive(self):
        a = mod.pixel_area_km2([116.0, 39.0, 117.0, 40.0], 100, 100)
        assert a > 0

    def test_latitude_shrinks_area(self):
        """高纬度经度收缩 → 单像元面积更小。"""
        low = mod.pixel_area_km2([116.0, 10.0, 117.0, 11.0], 100, 100)
        high = mod.pixel_area_km2([116.0, 60.0, 117.0, 61.0], 100, 100)
        assert high < low


class TestSnowAreaStats:
    def test_fractions(self):
        mask = np.zeros((10, 10), dtype=np.uint8)
        mask[0:5, :] = 1  # 一半雪
        stats = mod.snow_area_stats(mask, [116.0, 39.0, 117.0, 40.0])
        assert stats["snow_pixels"] == 50
        assert stats["total_pixels"] == 100
        assert abs(stats["snow_fraction"] - 0.5) < 1e-6
        assert stats["snow_area_km2"] > 0


class TestSynthetic:
    def test_shape_and_range(self):
        cube, temperature, info, truth = mod.generate_synthetic([116, 39, 117, 40])
        assert cube.ndim == 3
        assert cube.shape[0] == 6
        assert cube.min() >= 0.0 and cube.max() <= 1.0
        assert temperature.shape == cube.shape[1:]
        assert truth.shape == cube.shape[1:]
