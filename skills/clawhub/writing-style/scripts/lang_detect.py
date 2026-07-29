#!/usr/bin/env python3
"""Detect input language from stdin and print the matching style rule.

Read-only: reads stdin (if piped) and prints the detected language plus
its locale-appropriate convention. No filesystem writes.
"""

import sys
import unicodedata


LOCALE_RULES = {
    "zh": "Use Traditional Chinese punctuation (，。！？). Avoid mixed CJK/Latin spacing.",
    "ja": "Use Japanese-style spacing and punctuation (。、). Prefer polite register.",
    "ko": "Apply Korean spacing rules. Use formal speech level by default.",
    "en": "Use Oxford comma. Prefer -ize over -ise spelling.",
}


def detect_script(text):
    cjk_count = sum(
        1 for c in text
        if unicodedata.category(c) in ("Lo",) and
        unicodedata.name(c, "").startswith(("CJK", "HANGUL", "HIRAGANA", "KATAKANA"))
    )
    ratio = cjk_count / max(len(text), 1)
    if ratio > 0.3:
        names = [unicodedata.name(c, "") for c in text if unicodedata.category(c) == "Lo"]
        if any("HANGUL" in n for n in names):
            return "ko"
        if any(n.startswith(("HIRAGANA", "KATAKANA")) for n in names):
            return "ja"
        return "zh"
    return "en"


def main():
    text = sys.stdin.read() if not sys.stdin.isatty() else ""
    lang = detect_script(text) if text.strip() else "en"
    rule = LOCALE_RULES.get(lang, LOCALE_RULES["en"])
    print(f"[ok] detected language: {lang}")
    print(f"[info] style rule: {rule}")


if __name__ == "__main__":
    main()
