"""CLI argument parsing tests for map-algebra-calculator."""
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


def run_cli(args, timeout=60):
    return subprocess.run(
        [sys.executable, SCRIPT] + args,
        capture_output=True, text=True, timeout=timeout,
    )


class TestCLIBasics:
    def test_help(self):
        r = run_cli(["--help"])
        assert r.returncode == 0
        assert "--expr" in r.stdout
        assert "--preset" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        assert run_cli([]).returncode == 2

    def test_bad_preset_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--preset", "bad"])
        assert r.returncode == 2

    def test_bad_expr_exit_7_or_2(self):
        # 危险表达式应非 0 退出（UsageError → 2）
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--expr", "__import__('os')", "--quiet"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        assert run_cli(["--input", "nope.tif"]).returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        assert run_cli(["--synthetic"]).returncode == 2
