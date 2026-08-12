"""Core algorithm tests for text-to-map-nlp."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestDetectLayer:
    def test_vegetation_keyword(self):
        assert mod.detect_layer("生成北京的植被指数地图") == "ndvi"

    def test_nightlights_keyword(self):
        assert mod.detect_layer("上海夜间灯光分布") == "nightlights"

    def test_elevation_keyword(self):
        assert mod.detect_layer("区域高程地形图") == "elevation"

    def test_water_keyword(self):
        assert mod.detect_layer("湖泊水体提取") == "water"

    def test_temperature_keyword(self):
        assert mod.detect_layer("地表温度反演") == "temperature"

    def test_landcover_keyword(self):
        assert mod.detect_layer("土地利用分类") == "landcover"

    def test_default_when_no_match(self):
        assert mod.detect_layer("随便一张图") == "ndvi"

    def test_english_keyword(self):
        assert mod.detect_layer("show me the elevation DEM") == "elevation"


class TestDetectPlace:
    def test_known_place(self):
        assert mod.detect_place("北京植被") == "北京"
        assert mod.detect_place("Shanghai lights") == "上海"

    def test_unknown_place_none(self):
        assert mod.detect_place("某地植被") is None


class TestParseQuery:
    def test_full_parse(self):
        p = mod.parse_query("上海夜间灯光")
        assert p["layer"] == "nightlights"
        assert p["place"] == "上海"
        assert p["cmap"] == "magma"
        assert "上海" in p["title"]
        assert p["query"] == "上海夜间灯光"

    def test_layer_override(self):
        p = mod.parse_query("任意文本", layer_override="water")
        assert p["layer"] == "water"
        assert p["cmap"] == "Blues"

    def test_empty_query_raises(self):
        with pytest.raises(mod.UsageError):
            mod.parse_query("   ")

    def test_bad_override_raises(self):
        with pytest.raises(mod.UsageError):
            mod.parse_query("文本", layer_override="nope")


class TestSyntheticLayer:
    def test_ndvi_range(self):
        arr = mod.synthetic_layer("ndvi", 64, 64)
        assert arr.shape == (64, 64)
        assert arr.min() >= 0.0 and arr.max() <= 1.0

    def test_elevation_range(self):
        arr = mod.synthetic_layer("elevation", 64, 64)
        assert arr.min() >= 0.0 and arr.max() <= 4000.0

    def test_landcover_integer_classes(self):
        arr = mod.synthetic_layer("landcover", 64, 64)
        uniq = set(np.unique(arr).astype(int).tolist())
        assert uniq.issubset({0, 1, 2, 3, 4})
        assert len(uniq) >= 2  # 至少两个类别斑块

    def test_nightlights_nonnegative(self):
        arr = mod.synthetic_layer("nightlights", 64, 64)
        assert arr.min() >= 0.0

    def test_unknown_layer_raises(self):
        with pytest.raises(mod.UsageError):
            mod.synthetic_layer("bogus", 16, 16)

    def test_all_layers_produce_output(self):
        for layer in mod.LAYER_SPECS:
            arr = mod.synthetic_layer(layer, 32, 32)
            assert arr.shape == (32, 32)
            assert np.isfinite(arr).all()


class TestRenderMap:
    def test_png_written(self, tmp_path):
        arr = np.random.uniform(0, 1, (32, 32)).astype(np.float32)
        out = str(tmp_path / "map.png")
        ret = mod.render_map(arr, [116, 39, 117, 40], "RdYlGn", "测试", out)
        assert os.path.exists(ret)
        assert os.path.getsize(ret) > 1000  # 非空 PNG
        with open(ret, "rb") as f:
            assert f.read(8)[:4] == b"\x89PNG"


class TestBboxGeoJSON:
    def test_polygon_ring(self):
        gj = mod.bbox_to_geojson([116, 39, 117, 40], {"layer": "ndvi"})
        feat = gj["features"][0]
        ring = feat["geometry"]["coordinates"][0]
        assert ring[0] == ring[-1]
        xs = [pt[0] for pt in ring]
        ys = [pt[1] for pt in ring]
        assert min(xs) == 116 and max(xs) == 117
        assert min(ys) == 39 and max(ys) == 40
        assert feat["properties"]["layer"] == "ndvi"


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "layer.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
        np.testing.assert_allclose(rb, bbox, atol=1e-6)

    def test_read_missing_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/x.tif")
