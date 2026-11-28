---
name: fodda-brand-intelligence
description: "Build an on-demand, evidence-backed brand, competitor, and earnings intelligence dossier using Fodda's curated knowledge graphs, industry reports, and claim verification."
version: 1.0.0
author: fodda-ai
license: MIT
tags: [brand-intelligence, competitive-intelligence, earnings, research, market-intelligence]
metadata:
  author: Fodda
  category: market-intelligence
  harnesses:
    - hermes-agent
    - openclaw
    - claude
    - agentskills.io
  requires_tools:
    - fodda_discover
    - fodda_brand_intel
    - fodda_search
    - fodda_verify_claim
  openclaw:
    requires:
      env:
        - FODDA_API_KEY
    primaryEnv: FODDA_API_KEY
---

# Fodda Brand Intelligence Dossier

On-demand, evidence-backed brand and competitor dossier combining cross-graph brand presence, industry reports, domain trends, and claim verification.

## When to run

- When the user asks for an executive brand dossier, competitive positioning read, or strategic audit of a named consumer, retail, beauty, food and beverage, fashion, sport, media, or travel brand.

## Workflow

1. **Recon coverage (unbilled):**
   - Call `fodda_discover(mode="recon", topic="<brand and category context>")` to confirm Fodda's graph coverage and identify the strongest publisher and expert graphs for the brand.
2. **Pull cross-graph brand dossier:**
   - Call `fodda_brand_intel(mode="dossier", brand="<brand>", compare_brands=[...])` to capture trend footprint, ranked co-occurring competitors, and lifecycle signals.
3. **Deepen with reports and domain intelligence:**
   - Call `fodda_search(scope="report", query="<full semantic question about the brand's category strategy>")`.
   - Call `fodda_search(scope="domain", query="<full semantic question about consumer behavior shifts affecting the brand>")`.
   - Always write full, outcome-oriented semantic sentences—never single keywords.
4. **Verify load-bearing claims:**
   - For the 1–3 sharpest factual or market assertions in the draft, call `fodda_verify_claim(claim="<specific claim>")` to ground them against curated graphs and corporate earnings disclosures.
5. **Deliver the structured dossier:**
   - Present a clean brief covering **Brand Footprint**, **Competitive Overlap**, **Category & Report Signals**, **Verified Claims**, and **Strategic Implications**.

## Guardrails & Attribution

- Always attribute findings to the **named expert or publisher graph** returned in the tool output (e.g., *"PSFK's Retail graph shows..."*, *"Mintel's research indicates..."*)—never *"the Fodda graph"*.
- If a brand has minimal footprint in Fodda's graphs, state that plainly rather than padding.
- On HTTP `402`, `403`, or `429`, stop cleanly without retrying and relay `human_bridge.message_for_user` plus `https://www.fodda.ai/pricing`.
