#!/usr/bin/env python3
"""Initialize private project-local state for an orchestrated loop task."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path


def find_project_root(start: Path) -> Path:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            check=True,
            capture_output=True,
            text=True,
        )
        return Path(result.stdout.strip()).resolve()
    except (FileNotFoundError, subprocess.CalledProcessError):
        return start.resolve()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug[:56].rstrip("-") or "task"


def append_exclusion(path: Path) -> None:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    if any(line.strip() == ".loop/" for line in existing.splitlines()):
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    separator = "" if not existing or existing.endswith("\n") else "\n"
    path.write_text(
        existing + separator + "# Local loop-engineering state\n.loop/\n",
        encoding="utf-8",
    )


def ensure_private_state(root: Path, edit_gitignore: bool) -> None:
    """Exclude .loop locally; edit the tracked ignore file only by explicit request."""
    try:
        ignored = subprocess.run(
            ["git", "check-ignore", "-q", ".loop/probe"],
            cwd=root,
            check=False,
        )
        if ignored.returncode == 0:
            return
        if edit_gitignore:
            append_exclusion(root / ".gitignore")
            return
        result = subprocess.run(
            ["git", "rev-parse", "--git-path", "info/exclude"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
        exclude = Path(result.stdout.strip())
        if not exclude.is_absolute():
            exclude = root / exclude
        append_exclusion(exclude.resolve())
    except (FileNotFoundError, subprocess.CalledProcessError):
        # A non-Git directory has nothing to exclude from version control.
        return


def create_task(root: Path, task: str, mode: str) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
    task_dir = root / ".loop" / f"{slugify(task)}-{timestamp}"
    (task_dir / "handoffs").mkdir(parents=True, exist_ok=False)

    state = f"""# Loop state

- **status:** ACTIVE
- **mode:** {mode}
- **task:** {task}
- **created_utc:** {timestamp}
- **assignment_status:** ACTIVE
- **evidence_state:** NO RELIABLE EVIDENCE

## Starting point

## Target

## Measure and threshold

## Proof required

Choose one and state the evidence needed: ARTIFACT VERIFIED | OUTCOME VALIDATED | DECISION READY

## Guardrails and exclusions

## Next use or decision

## Strongest feasible evidence now

## Current facts and assumptions

## Execution mode and check owners

Choose real specialist, cold same-session pass, or in-memory pass; list only material checks.

## Execution topology (Deep only)

Default to one parent loop. Use an explicit topology only for material independent branches, distinct authority or failure boundaries, verified fan-in, or durable cross-artifact or cross-session dependencies. Otherwise record: Single parent loop; no explicit topology required.

Topology declaration:

For each node record: stable identifier and check owner; dependencies; required input and durable artifact; output contract; status and budget; failure route; merge owner; approval gate.

## Artifacts and handoffs

## Cycle receipts

For each meaningful cycle record: hypothesis and mechanism; intervention or test; predicted observation; actual observation; delta from baseline or prior cycle; guardrail result; learning; next decision.

## Verification, validation, and limitations

## Rejected directions

## Risks and unresolved decisions

## Next action

## Stop condition
"""
    (task_dir / "state.md").write_text(state, encoding="utf-8")
    (task_dir / "metadata.json").write_text(
        json.dumps(
            {
                "task": task,
                "mode": mode,
                "status": "ACTIVE",
                "evidence_state": "NO RELIABLE EVIDENCE",
                "created_utc": timestamp,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    return task_dir


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task", required=True, help="Concise task description")
    parser.add_argument("--root", default=".", help="Project path; defaults to current directory")
    parser.add_argument(
        "--mode",
        choices=("light", "standard", "deep"),
        default="standard",
        help="Initial loop depth",
    )
    parser.add_argument(
        "--edit-gitignore",
        action="store_true",
        help="Add .loop/ to the project .gitignore instead of Git's local exclude file",
    )
    args = parser.parse_args()

    start = Path(args.root).expanduser()
    if not start.is_dir():
        parser.error(f"Project path is not a directory: {start}")

    root = find_project_root(start)
    ensure_private_state(root, args.edit_gitignore)
    task_dir = create_task(root, args.task.strip(), args.mode)
    print(task_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
