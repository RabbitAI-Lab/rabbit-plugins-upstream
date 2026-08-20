#!/usr/bin/env python3
"""MCP-wrapper for din x402-API (fastmcp)."""
import os, urllib.request, json
from fastmcp import FastMCP

mcp = FastMCP("min-api")
BASE = os.environ.get("API_BASE", "http://localhost:8791")
KEY = os.environ.get("X402_API_KEY", "")

def _call(path, params=None):
    url = BASE + path
    if params: url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={"x-api-key": KEY})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode())

@mcp.tool()
def get_signals(symbol: str = "BTCUSDT") -> dict:
    """Hent signal-data fra API'et."""
    return _call("/v1/signals", {"symbol": symbol})

if __name__ == "__main__":
    mcp.run()
