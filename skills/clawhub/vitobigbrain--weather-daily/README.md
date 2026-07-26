# weather-daily

An OpenClaw Skill that fetches today's weather and appends a short
daily briefing to a markdown file in your Obsidian vault.

## Install

```bash
clawhub install weather-daily
```

## Configuration

Set `OPENWEATHER_API_KEY` before use — get a free key at
https://openweathermap.org/api. See `SKILL.md` for the full list of
declared requirements.

## What it needs, and why

This skill declares exactly what it uses in `SKILL.md`'s
`metadata.openclaw` block, nothing more:

- `curl` — the only command-line tool it calls
- `OPENWEATHER_API_KEY` — the only environment variable it reads

It writes only to `~/Obsidian/Daily/*.md` (or `WEATHER_DAILY_OUTPUT_DIR`
if set) and makes network requests only to `api.openweathermap.org`.
Nothing else. `scripts/weather_daily.sh` is the entire implementation —
short enough to read end to end before you trust it.

## Versioning & security

See `CHANGELOG.md` for version history (including a real security-hide
example) and `SECURITY.md` for how issues are reported, triaged, and
disclosed.

## Publishing

See `PUBLISHING.md` for the exact `clawhub` CLI commands used to ship
this skill.

## License

`MIT-0` (see `LICENSE`) — required by ClawHub for every published
skill; there is no per-skill license override.
