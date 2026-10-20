---
id: <job-id>
title: <Human-readable title>
enabled: true
mode: task
schedule:
  kind: daily
  timezone: <IANA timezone, e.g. America/New_York>
  time: "<HH:MM:SS>"
timeout_secs: 1800
delivery: []
---

<One-line description of this run.>

1. Run: python3 <path-to>/brief_engine.py --market <us|india>
   Writes <out-dir>/<market>/<STAMP>.json and latest.json (movers by
   % change and volume spike).
2. News scan (2-4 searches, news vertical). Focus for this run: <intraday|pre-market|close — what moved and why>.
3. Write analysis to <out-dir>/<market>/<STAMP>.analysis.md: for each
   significant mover — what moved, the news behind it, and why it matters.
   Keep it tight, no filler.
4. Update status file: read <status.json>, set key "<status_key>" to
   {last_run: <now ISO UTC>, result: ok|failed, summary: "<short>"},
   preserving all other keys.
5. Chat: message the user ONLY if something is genuinely significant
   (a watched name moved >5%, major market-wide event). Otherwise end
   quietly with a one-line verdict.

Notes:
- Keep `delivery` empty (or your own chat target) — never ship another
  person's chat UUIDs in a shared skill.
- Body steps reference YOUR paths; adjust <...> placeholders on install.
