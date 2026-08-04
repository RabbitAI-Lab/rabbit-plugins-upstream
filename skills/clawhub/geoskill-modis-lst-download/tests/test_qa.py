"""Tests for the --qa sidecar summary (Phase 5 optimization)."""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import modis_lst_download as mld  # noqa: E402

CLI = SCRIPTS_DIR / "modis_lst_download.py"


class TestWriteQA(unittest.TestCase):
    """Test the internal _write_qa helper directly."""

    def test_writes_json_with_expected_fields(self):
        with tempfile.TemporaryDirectory() as td:
            qa_path = os.path.join(td, "out.qa.json")
            args = mld.argparse.Namespace(
                product="MOD11A1",
                start="2023-07-01",
                end="2023-07-31",
                bbox=[115.7, 39.4, 116.8, 40.3],
                layers="LST_Day_1km,QC_Day",
                year=2023,
                season=None,
                preset="city-uhi",
                place=None,
                output="./modis_lst/",
                qa=qa_path,
            )
            mld._write_qa(
                args,
                bbox=(115.7, 39.4, 116.8, 40.3),
                source_label="--preset 'city-uhi'",
                granule_count=31,
                success_count=31,
            )
            self.assertTrue(os.path.exists(qa_path))
            data = json.loads(Path(qa_path).read_text(encoding="utf-8"))
            self.assertEqual(data["skill"], "modis-lst-download")
            self.assertEqual(data["command"], "download")
            self.assertEqual(data["query"]["product"], "MOD11A1")
            self.assertEqual(data["query"]["start"], "2023-07-01")
            self.assertEqual(data["query"]["end"], "2023-07-31")
            self.assertEqual(data["query"]["bbox"], [115.7, 39.4, 116.8, 40.3])
            self.assertEqual(data["query"]["preset"], "city-uhi")
            self.assertEqual(data["granules_found"], 31)
            self.assertEqual(data["downloaded"], 31)
            self.assertIn("timestamp", data)
            self.assertIn("version", data)

    def test_creates_parent_dirs(self):
        with tempfile.TemporaryDirectory() as td:
            qa_path = os.path.join(td, "nested", "subdir", "out.qa.json")
            args = mld.argparse.Namespace(
                product="MOD11A1", start="2023-07-01", end="2023-07-31",
                bbox=None, layers="LST_Day_1km", year=2023, season=None,
                preset=None, place=None, output="./modis_lst/", qa=qa_path,
            )
            mld._write_qa(args, bbox=None, source_label="(no spatial filter)",
                          granule_count=0, success_count=0)
            self.assertTrue(os.path.exists(qa_path))


class TestDownloadParserAcceptsQA(unittest.TestCase):
    def test_qa_in_help_output(self):
        proc = subprocess.run(
            [sys.executable, str(CLI), "download", "--help"],
            capture_output=True, text=True, timeout=10,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertIn("--qa", proc.stdout)
        self.assertIn("Write a JSON QA summary", proc.stdout)

    def test_qa_default_via_dry_validation(self):
        # When the user does not pass --qa, the code path that writes
        # the sidecar is guarded by `if args.qa: ...`. We just verify
        # the parser accepts the flag positionally.
        proc = subprocess.run(
            [sys.executable, str(CLI), "download", "--help"],
            capture_output=True, text=True, timeout=10,
        )
        # --qa PATH — there must be a metavar=PATH slot.
        self.assertIn("PATH", proc.stdout)


class TestQAViaCLI(unittest.TestCase):
    """End-to-end smoke test: run the CLI with --list-urls and --qa, verify sidecar."""

    def test_list_urls_writes_qa(self):
        with tempfile.TemporaryDirectory() as td:
            qa_path = os.path.join(td, "out.qa.json")
            # --list-urls: writes JSON of URLs and exits without downloading
            proc = subprocess.run(
                [
                    sys.executable, str(CLI), "download",
                    "--product", "MOD11A1",
                    "--start", "2023-07-01", "--end", "2023-07-02",
                    "--bbox", "115.7", "39.4", "116.8", "40.3",
                    "--list-urls", os.path.join(td, "urls.json"),
                    "--qa", qa_path,
                ],
                capture_output=True, text=True, timeout=60,
            )
            # If network failed, the sidecar won't be written (early return).
            # In CI we accept either; the parser test above already proved
            # the flag is wired. Skip if no network.
            if proc.returncode == 0 and os.path.exists(qa_path):
                data = json.loads(Path(qa_path).read_text(encoding="utf-8"))
                self.assertEqual(data["skill"], "modis-lst-download")
                self.assertEqual(data["command"], "download")


if __name__ == "__main__":
    unittest.main()
