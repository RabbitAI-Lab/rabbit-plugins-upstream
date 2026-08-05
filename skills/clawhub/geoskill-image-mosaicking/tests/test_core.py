"""Core algorithm tests for image-mosaicking."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestMosaic:
    def test_reconstruct_from_overlapping_crops(self):
        """两幅来自同一影像的重叠瓦片，镶嵌后应精确还原原图（重叠值相同）。"""
        rng = np.random.default_rng(0)
        truth = rng.uniform(0.1, 0.8, (3, 40, 60)).astype(np.float32)
        left = truth[:, :, 0:35].copy()
        right = truth[:, :, 25:60].copy()
        for method in ("average", "feather"):
            out = mod.mosaic([left, right], [(0, 0), (0, 25)], (40, 60), method=method)
            assert out.shape == truth.shape
            assert np.isfinite(out).all()
            np.testing.assert_allclose(out, truth, atol=1e-4)

    def test_average_of_constant_tiles(self):
        # left covers cols 0..14, right covers cols 5..19 (overlap 5..14)
        left = np.full((1, 10, 15), 0.3, dtype=np.float32)
        right = np.full((1, 10, 15), 0.3, dtype=np.float32)
        out = mod.mosaic([left, right], [(0, 0), (0, 5)], (10, 20), method="average")
        assert np.isfinite(out).all()
        np.testing.assert_allclose(out, 0.3, atol=1e-6)

    def test_feather_weight_interior_higher(self):
        w = mod._feather_weight(11, 11)
        # 中心权重最大，边缘为 1
        assert w[5, 5] == w.max()
        assert w[0, 0] == 1.0
        assert w[5, 5] > w[0, 5]

    def test_uncovered_pixel_is_nan(self):
        tile = np.full((1, 5, 5), 0.5, dtype=np.float32)
        out = mod.mosaic([tile], [(0, 0)], (10, 10), method="average")
        assert np.isfinite(out[0, 0, 0])
        assert np.isnan(out[0, 9, 9])

    def test_tile_out_of_canvas_raises(self):
        tile = np.ones((1, 5, 5), dtype=np.float32)
        with pytest.raises(mod.ValidationError):
            mod.mosaic([tile], [(8, 8)], (10, 10))

    def test_no_tiles_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.mosaic([], [], (10, 10))

    def test_bad_method_raises(self):
        tile = np.ones((1, 5, 5), dtype=np.float32)
        with pytest.raises(mod.UsageError):
            mod.mosaic([tile], [(0, 0)], (5, 5), method="bogus")


class TestSynthetic:
    def test_synthetic_shapes_and_overlap(self):
        tiles, offsets, canvas_shape, info = mod.generate_synthetic([116, 39, 117, 40])
        assert len(tiles) == 2
        assert canvas_shape == (128, 128)
        assert info["overlap_cols"] == 32
        # 两幅瓦片拼起来应覆盖整个画布宽度
        assert offsets[0][1] == 0
        assert offsets[1][1] + tiles[1].shape[2] == 128

    def test_synthetic_mosaic_recovers_truth(self):
        tiles, offsets, canvas_shape, info = mod.generate_synthetic([116, 39, 117, 40], seed=7)
        truth = info["_truth"]
        out = mod.mosaic(tiles, offsets, canvas_shape, method="feather")
        np.testing.assert_allclose(out, truth, atol=1e-4)


class TestGeoTiffIO:
    def test_write_and_read_roundtrip(self, tmp_path):
        cube = np.random.uniform(0, 1, (3, 16, 16)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "test.tif")
        mod.write_geotiff(path, cube, bbox)
        assert os.path.exists(path)
        read_back, read_bbox = mod.read_geotiff(path)
        assert read_back.shape == cube.shape
        np.testing.assert_allclose(read_bbox, bbox, atol=1e-6)
        np.testing.assert_allclose(read_back, cube, atol=1e-5)

    def test_read_missing_file_raises(self):
        with pytest.raises(mod.UsageError):
            mod.read_geotiff("/nonexistent/path/file.tif")
