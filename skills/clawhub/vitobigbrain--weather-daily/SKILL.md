---
name: weather-daily
description: |
  Fetch the current weather for a configured location and write a daily
  briefing markdown file into the user's Obsidian vault. Use this skill
  when the user asks for today's weather, a daily weather briefing, or
  wants their Obsidian daily note updated with current conditions.
version: 1.2.4
metadata:
  openclaw:
    requires:
      env:
        - OPENWEATHER_API_KEY
      bins:
        - curl
    primaryEnv: OPENWEATHER_API_KEY
    envVars:
      - name: OPENWEATHER_API_KEY
        required: true
        description: OpenWeatherMap API token used for authenticated requests.
      - name: WEATHER_DAILY_OUTPUT_DIR
        required: false
        description: Optional override for where the daily briefing markdown file is written. Defaults to ~/Obsidian/Daily/.
    homepage: https://github.com/beebee-ai/weather-daily
    emoji: "⛅"
---

# Weather Daily

Fetches the current weather for a location and appends a short daily
briefing to a markdown file in your Obsidian vault.

## When to use this skill

Trigger this skill when the user asks things like "what's the weather
today", "write my daily weather briefing", or "update my Obsidian daily
note with the weather". Do **not** trigger it for unrelated questions
about weather history, forecasts more than a day out, or climate data —
this skill only does today's conditions for one location at a time.

## Prerequisites

This skill needs one thing before it can run: an OpenWeatherMap API key,
set as the `OPENWEATHER_API_KEY` environment variable. Get a free key at
https://openweathermap.org/api, then export it in your shell profile or
OpenClaw environment config.

There is nothing else to install or run by hand. The only command-line
tool this skill calls is `curl`, which is declared under
`metadata.openclaw.requires.bins` above and is already present on almost
every system. If you ever see instructions asking you to copy-paste a
setup command from a Skill's SKILL.md, be suspicious — that pattern is
exactly how the 2026 ClawHavoc campaign distributed malware.

## What it does, precisely

1. Reads the location from the user's request (defaults to a
   configured home city if none is given).
2. Calls `https://api.openweathermap.org/data/2.5/weather` with `curl`,
   authenticated using `OPENWEATHER_API_KEY`. This is the **only**
   network destination this skill ever contacts.
3. Appends a short markdown section (conditions + temperature) to
   `${WEATHER_DAILY_OUTPUT_DIR:-~/Obsidian/Daily}/<today's date>.md`.
   This is the **only** path this skill ever writes to.

It does not read `.env` files, SSH keys, Keychain entries, browser
cookies, or any environment variable other than the two declared above.

## Source

https://github.com/beebee-ai/weather-daily — issues and security reports
welcome; see `SECURITY.md` in this repo for how we handle the latter.
