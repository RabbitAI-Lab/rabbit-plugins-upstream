# Agent Discovery

## What you can do with this skill

If a user needs **career direction guidance for the AI era** (China market):
screen them (Holland RIASEC 3-question, 5-values pick-2, 8-anchor), match
them against **12 concrete directions** with sourced 2026 demand ratings,
pull a **modeled salary reference range**, and render a **Markdown report**
with an upfront honesty disclaimer — this skill has one offline,
machine-readable command for each step.

## When to load it

- "我适合做什么工作 / 帮我做职业规划" → run the screens, then `match`
- "XX方向现在前景怎么样" → `references/job_demand.md` (dated sources)
  or the direction's `ai_rating` from `match`
- "这个岗位大概多少钱" → `salary` (modeled range + provenance line)
- "出一份报告 / 把结果整理一下" → `report` (or `report_generator.py`)
- "校验一下安装" → `python3 tools/career_selftest.py`

## When NOT to use it

- The user asks for a **live market quote or real offer range** — the salary
  DB is a factor-model reference (measured −80%…+432% drift vs scraped
  prices); point them to live platform data instead.
- The user wants a **certified psychological assessment** — these screens
  are conversational heuristics (MBTI retest 50-65%, Holland .91-.95).
- The user wants **overseas** roles in depth — `references/overseas_jobs.md`
  is a dated snapshot (2026-07-26), not a job board.

## Machine interface

`python3 scripts/career_planner.py <cmd> --help`. JSON on stdout
(ensure_ascii=False); machine-readable errors on stderr; exit 0 ok / 2 bad
input. python3 stdlib only; **zero network**.

## Trust model

Every claim is one of: **sourced** (dated, in `references/job_demand.md` and
`data/` meta), **modeled** (reproducible factor model — always labeled as
such), or **explicitly labeled 定性/启发式** (qualitative / heuristic).
If a claim has none of the three markers, it should not be in this skill —
that is the contract v2.0.0 exists to enforce (the selftest checks it).
