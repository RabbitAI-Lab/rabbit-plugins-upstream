"""Core algorithm tests for crop-health-diagnosis — verify physical correctness."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestIndices:
    def test_ndvi_known_value(self):
        # NIR=0.5, Red=0.1 -> (0.5-0.1)/(0.5+0.1)=0.6667
        red = np.array([[0.1]], dtype=np.float32)
        nir = np.array([[0.5]], dtype=np.float32)
        ndvi = mod.compute_ndvi(red, nir)
        assert ndvi[0, 0] == pytest.approx(0.6667, abs=1e-3)

    def test_ndvi_range(self):
        rng = np.random.default_rng(0)
        red = rng.uniform(0, 0.4, (32, 32)).astype(np.float32)
        nir = rng.uniform(0, 0.6, (32, 32)).astype(np.float32)
        ndvi = mod.compute_ndvi(red, nir)
        assert ndvi.min() >= -1.0 and ndvi.max() <= 1.0

    def test_ndvi_bare_soil_low_veg_high(self):
        # vegetation has higher NIR reflectance -> higher NDVI than bare soil
        veg = mod.compute_ndvi(np.array([[0.05]]), np.array([[0.5]]))
        soil = mod.compute_ndvi(np.array([[0.2]]), np.array([[0.25]]))
        assert veg[0, 0] > soil[0, 0]

    def test_ndre_known_value(self):
        rededge = np.array([[0.1]], dtype=np.float32)
        nir = np.array([[0.5]], dtype=np.float32)
        ndre = mod.compute_ndre(rededge, nir)
        assert ndre[0, 0] == pytest.approx(0.6667, abs=1e-3)

    def test_safe_ratio_zero_denominator(self):
        red = np.array([[0.0]], dtype=np.float32)
        nir = np.array([[0.0]], dtype=np.float32)
        ndvi = mod.compute_ndvi(red, nir)
        assert np.isfinite(ndvi).all()
        assert ndvi[0, 0] == 0.0


class TestHealthScore:
    def test_range_01(self):
        rng = np.random.default_rng(1)
        ndvi = rng.uniform(-0.2, 0.9, (16, 16)).astype(np.float32)
        ndre = rng.uniform(-0.2, 0.6, (16, 16)).astype(np.float32)
        lst = rng.uniform(293, 323, (16, 16)).astype(np.float32)
        score = mod.health_score(ndvi, ndre, lst)
        assert score.min() >= 0.0 and score.max() <= 1.0

    def test_healthy_beats_stressed(self):
        # healthy: high NDVI/NDRE, low LST; stressed: opposite
        h = mod.health_score(np.array([[0.8]]), np.array([[0.5]]), np.array([[296.0]]))
        s = mod.health_score(np.array([[0.05]]), np.array([[0.0]]), np.array([[320.0]]))
        assert h[0, 0] > s[0, 0]

    def test_lst_increases_lower_score(self):
        # same vegetation, hotter canopy -> lower health (transpiration limited)
        cool = mod.health_score(np.array([[0.6]]), np.array([[0.4]]), np.array([[298.0]]))
        hot = mod.health_score(np.array([[0.6]]), np.array([[0.4]]), np.array([[320.0]]))
        assert cool[0, 0] > hot[0, 0]


class TestAnomaly:
    def test_below_history_negative_z(self):
        cur = np.array([[0.3]], dtype=np.float32)
        mu = np.array([[0.6]], dtype=np.float32)
        sd = np.array([[0.1]], dtype=np.float32)
        z = mod.anomaly_zscore(cur, mu, sd)
        assert z[0, 0] < 0  # worse than history

    def test_above_history_positive_z(self):
        cur = np.array([[0.7]], dtype=np.float32)
        mu = np.array([[0.5]], dtype=np.float32)
        sd = np.array([[0.1]], dtype=np.float32)
        z = mod.anomaly_zscore(cur, mu, sd)
        assert z[0, 0] == pytest.approx(2.0, abs=1e-3)

    def test_zero_std_guard(self):
        cur = np.array([[0.5]], dtype=np.float32)
        mu = np.array([[0.5]], dtype=np.float32)
        sd = np.array([[0.0]], dtype=np.float32)
        z = mod.anomaly_zscore(cur, mu, sd)
        assert np.isfinite(z).all()


class TestClustering:
    def test_recovers_two_clusters(self):
        # two well-separated feature groups
        a = np.zeros((10, 10, 2), dtype=np.float32)
        b = np.ones((10, 10, 2), dtype=np.float32)
        feats = np.concatenate([a, b], axis=0)  # (20,10,2)
        labels = mod.spatial_cluster(feats, n_clusters=2)
        assert labels.shape == (20, 10)
        # top half and bottom half should get distinct labels
        assert len(np.unique(labels[:10])) == 1
        assert len(np.unique(labels[10:])) == 1
        assert labels[0, 0] != labels[19, 0]

    def test_cluster_count_capped(self):
        feats = np.zeros((8, 8, 2), dtype=np.float32)  # only 1 unique row
        labels = mod.spatial_cluster(feats, n_clusters=5)
        assert labels.max() + 1 <= 5


class TestClassifyHealth:
    def test_level_thresholds(self):
        score = np.array([[0.1, 0.5, 0.7, 0.9]], dtype=np.float32)
        lvl = mod.classify_health(score)
        assert lvl[0, 0] == 0  # poor
        assert lvl[0, 1] == 1  # sub
        assert lvl[0, 2] == 2  # moderate
        assert lvl[0, 3] == 3  # healthy


class TestDiagnosePipeline:
    def _cube(self):
        cube, packed = mod.generate_synthetic([116, 39, 117, 40])
        return cube, packed

    def test_diagnose_outputs(self):
        cube, packed = self._cube()
        res = mod.diagnose(cube, packed["aux"]["hist_mean"], packed["aux"]["hist_std"], n_clusters=3)
        h, w = cube.shape[1:]
        assert res["health"].shape == (h, w)
        assert res["health"].min() >= 0.0 and res["health"].max() <= 1.0
        assert res["level"].max() <= 3
        assert res["cluster"].shape == (h, w)
        assert np.isfinite(res["anomaly"]).all()

    def test_too_few_bands_raises(self):
        cube = np.random.uniform(0, 1, (2, 8, 8)).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.diagnose(cube)

    def test_synthetic_healthy_region_scores_higher(self):
        cube, packed = self._cube()
        res = mod.diagnose(cube, packed["aux"]["hist_mean"], packed["aux"]["hist_std"])
        health = res["health"]
        # top-left (healthy) vs bottom-right (stressed) corner blocks
        h, w = health.shape
        healthy_corner = health[:int(h * 0.3), :int(w * 0.3)].mean()
        stressed_corner = health[int(h * 0.7):, int(w * 0.7):].mean()
        assert healthy_corner > stressed_corner


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (2, 12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, cube, bbox)
        back, bb = mod.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/none.tif")
