"""Tests for the draft-mode save-draft click path.

Background: the original draft mode only filled the form and returned
without clicking anything server-side. The browser then closed and the
content was lost — drafts created on the server never appeared on the
user's phone (same account). Fix landed 2026-08-04: draft mode now
clicks the 保存草稿 button and verifies a toast/URL signal.

These tests lock in:
- selectors.json exposes save_draft_button_any + save_draft_success_any
- publisher.py exposes save_draft_and_wait + click_save_draft_button
- click_save_draft_button does not accidentally hit the 发布 button
  (save_draft_button_any excludes 发布 in the role/text selectors)
"""

import json
import sys
import unittest
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SKILL_ROOT))

from src.publisher import XhsPublisher  # noqa: E402


SELECTORS_PATH = SKILL_ROOT / "config" / "selectors.json"


class TestSelectors(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.selectors = json.loads(SELECTORS_PATH.read_text(encoding="utf-8"))

    def test_save_draft_button_any_present(self):
        self.assertIn("save_draft_button_any", self.selectors)
        entries = self.selectors["save_draft_button_any"]
        self.assertGreater(len(entries), 0, "save_draft_button_any must have at least one selector")
        for entry in entries:
            self.assertIn(entry.get("kind"), {"text", "role", "css", "placeholder"})

    def test_save_draft_button_excludes_publish(self):
        # The draft click path must never accidentally trigger the publish
        # button. Verify no entry in save_draft_button_any matches 发布.
        for entry in self.selectors["save_draft_button_any"]:
            value = entry.get("value") or entry.get("name") or ""
            self.assertNotEqual(
                value, "发布",
                "save_draft_button_any must not point at the publish button (发布); the click path is separate",
            )

    def test_save_draft_success_any_present(self):
        self.assertIn("save_draft_success_any", self.selectors)
        entries = self.selectors["save_draft_success_any"]
        self.assertGreater(len(entries), 0)
        # Must include at least one Chinese success phrase so DOM probes
        # work on the localized creator backend.
        texts = [e.get("value") for e in entries if e.get("kind") == "text"]
        self.assertTrue(any(t for t in texts if "保存" in (t or "") or "草稿" in (t or "")))

    def test_publish_button_any_unchanged(self):
        # Regression guard: adding save_draft selectors must not perturb
        # the existing publish_button_any entries.
        self.assertIn("publish_button_any", self.selectors)
        values = [e.get("value") or e.get("name") for e in self.selectors["publish_button_any"]]
        self.assertIn("发布", values)

    def test_save_draft_button_covers_xhs_real_labels(self):
        # Per user feedback 2026-08-04, the actual Xiaohongshu web creator
        # labels are 保存草稿 / 存草稿 / 暂存离开 (the last one appears in
        # the leave-confirmation dialog). Lock all three in so we don't
        # regress to only 存草稿.
        labels = {e.get("value") or e.get("name") for e in self.selectors["save_draft_button_any"]}
        for required in ("保存草稿", "存草稿", "暂存离开"):
            self.assertIn(required, labels, f"{required} must be present in save_draft_button_any")


class TestPublisherSurface(unittest.TestCase):
    """Smoke-test that the new methods exist on XhsPublisher with the right shape."""

    def test_save_draft_and_wait_is_coroutine(self):
        method = getattr(XhsPublisher, "save_draft_and_wait", None)
        self.assertTrue(callable(method), "XhsPublisher.save_draft_and_wait must be defined")
        # Methods defined with `async def` on a class are coroutine functions.
        import inspect
        self.assertTrue(inspect.iscoroutinefunction(method), "save_draft_and_wait must be async")

    def test_click_save_draft_button_is_coroutine(self):
        method = getattr(XhsPublisher, "click_save_draft_button", None)
        self.assertTrue(callable(method), "XhsPublisher.click_save_draft_button must be defined")
        import inspect
        self.assertTrue(inspect.iscoroutinefunction(method), "click_save_draft_button must be async")

    def test_run_dispatches_to_save_draft(self):
        """The draft branch in run() must route to save_draft_and_wait, not
        a silent return. Inspect the source to make sure the contract
        hasn't drifted back to the buggy version."""
        src = (SKILL_ROOT / "src" / "publisher.py").read_text(encoding="utf-8")
        self.assertIn("if content.mode == \"draft\":", src)
        # The body between the if and the publish branch must call save_draft_and_wait.
        # Use a coarse substring check — sufficient for a regression guard.
        self.assertIn("await self.save_draft_and_wait()", src)
        self.assertNotIn(
            "\"status\": \"draft_ready\"",
            src,
            "the legacy draft_ready return was a known-bug pattern (form data lost on close)",
        )


if __name__ == "__main__":
    unittest.main()