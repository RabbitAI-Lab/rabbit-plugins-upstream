"""Core algorithm tests for pest-disease-detection — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestSignals:
    def test_rededge_anomaly_positive_when_chlorophyll_drops(self):
        baseline = np.array([[0.6]], dtype=np.float32)
        current = np.array([[0.3]], dtype=np.float32)  # chlorophyll loss
        anom = mod.rededge_anomaly(current, baseline)
        assert anom[0, 0] == pytest.approx(0.3, abs=1e-4)

    def test_thermal_anomaly_positive_when_heating(self):
        baseline = np.array([[298.0]], dtype=np.float32)
        current = np.array([[310.0]], dtype=np.float32)  # stomatal closure
        anom = mod.thermal_anomaly(current, baseline)
        assert anom[0, 0] == pytest.approx(12.0, abs=1e-3)

    def test_temporal_decline_only_positive(self):
        now = np.array([[0.3, 0.7]], dtype=np.float32)
        prev = np.array([[0.6, 0.5]], dtype=np.float32)
        dec = mod.temporal_decline(now, prev)
        assert dec[0, 0] == pytest.approx(0.3, abs=1e-4)  # declined
        assert dec[0, 1] == pytest.approx(0.0, abs=1e-4)  # improved -> clipped to 0


class TestTexture:
    def test_uniform_low_variance(self):
        arr = np.full((16, 16), 0.5, dtype=np.float32)
        var = mod.texture_variance(arr, window=3)
        assert var.max() < 1e-6

    def test_heterogeneous_higher_variance(self):
        rng = np.random.default_rng(0)
        noisy = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        flat = np.full((32, 32), 0.5, dtype=np.float32)
        var_noisy = mod.texture_variance(noisy, window=3)
        var_flat = mod.texture_variance(flat, window=3)
        assert var_noisy.mean() > var_flat.mean()

    def test_variance_nonnegative(self):
        arr = np.random.default_rng(1).uniform(0, 1, (20, 20)).astype(np.float32)
        var = mod.texture_variance(arr, window=5)
        assert (var >= 0).all()


class TestProbability:
    def test_range_01(self):
        rng = np.random.default_rng(2)
        n = (16, 16)
        prob = mod.pest_probability(
            rng.uniform(0, 0.2, n).astype(np.float32),
            rng.uniform(0, 10, n).astype(np.float32),
            rng.uniform(0, 0.01, n).astype(np.float32),
            rng.uniform(0, 0.4, n).astype(np.float32),
        )
        assert prob.min() >= 0.0 and prob.max() <= 1.0

    def test_stressed_higher_than_healthy(self):
        zero = np.zeros((1, 1), dtype=np.float32)
        # healthy: no anomaly; stressed: large red-edge + thermal + decline anomalies
        healthy = mod.pest_probability(zero, zero, zero, zero)
        stressed = mod.pest_probability(
            np.array([[0.3]]), np.array([[15.0]]), np.array([[0.02]]), np.array([[0.4]]),
        )
        assert stressed[0, 0] > healthy[0, 0]
        assert stressed[0, 0] > 0.5

    def test_single_signal_monotonic(self):
        # more red-edge anomaly -> higher probability (others zero)
        zero = np.zeros((1, 1), dtype=np.float32)
        p1 = mod.pest_probability(np.array([[0.05]]), zero, zero, zero)
        p2 = mod.pest_probability(np.array([[0.3]]), zero, zero, zero)
        assert p2[0, 0] > p1[0, 0]


class TestRisk:
    def test_risk_levels(self):
        prob = np.array([[0.1, 0.3, 0.6, 0.8]], dtype=np.float32)
        risk = mod.classify_risk(prob)
        assert risk[0, 0] == 0
        assert risk[0, 1] == 1
        assert risk[0, 2] == 2
        assert risk[0, 3] == 3


class TestDetectPipeline:
    def test_patch_detected(self):
        cube_now, packed = mod.generate_synthetic([116, 39, 117, 40])
        aux = packed["aux"]
        res = mod.detect(cube_now, aux["cube_prev"], aux["ndre_baseline"], aux["lst_baseline"])
        prob = res["prob"]
        h, w = prob.shape
        center = prob[h // 2 - 3:h // 2 + 3, w // 2 - 3:w // 2 + 3].mean()
        corner = prob[:5, :5].mean()
        assert center > corner  # pest patch has higher probability
        assert prob.min() >= 0.0 and prob.max() <= 1.0

    def test_too_few_bands_raises(self):
        cube = np.random.uniform(0, 1, (2, 8, 8)).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.detect(cube, cube, np.zeros((8, 8)), np.zeros((8, 8)))
