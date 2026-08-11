"""Core algorithm tests for cloud-removal-gapfilling."""
import sys
import os

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestComposite:
    def test_median_fills_clouded_pixel(self):
        scenes = np.full((5, 1, 4, 4), 0.2, dtype=np.float32)
        scenes[0, 0, 0, 0] = np.nan
        scenes[1, 0, 0, 0] = np.nan
        comp = mod.composite_scenes(scenes, method="median")
        assert comp.shape == (1, 4, 4)
        np.testing.assert_allclose(comp[0, 0, 0], 0.2, atol=1e-5)

    def test_median_robust_to_bright_outliers(self):
        """Finite bright 'cloud' outliers are rejected by the median."""
        scenes = np.full((5, 1, 1, 1), 0.2, dtype=np.float32)
        scenes[3, 0, 0, 0] = 0.95
        scenes[4, 0, 0, 0] = 0.98
        comp = mod.composite_scenes(scenes, method="median")
        assert abs(float(comp[0, 0, 0]) - 0.2) < 1e-5

    def test_percentile_value(self):
        scenes = np.array([0.1, 0.2, 0.3, 0.4, 0.5], dtype=np.float32)
        scenes = scenes.reshape(5, 1, 1, 1)
        comp50 = mod.composite_scenes(scenes, method="percentile", percentile=50.0)
        comp0 = mod.composite_scenes(scenes, method="percentile", percentile=0.0)
        np.testing.assert_allclose(comp50[0, 0, 0], 0.3, atol=1e-5)
        np.testing.assert_allclose(comp0[0, 0, 0], 0.1, atol=1e-5)

    def test_full_gap_stays_nan(self):
        scenes = np.full((3, 1, 2, 2), 0.3, dtype=np.float32)
        scenes[:, 0, 1, 1] = np.nan
        comp = mod.composite_scenes(scenes)
        assert np.isnan(comp[0, 1, 1])
        assert np.isfinite(comp[0, 0, 0])

    def test_bad_method_raises(self):
        scenes = np.ones((2, 1, 4, 4), dtype=np.float32)
        with pytest.raises(mod.UsageError):
            mod.composite_scenes(scenes, method="bogus")

    def test_bad_ndim_raises(self):
        with pytest.raises(mod.ValidationError):
            mod.composite_scenes(np.ones((3, 4, 4), dtype=np.float32))


class TestCloudStats:
    def test_per_scene_fraction(self):
        scenes = np.full((4, 1, 10, 10), 0.2, dtype=np.float32)
        scenes[0, 0, :5, :5] = np.nan  # 25 / 100 pixels
        stats = mod.cloud_coverage_stats(scenes)
        assert abs(stats["per_scene_cloud_fraction"][0] - 0.25) < 1e-6
        assert stats["per_scene_cloud_fraction"][1] == 0.0
        assert stats["full_gap_fraction"] == 0.0

    def test_full_gap_fraction(self):
        scenes = np.full((3, 1, 4, 4), 0.2, dtype=np.float32)
        scenes[:, 0, 0, 0] = np.nan
        stats = mod.cloud_coverage_stats(scenes)
        assert abs(stats["full_gap_fraction"] - 1.0 / 16.0) < 1e-6
        assert stats["n_scenes"] == 3


class TestSynthetic:
    def test_shape_and_clouds(self):
        scenes, info = mod.generate_synthetic_scenes([116, 39, 117, 40], n_scenes=5, bands=4)
        assert scenes.shape == (5, 4, 128, 128)
        assert np.isnan(scenes).any()
        assert info["n_scenes"] == 5

    def test_composite_recovers_surface(self):
        scenes, info = mod.generate_synthetic_scenes(
            [116, 39, 117, 40], n_scenes=6, seed=7,
        )
        comp = mod.composite_scenes(scenes, method="median")
        stats = mod.cloud_coverage_stats(scenes)
        assert stats["full_gap_fraction"] < 0.02
        assert float(np.isfinite(comp).mean()) > 0.98
        # composite mean should be a sane reflectance-like value
        mean_val = float(np.nanmean(comp))
        assert 0.05 < mean_val < 0.9


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
