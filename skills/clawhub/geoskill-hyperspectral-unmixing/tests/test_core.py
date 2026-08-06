"""Core algorithm tests for hyperspectral-unmixing."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as hu


class TestEndmemberSpectra:
    def test_shape_range(self):
        E = hu.endmember_spectra(3, 20, seed=1)
        assert E.shape == (3, 20)
        assert E.min() >= 0.01 and E.max() <= 1.0

    def test_linear_independence(self):
        """端元峰值分离 → 光谱矩阵秩 = 端元数。"""
        E = hu.endmember_spectra(3, 20, seed=1)
        assert np.linalg.matrix_rank(E, tol=1e-2) == 3

    def test_bad_args(self):
        with pytest.raises(hu.UsageError):
            hu.endmember_spectra(0, 10)
        with pytest.raises(hu.UsageError):
            hu.endmember_spectra(2, 1)


class TestSynthetic:
    def test_shapes(self):
        cube, ab, E, info = hu.generate_synthetic([116, 39, 117, 40],
                                                  n_endmembers=3, n_bands=20)
        assert cube.shape == (20, 64, 64)
        assert ab.shape == (3, 64, 64)
        assert E.shape == (3, 20)
        # 丰度满足非负 + 和为 1
        assert ab.min() >= 0.0
        np.testing.assert_allclose(ab.sum(axis=0), 1.0, atol=1e-6)


class TestVCA:
    def test_extract_shape(self):
        cube, ab, E, _ = hu.generate_synthetic([116, 39, 117, 40],
                                               n_endmembers=3, n_bands=20, seed=3)
        data = cube.reshape(20, -1).astype(np.float64)
        ends, idx = hu.vca(data, 3, seed=1)
        assert ends.shape == (20, 3)
        assert len(idx) == 3 and len(set(idx)) == 3

    def test_invalid_p_raises(self):
        data = np.random.rand(5, 50)
        with pytest.raises(hu.UsageError):
            hu.vca(data, 0)


class TestNfindr:
    def test_extract_shape(self):
        cube, ab, E, _ = hu.generate_synthetic([116, 39, 117, 40],
                                               n_endmembers=3, n_bands=20, seed=4)
        data = cube.reshape(20, -1).astype(np.float64)
        ends, idx = hu.nfindr(data, 3, seed=1)
        assert ends.shape == (20, 3)
        assert len(set(idx)) == 3

    def test_p1(self):
        data = np.random.rand(6, 40)
        ends, idx = hu.nfindr(data, 1, seed=1)
        assert ends.shape == (6, 1) and len(idx) == 1


class TestDispatch:
    def test_unknown_method(self):
        data = np.random.rand(5, 30)
        with pytest.raises(hu.UsageError):
            hu.extract_endmembers(data, 2, method="ica")


class TestFCLSU:
    @pytest.mark.parametrize("method", ["vca", "nfindr"])
    def test_unmix_accuracy(self, method):
        """端到端：解混丰度与真值平均 MAE < 0.1。"""
        cube, truth_ab, E, _ = hu.generate_synthetic(
            [116, 39, 117, 40], n_endmembers=3, n_bands=20, seed=9, noise=0.005)
        data = cube.reshape(20, -1).astype(np.float64)
        ends, _ = hu.extract_endmembers(data, 3, method=method, seed=2)
        ab, rmse = hu.fclsu_unmix(data, ends)
        ab_map = ab.reshape(3, 64, 64)
        # 丰度非负且和为 1
        assert ab.min() >= -1e-9
        np.testing.assert_allclose(ab.sum(axis=0), 1.0, atol=1e-6)
        perm, mae = hu.match_abundances(ab_map, truth_ab)
        assert mae < 0.1, f"method={method} MAE={mae}"

    def test_abundance_constraints_exact(self):
        """已知端元 + 无噪混合 → 丰度几乎精确恢复。"""
        E = hu.endmember_spectra(3, 15, seed=5)  # (3, 15)
        rng = np.random.default_rng(0)
        A = rng.dirichlet(np.ones(3), size=50).T  # (3, 50)
        data = E.T @ A                            # (15, 50)
        ab, rmse = hu.fclsu_unmix(data, E.T)
        np.testing.assert_allclose(ab, A, atol=1e-4)
        assert rmse.max() < 1e-6


class TestMatchAbundances:
    def test_permutation_identity(self):
        ab = np.random.rand(3, 8, 8)
        perm, mae = hu.match_abundances(ab, ab)
        assert perm == [0, 1, 2]
        assert mae == 0.0

    def test_permutation_swap(self):
        rng = np.random.default_rng(1)
        ab = rng.random((3, 8, 8))
        shuffled = ab[[2, 0, 1]]
        perm, mae = hu.match_abundances(shuffled, ab)
        assert mae == 0.0
        # shuffled 的第 0 行 = ab 的第 2 行
        assert perm[0] == 2


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        hu.write_geotiff(path, cube, bbox)
        back, bb = hu.read_geotiff(path)
        assert back.shape == cube.shape
        np.testing.assert_allclose(bb, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(hu.UsageError):
            hu.read_geotiff("/nonexistent/x.tif")
