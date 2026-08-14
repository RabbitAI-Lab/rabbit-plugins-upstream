---
name: card-full
description: Return a compact full report for one major-US credit card, covering fees, offer, earnings, redemption, credits, travel benefits, protections, mechanics, eligibility, and strategy. Use when the user wants the whole card picture.
---

# Card Full

Return the whole-card view for one exact card variant.

## Workflow

1. Resolve the card with [../card-identity/SKILL.md](../card-identity/SKILL.md). If ambiguous, stop and return a numbered choice list.
2. Follow the `card-full` search ceiling and preferred sources in [../card-shared/source-policy.yaml](../card-shared/source-policy.yaml).
3. Run one shared discovery search: `CARD NAME review benefits welcome offer`. Use a short result payload.
4. Fetch the issuer page and, only when a required field remains unresolved, one approved secondary source. Do not separately search for elevated or historical offers unless the user asks when to apply, whether to wait, or for offer history.
5. When the user requests several cards, research them as one run: one shared discovery search, issuer pages fetched in parallel, and one secondary source total for live offer validation. Do not produce independent full-research loops for each card.
6. Stop when the contract is covered. Mark an unresolved optional detail `unconfirmed` instead of fetching more pages or reopening the same page.
7. Compose the output using [../card-shared/section-definitions.md](../card-shared/section-definitions.md) and the `card-full` contract in [../card-shared/command-contracts.yaml](../card-shared/command-contracts.yaml).
8. Apply [../card-shared/confidence-rules.md](../card-shared/confidence-rules.md) and [../card-shared/normalization-rules.md](../card-shared/normalization-rules.md). Keep `sources` in hidden YAML only.

## Required Sections

- `## 💰 Fees`
- `## 🎁 Welcome Offer`
- `## 📈 Earning Rates`
- `## 🔄 Redemption`
- `## 🏷️ Credits`
- `## ✈️ Travel Benefits`
- `## 🛡️ Protections`
- `## ⚙️ Account Mechanics`
- `## ✅ Eligibility`
- `## 🧭 Strategy`
- `## 👤 Who Is This Card For?`
- `## 🃏 Similar Cards`
- `## 📋 Confidence Notes`

The credits section includes only statement credits, cash-back rebates, and complimentary subscriptions with concrete dollar values. Keep enhanced earn rates and anniversary bonuses out of that section.
