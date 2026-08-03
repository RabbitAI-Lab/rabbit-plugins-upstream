# SENTINEL — Agent-Level Transaction Safety Oracle

> **M2M-native. x402 payments. Zero accounts. Zero API keys. Pre-execution safety for autonomous agents.**

> **Endpoint:** `https://sentinel-agent.dev` | **Version:** 1.0.0

This repo contains the **public interface, MCP server definitions, and developer kit** for SENTINEL. The core oracle is deployed at [sentinel-agent.dev](https://sentinel-agent.dev).

* * *

## What SENTINEL Is

SENTINEL is a **pre-execution transaction safety oracle** for autonomous AI agents. Before an agent signs a blockchain transaction, it calls SENTINEL and receives a **SAFE / UNSAFE / UNKNOWN** verdict plus a standardized **SENTINEL Score (AAA–D)** and a signed receipt. Pure M2M — no human in the loop.

- **Stack:** FastAPI + Supabase + Render (proven in production with the M2M model family)
- **Payment:** x402 v2, CAIP-2 compliant (`eip155:8453` + Solana)
- **Distribution:** CDP Bazaar + Agentic Market + 402 Index + PyPI (AgentKit/MCP providers)

* * *

## MCP Server (Model Context Protocol)

SENTINEL exposes a native **MCP server** compatible with Claude Desktop, Claude Code, Cursor, Windsurf, Smithery, and Glama.

### Connect in Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "sentinel": {
      "url": "https://sentinel-agent.dev/mcp"
    }
  }
}
```

### Connect in Claude Code

```bash
claude mcp add sentinel --url https://sentinel-agent.dev/mcp
```

### MCP Tools

| Tool | Description | Price |
| --- | --- | --- |
| `sentinel_guard` | Evaluate a transaction before signing — returns SAFE/UNSAFE verdict, SENTINEL Score (AAA-D), risk flags, signed receipt | $0.005 USDC |

### MCP Protocol

- **Transport:** stdio / streamable-http (real FastMCP SDK, `mcp` 1.26+)
- **Manifest:** `mcp_server.py` (FastMCP, `@mcp.tool()`)
- **Payment:** x402 micropayments on Base
- This `sentinel-public` repo is the **public MCP interface**; the tool
  delegates execution to the live endpoint at `https://sentinel-agent.dev/mcp`.

* * *

## The Problem This Solves

Autonomous agents pay for API calls via x402, but **nothing tells them whether the transaction they are about to sign is safe to execute**. A malicious `payTo`, an infinite ERC-20 approval, or a honeypot contract still gets paid. SENTINEL closes that gap: it is the verification step *upstream* of the payment.

SENTINEL covers:
- **Contract security** (honeypot, owner, taxes, blacklist)
- **Execution simulation** (balance drain)
- **MEV / sandwich exposure** (large swaps)
- **ERC-20 approval risk** (infinite allowances — the #1 agent loss vector)

The SENTINEL Score (0–100, grade AAA–D) is a transparent, graduated rating so agents and dashboards can quote a standard.

* * *

## Start Building

```bash
# Clone and configure
git clone https://github.com/teodorofodocrispin-cmyk/sentinel-public
cd sentinel-public
pip install -r requirements.txt

# Run the public MCP server locally (delegates to the live endpoint)
uvicorn mcp_server:app --reload --port 8001

# Test the manifest
curl https://sentinel-agent.dev/mcp
# → 402 Payment Required if unauthenticated, or tools/list if authenticated
```

* * *

_SENTINEL — Built in Bogotá, Colombia. Part of the M2M x402 model family (VeraData, Intelica, TrustBoost, SENTINEL)._
