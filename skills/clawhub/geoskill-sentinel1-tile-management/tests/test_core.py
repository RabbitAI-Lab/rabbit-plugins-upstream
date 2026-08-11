"""Core algorithm tests for sentinel1-tile-management."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as s1


class TestLinearToDb:
    def test_known_value(self):
        # σ⁰=0.1 → -10 dB
        db = s1.linear_to_db(np.array([[0.1]], dtype=np.float32))
        np.testing.assert_allclose(db, -10.0, atol=1e-4)

    def test_zero_floor(self):
        db = s1.linear_to_db(np.array([[0.0]], dtype=np.float32), floor=1e-4)
        np.testing.assert_allclose(db, -40.0, atol=1e-3)

    def test_range_reasonable(self):
        rng = np.random.default_rng(0)
        lin = np.power(10.0, rng.uniform(-3, 0, (32, 32)) / 10.0).astype(np.float32)
        db = s1.linear_to_db(lin)
        assert db.min() >= -30.5
        assert db.max() <= 0.5


class TestClip:
    def test_identity_full(self):
        arr = np.arange(100, dtype=np.float32).reshape(10, 10)
        out, bbox = s1.clip_to_bbox(arr, [0, 0, 10, 10], [0, 0, 10, 10])
        assert out.shape == (10, 10)
        np.testing.assert_allclose(bbox, [0, 0, 10, 10], atol=1e-6)

    def test_subwindow(self):
        arr = np.zeros((100, 100), dtype=np.float32)
        arr[40:60, 40:60] = 1.0
        out, bbox = s1.clip_to_bbox(arr, [0, 0, 100, 100], [40, 40, 60, 60])
        assert out.shape[0] == 20
        assert out.shape[1] == 20
        assert out.mean() == pytest.approx(1.0)

    def test_no_overlap_raises(self):
        arr = np.zeros((10, 10), dtype=np.float32)
        with pytest.raises(s1.ValidationError):
            s1.clip_to_bbox(arr, [0, 0, 10, 10], [50, 50, 60, 60])

    def test_multiband(self):
        arr = np.ones((3, 20, 20), dtype=np.float32)
        out, bbox = s1.clip_to_bbox(arr, [0, 0, 20, 20], [5, 5, 15, 15])
        assert out.ndim == 3
        assert out.shape[0] == 3


class TestStats:
    def test_band_statistics(self):
        db = np.array([[-10.0, -20.0], [-15.0, -25.0]], dtype=np.float32)
        st = s1.band_statistics(db)
        assert st["mean_db"] == pytest.approx(-17.5)
        assert st["min_db"] == pytest.approx(-25.0)
        assert st["max_db"] == pytest.approx(-10.0)
        assert st["pixels"] == 4

    def test_db_in_range(self):
        db = np.array([[-10.0, -50.0, 10.0]], dtype=np.float32)
        r = s1.db_in_range(db, -35.0, 5.0)
        # -10 in range; -50 below; 10 above
        assert r["in_range_fraction"] == pytest.approx(1 / 3)
        assert r["below_fraction"] == pytest.approx(1 / 3)
        assert r["above_fraction"] == pytest.approx(1 / 3)


class TestParsePols:
    def test_basic(self):
        assert s1._parse_pols("vv,vh") == ["vv", "vh"]

    def test_dedup(self):
        assert s1._parse_pols("VV, vv") == ["vv"]

    def test_invalid_raises(self):
        with pytest.raises(s1.UsageError):
            s1._parse_pols("vv,xx")

    def test_empty_raises(self):
        with pytest.raises(s1.UsageError):
            s1._parse_pols("  ")


class TestPipeline:
    def test_synthetic_db_in_range(self):
        cube, info = s1.generate_synthetic([116, 39, 117, 40], ["vv", "vh"])
        db, out_bbox, log = s1.process_pipeline(cube, ["vv", "vh"], [116, 39, 117, 40], None)
        assert db.shape[0] == 2
        assert db.min() > -40
        assert db.max() < 5
        # VV 应高于 VH（典型共极化 > 交叉极化）
        assert log["per_pol_statistics"]["vv"]["mean_db"] > log["per_pol_statistics"]["vh"]["mean_db"]

    def test_pipeline_clip(self):
        cube, _ = s1.generate_synthetic([116, 39, 117, 40], ["vv"])
        db, out_bbox, log = s1.process_pipeline(
            cube, ["vv"], [116, 39, 117, 40], [116.4, 39.4, 116.6, 39.6],
        )
        assert db.shape[1] < 128 and db.shape[2] < 128
        assert any(st["step"] == "clip_to_bbox" and not st.get("skipped") for st in log["steps"])

    def test_pol_band_mismatch_raises(self):
        cube = np.ones((1, 8, 8), dtype=np.float32)
        with pytest.raises(s1.ValidationError):
            s1.process_pipeline(cube, ["vv", "vh"], [0, 0, 1, 1], None)

    def test_steps_logged(self):
        cube, _ = s1.generate_synthetic([116, 39, 117, 40], ["vv"])
        _, _, log = s1.process_pipeline(cube, ["vv"], [116, 39, 117, 40], None)
        names = [st["step"] for st in log["steps"]]
        assert "load" in names
        assert "linear_to_db" in names


class TestSynthetic:
    def test_shapes(self):
        cube, info = s1.generate_synthetic([116, 39, 117, 40], ["vv", "vh", "hh"])
        assert cube.shape == (3, 128, 128)
        assert cube.min() > 0  # 线性功率为正

    def test_vv_greater_vh(self):
        cube, info = s1.generate_synthetic([116, 39, 117, 40], ["vv", "vh"], seed=3)
        assert cube[0].mean() > cube[1].mean()


class TestIO:
    def test_roundtrip(self, tmp_path):
        cube = np.random.uniform(0.001, 0.5, (2, 16, 16)).astype(np.float32)
        path = str(tmp_path / "g.tif")
        s1.write_geotiff(path, cube, [116.0, 39.0, 117.0, 40.0])
        back, bbox = s1.read_geotiff(path)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(s1.UsageError):
            s1.read_geotiff("/nonexistent/x.tif")
