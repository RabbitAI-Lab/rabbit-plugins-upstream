"""CLI argument parsing tests for sar-wind-speed."""
import subprocess
import sys
import os

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
        assert "--cmod" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_cmod_exit_2(self):
        r = run_cli(["--bbox", "121", "30", "122", "31", "--synthetic", "--cmod", "bad"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_cmod5_synthetic(self, tmp_path):
        out = str(tmp_path / "c5")
        r = run_cli(["--bbox", "121", "30", "122", "31", "--synthetic",
                     "--cmod", "cmod5", "--wind-dir", "45",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "wind_speed.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_cmod7_synthetic(self, tmp_path):
        out = str(tmp_path / "c7")
        r = run_cli(["--bbox", "121", "30", "122", "31", "--synthetic",
                     "--cmod", "cmod7", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "wind_speed.tif"))
