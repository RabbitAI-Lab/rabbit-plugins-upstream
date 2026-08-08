"""Core algorithm tests for precision-forestry-monitoring."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as pf


class TestAllometry:
    def test_analytic_solution(self):
        # V = a * DBH^b * H^c ; a=5e-5, b=2, c=1, DBH=20, H=15 -> 5e-5*400*15 = 0.3
        v = pf.allometric_volume(20.0, 15.0, a=5.0e-5, b=2.0, c=1.0)
        assert v == pytest.approx(0.3, rel=1e-9)

    def test_zero_dbh_or_height(self):
        assert pf.allometric_volume(0.0, 15.0, 5e-5, 2.0, 1.0) == 0.0
        assert pf.allometric_volume(20.0, 0.0, 5e-5, 2.0, 1.0) == 0.0

    def test_monotonic_in_dbh_and_height(self):
        v1 = pf.allometric_volume(10.0, 10.0, 6e-5, 1.9, 0.9)
        v2 = pf.allometric_volume(20.0, 10.0, 6e-5, 1.9, 0.9)
        v3 = pf.allometric_volume(20.0, 20.0, 6e-5, 1.9, 0.9)
        assert v2 > v1
        assert v3 > v2

    def test_crown_to_dbh_linear(self):
        assert pf.crown_to_dbh(4.0, k=3.0) == pytest.approx(12.0)


class TestCHM:
    def test_chm_equals_injected_difference(self):
        dtm = np.full((16, 16), 100.0, dtype=np.float32)
        dsm = dtm.copy()
        dsm[8, 8] = 122.5  # 22.5 m tree
        chm = pf.compute_chm(dsm, dtm)
        assert chm[8, 8] == pytest.approx(22.5, abs=1e-5)
        assert chm.min() >= 0.0

    def test_negative_clipped_to_zero(self):
        dtm = np.full((8, 8), 100.0, dtype=np.float32)
        dsm = dtm.copy()
        dsm[0, 0] = 95.0  # below ground
        chm = pf.compute_chm(dsm, dtm)
        assert chm[0, 0] == 0.0


class TestCanopyClosure:
    def test_bounds_01(self):
        rng = np.random.default_rng(0)
        chm = rng.uniform(0, 30, (64, 64)).astype(np.float32)
        c = pf.canopy_closure(chm, threshold=2.0)
        assert 0.0 <= c <= 1.0

    def test_full_canopy_is_one(self):
        chm = np.full((10, 10), 20.0, dtype=np.float32)
        assert pf.canopy_closure(chm, threshold=2.0) == pytest.approx(1.0)

    def test_empty_canopy_is_zero(self):
        chm = np.full((10, 10), 0.5, dtype=np.float32)
        assert pf.canopy_closure(chm, threshold=2.0) == pytest.approx(0.0)


class TestTreeDetection:
    def _gauss_tree(self, h=64, w=64, cy=32, cx=32, height=20.0, sigma=3.0):
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        return height * np.exp(-(((yy - cy) ** 2 + (xx - cx) ** 2)) / (2 * sigma ** 2))

    def test_single_peak_recovered(self):
        chm = self._gauss_tree(cy=30, cx=40, height=25.0).astype(np.float32)
        trees = pf.detect_trees(chm, min_height=5.0, footprint=5)
        assert len(trees) >= 1
        top = trees[0]
        assert abs(top["x"] - 40) <= 1
        assert abs(top["y"] - 30) <= 1
        assert top["height"] == pytest.approx(25.0, abs=0.5)

    def test_min_height_filters(self):
        chm = self._gauss_tree(height=3.0).astype(np.float32)
        assert pf.detect_trees(chm, min_height=5.0, footprint=5) == []

    def test_chm_height_matches_injected(self):
        """注入真值树高与 CHM 检测一致（核心验收点）。"""
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, info = pf.generate_synthetic_cube(bbox, seed=3)
        dsm, dtm = cube[0], cube[1]
        chm = pf.compute_chm(dsm, dtm)
        # 取注入的最高树，CHM 在该像元附近应接近注入高度
        inj = max(info["injected_trees"], key=lambda t: t["height"])
        local = chm[inj["y"] - 2:inj["y"] + 3, inj["x"] - 2:inj["x"] + 3]
        assert local.max() == pytest.approx(inj["height"], rel=0.1)


class TestCrownWidth:
    def test_gaussian_half_width(self):
        sigma = 4.0
        chm = (20.0 * np.exp(-(
            ((np.mgrid[0:64, 0:64][0] - 32) ** 2 + (np.mgrid[0:64, 0:64][1] - 32) ** 2)
        ) / (2 * sigma ** 2))).astype(np.float32)
        cw = pf.crown_width_from_chm(chm, 32, 32, pixel_size=1.0, frac=0.5)
        # 半高半径 ~ sigma*sqrt(2 ln2) ~ 4.71 -> 全宽 ~9.4，离散化允许误差
        assert 6.0 <= cw <= 14.0


class TestIndices:
    def test_ndvi_formula(self):
        nir = np.array([[0.5]], dtype=np.float32)
        red = np.array([[0.1]], dtype=np.float32)
        assert pf.ndvi(nir, red)[0, 0] == pytest.approx(0.4 / 0.6, rel=1e-6)

    def test_ndre_formula(self):
        nir = np.array([[0.6]], dtype=np.float32)
        re = np.array([[0.2]], dtype=np.float32)
        assert pf.ndre(nir, re)[0, 0] == pytest.approx(0.4 / 0.8, rel=1e-6)

    def test_ndvi_range(self):
        rng = np.random.default_rng(1)
        nir = rng.uniform(0, 1, (32, 32))
        red = rng.uniform(0, 1, (32, 32))
        out = pf.ndvi(nir, red)
        assert out.min() >= -1.0 and out.max() <= 1.0


class TestHealthGrade:
    def test_healthy_class(self):
        ndvi_arr = np.array([[0.7]], dtype=np.float32)
        ndre_arr = np.array([[0.4]], dtype=np.float32)
        assert pf.health_grade(ndvi_arr, ndre_arr, "combined")[0, 0] == 3

    def test_stressed_class(self):
        ndvi_arr = np.array([[0.2]], dtype=np.float32)
        ndre_arr = np.array([[0.05]], dtype=np.float32)
        assert pf.health_grade(ndvi_arr, ndre_arr, "combined")[0, 0] == 1

    def test_bare_is_zero(self):
        ndvi_arr = np.array([[0.05]], dtype=np.float32)
        ndre_arr = np.array([[0.0]], dtype=np.float32)
        assert pf.health_grade(ndvi_arr, ndre_arr, "combined")[0, 0] == 0


class TestSarBiomass:
    def test_monotonic_increasing(self):
        db = np.array([[-20.0, -12.0, -6.0]], dtype=np.float32)
        agb = pf.sar_biomass_t_ha(db)
        assert agb[0, 0] < agb[0, 1] < agb[0, 2]

    def test_nonnegative_and_bounded(self):
        db = np.linspace(-25, 0, 50).astype(np.float32).reshape(5, 10)
        agb = pf.sar_biomass_t_ha(db)
        assert agb.min() >= 0.0
        assert agb.max() <= 600.0


class TestStandEstimate:
    def test_end_to_end_stand(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, info = pf.generate_synthetic_cube(bbox, seed=5)
        chm = pf.compute_chm(cube[0], cube[1])
        px = pf.pixel_size_m(bbox, cube.shape[2])
        trees, summary = pf.estimate_stand(chm, pixel_size=px, min_height=5.0, footprint=5)
        assert summary["tree_count"] > 0
        assert summary["total_volume_m3"] > 0.0
        assert all(t["volume_m3"] >= 0 for t in trees)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(2).uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        pf.write_geotiff(path, cube, bbox)
        back, rb = pf.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(pf.UsageError):
            pf.read_geotiff("/nonexistent/nope.tif")
