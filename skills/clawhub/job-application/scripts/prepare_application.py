#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

from common import OUTPUT_DIR


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new application directory outside the skill installation.")
    parser.add_argument("--slug", required=True, help="Directory name in yyyy-mm-company-role form")
    parser.add_argument("--output-root", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--reuse", action="store_true", help="Return an existing directory instead of failing")
    args = parser.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-[a-z0-9][a-z0-9-]*", args.slug):
        raise SystemExit("Slug must match yyyy-mm-company-role using lowercase letters, digits, and hyphens")

    output_root = args.output_root.expanduser().resolve()
    application_dir = output_root / args.slug
    output_root.mkdir(parents=True, exist_ok=True)
    if application_dir.exists() and not args.reuse:
        raise SystemExit(f"Application directory already exists: {application_dir}")
    application_dir.mkdir(exist_ok=args.reuse)
    print(application_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
