#!/usr/bin/env python3
"""Validate a handoff request, specialist return, or parent closure."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REQUEST_HEADINGS = (
    "Goal",
    "Artifact",
    "Parent success",
    "Current state",
    "Already verified",
    "Remaining uncertainty",
    "Constraints",
    "Must preserve",
    "May change",
    "Specialist task",
    "Acceptance checks",
    "Predicted contribution",
)
RETURN_HEADINGS = (
    "Return status",
    "Findings",
    "Changes",
    "Evidence",
    "Actual observation",
    "Evidence state",
    "Unresolved after review",
    "Recommended next step",
)
VALID_STATES = {"PASS", "REWORK_REQUIRED", "BLOCKED", "NEEDS_HUMAN_JUDGMENT"}
VALID_EVIDENCE_STATES = {
    "NO RELIABLE EVIDENCE",
    "ARTIFACT VERIFIED",
    "OUTCOME VALIDATED",
    "DECISION READY",
}


VALID_DISPOSITIONS = {"ACCEPTED", "REWORK", "ESCALATED"}


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^### {re.escape(heading)}\s*$\n(.*?)(?=^## |^### |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        return ""
    return re.sub(r"<!--.*?-->", "", match.group(1), flags=re.DOTALL).strip()


def require_sections(text: str, headings: tuple[str, ...], problems: list[str]) -> None:
    for heading in headings:
        if not section(text, heading):
            problems.append(f"empty or missing required section: {heading}")


def lifecycle_status(text: str) -> str:
    match = re.search(r"^- \*\*status:\*\* (\S+)\s*$", text, re.MULTILINE)
    return match.group(1) if match else ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff", type=Path)
    parser.add_argument(
        "--stage",
        choices=("request", "return", "closed"),
        default="return",
        help="Lifecycle stage to validate; defaults to return",
    )
    args = parser.parse_args()

    try:
        text = args.handoff.read_text(encoding="utf-8")
    except OSError as exc:
        parser.error(str(exc))

    problems: list[str] = []
    require_sections(text, REQUEST_HEADINGS, problems)
    status = lifecycle_status(text)
    allowed_statuses = {
        "request": {"REQUESTED", "RETURNED", "CLOSED"},
        "return": {"RETURNED", "CLOSED"},
        "closed": {"CLOSED"},
    }[args.stage]
    if status not in allowed_statuses:
        problems.append(
            f"lifecycle status {status or '(missing)'} is invalid for {args.stage} validation"
        )

    if args.stage in {"return", "closed"}:
        require_sections(text, RETURN_HEADINGS, problems)
        state_text = section(text, "Return status")
        found_states = {state for state in VALID_STATES if state_text == state}
        if len(found_states) != 1:
            problems.append("Return status must contain exactly one completed valid status")

        evidence_text = section(text, "Evidence state")
        if evidence_text not in VALID_EVIDENCE_STATES:
            problems.append("Evidence state must contain exactly one completed valid state")

    if args.stage == "closed":
        require_sections(text, ("Parent disposition", "Integration evidence"), problems)
        disposition = section(text, "Parent disposition")
        if disposition not in VALID_DISPOSITIONS:
            problems.append("Parent disposition must be ACCEPTED, REWORK, or ESCALATED")

    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1

    print(f"Valid handoff: {args.handoff}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
