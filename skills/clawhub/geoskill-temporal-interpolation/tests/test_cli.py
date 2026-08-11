"""CLI argument parsing tests for temporal-interpolation."""
import subprocess
import sys
import os

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
        assert "--method" in r.stdout
        assert "--n-dates" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_method_exit_2(self):
        """Invalid method choice → argparse error → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "bogus"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        """Non-existent input file → UsageError → exit 2."""
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        """--synthetic without --bbox → UsageError → exit 2."""
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIMethods:
    def test_savgol_mode(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--method", "savgol", "--n-dates", "12", "--quiet",
            "--output-dir", "./_test_savgol",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists("./_test_savgol/smoothed_series.tif")
        assert os.path.exists("./_test_savgol/smoothing_params.json")

    def test_spline_mode(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--method", "spline", "--n-dates", "10", "--quiet",
            "--output-dir", "./_test_spline",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists("./_test_spline/smoothed_series.tif")
