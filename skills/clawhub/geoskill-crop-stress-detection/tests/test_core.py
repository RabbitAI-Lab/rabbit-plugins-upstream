"""Core algorithm tests for crop-stress-detection — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestCWSI:
    def test_zero_at_wet_reference(self):
        tc = np.array([[295.0]], dtype=np.float32)
        cwsi = mod.compute_cwsi(tc, t_wet=295.0, t_dry=315.0)
        assert cwsi[0, 0] == pytest.approx(0.0, abs=1e-6)

    def test_one_at_dry_reference(self):
        tc = np.array([[315.0]], dtype=np.float32)
        cwsi = mod.compute_cwsi(tc, t_wet=295.0, t_dry=315.0)
        assert cwsi[0, 0] == pytest.approx(1.0, abs=1e-6)

    def test_exact_formula(self):
        tc = np.array([[305.0]], dtype=np.float32)  # midpoint
        cwsi = mod.compute_cwsi(tc, t_wet=295.0, t_dry=315.0)
        assert cwsi[0, 0] == pytest.approx(0.5, abs=1e-4)

    def test_monotonic_with_temperature(self):
        tc = np.array([[297.0, 305.0, 313.0]], dtype=np.float32)
        cwsi = mod.compute_cwsi(tc, 295.0, 315.0)
        assert cwsi[0, 0] < cwsi[0, 1] < cwsi[0, 2]

    def test_clipped_to_01(self):
        tc = np.array([[280.0, 330.0]], dtype=np.float32)  # out of range
        cwsi = mod.compute_cwsi(tc, 295.0, 315.0)
        assert cwsi[0, 0] == 0.0
        assert cwsi[0, 1] == 1.0

    def test_invalid_reference_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.compute_cwsi(np.array([[300.0]]), t_wet=315.0, t_dry=295.0)


class TestChlorophyll:
    def test_cire_formula(self):
        # CIre = NIR/RedEdge - 1; NIR=0.5, RedEdge=0.1 -> 4.0
        cire = mod.chlorophyll_rededge_index(np.array([[0.1]]), np.array([[0.5]]))
        assert cire[0, 0] == pytest.approx(4.0, abs=1e-4)

    def test_chlorophyll_stress_inverted(self):
        # high chlorophyll -> low stress
        low_s = mod.chlorophyll_stress(np.array([[4.0]]))
        high_s = mod.chlorophyll_stress(np.array([[0.5]]))
        assert low_s[0, 0] < high_s[0, 0]

    def test_stress_range(self):
        cire = np.linspace(0, 5, 20).astype(np.float32).reshape(1, -1)
        s = mod.chlorophyll_stress(cire)
        assert s.min() >= 0.0 and s.max() <= 1.0


class TestSarWater:
    def test_water_content_monotonic_with_backscatter(self):
        sigma = np.array([[1e-4, 1e-3, 1e-2, 1e-1]], dtype=np.float32)
        wc = mod.sar_water_content(sigma)
        assert wc[0, 0] < wc[0, 1] < wc[0, 2] < wc[0, 3]

    def test_water_deficit_complement(self):
        wc = np.array([[0.8]], dtype=np.float32)
        deficit = mod.water_deficit_stress(wc)
        assert deficit[0, 0] == pytest.approx(0.2, abs=1e-6)


class TestFusion:
    def test_range_01(self):
        rng = np.random.default_rng(0)
        n = (16, 16)
        fused = mod.fuse_stress(rng.uniform(0, 1, n), rng.uniform(0, 1, n), rng.uniform(0, 1, n))
        assert fused.min() >= 0.0 and fused.max() <= 1.0

    def test_weighted_average(self):
        a = np.array([[1.0]], dtype=np.float32)
        b = np.array([[0.0]], dtype=np.float32)
        c = np.array([[0.0]], dtype=np.float32)
        # weights 0.4/0.3/0.3 -> 0.4*1 = 0.4
        fused = mod.fuse_stress(a, b, c)
        assert fused[0, 0] == pytest.approx(0.4, abs=1e-5)

    def test_all_stressed_high(self):
        one = np.array([[1.0]], dtype=np.float32)
        fused = mod.fuse_stress(one, one, one)
        assert fused[0, 0] == pytest.approx(1.0, abs=1e-6)


class TestDetectPipeline:
    def test_stressed_side_higher(self):
        cube, info = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.detect_stress(cube[0], cube[1], cube[2], cube[3],
                                info["t_wet"], info["t_dry"])
        stress = res["stress"]
        h, w = stress.shape
        left = stress[:, :int(w * 0.2)].mean()    # no stress
        right = stress[:, int(w * 0.8):].mean()    # severe stress
        assert right > left
        assert stress.min() >= 0.0 and stress.max() <= 1.0

    def test_cwsi_component_bounded(self):
        cube, info = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.detect_stress(cube[0], cube[1], cube[2], cube[3],
                                info["t_wet"], info["t_dry"])
        assert res["cwsi"].min() >= 0.0 and res["cwsi"].max() <= 1.0
        assert res["grade"].max() <= 3
