# Skill Auditor 🔒

Automated security audit for AI agent skills. Superset of [skill-vetter](https://clawhub.ai/spclaudehome/skill-vetter) with automated scanning, 0-100 risk scoring, batch mode, and CI integration.

[![Tests](https://img.shields.io/badge/tests-15%2F15%20passing-brightgreen)](tests/test_vet.py)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

## Why

The OpenClaw/ClawHub ecosystem has 67,000+ skills (2026-07). Community articles and 51CTO security reporting show that skills can contain backdoors, credential exfiltration, and RCE patterns. Existing tools like `skill-vetter` provide only a **manual checklist** — fine for one skill, doesn't scale.

Skill Auditor automates the same review with 30+ regex-based rules, a quantitative 0-100 risk score, batch mode for auditing an entire `skills/` directory, and CI integration (pre-commit / GitHub Action) so skills are audited on every PR.

## Quick Start

```bash
# Audit a single skill folder
python3 scripts/vet.py path/to/some-skill

# Audit with JSON output
python3 scripts/vet.py path/to/some-skill --json

# Audit all skills in a directory
python3 scripts/vet.py --batch path/to/skills/

# CI mode: exit non-zero if any skill scores HIGH (>=71)
python3 scripts/vet.py --batch path/to/skills/ --fail-on high
```

## Output Example

```
SKILL AUDIT REPORT
═══════════════════════════════════════════════════
Skill:    evil-todo
Version:  0.0.1
───────────────────────────────────────────────────
RISK SCORE: 100/100  →  ⛔ EXTREME

⛔ CRITICAL:
  • [CRED_SSH] SKILL.md:17 — Reads ~/.ssh (SSH private keys)
  • [CRED_AWS] SKILL.md:20 — Reads ~/.aws/credentials
  • [RCE_PICKLE] SKILL.md:34 — pickle.loads on external data

VERDICT: ❌ DO NOT INSTALL
═══════════════════════════════════════════════════
```

## Rules

30+ red-flag patterns in 4 severity tiers. See [references/rules.md](references/rules.md) for the full catalog.

| Tier | Weight | Examples |
|---|---|---|
| CRITICAL | 25 | SSH/AWS/keychain access, eval/pickle RCE, identity file manipulation |
| HIGH | 15 | curl\|sh, raw-IP URLs, pastebin uploads, shell=True, chmod 777 |
| MEDIUM | 10 | http:// (no TLS), tor, undeclared env vars, broad OAuth scopes |
| LOW | 5 | missing frontmatter/license, hardcoded paths, long sleeps |

Score is additive, capped at 100. See [references/scoring.md](references/scoring.md).

## Comparison with skill-vetter

| Feature | skill-vetter | skill-auditor |
|---|---|---|
| Audit method | Manual checklist | Automated scan + human judgment |
| Red flag rules | 13 | 30+ |
| Risk scoring | 4-tier label | 0-100 numeric + 4-tier label |
| Batch mode | ❌ | ✅ |
| CI integration | ❌ | ✅ (pre-commit, GitHub Action) |
| Permission mismatch check | ❌ | ✅ |
| Trust database | ❌ | ✅ (offline, community-maintained) |
| Output | Markdown template | Markdown + JSON |

skill-auditor is a **superset**, not a replacement. The manual judgment steps (source check, trust hierarchy, final decision) from skill-vetter are preserved as Steps 1, 5, 6 of the 6-step protocol.

## Installation

### Via ClawHub (when published)

```bash
clawhub install skill-auditor
```

### Manual

```bash
git clone <this-repo> ~/.openclaw/skills/skill-auditor
```

### As a CI dependency

Add as a git submodule or just vendor the `scripts/` directory:

```bash
git submodule add <this-repo> skills/skill-auditor
```

## Tests

```bash
python3 tests/test_vet.py
# Ran 15 tests in 0.002s — OK
```

Test cases include a benign skill sample (should score LOW) and a malicious skill sample (should score EXTREME).

## Documentation

- [SKILL.md](SKILL.md) — main skill file (loaded by OpenClaw)
- [references/rules.md](references/rules.md) — full rule catalog
- [references/scoring.md](references/scoring.md) — scoring model rationale
- [references/ci-integration.md](references/ci-integration.md) — CI setup guide
- [references/trust-database.md](references/trust-database.md) — known-malicious / known-benign skills
- [examples/github-action.yml](examples/github-action.yml) — ready-to-use GitHub Action
- [examples/report-example.md](examples/report-example.md) — sample audit report

## Limitations

- **Static analysis only**: pattern-matches on file content, does not run the skill or trace data flow.
- **Allowlist is opinionated**: domains not in `DEFAULT_ALLOWLIST` trigger HIGH. Edit per project.
- **No semantic understanding**: legitimate use of `~/.aws/credentials` (e.g. an AWS skill) will trigger `CRED_AWS`. Use Step 5 (human judgment) for context.
- **Runtime monitoring is a separate concern**: see the planned `skill-runtime-guard` companion skill.

## Roadmap

- [ ] Per-rule occurrence counting (`--strict` flag)
- [ ] Confidence scores for fuzzy regex matches
- [ ] Online lookups (ClawHub download count, last-updated) for Step 1
- [ ] SBOM-style declared-permissions matching
- [ ] Diff mode (`--compare last-week.txt`) for tracking score drift

## License

MIT. See [LICENSE](LICENSE).

## Acknowledgments

- [skill-vetter](https://clawhub.ai/spclaudehome/skill-vetter) by spclaudehome — original manual checklist protocol
- [SkillScan](https://clawhub.ai/tokauthai/skillscan) by tokauthai — alternative security gate
- 51CTO's [ClawHub security reporting](https://www.51cto.com/article/847901.html) — motivation for this skill

---

*Paranoia is a feature. Automation is a multiplier.* 🔒🦀
