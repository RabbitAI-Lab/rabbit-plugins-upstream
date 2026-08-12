"""Core algorithm tests for lulc-change-matrix."""
import json
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as cm_mod


class TestTransitionCounts:
    def test_known_matrix(self):
        t1 = np.array([[0, 0], [1, 1]], dtype=np.int32)
        t2 = np.array([[0, 1], [1, 1]], dtype=np.int32)
        cm, classes = cm_mod.transition_counts(t1, t2)
        assert classes == [0, 1]
        # rows=from, cols=to. 0->0:1, 0->1:1, 1->1:2
        assert cm[0, 0] == 1
        assert cm[0, 1] == 1
        assert cm[1, 1] == 2
        assert cm[1, 0] == 0

    def test_row_col_sums(self):
        rng = np.random.default_rng(0)
        t1 = rng.integers(0, 4, (30, 30)).astype(np.int32)
        t2 = rng.integers(0, 4, (30, 30)).astype(np.int32)
        cm, classes = cm_mod.transition_counts(t1, t2)
        # row sums == t1 class counts
        for i, c in enumerate(classes):
            assert cm[i, :].sum() == int((t1 == c).sum())
            assert cm[:, i].sum() == int((t2 == c).sum())
        assert cm.sum() == t1.size

    def test_shape_mismatch_raises(self):
        with pytest.raises(cm_mod.ValidationError):
            cm_mod.transition_counts(np.zeros((4, 4), np.int32),
                                     np.zeros((5, 5), np.int32))

    def test_empty_raises(self):
        with pytest.raises(cm_mod.ValidationError):
            cm_mod.transition_counts(np.zeros((0, 0), np.int32),
                                     np.zeros((0, 0), np.int32))


class TestProportions:
    def test_sums_to_one(self):
        cm = np.array([[3, 1], [1, 3]], dtype=np.int64)
        prop = cm_mod.matrix_proportions(cm)
        assert prop.sum() == pytest.approx(1.0)
        assert prop[0, 0] == pytest.approx(3 / 8)

    def test_empty_zero(self):
        cm = np.zeros((2, 2), dtype=np.int64)
        prop = cm_mod.matrix_proportions(cm)
        assert prop.sum() == 0.0


class TestChangeSummary:
    def test_changed_and_net(self):
        # 4x4 identity-ish: class0 loses 1 to class1
        cm = np.array([[3, 1], [0, 4]], dtype=np.int64)
        s = cm_mod.change_summary(cm, [0, 1], [116, 39, 117, 40], (2, 4))
        assert s["total_pixels"] == 8
        assert s["changed_pixels"] == 1
        assert s["unchanged_pixels"] == 7
        c0 = s["per_class"][0]
        c1 = s["per_class"][1]
        assert c0["gross_loss_pixels"] == 1
        assert c0["net_change_pixels"] == -1
        assert c1["gross_gain_pixels"] == 1
        assert c1["net_change_pixels"] == 1
        assert s["changed_area_km2"] > 0

    def test_no_change(self):
        cm = np.diag([5, 5]).astype(np.int64)
        s = cm_mod.change_summary(cm, [0, 1], [116, 39, 117, 40], (2, 5))
        assert s["changed_pixels"] == 0
        assert s["change_fraction"] == 0.0
        for c in s["per_class"]:
            assert c["net_change_pixels"] == 0


class TestSankey:
    def test_links_off_diagonal_only(self):
        cm = np.array([[3, 2], [1, 4]], dtype=np.int64)
        sk = cm_mod.sankey_data(cm, [0, 1])
        vals = {(l["from_class"], l["to_class"]): l["value"] for l in sk["links"]}
        assert vals == {(0, 1): 2, (1, 0): 1}
        # nodes have both sides
        sides = {n["side"] for n in sk["nodes"]}
        assert sides == {"from", "to"}

    def test_no_links_when_stable(self):
        cm = np.diag([5, 5]).astype(np.int64)
        sk = cm_mod.sankey_data(cm, [0, 1])
        assert sk["links"] == []


class TestSyntheticPair:
    def test_shapes_and_classes(self):
        t1, t2, info = cm_mod.generate_synthetic_pair(
            [116, 39, 117, 40], n_classes=5, width=48, height=40)
        assert t1.shape == (40, 48)
        assert t2.shape == (40, 48)
        assert info["n_classes"] == 5

    def test_injected_transition_exact(self):
        t1, t2, info = cm_mod.generate_synthetic_pair(
            [116, 39, 117, 40], n_classes=5, width=64, height=64, seed=3)
        inj = info["injected"]
        assert inj["pixel_count"] > 0
        cm, classes = cm_mod.transition_counts(t1, t2)
        idx = {c: i for i, c in enumerate(classes)}
        # exactly the injected count moved src->dst, and nothing else changed
        assert cm[idx[inj["from_class"]], idx[inj["to_class"]]] == inj["pixel_count"]
        changed = int((t1 != t2).sum())
        assert changed == inj["pixel_count"]
        assert cm.sum() - int(np.trace(cm)) == inj["pixel_count"]

    def test_n_classes_clamped(self):
        _, _, info = cm_mod.generate_synthetic_pair(
            [116, 39, 117, 40], n_classes=9, width=32, height=32)
        assert info["n_classes"] == 5


class TestTransitionCSV:
    def test_csv_written(self, tmp_path):
        cm = np.array([[3, 1], [0, 4]], dtype=np.int64)
        path = str(tmp_path / "tm.csv")
        cm_mod.write_transition_csv(path, cm, [0, 1])
        assert os.path.exists(path)
        import pandas as pd
        df = pd.read_csv(path, index_col=0)
        # 2 classes + col_total row, 2 classes + row_total col
        assert df.shape == (3, 3)


class TestGeoTiffIO:
    def test_int_roundtrip(self, tmp_path):
        arr = np.random.randint(0, 5, (16, 16)).astype(np.int32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "c.tif")
        cm_mod.write_geotiff(path, arr, bbox, dtype="int32", nodata=-1)
        back, rbbox = cm_mod.read_class_raster(path)
        np.testing.assert_array_equal(back, arr)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(cm_mod.UsageError):
            cm_mod.read_class_raster("/nonexistent/none.tif")
