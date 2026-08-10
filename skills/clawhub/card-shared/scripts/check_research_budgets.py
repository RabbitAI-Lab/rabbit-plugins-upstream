#!/usr/bin/env python3
"""Guard against research-budget regressions in the card skill suite."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required to run this validator.") from exc


ROOT = Path(__file__).resolve().parent.parent
POLICY_PATH = ROOT / "source-policy.yaml"

EXPECTED_BUDGETS = {
    "card-full": {
        "max_secondary": 1,
        "max_search_calls": 1,
        "max_page_fetches": 2,
        "multi_card_max_page_fetches": 4,
    },
    "card-compare": {"max_secondary": 1, "max_search_calls": 1, "max_page_fetches": 3},
    "card-value": {"max_secondary": 1, "max_search_calls": 1, "max_page_fetches": 2},
    "card-profile-recommend": {"max_secondary": 3, "max_search_calls": 2, "max_page_fetches": 6},
}


def main() -> int:
    data = yaml.safe_load(POLICY_PATH.read_text(encoding="utf-8"))
    search_policy = data.get("fast_search_policy", {})
    context_budget = search_policy.get("context_budget", {})
    ceilings = search_policy.get("command_source_ceilings", {})
    errors: list[str] = []

    if context_budget.get("response_length") != "short":
        errors.append("context_budget.response_length must be 'short'.")

    for command, expected in EXPECTED_BUDGETS.items():
        actual = ceilings.get(command, {})
        for key, maximum in expected.items():
            if actual.get(key) != maximum:
                errors.append(
                    f"{command}.{key} must be {maximum}; found {actual.get(key)!r}."
                )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("OK: research budgets are bounded for high-volume card commands")
    return 0


if __name__ == "__main__":
    sys.exit(main())
