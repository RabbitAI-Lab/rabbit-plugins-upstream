"""Core algorithm tests for suitability-analysis-framework."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestNormalize:
    def test_minmax_range(self):
        r = np.array([[1.0, 2.0], [3.0, 4.0]])
        norm = mod.normalize_minmax(r, positive=True)
        assert norm.min() == 0.0
        assert norm.max() == 1.0

    def test_minmax_monotonic_positive(self):
        r = np.array([[1.0, 2.0, 3.0]])
        norm = mod.normalize_minmax(r, positive=True)
        assert norm[0, 0] < norm[0, 1] < norm[0, 2]

    def test_minmax_negative_inverts(self):
        r = np.array([[1.0, 2.0, 3.0]])
        norm = mod.normalize_minmax(r, positive=False)
        assert norm[0, 0] > norm[0, 1] > norm[0, 2]

    def test_constant_returns_half(self):
        r = np.full((3, 3), 5.0)
        norm = mod.normalize_minmax(r)
        np.testing.assert_allclose(norm, 0.5)

    def test_fuzzy_membership(self):
        r = np.array([0.0, 5.0, 10.0, 15.0])
        mu = mod.fuzzy_membership(r, lo=5.0, hi=10.0, increasing=True)
        assert mu[0] == 0.0
        assert mu[1] == 0.0
        assert mu[2] == 1.0
        assert mu[3] == 1.0

    def test_fuzzy_invalid_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.fuzzy_membership(np.array([1.0]), lo=5.0, hi=5.0)


class TestAHP:
    def test_consistent_matrix_weights(self):
        """完全一致判断矩阵：权重应正比于各行标度，CR≈0。"""
        A = np.array([[1, 2, 4],
                      [1 / 2, 1, 2],
                      [1 / 4, 1 / 2, 1]])
        res = mod.ahp_weights(A)
        w = res["weights"]
        assert w.sum() == pytest.approx(1.0, abs=1e-9)
        # 一致矩阵权重 ∝ [4,2,1]
        expected = np.array([4, 2, 1]) / 7.0
        np.testing.assert_allclose(w, expected, atol=1e-6)
        assert res["CR"] < 1e-6
        assert res["consistent"]

    def test_inconsistent_matrix_cr_positive(self):
        """不一致矩阵 CR > 0。"""
        A = np.array([[1, 9, 1],
                      [1 / 9, 1, 9],
                      [1, 1 / 9, 1]])
        res = mod.ahp_weights(A)
        assert res["CR"] > 0
        assert res["weights"].sum() == pytest.approx(1.0, abs=1e-9)

    def test_non_reciprocal_raises(self):
        A = np.array([[1, 2], [3, 1]])  # 非互反
        with pytest.raises(mod.ValidationError):
            mod.ahp_weights(A)

    def test_negative_raises(self):
        A = np.array([[1, -2], [-1 / 2, 1]])
        with pytest.raises(mod.ValidationError):
            mod.ahp_weights(A)

    def test_built_matrix_consistent(self):
        """_build_ahp_matrix 生成的矩阵应完全一致。"""
        A = mod._build_ahp_matrix(4, dominance=3.0)
        res = mod.ahp_weights(A)
        assert res["CR"] < 1e-6


class TestEntropyWeights:
    def test_equal_factors_equal_weights(self):
        """完全相同的因子 → 熵权相等。"""
        f = np.random.default_rng(0).uniform(0.1, 0.9, (3, 10, 10))
        # 让 3 个因子相同
        f[1] = f[0]
        f[2] = f[0]
        res = mod.entropy_weights(f)
        np.testing.assert_allclose(res["weights"], [1 / 3, 1 / 3, 1 / 3], atol=1e-9)

    def test_diverse_factor_higher_weight(self):
        """信息量更大（差异更大）的因子应获得更高权重。"""
        rng = np.random.default_rng(1)
        uniform = np.full((1, 20, 20), 0.5)  # 无差异 → 高熵 → 低权重
        diverse = rng.uniform(0.01, 0.99, (1, 20, 20))  # 高差异 → 低熵 → 高权重
        f = np.concatenate([uniform, diverse], axis=0)
        res = mod.entropy_weights(f)
        assert res["weights"][1] > res["weights"][0]

    def test_weights_sum_one(self):
        f = np.random.default_rng(2).uniform(0.1, 0.9, (4, 12, 12))
        res = mod.entropy_weights(f)
        assert res["weights"].sum() == pytest.approx(1.0, abs=1e-9)

    def test_bad_shape_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.entropy_weights(np.ones((5, 5)))


class TestWeightedOverlay:
    def test_known_composite(self):
        """已知因子与权重 → 叠加值正确。"""
        f = np.array([[[1.0]], [[0.0]]])  # 2 因子 1 像元
        w = np.array([0.7, 0.3])
        score = mod.weighted_overlay(f, w)
        np.testing.assert_allclose(score, [[0.7]], atol=1e-12)

    def test_normalizes_weights(self):
        f = np.array([[[1.0]], [[1.0]]])
        w = np.array([2.0, 2.0])  # 未归一化
        score = mod.weighted_overlay(f, w)
        np.testing.assert_allclose(score, [[1.0]], atol=1e-12)

    def test_negative_weight_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.weighted_overlay(np.ones((2, 3, 3)), np.array([1.0, -1.0]))

    def test_count_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.weighted_overlay(np.ones((2, 3, 3)), np.array([1.0, 2.0, 3.0]))


class TestClassify:
    def test_equal_interval_classes(self):
        score = np.linspace(0, 1, 100).reshape(10, 10)
        classes, edges = mod.classify_suitability(score, n_classes=5, method="equal_interval")
        assert classes.min() >= 1
        assert classes.max() <= 5
        assert len(edges) == 6

    def test_quantile_balanced(self):
        """分位数分级每类样本数大致相等。"""
        score = np.arange(100).reshape(10, 10).astype(float)
        classes, _ = mod.classify_suitability(score, n_classes=4, method="quantile")
        uniq, counts = np.unique(classes, return_counts=True)
        assert counts.max() - counts.min() <= 2

    def test_too_few_classes_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.classify_suitability(np.ones((3, 3)), n_classes=1)

    def test_unknown_method_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.classify_suitability(np.ones((3, 3)), n_classes=3, method="natural_breaks")


class TestSynthetic:
    def test_shapes(self):
        cube, info = mod.generate_synthetic([116, 39, 117, 40], grid_size=32, n_factors=4)
        assert cube.shape == (4, 32, 32)
