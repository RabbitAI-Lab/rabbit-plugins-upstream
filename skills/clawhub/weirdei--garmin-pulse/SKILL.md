---
name: garmin-pulse
version: 2.2.0
homepage: https://github.com/weirdei/garmin-pulse
license: MIT
description: Syncs daily health and fitness data from Garmin Connect into markdown files. Sleep, activity, heart rate, stress, body battery, HRV, SpO2, weight, hydration, training status, endurance/hill scores, race predictions.
disable-model-invocation: true
metadata: {"openclaw":{"emoji":"💪","requires":{"bins":["uv"]},"install":[{"id":"uv","kind":"brew","formula":"uv","bins":["uv"],"label":"Install uv via Homebrew"}]}}
---

# Garmin Pulse

This skill syncs daily health data from Garmin Connect into markdown files that the agent reads locally.

## Setup

Authentication is required before the first sync. This only needs to happen once — tokens are cached for approximately one year.

If the sync command fails with "No cached tokens found", tell the user to run the setup command in their terminal:

```bash
uv run {baseDir}/scripts/sync_garmin.py --setup --email you@example.com
```

The password is prompted interactively via `getpass` — it is never echoed to screen, stored in shell history, or passed as a command argument. If Garmin asks for an MFA code, the script prompts for it. On success the user will see `Success! Tokens cached in ~/.garminconnect`. After that, all syncs use cached tokens only — no credentials are needed.

Do not ask the user for their password in chat and do not pass passwords as command-line arguments or via stdin piping, as these methods can expose credentials in process listings or conversation history.

## Syncing Data

Sync today's data:

```bash
uv run {baseDir}/scripts/sync_garmin.py
```

Sync a specific date:

```bash
uv run {baseDir}/scripts/sync_garmin.py --date 2026-02-07
```

Sync the last N days:

```bash
uv run {baseDir}/scripts/sync_garmin.py --days 7
```

## Reading Health Data

Health files are stored OUTSIDE the skill directory (so registry updates stay clean): `$GARMIN_PULSE_HEALTH_DIR` if set, else `~/.local/share/garmin-pulse/health/YYYY-MM-DD.md` — one file per day. Older installs with files in `{baseDir}/health/` keep using that location. A cron may also pass an explicit `--output-dir`.

To answer health or fitness questions, read the relevant date's file from the health output dir. If the file doesn't exist for the requested date, run the sync command for that date first.

Sections appear only when Garmin has data for them. Possible sections: Sleep (stages, score), Body (steps, calories, distance, floors, resting/max HR, body battery with charge/drain, HRV, SpO2, weight), Nutrition (calories vs goal, macros — Connect+ accounts with logged food), Hydration (intake, goal, sweat loss), Stress, Training Readiness, Training Status (VO2 max, load balance, acute/chronic load with ACWR, heat/altitude acclimation), Endurance Score, Hill Score, Race Predictions (5K/10K/half/marathon), Lactate Threshold (today only), Respiration, Fitness Age, Intensity Minutes, Activities (pace, cadence, power, training effect).

## Free vs paid Garmin data

Everything except the Nutrition section works on a free Garmin account. Food logging is a Connect+ (paid) feature: on subscribed accounts with logged food the section syncs, otherwise it is absent. Calories from the free MyFitnessPal integration are not synced.

## Related

- [garmin-nutrition](https://github.com/weirdei/garmin-nutrition) — writes food into the Garmin Connect log (add/delete entries, meal slots). This skill reads nutrition totals; that one logs the food. Both share the same `~/.garminconnect/` tokens.

## Dependencies

The sync script runs via [uv](https://docs.astral.sh/uv/), which reads the inline PEP 723 metadata and installs `garminconnect` automatically — no manual `pip install`.

## Credentials & Stored Data

Garmin Connect does not offer a public OAuth API, so a one-time email/password login is required. During setup, the password is used once to obtain OAuth tokens, then discarded. The tokens are cached locally in `~/.garminconnect/` for approximately one year. At runtime, only the cached tokens are used — no email or password is needed. If tokens expire, re-run the setup command.

**Paths written by this skill:**

- `~/.garminconnect/` — cached OAuth tokens (sensitive; grants access to the user's Garmin account)
- health output dir (see Reading Health Data) — daily markdown files with personal health data

## Credits

Based on [freakyflow/garminskill](https://github.com/freakyflow/garminskill); Garmin API access via [python-garminconnect](https://github.com/cyberjunky/python-garminconnect).

## Cron Setup

Schedule the sync to run every morning using OpenClaw's `cron` tool. Use `--days 3` so late-arriving data (sleep synced after the cron ran, evening activities) gets backfilled. No environment variables or credentials are needed.
