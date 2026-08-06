"""Core algorithm tests for spectral-unmixing."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestBuiltinEndmembers:
    def test_shape_and_names(self):
        em, names = mod.builtin_endmembers(3)
        assert em.shape == (3, 6)
        assert names == ["vegetation", "soil", "water"]

    def test_four_endmembers(self):
        em, names = mod.builtin_endmembers(4)
        assert em.shape == (4, 6)
        assert "impervious" in names

    def test_too_many_raises(self):
        with pytest.raises(mod.UsageError):
            mod.builtin_endmembers(99)


class TestUnmixPixel:
    def test_recovers_known_fractions(self):
        """无噪声混合应能精确反演丰度。"""
        em, _ = mod.builtin_endmembers(3)
        true_frac = np.array([0.6, 0.3, 0.1], dtype=np.float32)
        spectrum = true_frac @ em  # (6,)
        frac, rmse = mod.unmix_pixel(spectrum, em)
        np.testing.assert_allclose(frac, true_frac, atol=1e-3)
        assert rmse < 1e-4

    def test_abundance_sums_to_one(self):
        em, _ = mod.builtin_endmembers(3)
        rng = np.random.default_rng(0)
        spectrum = rng.uniform(0, 0.4, 6).astype(np.float32)
        frac, _ = mod.unmix_pixel(spectrum, em)
        np.testing.assert_allclose(frac.sum(), 1.0, atol=1e-5)
        assert (frac >= 0).all()


class TestUnmixCube:
    def test_output_shape(self):
        cube = np.random.uniform(0, 0.4, (6, 12, 12)).astype(np.float32)
        em, _ = mod.builtin_endmembers(3)
        abun, rmse = mod.unmix_cube(cube, em)
        assert abun.shape == (3, 12, 12)
        assert rmse.shape == (12, 12)

    def test_fractions_normalized(self):
        cube = np.random.uniform(0, 0.4, (6, 8, 8)).astype(np.float32)
        em, _ = mod.builtin_endmembers(3)
        abun, _ = mod.unmix_cube(cube, em)
        sums = abun.sum(axis=0)
        np.testing.assert_allclose(sums, 1.0, atol=1e-4)

    def test_band_mismatch_raises(self):
        cube = np.random.uniform(0, 1, (4, 8, 8)).astype(np.float32)
        em, _ = mod.builtin_endmembers(3)  # 6 bands
        with pytest.raises(mod.ValidationError):
            mod.unmix_cube(cube, em)


class TestAutoEndmembers:
    def test_extracts_requested_count(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40], n_endmembers=3)
        em, names = mod.extract_endmembers_auto(cube, 3)
        assert em.shape[0] == 3
        assert em.shape[1] == 6
        assert len(names) == 3

    def test_empty_raises(self):
        cube = np.zeros((6, 0, 0), dtype=np.float32)
        with pytest.raises(mod.ValidationError):
            mod.extract_endmembers_auto(cube, 3)


class TestSynthetic:
    def test_cube_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40], n_endmembers=3)
        assert cube.shape == (6, 96, 96)
        assert len(info["endmember_names"]) == 3

    def test_unmix_recovers_truth(self):
        """对合成影像解混，平均丰度应接近真值。"""
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40],
                                                 n_endmembers=3, seed=7)
        em, names = mod.builtin_endmembers(3)
        abun, _ = mod.unmix_cube(cube, em)
        for i, nm in enumerate(names):
            recovered = float(np.mean(abun[i]))
            truth = info["true_mean_abundance"][nm]
            assert abs(recovered - truth) < 0.05


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
