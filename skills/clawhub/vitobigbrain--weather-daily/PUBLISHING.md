# Publishing this skill

The `publish`/`inspect` block below is verified against
`clawhub skill publish --help` on an actual CLI install, v0.23.1 — not
just the docs. The `hide` / `rescan` / `undelete` block further down is
still sourced from docs.openclaw.ai and has **not** been confirmed
against a real `--help` output on this machine. Docs and the shipped
CLI have already disagreed once in this project (a documented
`--clawscan-note` flag that doesn't exist in v0.23.1's `skill publish`)
— so before you rely on `hide`/`rescan`/`undelete` in a real incident,
run `clawhub skill --help` (or `clawhub --help` in full) yourself and
confirm the exact flags first.

```bash
# one-time setup
npm i -g clawhub@latest   # if `clawhub --cli-version` looks stale after
                           # this, check `which -a clawhub` for a second,
                           # older install shadowing it on PATH
clawhub login              # opens a browser for OAuth; use --device on a headless box
clawhub whoami              # confirms the stored token

# publish a new version from this folder — verified flags only
cd weather-daily
clawhub skill publish . --version 1.2.4 \
  --changelog "See CHANGELOG.md for the full 1.2.4 entry." \
  --tags weather,obsidian,daily-brief \
  --dry-run                # preview only — nothing is created yet

# drop --dry-run once the preview looks right
clawhub skill publish . --version 1.2.4 \
  --changelog "See CHANGELOG.md for the full 1.2.4 entry." \
  --tags weather,obsidian,daily-brief

# look at what got published without installing it
clawhub inspect weather-daily --files
```

```bash
# NOT independently verified against this machine's CLI — confirm with
# `clawhub skill --help` before you actually need these in an incident.

# if a release ever gets flagged and you believe it's a false positive
clawhub skill rescan weather-daily

# emergency takedown of a specific version (soft delete, reversible)
clawhub skill hide weather-daily --reason "<why>"
clawhub skill undelete weather-daily   # if it turns out to be a false alarm
```

Notes:
- Publishing to ClawHub means the release is licensed `MIT-0` — this is
  enforced by ClawHub for every skill, not something you configure per
  release. Don't add a conflicting `license:` field to `SKILL.md`.
- `--dry-run` runs the full validation (owner permissions, slug,
  version, file limits) without creating a release — this is the real
  equivalent of a "lint" step, confirmed via `--help`, not a separate
  `lint` command.
- After a real publish, the release starts in `pending`, then automated
  security analysis moves it to `clean` (installable) or
  `suspicious`/`malicious` (held, with a notification to the owner).
