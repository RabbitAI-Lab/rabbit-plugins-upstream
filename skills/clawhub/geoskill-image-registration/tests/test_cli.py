"""CLI argument parsing tests for image-registration."""
import subprocess
import sys
import os

import numpy as np

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
        assert "--input" in r.stdout
        assert "--target" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_input_without_target_exit_2(self, tmp_path):
        """--input 指向真实栅格但缺 --target → UsageError → exit 2."""
        cube = np.random.uniform(0, 1, (1, 16, 16)).astype(np.float32)
        p = str(tmp_path / "ref.tif")
        mod.write_geotiff(p, cube, [116.0, 39.0, 117.0, 40.0])
        r = run_cli(["--input", p])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_ok(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic", "--quiet",
            "--output-dir", "./_test_cli_synth",
        ])
        assert r.returncode == 0, r.stderr
