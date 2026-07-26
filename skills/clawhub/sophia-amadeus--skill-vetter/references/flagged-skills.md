# Flagged Skills — Known Problematic Skills

Skills to approach with caution or avoid.

## High Confidence Rejections

| Skill | Reason |
|-------|--------|
| `fiverr-gig-automation` | Security flag: plaintext credential storage (FIVERR_EMAIL, FIVERR_PASSWORD), Selenium scraping, Fiverr ToS violations. Disabled on our system. |
| `freelance-proposal-engine` | Paired with fiverr-gig-automation, same security concerns. |

## Context-Dependent Caution

| Skill | Reason |
|-------|--------|
| `openclaw-deck-tracker` | New skill (v0.1.1), just uploaded. Not enough history to determine stability. |
| `claw-arena` | New entry, unknown community reception. |

## General Caution Rules

- Skills with < 10 downloads and no version history: approach carefully
- Skills with no description or < 50 word description: likely low-effort
- Skills last updated > 1 year ago: potentially abandoned, might have unpatched vulnerabilities
- Skills with `eval`, `exec`, or `rm -rf` in scripts without documentation: reject

## How to Update This File

When a new skill is flagged:
1. Add to appropriate section with reason
2. Document evidence (what specifically triggered the flag)
3. Note date and context

When a skill is cleared after review:
1. Move from rejection list to "cleared" note
2. Record what was checked and confirmed safe