"""CLI argument parsing tests for sar-flood-mapping."""
import subprocess
import sys
import os
import json

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


def run_cli(args, timeout=120):
    return subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True, text=True, timeout=timeout,
    )


class TestCLIBasics:
    def test_help(self):
        r = run_cli(["--help"])
        assert r.returncode == 0
        assert "--bbox" in r.stdout
        assert "--synthetic" in r.stdout
        assert "--threshold" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_threshold_exit_2(self):
        """Invalid threshold value → UsageError → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--threshold", "bogus"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        """Non-existent input file → UsageError → exit 2."""
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        """--synthetic without --bbox → UsageError → exit 2."""
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_auto_threshold(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--threshold", "auto",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "flood_extent.tif"))
        assert os.path.exists(os.path.join(out, "flood_area_stats.json"))
        assert os.path.exists(os.path.join(out, "flood_extent.geojson"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
        with open(os.path.join(out, "flood_area_stats.json"), encoding="utf-8") as f:
            stats = json.load(f)
        assert stats["threshold_mode"] == "auto_otsu"
        assert stats["water_fraction"] > 0

    def test_synthetic_manual_threshold(self, tmp_path):
        out = str(tmp_path / "out_m")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--threshold", "0.01",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "flood_area_stats.json"), encoding="utf-8") as f:
            stats = json.load(f)
        assert stats["threshold_mode"] == "manual"
        assert abs(stats["threshold_used"] - 0.01) < 1e-9

    def test_detection_matches_truth(self, tmp_path):
        """检测水体与注入真值 IoU 应较高（记入 manifest qa）。"""
        out = str(tmp_path / "out_iou")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "output-manifest.json"), encoding="utf-8") as f:
            man = json.load(f)
        assert man["qa"]["synthetic_iou"] > 0.5

    def test_bbox_only_auto_synthetic(self, tmp_path):
        out = str(tmp_path / "out_auto")
        r = run_cli([
            "--bbox", "116.39", "39.90", "116.40", "39.91",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
