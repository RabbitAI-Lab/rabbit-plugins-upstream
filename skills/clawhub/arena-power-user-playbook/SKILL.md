---
name: arena-power-user-playbook
version: 1.1.0
description: >
  Power-user guide to always getting top-tier frontier models on Arena.ai
  (LMArena/Chatbot Arena) without paying. Covers the Max multimodal router
  (proven to outperform every individual model), Direct vs Agent vs Battle vs
  Code mode selection, model rotation caveats, conversation-reset tricks,
  how to avoid weak "Pineapple" model responses, and a current list of which
  models lead each arena (text, code, vision, agent). Use when working with
  Arena.ai, choosing a chat mode, or optimizing for GPT-5 / Claude Opus /
  Gemini Pro tier responses.
author: orionshaowswmw
license: MIT
tags:
  - arena
  - lmarena
  - model-selection
  - router
  - max-router
  - prompt-engineering
  - power-user
  - gpt-5
  - claude
  - gemini
  - free-models
allowed-tools:
  - Read
  - WebFetch
  - Bash
---

# arena-power-user-playbook 🏆

**Always get GPT-5 / Claude Opus / Gemini Pro tier responses on Arena.ai without paying a dime.**

## The one-sentence playbook
Use **Direct Chat → Max** for most things, **Code Arena → Max** for coding, and **Agent Mode (fresh chat each big task)** for multi-step work. Arena is 100% free; the Max router beats any single model it routes to.

## Decision tree
1. **Simple, quick question** → Direct Chat → **Max** (default; multimodal router trained on 5M+ votes)
2. **Multi-step / research / build something** → **Agent Mode** at `/agent` (fresh chat per big task; T1 orchestrators)
3. **Coding** → **Code Arena → Max** (heavy Claude-Opus routing; Kimi K3 for front-end)
4. **Vision / image gen** → Direct → Max (multimodal; beats best single model by +3 Elo, 20+s faster)
5. **Compare two specific models** → Side-by-Side Mode (manual pick)
6. **Blind test / help the leaderboard** → Battle Mode (vote honestly)

## Why Max wins
Max is NOT a model — it's a latency-controlled router trained on 5M+ pairwise community votes. Per Arena's May 2026 Multimodal Max announcement:
- Vision: +3 Elo over the best individual model, 20+ seconds faster
- Frontend code: heavy reliance on claude-opus-4.5 variants (best latency/quality tradeoff)
- Text-to-image: beats top individual models on strength AND latency
- Text: routes ~62% to gpt-5.2-chat-latest, 38% diversified → +12 Elo over any single model

## Critical caveats (2026-07)
- GPT-5.4-High was removed from the Direct manual picker in April 2026, but Max still routes to the strongest available models.
- Agent Mode randomly assigns a fresh orchestrator per chat (all are T1+ per the Agent Arena leaderboard).
- Agent Mode has a ~5-message soft limit per thread (community observation); start a new chat for new tasks.
- Arena rotates models in/out; don't rely on one specific model name always being available.
- The community-named weak model "Pineapple" still occasionally appears in rotation. If you get a useless response, start a new chat or switch to Max.
- Battle Mode is for evaluation/voting, NOT real work (your votes improve Max for everyone).

## If you get a weak/bad response
- Direct chat: switch manual selection to **Max**
- Agent Mode: **start a new chat** (re-rolls the orchestrator)
- Battle Mode: vote honestly (this pushes bad models down the rankings)
- Clear the conversation and resubmit (Max re-routes per-prompt)

## Current frontier tier (mid-2026, per public leaderboards)
- **Claude Opus 4.7/4.8 / Fable 5** — deep reasoning, coding (note: Fable 5 currently suspended per US export control June 2026; returns when restored)
- **GPT-5.2/5.4/5.5/5.6-Sol** — general flagship, multimodal
- **Gemini 3.1 Pro** — long context (2M), vision, price-efficiency
- **Claude Sonnet 4.6/5** — best quality-per-dollar for ~80% of tasks
- **Kimi K3** — #1 on Arena Frontend Code Arena (July 2026)
- **DeepSeek V4 Pro/R1** — math/reasoning, ultra-cheap open-weight fallback

Smart move: let Max decide for you. It is provably better than picking any one model.

## URLs
- Direct Chat: https://arena.ai/ (select "Direct" top-left)
- Agent Mode: https://arena.ai/agent
- Agent leaderboard: https://arena.ai/leaderboard/agent
- Max router direct: https://arena.ai/max
- Blog post on Agent Mode: https://arena.ai/blog/agent-mode/
- Help center: https://help.arena.ai/articles/5432423882-how-to-use-agent-mode

## Background
Arena (formerly LMArena / Chatbot Arena) is run by the LMSYS team, backed by $250M+ funding, serves 10M+ monthly users who have contributed 700M+ conversations and 82M+ votes. They have publicly stated (Reddit, team comments, blog) they will not introduce a paid plan — their mission is that "everyone can use good models for free."
