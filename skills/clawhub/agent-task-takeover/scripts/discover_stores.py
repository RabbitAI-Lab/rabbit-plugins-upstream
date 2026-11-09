#!/usr/bin/env python3
"""Discover which AI coding agents have session stores on this machine.

Scans the known roots from references/agent-stores.md (CLI and Electron
agents alike) and prints what exists, the newest file inside, and when it
was last touched. Everything is read-only; nothing outside the listed
candidate roots is opened.

Usage:
  python discover_stores.py            # human-readable table
  python discover_stores.py --json     # machine-readable
  python discover_stores.py --days 14  # only stores touched in the last N days
"""
import argparse
import glob
import json
import os
import sys
import time
from pathlib import Path

from session_utils import ensure_utf8_stdout

HOME = Path.home()


def _app_support(app):
    """Per-platform config root for Electron (VS Code-family) apps."""
    if sys.platform == "darwin":
        return HOME / "Library" / "Application Support" / app / "User"
    if sys.platform == "win32":
        return Path(os.environ.get("APPDATA", HOME / "AppData/Roaming")) / app / "User"
    return HOME / ".config" / app / "User"


def _claude_root():
    # Claude Code honours CLAUDE_CONFIG_DIR; default ~/.claude.
    return Path(os.environ.get("CLAUDE_CONFIG_DIR", HOME / ".claude"))


# (agent, kind, human note, candidate glob patterns)
def candidates():
    vscode_family = ["Cursor", "Trae", "Code", "Kiro", "Windsurf", "Antigravity"]
    out = [
        ("opencode", "cli", "SQLite DB",
         [str(HOME / ".local/share/opencode/opencode.db"),
          str(HOME / ".local/share/opencode/project/*/storage/*.db")]),
        ("zcode", "cli", "rollout JSONL",
         [str(HOME / ".zcode/cli/rollout/*.jsonl")]),
        ("codex", "cli", "rollout JSONL",
         [str(HOME / ".codex/sessions/**/*.jsonl"),
          str(HOME / ".codex/sessions/*.jsonl")]),
        ("claude-code", "cli", "projects JSONL",
         [str(_claude_root() / "projects/*/*.jsonl")]),
        ("gemini-cli", "cli", "chats JSON",
         [str(HOME / ".gemini/tmp/*/chats/session-*.json")]),
        ("aider", "cli", "chat history md",
         [str(HOME / ".aider.chat.history.md")]),
        ("workbuddy", "electron", "app dir (store unconfirmed)",
         [str(HOME / ".workbuddy/workbuddy.db"),
          str(HOME / ".workbuddy/sessions")]),
    ]
    for app in vscode_family:
        user = _app_support(app)
        out.append((
            app.lower(), "electron", "state.vscdb / chatSessions",
            [str(user / "workspaceStorage/*/state.vscdb"),
             str(user / "workspaceStorage/*/chatSessions/*.json"),
             str(user / "globalStorage/state.vscdb")],
        ))
    return out


def scan(days):
    now = time.time()
    found = []
    for agent, kind, note, patterns in candidates():
        files = []
        for pattern in patterns:
            files.extend(p for p in glob.glob(pattern, recursive=True) if os.path.isfile(p))
        dirs = [p for pattern in patterns for p in glob.glob(pattern) if os.path.isdir(p)]
        if not files and not dirs:
            continue
        newest = None
        for path in files:
            try:
                mtime = os.path.getmtime(path)
            except OSError:
                continue
            if newest is None or mtime > newest[1]:
                newest = (path, mtime)
        for path in dirs:
            try:
                mtime = os.path.getmtime(path)
            except OSError:
                continue
            if newest is None or mtime > newest[1]:
                newest = (path + os.sep, mtime)
        if days and newest and (now - newest[1]) > days * 86400:
            continue
        found.append({
            "agent": agent,
            "kind": kind,
            "note": note,
            "files": len(files),
            "newest": newest[0] if newest else None,
            "mtime": newest[1] if newest else None,
        })
    found.sort(key=lambda item: item["mtime"] or 0, reverse=True)
    return found


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--days", type=int, default=0,
                        help="only stores touched within the last N days")
    args = parser.parse_args()
    ensure_utf8_stdout()

    found = scan(args.days)
    if args.json:
        print(json.dumps(found, ensure_ascii=False, indent=2))
        return
    if not found:
        print("no known agent stores found on this machine")
        return
    for item in found:
        when = time.strftime("%Y-%m-%d %H:%M", time.localtime(item["mtime"])) if item["mtime"] else "?"
        print(f"{item['agent']:<14} [{item['kind']:>8}]  {item['files']:>4} file(s)  "
              f"last touched {when}")
        print(f"{'':<14}  {item['note']}")
        if item["newest"]:
            print(f"{'':<14}  newest: {item['newest']}")


if __name__ == "__main__":
    main()
