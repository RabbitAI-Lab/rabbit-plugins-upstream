"""Tests for src/duplicate_guard.py — blocks repeat publishes.

DuplicateGuard is the gate that prevents accidentally re-publishing the
same note within a short window (default 10 minutes) and re-publishing
an identical fingerprint ever. publish mode hits this guard on every
attempt, so the test coverage here is critical for regression safety.
"""

import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from duplicate_guard import DuplicateGuard


class TestDuplicateGuard(unittest.TestCase):
    def test_first_publish_allowed(self):
        with tempfile.TemporaryDirectory() as tmp:
            runtime_dir = Path(tmp) / "runtime"
            runtime_dir.mkdir(parents=True)
            guard = DuplicateGuard(runtime_dir, min_interval_minutes=10)
            # Should not raise on first call.
            guard.check("fingerprint-abc")

    def test_duplicate_fingerprint_blocked(self):
        with tempfile.TemporaryDirectory() as tmp:
            runtime_dir = Path(tmp) / "runtime"
            runtime_dir.mkdir(parents=True)
            guard = DuplicateGuard(runtime_dir, min_interval_minutes=10)
            guard.record("fp-1", {"status": "published"})
            with self.assertRaises(RuntimeError) as ctx:
                guard.check("fp-1")
            self.assertIn("duplicate", str(ctx.exception).lower())

    def test_different_fingerprint_allowed_after_record(self):
        with tempfile.TemporaryDirectory() as tmp:
            runtime_dir = Path(tmp) / "runtime"
            runtime_dir.mkdir(parents=True)
            # min_interval_minutes=0 isolates the fingerprint dedup path
            # from the interval guard, which is exercised separately in
            # test_interval_blocks_within_window.
            guard = DuplicateGuard(runtime_dir, min_interval_minutes=0)
            guard.record("fp-1", {"status": "published"})
            guard.check("fp-2")  # different fingerprint, no interval pressure

    def test_interval_blocks_within_window(self):
        """Even a new fingerprint is blocked if the previous publish was
        within the configured interval (10 minutes by default)."""
        with tempfile.TemporaryDirectory() as tmp:
            runtime_dir = Path(tmp) / "runtime"
            runtime_dir.mkdir(parents=True)
            # Pre-populate the history file with a recent entry.
            history = {
                "last_published_at": datetime.now(timezone.utc).astimezone().isoformat(),
                "entries": [],
            }
            (runtime_dir / "published_history.json").write_text(
                json.dumps(history, ensure_ascii=False, indent=2), encoding="utf-8"
            )
            guard = DuplicateGuard(runtime_dir, min_interval_minutes=10)
            with self.assertRaises(RuntimeError) as ctx:
                guard.check("fp-new")
            self.assertIn("interval", str(ctx.exception).lower())

    def test_history_file_lives_in_runtime_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            runtime_dir = Path(tmp) / "runtime"
            runtime_dir.mkdir(parents=True)
            guard = DuplicateGuard(runtime_dir)
            self.assertEqual(guard.path.name, "published_history.json")
            self.assertEqual(guard.path.parent, runtime_dir)

    def test_record_truncates_history_to_200_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            runtime_dir = Path(tmp) / "runtime"
            runtime_dir.mkdir(parents=True)
            guard = DuplicateGuard(runtime_dir)
            for i in range(250):
                # Vary fingerprint so each `record` appends a new entry
                # (the dedup check would otherwise reject identical fps).
                guard.record(f"fp-{i}", {"i": i})
            payload = json.loads(guard.path.read_text(encoding="utf-8"))
            self.assertEqual(len(payload["entries"]), 200)
            # Most-recent entry is fp-249, oldest preserved fp-50.
            self.assertEqual(payload["entries"][-1]["fingerprint"], "fp-249")
            self.assertEqual(payload["entries"][0]["fingerprint"], "fp-50")


if __name__ == "__main__":
    unittest.main()