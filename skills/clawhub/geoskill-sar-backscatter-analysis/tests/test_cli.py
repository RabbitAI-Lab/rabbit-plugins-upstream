"""CLI argument parsing tests for sar-backscatter-analysis."""
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
        assert "--polarization" in r.stdout
        assert "--n-dates" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_polarization_exit_2(self):
        """Invalid polarization → UsageError → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--polarization", "xx"])
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
    def test_synthetic_dual_pol(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--n-dates", "6", "--polarization", "vv,vh",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "backscatter_stats.tif"))
        assert os.path.exists(os.path.join(out, "timeseries.json"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
        with open(os.path.join(out, "timeseries.json"), encoding="utf-8") as f:
            ts = json.load(f)
        # 4 stats × 2 pol + ratio = 9 bands
        assert len(ts["band_names"]) == 9
        assert "vv_vh_ratio" in ts["band_names"]
        assert len(ts["region_mean_timeseries"]["vv"]) == 6

    def test_synthetic_single_pol(self, tmp_path):
        out = str(tmp_path / "out_sp")
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--polarization", "vv", "--n-dates", "4",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "timeseries.json"), encoding="utf-8") as f:
            ts = json.load(f)
        assert len(ts["band_names"]) == 4  # mean/std/amp/cv, no ratio

    def test_bbox_only_auto_synthetic(self, tmp_path):
        out = str(tmp_path / "out_auto")
        r = run_cli([
            "--bbox", "116.39", "39.90", "116.40", "39.91",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
