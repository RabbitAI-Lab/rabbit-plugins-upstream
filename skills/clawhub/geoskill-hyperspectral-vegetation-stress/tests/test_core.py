"""Core algorithm tests for hyperspectral-vegetation-stress."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


WL = mod.default_wavelengths(int((mod.WL_MAX - mod.WL_MIN) / mod.WL_STEP) + 1)


class TestSpectrum:
    def test_red_edge_rises(self):
        spec = mod.veg_reflectance(WL, 715.0, 0.48, 0.04)
        i_red = mod.band_index(WL, 670.0)
        i_nir = mod.band_index(WL, 840.0)
        assert spec[i_nir] > spec[i_red] + 0.2

    def test_stress_blue_shifts_rep(self):
        healthy = mod.veg_reflectance(WL, 715.0, 0.48, 0.04)
        stressed = mod.veg_reflectance(WL, 698.0, 0.28, 0.06)
        rep_h = WL[np.argmax(np.gradient(healthy, WL))]
        rep_s = WL[np.argmax(np.gradient(stressed, WL))]
        assert rep_s < rep_h


class TestIndices:
    def test_ndre_lower_for_stress(self):
        h = mod.veg_reflectance(WL, 715.0, 0.48, 0.04)
        s = mod.veg_reflectance(WL, 698.0, 0.28, 0.06)
        cube = np.stack([h, s], axis=1)[:, :, None]     # (bands,2,1)
        n = mod.ndre(cube, WL)[:, 0]
        assert n[0] > n[1]
        assert n[0] > 0.1

    def test_rep_map_recovers_position(self):
        h = mod.veg_reflectance(WL, 715.0, 0.48, 0.04)
        cube = h[:, None, None]
        rep = mod.rep_map(cube, WL)
        assert abs(rep[0, 0] - 715.0) <= 12.0

    def test_sam_zero_for_identical(self):
        ref = mod.veg_reflectance(WL, 715.0, 0.48, 0.04)
        cube = ref[:, None, None]
        ang = mod.sam_map(cube, ref)
        assert ang[0, 0] == pytest.approx(0.0, abs=1e-5)

    def test_sam_positive_for_stress(self):
        ref = mod.veg_reflectance(WL, 715.0, 0.48, 0.04)
        stressed = mod.veg_reflectance(WL, 698.0, 0.28, 0.06)
        cube = stressed[:, None, None]
        ang = mod.sam_map(cube, ref)
        assert ang[0, 0] > 0.05


class TestStress:
    def test_classify_thresholds(self):
        s = np.array([[0.0, 0.3, 0.6, 0.9]])
        cls = mod.classify_stress(s)
        assert list(cls[0]) == [0, 1, 2, 3]

    def test_red_edge_scores_stress_higher(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, wl, info = mod.generate_synthetic(bbox, seed=3)
        stress, aux = mod.stress_red_edge(cube, wl)
        c = info["stress_blob_1"]["center_rc"]
        r = info["stress_blob_1"]["radius_px"]
        inside = stress[c[0] - 2:c[0] + 2, c[1] - 2:c[1] + 2].mean()
        # 背景健康区（远离斑块）
        bg = stress[2:8, 2:8].mean()
        assert inside > bg
        assert inside > 0.5

    def test_sam_scores_stress_higher(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, wl, info = mod.generate_synthetic(bbox, seed=5)
        stress, aux = mod.stress_sam(cube, wl)
        c = info["stress_blob_1"]["center_rc"]
        inside = stress[c[0] - 2:c[0] + 2, c[1] - 2:c[1] + 2].mean()
        bg = stress[2:8, 2:8].mean()
        assert inside > bg


class TestAnomalies:
    def test_extract_overlaps_truth(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, wl, info = mod.generate_synthetic(bbox, seed=9)
        stress, _ = mod.stress_red_edge(cube, wl)
        cls = mod.classify_stress(stress)
        feats = mod.extract_anomalies(stress, cls, bbox, thresh=0.4)
        assert len(feats) >= 1
        # 最强斑块中心应落在注入的重度斑块 bbox 内
        c = info["stress_blob_1"]["center_rc"]
        h, w = stress.shape
        lon_c, lat_c = mod.pixel_to_geo(c[1], c[0], bbox, h, w)
        top = feats[0]["properties"]
        ring = feats[0]["geometry"]["coordinates"][0]
        lons = [p[0] for p in ring]
        lats = [p[1] for p in ring]
        assert min(lons) <= lon_c <= max(lons)
        assert min(lats) <= lat_c <= max(lats)

    def test_no_anomaly_on_healthy(self):
        wl = WL
        healthy = mod.veg_reflectance(wl, 715.0, 0.48, 0.04)
        cube = np.repeat(healthy[:, None, None], 16, axis=1)
        cube = np.repeat(cube, 16, axis=2)
        stress, _ = mod.stress_red_edge(cube, wl)
        cls = mod.classify_stress(stress)
        feats = mod.extract_anomalies(stress, cls, [116, 39, 117, 40], thresh=0.4)
        assert len(feats) == 0


class TestSynthetic:
    def test_shape(self):
        cube, wl, info = mod.generate_synthetic([116, 39, 117, 40])
        assert cube.ndim == 3
        assert cube.shape[0] == wl.size
        assert info["n_stress_pixels"] > 0


class TestGeoTiff:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 3, (16, 16)).astype(np.float32)
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, [116.0, 39.0, 117.0, 40.0])
        back, bb = mod.read_cube(path)
        assert back.shape == (1, 16, 16)
        np.testing.assert_allclose(bb, [116.0, 39.0, 117.0, 40.0], atol=1e-6)
