"""CLI argument parsing tests for sar-forest-biomass."""
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
        assert "--band" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_band_exit_2(self):
        r = run_cli(["--bbox", "110", "22", "111", "23", "--synthetic", "--band", "x"])
        assert r.returncode == 2

    def test_bad_model_exit_2(self):
        r = run_cli(["--bbox", "110", "22", "111", "23", "--synthetic", "--model", "bad"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_saturation_l_synthetic(self, tmp_path):
        out = str(tmp_path / "satl")
        r = run_cli(["--bbox", "110", "22", "111", "23", "--synthetic",
                     "--band", "l", "--model", "saturation",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "forest_biomass.tif"))
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_linear_c_synthetic(self, tmp_path):
        out = str(tmp_path / "linc")
        r = run_cli(["--bbox", "110", "22", "111", "23", "--synthetic",
                     "--band", "c", "--model", "linear",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "forest_biomass.tif"))

    def test_calibration_csv(self, tmp_path):
        # 生成一个标定 CSV，验证 --calibration 路径可用
        import numpy as np
        csv = tmp_path / "samples.csv"
        agb = np.linspace(10, 200, 40)
        sigma0 = 0.033 * agb - 15.0 + np.random.default_rng(0).normal(0, 0.2, 40)
        with open(csv, "w", encoding="utf-8") as f:
            f.write("sigma0,agb\n")
            for s, a in zip(sigma0, agb):
                f.write(f"{s:.4f},{a:.2f}\n")
        out = str(tmp_path / "cal")
        r = run_cli(["--bbox", "110", "22", "111", "23", "--synthetic",
                     "--band", "c", "--model", "linear",
                     "--calibration", str(csv), "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr

    def test_missing_calibration_exit_2(self, tmp_path):
        out = str(tmp_path / "nocal")
        r = run_cli(["--bbox", "110", "22", "111", "23", "--synthetic",
                     "--calibration", "nope.csv", "--output-dir", out, "--quiet"])
        assert r.returncode == 2
