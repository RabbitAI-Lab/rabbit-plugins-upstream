---
name: ai-era-career-planner
version: 2.0.0
author: orionshaowswmw
license: MIT-0
description: >
  Offline, deterministic career planning for the AI era (China market focus).
  Holland RIASEC 3-question screen with a complete 8-combo deterministic code
  table, 5-value (pick-2) and 8-anchor screens, a 12-direction heuristic match
  with sourced 2026 job-demand ratings (AI Agent talent +244%, AI PM +87.7%,
  entry-level decline since 2022-10, etc.), an honest factor-model salary
  reference DB (5376 modeled ranges + 74 scraped cross-check samples with
  measured -80%..+432% drift — never presented as market data), and a
  Markdown report generator with an upfront honesty disclaimer.
  All scripts are python3-stdlib, zero network, JSON in/out, exit codes 0/2.
tags:
  - career
  - planning
  - holland-riasec
  - mbti
  - job-market
  - china
  - ai-era
  - salary-reference
metadata: {"openclaw": {"emoji": "🎓"}}
---

# ai-era-career-planner 🎓 v2.0.0

Offline career-planning engine for the AI era. Every number in this skill is
either **sourced** (dated, in `references/job_demand.md` and `data/` meta),
**modeled** (factor model, reproducible), or **labeled 定性/启发式**
(qualitative / heuristic). The v1.0.6 "verified" salary database is the
anti-pattern this version exists to fix: see `references/salary_data.md`.

## Hard rules (anti-hallucination contract)

1. Salary figures from `data/salary_database.json` are **factor-model
   reference ranges, NOT market data**. Never present them as real offers or
   platform quotes. Always emit the provenance line.
2. Assessments (Holland/MBTI/values/anchor) are **screening material**
   (MBTI retest consistency ~50-65%; Holland reliability ~.91-.95).
   Never say "your career is X" — say "this fits X better, let's discuss".
3. Fit indices are **heuristic, not predictions**:
   `fit = round(5×(0.4·holland + 0.3·values + 0.3·anchor))`, missing
   dimensions renormalize, documented in every output.
4. Trend claims must carry a source+date (`references/job_demand.md`);
   anything without one stays labeled **（定性）**.
5. All scripts: python3 stdlib, zero network, JSON to stdout, machine-readable
   errors to stderr, exit 0 = ok / 2 = bad input.

## Command contract

| Command | Purpose | Key flags |
|---|---|---|
| `holland` | 3-question → deterministic RIASEC code (all 8 combos) | `--answers '{"q1":...,"q2":...,"q3":...}'` |
| `match` | 12-direction heuristic match (top-N + full ranking) | `--answers '{"holland"|\\"holland_answers","values","anchor"}'` `--city` `--industry` `--level entry\|mid\|senior\|expert` `--top N` |
| `salary` | one modeled salary range + provenance | `--city --industry --occupation --level` \| `--list cities\|industries\|occupations\|levels` |
| `report` | Markdown report from a JSON result file (validated) | `--data-file results.json [--out 报告.md]` |
| `salary-db` | regenerate the salary DB deterministically | `python3 scripts/generate_salary_db.py [--date YYYY-MM-DD]` |

All commands: `python3 scripts/career_planner.py <cmd> ...` (the `report`
command is also standalone in `scripts/report_generator.py`).

Typical flow: ask the 3 Holland questions (+ pick-2 values, 1 anchor) →
`holland` → `match --city … --industry …` → write `results.json`
(`profile` fields + `recommendations` from match) → `report`.

## The 12 directions

AI/算法 · AI产品 · 数据分析 · 后端开发 · 金融分析 · 医疗健康 · 教育培训 ·
营销/跨境 · UI/UX · 保险经纪 · 机械/新能源 · 体制内.
Each has a sourced-or-labeled `ai_rating`, an entry path, and a risk line
(embedded in the script's `DIRECTIONS` table and echoed in every match output).

## Load map (progressive disclosure)

| File | Load when |
|---|---|
| `references/assessment.md` | running the screens; scoring rules & validity evidence |
| `references/job_demand.md` | citing ANY demand statistic (dated sources 2025-03 → 2026-07) |
| `references/salary_data.md` | explaining/auditing salary figures (method, drift audit, anchors) |
| `references/ai_career_impact.md` | AI-impact discussion (all qualitative, labeled) |
| `references/industries/*.md` | industry deep-dive (qualitative observations) |
| `references/mbti.md` | MBTI screen + 16-type→Holland crosswalk (heuristic) |
| `references/career_anchor.md` · `education_paths.md` · `flow_engine.md` | anchor screen · learning paths · conversation flow (paths A–D) |
| `references/overseas_jobs.md` | overseas roles (Tavily 2026-07-26, mid-level USD ranges) |
| `data/salary_database.json` | salary lookups (via `salary` command; 5376 modeled + 74 samples) |
| `data/insurance_broker_companies.json` | 保险经纪 direction (28 firms, public 400 lines, verify before quoting) |
| `tools/career_selftest.py` | verifying the install (offline, ~10 groups) |

## Verification

`python3 tools/career_selftest.py` → `ALL CHECKS PASSED`.
README.md carries the artifact tree hash with the recompute script.

## Privacy

All scripts are local and offline; they read only the files you pass them.
Career assessments stay on your machine. `tracker_system` writes files only
when the user explicitly asks (see `references/tracker_system.md`).
Insurance company entries are public business contact lines, not personal data.
