"""CLI argument parsing tests for monsoon-analysis."""
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
        assert "--region" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_region_exit_2(self):
        r = run_cli(["--bbox", "110", "20", "122", "40", "--region", "mars"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_synthetic_east_asia_exit_0(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "110", "20", "122", "40", "--region", "east_asia",
                     "--synthetic", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "monsoon_index.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_bbox_only_south_asia_exit_0(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "70", "8", "90", "30", "--region", "south_asia",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "monsoon_diagnosis.json"))
