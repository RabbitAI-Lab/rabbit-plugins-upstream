"""CLI argument parsing tests for strip-noise-removal."""
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
        assert "--direction" in r.stdout
        assert "--method" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent_file.tif"])
        assert r.returncode == 2

    def test_bad_direction_exit_2(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--direction", "diagonal",
        ])
        assert r.returncode == 2

    def test_bad_method_exit_2(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--method", "wavelet",
        ])
        assert r.returncode == 2

    def test_synthetic_run_exit_0(self, tmp_path):
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--output-dir", str(tmp_path / "out"),
            "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(str(tmp_path / "out" / "output-manifest.json"))
        assert os.path.exists(str(tmp_path / "out" / "destriped.tif"))
