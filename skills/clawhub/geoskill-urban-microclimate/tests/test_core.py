"""Core algorithm tests for urban-microclimate.

验证物理正确性：
- LST = base + α×ISA − β×NDVI（ISA 加热、NDVI 降温的解析解）
- 热岛强度 UHII = LST − LST_rural（解析）
- **热岛强度与 ISA 正相关**（核心验收）
- 通风指数 = SVF×(1-density) ∈ [0,1]，随密度递减
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestModelLST:
    def test_analytic(self):
        """base=25, α=10, β=6: ISA=1, NDVI=0 → 25+10 = 35"""
        isa = np.array([[1.0]], dtype=np.float32)
        ndvi = np.array([[0.0]], dtype=np.float32)
        lst = mod.model_lst(isa, ndvi, base_temp=25.0, alpha=10.0, beta=6.0)
        np.testing.assert_allclose(lst[0, 0], 35.0, atol=1e-4)

    def test_ndvi_cooling(self):
        """NDVI 升高 → LST 下降（蒸散降温）"""
        isa = np.array([[0.5, 0.5]], dtype=np.float32)
        ndvi = np.array([[0.0, 0.8]], dtype=np.float32)
        lst = mod.model_lst(isa, ndvi)
        assert lst[0, 0] > lst[0, 1]

    def test_isa_heating(self):
        """ISA 升高 → LST 上升"""
        isa = np.array([[0.1, 0.9]], dtype=np.float32)
        ndvi = np.array([[0.3, 0.3]], dtype=np.float32)
        lst = mod.model_lst(isa, ndvi)
        assert lst[0, 1] > lst[0, 0]


class TestHeatIslandIntensity:
    def test_analytic(self):
        lst = np.array([[35.0]], dtype=np.float32)
        uhii = mod.heat_island_intensity(lst, rural_reference=30.0)
        np.testing.assert_allclose(uhii[0, 0], 5.0, atol=1e-5)

    def test_cold_island_negative(self):
        lst = np.array([[28.0]], dtype=np.float32)
        uhii = mod.heat_island_intensity(lst, rural_reference=30.0)
        assert uhii[0, 0] < 0.0


class TestUHIIvsISA:
    def test_uhii_positively_correlated_with_isa(self):
        """核心验收：热岛强度与 ISA 正相关（相关系数 > 0.9）。

        固定 NDVI，LST = base + α×ISA − β×NDVI，UHII 随 ISA 线性递增。
        """
        isa = np.linspace(0.0, 1.0, 100).astype(np.float32)
        ndvi = np.full(100, 0.2, dtype=np.float32)
        lst = mod.model_lst(isa, ndvi, base_temp=25.0, alpha=10.0, beta=6.0)
        uhii = mod.heat_island_intensity(lst, rural_reference=22.0)
        corr = mod.correlation(uhii, isa)
        assert corr > 0.9

    def test_synthetic_positive_correlation(self):
        """合成场景：ISA 梯度 → UHII 与 ISA 正相关"""
        isa, ndvi, dens, svf, _ = mod.generate_synthetic([116, 39, 117, 40])
        lst = mod.model_lst(isa, ndvi)
        uhii = mod.heat_island_intensity(lst, rural_reference=22.0)
        corr = mod.correlation(uhii, isa)
        assert corr > 0.3  # 含 NDVI 协变与噪声，仍应为正相关


class TestVentilationIndex:
    def test_analytic(self):
        """SVF=0.8, density=0.5 → 0.8×0.5 = 0.4"""
        dens = np.array([[0.5]], dtype=np.float32)
        svf = np.array([[0.8]], dtype=np.float32)
        vi = mod.ventilation_index(dens, svf)
        np.testing.assert_allclose(vi[0, 0], 0.4, atol=1e-6)

    def test_range_01(self):
        rng = np.random.default_rng(0)
        dens = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        svf = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        vi = mod.ventilation_index(dens, svf)
        assert vi.min() >= 0.0
        assert vi.max() <= 1.0

    def test_decreases_with_density(self):
        svf = np.array([[0.8, 0.8]], dtype=np.float32)
        dens = np.array([[0.2, 0.9]], dtype=np.float32)
        vi = mod.ventilation_index(dens, svf)
        assert vi[0, 0] > vi[0, 1]


class TestCorrelation:
    def test_perfect_positive(self):
        x = np.arange(10, dtype=np.float64)
        y = 2 * x + 1
        np.testing.assert_allclose(mod.correlation(x, y), 1.0, atol=1e-9)

    def test_perfect_negative(self):
        x = np.arange(10, dtype=np.float64)
        y = -3 * x
        np.testing.assert_allclose(mod.correlation(x, y), -1.0, atol=1e-9)


class TestSynthetic:
    def test_shapes(self):
        isa, ndvi, dens, svf, info = mod.generate_synthetic([116, 39, 117, 40])
        assert isa.shape == (128, 128)
        assert svf.shape == (128, 128)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        back, rb = mod.read_geotiff(path)
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
        args = argparse.Namespace(
            alpha=10.0, beta=6.0, rural_temp=22.0, base_temp=25.0
        )
        mod.validate_params(args)

    def test_alpha_negative(self):
        import argparse
        args = argparse.Namespace(
            alpha=-5.0, beta=6.0, rural_temp=22.0, base_temp=25.0
        )
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_beta_negative(self):
        import argparse
        args = argparse.Namespace(
            alpha=10.0, beta=-1.0, rural_temp=22.0, base_temp=25.0
        )
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_rural_temp_out_of_range(self):
        import argparse
        args = argparse.Namespace(
            alpha=10.0, beta=6.0, rural_temp=200.0, base_temp=25.0
        )
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_base_temp_out_of_range(self):
        import argparse
        args = argparse.Namespace(
            alpha=10.0, beta=6.0, rural_temp=22.0, base_temp=-200.0
        )
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)
