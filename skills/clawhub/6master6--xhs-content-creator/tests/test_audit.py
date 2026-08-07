"""Tests for src/audit.py — audit log writer for each publisher run.

The audit log is the durability layer for SKILL.md §1.5 automation rule
("失败时保留 JSON/截图/DOM/日志"). These tests lock in the path layout
and event schema.
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from audit import AuditLog, now_stamp


class TestAuditLog(unittest.TestCase):
    def test_init_creates_directories(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "runtime" / "runs" / "20260804-XXX"
            al = AuditLog(run_dir)
            self.assertTrue(al.run_dir.exists())
            self.assertTrue(al.screenshots_dir.exists())
            self.assertTrue(al.dom_dir.exists())
            self.assertFalse(al.actions_path.exists())  # only created on first event

    def test_event_appends_to_actions_jsonl(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "runtime" / "runs" / "20260804-XXX"
            al = AuditLog(run_dir)
            al.event("login_required", timeout_seconds=180)
            al.event("publish_run_done", mode="publish")
            self.assertTrue(al.actions_path.exists())
            lines = [json.loads(line) for line in al.actions_path.read_text(encoding="utf-8").strip().splitlines()]
            self.assertEqual(len(lines), 2)
            self.assertEqual(lines[0]["action"], "login_required")
            self.assertEqual(lines[0]["timeout_seconds"], 180)
            self.assertEqual(lines[1]["action"], "publish_run_done")
            self.assertEqual(lines[1]["mode"], "publish")
            for entry in lines:
                self.assertIn("ts", entry)
                self.assertIn("action", entry)

    def test_write_json_creates_file_in_run_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "runtime" / "runs" / "20260804-XXX"
            al = AuditLog(run_dir)
            path = al.write_json("result.json", {"status": "ok", "run_id": "test"})
            self.assertTrue(path.exists())
            self.assertEqual(path.parent, al.run_dir)
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["status"], "ok")
            self.assertEqual(data["run_id"], "test")

    def test_event_records_screenshot_metadata(self):
        """Audit must record each screenshot/dom write as an event so the
        run timeline is reconstructable from actions.jsonl alone."""
        with tempfile.TemporaryDirectory() as tmp:
            run_dir = Path(tmp) / "runtime" / "runs" / "20260804-XXX"
            al = AuditLog(run_dir)
            # write_json is also audited.
            al.write_json("content.normalized.json", {"title": "t"})
            last = json.loads(al.actions_path.read_text(encoding="utf-8").strip().splitlines()[-1])
            self.assertEqual(last["action"], "write_json")
            self.assertEqual(last["name"], "content.normalized.json")

    def test_now_stamp_format(self):
        stamp = now_stamp()
        # Format: YYYYMMDD-HHMMSS = 15 chars, with `-` at index 8.
        self.assertEqual(len(stamp), 15)
        self.assertEqual(stamp[8], "-")
        # The first 8 chars must be digits (date).
        for ch in stamp[:8]:
            self.assertIn(ch, "0123456789")
        # The chars after the dash must be digits (time).
        for ch in stamp[9:]:
            self.assertIn(ch, "0123456789")


if __name__ == "__main__":
    unittest.main()