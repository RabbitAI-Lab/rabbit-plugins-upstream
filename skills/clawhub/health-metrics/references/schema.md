# DuckDB schema

The full analysis surface. Query these tables directly via the `duckdb` CLI or
`scripts/lib/query.py`'s `query(sql)` — there is no ORM, just SQL strings. If a metric you expect
isn't present, check `scripts/lib/metrics.py` first (it whitelists what ingest keeps).

## Analysis tables

- **`samples_qty(date, ts, metric, unit, qty, source)`** — simple quantity samples (steps, active
  energy, …).
- **`samples_hr(date, ts, metric, unit, min, avg, max, source)`** — min/avg/max-per-interval
  metrics (heart_rate).
- **`sleep_sessions(date, ts, in_bed_start, in_bed_end, sleep_start, sleep_end, core, deep, rem,
  awake, asleep, in_bed, total_sleep, source)`**.
- **`workouts(id PK, date, name, start, end, duration_s, is_indoor, location, temperature_c,
  humidity_pct, intensity, distance_km, avg_hr, min_hr, max_hr, avg_speed, max_speed,
  elevation_up_m, active_energy_kj, total_energy_kj, step_cadence, flights_climbed)`** — one row per
  workout.
- **`workout_route(workout_id, seq, ts, lat, lon, altitude, speed, course)`** — GPS points, only for
  outdoor workouts.
- **`workout_hr(workout_id, ts, min, avg, max)`** — per-minute HR during a workout.
- **`workout_hr_recovery(workout_id, seq, ts, min, avg, max)`** — post-workout HR recovery curve.

## Bookkeeping tables (not analysis data)

- **`ingested_files(filename PK, mtime, ingested_at)`** — mtime-based dedup tracking for
  HealthMetrics files.
- **`ingested_workout_files(filename PK, mtime, ingested_at)`** — same, for Workouts files.
