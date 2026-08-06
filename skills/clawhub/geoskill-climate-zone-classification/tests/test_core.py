"""Core algorithm tests for climate-zone-classification."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _cos_temp(base, amp):
    """北半球月均温：7 月(idx6)最热。"""
    months = np.arange(12)
    return base + amp * np.cos(2.0 * np.pi * (months - 6.0) / 12.0)


class TestKoppenSingle:
    def test_af_tropical_rainforest(self):
        t = np.full(12, 27.0)
        p = np.full(12, 100.0)
        code, label = mod.koppen_single(t, p)
        assert label == "Af"
        assert code == 1

    def test_am_tropical_monsoon(self):
        t = np.full(12, 27.0)
        p = np.array([20.0] + [180.0] * 11)  # psum=2000, pmin=20, am_thresh=20
        code, label = mod.koppen_single(t, p)
        assert label == "Am"

    def test_aw_tropical_savanna(self):
        t = np.full(12, 27.0)
        p = mod._monthly_precip(1400.0, "summer")
        code, label = mod.koppen_single(t, p)
        assert label == "Aw"

    def test_bwh_hot_desert(self):
        t = _cos_temp(25.0, 9.0)
        p = np.full(12, 10.0)  # psum=120, very dry
        code, label = mod.koppen_single(t, p)
        assert label == "BWh"

    def test_cfa_humid_subtropical(self):
        t = _cos_temp(17.0, 9.0)  # tmin=8, tmax=26
        p = mod._monthly_precip(1100.0, "uniform")
        code, label = mod.koppen_single(t, p)
        assert label == "Cfa"

    def test_dfb_warm_summer_continental(self):
        t = _cos_temp(6.0, 14.0)  # tmin=-8, tmax=20
        p = mod._monthly_precip(600.0, "uniform")
        code, label = mod.koppen_single(t, p)
        assert label == "Dfb"

    def test_et_tundra(self):
        t = _cos_temp(-2.0, 4.0)  # tmax=2, tmin=-6
        p = mod._monthly_precip(250.0, "uniform")
        code, label = mod.koppen_single(t, p)
        assert label == "ET"

    def test_ef_ice_cap(self):
        t = np.full(12, -10.0)  # tmax=-10 < 0
        p = np.full(12, 5.0)
        code, label = mod.koppen_single(t, p)
        assert label == "EF"

    def test_csb_dry_summer(self):
        """地中海型：夏干冬雨，凉夏。"""
        t = _cos_temp(15.0, 6.0)  # tmin=9, tmax=21 (<22 → b)
        p = mod._monthly_precip(600.0, "winter")  # 冬雨型
        code, label = mod.koppen_single(t, p)
        assert label in ("Csb", "Csa", "Cfb")  # 夏干应判 s
        assert label.startswith("Cs")

    def test_wrong_length_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.koppen_single(np.full(6, 20.0), np.full(12, 100.0))


class TestKoppenClassifyGrid:
    def test_output_shape(self):
        temp = np.random.default_rng(0).uniform(-5, 30, (12, 16, 16))
        precip = np.random.default_rng(1).uniform(0, 200, (12, 16, 16))
        codes = mod.koppen_classify(temp, precip)
        assert codes.shape == (16, 16)
        assert codes.dtype == np.int32

    def test_two_pixel_grid(self):
        """一个 Af 像元 + 一个 EF 像元。"""
        temp = np.zeros((12, 1, 2), dtype=np.float64)
        precip = np.zeros((12, 1, 2), dtype=np.float64)
        temp[:, 0, 0] = 27.0
        precip[:, 0, 0] = 100.0
        temp[:, 0, 1] = -10.0
        precip[:, 0, 1] = 5.0
        codes = mod.koppen_classify(temp, precip)
        assert codes[0, 0] == mod.koppen_single(np.full(12, 27.0), np.full(12, 100.0))[0]
        assert codes[0, 1] == mod.koppen_single(np.full(12, -10.0), np.full(12, 5.0))[0]

    def test_wrong_bands_raises(self):
        temp = np.zeros((6, 4, 4))
        precip = np.zeros((12, 4, 4))
        with pytest.raises(mod.ValidationError):
            mod.koppen_classify(temp, precip)


class TestStrahlerClassify:
    def test_output_shape_and_range(self):
        temp = np.random.default_rng(2).uniform(-5, 30, (12, 16, 16))
        precip = np.random.default_rng(3).uniform(0, 200, (12, 16, 16))
        codes = mod.strahler_classify(temp, precip)
        assert codes.shape == (16, 16)
        assert codes.min() >= 0
        assert codes.max() <= 10

    def test_tropical_wet(self):
        t = np.full(12, 27.0)
        p = np.full(12, 150.0)  # psum=1800 >= 1000
        codes = mod.strahler_classify(t[:, None, None], p[:, None, None])
        assert codes[0, 0] == 1  # tropical-wet

    def test_polar_ice(self):
        t = np.full(12, -15.0)
        p = np.full(12, 5.0)
        codes = mod.strahler_classify(t[:, None, None], p[:, None, None])
        assert codes[0, 0] == 10  # polar-ice


class TestDispatch:
    def test_koppen_dispatch(self):
        temp = np.full((12, 4, 4), 27.0)
        precip = np.full((12, 4, 4), 100.0)
        codes = mod.classify_climate(temp, precip, method="koppen")
        assert codes.shape == (4, 4)

    def test_strahler_dispatch(self):
        temp = np.full((12, 4, 4), 27.0)
        precip = np.full((12, 4, 4), 100.0)
        codes = mod.classify_climate(temp, precip, method="strahler")
        assert codes.shape == (4, 4)

    def test_unknown_method_raises(self):
        temp = np.full((12, 2, 2), 27.0)
        precip = np.full((12, 2, 2), 100.0)
        with pytest.raises(mod.UsageError):
            mod.classify_climate(temp, precip, method="foo")


class TestAreaStatistics:
    def test_fractions_sum_to_one(self):
        codes = np.array([[1, 1, 2], [2, 3, 3]], dtype=np.int32)
        stats = mod.area_statistics(codes, [116.0, 39.0, 117.0, 40.0], method="koppen")
        total_frac = sum(c["fraction"] for c in stats["classes"])
        assert abs(total_frac - 1.0) < 1e-9
        assert stats["total_pixels"] == 6

    def test_area_positive(self):
        codes = np.ones((10, 10), dtype=np.int32)
        stats = mod.area_statistics(codes, [116.0, 39.0, 117.0, 40.0], method="koppen")
        assert stats["classes"][0]["area_km2"] > 0


class TestClimateChange:
    def test_no_change(self):
        a = np.ones((8, 8), dtype=np.int32)
        b = np.ones((8, 8), dtype=np.int32)
        ch = mod.climate_change(a, b)
        assert ch["changed_pixels"] == 0
        assert ch["changed_fraction"] == 0.0

    def test_partial_change(self):
        a = np.ones((4, 4), dtype=np.int32)
        b = np.ones((4, 4), dtype=np.int32)
        b[0, 0] = 5
        b[1, 1] = 7
        ch = mod.climate_change(a, b)
        assert ch["changed_pixels"] == 2
        assert abs(ch["changed_fraction"] - 2 / 16) < 1e-9

    def test_shape_mismatch_raises(self):
        a = np.ones((4, 4), dtype=np.int32)
        b = np.ones((3, 3), dtype=np.int32)
        with pytest.raises(mod.ValidationError):
            mod.climate_change(a, b)


class TestSynthetic:
    def test_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert cube.ndim == 3
        assert cube.shape[0] == 24
        assert cube.shape[1] == 64
        assert cube.shape[2] == 64

    def test_koppen_band_recovery(self):
        """合成数据各气候带中心应恢复预期柯本类型。"""
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], seed=42)
        codes = mod.koppen_classify(cube[0:12], cube[12:24])
        for name, c in info["band_centers"].items():
            got = mod.KOPPEN_CODES[int(codes[c["row"], c["col"]])]
            assert got == name, f"band {name}: got {got} at {c}"


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(4).uniform(0, 30, (24, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        read_back, read_bbox = mod.read_geotiff(path)
        assert read_back.shape == cube.shape
        np.testing.assert_allclose(read_bbox, bbox, atol=1e-6)
        np.testing.assert_allclose(read_back, cube, atol=1e-5)

    def test_read_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/path/file.tif")
