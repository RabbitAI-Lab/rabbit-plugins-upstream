#!/usr/bin/env python3
"""Run a bounded WorkBuddy/CodeBuddy handshake without turning blank output into PASS."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path


PROMPT = (
    "Handshake only. Do not call members. List the data-quality gates "
    "before diagnosis and explain what BLOCKED may output."
)


def resolve_command() -> list[str] | None:
    command = shutil.which("codebuddy.cmd") or shutil.which("codebuddy")
    if not command:
        return None
    command_path = Path(command)
    if command_path.suffix.casefold() == ".cmd":
        base = command_path.parent
        node = base / "node.exe"
        cli = base / "node_modules" / "@tencent-ai" / "codebuddy-code" / "bin" / "codebuddy"
        if not node.is_file():
            node_value = shutil.which("node")
            node = Path(node_value) if node_value else node
        if node.is_file() and cli.is_file():
            return [str(node), str(cli)]
    return [str(command_path)]


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify a real omni-ecom WorkBuddy load")
    parser.add_argument("--plugin-dir", required=True)
    parser.add_argument("--timeout", type=int, default=90)
    parser.add_argument("--output")
    args = parser.parse_args()
    command = resolve_command()
    if not command:
        result = {
            "status": "INCONCLUSIVE",
            "reason": "codebuddy_not_found",
            "message": "codebuddy executable was not found on PATH.",
        }
    else:
        invocation = [*command, "-p", "--plugin-dir", args.plugin_dir, "--agent", "omni-ecom-team-lead", PROMPT]
        try:
            completed = subprocess.run(
                invocation,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=args.timeout,
                check=False,
            )
            stdout = (completed.stdout or "").strip()
            stderr = (completed.stderr or "").strip()
            if not stdout:
                result = {
                    "status": "INCONCLUSIVE",
                    "reason": "blank_stdout",
                    "exit_code": completed.returncode,
                    "stderr": stderr,
                    "message": "CLI exited without stdout; confirm the plugin in a new WorkBuddy session.",
                }
            else:
                folded = stdout.casefold()
                checks = [
                    any(token in folded for token in ("pass", "warn", "blocked")),
                    any(token in folded for token in ("data quality", "gate", "数据质量", "闸门")),
                    "blocked" in folded,
                ]
                result = {
                    "status": "PASS" if all(checks) and completed.returncode == 0 else "FAIL",
                    "exit_code": completed.returncode,
                    "checks": checks,
                    "stdout": stdout,
                    "stderr": stderr,
                }
        except subprocess.TimeoutExpired:
            result = {
                "status": "INCONCLUSIVE",
                "reason": "timeout",
                "message": "CLI timeout; timeout is not treated as a successful plugin load.",
            }
        except OSError as exc:
            result = {"status": "INCONCLUSIVE", "reason": "launch_error", "message": str(exc)}

    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        output = Path(args.output).resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(payload, end="")
    return 0 if result["status"] == "PASS" else 2 if result["status"] == "INCONCLUSIVE" else 1


if __name__ == "__main__":
    raise SystemExit(main())
