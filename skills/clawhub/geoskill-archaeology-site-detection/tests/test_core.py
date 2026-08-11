"""Core algorithm tests for archaeology-site-detection."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ad


class TestNdviNormalize:
    def test_ndvi_formula(self):
        assert ad.ndvi(np.array([[0.6]]), np.array([[0.2]]))[0, 0] == pytest.approx(0.4 / 0.8)

    def test_normalize_constant_is_zero(self):
        arr = np.full((8, 8), 5.0)
        assert np.all(ad.normalize01(arr) == 0.0)

    def test_normalize_bounds(self):
        rng = np.random.default_rng(0)
        out = ad.normalize01(rng.uniform(-3, 7, (32, 32)))
        assert out.min() >= 0.0 and out.max() <= 1.0
        assert out.max() == pytest.approx(1.0)


class TestDetrend:
    def test_constant_dem_zero_relief(self):
        dem = np.full((32, 32), 100.0)
        relief = ad.detrend_relief(dem, size=9)
        assert np.allclose(relief, 0.0, atol=1e-4)

    def test_mound_positive_center(self):
        yy, xx = np.mgrid[0:48, 0:48]
        dem = (100.0 + 4.0 * np.exp(-(((yy - 24) ** 2 + (xx - 24) ** 2)) / 18.0)).astype(np.float32)
        relief = ad.detrend_relief(dem, size=15)
        assert relief[24, 24] > relief[0, 0]
        assert relief[24, 24] > 0.0


class TestSpectralSar:
    def test_cropmark_positive(self):
        red = np.full((48, 48), 0.16, dtype=np.float32)
        nir = np.full((48, 48), 0.22, dtype=np.float32)
        red[24, 24] -= 0.05
        nir[24, 24] += 0.15
        anom = ad.vegetation_anomaly(red, nir, size=11)
        assert anom[24, 24] > 0.0

    def test_sar_zscore_zero_mean(self):
        rng = np.random.default_rng(1)
        sar = rng.normal(-15, 1, (64, 64)).astype(np.float32)
        z = ad.sar_anomaly(sar)
        assert abs(float(z.mean())) < 1e-4

    def test_sar_constant_zero(self):
        assert np.all(ad.sar_anomaly(np.full((10, 10), -12.0)) == 0.0)


class TestFusion:
    def test_weighted_in_bounds(self):
        rng = np.random.default_rng(2)
        layers = [rng.uniform(0, 1, (32, 32)) for _ in range(3)]
        fused = ad.fuse_anomalies(layers, weights=[1, 1, 1], method="weighted")
        assert fused.min() >= 0.0 and fused.max() <= 1.0

    def test_max_ge_weighted(self):
        rng = np.random.default_rng(3)
        layers = [rng.uniform(0, 1, (32, 32)) for _ in range(3)]
        fw = ad.fuse_anomalies(layers, method="weighted")
        fm = ad.fuse_anomalies(layers, method="max")
        assert float(fm.mean()) >= float(fw.mean()) - 1e-6

    def test_empty_raises(self):
        with pytest.raises(ad.ValidationError):
            ad.fuse_anomalies([])


class TestClassifyDetect:
    def test_classify_levels(self):
        score = np.array([[0.1, 0.6, 0.9]], dtype=np.float32)
        lvl = ad.classify_level(score, low=0.5, high=0.75)
        assert lvl[0, 0] == 0 and lvl[0, 1] == 1 and lvl[0, 2] == 2

    def test_detect_finds_injected_peak(self):
        score = np.zeros((64, 64), dtype=np.float32)
        yy, xx = np.mgrid[0:64, 0:64]
        score = np.exp(-(((yy - 40) ** 2 + (xx - 20) ** 2)) / 20.0).astype(np.float32)
        sites = ad.detect_sites(score, threshold=0.6, footprint=7)
        assert len(sites) >= 1
        top = sites[0]
        assert abs(top["x"] - 20) <= 1 and abs(top["y"] - 40) <= 1
        assert top["level"] == 2


class TestSyntheticDetection:
    def test_recovers_injected_site(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, info = ad.generate_synthetic_cube(bbox, seed=7)
        dem, red, nir, sar = cube[0], cube[1], cube[2], cube[3]
        relief = ad.detrend_relief(dem, 15)
        veg = ad.vegetation_anomaly(red, nir, 15)
        sarz = ad.sar_anomaly(sar)
        fused = ad.fuse_anomalies([relief, veg, sarz], [0.4, 0.35, 0.25], "weighted")
        sites = ad.detect_sites(fused, threshold=0.5, footprint=7)
        assert len(sites) >= 1
        # 最近的检出点应靠近某个注入遗迹
        inj = info["injected_sites"]
        def near(st):
            return min((st["x"] - i["x"]) ** 2 + (st["y"] - i["y"]) ** 2 for i in inj)
        assert min(near(s) for s in sites) <= 25  # within 5 px


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(4).uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "a.tif")
        ad.write_geotiff(path, cube, bbox)
        back, rb = ad.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ad.UsageError):
            ad.read_geotiff("/nonexistent/x.tif")
