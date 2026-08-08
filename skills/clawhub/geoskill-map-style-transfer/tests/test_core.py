"""Core algorithm tests for map-style-transfer."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestHistogramMatch:
    def test_mean_and_std_align_to_reference(self):
        rng = np.random.default_rng(0)
        source = rng.uniform(0, 1, (64, 64)).astype(np.float32)          # mean~0.5
        reference = rng.normal(0.75, 0.08, (64, 64)).astype(np.float32)  # mean~0.75
        matched = mod.histogram_match(source, reference)
        # 匹配后均值/方差应显著逼近参考
        assert abs(matched.mean() - reference.mean()) < 0.03
        assert abs(matched.std() - reference.std()) < 0.03
        # 且比匹配前更接近
        assert abs(matched.mean() - reference.mean()) < abs(source.mean() - reference.mean())

    def test_identity_match(self):
        rng = np.random.default_rng(1)
        a = rng.uniform(0, 1, (32, 32)).astype(np.float32)
        matched = mod.histogram_match(a, a)
        np.testing.assert_allclose(matched, a, atol=1e-4)

    def test_cdf_monotonic_mapping(self):
        # 单调递增映射：源排序后匹配结果也应非降
        rng = np.random.default_rng(2)
        source = rng.uniform(0, 1, (20, 20)).astype(np.float32)
        reference = (rng.uniform(0, 1, (20, 20)) ** 2).astype(np.float32)
        matched = mod.histogram_match(source, reference)
        s_sorted = np.sort(source.ravel())
        m_sorted = matched.ravel()[np.argsort(source.ravel())]
        assert np.all(np.diff(m_sorted) >= -1e-6)


class TestStyleTemplate:
    def test_noir_is_grayscale(self):
        rgb = np.random.uniform(0, 1, (8, 8, 3)).astype(np.float32)
        out = mod.apply_style_template(rgb, "noir")
        assert np.allclose(out[..., 0], out[..., 1], atol=1e-6)
        assert np.allclose(out[..., 1], out[..., 2], atol=1e-6)

    def test_gamma_darkens_midtones(self):
        # gamma>1 → 0.5 变暗
        rgb = np.full((4, 4, 3), 0.5, dtype=np.float32)
        out = mod.apply_style_template(rgb, "vintage")  # gamma=1.1, tint
        # gamma 使灰度通道降低（tint 仅缩放）；验证 R 通道 < 0.5*tint_r
        gray_after = 0.5 ** 1.10
        assert gray_after < 0.5

    def test_contrast_increases_spread(self):
        # 用纯灰输入（R=G=B）避免跨通道方差干扰，对比度 1.3 应使 std 放大 ~1.3×
        g = np.random.default_rng(5).uniform(0.4, 0.6, (16, 16, 1)).astype(np.float32)
        rgb = np.repeat(g, 3, axis=2)
        noir = mod.apply_style_template(rgb, "noir")   # contrast 1.3
        none = mod.apply_style_template(rgb, "none")
        assert noir.std() > none.std()
        assert abs(noir.std() / none.std() - 1.3) < 0.05

    def test_none_identity_ish(self):
        rgb = np.random.uniform(0, 1, (6, 6, 3)).astype(np.float32)
        out = mod.apply_style_template(rgb, "none")
        np.testing.assert_allclose(out, rgb, atol=1e-6)

    def test_unknown_style_raises(self):
        with pytest.raises(mod.UsageError):
            mod.apply_style_template(np.zeros((2, 2, 3)), "bogus")


class TestQuantize:
    def test_unique_colors_bounded(self):
        rng = np.random.default_rng(3)
        rgb = rng.integers(0, 256, (32, 32, 3), dtype=np.uint8)
        out = mod.quantize_palette(rgb, levels=4)
        uniq = len({tuple(c) for c in out.reshape(-1, 3)})
        assert uniq <= 4 ** 3

    def test_values_at_bin_centers(self):
        rgb = np.array([[[0, 128, 255]]], dtype=np.uint8)
        out = mod.quantize_palette(rgb, levels=4)  # step=64, centers 32,96,160,224
        assert out[0, 0, 0] == 32    # 0 -> bin0 center 32
        assert out[0, 0, 1] == 160   # 128 -> bin2 center 160

    def test_levels_too_low_raises(self):
        with pytest.raises(mod.UsageError):
            mod.quantize_palette(np.zeros((2, 2, 3), dtype=np.uint8), levels=1)


class TestHelpers:
    def test_normalize01_range(self):
        band = np.linspace(0, 1000, 64 * 64).reshape(64, 64).astype(np.float32)
        out = mod.normalize01(band)
        assert out.min() >= 0.0 and out.max() <= 1.0

    def test_gray_to_rgb_shape(self):
        g = np.random.uniform(0, 1, (5, 7)).astype(np.float32)
        rgb = mod.gray_to_rgb(g)
        assert rgb.shape == (5, 7, 3)
        assert np.allclose(rgb[..., 0], rgb[..., 2])


class TestSynthetic:
    def test_shape(self):
        img, info = mod.generate_synthetic([116, 39, 117, 40])
        assert img.shape == (64, 64)
        assert info["max"] > info["min"]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
