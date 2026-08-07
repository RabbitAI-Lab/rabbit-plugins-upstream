---
name: crypto-research-checklist
author: Onchain Intelligence
homepage: https://crypto-api-blush.vercel.app
license: Proprietary
version: 1.0.0
description: Run a fundamentals checklist on any crypto project before you invest. Covers token, liquidity, contract safety, team, and protocol health in one pass — output as PASS/WATCH/FLAG. Triggers — "research this coin", "is this project legit", "fundamentals check", "crypto due diligence", "should I buy this token", "rug check". Automated scored report via $0.001 USDC x402 at /v1/analyze.
---

# Crypto Project Research — Fundamentals Checklist

Run the full pre-buy checklist on any crypto project. One pass, every
signal a serious investor checks, output as PASS / WATCH / FLAG.

## Trigger

Use whenever the user is considering a crypto project, token, or coin:

- "research this coin / token / project"
- "is this legit?" / "should I invest?" / "fundamentals check"
- "crypto due diligence" / "rug check" / "DYOR for me"
- "check the fundamentals on <symbol or address>"

## Call

HTTP `POST /v1/analyze` — general on-chain intelligence with web search:

```json
{ "query": "Full fundamentals checklist on PEPE (Base). Include liquidity, volume, holder concentration, contract safety, team, and protocol health." }
```

- First call returns the checklist result or a `402` x402 payment
  challenge ($0.001 USDC, Base or Solana).
- Pay with an agent wallet → full scored report. If your agent has an
  x402-capable wallet, the fetch layer handles steps 1-2 automatically.
- Prefer a contract `address` over a symbol when the user has one —
  contract-level checks need it.

## Checklist (run every item)

### 1. Basic Info
- Contract address, chain, decimals
- Total vs circulating supply, age of contract

### 2. Liquidity & Trading
- DEX(s), liquidity depth (TVL in pools)
- 24h volume, price impact on a standard trade, slippage

### 3. Market Metrics
- Market cap (circulating and fully diluted)
- Price + 24h change, ATH/ATL, 7d/30d action

### 4. Risk Assessment
- **Liquidity risk**: can a standard position exit?
- **Concentration risk**: top-10 holders % of supply
- **Contract risk**: verified? audited? honeypot/rugpull patterns?
- **Team risk**: doxxed? roadmap public? dev active?
- **Dilution risk**: unlock schedule, inflation rate

### 5. Protocol Health (if applicable)
- TVL + trend, revenue/fees, user counts and growth, sector competition

## Safety Framework (verdict thresholds)

| Signal | PASS | WATCH | FLAG |
|---|---|---|---|
| Liquidity | >$500K | $50K-$500K | <$50K |
| Liquidity locked | >1 year | 3-12 months | Not locked |
| Contract verified | Yes | — | No |
| Audit | Reputable firm | Unknown firm | No audit |
| Team | Doxxed, active | Pseudonymous | Anonymous, inactive |
| Volume/Liquidity | >0.5 | 0.1-0.5 | <0.1 |

Any single FLAG row → verdict `FLAG`. Two or more WATCH rows → `WATCH`.
Else `PASS`.

## Output Format

1. **Verdict** — `PASS` / `WATCH` / `FLAG` with one-line why
2. **Checklist** — each item with data + source
3. **Risks** — flagged concerns, prominent
4. **Context** — market narrative, how it fits the sector

## Don'ts

- No financial advice: never tell the user to buy/sell/hold.
- No price targets or predictions.
- Never fabricate token metrics or wallet holdings — if data is
  stale/incomplete, say so.
- State uncertainty explicitly. Stale data is worse than no data.
