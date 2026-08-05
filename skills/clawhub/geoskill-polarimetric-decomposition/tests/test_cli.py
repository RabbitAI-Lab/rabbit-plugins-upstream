"""CLI argument parsing tests for polarimetric-decomposition."""
import subprocess
import sys
import os

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
        assert "--method" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_method_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--method", "bad"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIMethods:
    def test_cloude_synthetic(self, tmp_path):
        out = str(tmp_path / "cloude")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "cloude", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "cloude_H_A_alpha.tif"))

    def test_ha_alpha_synthetic(self, tmp_path):
        out = str(tmp_path / "ha")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "ha_alpha", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr

    def test_freeman_synthetic(self, tmp_path):
        out = str(tmp_path / "free")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "freeman", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "freeman_three_component.tif"))
