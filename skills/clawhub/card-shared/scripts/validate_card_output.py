#!/usr/bin/env python3
"""Validate a card command markdown response against the shared command contracts."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required to run this validator.") from exc


ROOT = Path(__file__).resolve().parent.parent
CONTRACTS_PATH = ROOT / "command-contracts.yaml"


def load_contracts() -> dict:
    return yaml.safe_load(CONTRACTS_PATH.read_text(encoding="utf-8"))


def extract_yaml_block(content: str) -> str:
    """Extract YAML from an HTML comment block only.

    YAML must be hidden inside <!-- --> comments. Bare fenced YAML blocks
    are not accepted — they would be visible to the user, violating the
    compact output rules.
    """
    match = re.search(r"<!--\s*```yaml\n(.*?)\n```\s*-->", content, re.DOTALL)
    if match:
        return match.group(1)
    raise ValueError(
        "Missing YAML block inside HTML comment. "
        "YAML must be wrapped in <!-- ```yaml ... ``` -->."
    )


def validate_sections(content: str, heading_prefix: str, sections: list[str]) -> list[str]:
    errors = []
    if heading_prefix and not re.search(r"^# ", content, re.MULTILINE):
        errors.append(f"Missing heading prefix: {heading_prefix}")

    last_index = -1
    for section in sections:
        index = content.find(section)
        if index == -1:
            errors.append(f"Missing required section: {section}")
            continue
        if index < last_index:
            errors.append(f"Section out of order: {section}")
        last_index = index
    return errors


def validate_yaml_data(data: dict, contract: dict) -> list[str]:
    errors = []
    for key in contract.get("required_top_level_keys", []):
        if key not in data:
            errors.append(f"Missing YAML key: {key}")
    for key in contract.get("list_keys", []):
        if key in data and not isinstance(data[key], list):
            errors.append(f"YAML key must be a list: {key}")
    for key in contract.get("object_keys", []):
        if key in data and not isinstance(data[key], dict):
            errors.append(f"YAML key must be an object: {key}")
    return errors


def validate_no_visible_yaml(content: str) -> list[str]:
    """Check that YAML blocks are only inside HTML comments, not visible."""
    errors = []
    stripped = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    if re.search(r"```yaml", stripped):
        errors.append("Visible YAML block found outside HTML comment. YAML must be hidden in <!-- --> comments.")
    return errors


def validate_no_visible_links(content: str) -> list[str]:
    """Check that no inline links appear in user-visible output."""
    errors = []
    stripped = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    if re.search(r"\[.*?\]\(https?://.*?\)", stripped):
        errors.append("Visible inline link found. Links should not appear in user-facing output.")
    if re.search(r"https?://\S+", stripped):
        errors.append("Visible raw URL found. URLs should not appear in user-facing output.")
    return errors


def validate_no_why_it_matters(content: str) -> list[str]:
    """Check that no 'Why It Matters' section exists."""
    errors = []
    stripped = re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)
    if re.search(r"^## .*Why It Matters", stripped, re.MULTILINE | re.IGNORECASE):
        errors.append("Found 'Why It Matters' section. This section has been removed from the compact format.")
    return errors


def validate_last_validated(data: dict) -> list[str]:
    """Check that the YAML block includes a last_validated date."""
    errors = []
    if "last_validated" not in data:
        errors.append("Missing YAML key: last_validated (date when fixture was last verified)")
    elif not isinstance(data["last_validated"], str):
        errors.append("last_validated must be a date string (YYYY-MM-DD)")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--command", required=True, help="Command name, for example: card-full")
    parser.add_argument("path", type=Path, help="Path to a markdown output file")
    args = parser.parse_args()

    contracts = load_contracts().get("commands", {})
    if args.command not in contracts:
        available = ", ".join(sorted(contracts))
        raise SystemExit(f"Unknown command '{args.command}'. Available: {available}")

    contract = contracts[args.command]
    content = args.path.read_text(encoding="utf-8")
    errors = validate_sections(content, contract["heading_prefix"], contract["sections"])
    errors.extend(validate_no_visible_yaml(content))
    errors.extend(validate_no_visible_links(content))
    errors.extend(validate_no_why_it_matters(content))

    try:
        yaml_block = extract_yaml_block(content)
        data = yaml.safe_load(yaml_block) or {}
    except Exception as exc:  # pragma: no cover
        errors.append(str(exc))
        data = {}

    if isinstance(data, dict):
        errors.extend(validate_yaml_data(data, contract))
        errors.extend(validate_last_validated(data))
    else:
        errors.append("YAML block must parse to an object.")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {args.command} -> {args.path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
