#!/usr/bin/env python3
"""Record a specialist return or close an integrated handoff."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

RETURN_STATES = ("PASS", "REWORK_REQUIRED", "BLOCKED", "NEEDS_HUMAN_JUDGMENT")
EVIDENCE_STATES = (
    "NO RELIABLE EVIDENCE",
    "ARTIFACT VERIFIED",
    "OUTCOME VALIDATED",
    "DECISION READY",
)
DISPOSITIONS = ("ACCEPTED", "REWORK", "ESCALATED")


def lifecycle_status(text: str) -> str:
    match = re.search(r"^- \*\*status:\*\* (\S+)\s*$", text, re.MULTILINE)
    return match.group(1) if match else ""


def set_lifecycle_status(text: str, value: str) -> str:
    updated, count = re.subn(
        r"^- \*\*status:\*\* \S+\s*$",
        f"- **status:** {value}",
        text,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise ValueError("handoff metadata status is missing or ambiguous")
    return updated


def replace_section(text: str, heading: str, value: str) -> str:
    pattern = rf"(^### {re.escape(heading)}\s*$\n)(.*?)(?=^## |^### |\Z)"
    updated, count = re.subn(
        pattern,
        lambda match: f"{match.group(1)}\n{value.strip()}\n\n",
        text,
        count=1,
        flags=re.MULTILINE | re.DOTALL,
    )
    if count != 1:
        raise ValueError(f"handoff section is missing or ambiguous: {heading}")
    return updated


def record_return(args: argparse.Namespace, text: str) -> str:
    if lifecycle_status(text) != "REQUESTED":
        raise ValueError("a specialist return can only be recorded on a REQUESTED handoff")
    values = {
        "Return status": args.return_status,
        "Findings": args.findings,
        "Changes": args.changes,
        "Evidence": args.evidence,
        "Actual observation": args.observation,
        "Evidence state": args.evidence_state,
        "Unresolved after review": args.uncertainty,
        "Recommended next step": args.next_step,
    }
    for heading, value in values.items():
        text = replace_section(text, heading, value)
    return set_lifecycle_status(text, "RETURNED")


def close_handoff(args: argparse.Namespace, text: str) -> str:
    if lifecycle_status(text) != "RETURNED":
        raise ValueError("a handoff can only be closed after a RETURNED specialist result")
    text = replace_section(text, "Parent disposition", args.disposition)
    text = replace_section(text, "Integration evidence", args.integration_evidence)
    return set_lifecycle_status(text, "CLOSED")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    returned = subparsers.add_parser("return", help="Record the specialist result")
    returned.add_argument("handoff", type=Path)
    returned.add_argument("--return-status", choices=RETURN_STATES, required=True)
    returned.add_argument("--findings", required=True)
    returned.add_argument("--changes", required=True)
    returned.add_argument("--evidence", required=True)
    returned.add_argument("--observation", required=True)
    returned.add_argument("--evidence-state", choices=EVIDENCE_STATES, required=True)
    returned.add_argument("--uncertainty", required=True)
    returned.add_argument("--next-step", required=True)

    closed = subparsers.add_parser("close", help="Record parent integration and close")
    closed.add_argument("handoff", type=Path)
    closed.add_argument("--disposition", choices=DISPOSITIONS, required=True)
    closed.add_argument("--integration-evidence", required=True)

    args = parser.parse_args()
    path = args.handoff.expanduser().resolve()
    try:
        text = path.read_text(encoding="utf-8")
        updated = record_return(args, text) if args.command == "return" else close_handoff(args, text)
        path.write_text(updated, encoding="utf-8")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
