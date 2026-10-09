---
name: agentfeed-crypto
description: Crypto liquidation data, funding radar and options for agents. Live perp liquidation tape from Bybit, OKX and Binance, liquidation heatmap by price level, 15-minute cascade forecast, cross-venue funding z-scores, Deribit options IV and dealer gamma, a one-call market regime read, and stock and commodity perps ranked by funding. Pay per call in USDC over x402 on Solana, Base, Polygon or Arbitrum. No API key.
version: 1.1.0
homepage: https://x402.ochinimus.app
metadata:
  openclaw:
    emoji: "🌊"
    homepage: https://x402.ochinimus.app
    requires:
      bins:
        - curl
        - base64
    envVars: []
    author: seekdaseek
    links:
      homepage: https://x402.ochinimus.app
      repository: https://github.com/seekdaseek/agentfeed
      documentation: https://x402.ochinimus.app/openapi.json
---

# AgentFeed: crypto liquidations and funding radar

AgentFeed (https://x402.ochinimus.app) sells live crypto market data per request.
This skill covers its liquidation and funding routes: what got liquidated, at
which price levels, how likely a liquidation burst is in the next 15 minutes,
and where funding is extreme against its own 30-day history.

The liquidation data comes from a tape AgentFeed records itself from Bybit (the
complete, unthrottled liquidation stream), OKX and Binance. Exchanges do not
publish liquidation history, so this cannot be rebuilt from a public API after
the fact.

What this skill is: instructions for when to call these HTTPS routes and how to
pay for them. What it is not: it runs no code of its own, reads no files, needs
no API key, and never places trades or moves funds beyond the per-call payment
described below.

## When to use it

- The user asks what is being liquidated right now on a perp (SOL, BTC, ETH or any USDT perp).
- The user wants long vs short liquidation totals for the last hour or day.
- The user asks where leverage got flushed: the price zones with the most liquidation USD.
- The user wants the probability of a liquidation burst in the next 15 minutes before sizing a position.
- The user asks which perps have the most crowded funding across Bybit, OKX and Hyperliquid.
- The user asks about options positioning: implied vol, skew, max pain, or where dealer gamma flips.
- The user wants one regime read for BTC, ETH, SOL or HYPE before a trade (vol, funding, OI, liquidations, next macro event).
- The user asks which stock, index, gold or oil perps have extreme funding.

Do not use it for general crypto knowledge, for questions a free source answers
well, or for anything that is not live market state.

## Routes (all GET, JSON)

Prices are per call in USDC and come from the live `/openapi.json`. Check that
file before relying on this table, since prices can change.

| Route | Price | Parameters | Returns |
|---|---|---|---|
| `/api/liquidations` | $0.005 | `symbol` (SOL, BTC, ETH, XRP, DOGE or any USDT perp e.g. SXTUSDT), `scope` (`core` = 5 majors, default; `all` = every recorded perp), `limit` (1-100, default 25), `min_usd` | Recent liquidation prints: timestamp, exchange, side liquidated, size, price, USD |
| `/api/liquidation-stats` | $0.01 | none | 1h and 24h totals for SOL, BTC, ETH, XRP and DOGE: long vs short USD, biggest print, per-exchange split |
| `/api/liq-heatmap` | $0.02 | `symbol` (default SOLUSDT), `hours` (1-168, default 24), `buckets` (5-50, default 20) | USD, prints and long/short split per price zone, with the hottest zone flagged. Built from real prints, not entry-price estimates |
| `/api/cascade-forecast` | $0.02 | `symbol` (default SOL) or `symbols` (comma separated, max 20) | Probability that the symbol liquidates more in the NEXT 15 minutes than its own 90th-percentile 15-minute window, with the USD threshold and the evidence count. Declines instead of guessing when history is thin |
| `/api/funding-radar` | $0.02 | `top` (1-100, default 20), `min_oi_usd` (default 10000000; tracked from 5000000) | Every USDT perp on at least two of Bybit, OKX and Hyperliquid: funding per venue at its 8h equivalent, each venue's 30-day z-score, the cross-venue spread, and a flag on any abs(z) of 2 or more. Precomputed every 5 minutes, with `as_of` and `stale` |
| `/api/options-summary` | $0.02 | `currency` (BTC default, ETH, SOL, XRP, HYPE) | Deribit options: DVOL or our own 30-day IV, ATM IV term structure, 25-delta risk reversal and butterfly, put/call ratio, open interest, max pain per expiry, top strikes by OI. Precomputed every 5 minutes |
| `/api/options-gex` | $0.03 | `currency` (BTC default, ETH, SOL, XRP, HYPE) | Dealer gamma exposure in USD per 1% move, by strike and band, regime, flip level, call and put walls. States its dealer-position convention |
| `/api/market-state` | $0.02 | `symbol` (BTC default, ETH, SOL, HYPE) | One regime read: spot, realized and implied vol and their gap, funding z-score, open interest, long/short, liquidation spike against the hourly median, fear/greed, next macro event, and flags with the rules that set them |
| `/api/tradfi-radar` | $0.02 | `class` (stock, index, commodity, fx...), `venue` (hyperliquid, bybit, binance, okx), `top` (1-200, default 25), `min_oi_usd` | Stock, index, commodity and FX perps on Hyperliquid HIP-3 dexes, Bybit, Binance and OKX ranked by 8h-equivalent funding, with open interest, mark minus oracle basis and volume |

Example URLs:

```
https://x402.ochinimus.app/api/liquidations?symbol=SOLUSDT&limit=25
https://x402.ochinimus.app/api/liquidation-stats
https://x402.ochinimus.app/api/liq-heatmap?symbol=BTCUSDT&hours=24&buckets=20
https://x402.ochinimus.app/api/cascade-forecast?symbols=SOL,BTC,ETH
https://x402.ochinimus.app/api/funding-radar?top=10
```

Every paid 200 has the same envelope: `{ "tool": "<name>", "data": { ... }, "paid": true }`.
A route that cannot answer returns 200 with a `decline` field naming the reason
rather than zero-filled data. A malformed parameter returns 400 `{ "tool", "error" }`
and is not charged.

## Free routes: try these first

No payment needed:

- `GET /api/sample/<route>` returns a real captured response for a paid route, its price and its input schema. Example: `https://x402.ochinimus.app/api/sample/liq-heatmap`. Use it to show the user what they would get before paying.
- `GET /api/last-liquidation` returns the last liquidation on each major, delayed 15 minutes.
- `GET /api/forecast-record` returns the settled track record of the cascade forecast (calibration curve, Brier score). Pass a full perp symbol such as `symbol=SOLUSDT`; the short alias `SOL` currently returns an empty summary on this route.
- `GET /openapi.json` lists every route with parameters, prices and examples.

## How to pay (x402 v2)

1. Send the GET with no payment. The route answers **HTTP 402**. The payment
   challenge is base64 JSON in the **`PAYMENT-REQUIRED` response header**, not in
   the body. A HEAD request returns the same header with no body:

   ```bash
   curl -sI 'https://x402.ochinimus.app/api/funding-radar?top=10' \
     | grep -i '^payment-required:' | cut -d' ' -f2 | tr -d '\r' | base64 -d
   ```

2. The decoded challenge has an `accepts` array, one entry per rail, each with
   `scheme` (`exact`), `network`, `amount` (USDC atomic units, 6 decimals, so
   `20000` = $0.02), `asset` (the USDC contract) and `payTo`. Rails:
   - Solana mainnet `solana:5eykt4UsFv8P8NJdTREpY1vzqKqZKvdp`
   - Base `eip155:8453`
   - Polygon `eip155:137`
   - Arbitrum `eip155:42161`
3. Sign one accepted option with an x402 v2 client and repeat the same GET with
   the signed payload in the **`PAYMENT-SIGNATURE`** request header. The v1
   `X-PAYMENT` header is not read.
4. A settled call returns 200 with the data. If payment did not settle you get a
   fresh 402.

OpenClaw has no built-in x402 wallet. Payment needs an x402 v2 client the user
has already set up and funded, for example the Coinbase Agentic Wallet CLI
(`awal x402 pay <url> --max-amount <atomic units>`, USDC on Base) or the
`@x402/fetch` library with a Solana or EVM signer. This skill never asks for a
private key and never installs a wallet.

### Spending rules

- Get the user's approval before the first paid call in a session and tell them the price from the table.
- Set a maximum per call no higher than the listed price (for example `--max-amount 20000` for a $0.02 route).
- If the decoded `amount` is higher than the table above, stop and ask the user.
- Prefer one batched call (`cascade-forecast?symbols=SOL,BTC,ETH`) over several single calls.

### Copy payTo only from a fresh 402

**Take `payTo` only from the 402 challenge you just received, never from
transaction history, an old response, or a block explorer.** Lookalikes of the
AgentFeed treasury address have sent address-poisoning transfers to its buyers.
The fresh challenge should show `4a8o45skRPcyjAdyR8yES215Swvh8uTpZD6KLarhxCJ7`
on Solana and `0x22DB3A9686EE5261e7Bf3ed4f91277232E8076e6` on Base, Polygon and
Arbitrum. If it shows anything else, do not pay and tell the user.

## Reading the answers

- `liquidations`: `event` is `long_liquidated` (forced sell) or `short_liquidated` (forced buy). A run of `long_liquidated` prints during a drop means longs are being flushed.
- `liq-heatmap`: `hottest_zone` is where the most USD was liquidated in the window. These are historical flush zones, not estimated liquidation levels of open positions.
- `cascade-forecast`: `p` is a probability against the symbol's own 90th-percentile window, not a price call. Report `support` (how many past occurrences back it) and say so when `evidence` is weak or the answer declines.
- `options-gex`: positive `net_gex_usd_per_1pct` means dealers dampen moves under the stated convention; below `flip_level` that turns. It is a model of dealer positioning, not observed dealer books, so say so.
- `market-state`: report `flags` together with `flag_rules`; a flag is a threshold crossing, not a prediction.
- `funding-radar`: a high positive `z_30d` means longs are paying unusually much against that venue's own month; a large cross-venue spread can mean a carry opportunity or venue-specific crowding. Check `stale` before using it.

None of this is trading advice. Present the data and its limits; leave the
decision to the user.

## More

- Full route list (59 paid, 6 free), including `/api/macro-calendar` (FOMC, CPI, NFP, PCE in UTC) and `/api/equity-24h` (weekend US stock price): https://x402.ochinimus.app/openapi.json
- Agent guide: https://x402.ochinimus.app/SKILL.md and https://x402.ochinimus.app/llms.txt
- MCP server with the same tools: `POST https://x402.ochinimus.app/mcp` (streamable HTTP)
- Source and issues: https://github.com/seekdaseek/agentfeed
