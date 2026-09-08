---
name: Place Hyperliquid
description: >-
  Place Hyperliquid perps — order/cancel/close via hl_place_order for OpenClaw/MCP.
  Agent wallet once, auto-round, 1bp builder fees on mainnet fills (no sub).
  Keywords: place order cancel close hyperliquid perps trading hl_place_order
  hl_cancel_order hl_close_position trading-agent.
topics:
  - place
  - order
  - cancel
  - close
  - hyperliquid
  - perps
  - trading
keywords:
  - place
  - order
  - cancel
  - close
  - hyperliquid
  - perps
  - trading
  - hl_place_order
  - hl_cancel_order
  - hl_close_position
metadata:
  openclaw:
    emoji: "📈"
    requires:
      bins:
        - npx
    envVars:
      - name: HYPELENS_NET
        required: false
        description: "mainnet (default, live 1bp fees) or testnet (practice)"
      - name: HYPELENS_AGENT_PK
        required: false
        description: agent-wallet pk required only to place/cancel/close
      - name: HYPELENS_FEED_URL
        required: false
        description: optional denser heat (advisory if unset — does not block place)
---

# Place Hyperliquid — install that works → first place in 3 steps

## Install (only these — no GitHub/skills.sh clone)

```bash
clawhub install hyperliquid-place
```

```bash
npx -y @hypelens/hypelens-agent-rail
```

```bash
claude mcp add hypelens -- npx -y @hypelens/hypelens-agent-rail
```

Also: `openclaw skills install hyperliquid-place`. Slugs: `hyperliquid-place` (canonical) · `hypelens-agent-rail` (redirect).

## Fee path = MAINNET (1bp builder)

Default net is **mainnet** (live 1bp builder fees). Escape: `HYPELENS_NET=testnet` to practice. `MAINNET_PLACEMENT_ENABLED=true`.

1. Approve on the net you will trade (`hl_approve_payloads` → MASTER signs approveAgent + ApproveBuilderFee **1bp**)
2. Net defaults to mainnet (optional: `HYPELENS_NET=testnet`)
3. First mainnet place with sizeUsd: `hl_place_order({coin:"BTC", isBuy:true, sizeUsd:12, leverage:2})`

## First place in 3 steps (wallet → approve → sizeUsd)

1. `hl_new_agent_wallet` → set `HYPELENS_AGENT_PK`
2. `hl_approve_payloads(agentAddress)` → MASTER signs approveAgent + ApproveBuilderFee **1bp**, POST both
3. `hl_place_order({coin:"BTC", isBuy:true, sizeUsd:12, leverage:2})` — **sizeUsd alone**; feed optional

Missing intel feed is **advisory** — does **not** block place. Missing PK errors name the same wallet → approve → sizeUsd path.

## Sizing rule

Warn if notional `sizeUsd` is more than **20% of account equity**. Size from balance; confirm mark before place.

## Tools

- **Place path:** `hl_quickstart`, `hl_exchange_status`, `hl_place_order`, `hl_cancel_order`, `hl_close_position`, `hl_balances`, `hl_positions`
- **Setup:** `hl_new_agent_wallet`, `hl_approve_payloads`
- **Optional edge (after install):** `hl_walls`, `hl_whale_book`, `hl_cascade`, `hl_pretrade_check`

## Keywords

place · order · cancel · close · hyperliquid · perps · trading · hl_place_order · mcp · openclaw · builder
