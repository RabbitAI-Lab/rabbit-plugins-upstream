"""Core algorithm tests for fire-weather-index (Canadian FWI System)."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as fwi


def _full(h, w, val):
    return np.full((h, w), val, dtype=np.float64)


class TestFFMC:
    def test_range_0_101(self):
        ffmc_prev = _full(8, 8, 85.0)
        out = fwi.ffmc_step(ffmc_prev, _full(8, 8, 30.0), _full(8, 8, 25.0),
                            _full(8, 8, 15.0), _full(8, 8, 0.0))
        assert out.min() >= 0.0
        assert out.max() <= 101.0

    def test_dry_hot_wind_raises_ffmc(self):
        """干热大风（无降水）应抬升 FFMC。"""
        ffmc_prev = _full(8, 8, 85.0)
        out = fwi.ffmc_step(ffmc_prev, _full(8, 8, 35.0), _full(8, 8, 20.0),
                            _full(8, 8, 25.0), _full(8, 8, 0.0))
        assert np.mean(out) > 85.0

    def test_rain_lowers_ffmc(self):
        """强降水后 FFMC 应明显下降。"""
        ffmc_prev = _full(8, 8, 92.0)
        out = fwi.ffmc_step(ffmc_prev, _full(8, 8, 22.0), _full(8, 8, 90.0),
                            _full(8, 8, 8.0), _full(8, 8, 25.0))
        assert np.mean(out) < 92.0


class TestDMCDC:
    def test_dmc_accumulates_without_rain(self):
        dmc_prev = _full(8, 8, 6.0)
        out = fwi.dmc_step(dmc_prev, _full(8, 8, 30.0), _full(8, 8, 0.0), month=7)
        assert np.mean(out) > 6.0

    def test_dmc_rain_reduces(self):
        dmc_prev = _full(8, 8, 60.0)
        out = fwi.dmc_step(dmc_prev, _full(8, 8, 20.0), _full(8, 8, 30.0), month=7)
        assert np.mean(out) < 60.0

    def test_dc_nonnegative(self):
        dc_prev = _full(8, 8, 15.0)
        out = fwi.dc_step(dc_prev, _full(8, 8, 28.0), _full(8, 8, 0.0), month=7)
        assert out.min() >= 0.0
        assert np.mean(out) > 15.0


class TestISIBUIFWI:
    def test_isi_increases_with_wind(self):
        ffmc = _full(8, 8, 90.0)
        low = fwi.isi_step(ffmc, _full(8, 8, 5.0))
        high = fwi.isi_step(ffmc, _full(8, 8, 30.0))
        assert np.mean(high) > np.mean(low)

    def test_bui_nonnegative(self):
        bui = fwi.bui_step(_full(8, 8, 40.0), _full(8, 8, 200.0))
        assert bui.min() >= 0.0

    def test_bui_branch_selection(self):
        """dmc <= 0.4*dc 走 branch1，否则 branch2。"""
        b1 = fwi.bui_step(_full(4, 4, 10.0), _full(4, 4, 100.0))  # 10 <= 40
        b2 = fwi.bui_step(_full(4, 4, 80.0), _full(4, 4, 100.0))  # 80 > 40
        assert b1.min() >= 0.0 and b2.min() >= 0.0

    def test_fwi_increases_with_isi(self):
        bui = _full(8, 8, 60.0)
        low = fwi.fwi_step(_full(8, 8, 2.0), bui)
        high = fwi.fwi_step(_full(8, 8, 20.0), bui)
        assert np.mean(high) > np.mean(low)

    def test_fwi_nonnegative(self):
        f = fwi.fwi_step(_full(8, 8, 5.0), _full(8, 8, 30.0))
        assert f.min() >= 0.0


class TestClassify:
    def test_class_breaks(self):
        arr = np.array([[1.0, 7.0, 15.0, 30.0, 80.0]], dtype=np.float64)
        cls = fwi.classify_fwi(arr)
        np.testing.assert_array_equal(cls, [[1, 2, 3, 4, 5]])


class TestSeries:
    def test_series_shapes(self):
        n, H, W = 10, 8, 8
        temp = np.full((n, H, W), 30.0)
        rh = np.full((n, H, W), 25.0)
        ws = np.full((n, H, W), 18.0)
        precip = np.zeros((n, H, W))
        months = np.full(n, 7, dtype=np.int32)
        s = fwi.compute_fwi_series(temp, rh, ws, precip, months)
        assert s["FWI"].shape == (n, H, W)
        # 持续干热大风 → FWI 随时间攀升
        assert s["FWI"][-1].mean() > s["FWI"][0].mean()

    def test_shape_mismatch_raises(self):
        with pytest.raises(fwi.ValidationError):
            fwi.compute_fwi_series(np.zeros((3, 4, 4)), np.zeros((3, 4, 5)),
                                   np.zeros((3, 4, 4)), np.zeros((3, 4, 4)),
                                   np.array([7, 7, 7]))

    def test_bad_ndim_raises(self):
        with pytest.raises(fwi.ValidationError):
            fwi.compute_fwi_series(np.zeros((4, 4)), np.zeros((4, 4)),
                                   np.zeros((4, 4)), np.zeros((4, 4)),
                                   np.array([7]))


class TestSynthetic:
    def test_shapes(self):
        met = fwi.generate_synthetic_meteo([116, 39, 117, 40], n_dates=20)
        assert met["temp"].shape == (20, 64, 64)
        assert len(met["info"]["dates"]) == 20
        assert met["info"]["rain_day_index"] == 14

    def test_dry_then_rain_signal(self):
        """干热期后强降水应使域均 FFMC 回落。"""
        met = fwi.generate_synthetic_meteo([116, 39, 117, 40], n_dates=30, seed=3)
        s = fwi.compute_fwi_series(met["temp"], met["rh"], met["ws"],
                                   met["precip"], met["months"])
        rd = met["info"]["rain_day_index"]
        ffmc_before = float(np.mean(s["FFMC"][rd - 1]))
        ffmc_after = float(np.mean(s["FFMC"][rd]))
        assert ffmc_after < ffmc_before
        # 末日 FWI 应非负且处于合理量级
        assert s["FWI"][-1].mean() >= 0.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 50, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        fwi.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        back, rb = fwi.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-4)

    def test_read_missing_raises(self):
        with pytest.raises(fwi.UsageError):
            fwi.read_geotiff("/nonexistent/x.tif")
