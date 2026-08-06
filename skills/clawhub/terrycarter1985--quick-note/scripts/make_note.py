#!/usr/bin/env python3
"""Append a timestamped note to today's daily note file."""

import argparse
import datetime
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="Quick note to daily file")
    parser.add_argument("text", help="Note content")
    parser.add_argument("--dir", default="./notes", help="Notes directory")
    parser.add_argument("--tag", action="append", default=[], help="Tag prefix")
    args = parser.parse_args()

    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")

    tag_str = " ".join(f"[{t}]" for t in args.tag)
    line = f"- {time_str} {tag_str} {args.text}".rstrip() + "\n"

    os.makedirs(args.dir, exist_ok=True)
    filepath = os.path.join(args.dir, f"{date_str}.md")

    # Add header if new file
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write(f"# Notes for {date_str}\n\n")

    with open(filepath, "a") as f:
        f.write(line)

    print(f"Added note to {filepath}")


if __name__ == "__main__":
    main()
