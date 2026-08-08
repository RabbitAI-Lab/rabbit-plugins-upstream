"""Core algorithm tests for lidar-coastal-erosion."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestTerrain:
    def test_land_sea_sign(self):
        # 小 x 陆地(正高程)，大 x 海(负高程)
        x = np.array([100.0, 5000.0])
        y = np.array([1000.0, 1000.0])
        z = mod.terrain_elevation(x, y, x_c0=3000.0, width_m=6000.0,
                                  height_m=2000.0, amp_frac=0.0)
        assert z[0] > 0
        assert z[1] < 0

    def test_zero_at_coastline(self):
        z = mod.terrain_elevation(np.array([3000.0]), np.array([1000.0]),
                                  x_c0=3000.0, width_m=6000.0,
                                  height_m=2000.0, amp_frac=0.0)
        assert abs(z[0]) < 1e-6


class TestCoastlineExtraction:
    def test_recovers_position(self):
        # 构造一个解析 DSM，海岸线在 x=3000
        xs = np.linspace(0, 6000, 120)
        ys = np.linspace(2000, 0, 40)
        XX, YY = np.meshgrid(xs, ys)
        dsm = (-12.0 * np.tanh((XX - 3000.0) / 100.0)).astype(np.float32)
        xc, _ = mod.extract_coastline(dsm, xs, ys, threshold=0.0)
        valid = np.isfinite(xc)
        assert valid.sum() > 30
        assert abs(np.nanmean(xc) - 3000.0) < 60.0

    def test_feature_geojson(self):
        xc = np.array([3000.0, 3010.0, np.nan, 2990.0])
        ys = np.array([4.0, 3.0, 2.0, 1.0])
        feat = mod.coastline_feature(xc, ys, [116, 39, 117, 40], "t1", 0.0)
        assert feat["geometry"]["type"] == "LineString"
        assert feat["properties"]["n_points"] == 3


class TestEPR:
    def test_retreat_positive(self):
        xc_t1 = np.full(10, 3000.0)
        xc_t2 = np.full(10, 2800.0)   # 向陆后退 200m
        epr = mod.compute_epr(xc_t1, xc_t2, dt_years=10.0)
        assert epr["mean_retreat_m"] == pytest.approx(200.0)
        assert epr["mean_epr_m_per_yr"] == pytest.approx(20.0)
        assert epr["frac_eroding"] == pytest.approx(1.0)

    def test_accretion_negative(self):
        xc_t1 = np.full(5, 3000.0)
        xc_t2 = np.full(5, 3200.0)   # 向海前进 → 堆积
        epr = mod.compute_epr(xc_t1, xc_t2, dt_years=10.0)
        assert epr["mean_retreat_m"] < 0
        assert epr["frac_eroding"] == pytest.approx(0.0)

    def test_no_overlap_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.compute_epr(np.full(3, np.nan), np.full(3, np.nan), 10.0)


class TestVolume:
    def test_erosion_volume(self):
        diff = np.array([[-2.0, 1.0], [-3.0, 0.0]], dtype=np.float32)
        vol = mod.erosion_volume(diff, res_x=10.0, res_y=10.0)
        # 侵蚀 = (2+3)*100 = 500; 堆积 = 1*100 = 100; 净 = (-2+1-3)*100 = -400
        assert vol["erosion_volume_m3"] == pytest.approx(500.0)
        assert vol["accretion_volume_m3"] == pytest.approx(100.0)
        assert vol["net_volume_m3"] == pytest.approx(-400.0)
        assert vol["max_erosion_depth_m"] == pytest.approx(3.0)


class TestSyntheticIntegration:
    def test_erosion_and_retreat(self):
        bbox = [116.0, 39.0, 116.05, 39.03]
        pts_t1, pts_t2, info = mod.generate_synthetic(bbox, 1.0, seed=7)
        dsm_t1, xs, ys, rx, ry = mod.points_to_dsm(pts_t1, bbox, 1.0)
        dsm_t2, _, _, _, _ = mod.points_to_dsm(pts_t2, bbox, 1.0)
        diff = dsm_t2 - dsm_t1

        # 侵蚀存在
        vol = mod.erosion_volume(diff, rx, ry)
        assert vol["erosion_volume_m3"] > 0
        assert vol["net_volume_m3"] < 0   # 净侵蚀

        # 海岸线后退
        xc_t1, _ = mod.extract_coastline(dsm_t1, xs, ys, 0.0)
        xc_t2, _ = mod.extract_coastline(dsm_t2, xs, ys, 0.0)
        assert np.nanmean(xc_t2) < np.nanmean(xc_t1)   # t2 更靠陆

        # EPR 后退量接近真值
        epr = mod.compute_epr(xc_t1, xc_t2, 10.0)
        true_retreat = info["true_retreat_m"]
        assert epr["mean_retreat_m"] > 0
        assert 0.6 * true_retreat < epr["mean_retreat_m"] < 1.4 * true_retreat
