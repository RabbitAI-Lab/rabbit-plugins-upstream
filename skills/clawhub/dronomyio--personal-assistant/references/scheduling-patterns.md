# Scheduling patterns

These patterns assume a cron-like scheduler that runs a task body on a
schedule and reports a result. Adapt the frontmatter to your platform;
the body conventions are what matter.

## Job definition shape

```yaml
id: <kebab-case-id>          # stable; used for status keys and logs
title: <Human-readable title>
enabled: true
mode: task
schedule:
  kind: daily               # or: interval (every: 30m), weekly, runonce
  timezone: <IANA timezone>  # market jobs anchor to market tz
  time: "<HH:MM:SS>"
timeout_secs: 1800
delivery: []                # chat target(s), or empty for silent
```

Then a markdown body of numbered steps (see `templates/brief-cron.md`).

## Cadence patterns that work

- **Market briefs:** pre-market, hourly intraday, close. Hourly jobs all
  share one body template with only the focus line changed
  ("what moved since the last run").
- **Daily digests:** one morning job that reads all `latest.json` files
  and composes a single Feed/dashboard post.
- **Ingest polling:** `interval: 30m` — poll an inbox, process new items,
  mark done. Quiet on success, report failures only.
- **Site checks:** daily ping (HTTP status + latency); weekly deep audit
  (link crawl). Alert only on state *change*, not every run.
- **Dashboard refresh:** one daily job that re-reads all flat files into
  the dashboard. Manual refresh available for "I want it now".

## The quiet-unless-significant rule

Every job body ends with explicit notification conditions, e.g.:

> Chat: message the user ONLY if something is genuinely significant
> (a watched name moved >5%, major market-wide event). Otherwise end
> quietly with a one-line verdict.

This is the single most important convention. Without it, 20+ daily jobs
become notification spam and the user stops reading all of them.

## Status tracking

Each job updates one shared `status.json`:

```json
{
  "<job-id>": {
    "last_run": "2026-01-01T12:00:00Z",
    "result": "ok",
    "summary": "67/67 resolved, 5 movers"
  }
}
```

Read-modify-write, preserving other keys. Dashboards surface `last_run`
as "last updated" stamps so staleness is visible.

## Failure handling

- Collection failures stay visible: a run that can't reach its source
  records `result: failed` with the error — it never writes a fake
  zero-movers file.
- Transient throttle (e.g. YouTube): wait 10 minutes, retry once, then
  record the failure and end quietly. Never fabricate the brief.
- A job that fails twice in a row earns a user-facing message; a single
  failure is just logged.
