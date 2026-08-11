"""CLI argument parsing tests for dinsar-coherence-analysis."""
import os
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from conftest import SCRIPT, mod as dc


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
        assert "--looks-r" in r.stdout
        assert "--looks-a" in r.stdout
        assert "--polarization" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_polarization_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--polarization", "xx"])
        assert r.returncode == 2

    def test_input_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif", "--slave", "also_missing.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_input_without_slave_exit_2(self, tmp_path):
        # 造一个真实存在的 master（2 波段实部/虚部），但不给 --slave
        cube = np.random.uniform(-1, 1, (2, 16, 16)).astype(np.float32)
        m = str(tmp_path / "m.tif")
        dc.write_geotiff(m, cube, [116.0, 39.0, 117.0, 40.0])
        r = run_cli(["--input", m])
        assert r.returncode == 2


class TestCLIEndToEnd:
    def test_bbox_only_runs(self, tmp_path):
        out = str(tmp_path / "o1")
        r = run_cli(["--bbox", "116", "39", "117", "40", "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "coherence.tif"))
        assert os.path.exists(os.path.join(out, "phase.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_custom_looks(self, tmp_path):
        out = str(tmp_path / "o2")
        r = run_cli([
            "--bbox", "116", "39", "117", "40", "--synthetic",
            "--looks-r", "4", "--looks-a", "4",
            "--polarization", "vh", "--output-dir", out, "--quiet",
        ])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "coherence_statistics.json"))
