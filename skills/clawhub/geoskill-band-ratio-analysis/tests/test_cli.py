"""CLI argument parsing tests for band-ratio-analysis."""
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
        assert "--indices" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_index_exit_2(self):
        """Invalid index name → UsageError → exit 2."""
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--indices", "bogus_index", "--quiet"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        """Non-existent input file → UsageError → exit 2."""
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        """--synthetic without --bbox → UsageError → exit 2."""
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIIndices:
    def test_single_index(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--indices", "ndvi", "--quiet",
            "--output-dir", "./_test_idx_ndvi",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists("./_test_idx_ndvi/ndvi.tif")

    def test_all_default_indices(self):
        r = run_cli([
            "--bbox", "116", "39", "117", "40",
            "--synthetic", "--quiet",
            "--output-dir", "./_test_idx_all",
        ])
        assert r.returncode == 0, r.stderr
        for name in mod.INDICES:
            assert os.path.exists(f"./_test_idx_all/{name}.tif")
