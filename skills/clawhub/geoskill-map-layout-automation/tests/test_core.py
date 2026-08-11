"""Core algorithm tests for map-layout-automation."""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestCartographicMath:
    def test_meters_per_degree_lon_equator(self):
        assert abs(mod.meters_per_degree_lon(0.0) - 111320.0) < 1.0

    def test_meters_per_degree_lon_60(self):
        # 60°N：cos(60)=0.5 → 约 55660 m/°
        assert abs(mod.meters_per_degree_lon(60.0) - 111320.0 * 0.5) < 1.0

    def test_nice_round_km_sequence(self):
        assert mod.nice_round_km(27.8) == 20.0
        assert mod.nice_round_km(7.3) == 5.0
        assert mod.nice_round_km(1.2) == 1.0
        assert mod.nice_round_km(0.3) == 0.5  # 小于 0.5 也返回 0.5
        assert mod.nice_round_km(120.0) == 100.0
        assert mod.nice_round_km(50.0) == 50.0

    def test_nice_round_km_invalid(self):
        with pytest.raises(mod.UsageError):
            mod.nice_round_km(0.0)

    def test_scale_bar_km_known(self):
        # 赤道 1° 宽图幅 → 宽 ≈111.32 km；fraction 0.25 → 目标 27.8 → 圆整 20
        bbox = [0.0, 0.0, 1.0, 1.0]
        bar, width = mod.scale_bar_km(bbox, fraction=0.25)
        assert abs(width - 111.32) < 0.1
        assert bar == 20.0

    def test_scale_bar_invalid_fraction(self):
        with pytest.raises(mod.UsageError):
            mod.scale_bar_km([0, 0, 1, 1], fraction=0.0)

    def test_scale_bar_high_latitude_shorter(self):
        # 同样 1° 宽，60°N 处图幅更窄 → 比例尺条更短
        _, w_eq = mod.scale_bar_km([0, 0, 1, 1])
        _, w_60 = mod.scale_bar_km([0, 60, 1, 61])
        assert w_60 < w_eq


class TestDrawingElements:
    def _ax(self):
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.set_xlim(0, 1); ax.set_ylim(0, 1)
        return fig, ax

    def test_scale_bar_adds_patches(self):
        fig, ax = self._ax()
        before = len(ax.patches)
        mod.draw_scale_bar(ax, [0.0, 0.0, 1.0, 1.0], bar_km=20.0)
        assert len(ax.patches) == before + 2  # 黑白两段

    def test_north_arrow_adds_annotation(self):
        fig, ax = self._ax()
        mod.draw_north_arrow(ax, [0.0, 0.0, 1.0, 1.0])
        # 指北针含 "N" 标注（annotate 箭头 + text N）
        labels = [t.get_text() for t in ax.texts]
        assert "N" in labels


class TestComposeLayout:
    def test_compose_and_save(self, tmp_path):
        dem = np.random.uniform(0, 500, (32, 32)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        bar_km, _ = mod.scale_bar_km(bbox)
        fig = mod.compose_layout(dem, bbox, "Test Map", "terrain", bar_km)
        png = str(tmp_path / "l.png"); pdf = str(tmp_path / "l.pdf")
        fig.savefig(png); fig.savefig(pdf, format="pdf")
        with open(png, "rb") as f:
            assert f.read(8) == b"\x89PNG\r\n\x1a\n"
        with open(pdf, "rb") as f:
            assert f.read(4) == b"%PDF"
        # 图上有标题
        ax = fig.axes[0]
        assert ax.get_title() == "Test Map"

    def test_compose_optional_elements(self):
        dem = np.random.uniform(0, 1, (16, 16)).astype(np.float32)
        bbox = [0.0, 0.0, 1.0, 1.0]
        fig_full = mod.compose_layout(dem, bbox, "T", "gray", 20.0)
        fig_bare = mod.compose_layout(dem, bbox, "T", "gray", 20.0,
                                      show_scalebar=False, show_north=False,
                                      show_legend=False)
        # 完整版有更多 artist（colorbar + patches + texts）
        n_full = len(fig_full.axes[0].patches) + len(fig_full.axes[0].texts)
        n_bare = len(fig_bare.axes[0].patches) + len(fig_bare.axes[0].texts)
        assert n_full > n_bare
        assert len(fig_full.axes) == 2  # 主图 + colorbar
        assert len(fig_bare.axes) == 1

    def test_unknown_cmap_raises(self):
        with pytest.raises(mod.UsageError):
            mod.compose_layout(np.zeros((4, 4)), [0, 0, 1, 1], "T", "bogus", 10.0)


class TestSynthetic:
    def test_shape(self):
        dem, info = mod.generate_synthetic([116, 39, 117, 40])
        assert dem.shape == (128, 128)
        assert info["max_elev"] > info["min_elev"]


class TestGeoTiffIO:
    def test_roundtrip(self, tmp_path):
        arr = np.random.uniform(0, 1, (12, 12)).astype(np.float32)
        bbox = [116.0, 39.0, 117.0, 40.0]
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, bbox)
        back, rb = mod.read_geotiff(path)
        np.testing.assert_allclose(back[0], arr, atol=1e-5)
