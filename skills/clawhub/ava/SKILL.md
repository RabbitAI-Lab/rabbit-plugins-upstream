---
name: ava
description: >
  Ava is the accountability layer for agent-managed capital, for coding agents
  (Claude Code, Cursor, OpenClaw, Codex). Policy-gated capital runtime over HTTP
  MCP: session, per-user Turnkey wallets, mandates written before the agent gets
  authority, conditions, portfolio. Deterministic gates sit below the model, so
  nothing the model emits can widen a limit. Testnet by default, fail closed,
  and it never invents a fill: every execution ends in a receipt stating exactly
  how much it can prove. Use when the human wants their coding agent to allocate
  capital under bounds they set, or to publish a recomputable track record.
  Triggers: Ava, agentic finance, MCP trading, mandate, agent wallet, OpenClaw
  DeFi, Claude trade, Cursor finance tools.
metadata:
  openclaw:
    requires:
      env: []
      optionalEnv:
        - AVA_API_BASE
        - AVA_USER_ID
        - AVA_TOKEN
        - AVA_PORTAL
        - AVA_ENABLE_LIVE
    primaryEnv: AVA_API_BASE
    homepage: https://getava.xyz
    tags:
      - defi
      - agentic-finance
      - trading
      - mcp
      - openclaw
      - multi-chain
      - mandates
---

# Ava — finance runtime for coding agents

**You (Claude / Cursor / OpenClaw) are one agent under a human `userId`.** The same human may run several of you (Claude + Cursor + OpenClaw). Humans with no coding agent hire Ava-hosted catalog agents for multi-venue tasks.

Adapters (CoW, Jupiter, Cetus, Morpho, …) are internal settlement engines. Never ask the human to pick a venue.

## Critical rules

1. **Testnet is default.** Never claim a live chain fill unless the API returns `liveSubmit: true` and a real venue order id or tx signature. Do not use the word "paper": there is no paper mode on a blockchain, and calling a testnet settle "paper" is the vocabulary that once let a fabricated fill read as real.
2. **Session first, and keep the token.** Call `ava_session` once. It returns a `userId` AND a bearer `token`, shown once. Send the token as `Authorization: Bearer <token>` on every later call; Ava derives the caller from it server-side. A `userId` in tool arguments is a claim that must match the token, and naming anyone else is refused with `USER_ID_ASSERTION_MISMATCH`. Then create **your** agent with `ava_create_agent` (`byo-external` + a unique `label` like `openclaw-home`).
3. **Quote/mandate → confirm → approve.** Never `ava_approve_execute` without explicit human yes for capital moves.
4. **Mandates > one-shot swaps** for "home of agentic finance" loops. Pass `agentInstanceId` so multi-agent capital stays isolated.
5. **Fail closed.** Surface `LIVE_*` / error codes honestly.
6. **Identity-gated execute paths need a credential, not just a token.** The bearer token proves which account is asking; it does not prove which key controls that account's mandates. `POST /v1/copilot/approve`, `/v1/lend/execute` and `/v1/workflows/execute` check an `x-ava-agent-credential` header and refuse without one once a deployment requires it. Get one with `node scripts/ava.mjs credential --key-file <path-to-the-same-key-that-signs-your-mandates>` before relying on those paths; a mandate must already be signed with that key or the server refuses at the challenge step (`PRINCIPAL_SIGNER_UNKNOWN`).

## Environment

```bash
export AVA_API_BASE=https://api.getava.xyz         # or http://127.0.0.1:8787 for local dev
export AVA_PORTAL=base                             # policy scope default
# AVA_USER_ID and AVA_TOKEN come from ava_session / CLI session and are written
# to ~/.config/ava-openclaw/state.json (mode 0600). Never echo the token.
```

## Install

### OpenClaw

```text
install the ava skill from <path-to-repo>/packages/openclaw-skill
```

```json
{
  "skills": {
    "load": {
      "extraDirs": ["/absolute/path/to/ava/v4/packages/openclaw-skill"]
    },
    "entries": {
      "ava": {
        "env": {
          "AVA_API_BASE": "https://api.getava.xyz",
          "AVA_PORTAL": "base"
        }
      }
    }
  }
}
```

### Claude / Cursor MCP

```json
{
  "mcpServers": {
    "ava": { "url": "https://api.getava.xyz/mcp" }
  }
}
```

Local: `http://127.0.0.1:8787/mcp`

## CLI

```bash
cd packages/openclaw-skill
node scripts/ava.mjs health
node scripts/ava.mjs session
node scripts/ava.mjs call ava_create_mandate '{"portal":"base","message":"Earn on 500 USDC on Base, max 5% drawdown"}'
node scripts/ava.mjs call ava_provision_wallet '{"family":"evm"}'
# One-command execute credential: challenge → sign EIP-712 locally with the
# same key your mandates are signed with → verify. Never pass the key as an
# argument; --key-file or --key-env only.
node scripts/ava.mjs credential --key-file ~/.config/ava-openclaw/signer.key
node scripts/ava.mjs turn "Swap 10 USDC to ETH on arbitrum with 50 bps slip"
node scripts/ava.mjs approve <executionId>
node scripts/ava.mjs portfolio
```

## SOP for coding agents (Mode A multi-agent)

```text
1. ava_session                                              → userId + bearer token
2. ava_create_agent { agentId: byo-external, label: ... }   → agentInstanceId
3. ava_provision_wallet (if capital)                        → address (fund if live)
4. node scripts/ava.mjs credential --key-file <signer key>  → execute-scoped credential (15 min)
   Required before an identity-gated execute path (ava_copilot_turn's approve, defi-lend, workflows)
   will accept the request; a mandate must already be signed with this key.
5. ava_create_mandate { agentInstanceId }  OR  ava_copilot_turn
6. Human confirm if required
7. ava_eval_mandate / ava_approve_execute
8. Return receipt JSON to human / logs / PR
```

## Mode B (human has no coding agent)

```text
ava_session → ava_hire_for_task { message: "Earn on 500 USDC..." }
→ Ava picks defi-lend / defi-swap / portfolio, creates agentInstance + mandate
→ venues internal; human only sees task + receipt
```

### Mandate (preferred product loop)

```bash
curl -sS -X POST "$AVA_API_BASE/mcp" \
  -H 'content-type: application/json' \
  -H "authorization: Bearer $AVA_TOKEN" -d '{
  "jsonrpc":"2.0","id":1,"method":"tools/call",
  "params":{
    "name":"ava_create_mandate",
    "arguments":{
      "portal":"base",
      "message":"Earn on 500 USDC on Base, max 5% drawdown, exit if ETH below 2000"
    }
  }
}'
```

### Trade quote (swap settlement)

`ava_copilot_turn` → show the plan → explicit human yes → `ava_approve_execute`. On testnet this settles against the local book; on mainnet it fails closed unless a real signature and venue confirmation exist.

### Credential (identity-gated execute)

```bash
node scripts/ava.mjs credential --key-file ~/.config/ava-openclaw/signer.key \
  --scopes execute --label "openclaw-agent on laptop"
```

One command: `POST /v1/principals/challenge` (server returns EIP-712 typed
data) → sign it locally with the private key — file or env var, **never** a
CLI argument — that your mandates are signed with → `POST
/v1/principals/verify`. The resulting credential is stored in
`~/.config/ava-openclaw/state.json` (mode 0600, never printed) and sent
automatically as `x-ava-agent-credential` on later authenticated calls, the
same way the bearer token is sent as `Authorization: Bearer`.

Honest scope: this credential is what `POST /v1/copilot/approve`,
`/v1/lend/execute` and `/v1/workflows/execute` check today. It expires in 15
minutes by design — a credential is a session capability, not standing
authority — and there is no silent refresh; run the command again. A signed
mandate for the same key must already exist, or the challenge step refuses
with `PRINCIPAL_SIGNER_UNKNOWN`.

## Tool catalog

| Tool | Purpose |
|------|---------|
| `ava_session` | Human/org identity: returns `userId` + a one-time bearer `token`; many agents under one |
| `ava_list_agent_catalog` | Hosted + BYO agent types |
| `ava_create_agent` | Spawn BYO (`byo-external`+label) or hosted agent |
| `ava_list_agents` | All agent instances for userId |
| `ava_hire_for_task` | Mode B: NL task → hosted agent + mandate |
| `ava_provision_wallet` | Turnkey wallet: evm / solana / sui |
| `ava_create_mandate` | Capital mandate (+ optional agentInstanceId) |
| `ava_list_mandates` | List mandates (filter by agentInstanceId) |
| `ava_eval_mandate` | Evaluate exits (live price if no snapshot) |
| `ava_copilot_turn` | NL trade plan + quote |
| `ava_approve_execute` | Testnet settle, or mainnet signed path that fails closed |
| `ava_portfolio` | Balances + fills |
| `ava_get_price` | Spot price |
| `ava_create_automation` | Price condition |
| `ava_list_automations` / `ava_eval_automation` | Automations |
| `ava_quote_swap` / `ava_plan_intent` | Structured plan helpers |

## Live capital

- Provisioned wallets + live quotes exist.
- CoW / Jupiter signed submit paths exist; empty wallets return honest `LIVE_INSUFFICIENT_BALANCE` / simulation fails.
- Never invent fills.

## Docs

- `docs/AGENTS.md` — coding-agent connect
- `docs/MCP.md` — protocol detail
- `research/progress/AGENTS_ARE_THE_USERS.md` — positioning lock
- `research/progress/TWO_USER_MODES.md` — multi-agent BYO + Ava-hosted
- `research/progress/HOME_OF_AGENTIC_FINANCE_2026-07-23.md` — market thesis
