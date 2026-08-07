"""Core algorithm tests for forest-cover-change."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as fc


class TestForestMask:
    def test_threshold(self):
        ndvi = np.array([[0.1, 0.3], [0.5, 0.8]], dtype=np.float32)
        m = fc.forest_mask(ndvi, threshold=0.3)
        assert m.tolist() == [[False, True], [True, True]]

    def test_all_below(self):
        m = fc.forest_mask(np.full((4, 4), 0.1, np.float32), 0.3)
        assert not m.any()


class TestCVA:
    def test_flat_series_zero(self):
        stack = np.full((4, 8, 8), 0.5, dtype=np.float32)
        mag = fc.change_vector_magnitude(stack)
        assert mag.max() < 1e-6

    def test_single_step(self):
        stack = np.zeros((2, 3, 3), dtype=np.float32)
        stack[1] = 0.6  # diff 0.6 everywhere
        mag = fc.change_vector_magnitude(stack)
        np.testing.assert_allclose(mag, 0.6, atol=1e-5)

    def test_two_steps_norm(self):
        stack = np.zeros((3, 2, 2), dtype=np.float32)
        stack[1] = 0.3
        stack[2] = 0.7  # diffs: 0.3, 0.4 -> norm 0.5
        mag = fc.change_vector_magnitude(stack)
        np.testing.assert_allclose(mag, 0.5, atol=1e-5)

    def test_bad_ndim_raises(self):
        with pytest.raises(fc.ValidationError):
            fc.change_vector_magnitude(np.zeros((4, 4), np.float32))

    def test_single_date_raises(self):
        with pytest.raises(fc.ValidationError):
            fc.change_vector_magnitude(np.zeros((1, 4, 4), np.float32))


class TestClassifyChange:
    def test_loss_gain_stable(self):
        # 3 pixels over 2 dates: loss, gain, stable
        stack = np.zeros((2, 1, 3), dtype=np.float32)
        stack[0] = [[0.7, 0.1, 0.7]]   # first
        stack[1] = [[0.1, 0.6, 0.7]]   # last
        cls, masks = fc.classify_forest_change(stack, threshold=0.3)
        assert cls[0, 0] == 1  # loss
        assert cls[0, 1] == 2  # gain
        assert cls[0, 2] == 0  # stable
        assert int(masks["loss"].sum()) == 1
        assert int(masks["gain"].sum()) == 1

    def test_small_drop_not_loss(self):
        stack = np.zeros((2, 1, 1), dtype=np.float32)
        stack[0] = [[0.7]]
        stack[1] = [[0.65]]  # drop 0.05 < default 0.1, still forest
        cls, _ = fc.classify_forest_change(stack, threshold=0.3)
        assert cls[0, 0] == 0

    def test_bad_ndim_raises(self):
        with pytest.raises(fc.ValidationError):
            fc.classify_forest_change(np.zeros((4, 4), np.float32))


class TestSynthetic:
    def test_shape(self):
        stack, info = fc.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=4, width=64, height=48, seed=1)
        assert stack.shape == (4, 48, 64)
        assert stack.min() >= 0.0 and stack.max() <= 1.0
        assert info["loss_pixel_count"] > 0
        assert info["gain_pixel_count"] > 0

    def test_detection_matches_injection(self):
        stack, info = fc.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=4, width=80, height=80, seed=2)
        cls, masks = fc.classify_forest_change(stack, threshold=0.3)
        # detected loss/gain exactly match injected masks
        np.testing.assert_array_equal(masks["loss"], info["loss_mask"])
        np.testing.assert_array_equal(masks["gain"], info["gain_mask"])
        assert cls.max() == 2

    def test_cva_higher_in_loss(self):
        stack, info = fc.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=4, width=80, height=80, seed=3)
        mag = fc.change_vector_magnitude(stack)
        mean_loss = mag[info["loss_mask"]].mean()
        stable = fc.forest_mask(stack[0], 0.3) & fc.forest_mask(stack[-1], 0.3)
        mean_stable = mag[stable].mean()
        assert mean_loss > mean_stable * 2


class TestStats:
    def test_series_and_areas(self):
        stack, info = fc.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=4, width=48, height=48, seed=4)
        cls, _ = fc.classify_forest_change(stack, threshold=0.3)
        stats = fc.forest_change_stats(cls, stack, [116, 39, 117, 40],
                                       threshold=0.3)
        assert len(stats["change_classes"]) == 3
        total_frac = sum(c["fraction"] for c in stats["change_classes"])
        assert total_frac == pytest.approx(1.0)
        assert len(stats["forest_area_series"]) == 4
        # net forest change negative (loss injected) -> last < first
        assert stats["net_forest_change_pixels"] < 0
        assert stats["total_area_km2"] > 0


class TestGeoTiffIO:
    def test_float_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (3, 12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "n.tif")
        fc.write_geotiff(path, arr, bbox, dtype="float32")
        back, rbbox = fc.read_ndvi_stack(path)
        assert back.shape == (3, 12, 12)
        np.testing.assert_allclose(back, arr, atol=1e-6)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(fc.UsageError):
            fc.read_ndvi_stack("/nonexistent/none.tif")
