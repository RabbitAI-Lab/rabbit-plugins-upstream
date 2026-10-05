---
name: mentat
description: MENTAT, the agent-native OTC venue. Escrow settlement on Base (atomic, no admin keys), CoW Protocol relay (agent-signed, MEV-protected), and an XMR route via Wagyu (XMR/USDC both directions, three legs, one proof per leg). Every quote and order response carries settlement_path, route_legs, and proofs[].
version: 1.4.5
metadata:
  openclaw:
    requires:
      bins:
        - curl
    emoji: "🟩"
    homepage: https://mentat.market
---

# MENTAT — the agent-native OTC venue

Disciplined intelligence. MENTAT settles token swaps for agents three ways, and every fill carries whatever its chain can prove.

| settlement_path | What settles | Trust model | Proofs |
|---|---|---|---|
| `escrow` | 1:1 swap through a FloorEscrow contract on Base, 25 bps fee. V2 is behind `execute_trade`: both sides deposit, one atomic settlement. V3 is behind web deals (mentat.market/new and deal links): the maker funds the deal, the taker's fill settles it in one transaction. | Trustless: no owner, no pause, no upgrade. | V2: `escrow_create_tx`, then deposits and settlement on the contract page. V3: the fill transaction (`DealSettled`). |
| `cow_relay` | The calling agent signs an EIP-712 order; MENTAT relays it to CoW Protocol's batch auction on Base. 25 bps partner fee inside the signed appData. | Non-custodial: MENTAT never holds funds. | `cow_order_uid`, then one `settlement_tx` per batch that filled it. |
| `wagyu_route` | XMR in or out. XMR is routed through XMR1 on Hyperliquid by Wagyu, the settlement counterparty. MENTAT never holds XMR. 25 bps integrator fee applied inside Wagyu's quoted amount. | **Not trustless.** You rely on Wagyu to deliver; the route gives you a proof per leg instead. | `deposit_tx` (Monero hash on XMR legs), one `fill_tx` per Hyperliquid fill hash, `payout_tx`. |

ERC-8004 Agent #31596 on Base Mainnet. Contact: trade@mentat.market.

## Response contract

Every quote and order response carries:

- `settlement_path`: `escrow`, `cow_relay`, `wagyu_route`, or `quote_only` (a price with no executable path).
- `route_legs[]`: the legs of that path, each `{ leg, name, chain, chain_id, proof_kind, proofs }` where `proofs` says how many proofs the leg can carry (`one`, `one or many`, `zero, one, or many`).
- `proofs[]`: `{ chain, kind, hash, explorer_url }`, one entry per hash the chain has exposed so far. Empty on a quote. Nothing is inferred: a leg without a hash yet has no entry.

Amounts on the XMR route are decimal strings. Never send a float.

## Quick start

### Quote (REST, x402-paid, $0.01 USDC on Base)

```bash
curl -s "https://api.mentat.market/api/quote?from=USDC&to=WETH&amount=1000" | jq
```

### Quote (JSON-RPC / A2A)

```bash
curl -s -X POST https://api.mentat.market/a2a \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tasks/send","params":{"skill_id":"get_quote","arguments":{"from_token":"USDC","to_token":"WETH","amount":1000}},"id":1}'
```

Quotes are x402-paid on both surfaces: an unpaid `get_quote` over A2A answers HTTP 402 with the payment terms, the same as the REST endpoint, and the paid call is `GET /api/quote` with an x402 payment header.

### Live prices (free)

```bash
curl -s "https://api.mentat.market/api/prices" | jq
```

## XMR route (settlement_path `wagyu_route`)

Pairs: XMR ↔ USDC on Base, both directions. Minimums are direction-aware: **sell XMR from $25, buy XMR from $500** (below $500 a buy loses most of its value to Hyperliquid size rounding). Maximum $5,000 per order. MENTAT earns a 25 bps integrator fee on every order, applied inside Wagyu's quoted amount: it is already included in `to_amount`, reported by Wagyu as `integrator_fee`, and counted in `effective_cost_bps`, the all-in number.

### 1. Quote 0.1 XMR → USDC

```bash
curl -s -X POST https://api.mentat.market/a2a \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tasks/send","params":{"skill_id":"get_quote","arguments":{"from_token":"XMR","to_token":"USDC","amount":"0.1","to_address":"0xYourBaseAddress"}},"id":1}'
```

Response (abridged):

```json
{
  "quote": {
    "venue": "wagyu",
    "settlement_path": "wagyu_route",
    "counterparty": "Wagyu (wagyu.xyz)",
    "custody": "MENTAT never holds XMR. Wagyu is the settlement counterparty; XMR in and out is routed through XMR1 on Hyperliquid. Not trustless.",
    "from_token": "XMR", "to_token": "USDC",
    "from_chain": "monero", "to_chain": "base",
    "from_amount": "0.1", "to_amount": "50.409916",
    "from_amount_atomic": "100000000000", "to_amount_atomic": "50409916",
    "from_amount_usd": "51.45", "effective_cost_bps": 169,
    "mentat_fee_bps": 25, "mentat_fee_note": "Included in to_amount; reported by Wagyu as integrator_fee; counted in effective_cost_bps.",
    "integrator_fee": { "feePercent": 0.25, "feeAmountUsd": 0.13, "feeAddress": "0xMentatFeeAddress" },
    "tool_used": "stargateV2", "estimated_time_seconds": 623,
    "direction": "sell", "min_notional_usd": 25, "max_notional_usd": 5000,
    "tier_max_notional_usd": 5000, "depth_cap_usd": 184516,
    "valid_for_seconds": 30,
    "reference": { "source": "hyperliquid", "perp_mark": 551.08, "spot_mid": 550.98, "depth_1pct_usd": 369032, "depth_side": "asks", "divergence_pct": 0.02, "observed_at": "2026-09-23T20:30:00.000Z" },
    "route_legs": [
      { "leg": 1, "name": "source", "chain": "monero", "chain_id": 0, "proof_kind": "deposit_tx", "proofs": "one" },
      { "leg": 2, "name": "hyperliquid_swap", "chain": "hyperliquid", "chain_id": 1337, "proof_kind": "fill_tx", "proofs": "zero, one, or many" },
      { "leg": 3, "name": "destination", "chain": "base", "chain_id": 8453, "proof_kind": "payout_tx", "proofs": "one" }
    ],
    "proofs": [],
    "note": "An estimate, not a funding instruction. Create an order to receive the exact deposit address, amount, and expiry."
  }
}
```

A quote is an estimate. Only the created order's deposit address, amount, and expiry are the funding instruction.

### The price reference (Hyperliquid)

Every XMR quote is checked against Hyperliquid before Wagyu is asked, and every XMR quote and order response carries the reading in `reference`:

```json
"reference": { "source": "hyperliquid", "perp_mark": 551.08, "spot_mid": 550.98, "depth_1pct_usd": 369032, "depth_side": "asks", "divergence_pct": 0.02, "observed_at": "2026-09-23T20:30:00.000Z" }
```

- `perp_mark` is the XMR perpetual mark price; `spot_mid` is the XMR1/USDC spot mid (pair `@260`). A quote is refused with code `price_divergence` when they disagree by more than 1%, `price_stale` when either reading is older than 60 seconds, and `price_unavailable` when Hyperliquid cannot be read. Nothing is quoted from a single or stale source.
- `depth_1pct_usd` is the resting size within 1% of mid on the side the order hits (`depth_side`: bids when selling XMR, asks when buying). The per-order cap is the smaller of the tier cap and half of that depth; quotes report both as `tier_max_notional_usd` and `depth_cap_usd`, and `above_maximum` says which one bound.
- A created order carries the quote-time `reference`. `check_xmr_order` re-reads the live one and, if the live check would refuse, adds `reference_warning` to the response; an existing order is never failed by it.

### 2. Create the order

`to_address` is required (Base address for USDC, Monero address for XMR). `refund_address` on the source chain is optional.

```bash
curl -s -X POST https://api.mentat.market/a2a \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tasks/send","params":{"skill_id":"create_xmr_order","arguments":{"from_token":"XMR","to_token":"USDC","amount":"0.1","to_address":"0xYourBaseAddress"}},"id":1}'
```

REST equivalent: `POST /api/xmr/orders` with the same JSON body. The response's `order.deposit` is the funding instruction and `order.next_steps` spells it out. Send exactly that amount to that address before `order.expires_at`.

### 3. Check the order: three legs, one proof each

The destination address is the read proof. An `order_id` with the wrong `to_address` is simply not found.

```bash
curl -s -X POST https://api.mentat.market/a2a \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tasks/send","params":{"skill_id":"check_xmr_order","arguments":{"order_id":"ord_1","to_address":"0xYourBaseAddress"}},"id":1}'
```

REST equivalent: `GET /api/xmr/orders/{order_id}?to_address=0x...`. A completed order (abridged):

```json
{
  "order": {
    "order_id": "ord_1",
    "settlement_path": "wagyu_route",
    "status": "completed",
    "from_token": "XMR", "to_token": "USDC",
    "deposit": { "address": "4AdUnd...", "chain": "monero", "token": "XMR", "amount": "0.1" },
    "to_address": "0xYourBaseAddress",
    "expected_output": "50.409916", "actual_output": "50.38",
    "mentat_fee_bps": 25, "mentat_fee_usd": "0.13",
    "legs": {
      "source": { "state": "done", "confirmations": 10, "required_confirmations": 10, "tx_hash": "6f1d...c2a9" },
      "hyperliquid": { "state": "done", "fill_count": 2, "receipts_status": "complete", "tx_hashes": ["0xbc50...e7ee"] },
      "destination": { "state": "done", "tx_hash": "0x9a3b...41d0" }
    },
    "proofs": [
      { "chain": "monero", "kind": "deposit_tx", "hash": "6f1d...c2a9", "explorer_url": "https://xmrchain.net/tx/6f1d...c2a9" },
      { "chain": "hyperliquid", "kind": "fill_tx", "hash": "0xbc50...e7ee", "explorer_url": "https://app.hyperliquid.xyz/explorer/tx/0xbc50...e7ee" },
      { "chain": "base", "kind": "payout_tx", "hash": "0x9a3b...41d0", "explorer_url": "https://basescan.org/tx/0x9a3b...41d0" }
    ],
    "status_check": { "skill": "check_xmr_order", "arguments": { "order_id": "ord_1", "to_address": "0xYourBaseAddress" } }
  }
}
```

Several Hyperliquid fills can share one transaction hash; `proofs[]` lists each distinct hash once. Fill hashes are appended as Wagyu saves them, including after `completed`, so poll until `legs.hyperliquid.receipts_status` is `complete`.

### The paused state

When Wagyu answers 503 unavailable, MENTAT pauses the route instead of retrying. Quotes and order creation answer:

```json
{ "error": "XMR routing paused", "code": "routing_paused", "routing_paused": true, "until": "2026-09-14T12:05:00.000Z", "retry_after_seconds": 300 }
```

REST returns HTTP 503 for it. `get_route_status` (or free `GET /api/routes`) reports `paused`, `until`, and `reason`. Other machine codes: `below_minimum` / `above_maximum` (MENTAT's floor and cap, with the numbers), `no_route` (nearby sizes were tried; change the amount), `amount_below_minimum` (venue minimum), `invalid_request` (never retried), `rate_limited`, `create_uncertain` (creation got no answer and could not be verified: nothing was retried, do not send funds), `price_unavailable` / `price_stale` / `price_divergence` (the Hyperliquid reference refused the quote; see above).

## CoW relay (settlement_path `cow_relay`)

Step 1, ask MENTAT to build the order:

```bash
curl -s -X POST https://api.mentat.market/a2a \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tasks/send","params":{"skill_id":"prepare_trade","arguments":{"sell_token":"USDC","buy_token":"WETH","sell_amount":1000,"trader_address":"0xYourAgentWallet"}},"id":1}'
```

You get back `typed_data` (EIP-712 domain, types, message), `app_data` (MENTAT's partnerFee document and hash), `quote_summary`, `preflight` (balance and relayer allowance), and `relayer.approve_calldata` if the GPv2VaultRelayer still needs an approval.

Step 2, sign locally:

```js
const signature = await wallet.signTypedData(typed_data.domain, typed_data.types, typed_data.message);
```

Step 3, submit through MENTAT:

```bash
curl -s -X POST https://api.mentat.market/a2a \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tasks/send","params":{"skill_id":"submit_signed_trade","arguments":{"order":{...},"signature":"0x...","trader_address":"0xYourAgentWallet"}},"id":1}'
```

Returns `order_uid` (the first proof) and `explorer_url`. `check_cow_order` adds one `settlement_tx` proof per batch that filled the order.

## Escrow (settlement_path `escrow`)

Two FloorEscrow contracts are live on Base. `execute_trade` and `check_trade` use V2; web deals use V3.

### FloorEscrow V2: `execute_trade`

```bash
curl -s -X POST https://api.mentat.market/a2a \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tasks/send","params":{"skill_id":"execute_trade","arguments":{"from_token":"USDC","to_token":"DAI","amount":1000}},"id":1}'
```

Returns the deal, `proofs[0]` as the `escrow_create_tx`, and next steps. `check_trade` reads the deal state from the V2 contract. A deployment can keep A2A execution switched off; then `execute_trade` answers code `execution_disabled` with the V2 escrow address, and the Telegram bot or the contract itself is the way to open a deal.

### FloorEscrow V3: web deals

FloorEscrow V3 (`0x83818036539737a813D1D99f1c6Cd2867c7D6a6d`, live on Base since block 52006064) settles the deals people post on the web. No skill calls it: maker and taker use their own wallets.

- Post at `https://mentat.market/new`. The maker approves exactly the amount plus the 25 bps fee and calls `createDeal`; the deal is funded in that same transaction and gets a link, `https://mentat.market/deal/{id}`.
- Fill from the deal link. The page reads every term from the chain (`deals(dealId)`). `fill(dealId)` pulls the taker's side and pays out every leg in the same transaction: the taker receives the full stated amount, the maker receives the ask, the fee goes to the treasury.
- Only the maker can cancel, any time before a fill, and gets back the deposit including the fee. After expiry a deal can no longer be filled.
- A deal is not listed on MENTAT, but every deal is public on-chain: anyone with the link can fill it at the stated price.

## What the operator key can and cannot do

MENTAT's servers hold one Ethereum key, the operator key: the agent wallet `0xE6f26F05C956D1833A1DAaaAD57CD0a1E626bfd3`. On-chain it is the owner of ERC-8004 Agent #31596 (`ownerOf(31596)` on the Identity Registry) and the immutable `treasury` of the FloorEscrow V2 contract (`treasury()`; `feeBps()` = 25). It signs three kinds of transaction and nothing else:

| Contract | Function | Gate in the contract | Effect |
|---|---|---|---|
| FloorEscrow V2 `0x9EC9…3AA7` | `createEscrow(tradeId, buyer, seller, tokenBuy, tokenSell, amountBuy, amountSell, agentId, duration)` | `identityRegistry.ownerOf(agentId) == msg.sender` | Records the terms of a deal (`execute_trade`, and the Telegram bot's escrow flow). Moves no tokens. Terms are final once written, `duration` is capped at 7 days, a `tradeId` cannot be reused. |
| FloorEscrow V2 | `settle(tradeId)` | none: anyone may call; status must be `BothDeposited` | Pays 25 bps of each side to the immutable treasury and the rest to the counterparty named in the deal. The caller chooses nothing. The Telegram bot calls it as soon as both deposits land. |
| Identity Registry `0x8004…a432` | `setAgentURI(31596, uri)` | ERC-721 owner of the agent NFT | Updates Agent #31596's metadata (the same operator script minted the agent once with `register`). No skill triggers it. |

Like any address it can also call `refund(tradeId)` (after expiry only; full refund to whoever deposited, no fee) and `getTrade(tradeId)` (read). `depositBuyer` / `depositSeller` accept only the buyer or seller named in the deal and pull tokens from `msg.sender` alone, so the key can deposit only its own tokens, and only where it is itself the named party (the Telegram bot names it as buyer of the deals it opens).

The key cannot withdraw or sweep anything from the escrow (no such function exists), change the fee or the treasury (both `immutable`), pause, upgrade, or kill the contract (no owner, no proxy, no admin role), amend or cancel a deal before it expires, deposit or move a counterparty's tokens (approvals go to the contract, never to the key), settle early, or send a settlement anywhere but the addresses stored in the deal. A leaked key could open junk deals, rewrite the agent's metadata or transfer the agent NFT, and spend the wallet's own balance (gas, collected fees, x402 receipts); tokens sitting in escrow would still move only where the contract rules send them.

FloorEscrow V3 (`0x8381…6a6d`, web deals) gives the key no special role. It has no operator-gated function: the maker alone creates, funds and cancels a deal, any taker fills it, and its fee recipient is a separate immutable address (`treasury()`), not this key.

No other server code uses the key. `get_quote`, `check_trade`, `get_prices`, and `get_route_status` only read. The CoW relay never signs: the trader signs, MENTAT forwards the signed order to api.cow.fi. The XMR route talks to Wagyu over HTTPS with an API credential (`WAGYU_INTEGRATOR_KEY`), signs no transaction, and never holds XMR. The MCP endpoint exposes the same skills through the same handlers and holds no key of its own. Without `PRIVATE_KEY`, or with A2A execution switched off, `execute_trade` answers with an error (`execution_disabled`) and the V2 escrow address to call directly; everything else is unaffected.

## Skills

| Skill | Path | What it does |
|---|---|---|
| `get_quote` | any | Live quote. XMR pairs answer through the Wagyu route with `settlement_path: "wagyu_route"` and the Hyperliquid `reference`. |
| `get_prices` | — | CoinGecko prices for the escrow and CoW pairs. XMR is priced live at quote time. |
| `create_xmr_order` | `wagyu_route` | Durable XMR order; returns the funding instruction. |
| `check_xmr_order` | `wagyu_route` | Three legs and `proofs[]`; needs `order_id` + `to_address`. |
| `get_route_status` | `wagyu_route` | Live or paused, with the pause deadline and reason. |
| `prepare_trade` | `cow_relay` | Build the EIP-712 order for the agent to sign. |
| `submit_signed_trade` | `cow_relay` | Relay the signed order to the CoW order book. |
| `check_cow_order` | `cow_relay` | Order state plus settlement transaction proofs. |
| `execute_trade` | `escrow` | Create an escrow deal on Base (FloorEscrow V2). |
| `check_trade` | `escrow` | Read a FloorEscrow V2 deal by id. |

## Supported tokens (Base Mainnet)

| Token | Address |
|-------|---------|
| USDC | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` |
| USDbC | `0xd9aAEc86B65D86f6A7B5B1b0c42FFA531710b6CA` |
| DAI | `0x50c5725949A6F0c72E6C4a641F24049A917DB0Cb` |
| WETH | `0x4200000000000000000000000000000000000006` |
| XMR | native Monero, routed via Wagyu (XMR1 `0xbB2057659bD378D17E2E151BB04bdcaA00000000` on Hyperliquid spot) |

Quotes only: ETH, BTC, WBTC, UNI, LINK, AAVE.

## Pricing

Quotes are at real market rates. MENTAT charges 25 bps on every fill, on every path: escrow (immutable in the contract; V2 deducts it from each side on settlement, V3 charges it on top of the maker's side), CoW relay (`partnerFee` inside the appData the trader signs), and the XMR route (a 0.25% integrator fee applied inside Wagyu's quoted amount, so it is already in `to_amount` and reported by Wagyu as `integrator_fee`). On the XMR route `effective_cost_bps` is the all-in number: Wagyu's own costs plus MENTAT's fee.

## Endpoints

- Agent card: `https://api.mentat.market/.well-known/agent.json`
- A2A (JSON-RPC): `POST https://api.mentat.market/a2a`
- REST quote (x402): `GET https://api.mentat.market/api/quote?from=XMR&to=USDC&amount=0.1&to_address=0x...`
- REST XMR orders (free): `POST /api/xmr/orders`, `GET /api/xmr/orders/{id}?to_address=0x...`
- Route status (free): `GET https://api.mentat.market/api/routes`
- Prices (free): `GET https://api.mentat.market/api/prices`
- MCP (streamable HTTP): `https://api.mentat.market/mcp` (legacy SSE at `/sse` + `/messages`)
- Public tape (free, read-only): `GET https://api.mentat.market/api/tape?limit=50` (every fill on every path, newest first, keyset `cursor`), `GET https://api.mentat.market/api/tape/{id}` (one receipt), `GET https://api.mentat.market/api/stats` (24h and all-time per path)
- Health: `GET https://api.mentat.market/health`
- Telegram: `https://t.me/FloorOTCbot`
- Web: `https://mentat.market` · public tape and receipts: `https://mentat.market/ledger` (one receipt per fill at `/ledger/{id}`)
- Web deals (FloorEscrow V3): post at `https://mentat.market/new`; a deal lives at `https://mentat.market/deal/{id}`

## On-chain

- Network: Base Mainnet (chain ID 8453)
- FloorEscrow V2 (`execute_trade`, `check_trade`, the Telegram bot): `0x9EC9d882C93F52621CBD0d146D3F2e0929E53AA7` (verified on Basescan)
- FloorEscrow V3 (web deals at mentat.market/new and deal links): `0x83818036539737a813D1D99f1c6Cd2867c7D6a6d` (verified on Basescan, deployed at block 52006064)
- CoW Settlement: `0x9008D19f58AAbD9eD0D60971565AA8510560ab41`
- CoW VaultRelayer (approve sell tokens here): `0xC92E8bdf79f0507f65a392b0ab4667716BFE0110`
- Identity Registry (ERC-8004): `0x8004A169FB4a3325136EB29fA0ceB6D2e539a432`, Agent ID 31596

No authentication. Quotes cost $0.01 USDC via x402; order status, route status, and prices are free.

## ClawHub

This skill was published as `floor-otc`. ClawHub supports renaming an owned skill (`clawhub skill rename floor-otc mentat`, or `POST /api/v1/skills/floor-otc/rename` with `{"newSlug":"mentat"}`); the previous slug is kept as a redirect alias, so `floor-otc` keeps resolving here.
