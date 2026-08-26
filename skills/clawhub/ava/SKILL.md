---
name: ava
description: Use Ava to execute bounded DeFi from a coding agent (Claude Code, Cursor, Codex, OpenClaw). Live money is ava_lend_execute on Base (Morpho), never ava_copilot_turn. Connect https://www.getava.xyz/mcp after ava_session.
license: MIT-0
compatibility: OpenClaw, Claude Code, Cursor, Codex. Requires HTTP MCP https://www.getava.xyz/mcp
metadata:
  homepage: https://getava.xyz
  mcp: https://www.getava.xyz/mcp
  clawhub: https://clawhub.ai/kamalbuilds/skills/ava
---

# Ava

Ava executes bounded DeFi. You never hold the key. You never invent a fill. Always call `tools/list` on the live server.

## Install

```bash
openclaw skills install @kamalbuilds/ava
```

ClawHub also documents `npx skills add`:

```bash
npx skills add @kamalbuilds/ava
```

## Hard rules

- Live money is `ava_lend_execute` on Base (Morpho). Never use `ava_copilot_turn`, `ava_preview_tx`, or `ava_approve_execute` for live or mainnet funds.
- After `ava_session`, connect HTTP MCP `https://www.getava.xyz/mcp` with `Authorization: Bearer <token>` before any other Ava call.
- Default portal is Base. Do not demo Sui. Do not swap USDC to SUI or route through Arbitrum.
- `ava_create_mandate` is an Ava row, not user EIP-712 consent. Say that. A signed user-controlled mandate is a separate step.
- `ava_plan_standing` returns an unsigned envelope. There is no MCP authorize or revoke. Do not claim hourly rotation is live.
- Copilot / `preview_tx` / `approve_execute` are testnet only. `ava_portfolio` is seeded simulation. Never narrate them as live fills or holdings.

## Two loops

| Loop | Tools | What it is |
| --- | --- | --- |
| Testnet (default trap) | `ava_copilot_turn` → `ava_preview_tx` → `ava_approve_execute` | Testnet quote. Not a live path. |
| Live lend | `ava_session` → MCP connect → `ava_create_mandate` → `ava_lend_execute` | Morpho Blue on Base. Two-phase `previewHash`. |

If the user wants real DeFi, use the live lend loop. Copilot is not a fallback and not a rehearsal of `ava_lend_execute`.

## Connect

Production MCP: `https://www.getava.xyz/mcp` (same as `https://api.getava.xyz/mcp`).

1. `ava_session` → keep `userId` and the one-time bearer `token`.
2. Connect HTTP MCP with `Authorization: Bearer <token>`.
3. Then run the live loop. Stop on `LEND_INSUFFICIENT_BALANCE`.

Claude Code:

```bash
claude mcp add --transport http ava https://www.getava.xyz/mcp \
  --header "Authorization: Bearer <token>"
```

Cursor / Codex: HTTP MCP at that URL with the same header.

## Live lend SOP

1. `ava_create_mandate` — tight lend-only (asset, chain, amount, allowed kinds). Tell the human it is an Ava row, unsigned until they sign.
2. `ava_lend_execute` without `previewHash` → preview.
3. Show the preview. Wait for an explicit yes.
4. `ava_lend_execute` again with the same `mandateId` and returned `previewHash`.
5. Return the receipt. Success is `proof.standing: chain-confirmed`. `verified: true` with unconfirmed standing is not a fill. `ok: true` with `filled: false` is not a fill.
6. Never retry after an ambiguous sign or submit. A new `executionId` is a new economic action.

## Example

User: "Lend 100 USDC on Base with Morpho, under a tight mandate."

```text
ava_session
→ connect https://www.getava.xyz/mcp with Bearer token
→ ava_create_mandate (portal: base, lend-only USDC on Morpho)
→ ava_lend_execute (no previewHash) → show preview, wait for yes
→ ava_lend_execute (same mandateId + previewHash)
→ receipt with proof.standing: chain-confirmed
```

## Proven venues

Re-check with `tools/list`. Proven: Morpho Blue on Base, Aave v3 on Monad / BNB / Avalanche. Do not list CoW, Jupiter, Cetus, Hyperliquid, Pendle, or Euler as live. A same-chain swap is one leg; do not invent a bridge.

## Env

```bash
export AVA_API_BASE=https://api.getava.xyz
export AVA_PORTAL=base
```

Fail closed. Typed refusal codes are success of the gate. The LLM is not the signer, policy, or verifier.
