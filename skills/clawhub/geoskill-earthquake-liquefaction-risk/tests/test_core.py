"""Core algorithm tests for earthquake-liquefaction-risk."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as lq


class TestCSR:
    def test_increases_with_pga(self):
        lo = float(lq.cyclic_stress_ratio(0.1, depth=3.0, water_table_depth=2.0))
        hi = float(lq.cyclic_stress_ratio(0.4, depth=3.0, water_table_depth=2.0))
        assert hi > lo > 0

    def test_decreases_with_depth(self):
        shallow = float(lq.cyclic_stress_ratio(0.3, depth=2.0))
        deep = float(lq.cyclic_stress_ratio(0.3, depth=15.0))
        assert shallow > deep

    def test_shallow_water_table_amplifies(self):
        shallow_wt = float(lq.cyclic_stress_ratio(0.3, depth=3.0, water_table_depth=0.0))
        deep_wt = float(lq.cyclic_stress_ratio(0.3, depth=3.0, water_table_depth=30.0))
        assert shallow_wt > deep_wt


class TestCRR:
    def test_increases_with_n(self):
        lo = float(lq.cyclic_resistance_ratio(5.0))
        hi = float(lq.cyclic_resistance_ratio(30.0))
        assert hi > lo

    def test_fines_reduce_resistance(self):
        clean = float(lq.cyclic_resistance_ratio(20.0, fines_pct=0.0))
        silty = float(lq.cyclic_resistance_ratio(20.0, fines_pct=40.0))
        assert clean > silty

    def test_bounded(self):
        assert float(lq.cyclic_resistance_ratio(1000.0)) <= 0.6


class TestFS:
    def test_decreases_with_pga(self):
        crr = lq.cyclic_resistance_ratio(15.0)
        fs_lo = float(lq.factor_of_safety(crr, lq.cyclic_stress_ratio(0.1)))
        fs_hi = float(lq.factor_of_safety(crr, lq.cyclic_stress_ratio(0.5)))
        assert fs_lo > fs_hi


class TestLPI:
    def test_non_negative(self):
        rng = np.random.default_rng(0)
        pga = rng.uniform(0.05, 0.6, (16, 16))
        n = rng.uniform(2, 50, (16, 16))
        lpi, fs = lq.lpi_raster(pga, n, depth=3.0, dz=3.0)
        assert lpi.min() >= 0.0
        assert fs.min() > 0.0

    def test_monotonic_with_pga(self):
        """PGA 越高 → FS 越低 → LPI 越高。"""
        n = np.full((8, 8), 10.0)
        lpi_lo, _ = lq.lpi_raster(np.full((8, 8), 0.1), n)
        lpi_hi, _ = lq.lpi_raster(np.full((8, 8), 0.5), n)
        assert lpi_hi.mean() >= lpi_lo.mean()
        assert lpi_hi.mean() > 0.0

    def test_inverse_with_n(self):
        """土越密实(N 越大) → 越抗液化 → LPI 越低。"""
        pga = np.full((8, 8), 0.4)
        lpi_loose, _ = lq.lpi_raster(pga, np.full((8, 8), 5.0))
        lpi_dense, _ = lq.lpi_raster(pga, np.full((8, 8), 30.0))
        assert lpi_loose.mean() > lpi_dense.mean()

    def test_zero_when_stable(self):
        """弱震动 + 密实土 → FS≥1 → LPI 全 0。"""
        lpi, fs = lq.lpi_raster(np.full((8, 8), 0.05), np.full((8, 8), 40.0))
        assert np.all(fs >= 1.0)
        assert lpi.sum() == 0.0

    def test_shape_mismatch_raises(self):
        with pytest.raises(lq.ValidationError):
            lq.lpi_raster(np.zeros((4, 4)), np.zeros((4, 5)))


class TestClassify:
    def test_levels_range(self):
        lpi = np.array([[0.0, 8.0, 20.0]])
        lvl = lq.classify_lpi(lpi)
        assert lvl[0, 0] == 0
        assert lvl[0, 1] == 1
        assert lvl[0, 2] == 2


class TestSynthetic:
    def test_shapes(self):
        layers, info = lq.generate_synthetic([116, 39, 117, 40])
        for k in ("pga", "n_value", "water_table"):
            assert layers[k].shape == (64, 64)
        assert layers["pga"].min() >= 0.0
        assert info["max_pga"] > 0.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        p = str(tmp_path / "l.tif")
        lq.write_geotiff(p, cube, bbox)
        back, bb = lq.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(lq.UsageError):
            lq.read_geotiff("/nonexistent/l.tif")
