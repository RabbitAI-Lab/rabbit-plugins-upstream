---
name: trustgrade
description: "Check crypto trust before acting — use when evaluating DeFi protocols, stablecoins, exchanges, tokens, or AI agents for safety, or before an agent executes a transaction; returns TrustGrade Scores (0-100) with grade, confidence, and risk level."
---

# TrustGrade — Crypto Trust Verification

Score crypto entities on trust before acting on them. One call returns a 0–100 TrustGrade Score with letter grade, confidence, and risk tier. 500+ entities scored: DeFi protocols, stablecoins, exchanges, tokens, and AI agents.

## When to use

- A user asks whether a protocol, stablecoin, exchange, or token is safe or trustworthy
- Comparing entities on trust ("USDC vs USDT vs DAI")
- An AI agent is about to execute a transaction — verify BEFORE executing
- Verifying another AI agent's identity before interacting with it
- Any crypto recommendation flow: score first, then advise

## How to call (MCP)

Server: `@trustgrade/mcp-server` (stdio transport, no API key required)

```json
{"mcpServers":{"trustgrade":{"command":"npx","args":["-y","@trustgrade/mcp-server"]}}}
```

Optional env `TRUSTGRADE_API` overrides the default base `https://api.trustgrade.ai`.

## Tools

- **check_trust** — the primary tool: TrustGrade Score (0–100), letter grade, confidence %, risk level for any scored entity
- **compare_trust** — side-by-side trust comparison of multiple entities
- **verify_transaction** — pre-flight check before an agent executes: agent limits, business verification, trust score, recipient whitelist, manipulation flags; returns an approved/rejected decision with a cryptographic receipt
- **verify_agent** — verify an AI agent's identity: DID, business KYB status, trust score, active status
- **get_business** — business verification status behind an entity or agent
- **register_agent** — register a new AI agent (model, capabilities) to get scored
- **list_entity_types** — all supported entity types

## Reading the result

- **Score 0–100** with letter grade (A+ … F) and confidence %
- **Risk level:** LOW · MEDIUM · HIGH
- **verify_transaction** returns `approved` or `rejected` with reasons — a rejection is a hard stop, not a suggestion
- The score reflects evidence quality and verification status — not price prediction or investment merit

## Rules

- Call check_trust before recommending any crypto entity; never call an unscored entity "safe"
- Quote the score with its grade and confidence; never round or editorialize
- If an entity isn't indexed, say so — do not guess a score
- For agent transactions: verify_transaction BEFORE execution; treat `rejected` as final
- Never present trust scores as investment advice or price forecasts
