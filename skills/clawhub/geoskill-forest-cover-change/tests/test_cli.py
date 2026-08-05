"""CLI argument parsing tests for forest-cover-change."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as fc, SCRIPT


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
        assert "--threshold" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_input_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_bad_threshold_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--threshold", "5"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_run_ok(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--n-dates", "4", "--quiet", "--output-dir", out,
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "forest_change_class.tif"))
        assert os.path.exists(os.path.join(out, "cva_magnitude.tif"))
        assert os.path.exists(os.path.join(out, "area_stats.json"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_bbox_only_autosynthetic_ok(self, tmp_path):
        out = str(tmp_path / "out2")
        r = run_cli([
            "--bbox", "121", "31", "122", "32", "--quiet", "--output-dir", out,
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
