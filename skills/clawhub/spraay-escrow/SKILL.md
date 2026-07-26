---
name: spraay-escrow
description: >-
  Safe agent-to-agent commerce via Spraay x402 escrow. Create, fund, monitor,
  release, or cancel on-chain escrows — pay on verified delivery instead of
  paying blind. Use when the user asks to escrow a payment, pay on delivery,
  hold funds until a task is verified, make a milestone payment, protect an
  agent-to-agent transaction, hire another agent safely, or release or cancel
  escrowed funds.
version: 1.0.0
homepage: https://spraay.app
metadata:
  openclaw:
    emoji: "💧"
    requires:
      bins:
        - curl
        - jq
      env:
        - SPRAAY_GATEWAY_URL
    primaryEnv: SPRAAY_GATEWAY_URL
    envVars:
      - name: SPRAAY_GATEWAY_URL
        required: true
        description: >-
          Spraay x402 gateway base URL (https://gateway.spraay.app).
          All API calls go exclusively to this endpoint.
---

# Spraay Escrow 💧

Escrowed payments for agent-to-agent commerce via the Spraay x402 gateway.
Create → fund → verify → release. Never pay an unknown agent blind.

All requests in this skill go exclusively to the user's configured
`SPRAAY_GATEWAY_URL`. No data is sent to any other external endpoint.

## Important Warnings

**Escrowed funds are real funds.** Funding an escrow locks real USDC
on-chain. Releasing an escrow transfers it irreversibly to the recipient.
Always confirm the following with the user before creating, funding,
releasing, or cancelling an escrow:

- Counterparty address is correct
- Amount and release conditions are intended and understood by both sides
- The user understands x402 micropayment fees are charged per API call

**Release is final.** Once escrowed funds are released, the transfer cannot
be undone. Do not release an escrow without explicit user confirmation that
the work or delivery has been verified.

## Setup

The gateway URL must be set in your environment or `openclaw.json`:

```
SPRAAY_GATEWAY_URL=https://gateway.spraay.app
```

No API key is needed. Payments are made per-request via the x402 HTTP payment
protocol (HTTP 402 → pay → retry). An x402-compatible wallet (Coinbase CDP
or similar) handles this automatically.

## When to Use Escrow vs. Direct Payment

Use escrow when:

- Paying an agent or party you have not transacted with before
- Payment depends on delivery of work, data, or a completed task
- The amount is large enough that a failed delivery would matter

Use direct batch payment (see the `spraay-payments` skill) when the
counterparty is trusted and no delivery condition applies.

## Escrow Lifecycle

An escrow moves through two steps before funds are locked:

1. **Create** — establishes the on-chain agreement between two parties
   (no funds locked yet).
2. **Fund** — deposits USDC into the escrow, locking it.
3. Then either **Release** (funds go to recipient) or **Cancel** (funds
   return to depositor; before funding, or by mutual agreement).

## Workflows

### 1. Create an Escrow — $0.10

Establishes the agreement. Funds are NOT locked until the fund step.

**Always confirm counterparty, amount, and release terms with the user
before creating.**

```bash
curl -X POST "$SPRAAY_GATEWAY_URL/api/v1/escrow/create" \
  -H "Content-Type: application/json" \
  -d '{
    "recipient": "0xABC...123",
    "amount": "100",
    "token": "USDC",
    "chain": "base",
    "conditions": "Dataset delivered and verified"
  }'
```

If you receive HTTP 402, the response body contains payment instructions. Pay
the facilitator, then retry with the `X-PAYMENT` header containing the proof.

The response includes an escrow ID. Save it — it is required for every
subsequent call.

### 2. Fund the Escrow — $0.02

Deposits USDC into the escrow, locking funds pending conditions. Required
after create and before release.

```bash
curl -X POST "$SPRAAY_GATEWAY_URL/api/v1/escrow/fund" \
  -H "Content-Type: application/json" \
  -d '{"id": "ESCROW_ID"}'
```

### 3. Check Escrow Status — $0.001

Fetch a single escrow with locked amount, parties, status, and release
conditions. Use before release/cancel to confirm state.

```bash
curl "$SPRAAY_GATEWAY_URL/api/v1/escrow/ESCROW_ID"
```

### 4a. Release Funds — $0.08

Transfers escrowed funds to the recipient. **Final and irreversible.**

**Always confirm with the user that delivery has been verified before
releasing.**

```bash
curl -X POST "$SPRAAY_GATEWAY_URL/api/v1/escrow/release" \
  -H "Content-Type: application/json" \
  -d '{"id": "ESCROW_ID"}'
```

### 4b. Cancel an Escrow — $0.02

Cancels before funding, or by mutual agreement afterward — locked funds
return to the depositor. Use for failed delivery, expired milestones, or
abandoned agreements.

```bash
curl -X POST "$SPRAAY_GATEWAY_URL/api/v1/escrow/cancel" \
  -H "Content-Type: application/json" \
  -d '{"id": "ESCROW_ID"}'
```

### List Your Escrows — $0.02

Active and historical escrows for a wallet, with status, locked amounts,
counterparties, and release conditions.

```bash
curl "$SPRAAY_GATEWAY_URL/api/v1/escrow/list?address=0xYOUR...ADDR"
```

### Recommended Flow for Hiring an Unknown Agent

1. (Optional) Screen the counterparty first — free address safety check and
   paid trust score via the `spraay-trust` skill.
2. Create the escrow and share the escrow ID with the counterparty.
3. Fund it. The counterparty confirms funding via escrow status, then
   performs the work.
4. Verify the delivery with the user.
5. Release on confirmation — or cancel if delivery failed.

## Free Endpoints

These gateway endpoints require no x402 payment and are useful alongside
escrow:

- `GET /api/v1/address/safety?address=0x...` — Screen a counterparty for
  phishing, sanctions, exploits, and mixer usage before escrowing
- `GET /free/prices` — Spot prices (show USD value before escrowing)
- `GET /free/resolve?name=alice.eth` — ENS/Basename resolution
- `GET /health` — Gateway health check

## x402 Payment Flow

1. Call any paid endpoint.
2. Receive HTTP 402 with payment details (`accepts` array with amount,
   asset, and payment address).
3. Agent wallet sends the micropayment.
4. Retry the request with the `X-PAYMENT` proof header.
5. Receive the response.

Escrow endpoint costs: create $0.10, fund $0.02, status $0.001,
release $0.08, cancel $0.02, list $0.02 — all in USDC on Base.

## Error Handling

- `402` — Payment required. Follow instructions in response body.
- `400` — Bad request. Check parameters.
- `404` — Escrow ID not found. Verify the ID.
- `500` — Server error. Retry after a moment.

## Tips

- Always confirm with the user before creating, funding, releasing, or
  cancelling.
- Create and fund are separate steps — an unfunded escrow locks nothing.
- Check escrow status before release or cancel to confirm state.
- Screen counterparties with the free address safety endpoint first.
- Pair with `spraay-trust` for a full due-diligence flow before escrowing.

## Links

- App: https://spraay.app
- Docs: https://docs.spraay.app
- GitHub: https://github.com/plagtech
