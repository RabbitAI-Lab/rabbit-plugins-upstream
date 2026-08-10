"""Core algorithm tests for stream-flow-simulation."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestSCSRunoff:
    def test_Q_less_than_P(self):
        """径流深必须小于降雨量。"""
        cn = np.array([70.0, 80.0, 90.0])
        Q, S, Ia = mod.scs_runoff_depth(100.0, cn)
        assert np.all(Q < 100.0)
        assert np.all(Q >= 0.0)

    def test_higher_cn_higher_Q(self):
        """CN 越高，径流深越大。"""
        cn = np.array([55.0, 70.0, 85.0, 95.0])
        Q, _, _ = mod.scs_runoff_depth(120.0, cn)
        assert np.all(np.diff(Q) > 0)

    def test_cn100_equals_P(self):
        """CN=100（水面）时径流深≈降雨。"""
        Q, _, _ = mod.scs_runoff_depth(80.0, np.array([100.0]))
        assert abs(Q[0] - 80.0) < 1e-6

    def test_small_rain_no_runoff(self):
        """降雨小于初损 Ia 时无产流。"""
        Q, S, Ia = mod.scs_runoff_depth(5.0, np.array([70.0]))
        assert Ia[0] > 5.0
        assert Q[0] == 0.0

    def test_formula_exact(self):
        """核对一个手算案例：CN=80, P=100 → S=63.5, Ia=12.7, Q=(87.3)²/(87.3+63.5)。"""
        Q, S, Ia = mod.scs_runoff_depth(100.0, np.array([80.0]))
        S_exp = 25400.0 / 80.0 - 254.0
        Ia_exp = 0.2 * S_exp
        Q_exp = (100.0 - Ia_exp) ** 2 / (100.0 - Ia_exp + S_exp)
        assert abs(S[0] - S_exp) < 1e-9
        assert abs(Q[0] - Q_exp) < 1e-6


class TestCNLookup:
    def test_known_codes(self):
        lu = np.array([[0, 1, 5], [3, 4, 6]])
        cn = mod.cn_from_landuse(lu)
        assert cn[0, 0] == 100   # water
        assert cn[0, 2] == 55    # forest
        assert cn[1, 1] == 69    # grassland

    def test_unknown_uses_default(self):
        cn = mod.cn_from_landuse(np.array([[99]]))
        assert cn[0, 0] == mod.DEFAULT_CN


class TestStormAndUH:
    def test_triangular_fractions_sum1(self):
        f = mod.triangular_fractions(20)
        assert abs(f.sum() - 1.0) < 1e-9
        assert np.all(f >= 0)

    def test_triangular_peak_shape(self):
        f = mod.triangular_fractions(21, peak_index=8)
        assert f[8] == f.max()

    def test_kirpich_increases_with_length(self):
        tc_short = mod.kirpich_tc_hours(500.0, 0.05)
        tc_long = mod.kirpich_tc_hours(5000.0, 0.05)
        assert tc_long > tc_short
        assert tc_short > 0

    def test_uh_volume_conservation(self):
        """单位线对 1 mm 的响应积分应等于流域体积 area×1000。"""
        area = 12.5
        dt_h = 0.5
        t, resp = mod.unit_hydrograph_response(area, tp_h=3.0, tb_h=8.0, dt_h=dt_h)
        volume = np.sum(resp) * dt_h * 3600.0
        assert abs(volume - area * 1000.0) / (area * 1000.0) < 1e-6
        assert resp.max() > 0


class TestHydrograph:
    def test_water_balance(self):
        """卷积后总径流量应与 SCS 产流体积一致（守恒）。"""
        area = 20.0
        dt_h = 0.5
        storm = mod.triangular_fractions(12)
        t, resp = mod.unit_hydrograph_response(area, 3.0, 8.0, dt_h)
        time_h, q, stats = mod.convolve_hydrograph(50.0, area, storm, t, resp, dt_h)
        assert abs(stats["volume_balance_ratio"] - 1.0) < 1e-6
        assert stats["peak_discharge_m3s"] > 0
        assert q.size == time_h.size

    def test_shorter_duration_higher_peak(self):
        """同样的总雨量，历时越短（重现期越大）洪峰越高。"""
        area = 15.0
        dt_h = 0.5
        t, resp = mod.unit_hydrograph_response(area, 3.0, 8.0, dt_h)
        long_storm = mod.triangular_fractions(24)    # 长历时
        short_storm = mod.triangular_fractions(6)    # 短历时
        _, _, s_long = mod.convolve_hydrograph(60.0, area, long_storm, t, resp, dt_h)
        _, _, s_short = mod.convolve_hydrograph(60.0, area, short_storm, t, resp, dt_h)
        assert s_short["peak_discharge_m3s"] > s_long["peak_discharge_m3s"]

    def test_invalid_fractions_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.convolve_hydrograph(50.0, 10.0, np.zeros(5), np.arange(3.0), np.ones(3), 0.5)


class TestSyntheticAndIO:
    def test_synthetic_shapes(self):
        info = mod.generate_synthetic([116, 39, 117, 40], grid_shape=(32, 32))
        assert info["dem"].shape == (32, 32)
        assert info["landuse"].shape == (32, 32)
        assert info["area_km2"] > 0
        assert info["slope"] > 0

    def test_area_km2_positive(self):
        a = mod.bbox_area_km2([116.0, 39.0, 117.0, 40.0])
        assert a > 1000  # 约 1°×1° 在中纬度 ~8500 km²

    def test_geotiff_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 50, (1, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "r.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back, arr, atol=1e-4)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
