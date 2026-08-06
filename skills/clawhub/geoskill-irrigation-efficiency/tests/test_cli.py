"""CLI argument parsing tests for irrigation-efficiency."""
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
        assert "--eff-method" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_eff_method_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--eff-method", "bad"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_synthetic_runs_exit_0(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "irrigation_demand.tif"))
        assert os.path.exists(os.path.join(out, "irrigation_efficiency.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
        with open(os.path.join(out, "irrigation_report.json"), encoding="utf-8") as f:
            rep = json.load(f)
        assert 0.0 <= rep["mean_efficiency"] <= 1.0
        assert rep["mean_demand_mm"] >= 0

    def test_usda_method_runs(self, tmp_path):
        out = str(tmp_path / "out_usda")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--eff-method", "usda", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
