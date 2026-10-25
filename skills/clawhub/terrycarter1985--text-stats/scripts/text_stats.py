#!/usr/bin/env python3
"""text_stats.py — Analyze a text/markdown file and print statistics."""

import argparse
import json
import os
import re
import sys
from collections import Counter


def analyze_text(text: str, top_n: int = 10, min_count: int = 2, wpm: int = 250):
    words = re.findall(r"[A-Za-z\u4e00-\u9fff]+", text)
    word_count = len(words)
    chars_raw = len(text)
    chars_no_spaces = len(re.sub(r"\s", "", text))
    sentences = len(re.findall(r"[.!?。！？]+", text)) or 1
    paragraphs = len([p for p in text.split(r"\n\n") if p.strip()]) or 1
    reading_time = max(1, round(word_count / wpm))

    stopwords = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "shall", "can", "not", "no",
        "that", "this", "these", "those", "it", "its", "i", "me", "my",
        "you", "your", "he", "she", "they", "we", "us", "them",
    }
    filtered = [w.lower() for w in words if w.lower() not in stopwords and len(w) > 1]
    top = Counter(filtered).most_common(top_n)
    top = [(w, c) for w, c in top if c >= min_count]

    return {
        "words": word_count,
        "chars_raw": chars_raw,
        "chars_no_spaces": chars_no_spaces,
        "sentences": sentences,
        "paragraphs": paragraphs,
        "reading_time_min": reading_time,
        "top_words": top,
    }


def print_report(filepath: str, stats: dict):
    name = os.path.basename(filepath)
    print(f"\n=== Text Stats: {name} ===")
    print(f"Words:        {stats['words']:,}")
    print(f"Chars (raw):  {stats['chars_raw']:,}")
    print(f"Chars (nosp): {stats['chars_no_spaces']:,}")
    print(f"Sentences:    {stats['sentences']:,}")
    print(f"Paragraphs:   {stats['paragraphs']:,}")
    print(f"Reading time: ~{stats['reading_time_min']} min (250 wpm)")
    if stats["top_words"]:
        print(f"\nMost common words (top {len(stats['top_words'])}):")
        line = "  ".join(f"{w} ({c})" for w, c in stats["top_words"])
        print(f"  {line}")
    print()


def process_path(path: str, top_n: int, min_count: int, wpm: int, as_json: bool):
    results = []
    if os.path.isfile(path):
        files = [path]
    elif os.path.isdir(path):
        files = []
        for root, _, fnames in os.walk(path):
            for f in sorted(fnames):
                if f.endswith((".txt", ".md")):
                    files.append(os.path.join(root, f))
    else:
        print(f"Error: {path} not found", file=sys.stderr)
        sys.exit(1)

    for fp in files:
        with open(fp, "r", encoding="utf-8", errors="replace") as f:
            text = f.read()
        stats = analyze_text(text, top_n, min_count, wpm)
        stats["file"] = os.path.basename(fp)
        results.append(stats)

        if as_json:
            print(json.dumps(stats, ensure_ascii=False))
        else:
            print_report(fp, stats)

    return results


def main():
    parser = argparse.ArgumentParser(description="Analyze text/markdown files.")
    parser.add_argument("path", help="File or directory to analyze")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--min-count", type=int, default=2)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--wpm", type=int, default=250)
    args = parser.parse_args()
    process_path(args.path, args.top, args.min_count, args.wpm, args.json)


if __name__ == "__main__":
    main()
