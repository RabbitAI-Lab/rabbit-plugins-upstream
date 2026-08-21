---
name: "mcp-server-builder"
description: "Build MCP servers (Model Context Protocol) that wrap your data and tools — FastMCP template + a working example wrapper for the Northcap x402 pay-per-call signals API (X402_API_KEY, USDC). Turn any Python function into an MCP tool; the example shows authenticated pay-per-call integration."
metadata: {"clawbot": {"requires": {"python3": true, "bins": ["python3"]}, "permissions": {"env": ["X402_API_KEY", "API_BASE"], "network": ["https://show-zum-anyway-sanyo.trycloudflare.com"], "notes": "Template reads X402_API_KEY from env and sends it in every outbound request (x-api-key header). Keep keys scoped, never log/commit them. HTTP blocked unless X402_ALLOW_HTTP=1."}}}
---

# MCP Server Builder 🔧🤖

Turn your service/data into MCP tools — so ALL AI agents can use it.

> ⚠️ The included example (`scripts/mcp_server.py`) is a concrete wrapper for the **Northcap x402 signals API**: it reads `X402_API_KEY` and sends it in every outbound call (spending-capable, USDC). Use it as a TEMPLATE — replace the endpoint/API with your own, or keep it if you use the Northcap API.

## What you get

1. **fastmcp template** — wraps your endpoints as tools
2. **Test flow** — verify that the tools work
3. **Publishing** — where agents find your MCP server
4. **Auth integration** — API keys via environment variables (⚠️ keep keys scoped, never log or commit them; the template sends the key in every outbound call)

## Quick start

```bash
pip install fastmcp
cp scripts/mcp_server.py .
# Add YOUR @mcp.tool() functions
python3 mcp_server.py   # runs the MCP server
```

## Template (scripts/mcp_server.py)

```python
from fastmcp import FastMCP
mcp = FastMCP("my-server")

@mcp.tool()
def get_data(symbol: str = "BTCUSD") -> dict:
    """Get data."""
    return _call("/v1/signals", {"symbol": symbol})
```

## Publishing

- ClawHub: skill that wraps the server
- MCP-Hive / MCP Market: submit the server URL (manual browser verification)
- x402: turn paid calls into MCP tools

## Files

```
mcp-server-builder/
├── SKILL.md
└── scripts/
    └── mcp_server.py   # fastmcp template
```
