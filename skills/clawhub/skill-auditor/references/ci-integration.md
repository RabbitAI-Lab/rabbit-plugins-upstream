# CI Integration

Three integration patterns. Pick what fits your workflow.

## 1. Pre-commit Hook (local)

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: local
    hooks:
      - id: skill-auditor
        name: Audit agent skills before commit
        entry: python3 skills/skill-auditor/scripts/vet.py
        language: system
        pass_filenames: true
        args: [--fail-on, high]
        files: ^skills/.+/SKILL\.md$
```

Effect: any commit that touches a `SKILL.md` triggers an audit. If the skill scores HIGH or above, the commit is rejected.

## 2. GitHub Action (PR gate)

`.github/workflows/audit-skills.yml`:

```yaml
name: Audit Agent Skills

on:
  pull_request:
    paths:
      - 'skills/**'
  schedule:
    # Re-audit every Monday for upstream drift
    - cron: '0 3 * * 1'

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Audit skills
        run: |
          python3 skills/skill-auditor/scripts/vet.py --batch skills/ --fail-on high
      - name: Upload audit reports
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: skill-audit-reports
          path: |
            skills/
```

Effect:
- Every PR touching `skills/` runs the audit.
- If any skill scores HIGH+, the PR check fails.
- Audit reports are uploaded as artifacts for review.
- Weekly cron re-audits to catch upstream drift (skills installed from ClawHub that get updated upstream).

## 3. CI Script (any CI)

For GitLab CI, CircleCI, etc:

```bash
#!/usr/bin/env bash
set -e

# Audit all skills; fail if any reach HIGH
python3 skills/skill-auditor/scripts/vet.py --batch skills/ --fail-on high

# Optional: output JSON for programmatic processing
python3 skills/skill-auditor/scripts/vet.py --batch skills/ --json > audit-report.json
```

## Thresholds

`--fail-on` accepts: `low | medium | high | critical`

| Threshold | Score | Strictness |
|---|---|---|
| `low` | ≥16 | Reject anything not perfectly clean. Recommended for security-sensitive orgs. |
| `medium` | ≥41 | Reject anything clearly suspicious. Balanced default. |
| `high` | ≥71 | Reject only egregious cases. Permissive. |
| `critical` | =100 | Only fail on extreme malware. Mostly for reporting, not blocking. |

## Output Formats for CI

- **Markdown (default)**: human-readable, good for CI logs.
- **JSON (`--json`)**: machine-readable, parse in your CI to extract specific rules, post comments on the PR, etc.
- **Score only (`--score`)**: one line per skill, easy to diff over time.

```bash
# Track score drift week-over-week
python3 skills/skill-auditor/scripts/vet.py --batch skills/ --score > this-week.txt
diff last-week.txt this-week.txt
```

## Customizing the Allowlist

For project-specific trusted domains, create `references/trust-database.md` and list them. The script reads it if present. Example:

```markdown
## Project-specific trusted domains

- internal.corp.example.com
- api.internal.tooling.dev
```

Or edit `DEFAULT_ALLOWLIST` in `scripts/vet.py` directly.

## Running on ClawHub-installed skills

To audit everything in `~/.openclaw/skills/`:

```bash
python3 skills/skill-auditor/scripts/vet.py --batch ~/.openclaw/skills/ --fail-on high
```

Recommended cadence:
- After every `clawhub install`
- Weekly (skills drift upstream)
- After OpenClaw version upgrades (sandbox rules may change)
