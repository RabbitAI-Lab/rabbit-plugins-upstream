"""Trusted local controls for handle-only ``SECRET.md`` files.

This module is intentionally independent of model-visible memory data. Callers
may expose only ``ScanResult.to_public_dict()``; they must never log or return
the file content, matched values, captures, hashes, or absolute file paths.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path


ASSIGNMENT_VALUE = re.compile(
    r"(?i)\b(?:api[_ -]?key|password|passwd|token|secret|private[_ -]?key|cookie)\b\s*(?:=|:)\s*\S+"
)
KNOWN_CREDENTIAL = re.compile(
    r"(?i)(?:\bsk-[a-z0-9_-]{12,}\b|\bgh[pousr]_[a-z0-9]{20,}\b|"
    r"\bAKIA[0-9A-Z]{16}\b|\beyJ[a-z0-9_-]{10,}\.[a-z0-9_-]{10,}\.)"
)
LOCATOR = re.compile(r"secret://[a-z0-9][a-z0-9._/-]*", re.IGNORECASE)


@dataclass(frozen=True)
class Finding:
    rule_id: str
    line: int
    column_bucket: str

    def public_dict(self) -> dict[str, object]:
        return {
            "rule_id": self.rule_id,
            "line": self.line,
            "column_bucket": self.column_bucket,
        }


@dataclass(frozen=True)
class ScanResult:
    status: str
    findings: tuple[Finding, ...]

    def to_public_dict(self) -> dict[str, object]:
        return {
            "status": self.status,
            "match_count": len(self.findings),
            "redacted_locations": [finding.public_dict() for finding in self.findings],
        }


def _bucket(column: int) -> str:
    """Return a non-reversible 16-column bucket label."""
    start = ((column - 1) // 16) * 16 + 1
    return f"{start}-{start + 15}"


def _finding_for_line(line: str, line_number: int) -> Finding | None:
    if not line.strip() or line.lstrip().startswith(("#", ">")):
        return None
    # A sanctioned locator may appear after a descriptive `secret`/`token`
    # label. Remove only that non-sensitive locator before testing the remaining
    # text, so the migration helper's own output scans clean while any trailing
    # credential material is still detected.
    without_locators = LOCATOR.sub("", line)
    assignment = ASSIGNMENT_VALUE.search(without_locators)
    if assignment:
        return Finding("assignment_value", line_number, _bucket(assignment.start() + 1))
    credential = KNOWN_CREDENTIAL.search(without_locators)
    if credential:
        return Finding("credential_pattern", line_number, _bucket(credential.start() + 1))
    return None


def scan_secret_file(path: Path) -> ScanResult:
    """Scan locally without exposing content to the result object."""
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeDecodeError):
        return ScanResult("scan_error", ())

    findings = tuple(
        finding
        for number, line in enumerate(text.splitlines(), start=1)
        if (finding := _finding_for_line(line, number)) is not None
    )
    status = "plaintext_suspected" if findings else "clean_locator_only"
    return ScanResult(status, findings)


def has_mode_0600(path: Path) -> bool:
    try:
        return (path.stat().st_mode & 0o777) == 0o600
    except OSError:
        return False


def force_mode_0600(path: Path) -> bool:
    try:
        os.chmod(path, 0o600)
    except OSError:
        return False
    return has_mode_0600(path)
