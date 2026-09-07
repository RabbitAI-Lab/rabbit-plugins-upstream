# ai-era-career-planner

**Categories:** education, career
**Tags:** #career #planning #holland-riasec #mbti #job-market #china #ai-era #salary-reference

## ✨ What this skill is

An **offline, deterministic** career-planning engine for the AI era (China
market focus): Holland RIASEC screening with a **complete 8-combo
deterministic code table**, a 5-values pick-2 screen, an 8-anchor screen, a
**12-direction heuristic match** with sourced 2026 job-demand ratings, an
**honest factor-model salary reference DB** (5376 modeled ranges + 74 scraped
cross-check samples with measured −80%…+432% drift), and a Markdown report
generator whose first section is an upfront honesty disclaimer.

v2.0.0 is a from-the-ground rebuild after a grounded audit of v1.0.6 found:

- a salary database labeled as if it came from a national statistics bureau
  plus 智联/前程无忧/猎聘/BOSS "2024" reports, which was actually a **factor
  model's synthetic output** with
  29 cells overwritten by scraped values (including a garbage ¥200,000/month
  point) and 12 scrape fragments injected as records;
- "verified" stamps on 74 samples, of which **32 were backfilled from the model
  itself** (no independent evidence) and 28 of 29 genuine scrapes deviate
  >10% from the model;
- a hollow 1.5KB SKILL.md with a fake 16-hex `verification_hash`, a comma-string
  tags field, no version/author, and a phantom reference to a nonexistent
  `references/i18n/en.md`;
- unsourced percentages in job_demand/industry_trends/ai_career_impact and
  industry notes; a mojibake'd MBTI question; hardcoded "v1.4" report footer;
  author-machine local filesystem paths shipped inside an artifact
  (a macOS home-directory path inside the v1 scrape report).

Every claim in v2.0.0 is **sourced** (dated, in `references/job_demand.md` and
`data/` meta), **modeled** (reproducible factor model), or **explicitly
labeled 定性/启发式**. The selftest enforces all of it.

## 🚀 Usage

Install from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/ai-era-career-planner
```

```bash
cd ai-era-career-planner
python3 tools/career_selftest.py                 # verify the install (offline)

# 1) Holland screen (all 8 combos deterministic)
python3 scripts/career_planner.py holland \
  --answers '{"q1":"安静","q2":"事实","q3":"规则"}'

# 2) 12-direction match (partial inputs OK — missing dims renormalize)
python3 scripts/career_planner.py match \
  --answers '{"holland":"R","values":["成就感","自主性"],"anchor":"自主/独立型"}' \
  --city 北京 --industry 互联网/IT --level entry --top 5

# 3) one modeled salary range (with provenance line)
python3 scripts/career_planner.py salary --city 北京 --industry 互联网/IT \
  --occupation 后端开发工程师 --level entry
python3 scripts/career_planner.py salary --list cities

# 4) report from a JSON result file (validated; actionable errors)
python3 scripts/career_planner.py report --data-file results.json --out 报告.md
python3 scripts/report_generator.py --data-file results.json          # standalone

# 5) regenerate the salary DB deterministically
python3 scripts/generate_salary_db.py --date 2026-09-06
```

Exit codes: 0 ok · 2 bad input (JSON errors to stderr, machine-readable).
All outputs are JSON (ensure_ascii=False); reports are Markdown.

## 🔐 Permissions & Requirements

- python3 (standard library only) — no dependencies, **no network access**.
- Reads only `data/` inside the skill and files you pass via `--data-file`.
- Writes only where you point `--out` / `--out-dir`. Nothing else.

## 🔒 Security & Privacy

- Career assessment data never leaves the machine; scripts are offline.
- `references/insurance_broker_companies.json` contains public business 400
  lines (28 firms, sourced 2024-09/2026-07); 8 legacy entries are flagged
  unverified (some numbers look like placeholders — verify before quoting).
- The tracker system (`references/tracker_system.md`) writes files **only**
  when the user explicitly asks and chooses the location.

## ✅ Verification Hash

This digest covers every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `140698faa789d7474103e73930570698a06688e8c8d5e5d947de276c36cfcc46`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
file differs from the published artifact; review before use.
