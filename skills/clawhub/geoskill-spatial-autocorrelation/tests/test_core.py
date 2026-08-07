"""Core algorithm tests for spatial-autocorrelation."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestWeights:
    def test_rook_row_stochastic(self):
        W = mod.rook_weights((4, 4))
        # 内部行和为 1
        sums = W.sum(axis=1)
        np.testing.assert_allclose(sums, 1.0, atol=1e-12)

    def test_rook_no_self(self):
        W = mod.rook_weights((3, 3))
        np.testing.assert_allclose(np.diag(W), 0.0, atol=1e-12)

    def test_knn_shape_and_rows(self):
        rng = np.random.default_rng(0)
        coords = rng.uniform(0, 1, (20, 2))
        W = mod.knn_weights(coords, k=5)
        assert W.shape == (20, 20)
        np.testing.assert_allclose(W.sum(1), 1.0, atol=1e-12)


class TestGlobalMoran:
    def test_random_near_zero(self):
        """随机分布 Moran's I 应接近期望值 -1/(n-1)。"""
        rng = np.random.default_rng(1)
        field = rng.normal(0, 1, (20, 20))
        W = mod.rook_weights((20, 20))
        res = mod.global_morans_i(field.ravel(), W)
        assert abs(res["I"]) < 0.15  # 接近 0

    def test_clustered_positive(self):
        """聚集分布 Moran's I 应显著为正。"""
        field = np.zeros((20, 20))
        field[:10, :10] = 5.0
        field[10:, 10:] = 5.0
        W = mod.rook_weights((20, 20))
        res = mod.global_morans_i(field.ravel(), W)
        assert res["I"] > 0.3

    def test_checkerboard_negative(self):
        """棋盘格（完全离散）Moran's I 应为负。"""
        yy, xx = np.mgrid[0:20, 0:20]
        field = ((xx + yy) % 2).astype(np.float64)
        W = mod.rook_weights((20, 20))
        res = mod.global_morans_i(field.ravel(), W)
        assert res["I"] < 0

    def test_p_value_range(self):
        rng = np.random.default_rng(2)
        field = rng.normal(0, 1, (15, 15))
        W = mod.rook_weights((15, 15))
        res = mod.global_morans_i(field.ravel(), W)
        assert 0 <= res["p_value"] <= 1

    def test_shape_mismatch_raises(self):
        W = mod.rook_weights((3, 3))
        with pytest.raises(mod.ValidationError):
            mod.global_morans_i(np.zeros(5), W)


class TestLocalMoran:
    def test_lisa_shape(self):
        rng = np.random.default_rng(3)
        field = rng.normal(0, 1, (12, 12))
        W = mod.rook_weights((12, 12))
        lisa = mod.local_morans_i(field.ravel(), W)
        assert lisa.shape == (144,)

    def test_lisa_positive_in_cluster(self):
        """高值聚集中心局部 I 应为正。"""
        field = np.zeros((10, 10))
        field[4:6, 4:6] = 10.0  # 中心高值块
        W = mod.rook_weights((10, 10))
        lisa = mod.local_morans_i(field.ravel(), W).reshape(10, 10)
        assert lisa[4, 4] > 0


class TestGiStar:
    def test_hotspot_positive_zscore(self):
        """高值区 Gi* z 得分应为正。"""
        field = np.zeros((15, 15))
        field[6:9, 6:9] = 100.0
        W = mod.rook_weights((15, 15))
        gi = mod.getis_ord_gi_star(field.ravel(), W).reshape(15, 15)
        assert gi[7, 7] > 2.0  # 显著热点

    def test_coldspot_negative_zscore(self):
        """低值包围的区域 Gi* z 得分应为负。"""
        field = np.ones((15, 15)) * 100.0
        field[6:9, 6:9] = 0.0
        W = mod.rook_weights((15, 15))
        gi = mod.getis_ord_gi_star(field.ravel(), W).reshape(15, 15)
        assert gi[7, 7] < -2.0


class TestMonteCarlo:
    def test_clustered_significant(self):
        """聚集场蒙特卡洛伪 p 应较小。"""
        field = np.zeros((15, 15))
        field[:7, :7] = 5.0
        field[8:, 8:] = 5.0
        W = mod.rook_weights((15, 15))
        mc = mod.monte_carlo_morans_i(field.ravel(), W, permutations=99)
        assert mc["pseudo_p"] < 0.05

    def test_random_not_significant(self):
        """随机场蒙特卡洛伪 p 应偏大。"""
        rng = np.random.default_rng(4)
        field = rng.normal(0, 1, (15, 15))
        W = mod.rook_weights((15, 15))
        mc = mod.monte_carlo_morans_i(field.ravel(), W, permutations=99)
        assert mc["pseudo_p"] > 0.01

    def test_pseudo_p_range(self):
        rng = np.random.default_rng(5)
        field = rng.normal(0, 1, (10, 10))
        W = mod.rook_weights((10, 10))
        mc = mod.monte_carlo_morans_i(field.ravel(), W, permutations=49)
        assert 0 < mc["pseudo_p"] <= 1.0


class TestSynthetic:
    def test_modes(self):
        for mode in ["cluster", "random", "gradient"]:
            field, info = mod.generate_synthetic([116, 39, 117, 40], grid_size=16, mode=mode)
            assert field.shape == (16, 16)
            assert info["mode"] == mode
