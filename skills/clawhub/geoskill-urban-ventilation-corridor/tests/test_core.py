"""Core algorithm tests for urban-ventilation-corridor.

验证物理正确性：
- 粗糙度随建筑高度/密度单调递增（Macdonald 式解析）
- 通风潜力 ∈ (0,1]，随粗糙度单调递减，exp 解析解
- Dijkstra 最小阻力路径沿低阻力廊道行走，代价等于解析最小值
"""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestAerodynamicRoughness:
    def test_analytic(self):
        """z0 = coeff × h × λp = 0.1 × 30 × 0.5 = 1.5"""
        h = np.array([[30.0]], dtype=np.float32)
        l = np.array([[0.5]], dtype=np.float32)
        z0 = mod.aerodynamic_roughness(h, l, coeff=0.1)
        np.testing.assert_allclose(z0[0, 0], 1.5, atol=1e-5)

    def test_monotonic_in_height(self):
        l = np.array([[0.5, 0.5]], dtype=np.float32)
        h = np.array([[10.0, 40.0]], dtype=np.float32)
        z0 = mod.aerodynamic_roughness(h, l)
        assert z0[0, 1] > z0[0, 0]

    def test_zero_when_no_building(self):
        h = np.array([[30.0]], dtype=np.float32)
        l = np.array([[0.0]], dtype=np.float32)
        z0 = mod.aerodynamic_roughness(h, l)
        np.testing.assert_allclose(z0[0, 0], 0.0, atol=1e-7)


class TestVentilationPotential:
    def test_range_01(self):
        z0 = np.linspace(0, 10, 50).astype(np.float32).reshape(5, 10)
        vp = mod.ventilation_potential(z0)
        assert vp.min() > 0.0
        assert vp.max() <= 1.0

    def test_zero_roughness_vp_one(self):
        z0 = np.array([[0.0]], dtype=np.float32)
        vp = mod.ventilation_potential(z0, k=0.5)
        np.testing.assert_allclose(vp[0, 0], 1.0, atol=1e-6)

    def test_exp_analytic(self):
        """VP = exp(-k×z0)，k=0.5, z0=2 → exp(-1)"""
        z0 = np.array([[2.0]], dtype=np.float32)
        vp = mod.ventilation_potential(z0, k=0.5)
        np.testing.assert_allclose(vp[0, 0], np.exp(-1.0), atol=1e-6)

    def test_monotonic_decreasing(self):
        z0 = np.array([[0.5, 1.0, 2.0, 5.0]], dtype=np.float32)
        vp = mod.ventilation_potential(z0)
        assert vp[0, 0] > vp[0, 1] > vp[0, 2] > vp[0, 3]


class TestLeastCostPath:
    def test_corridor_follows_low_cost_band(self):
        """低阻力横贯廊道 → 路径沿廊道行走，代价等于解析最小值。"""
        n = 21
        cost = np.ones((n, n), dtype=np.float64)
        cost[10, :] = 0.05  # 第 10 行低阻力廊道
        path, total = mod.least_cost_path(cost, (10, 0), (10, n - 1))
        # 路径应沿第 10 行直线行走
        rows = [p[0] for p in path]
        assert all(r == 10 for r in rows)
        # 代价 = 起点 cost(0.05) + 20 步 × 0.05 = 1.05
        np.testing.assert_allclose(total, 21 * 0.05, atol=1e-6)

    def test_path_connects_endpoints(self):
        cost = np.ones((10, 10), dtype=np.float64)
        path, total = mod.least_cost_path(cost, (0, 0), (9, 9))
        assert path[0] == (0, 0)
        assert path[-1] == (9, 9)
        # 8 邻域单位代价，对角最短 = 9×√2 + 起点 cost(1)
        np.testing.assert_allclose(total, 1.0 + 9 * 1.4142135623730951, atol=1e-6)

    def test_path_avoids_high_cost_barrier(self):
        """高阻力墙（留一个缺口）→ 路径绕行缺口。"""
        n = 15
        cost = np.ones((n, n), dtype=np.float64)
        cost[:, 7] = 100.0   # 第 7 列高阻力墙
        cost[3, 7] = 0.05    # 唯一缺口
        path, total = mod.least_cost_path(cost, (7, 0), (7, n - 1))
        cols_visited_at_wall = [p[0] for p in path if p[1] == 7]
        assert 3 in cols_visited_at_wall  # 必须经过缺口行 3
        assert total < 50.0  # 不应穿越高阻力墙


class TestPathToGeoJSON:
    def test_geojson_structure(self):
        path = [(0, 0), (0, 1), (0, 2)]
        bbox = [116.0, 39.0, 117.0, 40.0]
        gj = mod.path_to_geojson(path, bbox, 10, 10)
        assert gj["type"] == "FeatureCollection"
        assert len(gj["features"]) == 1
        assert gj["features"][0]["geometry"]["type"] == "LineString"
        assert len(gj["features"][0]["geometry"]["coordinates"]) == 3

    def test_empty_path(self):
        gj = mod.path_to_geojson([], [116, 39, 117, 40], 10, 10)
        assert gj["features"] == []


class TestSynthetic:
    def test_shapes(self):
        h, d, info = mod.generate_synthetic([116, 39, 117, 40])
        assert h.shape == (128, 128)
        assert d.shape == (128, 128)
        assert "corridor_row" in info


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
    def test_valid(self):
        import argparse
        args = argparse.Namespace(roughness_coeff=0.1, decay_k=0.5)
        mod.validate_params(args)

    def test_roughness_coeff_negative(self):
        import argparse
        args = argparse.Namespace(roughness_coeff=-1.0, decay_k=0.5)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_decay_k_negative(self):
        import argparse
        args = argparse.Namespace(roughness_coeff=0.1, decay_k=-0.5)
        with pytest.raises(mod.ValidationError):
            mod.validate_params(args)

    def test_decay_k_zero_allowed(self):
        """decay_k=0 合法（exp(0)=1.0，无衰减）"""
        import argparse
        args = argparse.Namespace(roughness_coeff=0.1, decay_k=0.0)
        mod.validate_params(args)  # should not raise

    def test_roughness_coeff_zero_allowed(self):
        """roughness_coeff=0 合法（z0=0）"""
        import argparse
        args = argparse.Namespace(roughness_coeff=0.0, decay_k=0.5)
        mod.validate_params(args)  # should not raise
