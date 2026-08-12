"""Core algorithm tests for sediment-transport-modeling."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as st


class TestSlope:
    def test_flat_dem_zero_slope(self):
        dem = np.full((32, 32), 100.0)
        slope = st.compute_slope_rad(dem, cellsize=10.0)
        assert np.allclose(slope, 0.0, atol=1e-6)

    def test_tilted_plane_constant_slope(self):
        # 沿 y 方向每像元升高 10 m，cellsize 10 m → tan(slope)=1 → 45°
        dem = np.tile(np.arange(32, dtype=float) * 10.0, (32, 1))
        slope = st.compute_slope_rad(dem, cellsize=10.0)
        interior = slope[2:-2, 2:-2]
        assert np.allclose(interior, np.pi / 4, atol=0.05)


class TestD8Flow:
    def test_accumulation_increases_downstream(self):
        # 平面向 col 31（低处）倾斜：水流沿列方向，越靠下游累积越大
        dem = np.tile(np.arange(32, dtype=float)[::-1], (32, 1))  # col0 高, col31 低
        acc, down = st.d8_flow_accumulation(dem, cellsize=1.0)
        assert acc.min() >= 1.0
        # 最下游一列（低处）累积应大于最上游一列
        assert acc[:, -1].mean() > acc[:, 0].mean()

    def test_single_pit_collects_all(self):
        # 漏斗状 DEM，中心最低 → 中心 2×2 洼地汇集几乎全部像元
        yy, xx = np.mgrid[0:16, 0:16]
        dem = ((xx - 7.5) ** 2 + (yy - 7.5) ** 2).astype(float)
        acc, down = st.d8_flow_accumulation(dem, cellsize=1.0)
        # D8 单流向把漏斗分成 4 个象限，分别汇入中心 4 个像元
        center_sum = acc[7:9, 7:9].sum()
        assert center_sum > 0.8 * acc.size


class TestLSFactors:
    def test_S_increases_with_slope(self):
        flat = st.slope_steepness_factor(np.array([0.0]))
        steep = st.slope_steepness_factor(np.deg2rad([20.0]))
        assert steep[0] > flat[0]
        assert flat[0] >= 0.0

    def test_L_increases_with_accumulation(self):
        slope = np.full(5, np.deg2rad(10.0))
        acc = np.array([1.0, 5.0, 20.0, 100.0, 500.0])
        L = st.slope_length_factor(acc, slope, cellsize=10.0)
        assert np.all(np.diff(L) > 0)  # 单调递增


class TestCoverFactor:
    def test_bare_higher_than_vegetated(self):
        ndvi = np.array([0.0, 0.3, 0.7, 0.9])
        C = st.cover_factor(ndvi)
        assert C[0] > C[1] > C[2] > C[3]

    def test_range_bounded(self):
        ndvi = np.linspace(-0.2, 1.0, 50)
        C = st.cover_factor(ndvi)
        assert C.min() >= 0.001
        assert C.max() <= 1.0


class TestRusle:
    def test_steep_more_erosion_than_flat(self):
        R = np.full((16, 16), 200.0)
        K = np.full((16, 16), 0.3)
        C = np.full((16, 16), 0.5)
        S_flat = np.full((16, 16), 0.5)
        S_steep = np.full((16, 16), 3.0)
        L = np.ones((16, 16))
        A_flat = st.rusle(R, K, L, S_flat, C)
        A_steep = st.rusle(R, K, L, S_steep, C)
        assert A_steep.mean() > A_flat.mean()

    def test_bare_more_erosion_than_vegetated(self):
        R = np.full((8, 8), 200.0); K = np.full((8, 8), 0.3)
        L = np.ones((8, 8)); S = np.ones((8, 8))
        A_bare = st.rusle(R, K, L, S, np.full((8, 8), 0.9))
        A_veg = st.rusle(R, K, L, S, np.full((8, 8), 0.1))
        assert A_bare.mean() > A_veg.mean()

    def test_non_negative(self):
        A = st.rusle(np.ones((4, 4)) * 100, np.ones((4, 4)) * 0.3,
                     np.ones((4, 4)), np.ones((4, 4)), np.ones((4, 4)))
        assert A.min() >= 0.0


class TestSDR:
    def test_decreases_with_area(self):
        s_small = st.sediment_delivery_ratio(1.0)
        s_large = st.sediment_delivery_ratio(1000.0)
        assert s_small > s_large

    def test_bounded(self):
        for a in [0.001, 1, 100, 10000]:
            assert 0.05 <= st.sediment_delivery_ratio(a) <= 0.9


class TestSedimentYield:
    def test_yield_is_fraction_of_erosion(self):
        A = np.full((10, 10), 100.0)  # 100 t/ha/yr
        res = st.sediment_yield(A, cell_area_m2=10000.0, sdr=0.3)
        # 100 cells × 1 ha × 100 t/ha = 10000 t/yr 总侵蚀
        assert res["total_erosion_t_per_yr"] == pytest.approx(10000.0)
        assert res["sediment_yield_t_per_yr"] == pytest.approx(3000.0)
        assert res["area_ha"] == pytest.approx(100.0)


class TestKeySources:
    def test_top_n_highest(self):
        A = np.arange(100, dtype=float).reshape(10, 10)
        bbox = [110.0, 35.0, 111.0, 36.0]
        sources = st.key_source_areas(A, bbox, top_n=5)
        assert len(sources) == 5
        vals = [s["erosion_modulus_t_ha_yr"] for s in sources]
        assert vals == sorted(vals, reverse=True)
        assert vals[0] == 99.0  # 最大值


class TestEndToEndSynthetic:
    def test_full_pipeline_reasonable(self):
        layers, info = st.generate_synthetic([110, 35, 111, 36], width=48, height=48)
        A, summary = st.run_model(
            layers["dem"], layers["R"], layers["K"], layers["ndvi"],
            info["cellsize_m"], [110, 35, 111, 36],
        )
        assert A.shape == (48, 48)
        assert A.min() >= 0.0
        # 量级合理：黄土丘陵侵蚀模数一般在 0 - 数万 t/ha/yr
        assert 0.0 < summary["yield"]["mean_erosion_modulus_t_ha_yr"] < 1e5
        assert summary["yield"]["sediment_yield_t_per_yr"] > 0
        assert len(summary["key_source_areas"]) > 0

    def test_synthetic_shape(self):
        layers, info = st.generate_synthetic([110, 35, 111, 36], width=64, height=64)
        assert layers["dem"].shape == (64, 64)
        assert "cellsize_m" in info
        assert info["cellsize_m"] > 0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 100, (16, 16)).astype(np.float32)
        bbox = [110.0, 35.0, 111.0, 36.0]
        path = str(tmp_path / "a.tif")
        st.write_geotiff(path, arr, bbox)
        assert os.path.exists(path)
        back, rbbox, cs = st.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-4)
        assert cs > 0

    def test_read_missing_raises(self):
        with pytest.raises(st.UsageError):
            st.read_geotiff("/nonexistent/x.tif")
