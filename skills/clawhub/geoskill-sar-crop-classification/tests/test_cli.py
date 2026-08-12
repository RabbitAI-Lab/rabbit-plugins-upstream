"""CLI argument parsing tests for sar-crop-classification."""
import subprocess
import sys
import os
import json

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
        assert "--bbox" in r.stdout
        assert "--synthetic" in r.stdout
        assert "--n-dates" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_n_dates_type_exit_2(self):
        """Non-integer --n-dates → argparse error → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--n-dates", "abc"])
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
    def test_synthetic_runs(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--n-dates", "6",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "crop_classification.tif"))
        assert os.path.exists(os.path.join(out, "crop_area_stats.json"))
        assert os.path.exists(os.path.join(out, "confusion_matrix.json"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_accuracy_above_threshold(self, tmp_path):
        """合成模式总体精度应 > 0.7。"""
        out = str(tmp_path / "out_acc")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--n-dates", "8",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "output-manifest.json"), encoding="utf-8") as f:
            man = json.load(f)
        assert man["qa"]["overall_accuracy"] > 0.7

    def test_all_three_classes_present(self, tmp_path):
        out = str(tmp_path / "out_cls")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "crop_area_stats.json"), encoding="utf-8") as f:
            stats = json.load(f)
        names = {c["class_name"] for c in stats["classes"]}
        assert names == {"rice", "wheat", "corn"}
        assert all(c["pixels"] > 0 for c in stats["classes"])

    def test_bbox_only_auto_synthetic(self, tmp_path):
        out = str(tmp_path / "out_auto")
        r = run_cli([
            "--bbox", "116.39", "39.90", "116.40", "39.91",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
