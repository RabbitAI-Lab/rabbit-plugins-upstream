#!/usr/bin/env python3
"""Text statistics: char/word/sentence/paragraph counts and reading time.

Usage:
    python text_stats.py <file>
    echo "some text" | python text_stats.py
"""
import json
import math
import re
import sys


def read_input() -> str:
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            return f.read()
    return sys.stdin.read()


def stats(text: str) -> dict:
    chars = len(text)
    chars_no_space = len(re.sub(r"\s", "", text))
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", text))
    latin_words = len(re.findall(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*", text))
    sentences = len([s for s in re.split(r"[。！？.!?]+", text) if s.strip()])
    paragraphs = len([p for p in re.split(r"\n\s*\n", text) if p.strip()])

    # 阅读时长：中文约 400 字/分钟，英文约 200 词/分钟
    reading_minutes = round(cjk_chars / 400 + latin_words / 200, 1)

    return {
        "chars": chars,
        "chars_no_space": chars_no_space,
        "cjk_chars": cjk_chars,
        "latin_words": latin_words,
        "sentences": sentences,
        "paragraphs": paragraphs,
        "reading_minutes": max(reading_minutes, 0.1) if text.strip() else 0,
    }


def main() -> None:
    text = read_input()
    if not text.strip():
        print(json.dumps({"error": "empty input"}, ensure_ascii=False))
        sys.exit(1)
    print(json.dumps(stats(text), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
