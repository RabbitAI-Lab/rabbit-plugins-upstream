---
name: arena-power-user-playbook
version: 2.0.0
author: orionshaowswmw
license: MIT-0
description: >
  Executable power-user playbook for arena.ai. Use when choosing an arena.ai
  mode (Direct / Agent / Side-by-Side / Battle) for a task, reading or checking
  the Agent Arena leaderboard, screening a response with measurable
  weak-response flags, chunking long Agent work with SESSION-STATE.md carry,
  or falling back to cloud providers when arena.ai throttles or is down.
  Bundles a dated, sourced model snapshot (2026-09-05) plus offline
  python3-stdlib scripts: mode advisor, weak-response screener, leaderboard
  rotation checker, state manager, local feedback log.
tags:
  - arena
  - arena-ai
  - model-selection
  - agent-mode
  - leaderboard
  - fallback
  - power-user
metadata: {"openclaw": {"emoji": "🏆"}}
---

# arena-power-user-playbook 🏆 v2.0.0

Executable companion to arena.ai power usage. Every claim here is either
**sourced** (dated, in `references/`), **measured** (script output), or
**labeled as a heuristic**. No unverifiable numbers, no phantom scripts.

## Hard rules (anti-hallucination contract)

1. Model names are **rotating data**, not facts. Never copy a name from this
   skill into a live decision; use the live picker or
   arena.ai/leaderboard/agent, then `model-check` against the snapshot.
2. The dated snapshot in `data/` is a **comparison baseline only**.
3. `weak` reports **screening flags**, never quality judgments.
4. Fallback is **cloud-only** — no local GGUF/llama.cpp, ever.
5. Every script prints one machine-readable summary line; full JSON via `--out`.
   Exit codes: 0 ok · 1 findings/changes · 2 usage or no data · 3 internal error.

## Command contract

| Command | Purpose | Key flags |
|---|---|---|
| `mode` | recommend Direct / Agent / Side-by-Side / Battle | `--task` `--files` `--steps` `--coding` `--compare` `--blind` `--budget-conscious` `--tasks file.json` |
| `weak` | screen one response with weighted heuristic flags (bands weak/medium/strong) | `--response` \| `--file` `--min-words 35` `--expect-short` |
| `model-check` | fresh leaderboard dump vs dated snapshot: drift, rotated-out, new | `--dump file.json` `--date` |
| `snapshot` | write a new dated snapshot from a dump | `--dump` `--date YYYY-MM-DD` `--out` |
| `state` | SESSION-STATE.md for chunked multi-chat work | `--file` `--action init\|add\|summary\|next\|validate` `--goal` `--phase` `--done ...` `--next ...` `--force` |
| `stats` | local feedback log + report (self-improvement loop) | `--action log\|report` `--event` `--model` `--mode` `--log` |
| `selftest` | run the skill self-test | — |

All commands: `python3 scripts/arena_playbook.py <cmd> ...` (python3 stdlib,
zero network, works on any agent runtime).

## Mode decision (quick)

- Compare two known models → **Side-by-Side** · Blind A/B vote → **Battle**
- Multi-step / tools / files + build / coding with iteration → **Agent**
  (official Agent Mode task mix: coding 29%, research 11%, planning 11%)
- Single-shot Q&A, including one-file questions → **Direct**
- "Max/High/xHigh" are **per-model compute tiers on the leaderboard**, not a
  router. Pick model, then a tier the task can afford (see Cost/Task P50).

Details + official sources: `references/modes.md`.

## Leaderboard (how to read it)

Headline = **Net Improvement (τ̂)** from causal tracing over in-the-wild
Agent sessions (95% CIs). Signals: confirmed success, praise-vs-complaint,
steerability, bash recovery, tool hallucination (lower = better). Small
session counts = wide CIs; adjacent ranks within CIs are not distinguishable.
Rotation protocol: `model-check` → `snapshot`. Details:
`references/leaderboard.md`.

## Weak response (3-strike escalation)

`weak` bands: weak ≥50, medium ≥25, strong <25 (screening only). On a real
task: strike 1 = new chat, same task · strike 2 = rephrase + fresh chat with
`state next` carry · strike 3 = higher tier or different family from the live
board · persistent = switch provider (cloud-only table) or split the task.
Log each strike via `stats log --event weak_response`. Details:
`references/fallback.md`.

## Load map (progressive disclosure)

| File | Load when |
|---|---|
| `references/modes.md` | deciding a mode beyond the quick table; auditing mode claims |
| `references/leaderboard.md` | reading ranks/CIs, running rotation protocol |
| `references/fallback.md` | arena.ai degraded, weak-response escalation, chunking |
| `data/model_snapshot_2026-09-05.json` | baseline for `model-check` — sourced from arena.ai/leaderboard/agent, board date 2026-09-05, fetched 2026-09-06 (verify before relying) |
| `tools/playbook_selftest.py` | verifying the install (10 groups, all offline) |

## Verification

`python3 scripts/arena_playbook.py selftest` → `ALL CHECKS PASSED`.
README.md carries the artifact tree hash with the recompute script.

## Privacy

Local scripts read only files you pass them; `stats` writes only to a local
log you name. Nothing leaves the machine. arena.ai itself processes your
prompts server-side — share only data appropriate for it.
