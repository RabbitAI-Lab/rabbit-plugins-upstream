"""Core algorithm tests for disaster-exposure-assessment."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ex


class TestExposedTotal:
    def test_exact_sum_inside(self):
        """暴露量 = 危险区内资产之和（精确相等）。"""
        mask = np.array([[True, False], [True, True]])
        value = np.array([[10.0, 100.0], [20.0, 30.0]])
        assert abs(ex.exposed_total(mask, value) - 60.0) < 1e-9

    def test_no_hazard_zero_exposure(self):
        mask = np.zeros((5, 5), dtype=bool)
        value = np.random.uniform(0, 100, (5, 5))
        assert ex.exposed_total(mask, value) == 0.0

    def test_superset_monotonic(self):
        """危险区扩大（超集）→ 暴露量不减。"""
        value = np.random.default_rng(0).uniform(1, 100, (10, 10))
        small = np.zeros((10, 10), dtype=bool); small[0:3, 0:3] = True
        large = small.copy(); large[3:6, 3:6] = True
        assert ex.exposed_total(large, value) >= ex.exposed_total(small, value)

    def test_shape_mismatch_raises(self):
        with pytest.raises(ex.ValidationError):
            ex.exposed_total(np.zeros((4, 4), dtype=bool), np.zeros((4, 5)))


class TestExposureFraction:
    def test_full_hazard_is_one(self):
        mask = np.ones((4, 4), dtype=bool)
        value = np.random.uniform(1, 10, (4, 4))
        assert abs(ex.exposure_fraction(mask, value) - 1.0) < 1e-9

    def test_zero_total_is_zero(self):
        assert ex.exposure_fraction(np.ones((3, 3), dtype=bool), np.zeros((3, 3))) == 0.0


class TestExposureByZone:
    def test_partition_sums_to_total(self):
        """各分区之和 = 全区总和。"""
        rng = np.random.default_rng(1)
        zones = np.array([[0, 1], [2, 1]])
        value = rng.uniform(1, 50, (2, 2))
        by = ex.exposure_by_zone(zones, value)
        assert set(by.keys()) == {0, 1, 2}
        assert abs(sum(by.values()) - value.sum()) < 1e-6
        assert abs(by[1] - (value[0, 1] + value[1, 1])) < 1e-9

    def test_shape_mismatch_raises(self):
        with pytest.raises(ex.ValidationError):
            ex.exposure_by_zone(np.zeros((4, 4), dtype=int), np.zeros((4, 5)))


class TestClassifyHazard:
    def test_levels_and_no_hazard(self):
        intensity = np.array([[0.0, 0.3, 1.0, 2.0]])
        z = ex.classify_hazard(intensity, breaks=(0.5, 1.5))
        assert z[0, 0] == 0  # 0 强度 → 无危险
        assert z[0, 1] == 0  # <0.5
        assert z[0, 2] == 1  # 0.5-1.5
        assert z[0, 3] == 2  # >1.5


class TestPointExposure:
    def test_counts_only_inside(self):
        from shapely.geometry import box
        poly = box(0, 0, 10, 10)  # 方形危险区
        pts = np.array([[5.0, 5.0], [20.0, 20.0], [1.0, 1.0]])  # 2 内 1 外
        vals = np.array([100.0, 999.0, 50.0])
        total, count = ex.point_exposure(pts, vals, poly)
        assert count == 2
        assert abs(total - 150.0) < 1e-9

    def test_empty_points(self):
        from shapely.geometry import box
        total, count = ex.point_exposure(np.zeros((0, 2)), np.zeros(0), box(0, 0, 1, 1))
        assert total == 0.0 and count == 0

    def test_bad_points_shape_raises(self):
        from shapely.geometry import box
        with pytest.raises(ex.ValidationError):
            ex.point_exposure(np.zeros((3, 3)), np.zeros(3), box(0, 0, 1, 1))


class TestVectorize:
    def test_produces_polygons(self):
        from rasterio.transform import from_bounds
        mask = np.zeros((20, 20), dtype=bool)
        mask[5:15, 5:15] = True
        transform = from_bounds(116, 39, 117, 40, 20, 20)
        polys = ex.vectorize_mask(mask, transform)
        assert len(polys) >= 1
        assert abs(polys[0].area - (10 / 20 * 1 * 10 / 20 * 1)) < 1e-6  # ~0.25 deg²


class TestSynthetic:
    def test_shapes(self):
        layers, info = ex.generate_synthetic([116, 39, 117, 40])
        for k in ("hazard", "asset", "population"):
            assert layers[k].shape == (64, 64)
        assert layers["points_xy"].shape[1] == 2
        assert info["n_points"] == layers["points_xy"].shape[0]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        p = str(tmp_path / "e.tif")
        ex.write_geotiff(p, cube, bbox)
        back, bb = ex.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ex.UsageError):
            ex.read_geotiff("/nonexistent/e.tif")
