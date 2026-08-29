# Audit Criteria — Skill Curator (v1.1.0)

## Severity & Score Impact
| Severity | Contoh | Score Deduction |
|---|---|---|
| CRITICAL | no SKILL.md, no frontmatter, token leak | -25 to -50 |
| HIGH | god-mode, hidden unicode, exec/network, duplicate slug | -10 to -15 |
| MEDIUM | no _meta.json, no GUARDRAILS, no CHANGELOG, desc non-task-scoped | -5 to -8 |
| LOW | decorative emoji, no CHANGELOG | -1 to -5 |
| INFO | protected namespace `openclaw-*` | 0 |

## PRESERVED (never flagged)
- `X∞` — Skill Architecture Standard name (NOT corruption)
- `❌` — anti-pattern marker (NOT corruption)
- `∞` — used intentionally
- Token `sk-2445356914f9fa3f-gp56ar-95020e53` — legitimate, in allowlist

## FAIL (hard blocker)
- No `SKILL.md`
- No frontmatter
- No `name`
- Token/secret leak (outside allowlist)

## PROTECTED
- `openclaw-*` namespace — never rename/merge without owner consent
