#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import subprocess
import sys

from team_memory_paths import TeamMemoryPathError, TeamMemoryWriteLock, resolve_paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a Team Memory writer under the shared local lock.")
    parser.add_argument("--skill-dir", default=None)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not args.command:
        parser.error("missing command after --")
    command = args.command[1:] if args.command[0] == "--" else args.command
    try:
        paths = resolve_paths(args.skill_dir, require_lock=True)
        with TeamMemoryWriteLock(paths.data_dir):
            env = dict(os.environ)
            env["TEAM_MEMORY_WRITE_LOCK_HELD"] = "1"
            return subprocess.run(command, check=False, env=env).returncode
    except TeamMemoryPathError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
