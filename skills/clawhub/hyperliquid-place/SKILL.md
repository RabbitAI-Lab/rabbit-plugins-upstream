---
name: Hyperliquid Place
description: >-
  Install: clawhub install hyperliquid-place — Hyperliquid place/cancel/close
  perps for OpenClaw/MCP. Agent wallet once, auto-round, 1bp on fills (no sub).
  Keywords: hyperliquid place cancel close order perps hl_place_order hl_cancel_order
  hl_close_position trading-agent.
metadata:
  openclaw:
    emoji: "📈"
    requires:
      bins:
        - npx
    envVars:
      - name: HYPELENS_NET
        required: false
        description: testnet (default) or mainnet
      - name: HYPELENS_AGENT_PK
        required: false
        description: agent-wallet pk required only to place/cancel/close
      - name: HYPELENS_FEED_URL
        required: false
        description: optional denser heat (advisory if unset — does not block place)
---

# Hyperliquid Place — Place / Cancel / Close Perps

**One-command install (ClawHub-native — no GitHub clone):**

```bash
clawhub install hyperliquid-place
```

Also works: openclaw skills install hyperliquid-place.

**MCP hosts:**

```bash
npx -y @hypelens/hypelens-agent-rail
claude mcp add hypelens -- npx -y @hypelens/hypelens-agent-rail
```


Slug aliases: `hyperliquid-place` (canonical) · `hypelens-agent-rail` (redirect).


## First place (wallet → approve → sizeUsd)

1. `hl_new_agent_wallet` → `HYPELENS_AGENT_PK`
2. `hl_approve_payloads(agentAddress)` → MASTER signs approveAgent + ApproveBuilderFee 1bp, POST both
3. `hl_place_order({coin:"BTC", isBuy:true, sizeUsd:12, leverage:2})` — sizeUsd alone; feed optional

**First place (testnet default):** after approve, `hl_place_order({coin:"BTC", isBuy:true, sizeUsd:12, leverage:2})` — **sizeUsd alone** auto-fetches mark and rounds size (`entryPx` optional). Feed optional.

Default net is **testnet**. Set `HYPELENS_NET=mainnet` for live. Missing intel feed is **advisory** — does **not** block place. Missing PK errors name the same wallet → approve → sizeUsd path.

## Sizing rule

Warn if notional `sizeUsd` is more than **20% of account equity**. Size from balance; confirm mark before place.

## Tools

- **Place path:** `hl_quickstart`, `hl_exchange_status`, `hl_place_order`, `hl_cancel_order`, `hl_close_position`, `hl_balances`, `hl_positions`
- **Setup:** `hl_new_agent_wallet`, `hl_approve_payloads`
- **Optional edge (after install):** `hl_walls`, `hl_whale_book`, `hl_cascade`, `hl_pretrade_check`

## Keywords

hyperliquid · place · cancel · close · order · perps · hl_place_order · mcp · openclaw · builder
