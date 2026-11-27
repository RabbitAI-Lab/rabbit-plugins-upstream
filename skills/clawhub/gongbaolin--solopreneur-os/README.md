# Solopreneur OS · Commercial Monetization Engine

**Turn raw professional expertise into a scalable one-person business—on demand.**

Built by **Solopreneur Lab** (`solopreneurlab.app`), Solopreneur OS is a pay-per-use AI Agent Skill designed for solo founders, independent consultants, and domain experts. No subscriptions, no fluff, zero AI slop.

---

## What It Delivers

| Module (`sku`) | Price | Deliverables |
| :--- | :---: | :--- |
| **`complete`** | **$0.39 USDT** | End-to-end 3-part commercial blueprint (Positioning + Content + High-Ticket Offer) |
| **`origin`** | **$0.19 USDT** | Sharp 1-sentence positioning, named proprietary framework, MVP & 7-day validation checklist |
| **`content`** | **$0.19 USDT** | 3 high-converting X/LinkedIn posts, 3 punchy short takes, and a zero-pitch DM lead funnel |
| **`leverage`** | **$0.19 USDT** | Outcome-based ROI math, 3-tier anchored pricing table, safe risk-reversal & outreach scripts |

---

## Quick Start

### 1. For AI Agents (OpenClaw / Claude / Custom Agents)
Point your agent to [`SKILL.md`](./SKILL.md) or install this repository directly in your agent's skill directory.

### 2. Direct API Call
```bash
curl -X POST https://api.solopreneurlab.app \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "your_unique_id",
    "sku": "complete",
    "mode": "auto",
    "user_input": "I am a senior B2B SaaS product manager with 8 years of experience looking to launch a solo advisory practice."
  }'
```

### Billing & Settlement
* Powered by **SkillPay.me** on **BNB Chain (USDT)**.
* If your balance is insufficient, the API returns `HTTP 402` with an instant top-up `payment_url`. Top up once and retry—unused balance stays in your account for future calls.

---

## License
MIT License · © 2026 Solopreneur Lab