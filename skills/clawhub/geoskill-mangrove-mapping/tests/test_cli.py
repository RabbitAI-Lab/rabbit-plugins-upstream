"""CLI argument parsing tests for mangrove-mapping."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as mm, SCRIPT


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
        assert "--n-dates" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_ndates_exit_2(self):
        """Invalid integer for --n-dates -> argparse error -> exit 2."""
        r = run_cli(["--bbox", "110", "21", "111", "22", "--synthetic",
                     "--n-dates", "notanint"])
        assert r.returncode == 2

    def test_bad_threshold_exit_2(self):
        r = run_cli(["--bbox", "110", "21", "111", "22", "--synthetic",
                     "--score-threshold", "abc"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_synthetic_bbox_runs(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "110", "21", "111", "22", "--synthetic",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "mangrove.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_multidate_change_runs(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "110", "21", "111", "22", "--synthetic",
                     "--n-dates", "3", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "mangrove_change.tif"))
