# Dashboard pattern (build reference)

The reference implementation is a private dashboard ("Command Center")
with one tab per concern. The dashboard app itself can't be bundled in
a skill — rebuild it on your own stack using this structure.

## Tab structure

1. **Markets** — watchlist movers per market (ticker, price, % change,
   volume vs average, driver headlines). Sortable; per-stock research
   notes persist. A "strategist's take" section can sit at the top as
   the lead section rather than a separate tab.
2. **Ideas/media brief** — timestamped takes from the transcript fetcher
   (guest, firm, 1–2 line idea, video timestamp). Personal-consumption
   content stays in this private surface.
3. **Ventures / site health** — per-site status from the link checker:
   last audit date, broken-link count, uptime ping. Broken-first ordering.
4. **Library / reading desk** — ingested items (URL, video, text, image)
   each with: written summary, "why you should care", spoken-word audio
   with playback, and a persistent comments thread.
5. **Talks / events** — event log with contacts, follow-up flags, and
   photo/video/voice attachments (optional extension).
6. **Strategy** — periodic regime + positioning commentary per market
   (regime label, factors with evidence, tailwind/headwind/watch tickers,
   linked drivers, history archive). Written by a scheduled agent run,
   clearly separated from the data tabs.

## Data wiring

- The dashboard never computes; it only reads the flat files the jobs
  write (`latest.json`, per-site reports, notes). All computation lives
  in the scripts / scheduled runs.
- Every tab shows a **"last updated" stamp** sourced from `status.json`
  (per-job `last_run`), plus one overall "last dashboard refresh" stamp.
  Staleness must be visible — a dashboard that silently shows old data
  is worse than no dashboard.
- One scheduled **refresh** job re-reads all files daily; a manual
  refresh control covers "I want it now".

## What not to copy

- Don't seed demo tickers, notes, or commentary that look like the
  user's real data. Empty states must be honest ("no briefs yet —
  run the engine first").
- Don't put licensed/walled content (transcripts, full articles) anywhere
  reachable beyond the user's private devices.
