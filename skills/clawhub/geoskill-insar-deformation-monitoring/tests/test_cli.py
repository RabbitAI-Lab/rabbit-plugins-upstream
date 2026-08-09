"""CLI argument parsing tests for insar-deformation-monitoring."""
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
        assert "--wavelength" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
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
            "--synthetic", "--wavelength", "0.0555",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "deformation.tif"))
        assert os.path.exists(os.path.join(out, "coherence.tif"))
        assert os.path.exists(os.path.join(out, "insar_params.json"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_bbox_only_auto_synthetic(self, tmp_path):
        out = str(tmp_path / "out_auto")
        r = run_cli([
            "--bbox", "116.39", "39.90", "116.40", "39.91",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_synthetic_high_correlation(self, tmp_path):
        """合成模式下恢复形变与真值相关系数应较高（记入 manifest qa）。"""
        out = str(tmp_path / "out_corr")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "output-manifest.json"), encoding="utf-8") as f:
            man = json.load(f)
        corr = man["qa"]["synthetic_correlation_with_truth"]
        assert abs(corr) > 0.8
