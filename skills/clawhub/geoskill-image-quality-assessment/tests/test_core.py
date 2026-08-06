"""Core algorithm tests for image-quality-assessment."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestSNR:
    def test_constant_high_snr(self):
        band = np.full((32, 32), 0.5, dtype=np.float32)
        # std~0 → inf
        assert mod.compute_snr(band) == float("inf")

    def test_noisy_lower_snr(self):
        rng = np.random.default_rng(0)
        clean = np.full((64, 64), 0.5)
        noisy = clean + rng.normal(0, 0.1, (64, 64))
        assert mod.compute_snr(noisy.astype(np.float32)) < mod.compute_snr(clean.astype(np.float32))

    def test_snr_positive(self):
        rng = np.random.default_rng(1)
        band = (0.3 + rng.normal(0, 0.02, (32, 32))).astype(np.float32)
        assert mod.compute_snr(band) > 0


class TestStriping:
    def test_uniform_low_striping(self):
        rng = np.random.default_rng(2)
        band = rng.normal(0.3, 0.05, (64, 64)).astype(np.float32)
        assert mod.compute_striping(band) < 0.2

    def test_striped_high(self):
        rng = np.random.default_rng(3)
        band = np.full((64, 64), 0.3)
        offsets = rng.normal(0, 0.3, 64)
        band = (band + offsets[np.newaxis, :]).astype(np.float32)
        assert mod.compute_striping(band) > 0.3


class TestDeadLines:
    def test_no_dead_lines(self):
        rng = np.random.default_rng(4)
        band = rng.normal(0.3, 0.05, (32, 32)).astype(np.float32)
        assert mod.compute_dead_lines(band) < 0.05

    def test_dead_column_detected(self):
        rng = np.random.default_rng(5)
        band = rng.normal(0.3, 0.05, (32, 32)).astype(np.float32)
        band[:, 10] = 0.0  # constant column
        band[:, 20] = 0.0
        frac = mod.compute_dead_lines(band)
        assert frac >= 2 / (32 + 32)


class TestCloudCover:
    def test_no_clouds(self):
        band = np.full((32, 32), 0.2, dtype=np.float32)
        assert mod.compute_cloud_cover(band, threshold=0.6) == 0.0

    def test_all_clouds(self):
        band = np.full((32, 32), 0.9, dtype=np.float32)
        assert mod.compute_cloud_cover(band, threshold=0.6) == 1.0

    def test_partial_clouds(self):
        band = np.full((10, 10), 0.2, dtype=np.float32)
        band[:5, :] = 0.9
        assert abs(mod.compute_cloud_cover(band, threshold=0.6) - 0.5) < 1e-6


class TestSharpness:
    def test_sharp_higher_than_blurred(self):
        rng = np.random.default_rng(6)
        sharp = rng.normal(0.3, 0.1, (64, 64)).astype(np.float32)
        from scipy.ndimage import gaussian_filter
        blurred = gaussian_filter(sharp, sigma=3).astype(np.float32)
        assert mod.compute_sharpness(sharp) > mod.compute_sharpness(blurred)


class TestAssessQuality:
    def test_all_metrics_keys(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.assess_quality(cube, mod.ALL_METRICS)
        assert "n_bands" in res
        assert "summary" in res
        assert "overall_score" in res
        assert "per_band" in res
        s = res["summary"]
        for k in ("mean_snr", "mean_striping", "mean_dead_lines",
                  "mean_cloud_cover", "mean_sharpness"):
            assert k in s

    def test_score_in_range(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.assess_quality(cube, mod.ALL_METRICS)
        assert 0.0 <= res["overall_score"] <= 100.0

    def test_subset_metrics(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.assess_quality(cube, ["snr", "cloud"])
        assert "mean_snr" in res["summary"]
        assert "mean_cloud_cover" in res["summary"]
        assert "mean_sharpness" not in res["summary"]


class TestComputeScore:
    def test_clean_better_than_defective(self):
        clean, _ = mod.generate_synthetic([116, 39, 117, 40], noise_level=0.005,
                                          cloud_fraction=0.0, stripe_strength=0.0)
        defective, _ = mod.generate_synthetic([116, 39, 117, 40], noise_level=0.1,
                                              cloud_fraction=0.4, stripe_strength=0.3,
                                              n_dead_cols=10, blur_sigma=2.0)
        sc = mod.assess_quality(clean, mod.ALL_METRICS)["overall_score"]
        sd = mod.assess_quality(defective, mod.ALL_METRICS)["overall_score"]
        assert sc > sd


class TestSynthetic:
    def test_shape(self):
        cube, info = mod.generate_synthetic([116, 39, 117, 40], width=64, height=48)
        assert cube.shape == (4, 48, 64)

    def test_deterministic(self):
        c1, _ = mod.generate_synthetic([116, 39, 117, 40], seed=99)
        c2, _ = mod.generate_synthetic([116, 39, 117, 40], seed=99)
        np.testing.assert_array_equal(c1, c2)

    def test_cloud_injection(self):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40], cloud_fraction=0.5)
        cc = mod.compute_cloud_cover(cube[0], threshold=0.6)
        assert cc > 0.3


class TestHTMLReport:
    def test_writes_file(self, tmp_path):
        cube, _ = mod.generate_synthetic([116, 39, 117, 40])
        res = mod.assess_quality(cube, mod.ALL_METRICS)
        path = str(tmp_path / "report.html")
        mod.write_html_report(path, res, "synthetic")
        assert os.path.exists(path)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        assert "Image Quality Report" in content
        assert "Overall Score" in content
