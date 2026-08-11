"""Core algorithm tests for volcanic-hazard-assessment."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as vh


class TestIndices:
    def test_thermal_anomaly_clips_negative(self):
        bt = np.array([[280.0, 290.0, 350.0]])  # baseline 290
        idx = vh.thermal_anomaly_index(bt, baseline=290.0)
        assert idx.min() >= 0.0
        assert idx.max() <= 1.0
        # 最热像元归一化为 1，低于基线的为 0
        assert idx[0, 2] == idx.max()

    def test_deformation_uses_magnitude(self):
        rate = np.array([[-50.0, 0.0, 50.0]])
        idx = vh.deformation_index(rate)
        assert idx[0, 0] == idx[0, 2]  # 沉降与隆起同幅 → 同指数
        assert idx[0, 1] == 0.0

    def test_so2_non_negative_and_bounded(self):
        col = np.array([[-5.0, 0.0, 100.0, 500.0]])
        idx = vh.so2_index(col)
        assert idx.min() >= 0.0
        assert idx.max() <= 1.0


class TestRecency:
    def test_recent_higher_than_old(self):
        assert vh.eruption_recency(5) > vh.eruption_recency(200)

    def test_zero_years_is_one(self):
        assert abs(vh.eruption_recency(0) - 1.0) < 1e-12

    def test_monotonic_decreasing(self):
        yrs = [0, 10, 50, 100, 500]
        vals = [vh.eruption_recency(y) for y in yrs]
        assert all(vals[i] >= vals[i + 1] for i in range(len(vals) - 1))

    def test_negative_raises(self):
        with pytest.raises(vh.ValidationError):
            vh.eruption_recency(-1)


class TestActivityScore:
    def test_bounded_01(self):
        rng = np.random.default_rng(0)
        th = rng.uniform(0, 1, (16, 16))
        df = rng.uniform(0, 1, (16, 16))
        so = rng.uniform(0, 1, (16, 16))
        s = vh.activity_score(th, df, so, recency=0.7)
        assert s.min() >= 0.0
        assert s.max() <= 1.0

    def test_all_zero_gives_recency_only(self):
        z = np.zeros((8, 8))
        s = vh.activity_score(z, z, z, recency=1.0, weights=(0.35, 0.25, 0.25, 0.15))
        # 三个空间分量为 0，只剩 recency 项 → 0.15/1.0 = 0.15
        np.testing.assert_allclose(s, 0.15, atol=1e-6)

    @pytest.mark.parametrize("comp", ["thermal", "deformation", "so2", "recency"])
    def test_monotonic_in_each_component(self, comp):
        """提升任一分量，评分不得下降。"""
        rng = np.random.default_rng(1)
        th = rng.uniform(0, 0.5, (12, 12))
        df = rng.uniform(0, 0.5, (12, 12))
        so = rng.uniform(0, 0.5, (12, 12))
        rec = 0.3
        base = vh.activity_score(th, df, so, rec)
        if comp == "thermal":
            hi = vh.activity_score(th + 0.5, df, so, rec)
        elif comp == "deformation":
            hi = vh.activity_score(th, df + 0.5, so, rec)
        elif comp == "so2":
            hi = vh.activity_score(th, df, so + 0.5, rec)
        else:
            hi = vh.activity_score(th, df, so, rec + 0.5)
        assert hi.mean() >= base.mean() - 1e-9

    def test_shape_mismatch_raises(self):
        with pytest.raises(vh.ValidationError):
            vh.activity_score(np.zeros((4, 4)), np.zeros((4, 5)), np.zeros((4, 4)), 0.5)


class TestClassify:
    def test_level_monotonic_with_score(self):
        score = np.linspace(0, 1, 100).reshape(10, 10)
        lvl = vh.classify_activity(score)
        assert lvl.min() >= 0 and lvl.max() <= 4
        flat = lvl.ravel()
        assert np.all(np.diff(flat) >= 0)

    def test_labels_length(self):
        assert len(vh.ACTIVITY_LABELS) == 5


class TestSynthetic:
    def test_shapes(self):
        layers, info = vh.generate_synthetic([120, 30, 121, 31])
        assert layers["brightness_temp"].shape == (64, 64)
        assert layers["deformation"].shape == (64, 64)
        assert layers["so2"].shape == (64, 64)
        assert info["max_bt"] > info["baseline"]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [120.0, 30.0, 121.0, 31.0]
        p = str(tmp_path / "v.tif")
        vh.write_geotiff(p, cube, bbox)
        back, bb = vh.read_geotiff(p)
        np.testing.assert_allclose(bb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(vh.UsageError):
            vh.read_geotiff("/nonexistent/v.tif")
