#!/usr/bin/env python3
"""JSON Tool - format, validate, minify, and query JSON data."""

import json
import sys
import argparse


def read_input(file_path: str | None) -> str:
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return sys.stdin.read()


def format_json(text: str, indent: int = 2) -> str:
    data = json.loads(text)
    return json.dumps(data, indent=indent, ensure_ascii=False)


def minify_json(text: str) -> str:
    data = json.loads(text)
    return json.dumps(data, separators=(",", ":"), ensure_ascii=False)


def validate_json(text: str) -> str:
    json.loads(text)
    return "Valid JSON"


def main():
    parser = argparse.ArgumentParser(description="JSON Tool")
    parser.add_argument("action", choices=["format", "minify", "validate"], help="Action to perform")
    parser.add_argument("file", nargs="?", help="Input file (default: stdin)")
    parser.add_argument("--indent", type=int, default=2, help="Indentation for format (default: 2)")
    args = parser.parse_args()

    text = read_input(args.file)

    if args.action == "format":
        print(format_json(text, args.indent))
    elif args.action == "minify":
        print(minify_json(text))
    elif args.action == "validate":
        print(validate_json(text))


if __name__ == "__main__":
    main()
