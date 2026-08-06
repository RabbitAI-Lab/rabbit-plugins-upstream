"""Core algorithm tests for sar-backscatter-analysis."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as sba


class TestParsePolarization:
    def test_valid(self):
        assert sba.parse_polarization("vv,vh") == ["vv", "vh"]
        assert sba.parse_polarization(" VV ") == ["vv"]

    def test_invalid_raises(self):
        with pytest.raises(sba.UsageError):
            sba.parse_polarization("vv,xx")

    def test_empty_raises(self):
        with pytest.raises(sba.UsageError):
            sba.parse_polarization(" , ")


class TestTemporalStats:
    def test_exact_values(self):
        # 时间轴 t=[0,1,2,3]：mean=1.5, std=sqrt(1.25), amp=3, cv=std/mean
        t = np.arange(4, dtype=np.float32)
        cube = np.broadcast_to(t[:, None, None], (4, 3, 2)).astype(np.float32).copy()
        st = sba.temporal_stats(cube)
        np.testing.assert_allclose(st["mean"], 1.5, atol=1e-5)
        np.testing.assert_allclose(st["std"], np.sqrt(1.25), atol=1e-5)
        np.testing.assert_allclose(st["amplitude"], 3.0, atol=1e-5)
        np.testing.assert_allclose(st["cv"], np.sqrt(1.25) / 1.5, atol=1e-5)

    def test_constant_series_zero_var(self):
        cube = np.full((5, 4, 4), 0.08, dtype=np.float32)
        st = sba.temporal_stats(cube)
        np.testing.assert_allclose(st["std"], 0.0, atol=1e-6)
        np.testing.assert_allclose(st["amplitude"], 0.0, atol=1e-6)
        np.testing.assert_allclose(st["cv"], 0.0, atol=1e-6)

    def test_bad_ndim_raises(self):
        with pytest.raises(sba.ValidationError):
            sba.temporal_stats(np.ones((4, 4), dtype=np.float32))


class TestPolarizationRatio:
    def test_exact(self):
        vv = np.full((4, 4), 0.08, dtype=np.float32)
        vh = np.full((4, 4), 0.02, dtype=np.float32)
        ratio = sba.polarization_ratio(vv, vh)
        np.testing.assert_allclose(ratio, 4.0, atol=1e-5)

    def test_zero_vh_gives_zero(self):
        vv = np.full((4, 4), 0.08, dtype=np.float32)
        vh = np.zeros((4, 4), dtype=np.float32)
        ratio = sba.polarization_ratio(vv, vh)
        np.testing.assert_allclose(ratio, 0.0)


class TestRegionMean:
    def test_curve_length(self):
        cube = np.random.default_rng(0).uniform(0.01, 0.1, (6, 8, 8)).astype(np.float32)
        curve = sba.region_mean_timeseries(cube)
        assert len(curve) == 6
        np.testing.assert_allclose(curve[0], cube[0].mean(), atol=1e-6)


class TestBuildStatsCube:
    def test_dual_pol_band_count(self):
        cubes = {
            "vv": np.random.default_rng(1).uniform(0.02, 0.1, (6, 8, 8)).astype(np.float32),
            "vh": np.random.default_rng(2).uniform(0.005, 0.03, (6, 8, 8)).astype(np.float32),
        }
        cube, names = sba.build_stats_cube(cubes, ["vv", "vh"])
        assert cube.shape[0] == 9  # 4+4+ratio
        assert names[-1] == "vv_vh_ratio"
        assert names[0] == "vv_mean"

    def test_single_pol_band_count(self):
        cubes = {"vv": np.random.default_rng(3).uniform(0.02, 0.1, (4, 8, 8)).astype(np.float32)}
        cube, names = sba.build_stats_cube(cubes, ["vv"])
        assert cube.shape[0] == 4
        assert "vv_vh_ratio" not in names


class TestSynthetic:
    def test_shapes(self):
        cubes, info = sba.generate_synthetic([116, 39, 117, 40], n_dates=6)
        assert set(cubes.keys()) == {"vv", "vh"}
        assert cubes["vv"].shape == (6, 64, 64)
        assert len(info["dates"]) == 6

    def test_phenology_signal_present(self):
        """VV 区域均值时序应有明显季节波动（注入 season_frac=0.6 →
        全周期 amp_frac 理论值 ≈ 2×0.6 = 1.2）。"""
        cubes, info = sba.generate_synthetic([116, 39, 117, 40], n_dates=12, seed=7)
        curve = np.array(sba.region_mean_timeseries(cubes["vv"]))
        amp_frac = (curve.max() - curve.min()) / curve.mean()
        assert 0.8 < amp_frac < 1.6

    def test_vv_greater_than_vh(self):
        cubes, _ = sba.generate_synthetic([116, 39, 117, 40], n_dates=6)
        assert cubes["vv"].mean() > cubes["vh"].mean()

    def test_n_dates_too_small_raises(self):
        with pytest.raises(sba.UsageError):
            sba.generate_synthetic([116, 39, 117, 40], n_dates=1)


class TestCubeFromInput:
    def test_even_split(self):
        data = np.arange(12 * 4 * 4, dtype=np.float32).reshape(12, 4, 4)
        cubes = sba.cube_from_input(data, ["vv", "vh"])
        assert cubes["vv"].shape[0] == 6
        assert cubes["vh"].shape[0] == 6
        np.testing.assert_allclose(cubes["vv"], data[:6])
        np.testing.assert_allclose(cubes["vh"], data[6:])

    def test_uneven_falls_back_to_first_pol(self):
        data = np.ones((5, 4, 4), dtype=np.float32)
        cubes = sba.cube_from_input(data, ["vv", "vh"])
        assert set(cubes.keys()) == {"vv"}
        assert cubes["vv"].shape[0] == 5


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.default_rng(4).uniform(0.01, 0.3, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        sba.write_geotiff(path, cube, bbox, band_names=["a", "b", "c"])
        assert os.path.exists(path)
        back, rbbox = sba.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_file_raises(self):
        with pytest.raises(sba.UsageError):
            sba.read_geotiff("/nonexistent/path/file.tif")
