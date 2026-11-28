---
name: fodda-market-signal-monitor
description: "Schedule recurring daily or weekly market, brand, and competitor intelligence briefs powered by Fodda's 381+ curated knowledge graphs, earnings Q&A, live institutional feeds, and living Human Agents."
version: 1.0.0
author: fodda-ai
license: MIT
tags: [market-intelligence, competitive-intelligence, trends, monitoring, research]
metadata:
  author: Fodda
  category: market-intelligence
  harnesses:
    - hermes-agent
    - openclaw
    - claude
    - agentskills.io
  requires_tools:
    - fodda_brand_intel
    - fodda_search
    - fodda_consult_expert
  openclaw:
    requires:
      env:
        - FODDA_API_KEY
    primaryEnv: FODDA_API_KEY
---

# Fodda Market Signal Monitor

Designed for scheduled recurring runs (daily or weekly) in Hermes Agent or any `agentskills.io`-compatible harness with persistent memory. Delivers a complete, cited competitive and category intelligence brief on every scheduled trigger.

## When to run

- On a recurring daily or weekly schedule (cron / heartbeat) monitoring a user's watchlist of brands, competitors, and consumer/retail/brand categories.
- On demand when a user asks for a fresh signal scan of their category or competitor set.
- Confirm the watchlist fits Fodda's domains (consumer, retail, beauty, fashion, food and beverage, sport, marketing, brand, media, travel, health, culture, macro-trends) before making billable calls.

## Workflow

Execute these four steps once per trigger:

1. **Watchlist signal pull:**
   - For a primary brand watchlist, call `fodda_brand_intel(mode="dossier", brand="<brand>")` (or `fodda_search(scope="batch", queries=[...])` with up to 10 semantic, outcome-oriented full-sentence queries—never single keywords).
2. **Corroborate with earnings and live institutional data:**
   - Call `fodda_brand_intel(mode="validated_trends", topic="<theme>", sector="<sector>")` to check whether executive earnings calls corroborate the shift.
   - Call `fodda_search(scope="supplemental", query="<semantic question>", brands=[...])` to pull corroborating live institutional signals.
3. **Pressure-test the sharpest signal with a living Human Agent:**
   - Identify one relevant active living Human Agent via `fodda_discover(mode="experts")` (if not already cached in memory) and call `fodda_consult_expert(type="human_agent", analyst_id="<id>", query="<sharpest signal question>")`.
   - Never fabricate direct quotes inside quotation marks for living Human Agents. Explicitly attribute the perspective to querying their Human Agent through Fodda.
4. **Diff against prior memory and deliver the brief:**
   - Compare findings against the previous run stored in persistent memory.
   - Save the updated snapshot to memory and deliver a concise brief structured as:
     - **What Changed** (net-new shifts since the prior run, citing named expert or publisher graphs—never "the Fodda graph")
     - **Why It Matters** (corroborating earnings or institutional evidence + Human Agent strategic lens)
     - **Next Move** (1–3 concrete actions for the team)

## Guardrails & Error Handling

- **Max 1 run per scheduled trigger.** Never spin in a retry loop if an API call fails.
- **On HTTP 402 (`payment_required`), 403, or 429:** Stop immediately without retrying. Relay `human_bridge.message_for_user`, `signup_url`, and `pricing_url` (`https://www.fodda.ai/pricing`) verbatim to the human so they can add a key or upgrade their plan.
- **Pricing transparency:** Defer to Fodda's published pricing at `https://www.fodda.ai/pricing` or live `402` responses rather than guessing static prices.
- **Attribution:** Always cite the named expert graph, research publisher, or corporate filing returned (e.g., *"PSFK's Retail graph shows..."*, *"Mintel's research indicates..."*). Never attribute insights to "the Fodda graph."
