#!/usr/bin/env python3
"""Install Dongwo's local engine and print lifecycle-hook snippets."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Set up Dongwo in a project")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--apply", action="store_true", help="apply the previewed setup")
    parser.add_argument("--force", action="store_true", help="replace installed engine")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    source = Path(__file__).with_name("dongwo.py")
    target = root / ".dongwo" / "scripts" / "dongwo.py"
    memory = root / ".dongwo" / "memory"
    profile = root / "myprofile.md"

    print("Dongwo setup plan:")
    print(f"- project root: {root}")
    print(f"- install engine: {target}")
    print(f"- create local memory directory: {memory}")
    print("- preference-like prompts will be retained locally after hooks are enabled")
    print("- existing Codex/Claude configuration will not be modified")
    if not args.apply:
        print("\nPreview only. Re-run with --apply after the user confirms.")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    memory.mkdir(parents=True, exist_ok=True)
    if target.exists() and not args.force:
        print(f"[keep] engine already exists: {target}")
    else:
        shutil.copy2(source, target)
        target.chmod(0o755)
        print(f"[ok] installed engine: {target}")

    if profile.exists():
        print(f"[keep] confirmed profile already exists: {profile}")
    else:
        print(f"[note] optional confirmed profile not created: {profile}")

    command = 'python3 "$PROJECT_ROOT/.dongwo/scripts/dongwo.py" hook --agent AGENT'
    codex = {
        "hooks": {
            "SessionStart": [
                {
                    "matcher": "startup|resume|clear|compact",
                    "hooks": [
                        {
                            "type": "command",
                            "command": command.replace("$PROJECT_ROOT", "$(git rev-parse --show-toplevel)").replace("AGENT", "codex"),
                            "statusMessage": "Load Dongwo preferences",
                            "additionalContextLimit": 4000,
                        }
                    ],
                }
            ],
            "UserPromptSubmit": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": command.replace("$PROJECT_ROOT", "$(git rev-parse --show-toplevel)").replace("AGENT", "codex"),
                            "statusMessage": "Update Dongwo preferences",
                            "additionalContextLimit": 4000,
                        }
                    ]
                }
            ],
        }
    }
    claude = {
        "hooks": {
            "SessionStart": [
                {
                    "matcher": "startup|resume|clear|compact",
                    "hooks": [
                        {
                            "type": "command",
                            "command": "/usr/bin/python3",
                            "args": [
                                "${CLAUDE_PROJECT_DIR}/.dongwo/scripts/dongwo.py",
                                "hook",
                                "--agent",
                                "claude",
                            ],
                            "statusMessage": "Load Dongwo preferences",
                            "timeout": 15,
                        }
                    ],
                }
            ],
            "UserPromptSubmit": [
                {
                    "hooks": [
                        {
                            "type": "command",
                            "command": "/usr/bin/python3",
                            "args": [
                                "${CLAUDE_PROJECT_DIR}/.dongwo/scripts/dongwo.py",
                                "hook",
                                "--agent",
                                "claude",
                            ],
                            "statusMessage": "Update Dongwo preferences",
                            "timeout": 15,
                        }
                    ]
                }
            ],
        }
    }

    print("\nMerge into .codex/hooks.json:")
    print(json.dumps(codex, ensure_ascii=False, indent=2))
    print("\nMerge into .claude/settings.json:")
    print(json.dumps(claude, ensure_ascii=False, indent=2))
    print("\nThen run:")
    print(f'DONGWO_ROOT="{root}" python3 "{target}" doctor')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
