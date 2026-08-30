#!/usr/bin/env python3
"""Create a new animation project from the bundled Remotion starter."""

import argparse
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Copy the English-learning Remotion starter into an empty directory."
    )
    parser.add_argument("target", type=Path)
    args = parser.parse_args()

    source = Path(__file__).resolve().parent.parent / "assets" / "remotion-starter"
    target = args.target.expanduser().resolve()

    if not source.is_dir():
        raise SystemExit(f"starter not found: {source}")
    if target.exists() and any(target.iterdir()):
        raise SystemExit(
            f"target must be new or empty; refusing to overwrite existing files: {target}"
        )

    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, dirs_exist_ok=True)
    print(f"initialized project: {target}")
    print("next: add transparent cutouts under public/assets/layers/")
    print("then: edit voice-manifest.json and script.json")


if __name__ == "__main__":
    main()
