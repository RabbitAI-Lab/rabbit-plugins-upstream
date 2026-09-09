---
name: Hyperliquid Trading Place
description: >-
  Place, cancel, or close Hyperliquid perps when the user
  explicitly asks to trade/place/cancel/close/execute. Not for wallet
  research (use hyperliquid-radar). Install: clawhub install hyperliquid-trading-place
  then cd skills/hyperliquid-trading-place/scripts && npm install && node start-mcp.mjs.
  Keywords: hyperliquid place cancel close hl_place_order perps openclaw mcp.
topics: [hyperliquid, trading, place, order, cancel, perps, openclaw, mcp, builder]
metadata:
  openclaw:
    emoji: "📈"
    requires:
      bins: [node, npm]
---

# Hyperliquid Trading Place

**WARNING:** Default network is mainnet real funds. Confirm size/side/leverage before place/cancel/close.

**Use when:** explicit trade / place / cancel / close / execute. Research: hyperliquid-radar.

**Why this rail:** Install alone equals zero dollars. Live fills only pay 1bp builder.

## Install (local scripts)

```bash
clawhub install hyperliquid-trading-place
cd skills/hyperliquid-trading-place/scripts && npm install
```

Start pinned MCP from local install:

```bash
node start-mcp.mjs
```

Alt: openclaw skills install, then same scripts install plus node start-mcp.mjs.

## Consent (ClawScan-safe)

- Only call `hl_place_order` / cancel / close when the user explicitly asks to **trade**, **place**, or **execute**.
- Do not place unsolicited. Do not solicit private keys unprompted.
- Heat tools (`hl_walls`, `hl_whale_book`, `hl_cascade`, `hl_pretrade_check`) are fine after install for sizing advice; place only on explicit user trading intent.

## Optional setup (when the user wants to trade)

Guidance path if the user asks to place or execute on mainnet:

1. `hl_quickstart` — or `hl_new_agent_wallet` → `export HYPELENS_AGENT_PK=<pk>`
2. `hl_approve_payloads(agentAddress)` → MASTER signs+POSTs approveAgent + ApproveBuilderFee **1bp** to `0x9548B8E9554a1968843B3C380431b10996247c88`
3. `hl_balances` — if equity=0, ask the user to deposit **USDC** to `fundHow.depositAddress` on [app.hyperliquid.xyz](https://app.hyperliquid.xyz) (~$15+), then recheck
4. `hl_place_order({coin:"BTC", isBuy:true, sizeUsd:12, leverage:2})` — **sizeUsd alone = IOC/market** (fills accrue 1bp builder); pass `entryPx` only for GTC limit. Only after user trading intent.

Paper: `HYPELENS_NET=testnet`. Default network is mainnet.

## Tools

- Place path: `hl_quickstart`, `hl_place_order`, `hl_cancel_order`, `hl_close_position`, `hl_balances`, `hl_positions`
- Setup: `hl_new_agent_wallet`, `hl_approve_payloads`
- Sizing advice (any time after install): `hl_walls`, `hl_whale_book`, `hl_cascade`, `hl_pretrade_check`

Fee: 1bp on live fills only (no subscription). Builder: `0x9548B8E9554a1968843B3C380431b10996247c88`.

## Related


Primary slug (same rail): `hyperliquid-place` — same scripts install path.
