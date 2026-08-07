"""CLI argument parsing tests for multimodal-fusion-ai."""
import subprocess
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod, SCRIPT


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
        assert "--weights" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_norm_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic", "--norm", "robust"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.tif"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2

    def test_bad_weights_count_exit_2(self):
        # 合成数据有 2 个模态，给 3 个权重 -> UsageError exit 2
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--weights", "0.3,0.3,0.4", "--quiet"])
        assert r.returncode == 2
