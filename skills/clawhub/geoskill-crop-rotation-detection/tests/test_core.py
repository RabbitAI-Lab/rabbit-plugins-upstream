"""Core algorithm tests for crop-rotation-detection — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestMinimalPeriod:
    def test_monoculture_period_1(self):
        assert mod.minimal_period(np.array([1, 1, 1, 1])) == 1

    def test_two_year_rotation(self):
        assert mod.minimal_period(np.array([1, 2, 1, 2])) == 2

    def test_three_year_rotation(self):
        assert mod.minimal_period(np.array([1, 2, 3, 1, 2, 3])) == 3

    def test_irregular_full_length(self):
        assert mod.minimal_period(np.array([1, 2, 1, 3])) == 4

    def test_partial_last_cycle(self):
        # [1,2,1,2,1] is 2-periodic with a partial final cycle
        assert mod.minimal_period(np.array([1, 2, 1, 2, 1])) == 2


class TestRecognizePattern:
    def test_monoculture(self):
        assert mod.recognize_pattern(np.array([1, 1, 1, 1])) == "monoculture"

    def test_two_year(self):
        assert mod.recognize_pattern(np.array([1, 2, 1, 2])) == "rotation-2yr"

    def test_three_year(self):
        assert mod.recognize_pattern(np.array([1, 2, 3, 1, 2, 3])) == "rotation-3yr"

    def test_noncrop(self):
        assert mod.recognize_pattern(np.array([0, 0, 0, 0])) == "non-crop"

    def test_irregular(self):
        assert mod.recognize_pattern(np.array([1, 2, 1, 3])) == "irregular"


class TestEncodeSequences:
    def test_distinct_sequences_unique_ids(self):
        # build (years=4, H=1, W=3) with three different per-pixel sequences
        s = np.zeros((4, 1, 3), dtype=np.int32)
        s[:, 0, 0] = [1, 1, 1, 1]  # monoculture
        s[:, 0, 1] = [1, 2, 1, 2]  # 2-yr rotation
        s[:, 0, 2] = [1, 2, 3, 1]  # 3-yr rotation (partial final cycle)
        seq_ids, unique = mod.encode_sequences(s)
        assert seq_ids.shape == (1, 3)
        # all three sequences distinct
        assert len(np.unique(seq_ids)) == 3
        assert unique.shape[0] == 3

    def test_too_few_years_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.encode_sequences(np.zeros((1, 4, 4), dtype=np.int32))


class TestRotationFrequency:
    def test_frequencies_sum_to_total(self):
        s = np.zeros((4, 2, 2), dtype=np.int32)
        s[:, 0, 0] = [1, 1, 1, 1]
        s[:, 0, 1] = [1, 1, 1, 1]
        s[:, 1, 0] = [1, 2, 1, 2]
        s[:, 1, 1] = [2, 2, 2, 2]
        res = mod.rotation_frequency(s)
        total = sum(v["count"] for v in res["frequency"].values())
        assert total == 4  # 2x2 grid
        assert res["frequency"]["monoculture"]["count"] == 3  # two corn + one soybean monoculture
        assert res["frequency"]["rotation-2yr"]["count"] == 1
        frac_sum = sum(v["fraction"] for v in res["frequency"].values())
        assert frac_sum == pytest.approx(1.0, abs=1e-6)


class TestPipeline:
    def test_synthetic_recovers_expected_patterns(self):
        stack, info = mod.generate_synthetic([116, 39, 117, 40], n_years=6)
        res = mod.detect_rotation(stack)
        pats = set(res["frequency"].keys())
        # the three injected patterns must dominate
        for expected in ["monoculture", "rotation-2yr", "rotation-3yr"]:
            assert expected in pats
        # together these three should cover the vast majority of pixels
        dom = sum(res["frequency"][p]["fraction"]
                  for p in ["monoculture", "rotation-2yr", "rotation-3yr"]
                  if p in res["frequency"])
        assert dom > 0.95

    def test_monoculture_dominates_left_half(self):
        stack, _ = mod.generate_synthetic([116, 39, 117, 40], n_years=6)
        res = mod.detect_rotation(stack)
        pmap = res["pattern_map"]
        h, w = pmap.shape
        left = pmap[:, :w // 2]
        assert np.mean(left == "monoculture") > 0.9

    def test_wrong_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.detect_rotation(np.zeros((8, 8), dtype=np.int32))
