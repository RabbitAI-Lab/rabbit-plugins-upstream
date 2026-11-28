---
name: solopreneur-os
description: A commercial monetization engine for solo founders and independent consultants. Transforms raw expertise into 0-to-1 niche positioning, zero-AI-slop organic content pipelines, and outcome-based high-ticket offers. Pay-per-use via BNB Chain USDT ($0.19 - $0.39).
version: 1.0.1
author: Solopreneur Lab
homepage: https://solopreneurlab.app
api_endpoint: https://api.solopreneurlab.app
pricing:
  currency: USDT (BNB Chain)
  complete: 0.39
  origin: 0.19
  content: 0.19
  leverage: 0.19
---

# Solopreneur OS Skill

Use this skill when the user wants to monetize their professional expertise as a one-person business, build an organic inbound content system (X / LinkedIn / Threads), or package their skills into high-ticket consulting/productized offers.

## Available SKUs (`sku` parameter)

| SKU | Price (USDT) | Best For |
| :--- | :--- | :--- |
| `complete` | **$0.39** | Full 3-part commercial blueprint (Origin + Content + High-Ticket Leverage) |
| `origin` | **$0.19** | 0-to-1 niche positioning, proprietary framework, MVP & 7-day validation plan |
| `content` | **$0.19** | 3 high-converting X/LinkedIn posts, 3 short takes, and a zero-pitch DM funnel |
| `leverage` | **$0.19** | Outcome-based ROI math, 3-tier anchored pricing table, risk-reversal & outreach scripts |

## Model Tiers (`mode` parameter)
* `auto` (Default): Balanced speed and strategic depth.
* `fast`: Rapid ideation and quick drafts.
* `deep`: Maximum analytical depth for complex B2B positioning and pricing.

## Privacy & Data Handling Disclosure

- **External Transmission:** Calling `https://api.solopreneurlab.app` transmits your request payload (`user_id`, `sku`, `mode`, and `user_input`) outside your local environment over encrypted HTTPS to Solopreneur Lab's inference gateway and SkillPay billing ledger.
- **Do Not Submit Confidential Data:** Never include client-confidential records, NDA-covered documents, proprietary trade secrets, credentials, or sensitive personal data (PII) in `user_input`.
- **Use a Pseudonymous `user_id`:** Pass a non-PII, pseudonymous identifier for `user_id` (e.g., `anon_demo_001`) to track prepaid micropayment balance without exposing personal identity.
- **Informed Consent Required:** Disclose this external transmission to the user and obtain explicit confirmation before sending any request.

## Execution Instructions for AI Agents

1. Collect the user's background, target audience, or raw notes as `user_input`, and select the appropriate `sku` (`complete`, `origin`, `content`, or `leverage`) and `mode` (`auto`, `fast`, or `deep`).
2. Inform the user that `user_input` and a pseudonymous `user_id` will be sent externally to `https://api.solopreneurlab.app`, warn against submitting confidential or PII data, and wait for explicit approval.
3. Once confirmed, send a `POST` request to `https://api.solopreneurlab.app` with a pseudonymous `user_id` representing the current user:

```bash
curl -X POST https://api.solopreneurlab.app \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "<pseudonymous_non_pii_id>",
    "sku": "complete",
    "mode": "auto",
    "user_input": "<sanitized_user_background_or_notes>"
  }'
```

4. **Handling HTTP 402 (Payment Required)**:
   * If the API returns `HTTP 402`, extract the `payment_url` from the JSON response.
   * Present the `payment_url` clearly to the user and instruct them to top up USDT on BNB Chain.
   * Once the user confirms payment, retry the exact same `POST` request with the same `user_id`.
5. **Handling HTTP 200 (Success)**:
   * Render the Markdown content from the `data` field directly to the user without truncating or summarizing.