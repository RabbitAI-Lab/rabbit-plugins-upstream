"""Core algorithm tests for precision-farming-zoning — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestStandardize:
    def test_zero_mean_unit_std(self):
        rng = np.random.default_rng(0)
        cube = rng.uniform(0, 100, (3, 40, 40)).astype(np.float32)
        std, stats = mod.standardize_layers(cube)
        for b in range(3):
            assert abs(float(std[b].mean())) < 1e-4
            assert abs(float(std[b].std()) - 1.0) < 1e-3
        assert len(stats) == 3

    def test_constant_layer_no_crash(self):
        cube = np.full((2, 10, 10), 5.0, dtype=np.float32)
        std, stats = mod.standardize_layers(cube)
        assert np.isfinite(std).all()

    def test_wrong_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.standardize_layers(np.zeros((10, 10), dtype=np.float32))


class TestKmeansZone:
    def test_recovers_three_zones(self):
        # three well-separated spatial clusters across a feature
        h, w = 30, 30
        feat = np.zeros((h, w, 2), dtype=np.float32)
        feat[:10, :] = 0.0
        feat[10:20, :] = 5.0
        feat[20:, :] = 10.0
        labels = mod.kmeans_zone(feat, n_zones=3)
        assert labels.shape == (h, w)
        # each horizontal band should be a single uniform zone
        assert len(np.unique(labels[:10])) == 1
        assert len(np.unique(labels[10:20])) == 1
        assert len(np.unique(labels[20:])) == 1
        # three distinct zones total
        assert len(np.unique(labels)) == 3

    def test_zone_count_capped_by_data(self):
        feat = np.zeros((8, 8, 2), dtype=np.float32)
        labels = mod.kmeans_zone(feat, n_zones=5)
        assert labels.max() + 1 <= 5

    def test_invalid_nzones_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.kmeans_zone(np.zeros((4, 4, 2), dtype=np.float32), n_zones=0)


class TestRecommendation:
    def test_low_ndvi_dry_soil_advice(self):
        rec = mod.zone_recommendation({"ndvi": 0.2, "soil_moisture": 0.1})
        assert "氮" in rec or "长势偏低" in rec
        assert "灌溉" in rec

    def test_high_ndvi_wet_soil_advice(self):
        rec = mod.zone_recommendation({"ndvi": 0.7, "soil_moisture": 0.5})
        assert "减量" in rec or "良好" in rec
        assert "排水" in rec or "防涝" in rec


class TestPipeline:
    def test_synthetic_recovers_three_zones(self):
        cube, info = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.zone_management(cube, n_zones=3)
        assert res["n_zones"] == 3
        assert len(res["zones"]) == 3
        # each zone has a recommendation string
        for z in res["zones"]:
            assert isinstance(z["recommendation"], str) and len(z["recommendation"]) > 0

    def test_zones_ordered_by_vigor(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.zone_management(cube, n_zones=3)
        ndvis = sorted(z["ndvi"] for z in res["zones"])
        # three distinct vigor levels should be recovered
        assert ndvis[0] < ndvis[1] < ndvis[2]
        assert ndvis[0] < 0.4 and ndvis[2] > 0.55

    def test_too_few_dims_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.zone_management(np.zeros((10, 10), dtype=np.float32))
