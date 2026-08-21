#!/usr/bin/env python3
"""Build a byte-for-byte reproducible Skill submission archive."""

from __future__ import annotations

import hashlib
import re
import stat
import zipfile
from pathlib import Path


FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
EXCLUDED_DIRECTORIES = {
    ".clawhub",
    ".git",
    "__MACOSX",
    "__pycache__",
    "dist",
    "node_modules",
    "temp",
    "tmp",
}
EXCLUDED_NAMES = {".DS_Store", ".clawhubignore"}
EXCLUDED_SUFFIXES = {".bak", ".log", ".pyc", ".tmp"}
SKILL_NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def read_skill_name(root: Path) -> str:
    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.search(r"(?m)^name:\s*['\"]?([^'\"\s]+)['\"]?\s*$", skill_text)
    if not match:
        raise ValueError("SKILL.md frontmatter is missing the name field")

    skill_name = match.group(1)
    if not SKILL_NAME_PATTERN.fullmatch(skill_name):
        raise ValueError(f"Invalid skill name: {skill_name}")
    return skill_name


def is_included(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    if set(relative.parts).intersection(EXCLUDED_DIRECTORIES):
        return False
    if path.name in EXCLUDED_NAMES or path.name.startswith("._"):
        return False
    if path.name.endswith("~"):
        return False
    return path.suffix.lower() not in EXCLUDED_SUFFIXES


def collect_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symbolic links are not allowed in the package: {path}")
        if path.is_file() and is_included(path, root):
            files.append(path)
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def archive_mode(path: Path) -> int:
    source_mode = path.stat().st_mode
    return 0o755 if source_mode & stat.S_IXUSR else 0o644


def write_archive(root: Path, archive_path: Path, skill_name: str) -> None:
    temporary_path = archive_path.with_name(f".{archive_path.name}.tmp")
    files = collect_files(root)

    try:
        with zipfile.ZipFile(
            temporary_path,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        ) as archive:
            for path in files:
                relative = path.relative_to(root).as_posix()
                info = zipfile.ZipInfo(
                    f"{skill_name}/{relative}",
                    date_time=FIXED_TIMESTAMP,
                )
                info.create_system = 3
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = archive_mode(path) << 16
                archive.writestr(info, path.read_bytes(), compresslevel=9)
        temporary_path.replace(archive_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    skill_name = read_skill_name(root)
    dist = root / "dist"
    archive_path = dist / f"{skill_name}.zip"
    checksum_path = archive_path.with_suffix(f"{archive_path.suffix}.sha256")

    dist.mkdir(parents=True, exist_ok=True)
    write_archive(root, archive_path, skill_name)
    checksum = sha256(archive_path)
    checksum_path.write_text(
        f"{checksum}  {archive_path.name}\n",
        encoding="utf-8",
    )

    print(f"Packaged {archive_path}")
    print(f"SHA-256 {checksum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
