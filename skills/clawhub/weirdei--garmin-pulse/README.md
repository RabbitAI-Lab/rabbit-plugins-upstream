# Garmin Pulse — OpenClaw Skill

An [OpenClaw](https://openclaw.ai) skill that syncs daily Garmin Connect health data into markdown files, one file per day, stored next to your agent.

The point is local state: the agent greps `health/*.md` and answers without touching Garmin's API. Live-query CLI wrappers exist; this is a durable local journal instead.

Based on [freakyflow/garminskill](https://github.com/freakyflow/garminskill): rewritten auth (MFA, no cloudscraper), fixed Body Battery and Stress parsing, added Training Status, Endurance/Hill Scores, Race Predictions, Lactate Threshold, Hydration, Nutrition.

## What it syncs

- **Sleep** — duration, stages, sleep score
- **Body** — steps, calories, distance, floors, resting/max HR, HRV, Body Battery (+charge/−drain), SpO2, weight
- **Nutrition** — calories vs goal, macros (Connect+ accounts with logged food)
- **Hydration** — intake vs goal, sweat loss
- **Stress** — average level
- **Training Readiness** — score, level, feedback
- **Training Status** — VO2 max, load balance, acute/chronic load (ACWR), heat/altitude acclimation
- **Endurance Score**, **Hill Score** — with classification
- **Race Predictions** — 5K / 10K / half / marathon
- **Lactate Threshold** — HR and FTP (today's file only)
- **Respiration**, **Fitness Age**, **Intensity Minutes**
- **Activities** — duration, distance, calories, HR, elevation, pace, cadence, power, training effect

Everything except Nutrition works on a free Garmin account (see [Free vs Connect+](#free-vs-connect)).

## Example output

```markdown
# Health — August 22, 2026

## Sleep: 7h 57m (Good)
Deep: 2h 35m | Light: 3h 35m | REM: 1h 47m | Awake: 0h 15m
Sleep Score: 89

## Body: 410 steps | 1,288 cal
Distance: 0.3 km | Floors: 0
Resting HR: 49 bpm | Max HR: 96 bpm
Body Battery: 58 (+43 / -6) | HRV: 36 ms
SpO2: 96.0%
Weight: 86.8 kg

## Stress: Avg 19 (Rest)

## Training Readiness: 83 (High) — Well Recovered

## Training Status
VO2 Max: 40.2
Training Load Balance: low aerobic 577 | high aerobic 373 | anaerobic 0 (AEROBIC_LOW_FOCUS)
Acute Load: acute 99 | chronic 233 | ACWR 0.4 | LOW (PEAKING_1)
Acclimation: heat 55% | altitude 900m | acclimation 100%

## Endurance Score: 4370 (Beginner)

## Hill Score: 46 (Strength: 45 | Endurance: 47)

## Race Predictions: 5K 30:12 | 10K 1:05:48 | Half 2:38:24 | Marathon 6:15:29

## Lactate Threshold: HR 169 bpm | FTP 340 W (3.9 W/kg)

## Respiration: Waking: 16 brpm | Sleeping: 14 brpm | Range: 6–21

## Fitness Age: 37 (2 years younger)

## Intensity Minutes: 154 weekly
Moderate: 34 | Vigorous: 60 | Goal: 150
```

Sections are only included when data is available.

## Setup

### Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)
  - macOS: `brew install uv`
  - Linux/WSL: `curl -LsSf https://astral.sh/uv/install.sh | sh`
  - Windows: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- A Garmin Connect account (MFA: see [Troubleshooting](#mfa))

### One-time setup

```bash
uv run scripts/sync_garmin.py --setup --email you@example.com
```

The password is prompted via `getpass` and used once to obtain OAuth tokens; with MFA enabled you are also prompted for the code. Tokens are cached in `~/.garminconnect/` (~1 year validity). Subsequent syncs need no credentials.

### Run it

```bash
# Sync today
uv run scripts/sync_garmin.py

# Sync a specific date
uv run scripts/sync_garmin.py --date 2026-01-26

# Sync the last 7 days
uv run scripts/sync_garmin.py --days 7

# Custom output directory (default: health/)
uv run scripts/sync_garmin.py --output-dir my-data

# Show details when a metric fails to fetch
uv run scripts/sync_garmin.py --verbose
```

Markdown files are written to `~/.local/share/garmin-pulse/health/YYYY-MM-DD.md` (override with `--output-dir` or `GARMIN_PULSE_HEALTH_DIR`; a legacy in-package `health/` dir with existing files keeps working).

### Cron

`--days 3` backfills late-arriving data (sleep, evening activities); re-syncing a day overwrites its file. OpenClaw's `cron` tool works, or a system crontab:

```bash
30 6 * * * uv run /path/to/garmin-pulse/scripts/sync_garmin.py --days 3
```

## Free vs Connect+

Connect+ (Garmin's paid subscription, March 2025) gates only new app features; device-derived metrics stay free.

| Data | Tier | Synced |
|---|---|---|
| Sleep, steps, HR, HRV, body battery, stress, SpO2, weight, respiration | Free | ✅ |
| Training readiness / status, VO2 max, fitness age, intensity minutes | Free | ✅ |
| Activities, race predictions, endurance/hill score, lactate threshold, hydration | Free | ✅ |
| Nutrition / food logging | Connect+ | ✅ when subscribed and logged |
| Active Intelligence, Performance Dashboard | Connect+ | ❌ app-only, no known API |

Calories from the free MyFitnessPal integration are not synced.

## Troubleshooting

### "No profile from connectapi"

Usually Garmin rate-limiting, not a wrong password. The script retries with backoff; if it still fails:

1. Wait a few minutes and try again.
2. Double-check your password — Garmin doesn't always return a clear auth error.
3. Check [connect.garmin.com](https://connect.garmin.com) in a browser.

### MFA

Untested, and not for lack of trying. Enabling two-step verification on the test account produced exactly nothing: no email, no SMS, no code. Garmin ships a fitness platform, GPS watches and a subscription tier, but cannot deliver six digits.

So the MFA path is whatever `python-garminconnect` does with a `prompt_mfa` callback: during `--setup` you should get a `Garmin MFA code:` prompt. If it works for you, say so in an issue. If it doesn't, also say so and it gets fixed.

### Tokens expired

Tokens last about a year. When they expire, re-run the setup command.

## Auth notes

Uses [python-garminconnect](https://github.com/cyberjunky/python-garminconnect). Setup (`--setup`) performs one interactive login and caches OAuth tokens in `~/.garminconnect/`; sync uses cached tokens only, with automatic refresh.

## Related

- [garmin-nutrition](https://github.com/weirdei/garmin-nutrition) — the write side: add and delete food entries in the Garmin Connect log. This skill reads the day's nutrition totals; that one logs the food. Both share the same `~/.garminconnect/` tokens.

## Credits

- Original skill: [freakyflow/garminskill](https://github.com/freakyflow/garminskill)
- Garmin API access: [cyberjunky/python-garminconnect](https://github.com/cyberjunky/python-garminconnect)

## License

MIT (see LICENSE) for the modifications in this fork; the original upstream skill was published without a license.
