#!/usr/bin/env python3
"""Tests for _clean() terminal-injection sanitisation.

Inbox content (from, subject, body) is fully attacker-controlled, so _clean()
must strip anything that could inject terminal escapes or reorder rendered text
while leaving ordinary printable text (including non-ASCII) untouched.

Run: python3 scripts/test_clean.py
"""

import unittest

import dropmail


class TestClean(unittest.TestCase):
    def test_none_and_non_str(self):
        self.assertEqual(dropmail._clean(None), "")
        self.assertEqual(dropmail._clean(123), "123")

    def test_plain_text_preserved(self):
        self.assertEqual(dropmail._clean("Hello, World!"), "Hello, World!")

    def test_tab_and_newline_kept(self):
        self.assertEqual(dropmail._clean("a\tb\nc"), "a\tb\nc")

    def test_unicode_text_preserved(self):
        # Accents, CJK, emoji are printable and must survive.
        s = "Café — 日本語 — 🚀"
        self.assertEqual(dropmail._clean(s), s)

    # ── C0 controls / ANSI ────────────────────────────────────────────────
    def test_ansi_csi_stripped(self):
        # ESC [31m red ... ESC [0m reset
        payload = "\x1b[31mDANGER\x1b[0m"
        self.assertEqual(dropmail._clean(payload), "[31mDANGER[0m")

    def test_null_and_bell_stripped(self):
        self.assertEqual(dropmail._clean("a\x00b\x07c"), "abc")

    def test_del_stripped(self):
        self.assertEqual(dropmail._clean("a\x7fb"), "ab")

    # ── C1 controls (the T09 gap) ─────────────────────────────────────────
    def test_c1_csi_stripped(self):
        # U+009B is a single-byte CSI; U+009D is a single-byte OSC.
        payload = "a31mXrest"
        cleaned = dropmail._clean(payload)
        self.assertNotIn("", cleaned)
        self.assertNotIn("", cleaned)
        self.assertEqual(cleaned, "a31mXrest")

    def test_all_c1_range_stripped(self):
        for cp in range(0x80, 0xA0):
            ch = chr(cp)
            self.assertEqual(dropmail._clean(f"x{ch}y"), "xy", f"C1 U+{cp:04X}")

    # ── OSC sequence (title/clipboard hijack) ─────────────────────────────
    def test_osc_title_sequence_stripped(self):
        # ESC ] 0 ; pwned BEL  — would rewrite the terminal title.
        payload = "\x1b]0;pwned\x07legit"
        cleaned = dropmail._clean(payload)
        self.assertNotIn("\x1b", cleaned)
        self.assertNotIn("\x07", cleaned)
        self.assertEqual(cleaned, "]0;pwnedlegit")

    # ── Unicode bidi overrides / isolates (the T09 gap) ───────────────────
    def test_bidi_overrides_stripped(self):
        for cp in ("‪", "‫", "‬", "‭", "‮"):
            self.assertEqual(dropmail._clean(f"a{cp}b"), "ab", f"U+{ord(cp):04X}")

    def test_bidi_isolates_stripped(self):
        for cp in ("⁦", "⁧", "⁨", "⁩"):
            self.assertEqual(dropmail._clean(f"a{cp}b"), "ab", f"U+{ord(cp):04X}")

    def test_lrm_rlm_stripped(self):
        self.assertEqual(dropmail._clean("a‎‏b"), "ab")

    def test_bidi_spoof_example(self):
        # RLO can visually hide a trailing command; after cleaning the raw
        # bytes are back in logical order and the override is gone.
        payload = "invoice‮gnp.exe"
        cleaned = dropmail._clean(payload)
        self.assertNotIn("‮", cleaned)
        self.assertEqual(cleaned, "invoicegnp.exe")


if __name__ == "__main__":
    unittest.main()
