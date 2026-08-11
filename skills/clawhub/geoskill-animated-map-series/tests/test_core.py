"""Core algorithm tests for animated-map-series."""
import io
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestUnifiedScale:
    def test_global_endpoints_span_all_periods(self):
        stack = np.zeros((2, 8, 8), dtype=np.float32)
        stack[0] = np.linspace(0, 10, 64).reshape(8, 8)
        stack[1] = np.linspace(100, 110, 64).reshape(8, 8)
        vmin, vmax = mod.unified_scale(stack, method="minmax")
        assert abs(vmin - 0.0) < 1e-3
        assert abs(vmax - 110.0) < 1e-3

    def test_percentile_method(self):
        rng = np.random.default_rng(0)
        stack = rng.uniform(0, 100, (3, 16, 16)).astype(np.float32)
        vmin, vmax = mod.unified_scale(stack, method="percentile", pct=2.0)
        assert vmin > 0.0
        assert vmax < 100.0
        assert vmin < vmax

    def test_constant_stack_guard(self):
        stack = np.full((3, 4, 4), 5.0, dtype=np.float32)
        vmin, vmax = mod.unified_scale(stack)
        assert vmax > vmin

    def test_normalize_frame_known(self):
        frame = np.array([[0, 5], [10, 15]], dtype=np.float32)
        out = mod.normalize_frame(frame, 0.0, 10.0)
        assert out[0, 0] == 0.0
        assert abs(out[0, 1] - 0.5) < 1e-6
        assert out[1, 0] == 1.0
        assert out[1, 1] == 1.0  # 超过 vmax 被裁剪


class TestRender:
    def test_colormap_rgb_shape_dtype(self):
        gray = np.random.uniform(0, 1, (10, 12)).astype(np.float32)
        rgb = mod.colormap_rgb(gray, "viridis")
        assert rgb.shape == (10, 12, 3)
        assert rgb.dtype == np.uint8

    def test_unknown_cmap_raises(self):
        with pytest.raises(mod.UsageError):
            mod.colormap_rgb(np.zeros((2, 2), dtype=np.float32), "bad_cmap")

    def test_render_frame_png_magic(self):
        gray = np.random.uniform(0, 1, (8, 8)).astype(np.float32)
        png = mod.render_frame_png(gray, "viridis", "t=1/3", 0.0, 1.0)
        assert png[:8] == b"\x89PNG\r\n\x1a\n"

    def test_comparable_frames_same_value_same_color(self):
        # 统一色标：两帧中值=0.5 的像元颜色应一致（可比性）
        f1 = np.full((4, 4), 0.5, dtype=np.float32)
        f2 = np.full((4, 4), 0.5, dtype=np.float32)
        c1 = mod.colormap_rgb(f1, "plasma")[0, 0]
        c2 = mod.colormap_rgb(f2, "plasma")[0, 0]
        assert np.array_equal(c1, c2)


class TestGif:
    def test_gif_magic_and_frames(self):
        frames = []
        for v in (10, 120, 230):
            gray = np.full((6, 6), v / 255.0, dtype=np.float32)
            frames.append(mod.render_frame_png(gray, "gray", "x", 0, 1))
        gif = mod.compose_gif(frames, duration_ms=100)
        assert gif[:4] == b"GIF8"
        from PIL import Image
        assert Image.open(io.BytesIO(gif)).n_frames == 3

    def test_compose_gif_empty_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.compose_gif([])


class TestSynthetic:
    def test_periods_and_shape(self):
        stack, info = mod.generate_synthetic([116, 39, 117, 40], periods=8)
        assert stack.shape == (8, 64, 64)
        assert info["periods"] == 8
        assert len(info["mean_per_period"]) == 8

    def test_ndvi_range(self):
        stack, _ = mod.generate_synthetic([116, 39, 117, 40], periods=6)
        assert stack.min() >= 0.0
        assert stack.max() <= 1.0

    def test_invalid_periods_raises(self):
        with pytest.raises(mod.UsageError):
            mod.generate_synthetic([116, 39, 117, 40], periods=0)


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (4, 12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "s.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        assert back.shape == arr.shape
        np.testing.assert_allclose(rb, bbox, atol=1e-6)
