"""Core algorithm tests for urban-population-estimation.

验证物理正确性：
- 建筑体积 = 面积 × 高度（解析）
- 人口分配严格守恒：Σ(density × pixel_area) = total_population
- 人口密度与权重正相关（高权重像元密度高）
- LULC 水体/植被权重为 0 → 无人
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBuildingVolume:
    def test_analytic(self):
        area = np.array([[100.0]], dtype=np.float32)
        height = np.array([[15.0]], dtype=np.float32)
        vol = mod.building_volume(area, height)
        np.testing.assert_allclose(vol[0, 0], 1500.0, atol=1e-4)

    def test_nonnegative(self):
        rng = np.random.default_rng(0)
        area = rng.uniform(-1, 100, (16, 16)).astype(np.float32)
        height = rng.uniform(-1, 50, (16, 16)).astype(np.float32)
        vol = mod.building_volume(area, height)
        assert vol.min() >= 0.0


class TestNightlightWeight:
    def test_brighter_higher_weight(self):
        nl = np.array([[0.2, 1.0]], dtype=np.float32)
        w = mod.nightlight_weight(nl)
        assert w[0, 1] > w[0, 0]

    def test_weight_range(self):
        rng = np.random.default_rng(1)
        nl = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        w = mod.nightlight_weight(nl)
        assert w.min() >= 0.1 - 1e-6
        assert w.max() <= 1.0 + 1e-6


class TestLulcWeight:
    def test_water_zero(self):
        lulc = np.array([[1, 2, 5]], dtype=np.int32)
        w = mod.lulc_weight(lulc)
        np.testing.assert_allclose(w[0, 0], 0.0, atol=1e-7)  # 水体
        np.testing.assert_allclose(w[0, 1], 1.0, atol=1e-7)  # 居住
        np.testing.assert_allclose(w[0, 2], 0.0, atol=1e-7)  # 植被


class TestAllocatePopulation:
    def test_conservation(self):
        """Σ(density × pixel_area) = total_population（严格守恒）"""
        rng = np.random.default_rng(2)
        weight = rng.uniform(0, 10, (32, 32))
        total = 50000.0
        pixel_area = 25.0
        density = mod.allocate_population(weight, total, pixel_area)
        estimated = float(np.sum(density) * pixel_area)
        np.testing.assert_allclose(estimated, total, rtol=1e-9)

    def test_conservation_various_totals(self):
        weight = np.ones((10, 10))
        for total in [1000.0, 1e6, 7.5]:
            density = mod.allocate_population(weight, total, pixel_area=1.0)
            np.testing.assert_allclose(np.sum(density), total, rtol=1e-9)

    def test_density_proportional_to_weight(self):
        """权重高一倍的像元，人口密度也高一倍"""
        weight = np.array([[1.0, 2.0]], dtype=np.float64)
        density = mod.allocate_population(weight, total_population=300.0, pixel_area=1.0)
        np.testing.assert_allclose(density[0, 1] / density[0, 0], 2.0, atol=1e-9)

    def test_zero_weight_uniform_fallback(self):
        """全零权重 → 均匀分配，仍守恒"""
        weight = np.zeros((4, 4))
        total = 160.0
        density = mod.allocate_population(weight, total, pixel_area=1.0)
        np.testing.assert_allclose(np.sum(density), total, rtol=1e-9)
        np.testing.assert_allclose(density, total / 16.0, atol=1e-9)

    def test_nonnegative(self):
        rng = np.random.default_rng(3)
        weight = rng.uniform(0, 5, (16, 16))
        density = mod.allocate_population(weight, 1000.0, 1.0)
        assert density.min() >= 0.0


class TestSynthetic:
    def test_shapes(self):
        h, nl, lulc, info = mod.generate_synthetic([116, 39, 117, 40])
        assert h.shape == (128, 128)
        assert nl.shape == (128, 128)
        assert lulc.shape == (128, 128)
        assert info["total_population"] == 100000.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (1, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb, _ = mod.read_geotiff(path)
        np.testing.assert_allclose(back, cube, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/file.tif")


class TestValidateBbox:
    def test_valid(self):
        b = mod.validate_bbox([116.0, 39.0, 117.0, 40.0])
        assert b == [116.0, 39.0, 117.0, 40.0]

    def test_w_ge_e_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.validate_bbox([117.0, 39.0, 116.0, 40.0])

    def test_s_ge_n_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.validate_bbox([116.0, 40.0, 117.0, 39.0])

    def test_zero_area_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.validate_bbox([116.0, 39.0, 116.0, 40.0])

    def test_lat_out_of_range_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.validate_bbox([116.0, 39.0, 117.0, 95.0])

    def test_lon_out_of_range_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.validate_bbox([200.0, 39.0, 210.0, 40.0])

    def test_none_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.validate_bbox(None)

    def test_wrong_length_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.validate_bbox([116.0, 39.0, 117.0])


class TestValidateParams:
    def test_valid(self):
        import argparse
        args = argparse.Namespace(total_population=100000.0, pixel_size=10.0)
        mod.validate_params(args)

    def test_total_population_negative(self):
        import argparse
        args = argparse.Namespace(total_population=-1000.0, pixel_size=10.0)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_pixel_size_zero(self):
        import argparse
        args = argparse.Namespace(total_population=100000.0, pixel_size=0.0)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_pixel_size_negative(self):
        import argparse
        args = argparse.Namespace(total_population=100000.0, pixel_size=-5.0)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)
