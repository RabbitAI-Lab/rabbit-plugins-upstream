"""Core algorithm tests for insurance-risk-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as ir


class TestProbability:
    def test_annual_probability_exact(self):
        assert ir.annual_probability(100.0) == pytest.approx(0.01)
        assert ir.annual_probability(50.0) == pytest.approx(0.02)

    def test_nonpositive_raises(self):
        with pytest.raises(ir.ValidationError):
            ir.annual_probability(0.0)


class TestVulnerability:
    def test_linear_endpoints_and_mid(self):
        x = np.array([[0.5, 1.75, 3.0]], dtype=np.float32)
        r = ir.vulnerability_ratio(x, i0=0.5, i1=3.0, curve="linear")
        assert r[0, 0] == pytest.approx(0.0)
        assert r[0, 1] == pytest.approx(0.5)
        assert r[0, 2] == pytest.approx(1.0)

    def test_linear_clips_outside(self):
        x = np.array([[0.0, 10.0]], dtype=np.float32)
        r = ir.vulnerability_ratio(x, 0.5, 3.0, "linear")
        assert r[0, 0] == 0.0 and r[0, 1] == 1.0

    def test_sigmoid_monotonic_bounded(self):
        x = np.linspace(0, 5, 50).astype(np.float32)
        r = ir.vulnerability_ratio(x, 0.5, 3.0, "sigmoid")
        assert np.all(np.diff(r) >= -1e-6)
        assert r.min() >= 0.0 and r.max() <= 1.0

    def test_sigmoid_midpoint_is_half(self):
        # x == (i0+i1)/2 时 sigmoid 恰为 0.5
        mid = 0.5 * (0.5 + 3.0)
        r = ir.vulnerability_ratio(np.array([[mid]], dtype=np.float32), 0.5, 3.0, "sigmoid")
        assert r[0, 0] == pytest.approx(0.5, abs=1e-5)

    def test_bad_curve_bounds_raise(self):
        with pytest.raises(ir.ValidationError):
            ir.vulnerability_ratio(np.zeros((2, 2)), 3.0, 0.5, "linear")


class TestExpectedLoss:
    def test_single_exact(self):
        asset = np.array([[100000.0]], dtype=np.float32)
        inten = np.array([[1.75]], dtype=np.float32)  # mid of [0.5,3.0] -> ratio 0.5
        loss = ir.expected_loss_single(asset, inten, return_period=100.0,
                                       i0=0.5, i1=3.0, curve="linear")
        # 0.01 * 100000 * 0.5 = 500
        assert loss[0, 0] == pytest.approx(500.0, rel=1e-6)

    def test_multi_hazard_additive(self):
        asset = np.array([[100000.0]], dtype=np.float32)
        intensities = {
            "flood": np.array([[3.0]], dtype=np.float32),    # ratio 1
            "wind": np.array([[60.0]], dtype=np.float32),    # ratio 1
            "seismic": np.array([[0.1]], dtype=np.float32),  # ratio 0
        }
        total, per = ir.multi_hazard_loss(asset, intensities, curve="linear")
        # flood: 1/100*1e5*1=1000 ; wind: 1/50*1e5*1=2000 ; seismic: 0
        assert per["flood"][0, 0] == pytest.approx(1000.0, rel=1e-6)
        assert per["wind"][0, 0] == pytest.approx(2000.0, rel=1e-6)
        assert per["seismic"][0, 0] == pytest.approx(0.0, abs=1e-3)
        assert total[0, 0] == pytest.approx(3000.0, rel=1e-6)

    def test_unknown_hazard_raises(self):
        asset = np.zeros((4, 4), dtype=np.float32)
        with pytest.raises(ir.ValidationError):
            ir.multi_hazard_loss(asset, {"volcano": np.zeros((4, 4))})


class TestRiskClass:
    def test_monotonic_classes(self):
        loss = np.array([[0.0, 5.0, 50.0, 500.0]], dtype=np.float32)
        cls = ir.risk_class(loss, [1.0, 10.0, 100.0])
        assert list(cls[0]) == [0, 1, 2, 3]


class TestSynthetic:
    def test_shape_and_positive_loss(self):
        bbox = [116.0, 39.0, 117.0, 40.0]
        cube, info = ir.generate_synthetic_cube(bbox, seed=3)
        assert cube.shape[0] == 4
        asset, flood, wind, seismic = cube[0], cube[1], cube[2], cube[3]
        total, _ = ir.multi_hazard_loss(asset, {"flood": flood, "wind": wind, "seismic": seismic})
        assert total.min() >= 0.0
        assert float(total.sum()) > 0.0


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (4, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "r.tif")
        ir.write_geotiff(path, cube, bbox)
        back, rb = ir.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(ir.UsageError):
            ir.read_geotiff("/nonexistent/z.tif")
