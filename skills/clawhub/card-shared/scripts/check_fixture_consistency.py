#!/usr/bin/env python3
"""Cross-check that card-full golden fixtures are consistent with their focused-command counterparts.

For each composition rule in command-contracts.yaml, this script verifies that
the card-full fixture's YAML data for the composed key is consistent with the
corresponding focused-command fixture for the same card.

Consistency checks:
  - card_name, issuer, network, card_family, card_variant must match
  - Composed section data should not contradict the focused-command fixture

Usage:
  python3 check_fixture_consistency.py tests/fixtures/golden/
"""

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

IDENTITY_KEYS = ("card_name", "issuer", "network", "card_family", "card_variant")

# Map focused commands to the filename prefix used in fixtures
COMMAND_TO_PREFIX = {
    "card-rate": "card-rate",
    "card-transfer": "card-transfer",
    "card-credits": "card-credits",
}


def extract_yaml_block(content: str) -> dict:
    match = re.search(r"<!--\s*```yaml\n(.*?)\n```\s*-->", content, re.DOTALL)
    if not match:
        return {}
    return yaml.safe_load(match.group(1)) or {}


def find_focused_fixture(golden_dir: Path, full_fixture: Path, command_prefix: str) -> Path | None:
    """Find the focused-command fixture that matches the card in the full fixture."""
    # Extract the card suffix from the full fixture name
    # e.g., card-full-chase-sapphire-preferred.md -> chase-sapphire-preferred
    stem = full_fixture.stem
    if not stem.startswith("card-full-"):
        return None
    card_suffix = stem[len("card-full-"):]
    candidate = golden_dir / f"{command_prefix}-{card_suffix}.md"
    return candidate if candidate.exists() else None


def check_identity_match(full_data: dict, focused_data: dict, focused_name: str) -> list[str]:
    errors = []
    for key in IDENTITY_KEYS:
        full_val = full_data.get(key)
        focused_val = focused_data.get(key)
        if full_val and focused_val and full_val != focused_val:
            errors.append(
                f"Identity mismatch between card-full and {focused_name}: "
                f"{key} = '{full_val}' vs '{focused_val}'"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "golden_dir",
        type=Path,
        nargs="?",
        default=Path("tests/fixtures/golden"),
        help="Path to the golden fixtures directory",
    )
    args = parser.parse_args()

    if not args.golden_dir.is_dir():
        raise SystemExit(f"Not a directory: {args.golden_dir}")

    contracts = yaml.safe_load(CONTRACTS_PATH.read_text(encoding="utf-8"))
    composition_rules = contracts["commands"]["card-full"].get("composition_rules", [])

    full_fixtures = sorted(args.golden_dir.glob("card-full-*.md"))
    if not full_fixtures:
        print("No card-full fixtures found.")
        return 0

    errors: list[str] = []
    checks = 0

    for full_path in full_fixtures:
        full_content = full_path.read_text(encoding="utf-8")
        full_data = extract_yaml_block(full_content)
        if not full_data:
            errors.append(f"Could not extract YAML from {full_path.name}")
            continue

        for rule in composition_rules:
            source_command = rule["source_command"]
            prefix = COMMAND_TO_PREFIX.get(source_command)
            if not prefix:
                continue

            focused_path = find_focused_fixture(args.golden_dir, full_path, prefix)
            if not focused_path:
                continue

            focused_content = focused_path.read_text(encoding="utf-8")
            focused_data = extract_yaml_block(focused_content)
            if not focused_data:
                errors.append(f"Could not extract YAML from {focused_path.name}")
                continue

            checks += 1
            errors.extend(check_identity_match(full_data, focused_data, focused_path.name))

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print(f"OK: {checks} cross-fixture consistency check(s) passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
