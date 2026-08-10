"""Core algorithm tests for mangrove-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as mm


class TestIndices:
    def test_ndvi_vegetation_high(self):
        nir = np.full((8, 8), 0.45, dtype=np.float32)
        red = np.full((8, 8), 0.04, dtype=np.float32)
        ndvi = mm.ndvi_index(nir, red)
        assert np.allclose(ndvi, (0.45 - 0.04) / (0.45 + 0.04), atol=1e-5)
        assert ndvi.mean() > 0.5

    def test_ndvi_water_negative(self):
        nir = np.full((4, 4), 0.015, dtype=np.float32)
        red = np.full((4, 4), 0.03, dtype=np.float32)
        assert mm.ndvi_index(nir, red).mean() < 0

    def test_ndvi_zero_denominator_safe(self):
        z = np.zeros((4, 4), dtype=np.float32)
        assert np.all(mm.ndvi_index(z, z) == 0)

    def test_ndwi_water_positive(self):
        green = np.full((4, 4), 0.06, dtype=np.float32)
        nir = np.full((4, 4), 0.015, dtype=np.float32)
        assert mm.ndwi_index(green, nir).mean() > 0

    def test_ndwi_vegetation_negative(self):
        green = np.full((4, 4), 0.10, dtype=np.float32)
        nir = np.full((4, 4), 0.40, dtype=np.float32)
        assert mm.ndwi_index(green, nir).mean() < 0


class TestCoastDistance:
    def test_water_zero_inland_increases(self):
        water = np.zeros((16, 32), dtype=bool)
        water[:, :8] = True  # left half water
        dist = mm.coast_distance_px(water)
        assert np.all(dist[:, :8] == 0)
        # inland distance increases moving right
        assert dist[8, 10] < dist[8, 20]
        assert dist[8, 20] > 0


class TestMangroveScore:
    def test_mangrove_high_upland_low(self):
        # mangrove-like: high ndvi, near coast, bright sar
        ndvi = np.array([[0.75]], dtype=np.float32)
        coast = np.array([[3.0]], dtype=np.float32)
        sar = np.array([[0.35]], dtype=np.float32)
        mask, score, comp = mm.mangrove_score(ndvi, coast, sar)
        assert score[0, 0] > mm.SCORE_THRESHOLD
        assert mask[0, 0]

        # upland: high ndvi but far from coast
        coast_far = np.array([[40.0]], dtype=np.float32)
        _, score_far, _ = mm.mangrove_score(ndvi, coast_far, sar)
        assert score_far[0, 0] < mm.SCORE_THRESHOLD

    def test_no_sar_still_works(self):
        ndvi = np.array([[0.75]], dtype=np.float32)
        coast = np.array([[3.0]], dtype=np.float32)
        mask, score, comp = mm.mangrove_score(ndvi, coast, sar=None)
        assert comp["sar_used"] is False
        assert score[0, 0] > mm.SCORE_THRESHOLD


class TestExtract:
    def test_synthetic_recovery_matches_truth(self):
        bbox = [110.0, 21.0, 111.0, 22.0]
        cube, truth, info = mm.generate_synthetic_scene(bbox, seed=1)
        mask, score, indices, comp = mm.extract_mangroves(cube)
        pred = mask.astype(bool)
        gt = truth.astype(bool)
        inter = np.logical_and(pred, gt).sum()
        union = np.logical_or(pred, gt).sum()
        iou = inter / union
        assert iou > 0.5, f"IoU too low: {iou}"

    def test_water_not_classified(self):
        bbox = [110.0, 21.0, 111.0, 22.0]
        cube, truth, info = mm.generate_synthetic_scene(bbox)
        mask, score, indices, _ = mm.extract_mangroves(cube)
        water = indices["water"] > 0.5
        # no water pixel should be classified as mangrove
        assert np.logical_and(mask, water).sum() == 0

    def test_too_few_bands_raises(self):
        cube = np.random.uniform(0, 1, (3, 8, 8)).astype(np.float32)
        with pytest.raises(mm.ValidationError):
            mm.extract_mangroves(cube)


class TestChange:
    def test_gain_loss_accounting(self):
        m0 = np.zeros((10, 10), dtype=bool)
        m0[0:5, :] = True       # 50 px at t0
        m1 = np.zeros((10, 10), dtype=bool)
        m1[0:3, :] = True       # 30 persist-ish
        m1[7:10, :] = True      # 30 gain
        chg = mm.mangrove_change(m0, m1, pixel_area_m2=2.0)
        # overlap rows 0:3 = 30 persist; loss rows 3:5 = 20; gain rows 7:10 = 30
        assert chg["persist_px"] == 30
        assert chg["loss_px"] == 20
        assert chg["gain_px"] == 30
        assert chg["area_t0_m2"] == 100.0
        assert chg["net_change_m2"] == (60 - 50) * 2.0


class TestSynthetic:
    def test_scene_shape_and_truth(self):
        cube, truth, info = mm.generate_synthetic_scene([110, 21, 111, 22])
        assert cube.shape == (5, 128, 128)
        assert truth.shape == (128, 128)
        assert truth.sum() > 0
        assert info["truth_mangrove_px"] == int(truth.sum())

    def test_epoch_shrinks_mangrove(self):
        _, t0, i0 = mm.generate_synthetic_scene([110, 21, 111, 22], epoch=0)
        _, t2, i2 = mm.generate_synthetic_scene([110, 21, 111, 22], epoch=2)
        assert i2["mangrove_width_frac"] < i0["mangrove_width_frac"]


class TestPixelArea:
    def test_positive_and_scale(self):
        a = mm.pixel_area_m2([110.0, 21.0, 111.0, 22.0], 128, 128)
        assert a > 0
        # smaller bbox -> smaller pixel area
        b = mm.pixel_area_m2([110.0, 21.0, 110.5, 21.5], 128, 128)
        assert b < a


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (5, 16, 16)).astype(np.float32)
        bbox = [110.0, 21.0, 111.0, 22.0]
        path = str(tmp_path / "t.tif")
        mm.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        back, rb = mm.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(mm.UsageError):
            mm.read_geotiff("/nonexistent/file.tif")
