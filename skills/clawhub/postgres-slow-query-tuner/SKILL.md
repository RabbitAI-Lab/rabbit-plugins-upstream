---
name: postgres-slow-query-tuner
description: >
  Interpret EXPLAIN ANALYZE output and suggest indexes or query rewrites for
  PostgreSQL. Use when a query is slow in staging or production.
metadata: {"clawdbot":{"emoji":"🐘","requires":{"bins":["psql"]}}}
---

# Cron Expression Coach
The skill helps with improving the query performance for postgresql.

## Purpose / Overview
Review and explain how the given query can be optimized.

## When to Use
- Optimizing a long query.

## Usage / Instructions
1. Ask what they want to schedule in natural language (cadence, timezone notes).
2. Confirm which dialect they need: classic 5-field crontab, or mention if they
   use a 6-field (seconds) system — default to 5 fields (`min hour dom mon dow`).
3. Draft a candidate expression and decode it field-by-field in a table-like list.
4. Provide at least three upcoming example run times **qualitatively**
   (e.g. "next Monday 09:30") without claiming a live timezone database.
5. Validate common mistakes:
   - DOW vs DOM both constrained (ask if they meant OR semantics)
   - Using `*/0` or out-of-range numbers
   - Confusing 0-Sunday vs 1-Monday conventions — state your assumption
6. For ranges and lists (`1-5`, `1,15`), restate in prose.
7. If they need "every N hours during business hours," build it with explicit
   hour lists rather than opaque tricks.
8. Offer a safe comment line for the crontab: `# purpose — owner — expression`.
9. Warn about DST cautions when scheduling near 2am local time.
10. Do not connect to PostgreSQL or read `EXPLAIN` plans. If the user pastes
    SQL, politely redirect: this skill only handles cron.
11. Provide one alternative expression when two interpretations are plausible.
12. End with a copy-paste ready crontab line plus the prose summary.
11. Keep answers structured with short headings so the user can skim.
12. If information is missing, ask at most two clarifying questions before guessing.
13. Prefer concrete commands or checklists the user can copy.
14. Call out assumptions explicitly when the environment is unknown.
15. Refuse to invent tool output you did not see; ask for a fresh paste instead.
16. When offering optional follow-ups, keep them clearly optional.
17. Stay within this skill's scope; suggest a different task type if the request drifts.
18. End with a brief "done when" criterion so the user knows success.
19. If user gives a postgresql query, then try to optimize it for better performance.


## Requirements / Dependencies

## Limitations / Caveats
Does not execute against a real calendar. Platform cron variants differ slightly.

## Security / Permissions
DB credentials may be needed.

## Description

Interpret EXPLAIN ANALYZE output and suggest indexes or query rewrites for PostgreSQL.

## License or terms

MIT

## Use case

Intended for practitioners who need help with: Interpret EXPLAIN ANALYZE output and suggest indexes or query rewrites for PostgreSQL.

## Risks and mitigations

## References

- PostgreSQL documentation: https://www.postgresql.org/docs/

## Ethical considerations

Illegal use of this skill is not allowed. The publisher will not be accountable for outcomes arising from unlawful use under country or international law. Prohibited examples include breaking into accounts without authorization, deploying ransomware, and trafficking in stolen personal data. Misuse against third-party systems without authorization is illegal.
