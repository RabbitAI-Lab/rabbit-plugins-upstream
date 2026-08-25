# @ava/openclaw-skill

OpenClaw skill-pack for Ava, the accountability layer for agent-managed capital.

**Loop:** mandate agreed before the agent has authority → conditions evaluated
against live data → execution passes the mandate and policy gates → receipt
stating exactly how much it can prove.

Same tools as Ava's HTTP MCP (`/mcp`). Testnet by default. Mainnet execution is
fail closed, and Ava never writes a receipt for a fill it cannot show.

The word "paper" is deliberately absent. There is no paper mode on a blockchain,
and calling a testnet settle "paper" is the vocabulary that once let a fabricated
fill pass for a real one.

## Why this exists

Distribution for crypto agents in 2026 is **OpenClaw skills + MCP**, not portal matrices. Bankr and Elsa ship skill packs; Ava ships one that wraps the existing runtime.

## Quick start

```bash
# 1. Run Ava api-worker (from monorepo root)
pnpm --filter @ava/api-worker exec tsx src/index.ts
# or your usual dev command on :8787

# 2. From this package
export AVA_API_BASE=http://127.0.0.1:8787
node scripts/ava.mjs health
node scripts/ava.mjs session
node scripts/ava.mjs turn "Swap 10 USDC to SUI on sui with 50 bps slip"
# user says yes
node scripts/ava.mjs approve <executionId>
node scripts/ava.mjs portfolio
```

## OpenClaw install

```text
install the ava skill from <monorepo>/packages/openclaw-skill
```

Or point `skills.load.extraDirs` at this directory (see `SKILL.md`).

## Files

| File | Role |
|------|------|
| `SKILL.md` | Agent instructions (SOP, rules, tools) |
| `scripts/ava.mjs` | Zero-dep CLI over MCP/REST |
| `catalog.json` | Marketplace-style metadata |
| `.env.example` | Local env template |

## MCP tools used

- `ava_copilot_turn`
- `ava_approve_execute` (testnet settle after confirm; mainnet fails closed without a real signature)
- `ava_portfolio`, `ava_get_price`, automations, plan/quote

Docs: `../../docs/MCP.md`, `../../docs/PRODUCT_REBOOT.md`.

## Tests

```bash
node --test ./scripts/ava.test.mjs
```
