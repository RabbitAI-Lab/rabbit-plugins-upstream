#!/usr/bin/env python3
"""Preview or safely merge a Dataify remote MCP configuration."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import platform
import shutil
import tempfile
from urllib.parse import quote
from urllib.parse import parse_qs, urlsplit
import urllib.request


ALL_TOOLS = (
    "user_info", "web_unlocker", "google_serp", "yandex_serp", "duckduckgo_serp", "bing_serp",
    "amazon", "youtube", "facebook", "instagram", "reddit", "walmart", "google", "booking",
    "indeed", "airbnb", "google_play_store", "github", "tiktok", "linkedin", "glassdoor",
    "twitter", "crunchbase", "zillow", "ebay",
)
PRESETS = {
    "lightweight": ("user_info", "web_unlocker", "google_serp"),
    "research": ("user_info", "google_serp", "web_unlocker", "github", "crunchbase", "indeed", "glassdoor"),
    "ecommerce": ("user_info", "amazon", "ebay", "walmart", "google_serp", "web_unlocker"),
    "social": ("user_info", "facebook", "instagram", "tiktok", "twitter", "linkedin", "reddit", "youtube"),
    "all": ALL_TOOLS,
}
CAPABILITIES = {"search": PRESETS["lightweight"], "research": PRESETS["research"], "ecommerce": PRESETS["ecommerce"], "social": PRESETS["social"]}


def tools_for_capability(capability: str) -> list[str]:
    if capability not in CAPABILITIES:
        raise ValueError("Unknown capability: {}".format(capability))
    return list(CAPABILITIES[capability])


def inspect_config(config: dict) -> dict:
    server = config.get("mcpServers", {}).get("dataify", {})
    url = server.get("url", "") if isinstance(server, dict) else ""
    query = parse_qs(urlsplit(url).query)
    return {"configured": bool(url), "server": "dataify", "tools": [item for value in query.get("tools", []) for item in value.split(",") if item], "credential": "configured" if query.get("token") else "missing", "url": "https://mcp.dataify.com/mcp?token=<redacted>" if url else None}


def verify_server(url: str, timeout: float = 30) -> dict:
    payload = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "dataify-skill-check", "version": "1.0"}}}).encode("utf-8")
    request = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read(2048).decode("utf-8", errors="replace")
            return {"status": "ready", "http_status": int(getattr(response, "status", 200)), "protocol_response": bool(body)}
    except urllib.error.HTTPError as exc:
        return {"status": "invalid_credentials" if exc.code in {401, 403} else "unavailable", "http_status": exc.code, "protocol_response": False}
    except (urllib.error.URLError, TimeoutError):
        return {"status": "unavailable", "http_status": None, "protocol_response": False}


def target_for(client: str, home: Path | None = None, system: str | None = None) -> Path | None:
    home = home or Path.home()
    system = (system or platform.system()).lower()
    mac = system in {"darwin", "macos"}
    if client == "claude":
        return home / ("Library/Application Support/Claude/claude_desktop_config.json" if mac else ".config/claude/claude_desktop_config.json")
    if client == "cursor":
        return home / ("Library/Application Support/Cursor/User/mcp.json" if mac else ".cursor/mcp.json")
    if client == "windsurf":
        return home / ("Library/Application Support/Windsurf/User/mcp.json" if mac else ".codeium/windsurf/mcp_config.json")
    if client == "codex":
        return home / ".codex/mcp.json"
    return None


def validate_tools(tools: list[str]) -> list[str]:
    values = list(dict.fromkeys(item.strip() for item in tools if item.strip()))
    unknown = sorted(set(values) - set(ALL_TOOLS))
    if unknown:
        raise ValueError("Unknown Dataify MCP tools: {}".format(", ".join(unknown)))
    return values


def configure(path: Path, token: str, tools: list[str], write: bool = False) -> dict:
    if not token.strip():
        raise RuntimeError("DATAIFY_API_TOKEN is not configured")
    tools = validate_tools(tools)
    existing = {}
    if path.exists():
        try:
            existing = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError("Existing MCP configuration is not valid JSON: {}".format(exc)) from exc
    existing.setdefault("mcpServers", {})
    url = "https://mcp.dataify.com/mcp?token={}&tools={}".format(quote(token.strip(), safe=""), ",".join(tools))
    existing["mcpServers"]["dataify"] = {"url": url}
    backup = None
    if write:
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            backup = path.with_suffix(path.suffix + ".bak")
            shutil.copy2(path, backup)
        fd, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
                json.dump(existing, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            os.replace(temporary, path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
    return {"client_config": str(path), "tools": tools, "written": write, "backup": str(backup) if backup else None, "server": "dataify", "credential": "configured"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client", choices=("claude", "cursor", "windsurf", "codex", "manual"), default="manual")
    parser.add_argument("--preset", choices=tuple(PRESETS), default="lightweight")
    parser.add_argument("--tools", help="Comma-separated override from the supported tool catalog.")
    parser.add_argument("--config-file", type=Path)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--inspect", action="store_true")
    parser.add_argument("--verify", action="store_true")
    parser.add_argument("--capability", choices=tuple(CAPABILITIES))
    args = parser.parse_args()
    target = args.config_file or target_for(args.client)
    if args.inspect:
        existing = json.loads(target.read_text(encoding="utf-8")) if target and target.exists() else {}
        print(json.dumps(inspect_config(existing), ensure_ascii=False, indent=2))
        return 0
    token = os.environ.get("DATAIFY_API_TOKEN", "").strip()
    if not token:
        print("DATAIFY_API_TOKEN is not configured. See https://dashboard.dataify.com/login?utm_source=skill.", file=__import__("sys").stderr)
        return 1
    tools = validate_tools(args.tools.split(",") if args.tools else tools_for_capability(args.capability) if args.capability else list(PRESETS[args.preset]))
    if target is None:
        result = {"server": "dataify", "url": "https://mcp.dataify.com/mcp?token=<redacted>&tools={}".format(",".join(tools))}
        if args.verify:
            configured_url = "https://mcp.dataify.com/mcp?token={}&tools={}".format(quote(token, safe=""), ",".join(tools))
            result["verification"] = verify_server(configured_url)
        print(json.dumps(result, indent=2))
        return 0
    try:
        result = configure(target, token, tools, write=args.write)
        if args.verify:
            configured_url = "https://mcp.dataify.com/mcp?token={}&tools={}".format(quote(token, safe=""), ",".join(tools))
            result["verification"] = verify_server(configured_url)
    except (OSError, ValueError, RuntimeError) as exc:
        print(str(exc), file=__import__("sys").stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
