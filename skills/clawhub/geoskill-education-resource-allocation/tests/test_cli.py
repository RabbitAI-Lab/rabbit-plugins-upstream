"""CLI tests for education-resource-allocation."""
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
        for flag in ("--bbox", "--synthetic", "--method"):
            assert flag in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0 and "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        assert run_cli([]).returncode == 2

    def test_bad_method_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--method", "kmeans"])
        assert r.returncode == 2

    def test_input_not_found_exit_2(self):
        assert run_cli(["--input", "missing.tif"]).returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        assert run_cli(["--synthetic"]).returncode == 2
