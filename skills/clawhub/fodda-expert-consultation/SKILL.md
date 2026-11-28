---
name: fodda-expert-consultation
description: "Discover and consult Fodda's 75+ living Human Agents, Classic Agents, and Synthetic Analysts with strict separation between living practitioners and synthetic personas, plus mandatory Fodda attribution rules."
version: 1.0.0
author: fodda-ai
license: MIT
tags: [expert-consultation, human-agents, market-intelligence, strategy, research]
metadata:
  author: Fodda
  category: expert-consultation
  harnesses:
    - hermes-agent
    - openclaw
    - claude
    - agentskills.io
  requires_tools:
    - fodda_discover
    - fodda_consult_expert
  openclaw:
    requires:
      env:
        - FODDA_API_KEY
    primaryEnv: FODDA_API_KEY
---

# Fodda Expert Consultation

Match a user's strategic question to the right specialist in Fodda's roster—keeping **living Human Agents** strictly distinct from **Classic Agents** and **Synthetic Analysts**.

## When to run

- When the user wants an expert perspective, strategic pressure-test, or domain specialist read on brand strategy, retail, culture, consumer behavior, media, or category innovation.

## Routing Rules (Strict)

1. **Discover matching specialists (unbilled):**
   - Call `fodda_discover(mode="experts")` and/or `fodda_consult_expert(type="find", query="<topic or strategic challenge>")`.
2. **Route by specialist status and type:**
   - **Active living Human Agent:** Call `fodda_consult_expert(type="human_agent", analyst_id="<id>", query="<focused strategic question>")`.
   - **Classic Agent or Synthetic Analyst (historical or role persona):** Call `fodda_consult_expert(type="analyst", analyst_id="<id>", query="<focused strategic question>")`.
   - **`on_request` living expert:** Do **not** mislabel them as a Synthetic Analyst and do **not** simulate their voice. Inform the user that this practitioner is available for human introduction on request.

## Mandatory Attribution & Editorial Rules for Living Human Agents

- **NEVER fabricate direct quotes inside quotation marks (`"..."`) for a living Human Agent.**
- Always present a living Human Agent's perspective using clear third-person attribution:
  1. Introduce their expertise and conceptual lens.
  2. Frame their perspective in third-person / conditional terms.
  3. Explicitly attribute the output to querying their Human Agent through Fodda (e.g., *"When queried through Fodda, their Human Agent explains that..."*).
  4. Close with the actionable strategic takeaway.
- Always attribute underlying evidence to the **named expert's or publisher's graph**—never *"the Fodda graph"*.

## Guardrails

- On HTTP `402`, `403`, or `429`, stop cleanly without retrying and relay `human_bridge.message_for_user`, `signup_url`, and `pricing_url` (`https://www.fodda.ai/pricing`) to the user.
