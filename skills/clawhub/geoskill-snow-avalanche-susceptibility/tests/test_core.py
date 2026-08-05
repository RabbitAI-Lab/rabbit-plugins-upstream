"""Core algorithm tests for snow-avalanche-susceptibility."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as av


class TestSlopeFactor:
    def test_peaks_near_38(self):
        """坡度因子在 ~38° 达峰，过缓/过陡都更低。"""
        vals = av.slope_factor(np.array([10.0, 38.0, 70.0]))
        assert vals[1] > vals[0]
        assert vals[1] > vals[2]
        assert abs(float(av.slope_factor(np.array([38.0]))[0]) - 1.0) < 1e-6

    def test_sweet_spot_range_high(self):
        s30_45 = av.slope_factor(np.array([30.0, 45.0])).mean()
        flat = float(av.slope_factor(np.array([5.0]))[0])
        assert s30_45 > flat


class TestAspectFactor:
    def test_north_higher_than_south(self):
        north = float(av.aspect_factor(np.array([0.0]))[0])
        south = float(av.aspect_factor(np.array([180.0]))[0])
        east = float(av.aspect_factor(np.array([90.0]))[0])
        assert abs(north - 1.0) < 1e-6
        assert abs(south - 0.0) < 1e-6
        assert north > east > south


class TestSnowFactor:
    def test_increases_saturating(self):
        s = av.snow_factor(np.array([0.0, 1.0, 3.0, 20.0]))
        assert s[0] == 0.0
        assert s[1] > s[0]
        assert s[2] > s[1]
        assert s[3] < 1.0 + 1e-6 and s[3] > 0.9


class TestTemperatureFactor:
    def test_peaks_near_zero(self):
        t = av.temperature_factor(np.array([-20.0, 0.0, 15.0]))
        assert t[1] > t[0]
        assert t[1] > t[2]


class TestRoughnessFactor:
    def test_smoother_more_prone(self):
        r = av.roughness_factor(np.array([0.0, 0.5, 1.0]))
        assert r[0] == 1.0
        assert r[2] == 0.0
        assert r[0] > r[1] > r[2]


class TestSusceptibilityFromFactors:
    def test_bounded_random(self):
        rng = np.random.default_rng(0)
        args = [rng.uniform(0, 1, (16, 16)) for _ in range(5)]
        s = av.susceptibility_from_factors(*args)
        assert s.min() >= 0.0 and s.max() <= 1.0

    def test_monotonic_in_snow(self):
        base = [np.full((8, 8), v) for v in (0.8, 0.6, 0.4, 0.3, 0.7)]
        s_lo = av.susceptibility_from_factors(*base)
        higher_snow = list(base); higher_snow[3] = np.full((8, 8), 0.9)
        s_hi = av.susceptibility_from_factors(*higher_snow)
        assert s_hi.mean() > s_lo.mean()

    def test_bad_weights_raise(self):
        z = [np.zeros((4, 4)) for _ in range(5)]
        with pytest.raises(av.ValidationError):
            av.susceptibility_from_factors(*z, weights=(0, 0, 0, 0, 0))


class TestAvalancheSusceptibility:
    def test_bounded_with_synthetic(self):
        layers, _ = av.generate_synthetic([90, 30, 91, 31])
        s = av.avalanche_susceptibility(layers["slope"], layers["aspect"], layers["roughness"],
                                        layers["snow_depth"], layers["temperature"])
        assert s.min() >= 0.0 and s.max() <= 1.0
        assert 0.0 < s.mean() < 1.0

    def test_shape_mismatch_raises(self):
        z = np.zeros((4, 4))
        with pytest.raises(av.ValidationError):
            av.avalanche_susceptibility(z, z, z, z, np.zeros((4, 5)))


class TestClassify:
    def test_levels_range(self):
        s = np.linspace(0, 1, 64 * 64).reshape(64, 64)
        lvl = av.classify_susceptibility(s)
        assert lvl.min() >= 0 and lvl.max() <= 3
        assert np.all(np.diff(lvl.ravel()) >= 0)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (4, 16, 16)).astype(np.float32)
        bbox = [90.0, 30.0, 91.0, 31.0]
        p = str(tmp_path / "a.tif")
        av.write_geotiff(p, cube, bbox)
        back, bb = av.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(av.UsageError):
            av.read_geotiff("/nonexistent/a.tif")
