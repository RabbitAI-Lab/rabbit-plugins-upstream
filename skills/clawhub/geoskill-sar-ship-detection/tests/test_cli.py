"""CLI argument parsing tests for sar-ship-detection."""
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
        assert "--cfar" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_cfar_exit_2(self):
        r = run_cli(["--bbox", "121", "30", "122", "31", "--synthetic", "--cfar", "bad"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_ca_synthetic(self, tmp_path):
        out = str(tmp_path / "ca")
        r = run_cli(["--bbox", "121", "30", "122", "31", "--synthetic",
                     "--cfar", "ca", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "ships.geojson"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_os_synthetic(self, tmp_path):
        out = str(tmp_path / "os")
        r = run_cli(["--bbox", "121", "30", "122", "31", "--synthetic",
                     "--cfar", "os", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "ships.geojson"))
