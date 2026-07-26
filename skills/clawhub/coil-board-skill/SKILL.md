---
name: coil-board
description: >-
  Buy Coil's scored, ranked stock board over x402 instead of building a scanner.
  Use when an agent needs a market read — is the tape risk-on or risk-off, which
  S&P 500 / Nasdaq-100 / macro names are set up to buy right now, or the full
  ~560-name board with opportunity, entry-timing and hold-strength scores. Pays
  per read in USDC on Base (eip155:8453) via the x402 protocol — no account, no
  card, no email. Research, not investment advice.
license: See https://coil.trade/terms
homepage: https://coil.trade/agents
---

# Coil Board API

Coil publishes a scored, ranked read of the US equity market (and a long-only
BTC/ETH trend book) that an agent can buy one read at a time over
[x402](https://x402.org). You are not buying raw OHLCV — that is free everywhere.
You are buying the **judgment**: which names are set up to buy, how strong the
regime is, and how the board ranks today, read top-down.

Everything here is an **impersonal research publication** — identical for every
buyer, scores and states only, never stop or target prices, never individualized
advice. Markets can lose money.

## When to use this skill

- You need a market-regime gate before doing something expensive: *is it risk-on
  or risk-off right now?* → call `/api/board/regime` ($0.005).
- You want today's ranked buy candidates without scanning 500 names yourself →
  call `/api/board/buylist` ($0.02).
- You want the whole board — every scored name across four books, sector lanes,
  both buy-list lanes — to do your own selection → call `/api/board/agent` ($0.25).

## The endpoints (15 — full catalogue at `GET https://coil.trade/api`)

| Endpoint | Price (USDC) | Returns |
|---|---|---|
| `GET https://coil.trade/api/board/regime`  | 0.005 | Regime verdict per book (risk-on / be-selective / stand-down) + the index→sector→name permission ladder. |
| `GET https://coil.trade/api/board/crypto`  | 0.005 | BTC/ETH long-only trend signal: LONG or CASH per sleeve, 50-day gates + the BTC 200-day master gate (UTC daily closes). |
| `GET https://coil.trade/api/board/indices` | 0.005 | The scored index row per book (SPY, QQQ, macro, BTC/ETH) — the cheapest top-down read. |
| `GET https://coil.trade/api/board/name?sym=NVDA` | 0.005 | One stock's full read + its book's regime. Any of ~560 names. |
| `GET https://coil.trade/api/board/movers`  | 0.005 | Top 10 gainers + 10 losers, fully scored. |
| `GET https://coil.trade/api/board/sectors` | 0.01  | Every sector ETF scored + the regime's green sectors. |
| `GET https://coil.trade/api/board/sector?name=Energy` | 0.01 | One sector's members, fully scored and ranked (`?etf=XLE` works too). |
| `GET https://coil.trade/api/board/leaders` | 0.01  | Top 10 leadership names per book by opportunity. |
| `GET https://coil.trade/api/board/buylist` | 0.02  | Today's ranked candidates per book across two lanes, with entry windows and leadership flags. |
| `GET https://coil.trade/api/board/top-volume` | 0.02 | Top-5 by 20-day dollar volume in every sector, fully scored. |
| `GET https://coil.trade/api/crypto/gate`   | 0.001 | The cheapest check: is the BTC 200-day master gate open? LONG/CASH per sleeve + verdict. |
| `GET https://coil.trade/api/tradfi-risk`   | 0.003 | TradFi risk-on/off for crypto agents: S&P + Nasdaq regime, sector breadth, ladder + the BTC/ETH gate. |
| `GET https://coil.trade/api/board/brief`   | 0.02  | The morning brief: regime per book + top-5 picks + biggest movers + crypto gate, in one call. |
| `GET https://coil.trade/api/board/asof?date=YYYY-MM-DD` | 0.02 | Point-in-time archived scores, verbatim from the append-only log — verifiable against the free `/api/board/proof`. |
| `GET https://coil.trade/api/board/agent`   | 0.25  | The full board: ~560 scored names, all four books, sector boards, both buy-list lanes. |

Free, before any payment: `GET /api/perf` (the engine's record vs SPY/QQQ) and
`GET /api/board/proof` (append-only sha256 commitments with a reproducible verification
recipe) — check the publisher before trusting it. `POST /api/key` with an email returns an
instant free key (~25 live calls/day on the cheap slices, `X-Coil-Key` header).

No wallet? The same board is also a **remote MCP server** — free tier, full board one market
day delayed: `claude mcp add --transport http coil https://coil.trade/mcp`

## Pairing with a broker (closing the loop)

Coil publishes **what to look at**; it never places orders and never sees an account. If the
agent also has execution — Robinhood's Trading MCP (agentic accounts, budgeted sub-account) or
Alpaca's MCP/CLI (paper trading, no funded account required) — load both servers in the same
client and follow this read order:

1. `get_market_regime` — if the ladder does not permit names, stand down. Do not place orders.
2. `get_buy_list` — consider only names that appear on it.
3. `get_stock_read` / `get_sector_read` — drill into candidates before committing.
4. Only then the broker's tools, sized by the operator's own rules.

`get_morning_brief` collapses steps 1–2 into one call. **Coil emits no position sizes, no stop
prices and no target prices** — risk definition belongs to the operator, not the publisher.
Full recipe: <https://coil.trade/agents/robinhood>

All live slices read from the **same freshest payload** (the as-of archive serves its requested date instead), so a cheap slice is never
staler than the full board. During US market hours the board recomputes about
every 5 minutes; the payload carries `computed_at` and an `intraday` flag, plus a
`freshness` block telling you when it is worth paying again.

## Try it free first

Before paying, validate your parser against the free preview — identical schema
to the paid board, previous day, top-3 names per book:

```
GET https://coil.trade/api/board/agent?preview=1
```

There is also an always-free delayed sample at
`GET https://coil.trade/api/board/free`.

## How payment works (x402)

1. `GET` the endpoint with no payment. It returns **HTTP 402** with a JSON body
   whose `accepts[0]` describes the requirement: `amount` (atomic USDC, 6
   decimals — `5000` = $0.005), `asset` (USDC `0x8335…2913`), `network`
   (`eip155:8453`, Base), and `payTo`.
2. Sign an EIP-3009 `TransferWithAuthorization` for that amount to `payTo` and
   resend the request with the `PAYMENT-SIGNATURE` header (base64 x402 v2 payload).
3. On success you get **HTTP 200** with the JSON board and an on-chain receipt in
   the `PAYMENT-RESPONSE` header.

Any standard x402 client handles this loop for you — e.g. `x402-fetch` with an
EVM signer, Coinbase AgentKit, or an x402 MCP bridge. The endpoints are indexed
in the Coinbase CDP x402 Bazaar; discovery metadata is also at
`https://coil.trade/.well-known/x402` and the OpenAPI spec at
`https://coil.trade/openapi.json`.

## Reading the payload

Each scored name carries (field names as returned):

- `opp_pct` — opportunity, 0–100. The board's headline blend.
- `entry_q` — entry quality, 0–100. Buyable now vs extended. Timing, not advice.
- `hold_q` — hold strength, 0–100. Trend durability.
- `state` — `firing` / `ready` / `setup` / `wait` / `chase` / `falling`.
- `sector`, `is_leader`, and (in buy-list lanes) a `window` note like `READY`.

Each book carries a `regime` object: `mode`, a plain-language `verdict`, which
sectors are green, and a `ladder` (index → sector → name) saying whether
individual names are enterable at all. **Read top-down**: if the regime says
stand down, the ranked names below it are context, not a green light.

## Knowing when to come back

The board is a moving read, not a one-time file. Poll `regime` cheaply to decide
whether to buy the fuller slices. The `freshness.next_refresh_at` field tells you
the earliest a new payload is worth paying for; polling faster returns the same
bytes. Outside US market hours you get the morning snapshot.

## What this is not

Not investment advice, not a managed account, not a signal service promising
returns, and not a guarantee of profit. Scores are derived from historical and
technical data and do not predict future results. See
<https://coil.trade/terms>.
