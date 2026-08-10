"""Core algorithm tests for sar-urban-mapping."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as um


class TestOtsu:
    def test_bimodal_separates(self):
        rng = np.random.default_rng(0)
        low = rng.normal(10, 1, 5000)
        high = rng.normal(100, 1, 5000)
        data = np.concatenate([low, high]).astype(np.float32)
        thr = um.otsu_threshold(data)
        assert 30 < thr < 80

    def test_constant_returns_value(self):
        data = np.full(100, 5.0, dtype=np.float32)
        thr = um.otsu_threshold(data)
        assert thr == pytest.approx(5.0)

    def test_empty_returns_zero(self):
        data = np.full(10, np.nan, dtype=np.float32)
        assert um.otsu_threshold(data) == 0.0


class TestGlcmContrast:
    def test_uniform_low_contrast(self):
        flat = np.full((32, 32), 128.0, dtype=np.float32)
        c = um.glcm_contrast(flat)
        assert c.max() == pytest.approx(0.0)

    def test_checkerboard_high_contrast(self):
        yy, xx = np.mgrid[0:32, 0:32]
        check = (((yy + xx) % 2) * 255).astype(np.float32)
        c_check = um.glcm_contrast(check)
        flat = np.full((32, 32), 128.0, dtype=np.float32)
        c_flat = um.glcm_contrast(flat)
        assert c_check.mean() > c_flat.mean() + 1.0

    def test_shape_preserved(self):
        arr = np.random.uniform(0, 255, (20, 30)).astype(np.float32)
        c = um.glcm_contrast(arr)
        assert c.shape == arr.shape


class TestMorphology:
    def test_fills_hole(self):
        mask = np.zeros((21, 21), dtype=np.uint8)
        mask[3:18, 3:18] = 1
        mask[9:12, 9:12] = 0  # 内部空洞
        closed = um.morphology_close(mask, size=5)
        # 空洞被填充
        assert closed[10, 10] == 1


class TestExtractUrban:
    def test_detects_bright_block(self):
        sigma0 = np.full((64, 64), 0.02, dtype=np.float32)
        sigma0[20:40, 20:40] = 0.5
        mask, params = um.extract_urban(sigma0, threshold="auto", use_texture=False)
        # 高亮块大部分被检出
        block_recall = mask[20:40, 20:40].mean()
        assert block_recall > 0.8
        # 背景大部分未检出
        bg = mask.copy()
        bg[20:40, 20:40] = 0
        assert bg.mean() < 0.1
        assert params["threshold_mode"] == "otsu"

    def test_fixed_threshold(self):
        sigma0 = np.full((32, 32), 0.1, dtype=np.float32)
        sigma0[:, 16:] = 0.3
        mask, params = um.extract_urban(sigma0, threshold=0.2, use_texture=False)
        assert params["threshold_mode"] == "fixed"
        # 亮区内部几乎全检出（边界受形态学开运算侵蚀，检查内部）
        assert mask[4:28, 18:28].mean() > 0.9
        # 暗区内部几乎不检出
        assert mask[4:28, 2:14].mean() < 0.1

    def test_bad_threshold_raises(self):
        sigma0 = np.ones((16, 16), dtype=np.float32)
        with pytest.raises(um.UsageError):
            um.extract_urban(sigma0, threshold="not_a_number", use_texture=False)

    def test_texture_suppresses_flat_bright(self):
        """平坦高 σ⁰ 裸土应被纹理门限抑制（相对纯阈值）。"""
        rng = np.random.default_rng(1)
        sigma0 = np.full((64, 64), 0.02, dtype=np.float32)
        sigma0 = sigma0 * np.exp(rng.normal(0, 0.15, (64, 64))).astype(np.float32)
        # 平坦高值裸土块（无纹理）
        sigma0[5:20, 5:20] = 0.3
        # 高纹理城市块
        yy, xx = np.mgrid[0:15, 0:15]
        checker = ((yy + xx) % 2).astype(np.float32)
        sigma0[40:55, 40:55] = 0.3 + 0.15 * checker
        mask_tex, _ = um.extract_urban(sigma0, threshold="auto", use_texture=True)
        mask_no, _ = um.extract_urban(sigma0, threshold="auto", use_texture=False)
        # 启用纹理后裸土块检出率下降
        assert mask_tex[5:20, 5:20].mean() < mask_no[5:20, 5:20].mean()


class TestSynthetic:
    def test_shapes(self):
        sigma0, truth, info = um.generate_synthetic([116, 39, 117, 40])
        assert sigma0.shape == (64, 64)
        assert truth.shape == (64, 64)
        assert info["truth_urban_fraction"] > 0

    def test_detection_matches_truth(self):
        """检测城市面积应与注入真值接近（IoU 合理）。"""
        sigma0, truth, info = um.generate_synthetic([116, 39, 117, 40], seed=7)
        mask, _ = um.extract_urban(sigma0, threshold="auto", use_texture=True)
        inter = np.logical_and(mask > 0, truth > 0).sum()
        union = np.logical_or(mask > 0, truth > 0).sum()
        iou = inter / max(union, 1)
        assert iou > 0.5, f"IoU too low: {iou:.3f}"

    def test_positive_sigma0(self):
        sigma0, _, _ = um.generate_synthetic([116, 39, 117, 40])
        assert sigma0.min() >= 0.0


class TestArea:
    def test_pixel_area_positive(self):
        px = um.pixel_area_km2([116, 39, 117, 40], 100, 100)
        # 1° × 1° ≈ 111 × 85 km，100×100 像元 → 每像元 ~0.94 km²
        assert 0.5 < px < 2.0

    def test_statistics_consistent(self):
        mask = np.zeros((10, 10), dtype=np.uint8)
        mask[:5, :] = 1
        stats = um.urban_statistics(mask, [116, 39, 117, 40], {"threshold_linear": 0.05})
        assert stats["urban_fraction"] == pytest.approx(0.5)
        assert stats["urban_pixels"] == 50
        assert stats["urban_area_km2"] > 0
        assert stats["threshold_linear"] == 0.05


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = (np.random.uniform(0, 1, (16, 16)) > 0.5).astype(np.uint8)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "m.tif")
        um.write_geotiff(path, arr, bbox, nodata=255, dtype="uint8")
        back, rbbox = um.read_geotiff(path)
        assert back.shape[1:] == arr.shape
        np.testing.assert_allclose(rbbox, bbox, atol=1e-6)

    def test_missing_raises(self):
        with pytest.raises(um.UsageError):
            um.read_geotiff("/nonexistent/x.tif")
