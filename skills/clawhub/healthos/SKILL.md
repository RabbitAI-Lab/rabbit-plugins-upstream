---
name: healthos
description: Read-only access to a HealthOS user's synced Apple Health data (daily summary, metrics, sleep, and workouts) via a personal read-scoped API token.
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - HEALTHOS_API_TOKEN
      bins:
        - python3
    primaryEnv: HEALTHOS_API_TOKEN
    envVars:
      - name: HEALTHOS_API_TOKEN
        required: true
        description: HealthOS personal API token with the health:summary:read, health:metrics:read, health:sleep:read, and health:workouts:read scopes.
      - name: HEALTHOS_API_URL
        required: false
        description: Override the HealthOS API base URL (default https://api.healthosx.com/api).
    emoji: "🩺"
    homepage: https://healthosx.com/developers
---

# HealthOS

Read-only access to a HealthOS user's health data (Apple Health synced from
their iPhone). Everything goes through the allow-listed helper script
`{baseDir}/scripts/healthos_api.py`; the skill performs **no writes**.

## When to use

Use this skill when the user asks about their own health data: "today's
summary", sleep, workouts, heart rate, steps, weight, HRV, respiratory rate,
or trends over a date range.

## How to answer

1. Run the helper script with the right subcommand (see below). It reads
   `HEALTHOS_API_TOKEN` (and optional `HEALTHOS_API_URL`) from the environment;
   never put the token in a prompt, argument, log, or example.
2. **State the date range and source coverage** in every answer (e.g. "for
   2026-09-09, from your iPhone 16 Pro Max").
3. **Measurement ≠ medical interpretation.** Report numbers and simple trends;
   never diagnose, and never claim a reading is safe or dangerous. If the user
   asks for medical meaning, say the data is for information only and suggest
   a clinician.
4. **Ask before requesting DNA or other separately-scoped data.** This skill is
   only wired for the summary/metrics/sleep/workouts scopes; anything else must
   be requested explicitly.

## Commands

```bash
python {baseDir}/scripts/healthos_api.py summary --date 2026-09-09 [--tz Europe/Berlin]
python {baseDir}/scripts/healthos_api.py metrics --type heart_rate --from 2026-09-09 --to 2026-09-10
python {baseDir}/scripts/healthos_api.py sleep --from 2026-09-08 --to 2026-09-10
python {baseDir}/scripts/healthos_api.py workouts --from 2026-09-08 --to 2026-09-10
```

Allowed `--type` values: `steps`, `active_energy`, `heart_rate`,
`resting_heart_rate`, `hrv_sdnn`, `respiratory_rate`, `body_weight`,
`blood_pressure_systolic`, `blood_pressure_diastolic`.

See `{baseDir}/references/api.md` for endpoint details and interpretation
guidance.
