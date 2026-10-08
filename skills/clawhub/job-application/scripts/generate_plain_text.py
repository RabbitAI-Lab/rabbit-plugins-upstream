#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from common import PROFILE_DIR, load_json, write_text


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a plain-text application.")
    parser.add_argument("--content", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--profile", type=Path, default=PROFILE_DIR / "master_profile.json")
    args = parser.parse_args()
    profile, content = load_json(args.profile), load_json(args.content)
    parts = [content.get("headline", ""), *content.get("paragraphs", []), profile["full_name"]]
    write_text(args.output, "\n\n".join(part.strip() for part in parts if part.strip()) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
