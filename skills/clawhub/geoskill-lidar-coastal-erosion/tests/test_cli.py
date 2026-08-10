"""CLI tests for lidar-coastal-erosion."""
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


def run_cli(args, timeout=90):
    return subprocess.run([sys.executable, SCRIPT] + args,
                          capture_output=True, text=True, timeout=timeout)


class TestCLIBasics:
    def test_help(self):
        r = run_cli(["--help"])
        assert r.returncode == 0
        assert "--bbox" in r.stdout
        assert "--synthetic" in r.stdout
        assert "--dt" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        assert run_cli([]).returncode == 2

    def test_input_not_found_exit_2(self):
        assert run_cli(["--input", "nope.xyz"]).returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        assert run_cli(["--synthetic"]).returncode == 2

    def test_synthetic_runs(self):
        out = "./_test_cli_out"
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "elevation_change.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_bbox_only_auto_synthetic(self):
        out = "./_test_cli_bboxonly"
        r = run_cli(["--bbox", "116", "39", "117", "40",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr

    def test_custom_dt(self):
        out = "./_test_cli_dt"
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--dt", "20", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
