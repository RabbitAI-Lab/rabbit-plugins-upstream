#!/usr/bin/env python3
"""Warn when a generated agent prompt lacks a portable loop contract."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

CHECKS = {
    "outcome contract": (r"\b(outcome contract|baseline.{0,80}target|target state)\b",),
    "measure and threshold": (r"\b(measure|metric)\b.{0,80}\b(threshold|target)\b",),
    "guardrails": (r"\bguardrail",),
    "required evidence state": (r"\b(ARTIFACT VERIFIED|OUTCOME VALIDATED|DECISION READY)\b",),
    "context inspection": (r"\b(inspect|read|examine|review)\b.{0,80}\b(repository|context|environment|existing)\b",),
    "verification and validation": (r"(?=.*\bverif)(?=.*\bvalidat)",),
    "cycle prediction and delta": (r"\b(hypothesis|predicted observation)\b.{0,200}\b(delta|actual observation|measure)\b",),
    "adaptation": (r"\b(diagnose|change approach|revise|adapt|contradicts)\b",),
    "success-contract integrity": (
        r"\b(not|never|without)\b.{0,120}\b(weaken|redefine|rewrite|change)\b.{0,120}\b(target|success|verifier|evidence|guardrail|authority)",
    ),
    "human boundary": (r"\b(human judgment|approval|irreversible|consequential)\b",),
    "terminal COMPLETE": (r"\bCOMPLETE\b",),
    "terminal BLOCKED": (r"\bBLOCKED\b",),
    "terminal NOT FEASIBLE": (r"\bNOT[_ ]FEASIBLE\b",),
    "terminal STAGNATED": (r"\bSTAGNATED\b",),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt", type=Path)
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    try:
        text = args.prompt.read_text(encoding="utf-8")
    except OSError as exc:
        parser.error(str(exc))

    missing = []
    for label, patterns in CHECKS.items():
        if not any(re.search(pattern, text, re.IGNORECASE | re.DOTALL) for pattern in patterns):
            missing.append(label)

    if re.search(r"\b(use loop engineering|iterate until good|keep improving)\b", text, re.IGNORECASE) and len(missing) >= 3:
        print("WARNING: prompt names iteration but does not teach a sufficient loop contract")

    if not missing:
        print("Portable loop contract signals found. Domain-specific simulation is still required.")
        return 0

    for item in missing:
        print(f"MISSING: {item}")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
