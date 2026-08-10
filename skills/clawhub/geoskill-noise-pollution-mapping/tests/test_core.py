"""Core algorithm tests for noise-pollution-mapping (physical correctness)."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestSourceLevel:
    def test_zero_flow_zero_level(self):
        assert M.source_level(0.0) == 0.0

    def test_higher_flow_higher_level(self):
        assert M.source_level(2000.0) > M.source_level(500.0)

    def test_higher_speed_higher_level(self):
        assert M.source_level(1000.0, speed=80.0) > M.source_level(1000.0, speed=40.0)

    def test_reference_value_reasonable(self):
        # flow=1000, speed=50 → 10*log10(1000) + 0 + 30 = 30 + 30 = 60
        lvl = M.source_level(1000.0, speed=50.0)
        np.testing.assert_allclose(lvl, 60.0, atol=0.1)


class TestGeometricAttenuation:
    def test_at_ref_dist_zero(self):
        d = np.full((4, 4), 15.0, dtype=np.float32)
        att = M.geometric_attenuation(d, ref_dist=15.0)
        np.testing.assert_allclose(att, 0.0, atol=1e-5)

    def test_point_source_double_dist_minus_6dB(self):
        """点源：距离加倍 → -6 dB。"""
        d1 = np.full((1,), 15.0, dtype=np.float32)
        d2 = np.full((1,), 30.0, dtype=np.float32)
        a1 = M.geometric_attenuation(d1, source_type="point")
        a2 = M.geometric_attenuation(d2, source_type="point")
        np.testing.assert_allclose(a2 - a1, -6.02, atol=0.1)

    def test_line_source_double_dist_minus_3dB(self):
        """线源：距离加倍 → -3 dB。"""
        d1 = np.full((1,), 15.0, dtype=np.float32)
        d2 = np.full((1,), 30.0, dtype=np.float32)
        a1 = M.geometric_attenuation(d1, source_type="line")
        a2 = M.geometric_attenuation(d2, source_type="line")
        np.testing.assert_allclose(a2 - a1, -3.01, atol=0.1)


class TestBarrierAttenuation:
    def test_zero_barriers_zero(self):
        bar = M.barrier_attenuation(np.zeros((4, 4)))
        assert np.all(bar == 0.0)

    def test_scales_with_count(self):
        bar = M.barrier_attenuation(np.full((4, 4), 2.0), per_barrier_db=5.0)
        np.testing.assert_allclose(bar, 10.0, rtol=1e-5)

    def test_clipped_at_max(self):
        bar = M.barrier_attenuation(np.full((4, 4), 10.0), per_barrier_db=5.0, max_db=20.0)
        assert np.all(bar <= 20.0)


class TestNoiseLevel:
    def test_decreases_with_distance(self):
        """噪声级随距离递减。"""
        d_near = np.full((1, 1), 30.0, dtype=np.float32)
        d_far = np.full((1, 1), 300.0, dtype=np.float32)
        bar = np.zeros((1, 1), dtype=np.float32)
        l_near = M.noise_level(70.0, d_near, bar)
        l_far = M.noise_level(70.0, d_far, bar)
        assert float(l_near[0, 0]) > float(l_far[0, 0])

    def test_barrier_reduces_level(self):
        d = np.full((1, 1), 100.0, dtype=np.float32)
        l_no = M.noise_level(70.0, d, np.zeros((1, 1)))
        l_bar = M.noise_level(70.0, d, np.full((1, 1), 2.0))
        assert float(l_bar[0, 0]) < float(l_no[0, 0])

    def test_clipped_0_120(self):
        d = np.full((4, 4), 0.0, dtype=np.float32)
        level = M.noise_level(200.0, d, np.zeros((4, 4)))
        assert level.max() <= 120.0
        assert level.min() >= 0.0

    def test_higher_source_higher_level(self):
        d = np.full((4, 4), 100.0, dtype=np.float32)
        bar = np.zeros((4, 4), dtype=np.float32)
        l1 = M.noise_level(60.0, d, bar)
        l2 = M.noise_level(80.0, d, bar)
        assert float(l2.mean()) > float(l1.mean())
