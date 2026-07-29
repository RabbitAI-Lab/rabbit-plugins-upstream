"""Tests for the --qa sidecar summary (Phase 5 optimization)."""

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import dem_download as dem  # noqa: E402


class TestWriteQASummary(unittest.TestCase):
    def test_writes_json(self):
        with tempfile.TemporaryDirectory() as td:
            qa_path = os.path.join(td, "run.qa.json")
            args = mock.Mock(spec=[])
            args.source = "auto"
            args.dataset = None
            args.resolution = 30
            args.bbox = "100,30,101,31"
            args.output = "out.tif"
            args.admin = None
            args.admin_code = None
            args.mode = "auto"
            dem.write_qa_summary(
                qa_path, skill="download-dem", command="download",
                args=args,
                payload={"dataset": "cop-dem-glo-30"},
            )
            self.assertTrue(os.path.exists(qa_path))
            data = json.loads(Path(qa_path).read_text(encoding="utf-8"))
            self.assertEqual(data["skill"], "download-dem")
            self.assertEqual(data["command"], "download")
            self.assertEqual(data["source"], "auto")
            self.assertEqual(data["dataset"], "cop-dem-glo-30")
            self.assertEqual(data["resolution"], 30)
            self.assertEqual(data["bbox"], "100,30,101,31")
            self.assertIn("timestamp", data)
            self.assertIn("version", data)

    def test_creates_parent_dirs(self):
        with tempfile.TemporaryDirectory() as td:
            qa_path = os.path.join(td, "nested", "subdir", "run.qa.json")
            args = mock.Mock(spec=[])
            dem.write_qa_summary(
                qa_path, skill="download-dem", command="download",
                args=args, payload={"x": 1},
            )
            self.assertTrue(os.path.exists(qa_path))


class TestDownloadParserQA(unittest.TestCase):
    def test_download_accepts_qa(self):
        parser = dem.build_parser()
        ns = parser.parse_args([
            "download", "--bbox", "100", "30", "101", "31",
            "--output", "out.tif", "--qa", "out.qa.json",
        ])
        self.assertEqual(ns.qa, "out.qa.json")
        self.assertEqual(ns.output, "out.tif")
        self.assertEqual(ns.bbox, [100.0, 30.0, 101.0, 31.0])

    def test_download_no_qa_defaults_none(self):
        parser = dem.build_parser()
        ns = parser.parse_args([
            "download", "--bbox", "100", "30", "101", "31",
            "--output", "out.tif",
        ])
        self.assertIsNone(ns.qa)


if __name__ == "__main__":
    unittest.main()
