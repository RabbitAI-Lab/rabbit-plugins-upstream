"""CLI argument parsing tests for sentinel1-tile-management."""
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
        assert "--mode" in r.stdout
        assert "--polarization" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_mode_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--mode", "sm"])
        assert r.returncode == 2

    def test_bad_polarization_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--polarization", "vv,zz"])
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
        assert os.path.exists(os.path.join(out, "sigma0_db.tif"))
        assert os.path.exists(os.path.join(out, "processing_log.json"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_ew_single_pol(self, tmp_path):
        out = str(tmp_path / "o2")
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--mode", "ew", "--polarization", "hh",
            "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr

    def test_db_range_valid(self, tmp_path):
        """输出 dB 值应在合理物理区间。"""
        import json
        import rasterio
        out = str(tmp_path / "o3")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        with rasterio.open(os.path.join(out, "sigma0_db.tif")) as src:
            data = src.read()
        assert data.min() > -40
        assert data.max() < 5
        with open(os.path.join(out, "processing_log.json"), encoding="utf-8") as f:
            log = json.load(f)
        assert "steps" in log and len(log["steps"]) >= 2
