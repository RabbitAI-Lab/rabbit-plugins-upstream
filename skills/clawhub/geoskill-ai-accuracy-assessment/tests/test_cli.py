"""CLI argument parsing tests for ai-accuracy-assessment."""
import subprocess
import sys
import os

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


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
        assert "--window" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_truth_file_not_found_exit_2(self):
        # input 存在但 truth 不存在 -> UsageError exit 2
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            pred_path = os.path.join(td, "pred.tif")
            mod.write_geotiff(pred_path, np.zeros((8, 8), dtype=np.float32),
                              [116, 39, 117, 40])
            r = run_cli(["--input", pred_path, "--truth", "nope.tif"])
            assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_single_band_input_no_truth_exit_6(self):
        """单波段输入且无 --truth -> 数据验证失败 exit 6。"""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            pred_path = os.path.join(td, "pred.tif")
            mod.write_geotiff(pred_path, np.zeros((8, 8), dtype=np.float32),
                              [116, 39, 117, 40])
            r = run_cli(["--input", pred_path])
            assert r.returncode == 6
