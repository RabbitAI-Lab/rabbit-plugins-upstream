"""Core algorithm tests for sar-flood-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as sfm


class TestParseThreshold:
    def test_auto(self):
        assert sfm.parse_threshold("auto") is None
        assert sfm.parse_threshold("AUTO") is None

    def test_numeric(self):
        assert sfm.parse_threshold("0.01") == pytest.approx(0.01)

    def test_bad_raises(self):
        with pytest.raises(sfm.UsageError):
            sfm.parse_threshold("bogus")


class TestOtsu:
    def test_bimodal_threshold_between_modes(self):
        rng = np.random.default_rng(0)
        low = rng.normal(0.003, 0.001, 3000)
        high = rng.normal(0.06, 0.01, 7000)
        vals = np.concatenate([low, high]).astype(np.float32)
        thr = sfm.otsu_threshold(vals)
        assert 0.01 < thr < 0.04  # 落在两峰之间

    def test_constant_returns_value(self):
        vals = np.full(100, 0.5, dtype=np.float32)
        thr = sfm.otsu_threshold(vals)
        assert thr == pytest.approx(0.5)

    def test_empty_raises(self):
        with pytest.raises(sfm.ValidationError):
            sfm.otsu_threshold(np.full(10, np.nan))


class TestSlope:
    def test_flat_dem_zero_slope(self):
        dem = np.full((16, 16), 100.0, dtype=np.float32)
        slope = sfm.slope_from_dem(dem, 30.0, 30.0)
        np.testing.assert_allclose(slope, 0.0, atol=1e-4)

    def test_tilted_plane_slope(self):
        # z = x（每米升 1m）→ 坡度 45°
        x = np.arange(32, dtype=np.float32)
        dem = np.broadcast_to(x[None, :], (8, 32)).copy()
        slope = sfm.slope_from_dem(dem, 1.0, 1.0)
        np.testing.assert_allclose(slope[:, 2:-2], 45.0, atol=1.0)


class TestExtractWater:
    def test_recovers_truth_fraction(self):
        cube, info = sfm.generate_synthetic([116, 39, 117, 40], seed=7)
        mask, thr = sfm.extract_water(cube[0])
        truth = info["water_truth"]
        frac_det = mask.mean()
        frac_truth = info["truth_water_fraction"]
        assert abs(frac_det - frac_truth) < frac_truth * 0.4 + 0.02
        # IoU
        inter = np.logical_and(mask > 0, truth > 0).sum()
        union = np.logical_or(mask > 0, truth > 0).sum()
        assert inter / union > 0.5

    def test_opening_removes_isolated_pixel(self):
        sigma = np.full((16, 16), 0.1, dtype=np.float32)
        sigma[8, 8] = 0.0001  # 孤立低值点
        mask_open, _ = sfm.extract_water(sigma, threshold=0.001, opening=True)
        mask_raw, _ = sfm.extract_water(sigma, threshold=0.001, opening=False)
        assert mask_raw.sum() >= 1
        assert mask_open.sum() == 0  # 开运算去掉孤立点

    def test_manual_threshold(self):
        cube, _ = sfm.generate_synthetic([116, 39, 117, 40])
        mask, thr = sfm.extract_water(cube[0], threshold=0.01)
        assert thr == pytest.approx(0.01)
        assert mask.dtype == np.uint8


class TestAreaStats:
    def test_fraction_and_pixels(self):
        mask = np.zeros((10, 10), dtype=np.uint8)
        mask[:5, :] = 1
        stats = sfm.flood_area_stats(mask, [116.0, 39.0, 117.0, 40.0])
        assert stats["water_pixels"] == 50
        assert stats["total_pixels"] == 100
        assert stats["water_fraction"] == pytest.approx(0.5)
        assert stats["area_km2"] > 0


class TestVectorize:
    def test_has_features(self):
        from rasterio.transform import from_bounds
        mask = np.zeros((16, 16), dtype=np.uint8)
        mask[4:10, 4:10] = 1
        tr = from_bounds(116.0, 39.0, 117.0, 40.0, 16, 16)
        fc = sfm.vectorize_mask(mask, tr)
        assert fc["type"] == "FeatureCollection"
        assert len(fc["features"]) >= 1
        assert fc["features"][0]["geometry"]["type"] in ("Polygon", "MultiPolygon")

    def test_empty_mask_no_features(self):
        from rasterio.transform import from_bounds
        mask = np.zeros((8, 8), dtype=np.uint8)
        tr = from_bounds(116.0, 39.0, 117.0, 40.0, 8, 8)
        fc = sfm.vectorize_mask(mask, tr)
        assert fc["features"] == []

    def test_write_geojson_readable(self, tmp_path):
        import geopandas as gpd
        from rasterio.transform import from_bounds
        mask = np.zeros((16, 16), dtype=np.uint8)
        mask[4:10, 4:10] = 1
        tr = from_bounds(116.0, 39.0, 117.0, 40.0, 16, 16)
        fc = sfm.vectorize_mask(mask, tr)
        path = str(tmp_path / "flood.geojson")
        sfm.write_geojson(path, fc)
        assert os.path.exists(path)
        gdf = gpd.read_file(path)
        assert len(gdf) >= 1

    def test_write_geojson_empty(self, tmp_path):
        import geopandas as gpd
        path = str(tmp_path / "empty.geojson")
        sfm.write_geojson(path, {"type": "FeatureCollection", "features": []})
        assert os.path.exists(path)
        gdf = gpd.read_file(path)
        assert len(gdf) == 0


class TestSynthetic:
    def test_shapes_and_truth(self):
        cube, info = sfm.generate_synthetic([116, 39, 117, 40])
        assert cube.shape == (1, 64, 64)
        assert info["water_truth"].shape == (64, 64)
        assert 0.0 < info["truth_water_fraction"] < 0.5

    def test_water_is_low_backscatter(self):
        cube, info = sfm.generate_synthetic([116, 39, 117, 40])
        sigma = cube[0]
        truth = info["water_truth"]
        assert sigma[truth > 0].mean() < sigma[truth == 0].mean() * 0.3


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(1).uniform(0.001, 0.1, (1, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        sfm.write_geotiff(path, cube, bbox)
        back, rbbox = sfm.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_read_missing_file_raises(self):
        with pytest.raises(sfm.UsageError):
            sfm.read_geotiff("/nonexistent/path/file.tif")
