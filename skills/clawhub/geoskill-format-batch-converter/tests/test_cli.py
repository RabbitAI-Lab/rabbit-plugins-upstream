"""CLI argument parsing tests for format-batch-converter."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import SCRIPT


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
        assert "--vector-target" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_vector_target_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--vector-target", "dxf"])
        assert r.returncode == 2

    def test_input_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent_dir_xyz"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_run_ok(self):
        out = "./_test_cli_run"
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--vector-target", "gpkg", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "conversion_log.json"))
        assert os.path.isdir(os.path.join(out, "converted"))
