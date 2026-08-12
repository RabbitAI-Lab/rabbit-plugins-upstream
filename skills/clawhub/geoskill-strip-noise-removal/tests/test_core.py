"""Core algorithm tests for strip-noise-removal."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _make_striped(seed=0, amp=0.2, h=64, w=64):
    rng = np.random.default_rng(seed)
    base = 0.3 + rng.normal(0, 0.02, (h, w))
    offsets = rng.normal(0, amp, w)
    return (base + offsets[np.newaxis, :]).astype(np.float32)


class TestStripeIndex:
    def test_striped_higher_than_clean(self):
        rng = np.random.default_rng(1)
        clean = rng.normal(0.3, 0.02, (64, 64)).astype(np.float32)
        striped = _make_striped(seed=1, amp=0.3)
        assert mod.compute_stripe_index(striped, "vertical") > \
               mod.compute_stripe_index(clean, "vertical")

    def test_constant_zero(self):
        band = np.full((16, 16), 0.5, dtype=np.float32)
        assert mod.compute_stripe_index(band, "vertical") == 0.0


class TestMomentMatching:
    def test_reduces_stripe_index(self):
        striped = _make_striped(seed=2, amp=0.25)
        before = mod.compute_stripe_index(striped, "vertical")
        corrected = mod.moment_matching(striped, "vertical")
        after = mod.compute_stripe_index(corrected, "vertical")
        assert after < before
        assert after < 0.05  # moment matching nearly eliminates column-mean stripes

    def test_preserves_shape(self):
        striped = _make_striped(seed=3)
        corrected = mod.moment_matching(striped, "vertical")
        assert corrected.shape == striped.shape

    def test_horizontal_direction(self):
        rng = np.random.default_rng(4)
        base = 0.3 + rng.normal(0, 0.02, (64, 64))
        offsets = rng.normal(0, 0.25, 64)
        striped = (base + offsets[:, np.newaxis]).astype(np.float32)
        corrected = mod.moment_matching(striped, "horizontal")
        assert mod.compute_stripe_index(corrected, "horizontal") < \
               mod.compute_stripe_index(striped, "horizontal")

    def test_bad_direction_raises(self):
        with pytest.raises(mod.UsageError):
            mod.moment_matching(np.ones((8, 8), dtype=np.float32), "diagonal")


class TestWeightedRegression:
    def test_reduces_stripe_index(self):
        striped = _make_striped(seed=5, amp=0.2)
        before = mod.compute_stripe_index(striped, "vertical")
        corrected = mod.weighted_regression(striped, "vertical")
        after = mod.compute_stripe_index(corrected, "vertical")
        assert after < before

    def test_preserves_shape(self):
        striped = _make_striped(seed=6)
        corrected = mod.weighted_regression(striped, "vertical")
        assert corrected.shape == striped.shape


class TestDestripe:
    def test_multiband(self):
        cube, _, _ = mod.generate_synthetic([116, 39, 117, 40], n_bands=3)
        corrected, params = mod.destripe(cube, "vertical", "moment")
        assert corrected.shape == cube.shape
        assert params["n_bands"] == 3

    def test_2d_input_promoted(self):
        band = _make_striped(seed=7)
        corrected, params = mod.destripe(band, "vertical", "moment")
        assert corrected.ndim == 3
        assert corrected.shape[0] == 1

    def test_bad_method_raises(self):
        cube = np.ones((2, 8, 8), dtype=np.float32)
        with pytest.raises(mod.UsageError):
            mod.destripe(cube, "vertical", "badmethod")

    def test_regression_method(self):
        cube, _, _ = mod.generate_synthetic([116, 39, 117, 40], n_bands=2,
                                            stripe_amplitude=0.2)
        corrected, params = mod.destripe(cube, "vertical", "regression")
        assert params["method"] == "regression"
        assert corrected.shape == cube.shape


class TestGenerateSynthetic:
    def test_shape_and_bands(self):
        cube, mask, info = mod.generate_synthetic([116, 39, 117, 40],
                                                  width=48, height=32, n_bands=5)
        assert cube.shape == (5, 32, 48)
        assert mask is None
        assert info["n_bands"] == 5

    def test_gap_mask(self):
        cube, mask, info = mod.generate_synthetic([116, 39, 117, 40], gap_fraction=0.2)
        assert mask is not None
        assert mask.shape == cube.shape
        assert 0.0 < mask.mean() < 1.0

    def test_deterministic(self):
        c1, _, _ = mod.generate_synthetic([116, 39, 117, 40], seed=42)
        c2, _, _ = mod.generate_synthetic([116, 39, 117, 40], seed=42)
        np.testing.assert_array_equal(c1, c2)

    def test_multiplicative_stripes(self):
        cube, _, _ = mod.generate_synthetic([116, 39, 117, 40],
                                            stripe_type="multiplicative",
                                            stripe_amplitude=0.3)
        assert cube.shape[0] == 4

    def test_dead_lines(self):
        cube, _, _ = mod.generate_synthetic([116, 39, 117, 40], n_dead_lines=5)
        # at least some columns should be all-zero in some band
        assert (cube == 0.0).any()
