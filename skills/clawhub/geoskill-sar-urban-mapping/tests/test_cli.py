"""CLI argument parsing tests for sar-urban-mapping."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import SCRIPT


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
        assert "--threshold" in r.stdout
        assert "--texture" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_texture_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--texture", "maybe"])
        assert r.returncode == 2

    def test_input_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIEndToEnd:
    def test_bbox_only_runs(self, tmp_path):
        out = str(tmp_path / "o1")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "urban_mask.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_synthetic_texture_false(self, tmp_path):
        out = str(tmp_path / "o2")
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--texture", "false", "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "urban_statistics.json"))
