"""Core algorithm tests for post-disaster-reconstruction."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as rc


class TestClassifyProgress:
    def test_all_categories(self):
        """五种进度类别各取一个代表像元，编码正确。"""
        B = np.array([[0.9, 0.9, 0.9, 0.9, 0.1]])
        D = np.array([[0.1, 0.9, 0.1, 0.1, 0.1]])
        R = np.array([[0.1, 0.9, 0.4, 0.9, 0.1]])
        cat = rc.classify_progress(B, D, R, thr_build=0.5, thr_damage=0.3)
        # destroyed, unchanged, under_construction, rebuilt, non_building
        assert cat[0].tolist() == [2, 1, 3, 4, 0]

    def test_categories_mutually_exclusive(self):
        rng = np.random.default_rng(0)
        B = rng.uniform(0, 1, (20, 20))
        D = rng.uniform(0, 1, (20, 20))
        R = rng.uniform(0, 1, (20, 20))
        cat = rc.classify_progress(B, D, R)
        assert cat.min() >= 0 and cat.max() <= 4
        fracs = rc.category_fractions(cat)
        assert abs(sum(fracs.values()) - 1.0) < 1e-9

    def test_destroyed_then_rebuilt_over_time(self):
        """毁坏像元随重建期强度上升：destroyed → under_construction → rebuilt。"""
        B = np.full((1, 3), 0.9)
        D = np.full((1, 3), 0.1)
        R = np.array([[0.1, 0.4, 0.9]])  # 低 / 中 / 高 重建强度
        cat = rc.classify_progress(B, D, R, thr_build=0.5, thr_damage=0.3)
        assert cat[0].tolist() == [2, 3, 4]

    def test_shape_mismatch_raises(self):
        with pytest.raises(rc.ValidationError):
            rc.classify_progress(np.zeros((4, 4)), np.zeros((4, 5)), np.zeros((4, 4)))

    def test_bad_thresholds_raise(self):
        z = np.zeros((4, 4))
        with pytest.raises(rc.ValidationError):
            rc.classify_progress(z, z, z, thr_build=0.3, thr_damage=0.5)


class TestRebuiltMonotonic:
    def test_rebuilt_increases_with_recovery(self):
        """固定灾前/损毁，重建强度越高 → rebuilt 像元越多（单调不减）。"""
        n = 64
        B = np.full((1, n), 0.9)
        D = np.full((1, n), 0.1)
        prev = -1
        counts = []
        for recovery in (0.0, 0.2, 0.5, 0.8, 1.0):
            R = D + recovery * (B - D)
            cat = rc.classify_progress(B, D, R, thr_build=0.5, thr_damage=0.3)
            c = int(np.count_nonzero(cat == 4))
            counts.append(c)
            assert c >= prev
            prev = c
        assert counts[0] == 0       # 无恢复 → 无 rebuilt
        assert counts[-1] == n      # 完全恢复 → 全部 rebuilt


class TestReconstructionProgress:
    def test_endpoints(self):
        B = np.array([0.9, 0.9])
        D = np.array([0.1, 0.1])
        R = np.array([0.1, 0.9])  # R=D / R=B
        prog = rc.reconstruction_progress(B, D, R)
        assert abs(prog[0] - 0.0) < 1e-6
        assert abs(prog[1] - 1.0) < 1e-6

    def test_linear_intermediate(self):
        B = np.full(5, 0.9); D = np.full(5, 0.1)
        R = np.array([0.1, 0.3, 0.5, 0.7, 0.9])
        prog = rc.reconstruction_progress(B, D, R)
        np.testing.assert_allclose(prog, [0.0, 0.25, 0.5, 0.75, 1.0], atol=1e-6)

    def test_monotonic_and_bounded(self):
        rng = np.random.default_rng(1)
        B = rng.uniform(0.5, 1, (16, 16))
        D = rng.uniform(0, 0.4, (16, 16))
        Rlo = D.copy()
        Rhi = np.clip(D + 0.5, 0, 1)
        p_lo = rc.reconstruction_progress(B, D, Rlo)
        p_hi = rc.reconstruction_progress(B, D, Rhi)
        assert p_lo.min() >= 0.0 and p_hi.max() <= 1.0
        assert p_hi.mean() >= p_lo.mean() - 1e-9

    def test_non_destroyed_is_zero(self):
        """B≈D（未毁坏）→ 进度为 0。"""
        B = np.full((4, 4), 0.8); D = np.full((4, 4), 0.8); R = np.full((4, 4), 0.8)
        prog = rc.reconstruction_progress(B, D, R)
        assert np.allclose(prog, 0.0)


class TestCategoryFractions:
    def test_sums_to_one(self):
        cat = np.array([[0, 1, 2], [3, 4, 0]])
        fr = rc.category_fractions(cat)
        assert abs(sum(fr.values()) - 1.0) < 1e-9
        assert fr["non_building"] == pytest.approx(2 / 6)


class TestSynthetic:
    def test_shapes_and_recovery(self):
        layers, info = rc.generate_synthetic([116, 39, 117, 40], recovery=0.6)
        for k in ("before", "damage", "rebuild"):
            assert layers[k].shape == (64, 64)
            assert layers[k].min() >= 0.0 and layers[k].max() <= 1.0
        assert info["recovery"] == 0.6

    def test_more_recovery_more_rebuilt(self):
        """合成场景：恢复程度越高，rebuilt 比例越高。"""
        def rebuilt_frac(recovery):
            layers, _ = rc.generate_synthetic([116, 39, 117, 40], recovery=recovery, seed=5)
            cat = rc.classify_progress(layers["before"], layers["damage"], layers["rebuild"])
            return float(np.mean(cat == 4))
        assert rebuilt_frac(0.9) >= rebuilt_frac(0.2)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        p = str(tmp_path / "p.tif")
        rc.write_geotiff(p, cube, bbox)
        back, bb = rc.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(rc.UsageError):
            rc.read_geotiff("/nonexistent/p.tif")
