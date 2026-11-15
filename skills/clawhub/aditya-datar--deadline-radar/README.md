# deadline-radar (OpenClaw skill)

Flags deadlines that are **at risk**: due within 3 days while the related repo has
uncommitted changes, unpushed commits, or no push to GitHub in 48 hours.

- Zero dependencies (Node ≥ 18), read-only (never writes files or touches repos).
- Works as an agent skill ("what's due?") and as a quiet command automation:
  `node {baseDir}/scripts/radar.mjs --alert` prints `NO_REPLY` when nothing is at risk.

## Install

```bash
openclaw skills install @OWNER/deadline-radar
```

## Example

```
⏳ Deadline risk
⚠ A3 Personal Assistant — final submission (CSCI 599) — due in 2 days: no push in 61h
```

Author: Aditya Datar (CSCI 599, Fall 2026). License: MIT.
