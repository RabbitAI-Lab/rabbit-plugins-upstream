"""Core algorithm tests for telecom-coverage-optimization."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as tc


class TestMobileCorrection:
    def test_small_city_formula(self):
        # f=1000, hm=1.5, 中小城市式: (1.1*3-0.7)*1.5-(1.56*3-0.8)=0.02
        a = tc.mobile_height_correction(1000.0, 1.5, environment="suburban")
        assert a == pytest.approx(0.02, abs=1e-4)

    def test_bad_frequency(self):
        with pytest.raises(tc.ValidationError):
            tc.mobile_height_correction(0.0, 1.5)


class TestPathLoss:
    def test_increases_with_distance(self):
        d = np.array([[1.0, 5.0, 20.0]], dtype=np.float32)
        l = tc.hata_path_loss(1800.0, 30.0, 1.5, d, "urban")
        assert l[0, 0] < l[0, 1] < l[0, 2]

    def test_increases_with_frequency(self):
        d = np.array([[5.0]], dtype=np.float32)
        l900 = tc.hata_path_loss(900.0, 30.0, 1.5, d, "urban")[0, 0]
        l1800 = tc.hata_path_loss(1800.0, 30.0, 1.5, d, "urban")[0, 0]
        assert l1800 > l900

    def test_environment_ordering(self):
        # 同样距离下 城区损耗 > 郊区 > 开阔地
        d = np.array([[5.0]], dtype=np.float32)
        lu = tc.hata_path_loss(1800.0, 30.0, 1.5, d, "urban")[0, 0]
        ls = tc.hata_path_loss(1800.0, 30.0, 1.5, d, "suburban")[0, 0]
        lo = tc.hata_path_loss(1800.0, 30.0, 1.5, d, "open")[0, 0]
        assert lu > ls > lo

    def test_bad_heights(self):
        with pytest.raises(tc.ValidationError):
            tc.hata_path_loss(1800.0, 0.0, 1.5, np.array([[1.0]]))

    def test_reasonable_magnitude(self):
        # 1km, 1800MHz, 30m 基站：Hata 城市损耗约 130 dB 量级
        l = tc.hata_path_loss(1800.0, 30.0, 1.5, np.array([[1.0]]), "urban")[0, 0]
        assert 110.0 < float(l) < 170.0


class TestClutterAndPower:
    def test_received_power_identity(self):
        pl = np.array([[120.0, 140.0]], dtype=np.float32)
        cl = np.array([[5.0, 10.0]], dtype=np.float32)
        rsl = tc.received_power(tx_dbm=43.0, gain_db=15.0, path_loss=pl, clutter=cl)
        # 43 + 15 - loss - clutter
        assert rsl[0, 0] == pytest.approx(43 + 15 - 120 - 5)
        assert rsl[0, 1] == pytest.approx(43 + 15 - 140 - 10)

    def test_no_clutter(self):
        pl = np.array([[100.0]], dtype=np.float32)
        rsl = tc.received_power(40.0, 10.0, pl, None)
        assert rsl[0, 0] == pytest.approx(40 + 10 - 100)

    def test_clutter_nonnegative(self):
        dem = np.full((8, 8), 50.0, dtype=np.float32)
        dem[4, 4] = 300.0
        building = np.zeros((8, 8), dtype=np.float32)
        cl = tc.clutter_loss(dem, building, hb=30.0)
        assert cl.min() >= 0.0
        assert cl[4, 4] > cl[0, 0]


class TestDistance:
    def test_zero_at_tower(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        # tower at center -> center pixel distance ~ small
        d = tc.distance_km_grid(bbox, 128, 128, 116.5, 39.5)
        assert d.shape == (128, 128)
        assert float(d.min()) < 2.0

    def test_corner_farther(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        d = tc.distance_km_grid(bbox, 64, 64, 116.5, 39.5)
        assert d[0, 0] > d[32, 32]


class TestCoverage:
    def test_coverage_bounds_and_center_covered(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, info = tc.generate_synthetic_cube(bbox, seed=2)
        dem, building = cube[0], cube[1]
        h, w = dem.shape
        best, covered = tc.coverage_from_towers(
            bbox, h, w, dem, building, info["towers"],
            f_mhz=1800.0, hm=1.5, environment="urban",
            tx_dbm=43.0, gain_db=15.0, threshold_dbm=-100.0,
        )
        frac = float(np.mean(covered))
        assert 0.0 <= frac <= 1.0
        # 强中心基站附近应被覆盖
        assert covered[h // 2, w // 2] == True  # noqa: E712

    def test_blind_equals_complement(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, info = tc.generate_synthetic_cube(bbox, seed=4)
        dem, building = cube[0], cube[1]
        h, w = dem.shape
        # 极高门限 -> 几乎全盲
        _, covered = tc.coverage_from_towers(
            bbox, h, w, dem, building, info["towers"],
            1800.0, 1.5, "urban", 43.0, 15.0, threshold_dbm=50.0)
        blind = 1.0 - float(np.mean(covered))
        assert blind >= float(np.mean(covered))  # 高门限下盲区占多数
        assert blind <= 1.0

    def test_lower_threshold_more_coverage(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, info = tc.generate_synthetic_cube(bbox, seed=6)
        dem, building = cube[0], cube[1]
        h, w = dem.shape
        args = dict(f_mhz=1800.0, hm=1.5, environment="urban", tx_dbm=43.0, gain_db=15.0)
        _, c_loose = tc.coverage_from_towers(bbox, h, w, dem, building, info["towers"],
                                             threshold_dbm=-110.0, **args)
        _, c_strict = tc.coverage_from_towers(bbox, h, w, dem, building, info["towers"],
                                              threshold_dbm=-80.0, **args)
        assert float(np.mean(c_loose)) >= float(np.mean(c_strict))


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "c.tif")
        tc.write_geotiff(path, cube, bbox)
        back, rb = tc.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(tc.UsageError):
            tc.read_geotiff("/nonexistent/c.tif")
