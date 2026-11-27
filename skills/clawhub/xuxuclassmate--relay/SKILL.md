---
name: relay
description: >-
  Use when one QA/dev engineer runs the whole dev+test lifecycle with a team of AI assistants:
  a supervisor dispatches, specialists each own one external write channel, and parallel helpers
  scale out — covering requirement → cases → review → data → execution → report → defects →
  notify → release. Before delivery a scoring gate checks the flow was followed and re-runs until
  it passes (default 80). Model-agnostic. (中文文档见 https://innonestx.github.io/relay/ 的语言切换。)
---

# relay — multi-agent dev+test workflow (entry)

In one line: **one engineer + a team of AI assistants run dev and test by the book, backstopped by a scoring gate.**

## Roles
A supervisor plus specialists (testing, defects, notifier, coder, docs). This is the entry/overview; the full 24 skills are in "Get the full pack" below.

## Core principles
1. The supervisor only dispatches — never executes.
2. One owner per external write channel (chat → notifier, defect system → defect manager, knowledge base → docs, code/deploy → coder).
3. Judge against the latest requirement: pass if it matches, file a defect if not, escalate if unclear.
4. Conclusions live in an online report; issue numbers stay in sync across chat, report and defect system.
5. Testing never queues — scale out parallel helpers; testers create their own data.
6. Security red lines override everything (no credentials in code/KB, redaction, deploy only when authorized).

## Typical flow (one requirement)
1. The supervisor splits and dispatches, quoting the user's words + time.
2. Testing: cases as md+json+visual → stored only after review passes.
3. Testing: make data → execute (headless-first, per-case evidence, judge by the latest requirement).
4. Conclusions → online report; mismatches → file a defect + notify the dev.
5. The supervisor summarizes back.

## The scoring gate (relay's signature)
Before delivering:
1. **Hard gate first** — check every key step exists and is in order. If not, force the flow from the missing step before scoring.
2. **Score out of 100** against the rubric.
3. **Verdict** — score ≥ PASS_SCORE (default 80, configurable) → pass; below → list the lost points, optimize, re-run the weak steps until it passes or escalate.

## Get the full pack (24 skills + server)
- GitHub: `InnoNestX/relay` — https://github.com/InnoNestX/relay
- Docs: https://innonestx.github.io/relay/ (English, with a 中文 toggle)
- MCP/CLI (any model/client): run the digest-pinned container or the local server — exact commands on the [install page](https://innonestx.github.io/relay/#install). CLI helpers: `relay list` / `relay score`.
- ClawHub plugin: `relay` (OpenClaw package — all skills + slash commands).
- Per-tool integrations: see `plugins/` in the repo (Claude Code / Cursor / ChatGPT / Gemini / Grok / MCP).

## Prohibitions
- The supervisor executing; one assistant holding two external write channels.
- Delivering without following the flow, or below the pass score.
- Credentials in code/KB; committing or deploying without authorization.

## Self-check
- [ ] Clear roles; dispatch carries the user's words + time
- [ ] Cases reviewed before saving; per-step evidence, judged by the latest requirement
- [ ] Conclusions in the online report; IDs synced in three places
- [ ] Scoring gate passed (≥ PASS_SCORE) or re-run/escalated

> The 24 skills themselves are bilingual (English + 中文). This entry page is English; see the docs site for the Chinese toggle.
