#!/usr/bin/env python3
"""Check that planned sub-agent tasks are truly independent (no shared files).

Supports the "Tasks are truly independent" checklist item. Reads a task list
(JSON) where each task declares the file paths it will touch, then flags any
overlap between tasks that would cause conflicting edits / merge pain.

Task list format:
[
  {"id": "auth",   "files": ["src/auth.py", "tests/test_auth.py"]},
  {"id": "billing","files": ["src/billing.py"]}
]
"""
import argparse
import json
import sys


def main():
    p = argparse.ArgumentParser(description="Detect file-path overlaps between sub-agent tasks.")
    p.add_argument("tasks", help="Path to a JSON task list (see module docstring for format)")
    args = p.parse_args()

    try:
        with open(args.tasks) as fh:
            tasks = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"Could not read task list: {e}")

    file_owner = {}
    conflicts = []
    for task in tasks:
        tid = task.get("id", "?")
        for f in task.get("files", []):
            if f in file_owner:
                conflicts.append((f, file_owner[f], tid))
            else:
                file_owner[f] = tid

    if not conflicts:
        print("OK: no shared files across tasks. Safe to parallelize.")
        return 0

    print("CONFLICT: the following files are claimed by more than one task:")
    for f, a, b in conflicts:
        print(f"  {f}  ->  tasks '{a}' and '{b}'")
    print("Partition ownership or serialize these tasks before spawning sub-agents.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
