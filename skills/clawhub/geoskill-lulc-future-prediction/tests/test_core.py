"""Core algorithm tests for lulc-future-prediction."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as fp


class TestTransitionMatrix:
    def test_counts(self):
        l1 = np.array([[1, 1], [2, 2]])
        l2 = np.array([[1, 2], [2, 2]])
        cm = fp.transition_matrix(l1, l2, n_classes=4)
        assert cm[0, 0] == 1   # 1->1
        assert cm[0, 1] == 1   # 1->2
        assert cm[1, 1] == 2   # 2->2
        assert cm.sum() == 4

    def test_shape_mismatch_raises(self):
        with pytest.raises(fp.ValidationError):
            fp.transition_matrix(np.zeros((2, 2)), np.zeros((3, 3)), 4)

    def test_out_of_range_raises(self):
        with pytest.raises(fp.ValidationError):
            fp.transition_matrix(np.array([[0, 1]]), np.array([[1, 1]]), 4)
        with pytest.raises(fp.ValidationError):
            fp.transition_matrix(np.array([[5, 1]]), np.array([[1, 1]]), 4)


class TestMarkovProbabilities:
    def test_rows_sum_to_one(self):
        cm = np.array([[3, 1], [0, 2]], dtype=float)
        p = fp.markov_probabilities(cm)
        np.testing.assert_allclose(p[0], [0.75, 0.25])
        np.testing.assert_allclose(p[1], [0.0, 1.0])
        np.testing.assert_allclose(p.sum(axis=1), [1.0, 1.0])

    def test_empty_row_becomes_identity(self):
        cm = np.array([[0, 0], [1, 1]], dtype=float)
        p = fp.markov_probabilities(cm)
        np.testing.assert_allclose(p[0], [1.0, 0.0])
        np.testing.assert_allclose(p[1], [0.5, 0.5])


class TestProjectAreas:
    def test_identity_no_change(self):
        p = np.eye(3)
        areas = np.array([10.0, 20.0, 30.0])
        np.testing.assert_allclose(fp.project_areas(areas, p, 5), areas)

    def test_one_step(self):
        p = np.array([[0.9, 0.1], [0.2, 0.8]])
        areas = np.array([100.0, 0.0])
        # [100,0] @ P = [90, 10]
        np.testing.assert_allclose(fp.project_areas(areas, p, 1), [90.0, 10.0])

    def test_negative_steps_raises(self):
        with pytest.raises(fp.ValidationError):
            fp.project_areas(np.array([1.0, 1.0]), np.eye(2), -1)

    def test_total_conserved(self):
        rng = np.random.default_rng(0)
        p = rng.random((4, 4))
        p = p / p.sum(axis=1, keepdims=True)
        areas = np.array([100.0, 50.0, 30.0, 20.0])
        proj = fp.project_areas(areas, p, 3)
        np.testing.assert_allclose(proj.sum(), areas.sum(), rtol=1e-6)


class TestNeighborhood:
    def test_adjacent_pixels_scored(self):
        lulc = np.zeros((5, 5), dtype=np.int64)
        lulc[2, 2] = 4  # 中心一个城市像元
        frac = fp.neighborhood_fraction(lulc, 4)
        # 中心像元的 8 邻域都是城市（自身不算，中心邻域内无城市）→ 0
        assert frac[2, 2] == 0.0
        # 紧邻的像元 8 邻域中有 1 个城市 → 1/8
        np.testing.assert_allclose(frac[1, 2], 1.0 / 8.0)
        # 远处像元为 0
        assert frac[0, 0] == 0.0


class TestCAMarkov:
    def test_urban_expands(self):
        """合成场景：预测后城市像元数应大于 t2。"""
        synth = fp.generate_synthetic([116, 39, 117, 40], seed=5)
        res = fp.ca_markov_predict(synth["lulc1"], synth["lulc2"],
                                   n_classes=4, n_steps=1, seed=5)
        urban_code = 4
        urban_t2 = res["current_areas"][urban_code - 1]
        urban_pred = res["predicted_counts"][urban_code - 1]
        assert urban_pred > urban_t2
        assert res["conversions"] > 0

    def test_total_pixels_conserved(self):
        synth = fp.generate_synthetic([116, 39, 117, 40])
        res = fp.ca_markov_predict(synth["lulc1"], synth["lulc2"],
                                   n_classes=4, n_steps=1)
        assert sum(res["predicted_counts"]) == synth["lulc2"].size

    def test_valid_class_codes(self):
        synth = fp.generate_synthetic([116, 39, 117, 40])
        res = fp.ca_markov_predict(synth["lulc1"], synth["lulc2"], n_classes=4)
        uniq = set(np.unique(res["predicted"]).tolist())
        assert uniq.issubset({1, 2, 3, 4})


class TestSynthetic:
    def test_t2_urban_greater_than_t1(self):
        synth = fp.generate_synthetic([116, 39, 117, 40])
        u1 = int(np.sum(synth["lulc1"] == 4))
        u2 = int(np.sum(synth["lulc2"] == 4))
        assert u2 > u1


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(1, 4, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        fp.write_geotiff(path, arr, bbox)
        back, rb = fp.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)

    def test_read_missing_raises(self):
        with pytest.raises(fp.UsageError):
            fp.read_geotiff("/no/such/file.tif")
