#!/usr/bin/env python3
"""Print a parallel dispatch plan: agents x independent tasks.

Reads a simple task list (JSON) and prints how many sub-agent sessions to spawn,
what each should own, and a suggested brief file name. Supports the "Write
per-task briefs" / "Spawn" steps.

Task list format:
[
  {"id": "config-audit-1", "objective": "Audit secrets in a.conf",
   "files": ["a.conf"], "acceptance": "No secrets reported"},
  {"id": "config-audit-2", "objective": "Audit secrets in b.conf",
   "files": ["b.conf"], "acceptance": "No secrets reported"}
]
"""
import argparse
import json
import sys


def main():
    p = argparse.ArgumentParser(description="Print a parallel dispatch plan from a task list.")
    p.add_argument("tasks", help="Path to a JSON task list (see module docstring)")
    args = p.parse_args()

    try:
        with open(args.tasks) as fh:
            tasks = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Could not read task list: {e}")

    print(f"Dispatch plan: spawn {len(tasks)} parallel sub-agent session(s) (depth 1)\n")
    for i, t in enumerate(tasks, 1):
        tid = t.get("id", f"task-{i}")
        obj = t.get("objective", "(no objective)")
        files = ", ".join(t.get("files", [])) or "(unspecified)"
        acc = t.get("acceptance", "(none stated)")
        brief = f"briefs/{tid}.md"
        print(f"Agent {i}: {tid}")
        print(f"  objective : {obj}")
        print(f"  owns files: {files}")
        print(f"  acceptance: {acc}")
        print(f"  brief file: {brief}")
        print()

    print("Then call sessions_yield to await completions (do NOT busy-poll).")
    print("Verify each returned result independently before trusting it.")


if __name__ == "__main__":
    main()
