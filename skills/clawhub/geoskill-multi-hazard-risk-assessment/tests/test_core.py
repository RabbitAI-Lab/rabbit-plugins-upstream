"""Core algorithm tests for multi-hazard-risk-assessment."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as mh


class TestNormalize:
    def test_range_01(self):
        a = np.random.uniform(-50, 500, (32, 32))
        n = mh.normalize01(a)
        assert n.min() >= 0.0
        assert n.max() <= 1.0
        assert abs(n.max() - 1.0) < 1e-5

    def test_constant_returns_zero(self):
        a = np.full((8, 8), 3.14)
        n = mh.normalize01(a)
        assert np.allclose(n, 0.0)


class TestSingleRisk:
    def test_bounded_01(self):
        h = np.random.uniform(0, 10, (32, 32))
        e = np.random.uniform(0, 100, (32, 32))
        v = np.random.uniform(0, 1, (32, 32))
        r = mh.compute_single_risk(h, e, v)
        assert r.min() >= 0.0
        assert r.max() <= 1.0

    def test_risk_monotonic_in_hazard(self):
        """加大危险度，平均风险不得下降（暴露/脆弱性固定）。"""
        rng = np.random.default_rng(1)
        e = rng.uniform(1, 100, (32, 32))
        v = rng.uniform(0.1, 1, (32, 32))
        h_lo = rng.uniform(0, 5, (32, 32))
        h_hi = h_lo + 10.0  # 全面抬升危险度
        r_lo = mh.compute_single_risk(h_lo, e, v)
        r_hi = mh.compute_single_risk(h_hi, e, v)
        assert np.mean(r_hi) >= np.mean(r_lo) - 1e-9

    def test_zero_exposure_zero_risk(self):
        """无暴露 → 无风险（常数暴露归一化为 0）。"""
        h = np.random.uniform(0, 10, (16, 16))
        e = np.zeros((16, 16))
        v = np.random.uniform(0, 1, (16, 16))
        r = mh.compute_single_risk(h, e, v)
        assert np.allclose(r, 0.0)

    def test_shape_mismatch_raises(self):
        with pytest.raises(mh.ValidationError):
            mh.compute_single_risk(np.zeros((4, 4)), np.zeros((4, 5)), np.zeros((4, 4)))


class TestCombine:
    def test_convex_combination_bounds(self):
        r1 = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        r2 = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        c = mh.combine_hazards([r1, r2], [0.3, 0.7])
        assert c.min() >= 0.0
        assert c.max() <= 1.0
        expected = 0.3 * r1 + 0.7 * r2
        np.testing.assert_allclose(c, expected, atol=1e-5)

    def test_equal_weights_is_mean(self):
        layers = [np.full((8, 8), v, dtype=np.float32) for v in (0.2, 0.4, 0.6)]
        c = mh.combine_hazards(layers)
        assert abs(float(c.mean()) - 0.4) < 1e-6

    def test_monotonic_in_each_layer(self):
        r1 = np.random.uniform(0, 0.5, (16, 16)).astype(np.float32)
        r2 = np.random.uniform(0, 0.5, (16, 16)).astype(np.float32)
        base = mh.combine_hazards([r1, r2])
        boosted = mh.combine_hazards([r1 + 0.3, r2])
        assert np.mean(boosted) >= np.mean(base) - 1e-9

    def test_empty_raises(self):
        with pytest.raises(mh.ValidationError):
            mh.combine_hazards([])

    def test_negative_weight_raises(self):
        r = [np.zeros((4, 4), dtype=np.float32)]
        with pytest.raises(mh.ValidationError):
            mh.combine_hazards(r, [-1.0])


class TestZones:
    def test_zone_range(self):
        risk = np.linspace(0, 1, 64 * 64).reshape(64, 64).astype(np.float32)
        z = mh.classify_zones(risk)
        assert z.min() >= 0
        assert z.max() <= 4  # len(breaks)=4 → zones 0..4
        assert z.dtype == np.int16

    def test_higher_risk_higher_zone(self):
        z = mh.classify_zones(np.array([[0.1, 0.9]], dtype=np.float32))
        assert z[0, 1] > z[0, 0]


class TestSynthetic:
    def test_shapes(self):
        layers, info = mh.generate_synthetic([116, 39, 117, 40], n_hazards=3)
        assert len(layers["hazards"]) == 3
        assert layers["exposure"].shape == (64, 64)
        assert layers["vulnerability"].shape == (64, 64)
        assert info["n_hazards"] == 3

    def test_end_to_end_positive_risk(self):
        layers, _ = mh.generate_synthetic([116, 39, 117, 40], n_hazards=2)
        risks = [mh.compute_single_risk(h, layers["exposure"], layers["vulnerability"])
                 for h in layers["hazards"]]
        combined = mh.combine_hazards(risks)
        assert combined.mean() > 0.0
        assert combined.max() <= 1.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        p = str(tmp_path / "t.tif")
        mh.write_geotiff(p, cube, bbox)
        back, bb = mh.read_geotiff(p)
        assert back.shape == cube.shape
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(mh.UsageError):
            mh.read_geotiff("/nonexistent/nope.tif")
