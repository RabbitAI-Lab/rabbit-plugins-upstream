---
name: deadline-radar
description: "Upcoming course and project deadlines from deadlines.md, with each repo's uncommitted changes and last commit."
metadata: { "openclaw": { "requires": { "bins": ["node", "git"] } } }
---

# deadline-radar

Use for "what's due this week?", deadline reminders in briefings and recaps, and the warning
"assignment due in 3 days, your repo has uncommitted changes".

Run the script with the `exec` tool from the workspace (it only reads files and runs `git status` / `git log`; no
network):

```bash
node {baseDir}/scripts/deadline_radar.mjs --file deadlines.md --root . --days 7
```

Options: `--days N` (look-ahead, default 7), `--alert-days N` (warn window, default 3), `--tz <IANA zone>`
(default `America/Los_Angeles`), `--root DIR` (repo paths in deadlines.md are relative to it; repos outside it are
ignored).

## deadlines.md

One deadline per line; the repo part is optional:

```
- 2026-11-13 23:59 | Project Lantern | Milestone 4: evaluation results | repo: projects/lantern
- every Thursday 23:59 | AGT 510 | Weekly problem set |
```

`<when>` is `YYYY-MM-DD HH:MM` or `every <Weekday> HH:MM`, in the `--tz` time zone. A sample is in
`{baseDir}/example/deadlines.md`. If the workspace has no deadlines.md, say so and offer to start one from the
sample.

## Reporting

The script prints JSON: `deadlines` (soonest first, with `due`, `daysLeft` and, when a repo is linked, its
`uncommittedFiles` and `lastCommit`) and `alerts`.

- If `alerts` is not empty, lead with it: something is due within the warn window and its repo has uncommitted
  changes. Suggest committing and pushing.
- Then list the deadlines, one line each: what, when, days left.
- Use only what the script returns. If a repo shows `found: false`, say the repo path wasn't found.
