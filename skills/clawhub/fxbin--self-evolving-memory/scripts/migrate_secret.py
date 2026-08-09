#!/usr/bin/env python3
"""Atomically replace scanner-identified SECRET.md lines with safe locators.

The migration plan is model-safe: it contains only scanner locations and new
``secret://`` locators. This helper alone reads legacy plaintext and never
prints it. A plan must cover every current finding exactly, preventing partial
or stale rewrites.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any

from secret_control import LOCATOR, Finding, force_mode_0600, has_mode_0600, scan_secret_file


SAFE_METADATA = re.compile(r"^[\w .,-]{1,120}$", re.UNICODE)
SAFE_LAST4 = re.compile(r"^(?:\*{4}|[A-Za-z0-9]{4})$")


def public_result(migration_status: str, secret_file: Path) -> dict[str, object]:
    return {
        "migration_status": migration_status,
        "scan": scan_secret_file(secret_file).to_public_dict(),
        "mode_0600": has_mode_0600(secret_file),
    }


def load_plan(path: Path) -> list[dict[str, Any]] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        replacements = data["replacements"]
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError):
        return None
    return replacements if isinstance(replacements, list) else None


def replacement_map(replacements: list[dict[str, Any]], findings: tuple[Finding, ...]) -> dict[int, str] | None:
    expected = {(finding.rule_id, finding.line) for finding in findings}
    seen: set[tuple[str, int]] = set()
    rendered: dict[int, str] = {}
    allowed_optional = {"owner", "purpose", "last4"}

    for item in replacements:
        if not isinstance(item, dict) or set(item) - ({"rule_id", "line", "locator"} | allowed_optional):
            return None
        rule_id, line, locator = item.get("rule_id"), item.get("line"), item.get("locator")
        if not isinstance(rule_id, str) or not isinstance(line, int) or not isinstance(locator, str):
            return None
        key = (rule_id, line)
        if key not in expected or key in seen or LOCATOR.fullmatch(locator) is None:
            return None
        safe_fields = [f"- locator: {locator}"]
        for field in ("owner", "purpose", "last4"):
            value = item.get(field)
            if value is not None:
                if (
                    not isinstance(value, str)
                    or SAFE_METADATA.fullmatch(value) is None
                    or (field == "last4" and SAFE_LAST4.fullmatch(value) is None)
                ):
                    return None
                safe_fields.append(f"{field}: {value}")
        seen.add(key)
        rendered[line] = " | ".join(safe_fields)
    return rendered if seen == expected else None


def atomic_replace(path: Path, content: str) -> bool:
    try:
        fd, temp_name = tempfile.mkstemp(prefix=".secret-migration-", dir=path.parent)
        try:
            os.fchmod(fd, 0o600)
            with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temp_name, path)
        except Exception:
            try:
                os.unlink(temp_name)
            except OSError:
                pass
            raise
    except (OSError, UnicodeError):
        return False
    return force_mode_0600(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate SECRET.md without exposing plaintext")
    parser.add_argument("--secret-file", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--confirmed-by-user", action="store_true")
    args = parser.parse_args()
    secret_file = Path(args.secret_file)

    if not args.confirmed_by_user:
        print(json.dumps(public_result("user_confirmation_required", secret_file), ensure_ascii=False, sort_keys=True))
        return 2
    initial = scan_secret_file(secret_file)
    if initial.status != "plaintext_suspected":
        print(json.dumps(public_result("no_action", secret_file), ensure_ascii=False, sort_keys=True))
        return 2
    replacements = load_plan(Path(args.plan))
    rendered = replacement_map(replacements, initial.findings) if replacements is not None else None
    if rendered is None:
        print(json.dumps(public_result("plan_mismatch", secret_file), ensure_ascii=False, sort_keys=True))
        return 2
    try:
        lines = secret_file.read_text(encoding="utf-8").splitlines(keepends=True)
    except (OSError, UnicodeDecodeError):
        print(json.dumps(public_result("read_failed", secret_file), ensure_ascii=False, sort_keys=True))
        return 2
    for line_number, replacement in rendered.items():
        newline = "\n" if lines[line_number - 1].endswith("\n") else ""
        lines[line_number - 1] = replacement + newline
    if not atomic_replace(secret_file, "".join(lines)):
        print(json.dumps(public_result("atomic_replace_failed", secret_file), ensure_ascii=False, sort_keys=True))
        return 2
    final = public_result("applied", secret_file)
    print(json.dumps(final, ensure_ascii=False, sort_keys=True))
    return 0 if final["scan"]["status"] == "clean_locator_only" and final["mode_0600"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
