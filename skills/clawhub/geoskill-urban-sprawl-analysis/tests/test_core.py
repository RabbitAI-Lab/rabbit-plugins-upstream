"""Core algorithm tests for urban-sprawl-analysis."""
import math
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as us


def disk(h, w, cx, cy, r):
    yy, xx = np.mgrid[0:h, 0:w]
    return (((xx - cx) ** 2 + (yy - cy) ** 2) <= r * r).astype(np.int32)


class TestPerimeter:
    def test_empty_zero(self):
        assert us.perimeter_pixels(np.zeros((10, 10), np.int32)) == 0

    def test_full_block_perimeter(self):
        b = np.ones((10, 10), np.int32)
        # 4-neighbor edge of a full 10x10 block = outer ring = 36 pixels
        assert us.perimeter_pixels(b) == 36

    def test_single_pixel(self):
        b = np.zeros((5, 5), np.int32)
        b[2, 2] = 1
        assert us.perimeter_pixels(b) == 1


class TestCompactnessFractal:
    def test_square_compactness(self):
        # square: 4*pi*A/P^2 = pi/4 ~ 0.785 (A in px, P in px for n x n: P=4n? use pixel counts)
        c = us.compactness(area_px=100, perimeter_px=36)
        assert 0.5 < c <= 1.0

    def test_compactness_bounds(self):
        assert us.compactness(0, 10) == 0.0
        assert us.compactness(10, 0) == 0.0
        assert 0.0 <= us.compactness(1000, 10) <= 1.0

    def test_fractal_bounds(self):
        d = us.fractal_dimension(area_px=100, perimeter_px=36)
        assert 1.0 <= d <= 2.0
        assert us.fractal_dimension(area_px=1, perimeter_px=4) == 1.0


class TestCentroid:
    def test_empty_none(self):
        assert us.centroid_lonlat(np.zeros((10, 10), np.int32), [0, 0, 1, 1]) is None

    def test_center_of_full_raster(self):
        b = np.ones((10, 10), np.int32)
        c = us.centroid_lonlat(b, [0.0, 0.0, 1.0, 1.0])
        # full raster centroid ~ middle
        assert abs(c[0] - 0.5) < 0.06
        assert abs(c[1] - 0.5) < 0.06

    def test_centroid_inside_bbox(self):
        b = disk(20, 20, 5, 15, 3)
        c = us.centroid_lonlat(b, [10.0, 20.0, 11.0, 21.0])
        assert 10.0 <= c[0] <= 11.0
        assert 20.0 <= c[1] <= 21.0


class TestCentroidDistance:
    def test_zero_when_none(self):
        assert us.centroid_distance_km(None, [1, 1]) == 0.0

    def test_latitude_degree(self):
        # 1 degree latitude ~ 110.57 km
        d = us.centroid_distance_km([116.0, 39.0], [116.0, 40.0])
        assert d == pytest.approx(110.57, rel=1e-3)


class TestUrbanMetrics:
    def test_empty_metrics(self):
        m = us.urban_metrics(np.zeros((8, 8), np.int32), [0, 0, 1, 1])
        assert m["present"] is False
        assert m["urban_pixels"] == 0

    def test_disk_metrics(self):
        b = disk(40, 40, 20, 20, 12)
        m = us.urban_metrics(b, [116.0, 39.0, 117.0, 40.0])
        assert m["present"] is True
        assert m["urban_pixels"] > 0
        assert m["urban_area_km2"] > 0
        assert 0.0 < m["compactness"] <= 1.0
        assert 1.0 <= m["fractal_dimension"] <= 2.0
        assert m["centroid"] is not None

    def test_bad_ndim_raises(self):
        with pytest.raises(us.ValidationError):
            us.urban_metrics(np.zeros((2, 2, 2), np.int32), [0, 0, 1, 1])


class TestSyntheticSeries:
    def test_shape_and_growth(self):
        stack, info = us.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=4, width=64, height=64, seed=1)
        assert stack.shape == (4, 64, 64)
        assert set(np.unique(stack).tolist()) <= {0, 1}
        counts = info["urban_pixels_per_date"]
        assert all(counts[i + 1] >= counts[i] for i in range(len(counts) - 1))
        assert counts[-1] > counts[0]  # expansion

    def test_n_dates_min(self):
        stack, info = us.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=1, width=32, height=32)
        assert stack.shape[0] == 2  # bumped to >=2


class TestTimeSeries:
    def test_expansion_and_centroid_shift(self):
        stack, info = us.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=4, width=80, height=80, seed=2)
        ts = us.sprawl_time_series(stack, [116, 39, 117, 40],
                                   start_year=2000, interval_years=5)
        assert len(ts["dates"]) == 4
        assert len(ts["changes"]) == 3
        assert ts["summary"]["net_expansion_detected"] is True
        assert ts["summary"]["total_net_area_km2"] > 0
        # centroid drifts east (positive longitude shift) due to east lobe
        first = ts["summary"]["first_centroid"]
        last = ts["summary"]["last_centroid"]
        assert last[0] > first[0]
        assert ts["summary"]["total_centroid_shift_km"] > 0

    def test_bad_ndim_raises(self):
        with pytest.raises(us.ValidationError):
            us.sprawl_time_series(np.zeros((10, 10), np.int32), [0, 0, 1, 1])

    def test_year_labels(self):
        stack, _ = us.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=3, width=32, height=32)
        ts = us.sprawl_time_series(stack, [116, 39, 117, 40],
                                   start_year=2005, interval_years=10)
        years = [d["year"] for d in ts["dates"]]
        assert years == [2005, 2015, 2025]


class TestVectorize:
    def test_geodataframe(self):
        stack, _ = us.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=3, width=48, height=48, seed=3)
        gdf = us.vectorize_series(stack, [116, 39, 117, 40])
        assert len(gdf) > 0
        assert str(gdf.crs) == "EPSG:4326"
        assert set(["date_index", "year"]).issubset(gdf.columns)

    def test_write_geojson(self, tmp_path):
        stack, _ = us.generate_synthetic_series(
            [116, 39, 117, 40], n_dates=2, width=32, height=32, seed=4)
        gdf = us.vectorize_series(stack, [116, 39, 117, 40])
        path = str(tmp_path / "foot.geojson")
        gdf.to_file(path, driver="GeoJSON")
        assert os.path.exists(path)


class TestGeoTiffIO:
    def test_stack_roundtrip(self, tmp_path):
        stack = np.random.randint(0, 2, (3, 12, 12)).astype(np.int32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "s.tif")
        us.write_geotiff(path, stack, bbox, dtype="int32")
        back, rbbox = us.read_binary_stack(path)
        assert back.shape == (3, 12, 12)
        np.testing.assert_array_equal(back, stack)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(us.UsageError):
            us.read_binary_stack("/nonexistent/none.tif")


class TestValidateBbox:
    def test_valid(self):
        b = us.validate_bbox([116.0, 39.0, 117.0, 40.0])
        assert b == [116.0, 39.0, 117.0, 40.0]

    def test_w_ge_e_raises(self):
        with pytest.raises(us.ValidationError):
            us.validate_bbox([117.0, 39.0, 116.0, 40.0])

    def test_s_ge_n_raises(self):
        with pytest.raises(us.ValidationError):
            us.validate_bbox([116.0, 40.0, 117.0, 39.0])

    def test_zero_area_raises(self):
        with pytest.raises(us.ValidationError):
            us.validate_bbox([116.0, 39.0, 116.0, 40.0])

    def test_lat_out_of_range_raises(self):
        with pytest.raises(us.ValidationError):
            us.validate_bbox([116.0, 39.0, 117.0, 95.0])

    def test_lon_out_of_range_raises(self):
        with pytest.raises(us.ValidationError):
            us.validate_bbox([200.0, 39.0, 210.0, 40.0])

    def test_none_raises(self):
        with pytest.raises(us.ValidationError):
            us.validate_bbox(None)

    def test_wrong_length_raises(self):
        with pytest.raises(us.ValidationError):
            us.validate_bbox([116.0, 39.0, 117.0])
