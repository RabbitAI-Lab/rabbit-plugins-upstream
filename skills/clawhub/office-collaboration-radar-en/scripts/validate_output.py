#!/usr/bin/env python3
"""Validate the English SkillHub package and its example outputs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SKILL_NAME = "office-collaboration-radar-en"
SKILL_VERSION = "0.1.1"
EVIDENCE_MAX_LEN = 80
CONFLICT_MARKER = "Conflict detected; human review required"

REQUIRED_HEADINGS = [
    "# Collaboration Status Card",
    "## Project Overview",
    "## Progress",
    "## Confirmed Decisions",
    "## Owner × Deadline Actions",
    "## Risks / Blockers / Dependencies",
    "## Cross-functional Relationships",
    "## Human Review Required",
    "## JSON Output",
]

REQUIRED_JSON_KEYS = [
    "project_overview",
    "progress",
    "confirmed_decisions",
    "action_items",
    "risks_dependencies",
    "cross_department_relationships",
    "needs_human_confirmation",
]

REQUIRED_FIELDS = {
    "project_overview": [
        "project_name", "time_range", "current_phase", "overall_status", "summary", "evidence",
    ],
    "progress": ["item", "status", "evidence"],
    "confirmed_decisions": ["decision", "result", "confirmed_by", "evidence"],
    "action_items": ["task", "owner", "department", "ddl", "deliverable", "status", "evidence"],
    "risks_dependencies": ["type", "description", "impact", "mitigation", "owner", "evidence"],
    "cross_department_relationships": ["from", "to", "collaboration_item", "status", "evidence"],
    "needs_human_confirmation": ["item", "reason", "suggested_confirm_with", "evidence"],
}

JSON_BLOCK_PATTERN = re.compile(r"```json\s*(\{.*?\})\s*```", re.DOTALL)
CHINESE_CHARACTER = re.compile(r"[\u3400-\u9fff]")
PII_PATTERNS = [
    re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    re.compile(r"(?<!\d)\d{17}[\dXx](?!\d)"),
]


def extract_json(markdown: str) -> dict:
    match = JSON_BLOCK_PATTERN.search(markdown)
    if not match:
        raise ValueError("missing fenced JSON object")
    payload = json.loads(match.group(1))
    if not isinstance(payload, dict):
        raise ValueError("JSON output must be an object")
    return payload


def validate_headings(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    positions: list[int] = []
    for heading in REQUIRED_HEADINGS:
        position = text.find(heading)
        if position < 0:
            errors.append(f"{path}: missing heading {heading}")
        else:
            positions.append(position)
    if len(positions) == len(REQUIRED_HEADINGS) and positions != sorted(positions):
        errors.append(f"{path}: headings are out of order")
    return errors


def validate_schema(path: Path, payload: dict) -> list[str]:
    errors: list[str] = []
    keys = list(payload)
    missing_keys = [key for key in REQUIRED_JSON_KEYS if key not in payload]
    if missing_keys:
        return [f"{path}: missing JSON keys {missing_keys}"]

    positions = [keys.index(key) for key in REQUIRED_JSON_KEYS]
    if positions != sorted(positions):
        errors.append(f"{path}: seven-module JSON keys are out of order")

    overview = payload["project_overview"]
    if not isinstance(overview, dict):
        errors.append(f"{path}: project_overview must be an object")
    else:
        for field in REQUIRED_FIELDS["project_overview"]:
            if field not in overview:
                errors.append(f"{path}: project_overview missing {field}")

    for section_name in REQUIRED_JSON_KEYS[1:]:
        section = payload[section_name]
        if not isinstance(section, list):
            errors.append(f"{path}: {section_name} must be a list")
            continue
        for index, item in enumerate(section):
            if not isinstance(item, dict):
                errors.append(f"{path}: {section_name}[{index}] must be an object")
                continue
            for field in REQUIRED_FIELDS[section_name]:
                if field not in item:
                    errors.append(f"{path}: {section_name}[{index}] missing {field}")
            evidence = item.get("evidence")
            if not isinstance(evidence, str) or not evidence.strip():
                errors.append(f"{path}: {section_name}[{index}] missing evidence")
            elif len(evidence) > EVIDENCE_MAX_LEN:
                errors.append(
                    f"{path}: {section_name}[{index}] evidence exceeds {EVIDENCE_MAX_LEN} characters"
                )

    action_items = payload.get("action_items") or []
    has_conflict = any(
        isinstance(item, dict) and item.get("conflict") == CONFLICT_MARKER
        for item in action_items
    )
    if has_conflict:
        review_items = payload.get("needs_human_confirmation") or []
        if not any(
            isinstance(item, dict) and item.get("evidence") == CONFLICT_MARKER
            for item in review_items
        ):
            errors.append(f"{path}: conflict has no matching human-review item")
    return errors


def validate_expected_output(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors = validate_headings(path, text)
    for pattern in PII_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path}: possible unredacted PII")
    try:
        payload = extract_json(text)
    except (ValueError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON output: {exc}")
        return errors
    errors.extend(validate_schema(path, payload))
    return errors


def validate_metadata(root: Path) -> list[str]:
    errors: list[str] = []
    skill_path = root / "SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8")
    for snippet in (
        f"name: {SKILL_NAME}",
        "description: >-",
    ):
        if snippet not in skill_text:
            errors.append(f"{skill_path}: missing {snippet}")

    agent_path = root / "agents" / f"{SKILL_NAME}.yaml"
    if not agent_path.exists():
        errors.append(f"{agent_path}: missing agent metadata")
    else:
        agent_text = agent_path.read_text(encoding="utf-8")
        for snippet in (
            f"version: {SKILL_VERSION}",
            f"Use ${SKILL_NAME}",
            "allow_implicit_invocation: true",
        ):
            if snippet not in agent_text:
                errors.append(f"{agent_path}: missing {snippet}")
    return errors


def validate_english_surface(root: Path) -> list[str]:
    errors: list[str] = []
    paths = [root / "SKILL.md"]
    paths.extend((root / "agents").glob("*.yaml"))
    paths.extend((root / "templates").glob("*.md"))
    paths.extend((root / "examples").glob("**/*"))
    for path in paths:
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml"}:
            if CHINESE_CHARACTER.search(path.read_text(encoding="utf-8")):
                errors.append(f"{path}: English-facing artifact contains Chinese text")
    return errors


def validate_package_hygiene(root: Path) -> list[str]:
    errors: list[str] = []
    forbidden_names = {".DS_Store", "__pycache__", ".clawhub", "dist"}
    for path in root.rglob("*"):
        if any(part in forbidden_names for part in path.relative_to(root).parts):
            errors.append(f"{path}: generated or local-only path must not be published")
        if path.is_symlink():
            errors.append(f"{path}: symbolic links are not allowed")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    errors.extend(validate_metadata(root))
    errors.extend(validate_english_surface(root))
    errors.extend(validate_package_hygiene(root))

    expected_outputs = sorted(root.glob("examples/*/expected-output.md"))
    if not expected_outputs:
        errors.append(f"{root}: no expected-output.md examples found")
    for path in expected_outputs:
        errors.extend(validate_expected_output(path))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    for path in expected_outputs:
        print(f"OK: {path.relative_to(root)}")
    print("ALL PASS -- English SkillHub package validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
