---
name: skill-auditor
description: Automated security audit for AI agent skills. Use BEFORE installing any skill from ClawHub, GitHub, or other sources. Scans SKILL.md + all files for 30+ red flag patterns, computes a 0-100 risk score, and outputs a structured report. Superset of skill-vetter with automated scanning, batch mode, and CI integration.
version: 1.0.0
license: MIT
---

# Skill Auditor 🔒

Automated, security-first audit for AI agent skills. **Never install a skill without auditing it first.**

> Superset of [skill-vetter](https://clawhub.ai/spclaudehome/skill-vetter) with three additions:
> (1) **Automated scanning** via `scripts/vet.py` — no more manual checklist reading.
> (2) **Quantitative risk score** (0-100) instead of just LOW/MED/HIGH labels.
> (3) **Batch mode + CI integration** — audit an entire `skills/` dir, hook into pre-commit / GitHub Actions.

## When to Use

- Before `clawhub install <skill>` from ClawHub
- Before `git clone` of any skill repo
- Before copying a skill folder into your workspace
- In CI: as a pre-commit hook or GitHub Action on repos that vendor skills
- Periodically: re-audit your installed skills after upstream updates (skills drift)

## Quick Start

```bash
# Audit a single skill folder
python3 {baseDir}/scripts/vet.py path/to/some-skill

# Audit with JSON output (for CI / programmatic use)
python3 {baseDir}/scripts/vet.py path/to/some-skill --json

# Audit all skills in a directory (batch mode)
python3 {baseDir}/scripts/vet.py --batch path/to/skills/

# Show risk score only (0-100)
python3 {baseDir}/scripts/vet.py path/to/some-skill --score
```

## The Audit Protocol (6 Steps)

The automated script handles steps 2-4. Steps 1, 5, 6 still benefit from human judgment.

### Step 1: Source Check (human)

- Where did this skill come from? (ClawHub / GitHub / DM / fork?)
- Is the author known/reputable? Cross-check on the platform's creator page.
- Download / star count (popularity signal, not safety signal).
- Last update date (stale skills rot).
- Are there reviews / discussions from other users?

### Step 2: Automated Code Scan (script)

`scripts/vet.py` reads ALL files in the skill folder and checks against 30+ red-flag rules. See [references/rules.md](references/rules.md) for the full rule set.

Categories covered:
- Network exfiltration (curl/wget to unknown hosts, IP-literal URLs, Pastebin, tor)
- Credential access (`~/.ssh`, `~/.aws`, `~/.config`, browser cookies, keychain)
- Identity files (`MEMORY.md`, `USER.md`, `SOUL.md`, `IDENTITY.md` — core agent files)
- Dangerous code (`eval()`, `exec()` with input, `pickle.loads`, `subprocess` with `shell=True`)
- Obfuscation (base64 decode, hex blobs, minified/encoded payloads)
- File system abuse (writes outside workspace, `sudo`, `chmod 777`, shell rc files)
- Permission escalation (sudo, modifying sudoers, requesting broad scopes)
- Supply chain (installing packages without listing them, curl|sh, pip install from raw URLs)

### Step 3: Permission Scope (script + human)

The script extracts declared permissions from frontmatter (`metadata.openclaw.requires`) and compares against actual file/network behavior. Mismatches are flagged:

- Declares `requires.bins: [gh]` but uses `curl` → mismatch
- No `requires.env` but reads `process.env.GITHUB_TOKEN` → mismatch
- Declares nothing but reads `~/.aws/credentials` → critical

### Step 4: Risk Scoring (script)

Each red flag has a weight (5-25 points). The script sums weights and caps at 100. See [references/scoring.md](references/scoring.md) for the full model.

| Score | Risk Level | Action |
|-------|------------|--------|
| 0-15  | 🟢 LOW     | Basic review, install OK |
| 16-40 | 🟡 MEDIUM  | Full code review required |
| 41-70 | 🔴 HIGH    | Human approval required |
| 71-100| ⛔ EXTREME | Do NOT install |

### Step 5: Trust Hierarchy (human)

Apply different scrutiny based on source:

1. **Official OpenClaw skills** → Lower scrutiny (still audit)
2. **High-star repos (1000+)** → Moderate scrutiny
3. **Known authors with track record** → Moderate scrutiny
4. **New / unknown sources** → Maximum scrutiny
5. **Skills requesting credentials** → Human approval always, regardless of source

### Step 6: Decision & Documentation (human)

Based on the audit report, decide:
- ✅ **SAFE TO INSTALL** — proceed
- ⚠️ **INSTALL WITH CAUTION** — install but monitor, or request changes from author
- ❌ **DO NOT INSTALL** — reject, optionally report to community

Document the decision in your team's trust ledger (see [references/trust-database.md](references/trust-database.md)).

## Output Format

The script produces a structured report:

```
SKILL AUDIT REPORT
═══════════════════════════════════════════════════
Skill:    [name]
Source:   [ClawHub / GitHub / other]
Author:   [username]
Version:  [version]
Audited:  [date] by skill-auditor v1.0.0
───────────────────────────────────────────────────
METRICS:
• Files scanned:    [count]
• Lines scanned:    [count]
• Rule violations:  [count]
• Scan duration:    [seconds]
───────────────────────────────────────────────────
RISK SCORE: 42/100  →  🔴 HIGH

RED FLAGS (by severity):
⛔ CRITICAL (25 pts each):
  • [rule_id] [file:line] — [description]
🔴 HIGH (15 pts each):
  • [rule_id] [file:line] — [description]
🟡 MEDIUM (10 pts each):
  • [rule_id] [file:line] — [description]
🟢 LOW (5 pts each):
  • [rule_id] [file:line] — [description]

PERMISSION MISMATCHES:
  • [declared vs actual]

VERDICT: ❌ DO NOT INSTALL
═══════════════════════════════════════════════════
```

JSON output (`--json`) is machine-readable for CI.

## CI Integration

See [references/ci-integration.md](references/ci-integration.md) for:

- Pre-commit hook (reject commits that add unaudited skills)
- GitHub Action (audit skills on PR)
- Scheduled re-audit (catch upstream drift)

Quick example — `.github/workflows/audit-skills.yml`:

```yaml
on: [pull_request]
jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: pip install -r skills/skill-auditor/requirements.txt  # if needed
      - run: python3 skills/skill-auditor/scripts/vet.py --batch skills/ --fail-on high
```

## Comparison with skill-vetter

| Feature | skill-vetter (v1.0) | skill-auditor (v1.0) |
|---|---|---|
| Audit method | Manual checklist | Automated scan + manual judgment |
| Red flag rules | 13 | 30+ |
| Risk scoring | 4-tier label | 0-100 numeric + 4-tier label |
| Batch mode | ❌ | ✅ |
| CI integration | ❌ | ✅ (pre-commit, GitHub Action) |
| Permission mismatch check | ❌ | ✅ |
| Trust database | ❌ | ✅ (optional, offline) |
| Output | Markdown template | Markdown + JSON |

## Trust Database

`references/trust-database.md` is an offline, community-maintained list of known-malicious and known-benign skill slugs. Contributions welcome via PR. The script reads it if present and warns on matches.

## Rules of Engagement

- **No skill is worth compromising security.**
- When in doubt, don't install.
- High-score skills from known authors still need review — supply chain attacks target trusted authors.
- Document every audit decision so future-you (and your team) can learn.
- Re-audit after upstream updates — skills drift.

## Files

```
skill-auditor/
├── SKILL.md                # this file
├── scripts/
│   ├── vet.py              # single-skill audit (main entry)
│   ├── batch_vet.py        # batch audit a directory
│   └── score.py            # scoring model (imported by vet.py)
├── references/
│   ├── rules.md            # full rule set (30+ rules)
│   ├── scoring.md          # scoring model explanation
│   ├── ci-integration.md   # CI setup guide
│   └── trust-database.md   # known-malicious / known-benign slugs
├── examples/
│   ├── report-example.md   # sample audit report
│   └── github-action.yml   # ready-to-use GitHub Action
└── tests/
    ├── test_vet.py         # test suite
    ├── test_skill_good/    # benign skill sample (should score low)
    └── test_skill_malicious/  # malicious skill sample (should score high)
```

---

*Paranoia is a feature. Automation is a multiplier.* 🔒🦀
