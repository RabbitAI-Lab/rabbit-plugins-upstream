"""Core algorithm tests for invasive-species-spread (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestClassifyPresence:
    def test_above_threshold_present(self):
        t0 = np.full((4, 4), 0.3, dtype=np.float32)
        t1 = np.full((4, 4), 0.3, dtype=np.float32)
        p0, new = M.classify_presence(t0, t1, threshold=0.15)
        assert np.all(p0 == 1)
        assert np.all(new == 0)  # 无新增（t1 不超 t0 范围）

    def test_new_invasion_detected(self):
        t0 = np.full((4, 4), 0.05, dtype=np.float32)  # 无入侵
        t1 = np.full((4, 4), 0.30, dtype=np.float32)  # 入侵出现
        p0, new = M.classify_presence(t0, t1, threshold=0.15)
        assert np.all(p0 == 0)
        assert np.all(new == 1)

    def test_persistent_not_new(self):
        t0 = np.full((4, 4), 0.30, dtype=np.float32)
        t1 = np.full((4, 4), 0.30, dtype=np.float32)
        _, new = M.classify_presence(t0, t1, threshold=0.15)
        assert np.all(new == 0)


class TestSpreadRate:
    def test_exact_formula(self):
        # r = (A1-A0)/(A0*dt) = (200-100)/(100*5) = 0.2
        r = M.spread_rate(100.0, 200.0, 5.0)
        np.testing.assert_allclose(r, 0.2, rtol=1e-6)

    def test_decline_negative_rate(self):
        r = M.spread_rate(200.0, 100.0, 5.0)
        assert r < 0.0

    def test_zero_initial_with_growth(self):
        r = M.spread_rate(0.0, 50.0, 5.0)
        assert r == float("inf")

    def test_zero_initial_no_growth(self):
        r = M.spread_rate(0.0, 0.0, 5.0)
        assert r == 0.0


class TestDistanceToSource:
    def test_source_pixel_zero_distance(self):
        presence = np.zeros((8, 8), dtype=np.uint8)
        presence[4, 4] = 1
        dist = M.distance_to_source(presence)
        assert dist[4, 4] == 0.0

    def test_distance_increases_away(self):
        presence = np.zeros((16, 16), dtype=np.uint8)
        presence[8, 8] = 1
        dist = M.distance_to_source(presence, cell_size=1.0)
        assert dist[8, 9] < dist[8, 12]

    def test_no_source_inf(self):
        presence = np.zeros((4, 4), dtype=np.uint8)
        dist = M.distance_to_source(presence)
        assert np.all(np.isinf(dist))


class TestRiskPrediction:
    def test_bounded_0_1(self):
        rng = np.random.default_rng(0)
        suit = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        dist = rng.uniform(0, 10000, (32, 32)).astype(np.float32)
        risk = M.risk_prediction(suit, dist)
        assert risk.min() >= 0.0
        assert risk.max() <= 1.0 + 1e-6

    def test_near_source_higher_risk(self):
        """靠近已知入侵点 → 风险更高（距离衰减）。"""
        suit = np.full((4, 4), 0.8, dtype=np.float32)
        r_near = M.risk_prediction(suit, np.full((4, 4), 100.0), dispersal_scale=5000)
        r_far = M.risk_prediction(suit, np.full((4, 4), 50000.0), dispersal_scale=5000)
        assert float(r_near.mean()) > float(r_far.mean())

    def test_suitability_drives_risk(self):
        """适宜性越高 → 风险越高（距离相同）。"""
        dist = np.full((4, 4), 1000.0, dtype=np.float32)
        r_hi = M.risk_prediction(np.full((4, 4), 0.9), dist)
        r_lo = M.risk_prediction(np.full((4, 4), 0.2), dist)
        assert float(r_hi.mean()) > float(r_lo.mean())

    def test_zero_suitability_zero_risk(self):
        risk = M.risk_prediction(np.zeros((4, 4)), np.full((4, 4), 100.0))
        assert np.all(risk == 0.0)
