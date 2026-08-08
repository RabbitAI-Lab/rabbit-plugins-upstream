"""Core algorithm tests for lidar-powerline-detection."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestGroundFilter:
    def test_estimate_ground(self):
        rng = np.random.default_rng(0)
        ground = np.column_stack([
            rng.uniform(0, 100, 500), rng.uniform(0, 100, 500),
            rng.normal(2.0, 0.2, 500)])
        gz = mod.estimate_ground_height(ground, percentile=5.0)
        assert abs(gz - 1.7) < 0.5

    def test_filter_above_ground(self):
        pts = np.array([
            [0, 0, 0.0], [1, 1, 0.5], [2, 2, 10.0], [3, 3, 20.0],
        ], dtype=float)
        above, gz = mod.filter_above_ground(pts, min_height=5.0)
        assert above.shape[0] == 2  # only 10 and 20 m points
        assert np.all(above[:, 2] > 5.0)


class TestPCA:
    def test_elongated_direction(self):
        rng = np.random.default_rng(1)
        t = np.linspace(0, 100, 300)
        xy = np.column_stack([t, rng.normal(0, 0.2, 300)])
        centroid, direction, eigvals = mod.pca_direction(xy)
        # principal direction should be ~ +x
        assert abs(direction[0]) > 0.99
        assert abs(direction[1]) < 0.05
        assert eigvals[0] > 100 * eigvals[1]


class TestLinearFeature:
    def test_extract_line(self):
        rng = np.random.default_rng(2)
        t = np.linspace(0, 100, 400)
        line = np.column_stack([t, rng.normal(0, 0.3, 400), np.full(400, 15.0)])
        scatter = np.column_stack([
            rng.uniform(0, 100, 300), rng.uniform(-30, 30, 300),
            rng.uniform(5, 20, 300)])
        pts = np.vstack([line, scatter])
        feat = mod.detect_linear_feature(pts, inlier_thresh=2.0)
        assert feat["n_inliers"] >= 380  # most line points captured
        assert feat["elongation"] > 5.0


class TestCatenary:
    def test_fit_recovers_params(self):
        # 真值悬链线
        span = 200.0
        a_true = 500.0
        u0 = span / 2.0
        offset = 5.0
        u = np.linspace(0, span, 200)
        z = offset + a_true * np.cosh((u - u0) / a_true)
        res = mod.fit_catenary(u, z)
        assert res["rmse"] < 1e-3
        assert abs(res["a"] - a_true) < 1e-1
        # 真值弧垂 = a*(cosh(span/2a)-1)
        true_sag = a_true * (np.cosh(span / (2 * a_true)) - 1)
        assert res["sag"] == pytest.approx(true_sag, rel=1e-3)

    def test_fit_with_noise(self):
        rng = np.random.default_rng(3)
        span = 300.0
        a_true = 800.0
        u = np.linspace(0, span, 300)
        z = 2.0 + a_true * np.cosh((u - span / 2) / a_true) + rng.normal(0, 0.1, 300)
        res = mod.fit_catenary(u, z)
        assert res["rmse"] < 0.5
        assert abs(res["a"] - a_true) / a_true < 0.1

    def test_too_few_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.fit_catenary(np.array([0.0, 1.0]), np.array([0.0, 1.0]))


class TestTowers:
    def test_cluster_two_towers(self):
        rng = np.random.default_rng(4)
        pts = []
        for (tx, ty) in [(10.0, 10.0), (200.0, 10.0)]:
            pts.append(np.column_stack([
                tx + rng.normal(0, 1.0, 100),
                ty + rng.normal(0, 1.0, 100),
                rng.uniform(0, 25, 100)]))
        cloud = np.vstack(pts)
        towers = mod.cluster_towers(cloud, ground_z=0.0, high_thresh=15.0)
        assert len(towers) == 2
        for t in towers:
            assert t["height"] > 5.0


class TestLineTree:
    def test_clearance(self):
        line = np.column_stack([np.linspace(0, 100, 50), np.zeros(50)])
        veg = np.array([[50.0, 3.0], [20.0, 10.0], [80.0, 0.5]])
        res = mod.line_tree_distance(line, veg)
        assert res["n_vegetation"] == 3
        # 离散线点间距 ~2m，[80,0.5] 到最近线点距离略大于 0.5
        assert res["min_distance"] == pytest.approx(0.645, abs=0.1)
        assert res["n_within_5m"] >= 2

    def test_empty(self):
        res = mod.line_tree_distance(np.zeros((0, 2)), np.zeros((0, 2)))
        assert res["min_distance"] is None


class TestSyntheticIntegration:
    def test_full_pipeline(self):
        bbox = [116.0, 39.0, 116.02, 39.01]  # ~1.7km x 1.1km
        points, info = mod.generate_synthetic(bbox, seed=7)
        assert points.shape[1] == 3
        above, gz = mod.filter_above_ground(points, 5.0)
        feat = mod.detect_linear_feature(above, inlier_thresh=3.0)
        assert feat["elongation"] > 5.0
        towers = mod.cluster_towers(above, gz, high_thresh=15.0)
        assert len(towers) == 2
        # 悬链线拟合残差应很小
        u = mod.project_along(feat["inlier_points"], feat["centroid"], feat["direction"])
        # 排除塔架附近
        tower_u = np.array([
            float((np.array(t["xy"]) - feat["centroid"]) @ feat["direction"])
            for t in towers])
        keep = np.min(np.abs(u[:, None] - tower_u[None, :]), axis=1) > 12.0
        env_u, env_z = mod.upper_envelope(u[keep], feat["inlier_points"][keep, 2])
        cat = mod.fit_catenary(env_u, env_z)
        assert cat["rmse"] < 1.0
        assert abs(cat["sag"] - info["true_sag"]) < 3.0
