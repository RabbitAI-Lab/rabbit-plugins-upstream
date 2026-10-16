# Architecture: Collect → Brief → Dashboard → Feed

The personal assistant is a set of small, independent loops that share a
convention: **keyless data in, flat files out, quiet unless significant.**

```
  SOURCES                    BRIEFS                    SURFACES
┌──────────┐                ┌──────────┐              ┌──────────────┐
│ Yahoo    │──tickers──────▶│ brief_   │──latest.json─▶│ Dashboard    │
│ Finance  │  watchlist.md │ engine.py │  movers+news │ (tabs)       │
│ (keyless)│               └──────────┘              └──────────────┘
└──────────┘                ┌──────────┐              ┌──────────────┐
│ Google   │──RSS──────────▶│ market_  │──numbers+   ─▶│ Feed digest  │
│ News RSS │               │ brief.py  │  headlines  │ (daily post) │
│ (keyless)│               └──────────┘              └──────────────┘
└──────────┘                ┌──────────┐              ┌──────────────┐
│ YouTube  │──yt-dlp───────▶│ surveil- │──transcript─▶│ Strategy     │
│ captions │  captions     │ lance_   │  + ideas     │ (regime call)│
│          │               │ fetch.py  │              └──────────────┘
└──────────┘               └──────────┘
┌──────────┐                ┌──────────┐              ┌──────────────┐
│ Your own │──crawl────────▶│ check_   │──per-site   ─▶│ Ventures/    │
│ sites    │  polite       │ links.py  │  JSON       │ health tab   │
└──────────┘               └──────────┘              └──────────────┘
┌──────────┐                ┌──────────┐              ┌──────────────┐
│ Inbox    │──poll─────────▶│ ingest   │──note.md +  ─▶│ Library tab  │
│ (links,  │  every 30m    │ worker    │  audio.mp3   │ (read+listen)│
│ files)   │               │ (agent)   │              └──────────────┘
└──────────┘               └──────────┘
```

## Design rules

1. **Keyless sources first.** Yahoo Finance chart API and Google News RSS
   need no keys. Add keyed sources (broker APIs, paid data) only behind
   explicit per-source flags.
2. **Flat files as the contract.** Every script writes timestamped JSON +
   a `latest.json` pointer. Downstream readers only ever read `latest.*`.
   No databases required for the core loop.
3. **Quiet unless significant.** Scheduled runs message the user only on
   genuine thresholds (e.g. a watched name moves >5%, a site goes down).
   Everything else is a one-line verdict in the run log.
4. **Status file, not memory.** A single `status.json` holds
   `{last_run, result, summary}` per job. Dashboards read it for
   "last updated" stamps. Never invent a run — if the job didn't run,
   the stamp says so.
5. **Personal-consumption boundaries.** Anything derived from licensed or
   login-walled sources (e.g. TV transcripts) stays local: never synced
   to public storage, never quoted at length.

## Optional extensions (not bundled)

- **Talk/event capture** with photo/video/voice attachments and local
  transcription (needs device media + a Whisper-class model).
- **Strategy writer**: a daily agent run that reads the briefs plus your
  holdings and writes a regime/positioning commentary. Keep it clearly
  separated from the data layer — commentary is opinion, briefs are data.
- **Voice control**: a spoken interface over the same job operations
  (run-now, reschedule, pause). The jobs don't change; only the trigger does.
