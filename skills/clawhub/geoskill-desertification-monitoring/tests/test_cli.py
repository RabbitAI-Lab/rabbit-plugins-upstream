"""CLI argument parsing tests for desertification-monitoring."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as dm, SCRIPT


def run_cli(args, timeout=60):
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
        r = run_cli(["--bbox", "100", "40", "101", "41", "--synthetic",
                     "--method", "bogus"])
        assert r.returncode == 2

    def test_bad_ndates_exit_2(self):
        r = run_cli(["--bbox", "100", "40", "101", "41", "--synthetic",
                     "--n-dates", "xx"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_synthetic_runs(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "100", "40", "101", "41", "--synthetic",
                     "--n-dates", "6", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "desertification_grade.tif"))
        assert os.path.exists(os.path.join(out, "ndvi_trend.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_linear_method_runs(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "100", "40", "101", "41", "--synthetic",
                     "--method", "linear", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
