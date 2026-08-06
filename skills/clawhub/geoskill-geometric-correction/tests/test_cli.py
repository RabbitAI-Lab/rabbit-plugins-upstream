"""CLI argument parsing tests for geometric-correction."""
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


def run_cli(args, timeout=90):
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
        assert "--order" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_order_exit_2(self):
        """order 3 is not a valid choice → argparse → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--order", "3"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_order1_synthetic_ok(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--order", "1", "--quiet",
            "--output-dir", "./_test_cli_order1",
        ])
        assert r.returncode == 0, r.stderr

    def test_order2_synthetic_ok(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--order", "2", "--quiet",
            "--output-dir", "./_test_cli_order2",
        ])
        assert r.returncode == 0, r.stderr
