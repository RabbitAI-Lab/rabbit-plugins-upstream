"""CLI argument parsing tests for radiometric-calibration."""
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
        assert "--bbox" in r.stdout
        assert "--synthetic" in r.stdout
        assert "--output-type" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_sensor_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--sensor", "bad"])
        assert r.returncode == 2

    def test_bad_output_type_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--output-type", "bad"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_radiance_ok(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--sensor", "landsat8", "--output-type", "toa_radiance", "--quiet",
            "--output-dir", "./_test_cli_radiance",
        ])
        assert r.returncode == 0, r.stderr

    def test_reflectance_ok(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--sensor", "sentinel2", "--output-type", "toa_reflectance", "--quiet",
            "--output-dir", "./_test_cli_refl",
        ])
        assert r.returncode == 0, r.stderr
