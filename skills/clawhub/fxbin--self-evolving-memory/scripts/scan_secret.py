#!/usr/bin/env python3
"""Emit the model-safe scanner result for a local SECRET.md file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from secret_control import scan_secret_file


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan SECRET.md without exposing its contents")
    parser.add_argument("--secret-file", required=True)
    args = parser.parse_args()
    result = scan_secret_file(Path(args.secret_file))
    print(json.dumps(result.to_public_dict(), ensure_ascii=False, sort_keys=True))
    return 0 if result.status in {"clean_locator_only", "plaintext_suspected"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
