#!/usr/bin/env python3
"""Create a populated request/return handoff from loop state."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")[:48] or "loop"


def section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if not match:
        return ""
    value = match.group(1).strip()
    if value.startswith("Choose one:") or value.startswith("For each meaningful cycle"):
        return ""
    return value


def require_state(state: str, headings: tuple[str, ...]) -> dict[str, str]:
    values = {heading: section(state, heading) for heading in headings}
    missing = [heading for heading, value in values.items() if not value]
    if missing:
        raise ValueError(
            "complete these parent state sections before creating a handoff: "
            + ", ".join(missing)
        )
    return values


def state_mode(state: str) -> str:
    match = re.search(r"^- \*\*mode:\*\*\s*(\S+)\s*$", state, re.MULTILINE)
    return match.group(1).lower() if match else ""


def require_deep_topology(state: str) -> str:
    if state_mode(state) != "deep":
        return ""

    topology = section(state, "Execution topology (Deep only)")
    match = re.search(
        r"^Topology declaration:[ \t]*([^\r\n]+?)[ \t]*$",
        topology,
        re.MULTILINE,
    )
    declaration = match.group(1).strip() if match else ""
    if not declaration:
        raise ValueError(
            "complete the Topology declaration in parent state before creating "
            "a Deep-mode handoff; record either a single parent loop or an "
            "explicit topology"
        )
    return declaration


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from-loop", required=True)
    parser.add_argument("--to-loop", required=True)
    parser.add_argument("--objective", required=True)
    parser.add_argument("--artifact", required=True)
    parser.add_argument("--uncertainty", required=True)
    parser.add_argument("--acceptance", required=True)
    parser.add_argument("--verified", default="No additional specialist-specific facts recorded.")
    parser.add_argument("--must-preserve", default="Parent guardrails and constraints.")
    parser.add_argument("--may-change", default="Only changes needed for the specialist objective.")
    parser.add_argument("--state-dir", required=True, type=Path)
    args = parser.parse_args()

    state_dir = args.state_dir.expanduser().resolve()
    state_path = state_dir / "state.md"
    if not state_path.is_file():
        parser.error(f"state.md not found in state directory: {state_dir}")

    state = state_path.read_text(encoding="utf-8")
    try:
        inherited = require_state(
            state,
            (
                "Starting point",
                "Target",
                "Measure and threshold",
                "Proof required",
                "Guardrails and exclusions",
                "Next use or decision",
            ),
        )
        topology_declaration = require_deep_topology(state)
    except ValueError as exc:
        parser.error(str(exc))

    parent_success = (
        f"Target: {inherited['Target']}\n\n"
        f"Measure: {inherited['Measure and threshold']}\n\n"
        f"Proof required: {inherited['Proof required']}\n\n"
        f"Next use: {inherited['Next use or decision']}"
    )
    current_state = f"Starting point: {inherited['Starting point']}"
    if topology_declaration:
        current_state += f"\n\nTopology declaration: {topology_declaration}"
    constraints = f"Guardrails and exclusions: {inherited['Guardrails and exclusions']}"

    handoffs = state_dir / "handoffs"
    handoffs.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    path = handoffs / f"{timestamp}-{slug(args.from_loop)}-to-{slug(args.to_loop)}.md"
    path.write_text(
        f"""# Specialist handoff

- **from:** {args.from_loop}
- **to:** {args.to_loop}
- **created_utc:** {timestamp}
- **status:** REQUESTED

## Handoff request

### Goal

{args.objective}

### Artifact

{args.artifact}

### Parent success

{parent_success}

### Current state

{current_state}

### Already verified

{args.verified}

### Remaining uncertainty

{args.uncertainty}

### Constraints

{constraints}

### Must preserve

{args.must_preserve}

### May change

{args.may_change}

### Specialist task

{args.objective}

### Acceptance checks

{args.acceptance}

### Predicted contribution

If the specialist resolves the stated uncertainty, the parent can remeasure the target using the acceptance checks above.

## Specialist return

### Return status

<!-- Choose exactly one: PASS | REWORK_REQUIRED | BLOCKED | NEEDS_HUMAN_JUDGMENT -->

### Findings

<!-- Specialist completes. -->

### Changes

<!-- Specialist completes; use "None" for a review-only handoff. -->

### Evidence

<!-- Specialist completes with commands, observations, sources, or artifacts. -->

### Actual observation

<!-- Specialist completes with the measured result or decision-relevant learning. -->

### Evidence state

<!-- Choose exactly one: NO RELIABLE EVIDENCE | ARTIFACT VERIFIED | OUTCOME VALIDATED | DECISION READY -->

### Unresolved after review

<!-- Specialist completes; use "None identified" only when supported. -->

### Recommended next step

<!-- Specialist completes. -->

## Parent closure

### Parent disposition

<!-- Parent completes after integration: ACCEPTED | REWORK | ESCALATED -->

### Integration evidence

<!-- Parent completes after rechecking the integrated result. -->
""",
        encoding="utf-8",
    )
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
