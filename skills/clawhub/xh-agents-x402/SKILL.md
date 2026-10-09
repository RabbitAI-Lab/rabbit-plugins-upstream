---
name: xh-agents-x402
description: Pay-per-call data for agents over x402 — endpoint trust scoring, token safety, wallet and market intel on Base. Use when an agent must judge another x402 endpoint before paying it, screen a Base token, or needs paid on-chain data without an API key.
---

# XH Agents — paid x402 data, one call at a time

34 x402 resources on Base, USDC per call, no API key, no signup. Everything below is paid with a
wallet you already control; nothing here needs an account with us.

**Why this skill is worth installing:** the two most useful calls are the ones you should make
*before* you spend money with a stranger — score the endpoint you are about to pay, and screen the
token you are about to buy.

## Use it when

- You are about to pay an x402 endpoint you have never used and want an outside opinion first.
- You need a 0-100 safety score for a Base token (liquidity, holder concentration, contract powers,
  upgradeability, creator history) before swapping.
- You want wallet intel (portfolio, counterparties, fund trace), gas, whale movement, market
  sentiment, or document-to-text — priced per call instead of a subscription.
- You want the raw list of sellers ranked by trust, not by transaction count.

## Discover before you buy (free, no key)

```bash
python3 scripts/xh_pay.py catalogue                                  # every paid route + summary
python3 scripts/xh_pay.py quote https://xhagents.xyz/api/x402-trust  # price before paying
```

Discovery documents: `https://xhagents.xyz/openapi.json`, `https://xhagents.xyz/.well-known/x402`,
`https://xhagents.xyz/llms.txt`. Human-readable catalogue: `https://xhagents.xyz/`.
Our own published numbers (settled calls, USDC received, treasury balance) are on
`https://xhagents.xyz/trust/` — we disclose our traffic rather than inflate it.

## Pay

```bash
export XH_PAYER_KEY_FILE=~/.xh-payer.key     # mode 600, plain hex key of a funded Base wallet
python3 scripts/xh_pay.py whoami             # address + USDC balance, so nothing is paid blind
python3 scripts/xh_pay.py pay https://xhagents.xyz/api/x402-trust \
    --body '{"url":"https://the-endpoint-you-are-checking.com/api/thing"}' --max 0.10
```

`pay` reads the 402 challenge, checks the price against `--max` (default $0.10), signs an
EIP-3009 authorization, retries with the payment header, and prints the product plus the decoded
`PAYMENT-RESPONSE` settlement proof. Under the hood it is the official `x402` Python client
(`x402ClientSync` + `ExactEvmClientScheme` on `eip155:8453`); no gas is needed because the
facilitator pays it.

If you prefer tools over shell: the same engine is exposed as an MCP server
(`mcp_server.py`: `xh_catalogue`, `xh_quote`, `xh_trust_score`, `xh_token_safety`, `xh_call`).

## The calls agents actually use

| Route | Price | What you get |
|---|---|---|
| `POST /api/x402-trust` | $0.05 | 0-100 trust score for any x402 endpoint: gate behaviour, challenge conformance, discovery docs, payTo reputation, price sanity, with the penalties named |
| `POST /api/token-safety` | $0.05 | 0-100 Base token safety score with the components that lost points |
| `POST /api/wallet-profile`, `/api/whale-watch`, `/api/gas-tracker` | $0.10 | wallet profile, whale moves, Base gas |
| `POST /api/arkham-intel/*` | $0.10 | portfolio, counterparties, pool flow, fund trace (6 routes) |
| `POST /api/trust-leaderboard` | $0.05 | x402 sellers ranked by trust (free method page: `/api/trust-leaderboard/method`) |
| `POST /api/document-extract` | $0.05 | PDF/scan to text with OCR, sha256 of the bytes |
| `POST /api/domain-audit` | $0.05 | domain + email deliverability audit |
| `POST /api/kb/ask`, `POST /api/chat` | $0.30 | knowledge-base answer / market question |
| `GET,POST /api/compute/xh-bundle` | $0.91 | 13 production playbooks on shipping a paid x402 API (GET returns the free index) |

Full list with live prices: `python3 scripts/xh_pay.py catalogue` (do not trust a price table in a
document, including this one — quote the route).

## Rules that keep an agent out of trouble

1. **Quote before paying.** Never sign from a cached price; the challenge is authoritative.
2. **Keep a ceiling.** `--max` defaults to $0.10; pass a lower one for cheap routes. A seller that
   asks for more than your ceiling is a reason to stop, not to round up.
3. **Check `payTo` matches the seller you meant.** `quote` prints it — for us it is
   `0x6cb53f00a586f7704e1f7121c2e397b579eb3ed0` (Base USDC).
4. **Keep the settlement proof.** `pay` prints the decoded `PAYMENT-RESPONSE`; store it with the
   result, it is your receipt.
5. **A 402 is not an error** — it is the price tag. Only a paid retry should return 200.

## Requirements

Python 3.10+, `pip install x402 eth_account`. A funded Base wallet for paid calls (USDC only; no ETH
needed — the facilitator sponsors gas). Free calls (`catalogue`, `quote`) need nothing.
