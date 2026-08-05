"""Core algorithm tests for lake-area-change."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as lc

SMALL_BBOX = [116.0, 39.0, 116.03, 39.03]


class TestComputeIndex:
    def test_water_positive_land_negative(self):
        green = np.array([0.06, 0.10])
        nir = np.array([0.015, 0.42])
        idx = lc.compute_index(green, nir)
        assert idx[0] > 0.3   # 水体高 NDWI
        assert idx[1] < -0.3  # 陆地低 NDWI

    def test_zero_denominator(self):
        idx = lc.compute_index(np.array([0.0]), np.array([0.0]))
        assert idx[0] == 0.0

    def test_bounded(self):
        rng = np.random.default_rng(0)
        g = rng.uniform(0, 0.5, (32, 32))
        n = rng.uniform(0, 0.5, (32, 32))
        idx = lc.compute_index(g, n)
        assert idx.min() >= -1.0 and idx.max() <= 1.0


class TestExtractWater:
    def test_threshold(self):
        idx = np.array([[-0.5, 0.1], [0.0, 0.6]])
        mask = lc.extract_water(idx, threshold=0.0)
        assert mask.tolist() == [[False, True], [True, True]]


class TestLakeArea:
    def test_area_scaling(self):
        mask = np.zeros((10, 10), dtype=bool)
        mask[0:5, 0:5] = True  # 25 cells
        area = lc.lake_area_km2(mask, cell_area_m2=10000.0)  # 1 ha/cell
        assert area == pytest.approx(25 * 10000.0 / 1e6)


class TestFitTrend:
    def test_shrinking(self):
        areas = np.array([10.0, 8.0, 6.0, 4.0, 2.0])
        t = lc.fit_trend(areas)
        assert t["trend"] == "shrinking"
        assert t["slope_per_step"] == pytest.approx(-2.0)
        assert t["r_squared"] == pytest.approx(1.0, abs=1e-6)
        assert t["total_change_pct"] < 0

    def test_expanding(self):
        areas = np.array([2.0, 4.0, 6.0, 8.0, 10.0])
        t = lc.fit_trend(areas)
        assert t["trend"] == "expanding"
        assert t["slope_per_step"] > 0

    def test_stable(self):
        areas = np.array([5.0, 5.01, 4.99, 5.0, 5.02])
        t = lc.fit_trend(areas)
        assert t["trend"] == "stable"

    def test_too_few_dates_raises(self):
        with pytest.raises(lc.UsageError):
            lc.fit_trend(np.array([5.0]))


class TestPolygonize:
    def test_returns_features(self):
        mask = np.zeros((20, 20), dtype=bool)
        mask[5:12, 5:12] = True
        feats = lc.polygonize_water(mask, SMALL_BBOX, date_index=0, area_km2=1.23)
        assert len(feats) >= 1
        f = feats[0]
        assert f["type"] == "Feature"
        assert f["geometry"]["type"] in ("Polygon", "MultiPolygon")
        assert f["properties"]["date_index"] == 0
        assert f["properties"]["area_km2"] == pytest.approx(1.23)


class TestSynthetic:
    def test_cube_shape(self):
        cube, info = lc.generate_synthetic(SMALL_BBOX, n_dates=5, width=64, height=64)
        assert cube.shape == (5, 64, 64)
        assert info["n_dates"] == 5
        assert len(info["true_areas_km2"]) == 5

    def test_shrinking_true_areas_decrease(self):
        cube, info = lc.generate_synthetic(SMALL_BBOX, n_dates=6, trend="shrinking")
        areas = info["true_areas_km2"]
        assert areas[0] > areas[-1]

    def test_expanding_true_areas_increase(self):
        cube, info = lc.generate_synthetic(SMALL_BBOX, n_dates=6, trend="expanding")
        areas = info["true_areas_km2"]
        assert areas[-1] > areas[0]

    def test_single_date_raises(self):
        with pytest.raises(lc.UsageError):
            lc.generate_synthetic(SMALL_BBOX, n_dates=1)


@pytest.mark.parametrize("trend", ["shrinking", "expanding", "stable"])
class TestEndToEndTrend:
    def test_detected_trend_matches_injected(self, trend):
        """检测到的面积趋势应与注入一致。"""
        cube, info = lc.generate_synthetic(
            SMALL_BBOX, n_dates=6, width=80, height=80, trend=trend, seed=11)
        result = lc.run_model(cube, info["cell_area_m2"], SMALL_BBOX, threshold=0.0)
        assert result["trend"]["trend"] == trend
        assert result["n_dates"] == 6
        assert len(result["areas_km2"]) == 6
        assert len(result["features"]) >= 1
        # 面积应为正且有限
        assert all(a >= 0 for a in result["areas_km2"])
        if trend == "shrinking":
            assert result["trend"]["slope_per_step"] < 0
            assert result["areas_km2"][0] > result["areas_km2"][-1]
        elif trend == "expanding":
            assert result["trend"]["slope_per_step"] > 0
            assert result["areas_km2"][-1] > result["areas_km2"][0]


class TestDetectedVsTrue:
    def test_detected_areas_close_to_true(self):
        """提取面积应与真值面积接近（像元量化误差内）。"""
        cube, info = lc.generate_synthetic(
            SMALL_BBOX, n_dates=5, width=96, height=96, trend="shrinking", seed=3)
        result = lc.run_model(cube, info["cell_area_m2"], SMALL_BBOX, threshold=0.0)
        true = np.array(info["true_areas_km2"])
        det = np.array(result["areas_km2"])
        # 相对误差 < 10%
        rel = np.abs(det - true) / np.maximum(true, 1e-9)
        assert np.all(rel < 0.10)


class TestGeoTiffIO:
    def test_roundtrip_multiband(self, tmp_path):
        arr = np.random.uniform(-1, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "s.tif")
        lc.write_geotiff(path, arr, bbox)
        back, rbbox, ca = lc.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, arr, atol=1e-4)
        assert ca > 0

    def test_read_missing_raises(self):
        with pytest.raises(lc.UsageError):
            lc.read_geotiff("/nonexistent/x.tif")
