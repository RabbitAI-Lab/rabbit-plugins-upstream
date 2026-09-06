# Reading the Agent Arena leaderboard correctly

Sources: arena.ai/leaderboard/agent (fetched 2026-09-06; board date
2026-09-05, 59 models, 2,285,256 sessions) and the official methodology
post "Agent Arena: Causal Evaluation of Agents in the Real World"
(arena.ai/blog/agent-arena-methodology, 2026-06-04).

## What the ranking measures (official)

Rankings are **not** pairwise Elo votes. The methodology is **causal
tracing**: the agent is treated as a multi-component system (orchestrator
model + subagents + image models + harness); component selections are
treatments in a multi-intervention randomized controlled trial over
in-the-wild sessions. The headline column **Net Improvement (τ̂)** is the
estimated causal treatment effect with 95% CIs. This decouples the
orchestrator's contribution from the harness and subagents.

## The five signals (official definitions)

| Signal | Definition |
|---|---|
| Confirmed success | Final user approve/disapprove of the task trajectory (approve/disapprove buttons on every turn; multiple tasks can exist per session) |
| Praise vs complaint | Explicit verbal praise ("looks great") vs complaint ("this is broken"); success if praise outnumbers complaints |
| Steerability | The agent executes a user correction ("no, do X instead") and the user accepts the fix |
| Bash recovery | Turns to recover from a model-caused bash error (not environment issues); giving up adds a penalty |
| Tool hallucination | References to tools that do not exist — **lower is better** |

Extra board columns: Sessions (sample size — small numbers mean wide CIs),
Cost/Task P50, Output Tokens/Task P50, Price $/M.

## Compute tiers are part of the entry

Leaderboard entries are **(model, tier)** pairs — e.g. "Claude Opus 5
(High)" and "Claude Opus 5 (Max)" are separate entries; "GPT 5.6 Sol
(xHigh)" too. Tiers observed on the board: High, Max, xHigh, Medium.
**Consequence:** "use the Max model" is not a setting you pick globally —
it is a per-model reasoning/compute tier offered for some models. Pick the
model, then the tier the task can afford (cost per task varies widely
across tiers — the board's Cost/Task P50 column shows it).

## Rotation protocol (executable)

Model names and tiers rotate. This skill therefore ships a **dated
snapshot** (`data/model_snapshot_YYYY-MM-DD.json`) and a checker:

1. Paste/copy the current top rows from arena.ai/leaderboard/agent into a
   JSON file: `{"dump_date": "YYYY-MM-DD", "total_models": N, "top":
   [{"rank": 1, "model": "Name (Tier)", ...}, ...]}` (extra columns are
   ignored).
2. `python3 scripts/arena_playbook.py model-check --dump mydump.json`
   → reports rank drift, rotated-out entries, and new/renamed entries
   against the latest snapshot. Matching key = normalized
   (name-without-tier, tier); anything unmatched is reported as
   "verify against live leaderboard" — the tool does not guess renames.
3. If the check shows rotation, `python3 scripts/arena_playbook.py
   snapshot --dump mydump.json --date YYYY-MM-DD` writes the new snapshot
   into data/ (future checks use it as baseline).

Rules:
- A dump **older** than the snapshot still computes — but the output warns
  the delta is historical, not drift.
- **Never** copy model names from the snapshot into prompts as if they were
  current. The snapshot is a *comparison baseline*, and every live decision
  should be made from the live board or the live model picker.

## What NOT to read into the numbers

- CIs: with thousands of sessions, even ±1pp effects are "significant" —
  adjacent ranks within their CIs are statistically indistinguishable.
- Small-session rows (e.g. a few thousand) are noisier than 70k-session rows.
- Cost/Task and Tokens/Task are medians (P50), not averages.
- The board ranks **orchestrator models** for Agent Mode; it does not rank
  Direct-chat quality, vision quality, or price-per-token efficiency in
  isolation.

## Grounding of this skill's own claims

Every model name in this skill must appear in a dated snapshot or in the
live board at fetch time. v1.x's "verified July 2026" list contained items
the live board contradicts (e.g. "Fable 5 suspended June 2026" — the board
shows Fable 5.1 (Max) at #1 on 2026-09-05). That is the failure mode this
snapshot protocol prevents.
