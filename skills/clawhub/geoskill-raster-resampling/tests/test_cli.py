"""CLI argument parsing tests for raster-resampling."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import SCRIPT


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
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "lanczos"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_run_ok(self):
        out = "./_test_cli_run"
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "bilinear", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "resampled.tif"))

    def test_all_methods_ok(self):
        for meth in ("nearest", "bilinear", "cubic"):
            out = f"./_test_cli_{meth}"
            r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                         "--method", meth, "--scale", "0.5",
                         "--output-dir", out, "--quiet"])
            assert r.returncode == 0, f"{meth}: {r.stderr}"
