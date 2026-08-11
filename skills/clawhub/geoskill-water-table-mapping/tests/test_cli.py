"""CLI argument parsing tests for water-table-mapping."""
import subprocess
import sys
import os
import csv
import json

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


def run_cli(args, timeout=180):
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

    def test_input_csv_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.csv"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_synthetic_idw_runs(self, tmp_path):
        out = str(tmp_path / "out")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--method", "idw",
                     "--grid-size", "32", "--n-wells", "25", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "water_table.tif"))
        assert os.path.exists(os.path.join(out, "depth_to_water.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_input_csv_runs(self, tmp_path):
        csv_path = str(tmp_path / "wells.csv")
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["x", "y", "level"])
            for i in range(20):
                x = 116.0 + (i % 5) * 0.2
                y = 39.0 + (i // 5) * 0.2
                level = 40.0 - 2.0 * (i % 5) - 1.0 * (i // 5)
                w.writerow([x, y, level])
        out = str(tmp_path / "out_csv")
        r = run_cli(["--input", csv_path, "--bbox", "116", "39", "117", "40",
                     "--grid-size", "24", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "water_table.tif"))
