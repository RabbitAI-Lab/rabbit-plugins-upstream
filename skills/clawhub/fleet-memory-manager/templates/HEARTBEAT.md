# Local memory-health check

This file does not authorize scheduled work. Enable a schedule only after the
user explicitly approves the schedule, timezone, files, and review workflow.

When an approved local check runs:

1. Count daily notes older than 30 days and propose them for review or deletion.
2. Flag durable entries whose review date has passed.
3. Check whether `memory/CONSOLIDATION_CANDIDATES.md` is awaiting review.
4. Report only file names, counts, and review dates. Do not include private
   memory contents in notifications.
5. Do not access external services or send messages unless separately approved.

Consolidation may write proposed changes only to
`memory/CONSOLIDATION_CANDIDATES.md`. It must not edit `MEMORY.md` or `USER.md`.

If no review is needed, stay silent.
