#!/usr/bin/env python3
"""Validate metadata and record fields in platform rule Markdown files."""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLATFORMS = ROOT / "references" / "platforms"
REQUIRED_FILE_FIELDS = {
    "platform",
    "display_name",
    "jurisdiction",
    "official_policy_url",
    "last_checked",
    "status",
}
FILE_STATUSES = {"active", "partial", "stale", "archived"}
REQUIRED_RULE_FIELDS = {
    "Authority",
    "Status",
    "Surfaces",
    "Risk default",
    "Source",
    "Published or observed",
    "Verified",
    "Summary",
    "Notes",
}
AUTHORITIES = {"law", "official", "campaign", "heuristic", "unknown"}
RULE_STATUSES = {"active", "superseded", "disputed", "stale", "unknown"}
RISK_LEVELS = {"prohibited", "high", "medium", "low", "verify"}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}, text
    metadata: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"\'')
    return metadata, text[match.end() :]


def valid_date(value: str) -> bool:
    if value == "unknown":
        return True
    try:
        dt.date.fromisoformat(value)
        return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value))
    except ValueError:
        return False


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    metadata, body = parse_frontmatter(path.read_text(encoding="utf-8"))
    missing = REQUIRED_FILE_FIELDS - metadata.keys()
    if missing:
        errors.append(f"missing file metadata: {', '.join(sorted(missing))}")
        return errors
    if metadata["status"] not in FILE_STATUSES:
        errors.append(f"invalid file status: {metadata['status']}")
    if not valid_date(metadata["last_checked"]):
        errors.append(f"invalid last_checked date: {metadata['last_checked']}")

    headings = list(
        re.finditer(r"^## ([A-Z0-9]+(?:-[A-Z0-9]+)*-[0-9]{3,}): .+$", body, re.MULTILINE)
    )
    if not headings:
        if metadata["status"] != "partial":
            errors.append("no rule records found; use file status partial while extraction is pending")
        return errors

    seen: set[str] = set()
    for index, heading in enumerate(headings):
        rule_id = heading.group(1)
        if rule_id in seen:
            errors.append(f"duplicate rule ID: {rule_id}")
        seen.add(rule_id)
        end = headings[index + 1].start() if index + 1 < len(headings) else len(body)
        record = body[heading.end() : end]
        fields = dict(re.findall(r"^- ([A-Za-z ]+):\s*(.*)$", record, re.MULTILINE))
        missing_fields = REQUIRED_RULE_FIELDS - fields.keys()
        if missing_fields:
            errors.append(f"{rule_id} missing fields: {', '.join(sorted(missing_fields))}")
            continue
        if fields["Authority"] not in AUTHORITIES:
            errors.append(f"{rule_id} invalid Authority: {fields['Authority']}")
        if fields["Status"] not in RULE_STATUSES:
            errors.append(f"{rule_id} invalid Status: {fields['Status']}")
        if fields["Risk default"] not in RISK_LEVELS:
            errors.append(f"{rule_id} invalid Risk default: {fields['Risk default']}")
        for date_field in ("Published or observed", "Verified"):
            if not valid_date(fields[date_field]):
                errors.append(f"{rule_id} invalid {date_field} date: {fields[date_field]}")
    return errors


def main() -> int:
    files = sorted(path for path in PLATFORMS.glob("*.md") if path.name != "index.md")
    if not files:
        print("OK: no platform rule files yet")
        return 0

    total_errors = 0
    for path in files:
        errors = validate_file(path)
        if errors:
            total_errors += len(errors)
            for error in errors:
                print(f"ERROR {path.relative_to(ROOT)}: {error}")
        else:
            print(f"OK: {path.relative_to(ROOT)}")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main())
