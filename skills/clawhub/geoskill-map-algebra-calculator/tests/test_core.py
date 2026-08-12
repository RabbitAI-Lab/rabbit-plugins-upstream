"""Core algorithm tests for map-algebra-calculator."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


def _bands():
    b1 = np.full((4, 4), 0.1, dtype=np.float32)   # red
    b2 = np.full((4, 4), 0.5, dtype=np.float32)   # nir
    return {"b1": b1, "b2": b2}


class TestEvaluate:
    def test_ndvi_analytic(self):
        out = mod.evaluate_expression("(b2 - b1) / (b2 + b1)", _bands())
        # (0.5-0.1)/(0.5+0.1) = 0.4/0.6 = 0.6667
        np.testing.assert_allclose(out, 0.4 / 0.6, atol=1e-5)

    def test_linear_expression(self):
        bands = {"b1": np.array([[1.0, 2.0], [3.0, 4.0]], dtype=np.float32)}
        out = mod.evaluate_expression("b1 * 2 + 3", bands)
        np.testing.assert_allclose(out, [[5, 7], [9, 11]], atol=1e-5)

    def test_function_sqrt(self):
        bands = {"b1": np.full((3, 3), 4.0, dtype=np.float32)}
        out = mod.evaluate_expression("sqrt(b1)", bands)
        np.testing.assert_allclose(out, 2.0, atol=1e-5)

    def test_power_and_const(self):
        bands = {"b1": np.full((2, 2), 3.0, dtype=np.float32)}
        out = mod.evaluate_expression("b1 ** 2", bands)
        np.testing.assert_allclose(out, 9.0, atol=1e-5)

    def test_divide_by_zero_yields_zero(self):
        bands = {"b1": np.ones((3, 3), dtype=np.float32),
                 "b2": np.zeros((3, 3), dtype=np.float32)}
        out = mod.evaluate_expression("b1 / b2", bands)
        assert np.all(out == 0.0)
        assert np.all(np.isfinite(out))

    def test_unary_minus(self):
        bands = {"b1": np.full((2, 2), 5.0, dtype=np.float32)}
        out = mod.evaluate_expression("-b1 + 1", bands)
        np.testing.assert_allclose(out, -4.0, atol=1e-5)

    def test_broadcast_scalar(self):
        bands = {"b1": np.ones((4, 5), dtype=np.float32)}
        out = mod.evaluate_expression("b1 + 10", bands)
        assert out.shape == (4, 5)
        np.testing.assert_allclose(out, 11.0, atol=1e-6)


class TestSecurity:
    def test_import_rejected(self):
        with pytest.raises(mod.UsageError):
            mod.evaluate_expression("__import__('os')", _bands())

    def test_attribute_access_rejected(self):
        with pytest.raises(mod.UsageError):
            mod.evaluate_expression("b1.shape", _bands())

    def test_non_whitelist_func_rejected(self):
        with pytest.raises(mod.UsageError):
            mod.evaluate_expression("system('ls')", _bands())

    def test_subscript_rejected(self):
        with pytest.raises(mod.UsageError):
            mod.evaluate_expression("b1[0]", _bands())

    def test_unknown_variable_rejected(self):
        with pytest.raises(mod.UsageError):
            mod.evaluate_expression("b99 + 1", _bands())

    def test_syntax_error_rejected(self):
        with pytest.raises(mod.UsageError):
            mod.evaluate_expression("b1 +* 2", _bands())


class TestPresets:
    def test_build_preset_ndvi(self):
        expr = mod.build_preset_expression("ndvi", red=3, nir=4)
        assert expr == "(b4 - b3) / (b4 + b3)"

    def test_build_preset_ndwi(self):
        expr = mod.build_preset_expression("ndwi", green=2, nir=4)
        assert expr == "(b2 - b4) / (b2 + b4)"

    def test_unknown_preset_raises(self):
        with pytest.raises(mod.UsageError):
            mod.build_preset_expression("bogus")


class TestSynthetic:
    def test_ndvi_vegetation_gt_water(self):
        cube, info = mod.generate_synthetic([116, 39, 117, 40])
        assert cube.shape[0] == 4
        bands = {f"b{i + 1}": cube[i] for i in range(4)}
        ndvi = mod.evaluate_expression("(b4 - b3) / (b4 + b3)", bands)
        # 植被区在右侧 (x>0.66 → 列 > 0.66*64)，水体在左侧 (x<0.33)
        veg_mean = ndvi[:, 50:].mean()
        water_mean = ndvi[:, :14].mean()
        assert veg_mean > 0.6
        assert water_mean < 0.0
        assert veg_mean > water_mean
