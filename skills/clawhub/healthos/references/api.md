# HealthOS API — reference

Base URL: `https://api.healthosx.com/api`. Auth: `Authorization: Bearer <token>`.

## Scopes

| Scope | Endpoint | Returns |
|---|---|---|
| `health:summary:read` | `GET /v1/health/summary?date=YYYY-MM-DD&tz=IANA` | One day's activity (steps, active energy), vitals (HR avg/min/max, resting HR, respiratory rate, HRV, weight), sleep (asleep/in-bed minutes), workouts (count, calories) |
| `health:metrics:read` | `GET /v1/health/metrics?metric_type=X&from=&to=&limit=` | Metric series (timestamp, value, unit, source) |
| `health:sleep:read` | `GET /v1/health/sleep?from=&to=` | Sleep-stage intervals (start, end, stage, source) |
| `health:workouts:read` | `GET /v1/health/workouts?from=&to=` | Workouts (start, end, activity, calories, source) |
| `health:metrics:read` | `GET /v1/health/archive/samples?registry_id=&from=&to=` | Canonical numeric/correlation samples (every Apple Health quantity type) |
| `health:metrics:read` | `GET /v1/health/archive/events?registry_id=&from=&to=` | Canonical category events (sleep stages, symptoms, cycle, mindful, …) |
| `health:workouts:read` | `GET /v1/health/archive/workouts?from=&to=` | Canonical workouts (full fidelity: activity, calories, distance, indoor) |
| `health:metrics:read` | `GET /v1/health/archive/workout-series?from=&to=` | Workout metric series (HR, power, cadence …) |
| `health:metrics:read` | `GET /v1/health/archive/routes?from=&to=` | GPS route segments (points) |
| `health:metrics:read` | `GET /v1/health/archive/ecg?from=&to=` | ECG records (classification, average HR, sample count) |

`from`/`to` are ISO-8601 (UTC) or `YYYY-MM-DD`; the client normalises dates.

## Metric types (allow-listed)

`steps`, `active_energy` (kcal), `heart_rate` (count/min), `resting_heart_rate`,
`hrv_sdnn` (ms), `respiratory_rate` (count/min), `body_weight` (kg),
`blood_pressure_systolic`/`blood_pressure_diastolic` (mmHg).

## Interpretation guidance

- **Units are stable** (canonical). Timestamps are UTC.
- **Steps and active energy are cumulative per interval** — chart them at the
  interval end, not the start.
- **Sleep stages** use the values `INBED`, `ASLEEP`, `AWAKE`, `ASLEEPCORE`,
  `ASLEEPDEEP`, `ASLEEPREM` (or `CORE`/`DEEP`/`REM` from older sources). Sum
  non-`AWAKE`, non-`INBED` stages for "asleep".
- **HRV is SDNN in milliseconds.** Lower is not automatically "worse".
- **Weight** may be sparse (one sample per weigh-in).
- **These are measurements, not diagnoses.** Always cite the date range and
  source, and do not interpret a reading as safe or dangerous.

## Privacy

- The token is a secret: never include it in prompts, arguments, logs, or
  examples. It is read from `HEALTHOS_API_TOKEN`.
- The API is read-only for this skill; there are no write endpoints in scope.
- DNA and labs data require separate opt-in scopes and are **not** part of this
  skill. Ask the user before requesting them.
