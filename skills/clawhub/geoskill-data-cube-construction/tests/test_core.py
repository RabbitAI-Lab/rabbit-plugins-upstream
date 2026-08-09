"""Core algorithm tests for data-cube-construction."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestSyntheticCube:
    def test_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=6, bands=4)
        assert cube.ndim == 4
        assert cube.shape[0] == 6
        assert cube.shape[1] == 4
        assert len(info["dates"]) == 6
        assert len(info["band_names"]) == 4

    def test_value_range(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert cube.min() >= 0.0
        assert cube.max() <= 1.0

    def test_temporal_variation_in_nir(self):
        """NIR（波段 3）应随物候有时间变化。"""
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=8, bands=4)
        nir_means = [float(np.mean(cube[t, 3])) for t in range(8)]
        assert max(nir_means) - min(nir_means) > 0.01

    def test_invalid_n_dates_raises(self):
        with pytest.raises(mod.UsageError):
            mod.generate_synthetic_cube([116, 39, 117, 40], n_dates=0)


class TestBuildDataArray:
    def test_dims_and_coords(self):
        xr = pytest.importorskip("xarray")
        cube = np.random.rand(3, 2, 8, 8).astype(np.float32)
        dates = ["2023-01-01", "2023-01-17", "2023-02-02"]
        bands = ["blue", "green"]
        da = mod.build_data_array(cube, [116, 39, 117, 40], dates, bands)
        assert da.dims == ("time", "band", "y", "x")
        assert list(da.coords["band"].values) == bands
        assert da.shape == cube.shape
        assert da.attrs["crs"] == "EPSG:4326"

    def test_ndim_mismatch_raises(self):
        cube = np.random.rand(3, 8, 8).astype(np.float32)  # 3D
        with pytest.raises(mod.ValidationError):
            mod.build_data_array(cube, [116, 39, 117, 40], ["d"], ["b"])

    def test_date_length_mismatch_raises(self):
        cube = np.random.rand(3, 2, 8, 8).astype(np.float32)
        with pytest.raises(mod.ValidationError):
            mod.build_data_array(cube, [116, 39, 117, 40], ["only-one"], ["b1", "b2"])


class TestStatistics:
    def test_stats_keys(self):
        cube = np.random.rand(4, 3, 10, 10).astype(np.float32)
        stats = mod.cube_statistics(cube)
        assert "global_mean" in stats
        assert len(stats["per_time"]) == 4
        assert len(stats["per_band"]) == 3


class TestNetCDFRoundtrip:
    def test_write_and_read(self, tmp_path):
        cube = np.random.rand(3, 2, 8, 8).astype(np.float32)
        dates = ["2023-01-01", "2023-01-17", "2023-02-02"]
        bands = ["blue", "green"]
        da = mod.build_data_array(cube, [116, 39, 117, 40], dates, bands)
        path = str(tmp_path / "cube.nc")
        mod.write_netcdf(da, path)
        assert os.path.exists(path)
        back, meta = mod.read_netcdf(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_netcdf("/nonexistent/cube.nc")
