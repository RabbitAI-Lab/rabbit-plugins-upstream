#!/usr/bin/env python3
"""Helper to maintain MEMORY.md and regenerate the memory graph."""

import argparse
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
MEMORY_PATH = ROOT / "MEMORY.md"
GRAPH_DOT = ROOT / "memory_graph.dot"


def log(message: str):
    print(f"[{datetime.now(timezone.utc).isoformat()}] {message}")


def add_entry(section: str, entry: str):
    if not MEMORY_PATH.exists():
        raise FileNotFoundError(f"{MEMORY_PATH} not found")

    content = MEMORY_PATH.read_text(encoding="utf-8")
    pattern = rf"(## {re.escape(section)}\n)(.*?)(\n## |\Z)"
    match = re.search(pattern, content, re.S)
    if not match:
        raise ValueError(f"Section '{section}' not found in MEMORY.md")

    existing = match.group(2).rstrip()
    new_entry = entry.strip()
    if not new_entry.startswith("-"):
        new_entry = f"- {new_entry}"

    if new_entry in existing:
        log("Entry already exists. Skipping.")
        return

    updated = f"{existing}\n{new_entry}\n"
    new_content = content[:match.end(1)] + updated + content[match.end(2):]
    MEMORY_PATH.write_text(new_content, encoding="utf-8")
    log(f"Added entry to '{section}'")


def rebuild_graph():
    if not GRAPH_DOT.exists():
        raise FileNotFoundError(f"{GRAPH_DOT} not found")
    for fmt in ["svg", "png"]:
        out = ROOT / f"memory_graph.{fmt}"
        subprocess.run(["dot", f"-T{fmt}", str(GRAPH_DOT), "-o", str(out)], check=True)
        log(f"Rebuilt {out}")


def main():
    parser = argparse.ArgumentParser(description="Maintain memory files")
    parser.add_argument("--section", help="Section in MEMORY.md to append to")
    parser.add_argument("--entry", help="Entry text to add")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild memory graph images")
    args = parser.parse_args()

    if args.section and args.entry:
        add_entry(args.section, args.entry)

    if args.rebuild or (args.section and args.entry):
        rebuild_graph()


if __name__ == "__main__":
    main()
