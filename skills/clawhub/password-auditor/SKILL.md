---
name: password-auditor
description: "Audit password vault exports (Bitwarden, 1Password, KeePass, Chrome, Firefox) for reuse, weakness, staleness, breach exposure, and 2FA gaps without ever storing or transmitting a plaintext password. Use when the user asks to audit passwords, check password strength/reuse, review vault health, or verify whether credentials appeared in breaches."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [security, passwords, audit, breach, privacy, 2fa, vault]
---
# Password Auditor

Audit your password habits **without ever storing or transmitting a password**. Works from an exported CSV/JSON password vault (Bitwarden, 1Password, KeePass, Chrome, Firefox): it analyzes reuse, weakness, staleness, breach exposure, and 2FA availability, then produces an actionable prioritized fix list.

## Overview

`password-auditor` ingests a vault export you already have on disk, computes risk findings locally (no network required except an optional breach check via the k-anonymity HaveIBeenPwned API, which only ever sees the first 5 hex chars of a SHA-1 hash), and emits:

- A terminal risk report with a 0-100 security score
- A prioritized remediation plan (worst offenders first)
- Machine-readable JSON for tracking progress over time
- A self-contained HTML dashboard you can open in any browser

## When to Use

- User says "audit my passwords", "are my passwords safe?", "how bad is my password reuse?"
- After a vault export from any major password manager
- Periodic security hygiene reviews (quarterly recommended)
- Post-breach: check whether specific credentials appeared in known breaches
- Before migrating between password managers (find weak/reused entries first)

**Don't use for:** storing passwords, auto-changing them, or managing a vault — this skill is read-only analysis. It never writes credentials anywhere and its output contains **zero plaintext passwords**.

## How It Works

1. **Parse** the export (auto-detects Bitwarden/1Password/KeePass/Chrome/Firefox CSV shapes, plus generic JSON).
2. **Normalize** each entry: title, username, password, URL, last-modified date, folder/group.
3. **Analyze** five risk dimensions:
   - **Reuse** — identical password across N entries (the #1 account-takeover multiplier)
   - **Weakness** — zxcvbn-style entropy estimation via length, charset, pattern, and common-password lists
   - **Staleness** — passwords untouched for years (pre-date modern breach knowledge)
   - **Breach exposure** — optional HIBP k-anonymity range check (only 5 hash chars leave the machine)
   - **2FA opportunity** — sites known to offer 2FA where the vault has no TOTP secret
4. **Score** — weighted composite 0-100 (higher = safer), with per-dimension sub-scores.
5. **Report** — terminal summary, JSON, and HTML dashboard with the remediation plan.

## Quick Start

```bash
# Analyze a vault export (offline analysis)
python3 scripts/password_auditor.py --vault ~/bitwarden_export.csv

# Include breach checking (only 5-char hash prefixes are sent)
python3 scripts/password_auditor.py --vault ~/export.csv --check-breaches

# Generate full report set (JSON + HTML dashboard)
python3 scripts/password_auditor.py --vault ~/export.csv --json report.json --html dashboard.html

# Create a sample vault to see how it works without touching real data
python3 scripts/password_auditor.py --demo --html demo_dashboard.html
```

## Scoring Model

| Dimension | Weight | What lowers the score |
|---|---|---|
| Reuse | 35% | Same password on multiple sites |
| Weakness | 30% | Short, common, or patterned passwords |
| Breach exposure | 20% | Password appears in known breach corpora |
| Staleness | 10% | Passwords older than ~4 years never rotated |
| 2FA coverage | 5% | No TOTP stored for 2FA-capable critical sites |

Critical sites (email, banking, cloud storage, identity providers) get an importance multiplier — a reused password on your email is far worse than on a forum.

## Common Pitfalls

1. **Leaving the vault export on disk.** Exports are plaintext — delete them (and empty trash) after auditing. The skill reminds you, and `--json` output never contains passwords.
2. **Trusting "strong-looking" passwords.** `Tr0ub4dor&3`-style leetspeak scores weak; entropy estimation catches patterns humans over-trust.
3. **Auditing once.** Re-run quarterly and diff JSON reports (`--json`) to prove habits improve.
4. **Skipping `--check-breaches` over privacy fears.** The HIBP API uses k-anonymity: it receives only the first 5 characters of the SHA-1 hash — mathematically cannot reconstruct your password.
5. **Fixing low-value accounts first.** Follow the remediation plan's priority order: reused + breached + critical-site credentials before anything else.

## Verification Checklist

- [ ] Report generated and shows entry count matching your vault
- [ ] No password appears in any output file (JSON/HTML contain hashes/metadata only)
- [ ] Breach check (if used) completed with per-entry suffix counts
- [ ] Vault export deleted from disk after the audit
- [ ] Remediation plan's top-5 items scheduled in your password manager

## One-Shot Recipes

**Quarterly audit with trend tracking**
```bash
python3 scripts/password_auditor.py --vault export.csv --json audit_$(date +%Y%m%d).json --html audit_$(date +%Y%m%d).html
python3 scripts/password_auditor.py --compare audit_20260501.json audit_20260801.json
```

**Post-breach panic check**
```bash
python3 scripts/password_auditor.py --vault export.csv --check-breaches --min-breach-count 1
```

## References

- `references/risk-model.md` — full scoring methodology, entropy math, site criticality tiers
- `references/export-formats.md` — field mappings for every supported vault export
