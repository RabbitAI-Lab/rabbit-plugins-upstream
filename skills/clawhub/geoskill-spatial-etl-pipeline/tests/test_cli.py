"""CLI argument parsing tests for spatial-etl-pipeline."""
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
        assert "--config" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_config_not_found_exit_2(self):
        r = run_cli(["--config", "nonexistent.json"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_run_ok(self):
        out = "./_test_cli_run"
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--features", "30", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "etl_report.json"))
        assert os.path.exists(os.path.join(out, "etl_output.geojson"))

    def test_custom_config_ok(self, tmp_path):
        cfg = {
            "source": {"type": "synthetic", "bbox": [116, 39, 117, 40], "n": 15},
            "steps": [{"op": "add_field", "name": "area", "source": "area"}],
            "load": {"format": "geojson",
                     "path": str(tmp_path / "custom.geojson")},
        }
        cfg_path = tmp_path / "cfg.json"
        cfg_path.write_text(json.dumps(cfg), encoding="utf-8")
        out = str(tmp_path / "out")
        r = run_cli(["--config", str(cfg_path), "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(str(tmp_path / "custom.geojson"))
