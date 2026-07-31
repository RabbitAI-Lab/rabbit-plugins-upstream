#!/usr/bin/env python3
"""Build an allowlisted, privacy-scanned ClawHub Skill archive."""

import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path


ALLOWED = [
    re.compile(r"^SKILL\.md$"),
    re.compile(r"^agents/openai\.yaml$"),
    re.compile(r"^scripts/[A-Za-z0-9_.-]+\.py$"),
    re.compile(r"^references/[A-Za-z0-9_.-]+\.md$"),
    re.compile(r"^assets/[A-Za-z0-9_.-]+\.(?:json|svg)$"),
]

DENIED_NAMES = re.compile(r"(^|/)(?:\.env|\.git|__pycache__|node_modules|logs?|cache|tmp)(/|$)", re.I)
DENIED_EXTENSIONS = {".mp3", ".wav", ".m4a", ".mp4", ".mov", ".jpg", ".jpeg", ".png", ".webp", ".srt"}
PATTERNS = {
    "windows_absolute_path": re.compile(r"[A-Za-z]:[\\/](?:Users|Documents|Desktop|AppData)[\\/]", re.I),
    "unix_home_path": re.compile(r"/(?:Users|home)/[^/\s]+/"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b"),
    "authorization_header": re.compile(r"\b(?:Authorization\s*:|Bearer\s+[A-Za-z0-9._-]{12,})", re.I),
    "cookie_header": re.compile(r"\bCookie\s*:", re.I),
    "assigned_secret": re.compile(r"\b(?:api[_-]?key|secret|password)\s*[=:]\s*['\"][^'\"]+", re.I),
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def allowed(path: str) -> bool:
    return any(pattern.fullmatch(path) for pattern in ALLOWED)


def scan_text(path: str, data: bytes, denied_terms):
    issues = []
    text = data.decode("utf-8", errors="replace")
    for label, pattern in PATTERNS.items():
        if pattern.search(text):
            issues.append(f"{path}: {label}")
    lowered = text.casefold()
    for term in denied_terms:
        if term.casefold() in lowered:
            issues.append(f"{path}: denied term {term!r}")
    return issues


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-dir", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--deny", action="append", default=[])
    args = parser.parse_args()

    root = Path(args.skill_dir).expanduser().resolve()
    output = Path(args.out).expanduser().resolve()
    if not (root / "SKILL.md").is_file():
        raise SystemExit("Skill folder has no SKILL.md")

    selected = []
    issues = []
    for file_path in sorted(path for path in root.rglob("*") if path.is_file()):
        relative = file_path.relative_to(root).as_posix()
        if DENIED_NAMES.search(relative) or file_path.suffix.lower() in DENIED_EXTENSIONS:
            continue
        if not allowed(relative):
            continue
        data = file_path.read_bytes()
        issues.extend(scan_text(relative, data, args.deny))
        selected.append((relative, data))

    if issues:
        print(json.dumps({"status": "fail", "issues": issues}, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    if not selected:
        raise SystemExit("No files selected")

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, data in selected:
            archive.writestr(f"{root.name}/{relative}", data)

    with zipfile.ZipFile(output, "r") as archive:
        archived = sorted(archive.namelist())
        expected = sorted(f"{root.name}/{relative}" for relative, _ in selected)
        if archived != expected:
            raise SystemExit("Archive verification failed")

    payload = output.read_bytes()
    result = {
        "status": "pass",
        "archive": output.name,
        "sha256": sha256_bytes(payload),
        "files": [relative for relative, _ in selected],
        "bytes": len(payload),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
