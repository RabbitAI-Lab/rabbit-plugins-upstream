---
name: sentinel-transaction-safety
version: "1.0.0"
description: Pre-execution transaction safety oracle for autonomous AI agents. Before signing an on-chain transaction, an agent calls SENTINEL and receives a SAFE / UNSAFE / UNKNOWN verdict, a standardized SENTINEL Score (0-100, grade AAA-D), and an ed25519-signed receipt. Checks contract security (GoPlus), execution simulation (Alchemy eth_call), honeypot detection (honeypot.is), and LP concentration/rug risk. Pay-per-call via x402 ($0.005 USDC on Base) — no accounts, no API keys, no SDK required. No free trial.
license: MIT
compatibility: Requires internet access to reach the SENTINEL API. No local dependencies. Compatible with any agent that can make HTTP POST requests and hold a Base-compatible wallet capable of signing an EIP-3009 USDC authorization. There is no no-wallet preview endpoint.
metadata:
  author: teodorofodocrispin-cmyk
  version: "1.0.0"
  endpoint: https://sentinel-agent.dev/v1/guard
  health: https://sentinel-agent.dev/health
  pricing: https://sentinel-agent.dev/pricing
  payment: Base USDC via x402 ($0.005 per call, EIP-3009, facilitator-free local verification)
  trial: none — every call requires a valid x402 payment
  requires_env: none
  wallet_security: >
    SENTINEL NEVER requires wallet private keys, seed phrases, or signing credentials.
    The agent signs an EIP-3009 TransferWithAuthorization with its own wallet, entirely
    client-side, and only submits the resulting signed authorization as the X-PAYMENT
    header. SENTINEL verifies that signature locally (facilitator-free) and never
    receives or stores a private key.
  infrastructure: FastAPI + Supabase + Render (AWS)
  data_sources:
    - GoPlus token security API (contract risks, honeypot flags, ownership, taxes)
    - Alchemy eth_call (transaction simulation)
    - honeypot.is (independent sell-simulation cross-check)
    - LP concentration / known-locker detection (UNCX Base)
  features:
    - pre_execution_safety_verdict (SAFE / UNSAFE / UNKNOWN)
    - sentinel_score (0-100, graded AAA-D)
    - signed_receipt (ed25519, independently verifiable)
    - lp_concentration_check (rug-by-liquidity-removal detection)
  mcp_server: https://sentinel-agent.dev/mcp
  homepage: https://github.com/teodorofodocrispin-cmyk/sentinel-public
---

> ⚠️ **Data Handling Notice:** SENTINEL sends the unsigned transaction payload (chain, sender, tx data) to a remote API (`sentinel-agent.dev`) for evaluation. The payload is processed to produce a verdict and is not required to be a signed or broadcastable transaction. Review the transparency notice below before sending any transaction containing sensitive calldata.

# SENTINEL — Agent Transaction Safety Oracle v1.0.0

A pre-execution safety oracle for autonomous AI agents. Before an agent signs a blockchain transaction, it calls SENTINEL and gets back a **SAFE / UNSAFE / UNKNOWN** verdict, a standardized **SENTINEL Score (0–100, grade AAA–D)**, and a signed receipt — all before a single unit of value moves. Pure M2M, pay-per-call via x402, no accounts.

Running on FastAPI + Supabase + Render — the same production stack as the rest of this M2M model family (VeraData, Intelica, TrustBoost).

---

## ⚠️ Transparency Notice (Read Before Installing)

### 1. Data Transmission

The transaction payload you send (`chain`, `from`, `tx`) is transmitted to Render (AWS) infrastructure for processing via FastAPI.

**What SENTINEL evaluates:** contract security (GoPlus), execution simulation (Alchemy `eth_call`), honeypot cross-check (honeypot.is), and LP concentration. The evaluation is produced by rule-based checks plus an LLM council (Claude Haiku + GPT-4o-mini) server-side.

**What SENTINEL stores:** verdict, payer address, chain, and price paid, logged to Supabase for usage tracking. It does not require or store your wallet's private key at any point.

**For strict no-transmission requirements** (air-gapped systems, or transactions containing sensitive calldata that must never leave the local machine): this service is not suitable.

### 2. Payment Model and Autonomous Safety

SENTINEL uses **x402 with local EIP-3009 verification** — no facilitator dependency for verification, no human confirmation needed.

**How autonomous payment works safely:**

1. Agent calls `POST /v1/guard` without payment → receives HTTP 402 with `accepts` (network `base`, price $0.005 USDC, `payTo` published in the response).
2. Agent signs an EIP-3009 `TransferWithAuthorization` for the exact amount, using its own wallet's private key — **that signature never leaves the agent's own environment**.
3. Agent retries the request with the signed authorization in the `X-PAYMENT` header.
4. SENTINEL recovers the signer locally (`eth_account.recover_message`) and verifies it against the expected wallet — no third-party facilitator call required to validate the payment.
5. Verdict + signed receipt are returned only after verification succeeds.

**Why this is safe for autonomous agents:**

- The agent's private key never touches SENTINEL infrastructure — only the resulting signed authorization does.
- Verification is local and deterministic (cryptographic signature recovery), not an opaque third-party call.
- SENTINEL cannot initiate a charge — the agent must construct and sign the authorization itself.

**No trial mode.** Unlike other services in this model family, SENTINEL has no free preview endpoint today. Every call to `/v1/guard` requires a valid payment; there is no `tx_hash=TRIAL` equivalent. Budget for $0.005 USDC per pre-execution check.

### 3. Audit Trail

Every call is logged to Supabase (`sentinel_usage`) with: verdict, payer address, chain, and price — never the full calldata beyond what was needed for evaluation.

### 4. Operator Verification

- **GitHub:** https://github.com/teodorofodocrispin-cmyk
- **Repository:** https://github.com/teodorofodocrispin-cmyk/sentinel-public
- **Health endpoint:** https://sentinel-agent.dev/health
- **Pricing:** https://sentinel-agent.dev/pricing

---

## When to use this skill

Activate this skill when:
- An agent is about to sign an on-chain transaction on Base and wants a pre-flight safety check (rug pull, honeypot, malicious contract, infinite approval).
- The agent needs a signed, independently verifiable SAFE/UNSAFE/UNKNOWN verdict before spending funds.
- The agent's wallet has budget for per-call payment ($0.005 USDC) — there is no free fallback.

## When NOT to use this skill

- Strict zero-transmission environments (air-gapped, on-premise) — the transaction payload leaves the local machine.
- Any agent without an x402-capable wallet able to sign EIP-3009 authorizations on Base. There is no no-wallet preview to fall back to.
- Transactions containing calldata that must never be transmitted to a third party.

---

## How it works

1. Agent `POST`s `{chain, from, tx}` to `sentinel-agent.dev/v1/guard`.
2. SENTINEL runs contract security (GoPlus), simulation (Alchemy `eth_call`), honeypot cross-check (honeypot.is), and LP concentration analysis.
3. An LLM council (Claude Haiku + GPT-4o-mini) reviews the aggregated signals.
4. SENTINEL returns a JSON verdict (`SAFE` / `UNSAFE` / `UNKNOWN`), a 0–100 risk score with AAA–D grade, the contributing risk signals, and an ed25519-signed receipt.

---

## Try it — check pricing and health first (free, no wallet needed)

```bash
curl https://sentinel-agent.dev/health
curl https://sentinel-agent.dev/pricing
```

These two endpoints are free and require no payment. `POST /v1/guard` itself always requires payment — there is no free equivalent.

---

## API Request

**Endpoint:** `POST https://sentinel-agent.dev/v1/guard`
**Headers:** `Content-Type: application/json`, `X-PAYMENT: <x402 signed authorization>`

```json
{
  "chain": "base",
  "from": "0xYourAgentWallet",
  "tx": { "to": "0xTargetContract", "data": "0x...", "value": "0x0" }
}
```

## API Response (no payment, 402)

```json
{
  "x402Version": 2,
  "accepts": [
    { "network": "base", "amount": "5000", "payTo": "0xCf1d31020A7915421f6d66B9835Dcb6f422337E7" }
  ]
}
```

## API Response (success, 200)

```json
{
  "verdict": "SAFE",
  "sentinelScore": 94,
  "grade": "AAA",
  "contract": { "risks": [] },
  "lpConcentration": "locked",
  "signature": "ed25519:...",
  "signer": "sentinel-agent.dev"
}
```

## SENTINEL Score grading

| Grade | Score range | Meaning |
|-------|-------------|---------|
| AAA | 90-100 | No material risk signals detected |
| AA/A | 70-89 | Minor advisory signals, no hard risks |
| BBB/BB/B | 40-69 | Moderate risk signals present |
| CCC/CC/C | 15-39 | Significant risk signals |
| D | 0-14 | Hard risk detected (honeypot, extreme LP concentration, simulation failure) |

---

## Known Limitations

- **No free trial or no-wallet preview endpoint exists today.** Every `/v1/guard` call requires payment.
- Verdicts reflect the checks currently implemented (GoPlus contract security, Alchemy simulation, honeypot.is, LP concentration); they are not a guarantee against novel or unseen attack patterns.
- `KNOWN_LOCKERS` (used for LP-lock detection) currently covers UNCX on Base; liquidity locked in unlisted lockers may be scored as `moderate` (advisory) instead of `locked` (clean).
- **No certified audit:** the SENTINEL Score is produced by rule-based checks plus an LLM council, not by a certified security firm.
- Paid endpoint verification is local/facilitator-free for `/verify`; on-chain settlement of the payment itself still depends on a settler submitting the authorization (self-settle or facilitator).

## Resources

- GitHub: https://github.com/teodorofodocrispin-cmyk/sentinel-public
- Health check: https://sentinel-agent.dev/health
- Pricing: https://sentinel-agent.dev/pricing
- Agent card (A2A): https://sentinel-agent.dev/.well-known/agent.json
- Docs (LLM-readable): https://sentinel-agent.dev/llms.txt
- MCP server: https://sentinel-agent.dev/mcp
- Infrastructure: FastAPI + Supabase + Render (AWS)
