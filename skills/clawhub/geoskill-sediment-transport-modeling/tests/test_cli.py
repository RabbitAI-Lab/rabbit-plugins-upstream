"""CLI argument parsing tests for sediment-transport-modeling."""
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SKILL_DIR, SCRIPT


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
        assert "--sdr" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        """No arguments → UsageError → exit 2."""
        r = run_cli([])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        """--synthetic without --bbox → UsageError → exit 2."""
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        """Non-existent input file → UsageError → exit 2."""
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_runs_exit_0(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli([
            "--bbox", "110", "35", "111", "36", "--synthetic",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "erosion_modulus.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))
