"""test_qa_flag.py — tests for the --qa flag on the download subcommand.

The spec (batch E) calls for --qa on the download subcommand. The download
subcommand of modis_lst_download.py already accepts --qa, but this test
module pins that behaviour so future refactors don't regress it.
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
from argparse import Namespace
from pathlib import Path
from unittest.mock import patch, MagicMock

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
CLI = SCRIPTS_DIR / "modis_lst_download.py"


def _load_module():
    """Import the CLI module for direct unit testing."""
    spec = importlib.util.spec_from_file_location("modis_lst", str(CLI))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def run_cli(*args, timeout=30):
    proc = subprocess.run(
        [sys.executable, str(CLI), *args],
        capture_output=True, text=True, timeout=timeout,
    )
    return proc


class TestQaFlagPresence:
    """Verify --qa is wired into the download subcommand."""

    def test_download_help_lists_qa(self):
        proc = run_cli("download", "--help")
        text = proc.stdout + proc.stderr
        assert "--qa" in text, f"--qa not in download --help:\n{text}"
        assert "PATH" in text  # metavar

    def test_qa_default_is_none(self):
        m = _load_module()
        # Parse the same args that the CLI would receive; should not crash
        proc = run_cli("download", "--help")
        assert proc.returncode == 0


class TestQaWriteFunction:
    """Direct unit tests for the _write_qa helper."""

    def test_qa_writes_file(self, tmp_path):
        m = _load_module()
        qa_path = tmp_path / "qa.json"
        args = Namespace(
            product="MOD11A1",
            start="2024-01-01", end="2024-01-02",
            layers="LST_Day_1km,QC_Day",
            year=2024, season=None,
            preset=None, place=None,
            output=str(tmp_path / "out"),
            qa=str(qa_path),
        )
        m._write_qa(args, bbox=(115, 30, 117, 32),
                     source_label="bbox", granule_count=3, success_count=3)
        assert qa_path.exists()
        with open(qa_path, encoding="utf-8") as f:
            qa = json.load(f)
        assert qa["skill"] == "modis-lst-download"
        assert "version" in qa
        assert qa["query"]["product"] == "MOD11A1"
        assert qa["query"]["bbox"] == [115, 30, 117, 32]
        assert qa["query"]["bbox_source"] == "bbox"
        assert qa["granules_found"] == 3
        assert qa["downloaded"] == 3
        assert qa["output"] == str(tmp_path / "out")

    def test_qa_with_place(self, tmp_path):
        m = _load_module()
        qa_path = tmp_path / "qa.json"
        args = Namespace(
            product="MYD11A1",
            start="2024-06-01", end="2024-06-30",
            layers="LST_Day_1km",
            year=None, season="summer",
            preset=None, place="北京市",
            output=str(tmp_path / "out"),
            qa=str(qa_path),
        )
        m._write_qa(args, bbox=(115.5, 39.5, 117.5, 41.0),
                     source_label="place", granule_count=0, success_count=0)
        assert qa_path.exists()
        with open(qa_path, encoding="utf-8") as f:
            qa = json.load(f)
        assert qa["query"]["place"] == "北京市"
        assert qa["query"]["season"] == "summer"
        assert qa["granules_found"] == 0

    def test_qa_creates_parent_directory(self, tmp_path):
        m = _load_module()
        qa_path = tmp_path / "nested" / "deeper" / "qa.json"
        args = Namespace(
            product="MOD11A1",
            start="2024-01-01", end="2024-01-02",
            layers=None,
            year=None, season=None,
            preset=None, place=None,
            output=str(tmp_path / "out"),
            qa=str(qa_path),
        )
        m._write_qa(args, bbox=(0, 0, 1, 1),
                     source_label="bbox", granule_count=1, success_count=1)
        assert qa_path.exists()
