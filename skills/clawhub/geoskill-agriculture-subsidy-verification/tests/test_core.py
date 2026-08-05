"""Core algorithm tests for agriculture-subsidy-verification — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod

gpd = pytest.importorskip("geopandas")
from shapely.geometry import box  # noqa: E402
from rasterio.transform import from_bounds  # noqa: E402


def _two_parcels():
    """10x10 网格，左右两个地块（parcel 1/2），完整覆盖。"""
    transform = from_bounds(0.0, 0.0, 10.0, 10.0, 10, 10)
    gdf = gpd.GeoDataFrame(
        {"parcel_id": [1, 2], "declared_crop_frac": [0.9, 0.8]},
        geometry=[box(0, 0, 5, 10), box(5, 0, 10, 10)], crs="EPSG:4326",
    )
    return gdf, transform


class TestClassifyCrop:
    def test_threshold_exact(self):
        ndvi = np.array([[0.1, 0.3, 0.5]], dtype=np.float32)
        mask = mod.classify_crop(ndvi, threshold=0.3)
        assert list(mask[0]) == [0, 1, 1]

    def test_high_ndvi_is_crop(self):
        ndvi = np.full((4, 4), 0.6, dtype=np.float32)
        assert mod.classify_crop(ndvi).mean() == 1.0

    def test_bare_is_noncrop(self):
        ndvi = np.full((4, 4), 0.1, dtype=np.float32)
        assert mod.classify_crop(ndvi).mean() == 0.0

    def test_2d_required(self):
        with pytest.raises(mod.ValidationError):
            mod.classify_crop(np.zeros((2, 4, 4)))


class TestRasterize:
    def test_burns_parcels(self):
        gdf, transform = _two_parcels()
        grid = mod.rasterize_parcels(gdf, transform, out_shape=(10, 10))
        assert grid.shape == (10, 10)
        # left half parcel 1, right half parcel 2, full coverage (no 0)
        assert (grid[:, :5] == 1).all()
        assert (grid[:, 5:] == 2).all()
        assert (grid > 0).all()

    def test_missing_column_raises(self):
        transform = from_bounds(0, 0, 10, 10, 10, 10)
        gdf = gpd.GeoDataFrame({"foo": [1]}, geometry=[box(0, 0, 5, 10)], crs="EPSG:4326")
        with pytest.raises(mod.ValidationError):
            mod.rasterize_parcels(gdf, transform, out_shape=(10, 10))


class TestObservedFractions:
    def test_full_crop_parcel(self):
        gdf, transform = _two_parcels()
        grid = mod.rasterize_parcels(gdf, transform, out_shape=(10, 10))
        crop = np.zeros((10, 10), dtype=np.uint8)
        crop[:, :5] = 1  # parcel 1 fully cropped; parcel 2 bare
        fracs = mod.observed_crop_fractions(crop, grid)
        assert fracs[1] == pytest.approx(1.0, abs=1e-6)
        assert fracs[2] == pytest.approx(0.0, abs=1e-6)

    def test_shape_mismatch_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.observed_crop_fractions(np.zeros((4, 4)), np.zeros((5, 5)))


class TestVerifySubsidy:
    def test_consistent_not_flagged(self):
        gdf, _ = _two_parcels()
        obs = {1: 0.9, 2: 0.8}  # matches declared exactly
        records = mod.verify_subsidy(gdf, obs, tolerance=0.15)
        assert all(not r["flagged"] for r in records)
        assert all(r["reason"] == "consistent" for r in records)

    def test_over_declared_flagged(self):
        gdf, _ = _two_parcels()
        obs = {1: 0.9, 2: 0.1}  # parcel 2 declared 0.8 but observed 0.1
        records = mod.verify_subsidy(gdf, obs, tolerance=0.15)
        rec2 = next(r for r in records if r["parcel_id"] == 2)
        assert rec2["flagged"] is True
        assert rec2["reason"] == "over-declared"

    def test_under_declared_flagged(self):
        gdf, _ = _two_parcels()
        obs = {1: 0.9, 2: 1.0}  # declared 0.8 observed 1.0 -> diff +0.2 > 0.15
        records = mod.verify_subsidy(gdf, obs, tolerance=0.15)
        rec2 = next(r for r in records if r["parcel_id"] == 2)
        assert rec2["flagged"] is True
        assert rec2["reason"] == "under-declared"


class TestFullPipeline:
    def test_synthetic_flags_fraudulent_parcels(self):
        ndvi, packed = mod.generate_synthetic([116, 39, 117, 40])
        gdf, transform = packed["parcels"], packed["transform"]
        res = mod.run_verification(ndvi, gdf, transform, threshold=0.30, tolerance=0.15)
        flagged_ids = {r["parcel_id"] for r in res["records"] if r["flagged"]}
        # parcels 3 (over-declared) and 4 (under-declared) must be flagged
        assert 3 in flagged_ids
        assert 4 in flagged_ids
        # parcels 1 and 2 are honest -> not flagged
        assert 1 not in flagged_ids
        assert 2 not in flagged_ids
        assert res["stats"]["n_flagged"] == 2
        assert res["crop_mask"].shape == ndvi.shape
