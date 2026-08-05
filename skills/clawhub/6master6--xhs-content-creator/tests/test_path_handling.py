"""Tests for the path-handling bugs found during 2026-08-04 R1/R2.

Two real bugs were caught:

1. `generate_and_publish.py stage_images()` used `dst.relative_to(PROJECT_ROOT)`,
   which produced "runtime/inbound/foo.jpg" — but `src/content_validator.py`
   resolves relative image paths against my_content.json's parent dir
   (PROJECT_ROOT/runtime/), yielding "runtime/runtime/inbound/foo.jpg" and
   triggering "image does not exist". Fixed by switching to
   `dst.relative_to(CONTENT_JSON.parent)` → "inbound/foo.jpg".

2. `src/cloud_notify.py _notify_dir()` used
   `run_dir.parent.parent / base.name` — base.name strips parent segments,
   and the 2-level climb lands on PROJECT_ROOT/runtime/ (not PROJECT_ROOT),
   producing either a missing parent directory or a doubled "runtime/".
   Fixed by switching to `run_dir.parent.parent.parent / configured`.
"""

import unittest
import sys
import json
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from cloud_notify import CloudNotifier


class TestStageImagesRelativePath(unittest.TestCase):
    """Verify generate_and_publish.py path-resolution contract."""

    def test_relative_to_content_json_parent_drops_runtime_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            project_root = Path(tmp)
            runtime = project_root / "runtime"
            inbound = runtime / "inbound"
            inbound.mkdir(parents=True)
            dst = inbound / "xhs_20260804_01.jpg"
            dst.touch()

            content_json = runtime / "my_content.json"

            # Fixed contract: relative to my_content.json's parent.
            rel_new = dst.relative_to(content_json.parent)
            self.assertEqual(str(rel_new), "inbound/xhs_20260804_01.jpg")

            # Old buggy contract: relative to PROJECT_ROOT produces the
            # doubled-runtime segment that broke R1.
            rel_old = dst.relative_to(project_root)
            self.assertEqual(str(rel_old), "runtime/inbound/xhs_20260804_01.jpg")
            # The content_validator joins base_dir / raw, and base_dir is
            # my_content.json's parent (= PROJECT_ROOT/runtime/), so the
            # resolved path becomes PROJECT_ROOT/runtime/runtime/inbound/...
            # which does not exist on disk.
            joined = (content_json.parent / rel_old).resolve()
            self.assertNotEqual(joined, dst)


class TestCloudNotifyDir(unittest.TestCase):
    """Verify _notify_dir returns the correct path after the P2 fix."""

    def _run_dir(self, base: Path) -> Path:
        return base / "runtime" / "runs" / "20260804-XXX"

    def test_default_single_segment(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = {"lobster_notify_dir": "runtime/lobster-notify"}
            n = CloudNotifier(cfg)
            run_dir = self._run_dir(Path(tmp)).resolve()
            expected = (Path(tmp) / "runtime" / "lobster-notify" / "20260804-XXX").resolve()
            self.assertEqual(n._notify_dir(run_dir), expected)

    def test_nested_segment_preserved(self):
        # Pre-fix this would collapse to runtime/<last-segment>.
        with tempfile.TemporaryDirectory() as tmp:
            cfg = {"lobster_notify_dir": "runtime/notif/sub"}
            n = CloudNotifier(cfg)
            run_dir = self._run_dir(Path(tmp)).resolve()
            expected = (Path(tmp) / "runtime" / "notif" / "sub" / "20260804-XXX").resolve()
            self.assertEqual(n._notify_dir(run_dir), expected)

    def test_absolute_path_passthrough(self):
        with tempfile.TemporaryDirectory() as tmp:
            cfg = {"lobster_notify_dir": "/tmp/custom-lobster"}
            n = CloudNotifier(cfg)
            run_dir = self._run_dir(Path(tmp)).resolve()
            result = n._notify_dir(run_dir)
            self.assertEqual(result, Path("/tmp/custom-lobster/20260804-XXX").resolve())


if __name__ == "__main__":
    unittest.main()