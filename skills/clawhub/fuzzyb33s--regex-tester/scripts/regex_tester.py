#!/usr/bin/env python3
"""Regex tester - test and debug regular expressions with real-time matching."""

import re
import sys
import json
import argparse
from typing import Optional


COMMON_PATTERNS = {
    "email": (r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "Email address"),
    "url": (r"https?://[^\s]+", "HTTP/HTTPS URL"),
    "ipv4": (r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IPv4 address"),
    "uuid": (r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", "UUID"),
    "phone": (r"\+?[\d\s\-()]{10,}", "Phone number"),
    "date-iso": (r"\d{4}-\d{2}-\d{2}", "ISO date (YYYY-MM-DD)"),
    "time-24h": (r"([01]?\d|2[0-3]):[0-5]\d", "24-hour time"),
    "hex-color": (r"#[0-9a-fA-F]{3,8}\b", "Hex color code"),
    "slug": (r"[a-z0-9]+(?:-[a-z0-9]+)*", "URL slug"),
    "credit-card": (r"\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}", "Credit card number"),
    "hashtag": (r"#[a-zA-Z0-9_]+", "Hashtag"),
    "mention": (r"@[a-zA-Z0-9_]+", "@mention"),
    "integer": (r"-?\d+", "Integer"),
    "float": (r"-?\d+\.?\d*", "Float number"),
    "html-tag": (r"<[^>]+>", "HTML tag"),
    "whitespace": (r"\s+", "Whitespace runs"),
    "word": (r"\b\w+\b", "Word"),
    "line": (r".+$", "Line"),
}


def build_flags(flag_str: str) -> int:
    flags = 0
    if "i" in flag_str:
        flags |= re.IGNORECASE
    if "m" in flag_str:
        flags |= re.MULTILINE
    if "s" in flag_str:
        flags |= re.DOTALL
    return flags


def list_patterns():
    print("\nCommon Patterns:\n")
    print(f"  {'Name':<16} {'Description':<30} Pattern")
    print(f"  {'-'*14} {'-'*30} {'-'*40}")
    for name, (pat, desc) in sorted(COMMON_PATTERNS.items()):
        print(f"  {name:<16} {desc:<30} {pat}")
    print()


def test_regex(pattern: str, text: str, flags: int, as_json: bool = False) -> int:
    try:
        compiled = re.compile(pattern, flags)
    except re.error as e:
        if as_json:
            print(json.dumps({"valid": False, "error": str(e)}))
        else:
            print(f"Invalid regex: {e}", file=sys.stderr)
        return 2

    matches = list(compiled.finditer(text))

    if as_json:
        result = {
            "valid": True,
            "pattern": pattern,
            "text": text,
            "match_count": len(matches),
            "matches": [],
        }
        for m in matches:
            match_data = {
                "match": m.group(),
                "start": m.start(),
                "end": m.end(),
                "groups": list(m.groups()) if m.groups() else None,
            }
            result["matches"].append(match_data)
        print(json.dumps(result, indent=2))
    else:
        print(f"Pattern: {pattern}")
        print(f"Text:    \"{text[:60]}{'...' if len(text) > 60 else ''}\"\n")

        if not matches:
            print("No matches found.")
            return 1

        print(f"Matches: {len(matches)} found")
        for i, m in enumerate(matches):
            group_str = f" (pos {m.start()}-{m.end()})"
            print(f"  [{i}] \"{m.group()}\"{group_str}")

        # Show groups
        first_with_groups = next((m for m in matches if m.groups()), None)
        if first_with_groups:
            print("\nGroups:")
            for i, g in enumerate(first_with_groups.groups(), 1):
                print(f"  [{i}] \"{g}\"")

    return 0


def main():
    parser = argparse.ArgumentParser(description="Test and debug regular expressions.")
    parser.add_argument("--pattern", "-p", help="Regex pattern to test")
    parser.add_argument("--text", "-t", help="Test string to match against")
    parser.add_argument("--flags", "-f", default="", help="Flags: i (ignorecase), m (multiline), s (dotall)")
    parser.add_argument("--json", "-j", action="store_true", help="Output as JSON")
    parser.add_argument("--list-patterns", "-l", action="store_true", help="List common patterns")

    args = parser.parse_args()

    if args.list_patterns:
        list_patterns()
        return 0

    if not args.pattern:
        print("Error: --pattern is required (or use --list-patterns)", file=sys.stderr)
        return 2

    # Check if pattern is a shorthand name
    if args.pattern in COMMON_PATTERNS:
        actual_pattern, _ = COMMON_PATTERNS[args.pattern]
        args.pattern = actual_pattern

    if args.text is None:
        print("Enter test text (Ctrl+Z / Ctrl+D to finish):", file=sys.stderr)
        text = sys.stdin.read().rstrip("\n")
    else:
        text = args.text

    flags = build_flags(args.flags)
    return test_regex(args.pattern, text, flags, args.json)


if __name__ == "__main__":
    sys.exit(main())
