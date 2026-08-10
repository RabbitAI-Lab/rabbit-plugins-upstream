"""Core algorithm tests for urban-growth-boundary.

验证物理正确性：
- 扩张速率 = (A2-A1)/A1/years（解析）
- 约束惩罚 ∈ [0,1]，随坡度递增
- 增长适宜性 = tendency × (1-penalty)，陡坡+生态 → 近 0
- 适宜性 ∈ [0,1]
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestExpansionRate:
    def test_analytic(self):
        """100 → 150 over 10 yr → (50/100)/10 = 0.05/yr"""
        np.testing.assert_allclose(
            mod.expansion_rate(100.0, 150.0, 10.0), 0.05, atol=1e-9)

    def test_zero_area(self):
        assert mod.expansion_rate(0.0, 100.0, 10.0) == 0.0

    def test_zero_years(self):
        assert mod.expansion_rate(100.0, 150.0, 0.0) == 0.0

    def test_shrinkage_negative(self):
        """建成区萎缩 → 负速率"""
        assert mod.expansion_rate(100.0, 80.0, 10.0) < 0.0


class TestConstraintPenalty:
    def test_range_01(self):
        rng = np.random.default_rng(0)
        s = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        c = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        e = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        p = mod.constraint_penalty(s, c, e)
        assert p.min() >= 0.0
        assert p.max() <= 1.0 + 1e-6

    def test_steep_slope_high_penalty(self):
        steep = np.array([[0.9]], dtype=np.float32)
        flat = np.array([[0.0]], dtype=np.float32)
        zero = np.array([[0.0]], dtype=np.float32)
        p_steep = mod.constraint_penalty(steep, zero, zero)
        p_flat = mod.constraint_penalty(flat, zero, zero)
        assert p_steep[0, 0] > p_flat[0, 0]

    def test_all_max_penalty_one(self):
        s = c = e = np.array([[1.0]], dtype=np.float32)
        p = mod.constraint_penalty(s, c, e, w_slope=0.4, w_crop=0.3, w_eco=0.3)
        np.testing.assert_allclose(p[0, 0], 1.0, atol=1e-6)


class TestGrowthSuitability:
    def test_analytic(self):
        """tendency=0.8, penalty=0.5 → 0.8×0.5 = 0.4"""
        t = np.array([[0.8]], dtype=np.float32)
        p = np.array([[0.5]], dtype=np.float32)
        s = mod.growth_suitability(t, p)
        np.testing.assert_allclose(s[0, 0], 0.4, atol=1e-6)

    def test_range_01(self):
        rng = np.random.default_rng(1)
        t = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        p = rng.uniform(0, 1, (16, 16)).astype(np.float32)
        s = mod.growth_suitability(t, p)
        assert s.min() >= 0.0
        assert s.max() <= 1.0

    def test_protected_steep_near_zero(self):
        """陡坡 + 生态 → penalty≈1 → 适宜性≈0"""
        t = np.array([[0.9]], dtype=np.float32)
        p = np.array([[1.0]], dtype=np.float32)
        s = mod.growth_suitability(t, p)
        assert s[0, 0] < 0.01

    def test_decreases_with_penalty(self):
        t = np.array([[0.8, 0.8]], dtype=np.float32)
        p = np.array([[0.1, 0.7]], dtype=np.float32)
        s = mod.growth_suitability(t, p)
        assert s[0, 0] > s[0, 1]


class TestSlopeFromDem:
    def test_flat_zero_slope(self):
        dem = np.full((16, 16), 100.0, dtype=np.float32)
        s = mod.slope_from_dem(dem)
        np.testing.assert_allclose(s, 0.0, atol=1e-5)

    def test_range_01(self):
        rng = np.random.default_rng(2)
        dem = rng.uniform(0, 100, (16, 16)).astype(np.float32)
        s = mod.slope_from_dem(dem)
        assert s.min() >= 0.0
        assert s.max() <= 1.0


class TestExpansionTendency:
    def test_new_growth_high_tendency(self):
        """新增建成区附近趋势高"""
        b1 = np.zeros((32, 32), dtype=np.float32)
        b2 = np.zeros((32, 32), dtype=np.float32)
        b1[14:18, 14:18] = 1.0
        b2[14:18, 14:18] = 1.0
        b2[14:18, 20:26] = 1.0  # 向东新增
        tend = mod.expansion_tendency(b1, b2, smooth=3)
        assert tend.max() <= 1.0 + 1e-6
        # 新增区趋势 > 老建成区（无新增）
        assert tend[16, 22] > tend[16, 5]


class TestSynthetic:
    def test_shapes(self):
        b1, b2, s, c, e, info = mod.generate_synthetic([116, 39, 117, 40])
        assert b1.shape == (128, 128)
        assert b2.shape == (128, 128)
        # t2 建成区 ≥ t1
        assert (b2 > 0).sum() >= (b1 > 0).sum()


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (2, 16, 16)).astype(np.float32)
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
    def test_valid(self, monkeypatch):
        import argparse
        args = argparse.Namespace(threshold=0.3, years=10.0)
        mod.validate_params(args)  # should not raise

    def test_threshold_negative(self):
        import argparse
        args = argparse.Namespace(threshold=-0.5, years=10.0)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_threshold_above_one(self):
        import argparse
        args = argparse.Namespace(threshold=1.5, years=10.0)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_years_zero(self):
        import argparse
        args = argparse.Namespace(threshold=0.3, years=0.0)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_years_negative(self):
        import argparse
        args = argparse.Namespace(threshold=0.3, years=-5.0)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)
