#!/usr/bin/env python3
"""MCP wrapper for your x402 API (fastmcp).

⚠️ SECURITY: reads X402_API_KEY from the environment and sends it in every
outbound request (x-api-key header). The API key is spending-capable
(x402, USDC) — never log it, never commit it, and keep it scoped.
HTTP is blocked by default: set X402_ALLOW_HTTP=1 only if you deliberately
accept sending the key over plain HTTP.
"""
import os, ssl, urllib.request, json
from fastmcp import FastMCP

mcp = FastMCP("my-x402-api")
ALLOW_HTTP = os.environ.get("X402_ALLOW_HTTP", "") == "1"
BASE = os.environ.get("API_BASE", "https://show-zum-anyway-sanyo.trycloudflare.com")
_CA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "northcap-ca.pem")


def _ctx():
    if "https://show-zum-anyway-sanyo.trycloudflare.com" in BASE or "localhost" in BASE:
        return ssl.create_default_context(cafile=_CA)
    return ssl.create_default_context()
if BASE.startswith("http://") and not ALLOW_HTTP:
    raise SystemExit("ERROR: API_BASE uses HTTP, but the API key is spending-capable. "
                     "Use HTTPS (API_BASE=https://...), or set X402_ALLOW_HTTP=1 consciously.")
KEY = os.environ.get("X402_API_KEY", "")

def _call(path, params=None):
    url = BASE + path
    if params: url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={"x-api-key": KEY})
    with urllib.request.urlopen(req, timeout=20, context=_ctx()) as r:
        return json.loads(r.read().decode())

@mcp.tool()
def get_signals(symbol: str = "BTCUSDT") -> dict:
    """Fetch signal data from the API."""
    return _call("/v1/signals", {"symbol": symbol})

if __name__ == "__main__":
    mcp.run()
