# arena.ai modes — what they actually are (verified 2026-09-06)

Source: arena.ai official pages and the Agent Mode blog
(arena.ai/blog/agent-mode, published 2026-06-04, updated 2026-06-05),
fetched 2026-09-06. Re-verify before relying on this if the product changed.

## The four documented modes

| Mode | URL | What it is (official) | Use when |
|---|---|---|---|
| Direct | arena.ai/ | Single-model chat (one conversation with one model) | Single-shot Q&A, quick lookups, one-off generation, anything that fits in one exchange |
| Battle | arena.ai/ | Blind A/B: two anonymous models answer, you vote | Honestly evaluating two models head-to-head; contributing to the arena's evaluation data |
| Side-by-Side | arena.ai/ | Compare models on the same prompt with visible identities | Deciding between two known models for a specific task |
| Agent | arena.ai/agent | Autonomous multi-step: the agent plans and uses built-in tools in a sandbox | Multi-step workflows: research + build, coding with iteration, file processing pipelines |

Mode switch: top-left dropdown on the homepage (default "Battle Mode") or
go directly to arena.ai/agent.

## Agent Mode — official capabilities (2026-06-04)

Built-in tools: **web search, image generation, file upload, coding
assistance, sandbox/bash environment, GitHub connect** (NEW as of the
2026-06-05 update). The agent "autonomously builds a plan and uses its
built-in tools to accomplish the entire multi-step workflow in one go."

**Official task-mix breakdown** (what real users actually do in Agent
Mode): coding 29%, research 11%, planning 11%, workflow automation 3.9%,
rest long-tail (data analysis, translation, media analysis).

**Official usage pattern**: users delegate in the first message, then
*tighten* control in follow-ups — treat the agent like a hands-on-managed
employee, not a fire-and-forget process. Twice as many users end up
tightening controls rather than loosening them.

## Home-page builders (verified on arena.ai/, 2026-09-06)

Image edits, landing page, dashboard, playable browser game, design-to-code
(image in, app out), full-stack app — these are task templates, not
separate modes.

## What is NOT a documented mode (removed from this skill in v2.0.0)

- "Code Arena" — no such mode in official docs; coding is a task category
  inside Agent Mode (29% of its traffic) and Direct chat.
- "Max router" — no router by that name. "Max" is a **per-model compute
  tier** (see references/leaderboard.md).

## Choosing a mode — executable version

`python3 scripts/arena_playbook.py mode --task "..." [--files N] [--steps N]
[--coding] [--compare] [--blind] [--budget-conscious]`

Rule order (deterministic, documented in code):
1. `--compare` → Side-by-Side
2. `--blind` → Battle
3. Agent when: steps>=3, OR files>=2, OR file+coding/deliverable/multi-step,
   OR coding+steps>=2, OR deliverable wording + multi-step/file, OR tool-chain
   wording (search/scrape/fetch + produce)
4. Otherwise → Direct

`--budget-conscious` downgrades low-complexity Agent picks to Direct.

**Why not "files → Agent"?** A single-file question ("what is the average
of column A in this CSV?") is a Direct task; forcing Agent adds latency and
cost for no benefit. Agent is for *multi-step tool workflows*, matching the
official task-mix data.
