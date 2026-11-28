---
name: fodda-market-intelligence
description: "Expert-curated market, consumer and competitive intelligence for AI agents, with cited evidence across brands, trends, earnings and institutional data."
version: 1.0.0
author: fodda-ai
homepage: https://www.fodda.ai
license: MIT
tags: [market-intelligence, competitive-intelligence, consumer-trends, brand-research, market-research]
metadata:
  author: Fodda
  category: market-intelligence
  harnesses:
    - openclaw
    - hermes-agent
    - claude
    - agentskills.io
  requires_tools:
    - fodda_discover
    - fodda_search
    - fodda_brand_intel
    - fodda_consult_expert
    - fodda_verify_claim
  openclaw:
    requires:
      env:
        - FODDA_API_KEY
    primaryEnv: FODDA_API_KEY
---

# Fodda Market Intelligence

Use Fodda when a task requires **evidence-backed market, consumer, or competitive intelligence** rather than generic web search—backed by expert-curated knowledge graphs, industry reports, corporate earnings commentary, quantitative statistics, live institutional data feeds, and living Human Agents with source provenance attached.

## When to use Fodda

Invoke Fodda only when the user explicitly needs domain intelligence, cited research, or strategic market evidence (do **not** trigger automatically on casual mentions of a company name):

- **Market & category research:** emerging consumer trends, cultural shifts, and category dynamics
- **Competitive & brand intelligence:** brand positioning, competitive landscapes, and co-occurring players
- **Earnings intelligence:** management commentary, analyst Q&A, and earnings-corroborated trends
- **Quantitative evidence & verification:** cited market statistics, institutional data, and factual claim verification
- **Specialist perspectives:** consulting living Human Agents or Classic/Synthetic Analysts

Typical requests include:
- *"What consumer trends are emerging in this category?"*
- *"Research this brand and its closest competitors."*
- *"What signals suggest this market is changing?"*
- *"Find evidence for or against this market strategy."*
- *"What has management said about this issue in recent earnings calls?"*
- *"Give me cited statistics supporting this consumer trend."*
- *"What are industry experts saying about this shift?"*

## Routing Workflow

1. **Discover coverage (unbilled):** Call `fodda_discover(mode="recon", topic="<question>")` when unsure which graphs or specialists fit the topic.
2. **Search curated research & live data:**
   - Trends & consumer shifts: `fodda_search(scope="domain", query="<full semantic sentence>")`
   - Industry reports: `fodda_search(scope="report", query="<full semantic sentence>")`
   - Quantitative data: `fodda_search(scope="statistics", query="<full semantic sentence>")` and `fodda_search(scope="supplemental", query="<full semantic sentence>")`
3. **Brand, competitor & earnings reads:** Call `fodda_brand_intel(mode="dossier" | "earnings" | "divergence" | "validated_trends")`.
4. **Verify load-bearing claims:** Call `fodda_verify_claim(claim="<specific market claim>")`.
5. **Consult specialists (when perspective is requested):** Use `fodda_consult_expert(type="human_agent")` for active living Human Agents and `fodda_consult_expert(type="analyst")` for Classic/Synthetic Analysts. Never fabricate direct quotes inside quotation marks for living Human Agents.

## Guardrails & Attribution

- **Named attribution:** Always attribute insights to the **named expert or publisher graph** or corporate filing returned (e.g., *"PSFK's Retail graph shows..."*, *"Mintel's research indicates..."*)—never *"the Fodda graph"*.
- **Clean `402` / quota handling:** On HTTP `402`, `403`, or `429`, stop immediately without retry loops and relay `human_bridge.message_for_user`, `signup_url`, and `pricing_url` (`https://www.fodda.ai/pricing`).
- **Pricing hygiene:** Always defer to `https://www.fodda.ai/pricing` or live `402` responses rather than guessing static prices.
