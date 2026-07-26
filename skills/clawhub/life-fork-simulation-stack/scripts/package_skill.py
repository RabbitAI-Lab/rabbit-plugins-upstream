#!/usr/bin/env python3
"""Build a clean, deterministic upload zip for this skill."""

from __future__ import annotations

import argparse
import stat
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXCLUDED_PARTS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "__MACOSX",
    "__pycache__",
}

EXCLUDED_NAMES = {
    ".DS_Store",
    "Thumbs.db",
}


def should_exclude(relative: Path) -> bool:
    if any(part in EXCLUDED_PARTS for part in relative.parts):
        return True
    if relative.name in EXCLUDED_NAMES:
        return True
    if relative.name.startswith("._"):
        return True
    if relative.suffix in {".pyc", ".pyo"}:
        return True
    return False


def package_files(output: Path) -> list[Path]:
    output_resolved = output.resolve()
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if should_exclude(relative):
            continue
        if path.resolve() == output_resolved:
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(ROOT).as_posix())


def zip_info(path: Path, archive_name: str) -> zipfile.ZipInfo:
    info = zipfile.ZipInfo(archive_name, date_time=(2020, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    mode = stat.S_IMODE(path.stat().st_mode)
    info.external_attr = (stat.S_IFREG | mode) << 16
    info.create_system = 3
    return info


def build_zip(output: Path) -> int:
    output = output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    files = package_files(output)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files:
            relative = path.relative_to(ROOT).as_posix()
            archive_name = f"{ROOT.name}/{relative}"
            archive.writestr(zip_info(path, archive_name), path.read_bytes())

    print(f"WROTE {output}")
    print(f"FILES {len(files)}")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build a clean upload zip for the skill.")
    parser.add_argument("output", type=Path, help="Output zip path.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return build_zip(args.output)


if __name__ == "__main__":
    raise SystemExit(main())
