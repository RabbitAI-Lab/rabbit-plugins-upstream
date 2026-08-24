#!/usr/bin/env python3
"""Run deterministic smoke checks for the documented JYS next-skill policy."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


HOOK_TERMS = ("开头", "开场", "第一句", "第一幕", "前几秒", "钩子")


def explicit_skill(text: str) -> str | None:
    match = re.search(r"\$(jys-s[1-5])\b", text, re.IGNORECASE)
    return match.group(1).lower() if match else None


def route(state: dict[str, Any], user_input: str) -> str:
    explicit = explicit_skill(user_input)
    if explicit:
        return explicit
    stage = str(state.get("current_stage", "")).upper()
    if any(term in user_input for term in HOOK_TERMS):
        if stage == "S2":
            return "jys-s2"
        if stage == "S4":
            return "jys-s4"
    if stage == "S3" and ("没有" in user_input or "新产品" in user_input):
        return "jys-s1"
    return str(state.get("next_skill") or state.get("current_skill") or "jys")


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate deterministic JYS next-skill state cases.")
    parser.add_argument("--cases", type=Path, default=Path(__file__).resolve().parents[1] / "evals" / "state_transition_cases.json")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.cases.read_text(encoding="utf-8"))
    results = []
    for case in payload.get("cases", []):
        actual = route(case.get("state", {}), str(case.get("user_input", "")))
        expected = case.get("expected_skill")
        results.append({"name": case.get("name"), "expected": expected, "actual": actual, "passed": actual == expected})
    result = {
        "ok": all(row["passed"] for row in results) and bool(results),
        "summary": {"total": len(results), "passed": sum(1 for row in results if row["passed"])},
        "results": results,
        "evidence_type": "deterministic_policy_smoke",
        "provider_backed_routing_eval": "missing evidence",
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    if not result["ok"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
