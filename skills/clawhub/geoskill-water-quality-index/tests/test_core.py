"""Core algorithm tests for water-quality-index."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestForwardAndRetrieval:
    def test_forward_shape_nonneg(self):
        chl = np.array([[1.0, 5.0], [10.0, 30.0]])
        tss = np.array([[2.0, 4.0], [6.0, 8.0]])
        rrs = mod.forward_rrs(chl, tss)
        assert rrs.shape == (4, 2, 2)
        assert np.all(rrs >= 0)

    def test_tss_inversion_exact(self):
        """红波段 Gordon 逆应精确恢复 TSS（红光吸收近似常数）。"""
        tss = np.array([[1.0, 10.0, 30.0, 60.0]])
        chl = np.full((1, 4), 5.0)
        rrs = mod.forward_rrs(chl, tss)
        red = rrs[2]
        tss_back = mod.tss_from_red(red)
        np.testing.assert_allclose(tss_back, tss, rtol=1e-3)

    def test_chl_monotonic(self):
        """蓝绿比值越低（越绿）→ 叶绿素越高。"""
        green = np.full(4, 0.02)
        blue = np.array([0.03, 0.02, 0.01, 0.005])  # 递减的蓝/绿比
        chl = mod.chl_a_oc3(blue, green)
        assert np.all(np.diff(chl) > 0)

    def test_chl_positive(self):
        chl = mod.chl_a_oc3(np.array([0.01, 0.02]), np.array([0.02, 0.02]))
        assert np.all(chl > 0)


class TestSecchi:
    def test_decreases_with_chl(self):
        chl = np.array([0.5, 5.0, 30.0])
        tss = np.full(3, 5.0)
        sd = mod.secchi_depth(chl, tss)
        assert np.all(np.diff(sd) < 0)

    def test_decreases_with_tss(self):
        chl = np.full(3, 5.0)
        tss = np.array([1.0, 20.0, 60.0])
        sd = mod.secchi_depth(chl, tss)
        assert np.all(np.diff(sd) < 0)

    def test_positive(self):
        sd = mod.secchi_depth(np.array([1.0, 50.0]), np.array([1.0, 100.0]))
        assert np.all(sd > 0)


class TestNDWI:
    def test_water_higher_than_land(self):
        green = np.array([0.05, 0.09])
        nir = np.array([0.005, 0.45])  # 水：低 NIR；陆：高 NIR
        nd = mod.ndwi(green, nir)
        assert nd[0] > 0      # 水体 NDWI > 0
        assert nd[1] < 0      # 陆地 NDWI < 0

    def test_water_mask(self):
        green = np.array([[0.05, 0.09]])
        nir = np.array([[0.005, 0.45]])
        mask = mod.water_mask(mod.ndwi(green, nir), threshold=0.0)
        assert mask[0, 0] == True
        assert mask[0, 1] == False


class TestTrophic:
    def test_thresholds(self):
        chl = np.array([1.0, 3.0, 10.0, 30.0])
        cls = mod.trophic_class(chl)
        np.testing.assert_array_equal(cls, [0, 1, 2, 3])

    def test_names_length(self):
        assert len(mod.TROPHIC_NAMES) == 4
        assert len(mod.TROPHIC_CN) == 4


class TestParseParameters:
    def test_valid(self):
        assert mod.parse_parameters("chl_a,tss,secchi") == ["chl_a", "tss", "secchi"]

    def test_dedup(self):
        assert mod.parse_parameters("chl_a,chl_a,tss") == ["chl_a", "tss"]

    def test_invalid_raises(self):
        with pytest.raises(mod.UsageError):
            mod.parse_parameters("chl_a,bogus")

    def test_empty_raises(self):
        with pytest.raises(mod.UsageError):
            mod.parse_parameters("  ,  ")


class TestSyntheticAndIO:
    def test_shapes_and_land(self):
        info = mod.generate_synthetic([116, 39, 117, 40], grid_shape=(32, 32))
        assert info["rrs"].shape == (4, 32, 32)
        assert info["chl_truth"].shape == (32, 32)
        assert np.any(info["land_mask"])   # 有陆地块
        assert np.any(~info["land_mask"])  # 也有水体

    def test_retrieval_correlates_truth(self):
        """合成反演：chl / tss 与注入真值高相关。"""
        info = mod.generate_synthetic([116, 39, 117, 40], grid_shape=(48, 48), seed=7)
        rrs = info["rrs"]
        nd = mod.ndwi(rrs[1], rrs[3])
        wmask = mod.water_mask(nd, 0.0) & (~info["land_mask"])
        assert np.count_nonzero(wmask) > 100
        chl = mod.chl_a_oc3(rrs[0], rrs[1])[wmask]
        tss = mod.tss_from_red(rrs[2])[wmask]
        corr_chl = np.corrcoef(chl, info["chl_truth"][wmask])[0, 1]
        corr_tss = np.corrcoef(tss, info["tss_truth"][wmask])[0, 1]
        assert corr_chl > 0.7
        assert corr_tss > 0.9

    def test_geotiff_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (4, 12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back, arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
