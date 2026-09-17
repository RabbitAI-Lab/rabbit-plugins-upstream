# Changelog

## v2.0.0 — 2026-09-06

Complete from-the-ground rebuild after a grounded, evidence-based audit of
v1.0.6 (installed and read file-by-file; every v1 claim re-derived by running
the bundled generator against the shipped database).

### Provenance findings (the core fix)

- **Fabricated salary provenance (v1 → removed).** `salary_database.json`
  meta claimed 国家统计局/智联招聘/前程无忧/猎聘/BOSS直聘 "2024" sources and
  "verified" stamps. The bundled generator reproduces the shipped values
  exactly: all 5376 modeled records are factor-model output
  (tier1 baseline × level × industry × city × [0.9,1.1]). v2 meta states the
  method and the honest provenance statement in every query output.
- **Contaminated v1 records.** v1 shipped 5388 records: 5376 modeled − 29
  overwritten by scraped values + 12 injected scrape fragments (city "未知",
  fragment occupation names, HR 0-208,333/month). One overwrite was a
  garbage ¥200,000/month point for 算法工程师/北京/mid (v1's own scrape sample
  shows +432% drift vs the model). v2 ships the clean 5376 modeled records;
  all scraped material lives separately in `scrape_samples`.
- **"Verified" samples were mostly not verified.** Of the 74 v1
  "verification" samples: 32 are byte-identical to model values (backfilled
  during v1's verification pass — zero independent evidence), 29 are genuine
  scraped prices, 13 are non-modelable fragments. Recomputed drift of the 29
  genuine samples: **28 of 29 deviate >10% from the model (−80.2% to +431.9%)**.
  v1 had even applied "drift corrections" that moved values toward the model
  in some cases and away in others. v2 keeps the samples as raw evidence with
  computed `drift_vs_modeled_pct` and a summary stating exactly this.
- **Calibration anchors added** (dated public data, for comparison only):
  航空航天 AI 工程师 ¥22,787/mo, 新能源 ¥22,594/mo (智联招聘《2026年人工智能
  产业人才发展报告》2026-07-21, H1 2026 data); 算法工程师 ¥23,510/mo
  (新华社 2025-03-26) vs model tier1-mid 25920-49280 — directional evidence
  that model midpoints sit well above platform averages.

### New engine (offline, deterministic, JSON in/out)

- `scripts/career_planner.py` — single CLI, python3 stdlib, zero network:
  - `holland`: 3-question screen → **complete 8-combo deterministic table**
    (v1 listed 5 of 8 combos and one of the "options" (说服) was not an
    option of any question); mixed `I/A` code for 安静+概念+自由.
  - `match`: 12 directions (AI/算法, AI产品, 数据分析, 后端开发, 金融分析,
    医疗健康, 教育培训, 营销/跨境, UI/UX, 保险经纪, 机械/新能源, 体制内),
    documented heuristic `fit = round(5×(0.4·holland + 0.3·values +
    0.3·anchor))` with per-dimension sub-scores; missing dimensions are
    marked `not_assessed` and weights renormalize; deterministic tie-break
    (fit desc → salary median desc → name asc); salary lookup per
    `--city/--industry/--level` with null+note fallbacks; every output
    carries `assessment_type: "screening"` + validity note (MBTI retest
    50-65%; Holland .91-.95) + the heuristic disclaimer.
  - `salary`: exact modeled range + factor-model provenance line;
    `--list cities|industries|occupations|levels`; invalid values → exit 2
    with the valid list.
  - `report`: JSON schema validation with actionable errors; data via
    `--data-file` (no more argv-embedded JSON); report opens with a 4-point
    honesty disclaimer; footer now v2.0.0 (v1 hardcoded "v1.4").
- `scripts/generate_salary_db.py` — honest rewrite; reads
  `data/scrape_samples.json` at runtime (no inline data), writes
  `data/salary_database.json` deterministically (date arg only).
- `scripts/report_generator.py` — standalone report CLI, same validation,
  corrected footer.
- `tools/career_selftest.py` — 95 offline checks in 11 groups:
  frontmatter compliance, phantom-free tree (no `/Users/` paths, no
  fabricated 2024 source strings, no 国家统计局 claim), all 8 Holland
  combos + exit-2 paths, match determinism/tie-break/partial-input,
  salary known value (13500-24200) + invalid-city exit 2, report roundtrip
  + malformed-JSON exit 2, DB integrity (5376 records, arithmetic
  reproduction, regeneration determinism), scrape-sample honesty (32/29/13
  breakdown, no verification fields), insurance JSON hygiene, reference
  labels (定性/供参考 everywhere qualitative), CLI contract.

### References

- `references/job_demand.md` — rebuilt on dated public sources: 智联招聘
  2026-07-21 (AI Agent +244%, AI PM +87.7%, 供需 2.62, 航空航天 ¥22,787,
  新能源 ¥22,594…), 新华社 2025-03-26 (算法 +46.8% @ ¥23,510…),
  新浪财经 2026-03-31 (AI PM +129%, entry-level decline since 2022-10,
  72% of tier-1 firms require AI-tool skills), 苏州人社局 2026-07-03
  (AI 应届 +28.4%, 21% from high-end manufacturing). Every figure dated;
  remaining direction claims explicitly labeled 定性.
- `references/assessment.md` — complete 8-combo table, values screen fixed
  (v1 said "选三项" while listing 5; now "5 选 2"), scoring rules documented,
  validity evidence cited (pigment.is 2026-04-20).
- `references/mbti.md` — mojibake fixed (E/I question missing separator),
  MBTI→Holland crosswalk completed (v1 covered 12 of 16 types; ISFJ/INFJ/
  INTP/ESFP added), labeled heuristic.
- `references/salary_data.md` — method, the 29/12 contamination finding,
  32/29/13 sample breakdown, drift range, calibration anchors.
- `references/industries/*.md` (6) — each now carries an explicit
  "定性行业观察（供参考）" label; tech_career's unsourced "CRUD -40%" →
  "CRUD类岗位收缩（定性判断）", 薪资曲线 labeled 经验区间.
- `references/ai_career_impact.md`, `industry_trends.md` — labeled
  qualitative (the "70%常见问题" figure flagged as an unsourced estimate).
- `references/overseas_jobs.md` — kept (genuinely sourced Tavily
  2026-07-26), author-machine raw-data path line replaced with provenance
  note + last-updated.
- `references/integrations.md` — phantom `references/i18n/en.md` reference
  removed; user-authorization principles kept.
- `data/insurance_broker_companies.json` — moved from `references/`,
  cleaned (raw_answer/snippets/verified booleans stripped), 8 legacy
  (2024-09-01) entries flagged unverified with suspected-placeholder
  numbers; public-contact + verify-before-quoting note in `_meta`.
- Removed: `references/salary_scrape_report.txt` (author-machine artifact,
  `/Users/walter/...` path), `references/salary_database.json` (moved to
  `data/` as the honest version).

### SKILL.md

Full rewrite: version/author/license, description ≤1024 chars, proper YAML
tags list, no fake `verification_hash`, hard-rules anti-hallucination
contract, command contract table, 12-direction list, progressive-disclosure
load map, verification section, privacy section.

### Multi-model audit trail (2026-09-06)

Pass 1 — 3 adversarial audits, different providers/models, verbatim-quote
guard (every quoted claim byte-verified against the tree before triage):

- Engine audit (cohere, command-a-03-2025): 4 findings — 0 valid.
  False positives, each verified by execution: `sorted(set)` is
  deterministic (3-run test); `holland_answers` partial input exits 2 with
  an actionable message (test); report validation cannot be bypassed
  (exit-2 + empty stdout test); `annual_note` is deliberately-preserved raw
  evidence.
- Honesty audit (llm7): 5 findings — 2 "high" false positives (the v1
  audit-trail text in CHANGELOG misattributed to v2 meta; the 32/74
  model-backfill disclosure is honesty, not fabrication), 1 stale (the
  "CRUD -40%" string only survives as a v1-flaw citation in CHANGELOG),
  2 accepted as minor label additions (校准锚点 title += 供参考; MBTI
  crosswalk title += 启发式).
- Contract audit (gemini-3.1-flash-lite after mistral/zai rate-limits):
  5 findings — 1 valid (selftest had no `salary --list <invalid>` boundary
  check → added, now 96 checks), 4 false positives verified against code
  and execution (optional-flags-by-design with explicit exit-2 handling;
  load-map glob is standard; catch-all `except` → `err()` → exit 2;
  "token cost" framing is a category error — the agent receives a few
  hundred characters of JSON, not the 1.5MB DB).

Pass 2 — 2-model diff re-audit of the 3 changed files + re-verification of
all 9 rejected findings (results in the pre-publish notes; no further code
changes required beyond those already applied).
