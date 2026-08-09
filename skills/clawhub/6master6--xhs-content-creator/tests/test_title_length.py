"""Tests for title length accounting (per SKILL.md §1.5).

The 2026-08-04 history: an earlier over-broad rule
(sum 2 if ord(c) > 0x2600) double-counted every CJK character and
fullwidth punctuation, contradicting the documented "emoji weight 2
chars, everything else weight 1" semantic. This file locks the
corrected rule in via the historical regression cases at the bottom.
"""

import unittest

import sys
from pathlib import Path

# Make sibling scripts/ importable without a package marker.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from validate_content import title_len_xhs


class TestTitleLength(unittest.TestCase):
    def test_pure_chinese_chars_count_one(self):
        self.assertEqual(title_len_xhs("示例公园"), 4)

    def test_emoji_counts_as_two(self):
        # U+1F304 is in the Misc Symbols & Pictographs emoji range.
        # 🌄(2) + space(1) + 示例公园(4) = 7
        n = title_len_xhs("🌄 示例公园")
        self.assertEqual(n, 7)

    def test_cjk_chars_count_one_each(self):
        # SKILL.md §1.5 semantics: only emoji weigh 2, CJK chars weigh 1.
        self.assertEqual(title_len_xhs("示例公园"), 4)

    def test_fullwidth_pipe_counts_as_one(self):
        # U+FF5C ｜ — fullwidth punctuation is NOT in the emoji range,
        # so it weights 1. (The original failure was caused by
        # over-counting fullwidth chars.)
        # 示例公园(4) + ｜(1) + 被遗忘的远方(6) = 11
        n = title_len_xhs("示例公园｜被遗忘的远方")
        self.assertEqual(n, 11)

    def test_middot_counts_as_one(self):
        # U+00B7 · — below the emoji range, counts as 1.
        # Use it as a single-char separator instead of ｜ to save space.
        # 示例公园(4) + ·(1) + 城市远方(4) = 9
        n = title_len_xhs("示例公园·城市远方")
        self.assertEqual(n, 9)

    def test_typical_emoji_chinese_title_under_limit(self):
        # A realistic 10-char title with one emoji (🌄 + 8 CJK + · + 4 CJK).
        # = 2 + 1 + 4 + 1 + 4 = 12 (under 20 cap).
        n = title_len_xhs("🌄 示例公园·城市远方")
        self.assertLessEqual(n, 20)

    def test_under_limit_passes(self):
        n = title_len_xhs("🌄 示例公园·城市远方")
        self.assertLessEqual(n, 20)

    def test_empty_title(self):
        self.assertEqual(title_len_xhs(""), 0)


class TestTitleLengthHistoricalRegression(unittest.TestCase):
    """Regression cases for the over-broad title-length bug.

    Pre-fix, titles mixing emoji + CJK + ｜ were double-counted because
    every codepoint above U+2600 (including CJK and fullwidth punct)
    was counted as 2 chars. After tightening to "emoji range only",
    titles that previously failed the 20-char cap now fit.
    """

    def test_fullwidth_pipe_in_long_title_under_limit(self):
        # The historical failure mode: a title with emoji + CJK + ｜
        # would trip the 20-char cap because ｜ was double-counted.
        # Under the fixed rule, this title weighs 17 chars.
        title = "🌄 示例公园｜被遗忘的远方"
        self.assertLessEqual(title_len_xhs(title), 20)

    def test_long_emoji_cjk_title_under_limit(self):
        # Stress: a longer title that exercised the same bug.
        title = "🌄 " + "示例" * 6 + "｜" + "被遗忘的远方"
        # 🌄(2) + (1) + 示例×6(12) + ｜(1) + 被遗忘的远方(6) = 22
        self.assertGreater(title_len_xhs(title), 20)  # still over
        # but the emoji + CJK component sum (without ｜) is well under.
        self.assertLessEqual(title_len_xhs(title), 25)


if __name__ == "__main__":
    unittest.main()