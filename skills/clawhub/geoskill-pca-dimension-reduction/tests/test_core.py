"""Core algorithm tests for pca-dimension-reduction."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestPcaTransform:
    def test_scores_shape(self):
        cube = np.random.uniform(0, 1, (6, 32, 32)).astype(np.float32)
        res = mod.pca_transform(cube, 3)
        assert res["scores"].shape == (3, 32, 32)

    def test_pc1_largest_variance(self):
        """第一主成分方差（特征值）应最大。"""
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        res = mod.pca_transform(cube, cube.shape[0])
        ev = res["eigenvalues"]
        assert ev[0] == ev.max()
        # 降序
        assert np.all(np.diff(ev) <= 1e-9)

    def test_explained_ratio_sums_to_one(self):
        cube = np.random.uniform(0, 1, (5, 24, 24)).astype(np.float32)
        res = mod.pca_transform(cube, 5)
        np.testing.assert_allclose(res["explained_ratio"].sum(), 1.0, atol=1e-6)

    def test_synthetic_pc1_dominates(self):
        """高相关合成影像 PC1 贡献率应很高（>0.9）。"""
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        res = mod.pca_transform(cube, 3)
        assert res["explained_ratio"][0] > 0.9

    def test_loadings_orthonormal(self):
        cube = np.random.uniform(0, 1, (4, 20, 20)).astype(np.float32)
        res = mod.pca_transform(cube, 4)
        L = res["loadings"]
        np.testing.assert_allclose(L.T @ L, np.eye(4), atol=1e-6)

    def test_n_components_too_large_raises(self):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        with pytest.raises(mod.UsageError):
            mod.pca_transform(cube, 99)


class TestInversePca:
    def test_full_reconstruction_exact(self):
        """保留全部主成分时重构应几乎无损。"""
        cube = np.random.uniform(0, 1, (4, 16, 16)).astype(np.float32)
        res = mod.pca_transform(cube, 4)
        recon = mod.inverse_pca(res["scores"], res["loadings"], res["mean"], 4)
        np.testing.assert_allclose(recon, cube, atol=1e-3)

    def test_partial_reconstruction_bounded(self):
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        res = mod.pca_transform(cube, 2)
        recon = mod.inverse_pca(res["scores"], res["loadings"], res["mean"], 6)
        rmse = float(np.sqrt(np.mean((recon - cube) ** 2)))
        assert rmse < 0.2  # 前两主成分已捕获绝大部分方差


class TestSynthetic:
    def test_cube_shape(self):
        cube, info = mod.generate_synthetic_cube([116, 39, 117, 40])
        assert cube.shape == (6, 128, 128)
        assert info["n_bands"] == 6

    def test_bands_correlated(self):
        """合成影像各波段应高度相关。"""
        cube, _ = mod.generate_synthetic_cube([116, 39, 117, 40])
        flat = cube.reshape(6, -1)
        corr = np.corrcoef(flat)
        off_diag = corr[np.triu_indices(6, k=1)]
        assert off_diag.min() > 0.9


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
