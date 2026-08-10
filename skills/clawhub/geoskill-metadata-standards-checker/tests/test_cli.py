"""CLI argument parsing tests for metadata-standards-checker."""
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(__file__))
from conftest import SCRIPT


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
        assert "--standard" in r.stdout

    def test_version(self):
        r = run_cli(["--version"])
        assert r.returncode == 0
        assert "1.0.0" in r.stdout

    def test_no_args_exit_2(self):
        r = run_cli([])
        assert r.returncode == 2

    def test_bad_standard_exit_2(self):
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--standard", "dublin"])
        assert r.returncode == 2

    def test_input_file_not_found_exit_2(self):
        r = run_cli(["--input", "nonexistent.xml"])
        assert r.returncode == 2

    def test_synthetic_without_bbox_exit_2(self):
        r = run_cli(["--synthetic"])
        assert r.returncode == 2


class TestCLIRun:
    def test_synthetic_run_ok(self):
        out = "./_test_cli_run"
        r = run_cli(["--bbox", "116", "39", "117", "40", "--synthetic",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "output-manifest.json"))

    def test_real_input_run_ok(self, tmp_path):
        # 写一个真实 ISO 文件再喂给 CLI
        sys.path.insert(0, os.path.dirname(__file__))
        from conftest import mod as M
        xml = M.build_iso_xml([116, 39, 117, 40], True)
        p = tmp_path / "real.xml"
        p.write_text(xml, encoding="utf-8")
        out = str(tmp_path / "out")
        r = run_cli(["--input", str(p), "--standard", "iso19115",
                     "--output-dir", out, "--quiet"])
        assert r.returncode == 0, r.stderr
        assert os.path.exists(os.path.join(out, "metadata_report.json"))
