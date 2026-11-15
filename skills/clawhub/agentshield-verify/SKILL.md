---
name: agentshield-verify
description: "Verify before you act: pay-per-call checks for bank transfers, invoices, business-day deadlines, public holidays and stablecoin transfers via agentshield.live (x402, USDC on Base). Use before money moves, an invoice is sent or paid, or a date is promised."
---

# agentshield.live: verify before you act

Deterministic checks that return `ok` and a `failed` list. Paid per call in USDC on Base with the caller's own key. No account. Unknown input returns 404 and is not charged.

## When to use

- Before a bank transfer: `GET https://agentshield.live/transfer?iban=...&bic=...&amount=...&currency=EUR`
- Before sending or paying an invoice: `/invoice?net=&vat=&gross=&country=` (optional `registry=1` asks EU VIES)
- Before promising a date: `/deadline?date=YYYY-MM-DD&days=N&country=DE&region=BY`
- Public holidays of a year: `/holidays?country=DE&year=2026&region=BY`
- Before sending USDC/USDT: `/cryptopay?to=0x...&chain=base&token=USDC`

Do not pay for simple arithmetic (leap year, gcd, factorial, weekday). Ask the free `choose_route` MCP tool first when unsure: `https://agentshield.live/mcp` returns `pay`, `compute` or `skip`.

## How to call

1. Request the URL. It answers HTTP 402 with the exact price in the `PAYMENT-REQUIRED` header.
2. Pay with your own x402 client and key (never share the key). Kit with a per-call cap `maxUsdc`: https://github.com/bartelmost/agentshield-agent-kit
3. Repeat the request. Read `ok` and `failed`; fix the failed fields before you proceed.

All routes and live prices: https://agentshield.live/llms.txt. Not a firewall, not a security audit, not a certificate. Answers are stored and deterministic, not live market data.
