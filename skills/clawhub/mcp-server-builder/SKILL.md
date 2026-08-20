---
name: "mcp-server-builder"
description: "Build MCP servers (Model Context Protocol) that wrap your data and tools — FastMCP templates, client examples, and deployment notes. Turn any Python function into an MCP tool."
---

# MCP Server Builder 🔧🤖

Gør din service/data til MCP-værktøjer — så ALLE AI-agenter kan bruge den.

## Hvad du får

1. **fastmcp-skabelon** — wrapper dine endpoints som tools
2. **Test-flow** — verificér at tools virker
3. **Publicering** — hvor agenter finder din MCP-server
4. **Auth-integration** — API-nøgler via miljøvariabler

## Hurtig start

```bash
pip install fastmcp
cp scripts/mcp_server.py .
# Tilføj DINE @mcp.tool()-funktioner
python3 mcp_server.py   # kører MCP-serveren
```

## Skabelon (scripts/mcp_server.py)

```python
from fastmcp import FastMCP
mcp = FastMCP("min-server")

@mcp.tool()
def get_data(symbol: str = "BTCUSD") -> dict:
    """Hent data."""
    return _call("/v1/signals", {"symbol": symbol})
```

## Publicering

- ClawHub: skill der wrapper serveren
- MCP-Hive / MCP Market: submit server-URL (manuel browser-verifikation)
- x402: gør betalte kald til MCP-tools

## Filer

```
mcp-server-builder/
├── SKILL.md
└── scripts/
    └── mcp_server.py   # fastmcp-skabelon
```
