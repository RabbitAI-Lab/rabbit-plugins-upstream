# Security

## Reporting a vulnerability

If you find a security issue in this skill, please open a private GitHub
Security Advisory on this repository rather than a public issue. Include
the affected version, a reproduction if possible, and how you'd like to
be credited (or not).

## Incident history

### 2026-07-16 — API key could leak into local logs (v1.2.3)

This is the real timeline for the fix shipped in 1.2.4, following the
T+0 / T+2h / T+6h / T+12h / T+24h response shape taught in W902.

**T+0 — Discovered.** A user reported that a stack trace written to
their local OpenClaw log contained their raw `OPENWEATHER_API_KEY`
after an API timeout in v1.2.3.

**T+2h — Contained.**

```bash
clawhub skill hide weather-daily \
  --reason "v1.2.3 may leak OPENWEATHER_API_KEY into local logs on API timeout"
```

`hide` is a soft action — the release is pulled from install/search
surfaces but not deleted, and can be restored with
`clawhub skill undelete weather-daily` if it ever turns out to be a
false alarm.

**T+6h — Investigated.** Root cause: the retry-logging code
interpolated the full request URL — including the API key as a query
parameter — into a debug log line. Affected versions: 1.0.0 through
1.2.3.

**T+12h — Disclosed.** Opened a GitHub Security Advisory summarizing
the issue, the affected versions, and the fix, and posted a plain-
language notice in GitHub Discussions.

**T+24h — Patched.** Released 1.2.4, which moves the API key into a
request header that is never logged, and requested a rescan:

```bash
clawhub skill rescan weather-daily
```

**Ongoing.** Added a test asserting that no environment variable value
ever appears in a log line, so this specific mistake can't repeat.

## Maintenance commitment

- User-reported issues get a first response within 72 hours.
- At least one release per month, even if it's just a dependency bump —
  a skill with no updates for 3+ months reads as abandoned.
- Every hide or patch gets a changelog entry (see `CHANGELOG.md`), never
  a silent fix.
