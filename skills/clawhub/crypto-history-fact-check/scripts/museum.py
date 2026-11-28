#!/usr/bin/env python3
"""Query the BTC.com Museum MCP endpoint without an MCP client.

Usage:
  python3 museum.py search "Bitcoin Pizza Day" [--locale en|zh] [--limit 5]
  python3 museum.py fetch narrative:events-pizza-day [--locale en|zh]

Standard library only. Prints the tool result as JSON.
"""
import argparse
import json
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://btc.com/api/mcp"
USER_AGENT = "bitcoin-history-skill/1.0"


def call(tool, arguments):
    body = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": tool, "arguments": arguments},
    }).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        method="POST",
        headers={
            "content-type": "application/json",
            "accept": "application/json, text/event-stream",
            "user-agent": USER_AGENT,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            sys.exit("Rate limited by the museum (429). Wait a minute and try again.")
        sys.exit(f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:500]}")
    except urllib.error.URLError as e:
        sys.exit(f"Could not reach {ENDPOINT}: {e.reason}")

    # The server answers with plain JSON; tolerate an SSE-framed reply too.
    if raw.lstrip().startswith("event:") or raw.lstrip().startswith("data:"):
        raw = "".join(
            line[5:].strip() for line in raw.splitlines() if line.startswith("data:")
        )
    msg = json.loads(raw)
    if "error" in msg:
        sys.exit(f"Error: {json.dumps(msg['error'], ensure_ascii=False)}")
    result = msg.get("result", {})
    if result.get("structuredContent") is not None:
        return result["structuredContent"]
    texts = [c.get("text", "") for c in result.get("content", []) if c.get("type") == "text"]
    joined = "\n".join(texts)
    try:
        return json.loads(joined)
    except ValueError:
        return {"text": joined, "isError": result.get("isError", False)}


def main():
    p = argparse.ArgumentParser(description="BTC.com Museum lookup")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search")
    s.add_argument("query")
    s.add_argument("--locale", choices=["en", "zh"])
    s.add_argument("--limit", type=int, default=10)
    f = sub.add_parser("fetch")
    f.add_argument("id")
    f.add_argument("--locale", choices=["en", "zh"], default="en")
    a = p.parse_args()

    if a.cmd == "search":
        args = {"query": a.query[:200], "limit": max(1, min(10, a.limit))}
        if a.locale:
            args["locale"] = a.locale
        out = call("search", args)
    else:
        out = call("fetch", {"id": a.id, "locale": a.locale})
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
