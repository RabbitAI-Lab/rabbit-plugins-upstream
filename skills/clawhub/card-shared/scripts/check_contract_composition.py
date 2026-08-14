#!/usr/bin/env python3
"""Validate that card-full reuses the focused command contracts defined in command-contracts.yaml.

Also documents that card-news is intentionally independent — it is not composed
into card-full because news is time-windowed and conceptually separate from the
static card framework.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required to run this validator.") from exc


ROOT = Path(__file__).resolve().parent.parent
CONTRACTS_PATH = ROOT / "command-contracts.yaml"

# card-news is intentionally not composed into card-full.
# News is time-windowed (3-month lookback) and conceptually independent
# from the static card framework that card-full assembles.
EXPECTED_UNCOMPOSED = {"card-news"}


def main() -> int:
    data = yaml.safe_load(CONTRACTS_PATH.read_text(encoding="utf-8"))
    commands = data.get("commands", {})
    full_contract = commands.get("card-full", {})
    rules = full_contract.get("composition_rules", [])
    errors: list[str] = []

    if not rules:
        errors.append("card-full is missing composition_rules.")

    full_keys = set(full_contract.get("required_top_level_keys", []))
    composed_sources = set()

    for rule in rules:
        full_key = rule["full_key"]
        source_command = rule["source_command"]
        source_key = rule["source_key"]
        source_contract = commands.get(source_command)
        composed_sources.add(source_command)

        if full_key not in full_keys:
            errors.append(f"card-full missing required key referenced by composition rule: {full_key}")

        if source_contract is None:
            errors.append(f"Missing source command for composition rule: {source_command}")
            continue

        source_keys = set(source_contract.get("required_top_level_keys", []))
        if source_key not in source_keys:
            errors.append(
                f"{source_command} missing required key referenced by composition rule: {source_key}"
            )

    # Verify that uncomposed commands are expected
    focused_commands = {
        name
        for name in commands
        if name
        not in {
            "card-full",
            "card-compare",
            "card-value",
            "card-wallet",
            "card-profile-recommend",
        }
    }
    uncomposed = focused_commands - composed_sources
    unexpected = uncomposed - EXPECTED_UNCOMPOSED
    if unexpected:
        errors.append(
            f"Focused command(s) not composed into card-full and not in EXPECTED_UNCOMPOSED: "
            f"{', '.join(sorted(unexpected))}"
        )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: card-full composition rules match focused command contracts")
    if EXPECTED_UNCOMPOSED & focused_commands:
        for cmd in sorted(EXPECTED_UNCOMPOSED & focused_commands):
            print(f"  NOTE: {cmd} is intentionally not composed into card-full")
    return 0


if __name__ == "__main__":
    sys.exit(main())
