"""Core algorithm tests for glacier-retreat-monitoring."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as gr


class TestNDSI:
    def test_snow_high(self):
        green = np.full((4, 4), 0.80, dtype=np.float32)
        swir = np.full((4, 4), 0.10, dtype=np.float32)
        ndsi = gr.ndsi_index(green, swir)
        assert np.allclose(ndsi, 0.7 / 0.9, atol=1e-5)
        assert ndsi.mean() > 0.4

    def test_rock_low(self):
        green = np.full((4, 4), 0.12, dtype=np.float32)
        swir = np.full((4, 4), 0.35, dtype=np.float32)
        assert gr.ndsi_index(green, swir).mean() < 0

    def test_zero_denominator_safe(self):
        z = np.zeros((3, 3), dtype=np.float32)
        assert np.all(gr.ndsi_index(z, z) == 0)


class TestMaskAndTerminus:
    def test_mask_threshold(self):
        ndsi = np.array([[0.1, 0.5, 0.8]], dtype=np.float32)
        mask = gr.glacier_mask(ndsi)
        assert mask.tolist() == [[False, True, True]]

    def test_terminus_row_empty(self):
        assert np.isnan(gr.terminus_row(np.zeros((4, 4), dtype=bool)))

    def test_terminus_row_centroid(self):
        mask = np.zeros((10, 10), dtype=bool)
        mask[2:4, :] = True  # rows 2,3 -> mean 2.5
        assert abs(gr.terminus_row(mask) - 2.5) < 1e-6


class TestPolygons:
    def test_polygons_generated(self):
        mask = np.zeros((32, 32), dtype=bool)
        mask[4:16, 4:16] = True
        bbox = [86.0, 28.0, 87.0, 29.0]
        feats = gr.glacier_polygons(mask, bbox, date_index=0, pixel_area_m2=100.0)
        assert len(feats) >= 1
        f = feats[0]
        assert f["type"] == "Feature"
        assert f["geometry"]["type"] in ("Polygon", "MultiPolygon")
        assert f["properties"]["date_index"] == 0
        assert f["properties"]["area_m2"] == pytest.approx(mask.sum() * 100.0)

    def test_empty_mask_no_polygons(self):
        mask = np.zeros((16, 16), dtype=bool)
        feats = gr.glacier_polygons(mask, [86, 28, 87, 29], date_index=0)
        assert feats == []


class TestAnalyzeRetreat:
    def test_retreat_detected(self):
        areas = [1000.0, 800.0, 600.0]
        rows = [10.0, 8.0, 6.0]  # decreasing -> upslope retreat
        res = gr.analyze_retreat(areas, rows, pixel_size_m=50.0, years_per_step=1.0)
        assert res["retreating"] is True
        assert res["total_terminus_shift_m"] == pytest.approx(-200.0)
        assert res["total_area_change_m2"] == pytest.approx(-400.0)
        assert res["interval_rates"][0]["retreat_rate_m_per_yr"] == pytest.approx(-100.0)

    def test_advance_detected(self):
        areas = [600.0, 800.0]
        rows = [6.0, 9.0]  # increasing -> advance
        res = gr.analyze_retreat(areas, rows, pixel_size_m=50.0)
        assert res["retreating"] is False
        assert res["total_terminus_shift_m"] > 0


class TestSynthetic:
    def test_shape(self):
        cube, elev, info = gr.generate_synthetic_series([86, 28, 87, 29], n_dates=3)
        assert cube.shape == (3, 2, 128, 128)
        assert elev.shape == (128, 128)

    def test_glacier_retreats_over_time(self):
        cube, elev, info = gr.generate_synthetic_series([86, 28, 87, 29], n_dates=3, seed=7)
        greens, swirs = gr.unpack_cube(cube, 3)
        areas, rows = [], []
        for k in range(3):
            mask = gr.glacier_mask(gr.ndsi_index(greens[k], swirs[k]))
            areas.append(mask.sum())
            rows.append(gr.terminus_row(mask))
        # area should decrease each epoch
        assert areas[0] > areas[1] > areas[2]
        # terminus row should decrease (upslope retreat)
        assert rows[0] > rows[-1]

    def test_unpack_wrong_shape_raises(self):
        bad = np.zeros((3, 128, 128), dtype=np.float32)
        with pytest.raises(gr.ValidationError):
            gr.unpack_cube(bad, 3)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 2, 16, 16)).astype(np.float32)
        # write a single-band slice to test 3D path
        bbox = [86.0, 28.0, 87.0, 29.0]
        path = str(tmp_path / "t.tif")
        gr.write_geotiff(path, cube[0], bbox)
        back, rb = gr.read_geotiff(path)
        assert back.shape == (2, 16, 16)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(gr.UsageError):
            gr.read_geotiff("/nonexistent/x.tif")
