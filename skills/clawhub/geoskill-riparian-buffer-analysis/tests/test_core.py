"""Core algorithm tests for riparian-buffer-analysis."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as rb

# 小区域（约 2-3 km）使 30-200 m 缓冲带跨越多个像元
SMALL_BBOX = [116.0, 39.0, 116.03, 39.03]


class TestFlowAndRiver:
    def test_accumulation_min_one(self):
        dem = np.random.default_rng(0).normal(100, 5, (24, 24))
        acc = rb.d8_flow_accumulation(dem, 10.0)
        assert acc.min() >= 1.0

    def test_river_mask_threshold(self):
        acc = np.array([[1, 10, 100], [5, 60, 200]], dtype=float)
        mask = rb.extract_river_mask(acc, threshold=50)
        assert mask.tolist() == [[False, False, True], [False, True, True]]

    def test_river_threshold_too_low_raises(self):
        with pytest.raises(rb.UsageError):
            rb.extract_river_mask(np.ones((3, 3)), threshold=1)


class TestUTM:
    def test_beijing_north(self):
        epsg = rb.utm_epsg_for_bbox([116.0, 39.0, 117.0, 40.0])
        assert epsg == 32650  # 北京位于 UTM 50N

    def test_south_hemisphere(self):
        epsg = rb.utm_epsg_for_bbox([150.0, -34.0, 151.0, -33.0])
        assert epsg == 32756  # 南半球


class TestBuffers:
    def _river_geom(self):
        layers, info = rb.generate_synthetic(SMALL_BBOX, width=96, height=96, seed=1)
        acc = rb.d8_flow_accumulation(layers["dem"], info["cellsize_m"])
        mask = rb.extract_river_mask(acc, threshold=30)
        return rb.river_geometry(mask, SMALL_BBOX)

    def test_area_increases_with_distance(self):
        geom = self._river_geom()
        assert geom is not None
        buffers, areas, epsg = rb.make_buffers(geom, [30, 50, 100, 200], SMALL_BBOX)
        vals = [areas[d] for d in [30, 50, 100, 200]]
        assert vals[0] < vals[1] < vals[2] < vals[3]
        assert all(a > 0 for a in vals)

    def test_buffer_returns_4326(self):
        geom = self._river_geom()
        buffers, areas, epsg = rb.make_buffers(geom, [50], SMALL_BBOX)
        assert buffers[50.0].crs.to_epsg() == 4326


class TestIntegrityScore:
    def test_vegetated_high(self):
        fracs = {"water": 0.0, "vegetation": 0.8, "cropland": 0.1,
                 "built_up": 0.05, "bare": 0.05, "other": 0.0}
        score, level = rb.integrity_score(fracs)
        assert level == "high"
        assert score > 0.6

    def test_built_up_low(self):
        fracs = {"water": 0.0, "vegetation": 0.1, "cropland": 0.0,
                 "built_up": 0.9, "bare": 0.0, "other": 0.0}
        score, level = rb.integrity_score(fracs)
        assert level == "low"
        assert score < 0.3

    def test_water_excluded(self):
        # 50% 水 + 50% 植被 → 陆地全为植被 → 高分
        fracs = {"water": 0.5, "vegetation": 0.5, "cropland": 0.0,
                 "built_up": 0.0, "bare": 0.0, "other": 0.0}
        score, level = rb.integrity_score(fracs)
        assert score == pytest.approx(1.0)


class TestLulcStats:
    def test_fractions_sum_to_one(self):
        layers, info = rb.generate_synthetic(SMALL_BBOX, width=96, height=96, seed=2)
        acc = rb.d8_flow_accumulation(layers["dem"], info["cellsize_m"])
        mask = rb.extract_river_mask(acc, threshold=30)
        geom = rb.river_geometry(mask, SMALL_BBOX)
        buffers, areas, epsg = rb.make_buffers(geom, [100], SMALL_BBOX)
        stats = rb.lulc_stats_in_buffer(layers["lulc"], buffers[100.0], SMALL_BBOX)
        total_frac = sum(stats["fractions"].values())
        assert total_frac == pytest.approx(1.0, abs=1e-3)
        assert stats["cell_count"] > 0
        # 河道附近应有植被与水体
        assert stats["fractions"]["vegetation"] > 0


class TestEndToEnd:
    def test_full_pipeline(self):
        layers, info = rb.generate_synthetic(SMALL_BBOX, width=96, height=96, seed=3)
        result = rb.run_model(
            layers["dem"], layers["lulc"], info["cellsize_m"], SMALL_BBOX,
            river_threshold=30, buffer_distances=[30, 50, 100, 200],
        )
        assert result["n_river_cells"] > 0
        assert result["area_monotonic"] is True
        assert len(result["buffers"]) == 4
        assert len(result["features"]) >= 4
        # 每个缓冲带都有完整性评分
        for b in result["buffers"]:
            assert 0.0 <= b["integrity_score"] <= 1.0
            assert b["integrity_level"] in ("low", "medium", "high")

    def test_composition_changes_with_width(self):
        """缓冲带越宽：水体占比下降（河道在中心），外围建设用地被纳入。"""
        layers, info = rb.generate_synthetic(SMALL_BBOX, width=96, height=96, seed=4)
        result = rb.run_model(
            layers["dem"], layers["lulc"], info["cellsize_m"], SMALL_BBOX,
            river_threshold=30, buffer_distances=[50, 2000],
        )
        narrow = next(b for b in result["buffers"] if b["buffer_distance_m"] == 50)
        wide = next(b for b in result["buffers"] if b["buffer_distance_m"] == 2000)
        # 水体集中在河道中心，宽缓冲带稀释 → 水占比下降
        assert narrow["fractions"]["water"] > wide["fractions"]["water"]
        # 建设用地在外围，窄缓冲带够不到，宽缓冲带纳入
        assert wide["fractions"]["built_up"] > narrow["fractions"]["built_up"]
        assert narrow["fractions"]["built_up"] == pytest.approx(0.0, abs=1e-6)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 100, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "x.tif")
        rb.write_geotiff(path, arr, bbox)
        back, rbbox, cs = rb.read_geotiff(path)
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)
        np.testing.assert_allclose(back[0], arr, atol=1e-4)
        assert cs > 0

    def test_read_missing_raises(self):
        with pytest.raises(rb.UsageError):
            rb.read_geotiff("/nonexistent/x.tif")
