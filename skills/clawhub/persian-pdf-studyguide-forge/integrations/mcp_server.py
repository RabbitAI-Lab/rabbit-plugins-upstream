#!/usr/bin/env python3
"""mcp_server.py — expose the skill as an MCP server over stdio.

Zero dependencies: implements the Model Context Protocol JSON-RPC handshake
directly, so any MCP host (Claude Desktop, Claude Code, Cursor, Windsurf,
Zed, Continue, VS Code Copilot agents, LibreChat, custom hosts) can mount the
skill without installing an SDK.

Register it, e.g. in an MCP host config:

    {
      "mcpServers": {
        "persian-pdf-studyguide-forge": {
          "command": "python3",
          "args": ["/abs/path/to/skill/integrations/mcp_server.py"],
          "env": {"OPENAI_API_KEY": "..."}
        }
      }
    }

Every tool call shells out to the same `scripts/forge.py` contract the CLI and
every other runtime use, so results are identical no matter who calls.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = json.loads((ROOT / "integrations/tool-spec.json").read_text("utf-8"))
PROTOCOL_VERSION = "2024-11-05"


def _tools() -> list:
    return [{
        "name": SPEC["name"],
        "description": SPEC["description"],
        "inputSchema": SPEC["input_schema"],
    }]


def _call(args: dict) -> dict:
    job = {k: v for k, v in (args or {}).items() if v not in (None, "")}
    job.setdefault("command", "describe")
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/forge.py"), "--stdin"],
        input=json.dumps(job), capture_output=True, text=True, cwd=str(ROOT))
    stdout = (proc.stdout or "").strip()
    try:
        payload = json.loads(stdout) if stdout else {}
    except json.JSONDecodeError:
        payload = {"raw_stdout": stdout[:4000]}
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    if proc.returncode != 0:
        tail = "\n".join((proc.stderr or "").strip().splitlines()[-12:])
        text += f"\n\n[exit={proc.returncode}]\n{tail}"
    return {"content": [{"type": "text", "text": text}],
            "isError": proc.returncode not in (0,)}


def _respond(msg_id, result=None, error=None) -> None:
    out = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        out["error"] = error
    else:
        out["result"] = result
    sys.stdout.write(json.dumps(out) + "\n")
    sys.stdout.flush()


def main() -> int:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        method, mid, params = msg.get("method"), msg.get("id"), msg.get("params") or {}

        if method == "initialize":
            _respond(mid, {
                "protocolVersion": PROTOCOL_VERSION,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "persian-pdf-studyguide-forge", "version": "1.5.1"},
            })
        elif method in ("notifications/initialized", "initialized"):
            continue                                  # notification: no reply
        elif method == "tools/list":
            _respond(mid, {"tools": _tools()})
        elif method == "tools/call":
            if params.get("name") != SPEC["name"]:
                _respond(mid, error={"code": -32602,
                                     "message": f"unknown tool {params.get('name')}"})
            else:
                _respond(mid, _call(params.get("arguments") or {}))
        elif method == "ping":
            _respond(mid, {})
        elif method == "shutdown":
            _respond(mid, {})
            return 0
        elif mid is not None:
            _respond(mid, error={"code": -32601, "message": f"unknown method {method}"})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
