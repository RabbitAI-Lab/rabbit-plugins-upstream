"""Core algorithm tests for habitat-suitability-modeling (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


@pytest.fixture(scope="module")
def scene():
    stack, presence, info = M.generate_synthetic([116, 39, 117, 40], width=96, height=96, seed=7)
    env_norm, _, _ = M.normalize_stack(stack)
    X, y = M.build_samples(env_norm, presence)
    return env_norm, X, y, presence


class TestNormalize:
    def test_bounds(self):
        rng = np.random.default_rng(0)
        stack = rng.uniform(-10, 10, (4, 16, 16)).astype(np.float32)
        n, mins, maxs = M.normalize_stack(stack)
        assert n.min() >= 0.0 and n.max() <= 1.0
        assert mins.shape == (4,) and maxs.shape == (4,)

    def test_constant_band_zero(self):
        stack = np.full((2, 8, 8), 5.0, dtype=np.float32)
        n, _, _ = M.normalize_stack(stack)
        assert np.all(n == 0.0)


class TestFit:
    def test_unknown_model_raises(self, scene):
        _, X, y, _ = scene
        with pytest.raises(M.UsageError):
            M.fit_suitability(X, y, model="bogus")

    def test_single_class_raises(self):
        X = np.random.default_rng(1).uniform(0, 1, (20, 3)).astype(np.float32)
        y = np.ones(20, dtype=np.int32)
        with pytest.raises(M.ValidationError):
            M.fit_suitability(X, y, model="rf")


class TestSuitability:
    @pytest.mark.parametrize("model", ["rf", "logreg"])
    def test_probability_range(self, scene, model):
        env_norm, X, y, _ = scene
        m = M.fit_suitability(X, y, model=model)
        s = M.predict_suitability(m, env_norm)
        assert s.min() >= 0.0
        assert s.max() <= 1.0
        assert s.shape == env_norm.shape[1:]

    def test_learns_signal_presence_higher(self, scene):
        """presence 像元的平均适宜性应高于 absence。"""
        env_norm, X, y, presence = scene
        m = M.fit_suitability(X, y, model="rf")
        s = M.predict_suitability(m, env_norm)
        assert float(s[presence == 1].mean()) > float(s[presence == 0].mean())

    def test_cross_val_auc_above_chance(self, scene):
        _, X, y, _ = scene
        auc = M.cross_val_auc(X, y, model="rf")
        assert auc > 0.6  # 强 ndvi 信号，3 折 CV AUC 应明显高于 0.5 随机水平


class TestImportance:
    @pytest.mark.parametrize("model", ["rf", "logreg"])
    def test_sums_to_one(self, scene, model):
        _, X, y, _ = scene
        m = M.fit_suitability(X, y, model=model)
        imp = M.variable_importance(m, M.ENV_BANDS)
        assert abs(sum(imp.values()) - 1.0) < 1e-6
        assert all(v >= 0.0 for v in imp.values())

    def test_ndvi_dominant(self, scene):
        """生态位由 ndvi 驱动，RF 的 ndvi 重要度应最高。"""
        _, X, y, _ = scene
        m = M.fit_suitability(X, y, model="rf")
        imp = M.variable_importance(m, M.ENV_BANDS)
        assert max(imp, key=imp.get) == "ndvi"


class TestSynthetic:
    def test_shapes(self):
        stack, presence, info = M.generate_synthetic([116, 39, 117, 40], width=64, height=64)
        assert stack.shape == (4, 64, 64)
        assert presence.shape == (64, 64)
        assert set(np.unique(presence)).issubset({0, 1})
        assert 0.05 < info["prevalence"] < 0.95
