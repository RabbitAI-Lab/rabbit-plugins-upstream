---
name: healthos
description: Read-only access to a HealthOS user's synced Apple Health data — daily summary, metrics, sleep, workouts, and the full raw archive (every synced sample and category event) via a personal read-scoped API token.
version: 1.0.4
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
any other synced metric (blood oxygen, VO₂ max, resting energy, distance,
nutrients, body temperature, …), or trends over a date range. Use `catalog` to
see which types the platform supports, and `coverage` to see which of those the
user has actually synced.

## Data access & boundaries

This skill is **read-only** and scoped to the data the user's own account has
already synced from their iPhone. It can read:

- **Projected summaries** — daily summary, per-metric series (steps, heart rate,
  HRV, resting HR, respiratory rate, weight, blood pressure), sleep stages,
  workouts.
- **The raw archive** — `catalog` (supported types), `coverage` (what the user
  has), and source-faithful `samples`/`events` for any synced quantity or
  category type (blood oxygen, VO₂ max, resting energy, distance, nutrients,
  body temperature, symptoms, …).

It **cannot** write anything, and it **cannot** read labs, DNA, or other
separately-scoped data — those require their own opt-in scopes and are out of
scope. The bearer token only grants the four read scopes listed in the
frontmatter.

## Security & token handling

- The token is read **only** from the `HEALTHOS_API_TOKEN` environment variable;
  never from a prompt, argument, or file, and it is never logged or echoed.
- The API origin is **fixed** to `https://api.healthosx.com/api`; it is not
  overridable, so the token is never sent to any other host.
- Every request is a `GET` to an allow-listed path; there is no write surface.
- The helper script (`scripts/healthos_api.py`) is the only network client.

## How to answer

1. Run the helper script with the right subcommand (see below). It reads
   `HEALTHOS_API_TOKEN` from the environment; never put the token in a prompt,
   argument, log, or example.
2. **State the date range and source coverage** in every answer (e.g. "for
   2026-09-09, from your iPhone 16 Pro Max").
3. **Measurement ≠ medical interpretation.** Report numbers and simple trends;
   never diagnose, and never claim a reading is safe or dangerous. If the user
   asks for medical meaning, say the data is for information only and suggest
   a clinician.
4. **Ask before requesting separately-scoped data.** This skill reads the
   summary/metrics/sleep/workouts endpoints and the raw sample/event archive.
   Labs, DNA, and other separately-scoped data still need an explicit request.

## Commands

```bash
python {baseDir}/scripts/healthos_api.py summary --date 2026-09-09 [--tz Europe/Berlin]
python {baseDir}/scripts/healthos_api.py metrics --type heart_rate --from 2026-09-09 --to 2026-09-10
python {baseDir}/scripts/healthos_api.py sleep --from 2026-09-08 --to 2026-09-10
python {baseDir}/scripts/healthos_api.py workouts --from 2026-09-08 --to 2026-09-10
python {baseDir}/scripts/healthos_api.py catalog
python {baseDir}/scripts/healthos_api.py coverage
python {baseDir}/scripts/healthos_api.py samples --type basal_energy --from 2026-09-08 --to 2026-09-10
python {baseDir}/scripts/healthos_api.py events --type sleep_analysis --from 2026-09-08 --to 2026-09-10
```

Allowed `--type` values for `metrics`: `steps`, `active_energy`, `heart_rate`,
`resting_heart_rate`, `hrv_sdnn`, `respiratory_rate`, `body_weight`,
`blood_pressure_systolic`, `blood_pressure_diastolic`.

`samples` and `events` accept **any** registry id from `catalog` (e.g.
`oxygen_saturation`, `vo2_max`, `basal_energy`, `dietary_energy`, `symptom_fever`);
they return the raw source-faithful archive. `coverage` lists which families the
user has data for.

See `{baseDir}/references/api.md` for endpoint details and interpretation
guidance.

## Support & feedback

- **Documentation & developer program:** https://healthosx.com/developers
- **API early access:** developers@healthosx.com
- **Support / feedback / bug reports:** support@healthosx.com

HealthOS is the operating system for biological data; this skill reads only the
data your own account has already synced. For anything else (labs, DNA, glucose,
nutrition), ask the user and request the corresponding scope explicitly.

