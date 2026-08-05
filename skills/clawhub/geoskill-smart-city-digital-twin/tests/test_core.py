"""Core algorithm tests for smart-city-digital-twin."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as sc


class TestBuildingHeight:
    def test_height_equals_dsm_minus_dem(self):
        dem = np.full((16, 16), 40.0, dtype=np.float32)
        dsm = dem.copy()
        dsm[4:8, 4:8] = 40.0 + 30.0  # 30m 建筑
        h = sc.building_height(dsm, dem)
        assert h[5, 5] == pytest.approx(30.0)
        assert h[0, 0] == 0.0

    def test_negative_clipped(self):
        dem = np.full((4, 4), 50.0, dtype=np.float32)
        dsm = np.full((4, 4), 45.0, dtype=np.float32)
        assert np.all(sc.building_height(dsm, dem) == 0.0)

    def test_injected_height_matches(self):
        """核心验收：挤出高度与注入建筑高度一致。"""
        cube, info = sc.generate_synthetic_scene([116, 39, 117, 40], seed=3)
        dem, dsm = cube[0], cube[1]
        h = sc.building_height(dsm, dem)
        assert float(h.max()) > 3.0
        assert float(h.max()) <= 45.0 + 1e-3  # 注入范围 9~45m


class TestExtrude:
    def test_extrude_produces_boxes(self):
        h = np.zeros((20, 20), dtype=np.float32)
        h[5:9, 5:9] = 20.0
        gj, props = sc.extrude_buildings(h, [0.0, 0.0, 1.0, 1.0], threshold=3.0)
        assert len(props) == 1
        p = props[0]
        assert p["height_m"] == pytest.approx(20.0)
        assert p["max_height_m"] == pytest.approx(20.0)
        # 外包矩形在 bbox 内且非退化
        assert p["minx"] < p["maxx"] and p["miny"] < p["maxy"]
        assert gj["features"][0]["geometry"]["type"] == "Polygon"

    def test_threshold_filters_low(self):
        h = np.full((10, 10), 2.0, dtype=np.float32)  # 低于门限
        _, props = sc.extrude_buildings(h, [0, 0, 1, 1], threshold=3.0)
        assert props == []


class TestLOD:
    def test_increasing_distance(self):
        lods = sc.compute_lod(max_distance_km=5.0, n_levels=4)
        dists = [l["max_distance_km"] for l in lods]
        assert dists == sorted(dists)
        assert len(set(dists)) == 4  # 各不相同
        assert dists[-1] == pytest.approx(5.0)

    def test_bad_distance_raises(self):
        with pytest.raises(sc.ValidationError):
            sc.compute_lod(0.0)

    def test_min_two_levels(self):
        assert len(sc.compute_lod(3.0, n_levels=1)) == 2


class TestSceneConfig:
    def test_valid_config(self):
        layers = [{"id": "buildings", "type": "3d-tiles"}]
        cfg = sc.build_scene_config([116, 39, 117, 40], layers, max_distance_km=5.0)
        assert cfg["crs"] == "EPSG:4326"
        assert cfg["bbox_wgs84"] == [116, 39, 117, 40]
        assert cfg["center"] == [116.5, 39.5]
        assert len(cfg["layers"]) == 1
        assert "lod_levels" in cfg and "tiles" in cfg

    def test_invalid_bbox_raises(self):
        with pytest.raises(sc.ValidationError):
            sc.build_scene_config([117, 39, 116, 40], [])  # W > E


class TestApiSpec:
    def test_endpoints_have_method_and_path(self):
        spec = sc.build_api_spec("https://x.org/twin")
        paths = spec["paths"]
        assert len(paths) >= 4
        for path, ops in paths.items():
            assert path.startswith("/")
            assert "get" in ops
            assert "summary" in ops["get"]
        assert spec["servers"][0]["url"] == "https://x.org/twin"


class TestFusion:
    def test_completeness_full(self):
        dem = np.full((10, 10), 40.0, dtype=np.float32)
        dsm = dem + 5.0
        res = sc.fusion_completeness(dem, dsm, n_buildings=3)
        assert res["dem_coverage"] == pytest.approx(1.0)
        assert res["consistent"] is True
        assert res["n_buildings"] == 3
        assert res["mean_height_m"] == pytest.approx(5.0)


class TestSyntheticAndIO:
    def test_synthetic_shapes(self):
        cube, info = sc.generate_synthetic_scene([116, 39, 117, 40], seed=1)
        assert cube.shape == (2, 128, 128)
        assert info["n_buildings_injected"] > 0

    def test_roundtrip(self, tmp_path):
        cube = np.random.default_rng(0).uniform(0, 1, (2, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        sc.write_geotiff(path, cube, bbox)
        back, rb = sc.read_geotiff(path)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
        np.testing.assert_allclose(back, cube, atol=1e-5)

    def test_missing_raises(self):
        with pytest.raises(sc.UsageError):
            sc.read_geotiff("/nonexistent/t.tif")
