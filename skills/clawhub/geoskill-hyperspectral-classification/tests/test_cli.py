"""CLI argument parsing tests for hyperspectral-classification."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import SCRIPT


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
        assert "--method" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_method_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--method", "bad"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_rf(self, tmp_path):
        out = str(tmp_path / "out_rf")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "rf", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "classification.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_bbox_only_auto_synthetic(self, tmp_path):
        """仅给 --bbox（无 --input、无 --synthetic）也应自动走合成。"""
        out = str(tmp_path / "out_auto")
        r = run_cli(["--bbox", "121", "31", "122", "32",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_accuracy_reported(self, tmp_path):
        import json
        out = str(tmp_path / "out_acc")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "accuracy.json"), encoding="utf-8") as f:
            acc = json.load(f)
        assert acc["overall_accuracy"] > 0.75
