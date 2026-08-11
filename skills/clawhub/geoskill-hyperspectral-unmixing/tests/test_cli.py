"""CLI argument parsing tests for hyperspectral-unmixing."""
import json
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
        assert "--n-endmembers" in r.stdout

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


class TestCLIRun:
    def test_synthetic_vca(self, tmp_path):
        out = str(tmp_path / "out_vca")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "vca", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "abundances.tif"))
        assert os.path.exists(os.path.join(out, "endmembers.json"))
        assert os.path.exists(os.path.join(out, "residual.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_bbox_only_auto_synthetic(self, tmp_path):
        out = str(tmp_path / "out_auto")
        r = run_cli(["--bbox", "121", "31", "122", "32",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr

    def test_abundance_mae_reported(self, tmp_path):
        out = str(tmp_path / "out_mae")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "nfindr", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        with open(os.path.join(out, "output-manifest.json"), encoding="utf-8") as f:
            man = json.load(f)
        assert man["qa"]["mean_abundance_mae"] < 0.1
