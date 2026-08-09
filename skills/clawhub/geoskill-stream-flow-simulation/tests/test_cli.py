"""CLI argument parsing tests for stream-flow-simulation."""
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
        assert "--rainfall" in r.stdout
        assert "--return-period" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
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
                     "--rainfall", "100", "--return-period", "10",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
        assert os.path.exists(os.path.join(out, "runoff_depth.tif"))
        with open(os.path.join(out, "hydrograph.json"), encoding="utf-8") as f:
            hydro = json.load(f)
        assert hydro["stats"]["peak_discharge_m3s"] > 0
        # 径流深必须小于降雨
        assert hydro["mean_runoff_depth_mm"] < hydro["rainfall_mm"]
