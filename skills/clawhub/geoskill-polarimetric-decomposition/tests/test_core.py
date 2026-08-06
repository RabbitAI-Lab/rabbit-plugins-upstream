"""Core algorithm tests for polarimetric-decomposition."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


RNG = np.random.default_rng(0)


def _T_stack(T):
    """把 (3,3) 矩阵包成 (1,1,3,3) 供 cloude_pottier 使用。"""
    return T.reshape(1, 1, 3, 3)


class TestT3Encoding:
    def test_roundtrip(self):
        # 构造随机 Hermitian PSD 堆栈
        h, w = 8, 6
        A = (RNG.standard_normal((h, w, 3, 3))
             + 1j * RNG.standard_normal((h, w, 3, 3)))
        T = A + np.swapaxes(A.conj(), -1, -2)  # Hermitian
        bands = mod.T3_to_bands(T)
        assert bands.shape == (9, h, w)
        T2 = mod.bands_to_T3(bands)
        np.testing.assert_allclose(T2, T, atol=1e-5)

    def test_wrong_bands_raises(self):
        cube = np.zeros((3, 4, 4), dtype=np.float32)
        with pytest.raises(mod.ValidationError):
            mod.bands_to_T3(cube)


class TestCloudePottier:
    def test_pure_surface_low_entropy_low_alpha(self):
        # 单一散射机制：特征值 [1,0,0] → H≈0，α=设定值
        e1 = mod._scatter_vector(15.0, 30.0, 10.0)
        T = mod._make_T(e1, np.array([1.0, 0.0, 0.0]), RNG)
        res = mod.cloude_pottier(_T_stack(T))
        assert res["entropy"][0, 0] == pytest.approx(0.0, abs=1e-3)
        assert res["alpha"][0, 0] == pytest.approx(15.0, abs=1.0)

    def test_pure_double_bounce_high_alpha(self):
        e1 = mod._scatter_vector(82.0, 20.0, 90.0)
        T = mod._make_T(e1, np.array([1.0, 0.0, 0.0]), RNG)
        res = mod.cloude_pottier(_T_stack(T))
        assert res["alpha"][0, 0] == pytest.approx(82.0, abs=1.0)
        assert res["entropy"][0, 0] == pytest.approx(0.0, abs=1e-3)

    def test_identity_max_entropy(self):
        # 三个相等特征值 → H=1（最大熵）
        T = np.eye(3, dtype=np.complex128)
        res = mod.cloude_pottier(_T_stack(T))
        assert res["entropy"][0, 0] == pytest.approx(1.0, abs=1e-6)
        # 单位阵特征向量为坐标基，α = mean(0,90,90) = 60°
        assert res["alpha"][0, 0] == pytest.approx(60.0, abs=1e-3)

    def test_anisotropy_range(self):
        A = (RNG.standard_normal((16, 16, 3, 3))
             + 1j * RNG.standard_normal((16, 16, 3, 3)))
        T = A + np.swapaxes(A.conj(), -1, -2) + 4 * np.eye(3)
        res = mod.cloude_pottier(T)
        assert np.all(res["entropy"] >= -1e-6)
        assert np.all(res["entropy"] <= 1.0 + 1e-6)
        assert np.all(res["anisotropy"] >= -1e-6)
        assert np.all(res["anisotropy"] <= 1.0 + 1e-6)
        assert np.all(res["alpha"] >= -1e-3)
        assert np.all(res["alpha"] <= 90.0 + 1e-3)

    def test_bad_shape_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.cloude_pottier(np.zeros((3, 3), dtype=np.complex128))


class TestFreeman:
    def test_surface_dominated(self):
        # HH 主导 → 表面散射为主
        c11 = np.array([[1.0]]); c22 = np.array([[0.2]]); c33 = np.array([[0.02]])
        res = mod.freeman_three_component(c11, c22, c33)
        assert res["Ps"][0, 0] > res["Pd"][0, 0]
        assert res["Ps"][0, 0] > res["Pv"][0, 0]

    def test_double_bounce_dominated(self):
        # VV 远强于 HH → 二面角散射为主
        c11 = np.array([[0.4]]); c22 = np.array([[1.5]]); c33 = np.array([[0.02]])
        res = mod.freeman_three_component(c11, c22, c33)
        assert res["Pd"][0, 0] > res["Ps"][0, 0]

    def test_volume_dominated(self):
        # 交叉极化 HV 很高 → 体散射为主
        c11 = np.array([[0.6]]); c22 = np.array([[0.6]]); c33 = np.array([[0.8]])
        res = mod.freeman_three_component(c11, c22, c33)
        assert res["Pv"][0, 0] > res["Ps"][0, 0]
        assert res["Pv"][0, 0] > res["Pd"][0, 0]

    def test_energy_conservation(self):
        c11 = RNG.uniform(0.1, 1.5, (20, 20))
        c22 = RNG.uniform(0.1, 1.5, (20, 20))
        c33 = RNG.uniform(0.01, 0.6, (20, 20))
        res = mod.freeman_three_component(c11, c22, c33)
        s = res["Ps"] + res["Pd"] + res["Pv"]
        np.testing.assert_allclose(s, res["span"], rtol=1e-5)
        assert np.all(res["Ps"] >= 0)
        assert np.all(res["Pd"] >= 0)
        assert np.all(res["Pv"] >= 0)


class TestSynthetic:
    def test_synthetic_T3_shape(self):
        cube, info = mod.generate_synthetic_T3([116, 39, 117, 40], width=16, height=16, seed=1)
        assert cube.shape == (9, 16, 16)
        assert info["encoding"] == "T3-9band"

    def test_synthetic_T3_zones_separable(self):
        """合成场景左=表面、中=体、右=二面角，分解后 α 应呈 低<中<高 的排序。"""
        cube, info = mod.generate_synthetic_T3([116, 39, 117, 40], width=24, height=24, seed=3)
        T = mod.bands_to_T3(cube)
        res = mod.cloude_pottier(T)
        alpha = res["alpha"]
        surf = alpha[:, 2:6].mean()     # 左区（表面，α≈12）
        vol = alpha[:, 10:14].mean()    # 中区（体，α≈50）
        dbl = alpha[:, 18:22].mean()    # 右区（二面角，α≈82）
        assert surf < vol < dbl
        # 体散射区熵应高于表面散射区
        ent = res["entropy"]
        assert ent[:, 10:14].mean() > ent[:, 2:6].mean()

    def test_synthetic_C3_shape(self):
        cube, info = mod.generate_synthetic_C3([116, 39, 117, 40], width=16, height=16, seed=1)
        assert cube.shape == (3, 16, 16)
        assert info["encoding"] == "C3-3band"

    def test_synthetic_C3_freeman_zones(self):
        cube, info = mod.generate_synthetic_C3([116, 39, 117, 40], width=24, height=24, seed=5)
        res = mod.freeman_three_component(cube[0], cube[1], cube[2])
        # 体散射区（中）Pv 最高
        pv_vol = res["Pv"][:, 10:14].mean()
        pv_surf = res["Pv"][:, 2:6].mean()
        assert pv_vol > pv_surf
        # 二面角区（右）Pd 高于表面散射区（左）
        pd_dbl = res["Pd"][:, 18:22].mean()
        pd_surf = res["Pd"][:, 2:6].mean()
        assert pd_dbl > pd_surf


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = RNG.uniform(0, 1, (3, 16, 16)).astype(np.float32)
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
