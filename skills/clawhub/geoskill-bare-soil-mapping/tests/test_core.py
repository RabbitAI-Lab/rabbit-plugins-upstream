"""Core algorithm tests for bare-soil-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as bs


class TestBSI:
    def test_bare_soil_high(self):
        blue = np.full((4, 4), 0.10, dtype=np.float32)
        green = np.full((4, 4), 0.14, dtype=np.float32)
        red = np.full((4, 4), 0.30, dtype=np.float32)
        nir = np.full((4, 4), 0.18, dtype=np.float32)
        swir = np.full((4, 4), 0.40, dtype=np.float32)
        bsi = bs.bsi_index(blue, green, red, nir, swir)
        # ((0.40+0.30)-(0.18+0.10))/((0.40+0.30)+(0.18+0.10))
        assert np.allclose(bsi, (0.70 - 0.28) / 0.98, atol=1e-5)
        assert bsi.mean() > 0.4

    def test_vegetation_negative(self):
        blue = np.full((4, 4), 0.03, dtype=np.float32)
        green = np.full((4, 4), 0.09, dtype=np.float32)
        red = np.full((4, 4), 0.04, dtype=np.float32)
        nir = np.full((4, 4), 0.45, dtype=np.float32)
        swir = np.full((4, 4), 0.18, dtype=np.float32)
        assert bs.bsi_index(blue, green, red, nir, swir).mean() < 0

    def test_zero_denominator_safe(self):
        z = np.zeros((3, 3), dtype=np.float32)
        assert np.all(bs.bsi_index(z, z, z, z, z) == 0)


class TestFeatures:
    def test_brightness(self):
        cube = np.ones((5, 4, 4), dtype=np.float32) * 0.2
        assert np.allclose(bs.brightness(cube), 0.2)

    def test_local_std_smooth_vs_rough(self):
        smooth = np.full((32, 32), 0.3, dtype=np.float32)
        rng = np.random.default_rng(0)
        rough = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        assert bs.local_std(smooth).mean() < 0.01
        assert bs.local_std(rough).mean() > 0.1


class TestOtsu:
    def test_bimodal(self):
        rng = np.random.default_rng(1)
        low = rng.uniform(0.0, 0.1, 500)
        high = rng.uniform(0.7, 0.9, 500)
        vals = np.concatenate([low, high]).astype(np.float32)
        t = bs.otsu_threshold(vals)
        assert 0.2 < t < 0.6

    def test_empty(self):
        t = bs.otsu_threshold(np.array([], dtype=np.float32))
        assert t == bs.DEFAULT_SCORE_THRESHOLD


class TestResolveThreshold:
    def test_auto(self):
        score = np.array([[0.1, 0.8]], dtype=np.float32)
        t = bs.resolve_threshold("auto", score)
        assert 0.0 <= t <= 1.0

    def test_explicit_float(self):
        score = np.zeros((2, 2), dtype=np.float32)
        assert bs.resolve_threshold("0.6", score) == pytest.approx(0.6)

    def test_invalid_string_raises(self):
        score = np.zeros((2, 2), dtype=np.float32)
        with pytest.raises(bs.UsageError):
            bs.resolve_threshold("banana", score)

    def test_out_of_range_raises(self):
        score = np.zeros((2, 2), dtype=np.float32)
        with pytest.raises(bs.UsageError):
            bs.resolve_threshold("1.5", score)


class TestExtract:
    def test_synthetic_recovery(self):
        cube, truth, info = bs.generate_synthetic_scene([116, 39, 117, 40], seed=3)
        mask, score, thr, comp = bs.extract_bare_soil(cube, threshold_arg="auto")
        pred = mask.astype(bool)
        gt = truth.astype(bool)
        iou = np.logical_and(pred, gt).sum() / np.logical_or(pred, gt).sum()
        assert iou > 0.6, f"IoU too low: {iou}"

    def test_vegetation_water_excluded(self):
        cube, truth, info = bs.generate_synthetic_scene([116, 39, 117, 40])
        mask, score, thr, comp = bs.extract_bare_soil(cube, threshold_arg="0.4")
        # water is bottom-left, vegetation is top; neither should be bare soil
        yy, xx = np.mgrid[0:cube.shape[1], 0:cube.shape[2]]
        yyn = yy / (cube.shape[1] - 1)
        veg = yyn < 0.40
        assert np.logical_and(mask, veg).sum() == 0

    def test_too_few_bands_raises(self):
        cube = np.random.uniform(0, 1, (3, 8, 8)).astype(np.float32)
        with pytest.raises(bs.ValidationError):
            bs.bare_soil_score(cube)


class TestSynthetic:
    def test_shape_truth(self):
        cube, truth, info = bs.generate_synthetic_scene([116, 39, 117, 40])
        assert cube.shape == (5, 128, 128)
        assert truth.sum() > 0
        assert info["truth_bare_soil_px"] == int(truth.sum())


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (5, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        bs.write_geotiff(path, cube, bbox)
        back, rb = bs.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(bs.UsageError):
            bs.read_geotiff("/nonexistent/x.tif")
