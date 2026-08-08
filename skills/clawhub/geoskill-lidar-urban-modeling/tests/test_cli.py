"""CLI argument parsing tests for lidar-urban-modeling."""
import json
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


def run_cli(args, timeout=180):
    return subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True, text=True, timeout=timeout,
    )


class TestCLIBasics:
    def test_help(self):
        r = run_cli(["--help"])
        assert r.returncode == 0
        for opt in ("--bbox", "--synthetic", "--min-height",
                    "--ground-method", "--cell-size"):
            assert opt in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """无参数 → UsageError → exit 2。"""
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_ground_method_exit_2(self):
        """非法 choices → argparse error → exit 2。"""
        r = run_cli(["--bbox", "116", "39", "117", "40",
                     "--ground-method", "kriging"])
        assert r.returncode == 2

    def test_input_not_found_exit_2(self):
        """输入文件不存在 → UsageError → exit 2。"""
        r = run_cli(["--input", "does_not_exist_cloud.npy"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        """--synthetic 但没给 --bbox → UsageError → exit 2。"""
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_bbox_only_autosynthetic(self, tmp_path):
        """仅给 bbox（无 --input）→ 自动合成并产出全部产物。"""
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "116", "39", "117", "40",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        for name in ("ndsm.tif", "buildings.geojson",
                     "stats.json", "output-manifest.json"):
            assert os.path.exists(os.path.join(out, name)), name
        with open(os.path.join(out, "stats.json"), encoding="utf-8") as f:
            stats = json.load(f)
        assert stats["n_buildings_detected"] >= 6
        assert stats["detection_rate"] >= 0.8
        assert stats["height_rmse_m"] < 1.0
        with open(os.path.join(out, "output-manifest.json"), encoding="utf-8") as f:
            man = json.load(f)
        assert man["exit_code"] == 0
        assert man["skill"] == "geoskill-lidar-urban-modeling"

    def test_input_npy_run(self, tmp_path):
        """真实输入模式：读 .npy 点云。"""
        points, info = mod.generate_synthetic([116, 39, 117, 40],
                                              seed=21, n_buildings=4)
        cloud = str(tmp_path / "cloud.npy")
        np.save(cloud, points)
        out = str(tmp_path / "out")
        r = run_cli(["--input", cloud, "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "stats.json"), encoding="utf-8") as f:
            stats = json.load(f)
        assert stats["n_buildings_detected"] >= 3
        assert stats["total_volume_m3"] > 0

    def test_percentile_method_run(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--ground-method", "percentile",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "stats.json"), encoding="utf-8") as f:
            stats = json.load(f)
        assert stats["ground_method"] == "percentile"
        assert stats["n_buildings_detected"] >= 6

    def test_high_min_height_zero_buildings(self, tmp_path):
        """min-height 过高 → 0 栋建筑，但仍产出合法空矢量。"""
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--min-height", "200", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "stats.json"), encoding="utf-8") as f:
            stats = json.load(f)
        assert stats["n_buildings_detected"] == 0
        with open(os.path.join(out, "buildings.geojson"), encoding="utf-8") as f:
            doc = json.load(f)
        assert doc["features"] == []
