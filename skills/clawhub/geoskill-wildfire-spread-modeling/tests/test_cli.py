"""CLI argument parsing tests for wildfire-spread-modeling."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import SCRIPT


def run_cli(args, timeout=90):
    return subprocess.run([sys.executable, SCRIPT] + args,
                          capture_output=True, text=True, timeout=timeout)


class TestCLIBasics:
    def test_help(self):
        r = run_cli(["--help"])
        assert r.returncode == 0
        assert "--bbox" in r.stdout
        assert "--synthetic" in r.stdout
        assert "--steps" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        assert run_cli([]).returncode == 2

    def test_input_not_found_exit_2(self):
        assert run_cli(["--input", "nonexistent.tif"]).returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        assert run_cli(["--synthetic"]).returncode == 2

    def test_synthetic_run_ok(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--output-dir", "./_test_cli_out", "--quiet"])
        assert r.returncode == 0, r.stderr
