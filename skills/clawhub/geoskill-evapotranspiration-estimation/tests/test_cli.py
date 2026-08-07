"""CLI argument parsing tests for evapotranspiration-estimation."""
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as et, SCRIPT


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
        assert "--method" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_method_exit_2(self):
        """Invalid method choice → argparse error → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--method", "bad"])
        assert r.returncode == 2

    def test_bad_alpha_exit_2(self):
        """Non-numeric --alpha → argparse type error → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--alpha", "abc"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        """Non-existent input file → UsageError → exit 2."""
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        """--synthetic without --bbox → UsageError → exit 2."""
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_pt_run_ok(self, tmp_path):
        out = str(tmp_path / "out_pt")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--method", "pt",
                     "--synthetic", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
        assert os.path.exists(os.path.join(out, "evapotranspiration.tif"))
        assert os.path.exists(os.path.join(out, "et_stats.json"))

    def test_sebal_run_ok(self, tmp_path):
        out = str(tmp_path / "out_sebal")
        r = run_cli(["--bbox", "121", "31", "122", "32", "--method", "sebal",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
