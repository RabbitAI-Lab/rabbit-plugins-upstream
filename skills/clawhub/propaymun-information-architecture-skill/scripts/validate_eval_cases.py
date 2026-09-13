#!/usr/bin/env python3
"""Validate the behavioral evaluation catalog and multi-turn journeys."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_ROUTES = {"agent-skill", "workspace-kit"}
ALLOWED_PRIORITIES = {"critical", "high", "medium", "low"}


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def nonempty_string_list(value: Any) -> bool:
    return isinstance(value, list) and bool(value) and all(nonempty_string(item) for item in value)


def validate_data(data: Any) -> dict[str, Any]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return {
            "valid": False,
            "atomic_case_count": 0,
            "journey_count": 0,
            "multi_turn_journey_count": 0,
            "errors": ["root must be a mapping"],
        }

    if data.get("version") != 5:
        errors.append("version must be 5")
    if not nonempty_string(data.get("skill")):
        errors.append("skill must be a non-empty string")

    contract = data.get("evaluation_contract")
    if not isinstance(contract, dict):
        errors.append("evaluation_contract must be a mapping")
    else:
        for field in ("execution", "result_record_required", "pass_rules"):
            if not nonempty_string_list(contract.get(field)):
                errors.append(f"evaluation_contract.{field} must be a non-empty string list")

    cases = data.get("cases")
    journeys = data.get("journeys")
    if not isinstance(cases, list) or not cases:
        errors.append("cases must be a non-empty list")
        cases = []
    if not isinstance(journeys, list) or not journeys:
        errors.append("journeys must be a non-empty list")
        journeys = []

    ids: list[str] = []
    for index, case in enumerate(cases):
        prefix = f"cases[{index}]"
        if not isinstance(case, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        for field in ("id", "behavior_expected", "prompt"):
            if not nonempty_string(case.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string")
        if nonempty_string(case.get("id")):
            ids.append(case["id"])
        if not nonempty_string_list(case.get("invariants")):
            errors.append(f"{prefix}.invariants must be a non-empty string list")
        if "follow_up" in case and not nonempty_string_list(case.get("follow_up_invariants")):
            errors.append(f"{prefix}.follow_up_invariants must accompany follow_up")

    multi_turn_count = 0
    for index, journey in enumerate(journeys):
        prefix = f"journeys[{index}]"
        if not isinstance(journey, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        for field in ("id", "purpose", "priority"):
            if not nonempty_string(journey.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string")
        if nonempty_string(journey.get("id")):
            ids.append(journey["id"])
        if journey.get("priority") not in ALLOWED_PRIORITIES:
            errors.append(f"{prefix}.priority must be one of {sorted(ALLOWED_PRIORITIES)}")
        routes = journey.get("package_routes")
        if not nonempty_string_list(routes) or not set(routes).issubset(ALLOWED_ROUTES):
            errors.append(f"{prefix}.package_routes must use only {sorted(ALLOWED_ROUTES)}")
        if not isinstance(journey.get("environment"), dict) and not isinstance(journey.get("variants"), list):
            errors.append(f"{prefix} must define environment or variants")

        turns = journey.get("turns")
        if not isinstance(turns, list) or not turns:
            errors.append(f"{prefix}.turns must be a non-empty list")
            turns = []
        if len(turns) > 1:
            multi_turn_count += 1
        for turn_index, turn in enumerate(turns):
            turn_prefix = f"{prefix}.turns[{turn_index}]"
            if not isinstance(turn, dict) or not nonempty_string(turn.get("user")):
                errors.append(f"{turn_prefix}.user must be a non-empty string")
                continue
            observe = turn.get("observe")
            if not isinstance(observe, dict):
                errors.append(f"{turn_prefix}.observe must be a mapping")
                continue
            for field in ("must", "must_not"):
                if not nonempty_string_list(observe.get(field)):
                    errors.append(f"{turn_prefix}.observe.{field} must be a non-empty string list")

        for field in ("rubric_dimensions", "critical_failures", "unmeasured_layers"):
            if not nonempty_string_list(journey.get(field)):
                errors.append(f"{prefix}.{field} must be a non-empty string list")

        variants = journey.get("variants", [])
        if variants:
            if not isinstance(variants, list):
                errors.append(f"{prefix}.variants must be a list")
            else:
                variant_ids: list[str] = []
                for variant_index, variant in enumerate(variants):
                    variant_prefix = f"{prefix}.variants[{variant_index}]"
                    if not isinstance(variant, dict):
                        errors.append(f"{variant_prefix} must be a mapping")
                        continue
                    if not nonempty_string(variant.get("id")):
                        errors.append(f"{variant_prefix}.id must be a non-empty string")
                    else:
                        variant_ids.append(variant["id"])
                    if not isinstance(variant.get("environment"), dict):
                        errors.append(f"{variant_prefix}.environment must be a mapping")
                    if not nonempty_string(variant.get("expected_outcome")):
                        errors.append(f"{variant_prefix}.expected_outcome must be a non-empty string")
                if len(variant_ids) != len(set(variant_ids)):
                    errors.append(f"{prefix}.variants contains duplicate ids")

    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    if duplicates:
        errors.append(f"duplicate case or journey ids: {duplicates}")
    if multi_turn_count < 3:
        errors.append("at least three journeys must contain multiple user turns")

    return {
        "valid": not errors,
        "atomic_case_count": len(cases),
        "journey_count": len(journeys),
        "multi_turn_journey_count": multi_turn_count,
        "errors": errors,
    }


def validate(path: Path) -> dict[str, Any]:
    try:
        import yaml
    except ImportError as exc:  # pragma: no cover - environment-specific guidance
        raise SystemExit(
            "PyYAML is required for evaluation validation. "
            "Install evals/requirements.txt in a temporary QA environment."
        ) from exc
    return validate_data(yaml.safe_load(path.read_text(encoding="utf-8")))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("evals/cases.yaml"))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = validate(args.path)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(
            f"atomic={result['atomic_case_count']} journeys={result['journey_count']} "
            f"multi_turn={result['multi_turn_journey_count']}"
        )
        for error in result["errors"]:
            print(f"ERROR: {error}", file=sys.stderr)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
