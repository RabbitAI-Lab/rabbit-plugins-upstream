"""Core algorithm tests for band-ratio-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _fake_bands(h=16, w=16):
    """构造一组已知反射率波段（植被特征：NIR 高、Red 低）。"""
    return {
        "blue":  np.full((h, w), 0.05, dtype=np.float32),
        "green": np.full((h, w), 0.10, dtype=np.float32),
        "red":   np.full((h, w), 0.05, dtype=np.float32),
        "nir":   np.full((h, w), 0.50, dtype=np.float32),
        "swir1": np.full((h, w), 0.20, dtype=np.float32),
        "swir2": np.full((h, w), 0.10, dtype=np.float32),
    }


class TestIndexFormulas:
    def test_ndvi_value(self):
        b = _fake_bands()
        ndvi = mod.compute_index("ndvi", b)
        # (0.5-0.05)/(0.5+0.05) = 0.818
        np.testing.assert_allclose(ndvi, 0.818, atol=0.01)

    def test_ndwi_value(self):
        b = _fake_bands()
        ndwi = mod.compute_index("ndwi", b)
        # (0.10-0.50)/(0.10+0.50) = -0.667
        np.testing.assert_allclose(ndwi, -0.667, atol=0.01)

    def test_mndwi_value(self):
        b = _fake_bands()
        mndwi = mod.compute_index("mndwi", b)
        # (0.10-0.20)/(0.10+0.20) = -0.333
        np.testing.assert_allclose(mndwi, -0.333, atol=0.01)

    def test_ndbi_value(self):
        b = _fake_bands()
        ndbi = mod.compute_index("ndbi", b)
        # (0.20-0.50)/(0.20+0.50) = -0.4286
        np.testing.assert_allclose(ndbi, -0.4286, atol=0.01)

    def test_savi_value(self):
        b = _fake_bands()
        savi = mod.compute_index("savi", b)
        # 1.5*(0.5-0.05)/(0.5+0.05+0.5) = 1.5*0.45/1.05 = 0.643
        np.testing.assert_allclose(savi, 0.643, atol=0.01)

    def test_evi_positive_for_vegetation(self):
        b = _fake_bands()
        evi = mod.compute_index("evi", b)
        assert float(np.mean(evi)) > 0


class TestSafeDivision:
    def test_zero_denominator(self):
        num = np.array([1.0, 2.0], dtype=np.float32)
        den = np.array([0.0, 4.0], dtype=np.float32)
        out = mod._safe_ratio(num, den)
        assert out[0] == 0.0
        np.testing.assert_allclose(out[1], 0.5, atol=1e-6)


class TestComputeIndexErrors:
    def test_unknown_index_raises(self):
        with pytest.raises(mod.UsageError):
            mod.compute_index("bogus", _fake_bands())

    def test_missing_band_raises(self):
        b = {"nir": np.zeros((4, 4), dtype=np.float32)}  # 缺 red
        with pytest.raises(mod.ValidationError):
            mod.compute_index("ndvi", b)


class TestIndexStats:
    def test_stats_range(self):
        arr = np.array([0.0, 0.5, 1.0], dtype=np.float32)
        st = mod.index_stats(arr)
        assert st["min"] == 0.0
        assert st["max"] == 1.0
        assert 0.49 < st["mean"] < 0.51

    def test_stats_empty(self):
        arr = np.full((4, 4), np.nan, dtype=np.float32)
        st = mod.index_stats(arr)
        assert st["n_valid"] == 0


class TestSynthetic:
    def test_cube_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert cube.shape == (6, 128, 128)
        assert set(info["band_names"]) == set(mod.BAND_INDEX.keys())

    def test_cube_range(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert cube.min() >= 0.0
        assert cube.max() <= 1.0

    def test_vegetation_high_nir(self):
        """合成影像中 NIR 波段均值应高于 Red（含植被像元）。"""
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert float(np.mean(cube[3])) > float(np.mean(cube[2]))

    def test_indices_on_synthetic(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        bands = mod.cube_to_bands(cube, list(mod.BAND_INDEX.keys()))
        ndvi = mod.compute_index("ndvi", bands)
        assert ndvi.shape == (128, 128)
        # 植被区 NDVI 应为正
        assert float(np.max(ndvi)) > 0.5


class TestGeoTiffIO:
    def test_write_read_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        back, rbbox = mod.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/path/file.tif")
