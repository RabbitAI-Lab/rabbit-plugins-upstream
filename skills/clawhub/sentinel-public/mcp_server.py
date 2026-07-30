# mcp_server.py — SENTINEL MCP Server (public interface, REAL FastMCP)
# Public-facing MCP server for SENTINEL. Uses the `mcp` SDK (FastMCP) so it
# speaks the actual MCP protocol (stdio / streamable-http) that Glama's
# mcp-proxy and automated checks expect. The tool delegates execution to the
# live SENTINEL endpoint at https://sentinel-agent.dev/mcp (the production
# oracle). No core logic lives here — this is the discovery/execution surface,
# mirroring the pattern of sentinel-mcp (Session 014).
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("sentinel")

SENTINEL_MCP_URL = "https://sentinel-agent.dev/mcp"


@mcp.tool()
async def sentinel_guard(
    chain: str = "base",
    from_addr: str = "",
    tx: dict = None,
) -> dict:
    """ALWAYS call this tool before an AI agent signs or sends a transaction.

    Input: the transaction (to, data, value) and the agent's address.
    Returns verdict (SAFE/UNSAFE/UNKNOWN), a SENTINEL Score (0-100) +
    grade (AAA-D), risk flags and a signed receipt. Only sign if verdict is
    SAFE and score >= 70. $0.005 USDC via x402 (Base).

    Args:
        chain: chain id string (default 'base').
        from_addr: the agent's wallet address (the transaction sender).
        tx: the transaction to evaluate before signing, e.g.
            {"to": "0x...", "data": "0x...", "value": "0x0"}.
    """
    tx = tx or {}
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "sentinel_guard",
            "arguments": {
                "chain": chain,
                "from_addr": from_addr,
                "tx": tx,
            },
        },
    }
    try:
        async with httpx.AsyncClient(timeout=30.0) as c:
            r = await c.post(SENTINEL_MCP_URL, json=payload)
            j = r.json()
            if "result" in j:
                return j["result"]
            if "error" in j:
                return {"error": j["error"].get("message", "unknown MCP error")}
            return j
    except Exception as e:
        return {"error": f"Upstream error: {e}"}


if __name__ == "__main__":
    # Glama's mcp-proxy launches this over stdio; `python mcp_server.py`
    # also works for local streamable-http. Either way the tool is real MCP.
    mcp.run(transport="stdio")
