#!/usr/bin/env python3
"""Ingest Apple Health Auto Export daily Workouts JSON files into the shared
DuckDB store. Only Workouts-YYYY-MM-DD.json files are read (per-workout full
fidelity records). Dedup unit is the workout `id`: re-ingesting a file that
contains a previously-seen workout replaces that workout's rows everywhere.

Per-sample activeEnergy/basalEnergy/stepCount/cyclingDistance series are
intentionally NOT ingested for v1 -- the scalar totals already captured in
`workouts` (distance, active/total energy, cadence, etc.) cover the planned
reports, and those series are the bulk of the file size.
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.query import db_path

# Source folder is configurable via $HEALTH_WORKOUTS_DIR; defaults to the standard
# Apple Health Auto Export iCloud location under the current user's home.
DIR = Path(os.environ.get(
    "HEALTH_WORKOUTS_DIR",
    Path.home() / "Library/Mobile Documents/iCloud~com~ifunography~HealthExport"
                  "/Documents/iCloud Drive Workouts",
))
DB_PATH = db_path()
DAILY_FILE_RE = re.compile(r"^Workouts-\d{4}-\d{2}-\d{2}\.json$")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS workouts(
    id VARCHAR PRIMARY KEY, date DATE, name VARCHAR,
    start TIMESTAMPTZ, "end" TIMESTAMPTZ, duration_s DOUBLE,
    is_indoor BOOLEAN, location VARCHAR,
    temperature_c DOUBLE, humidity_pct DOUBLE, intensity DOUBLE,
    distance_km DOUBLE, avg_hr DOUBLE, min_hr DOUBLE, max_hr DOUBLE,
    avg_speed DOUBLE, max_speed DOUBLE, elevation_up_m DOUBLE,
    active_energy_kj DOUBLE, total_energy_kj DOUBLE,
    step_cadence DOUBLE, flights_climbed DOUBLE
);
CREATE TABLE IF NOT EXISTS workout_route(
    workout_id VARCHAR, seq INTEGER, ts TIMESTAMPTZ,
    lat DOUBLE, lon DOUBLE, altitude DOUBLE, speed DOUBLE, course DOUBLE
);
CREATE TABLE IF NOT EXISTS workout_hr(
    workout_id VARCHAR, ts TIMESTAMPTZ, min DOUBLE, avg DOUBLE, max DOUBLE
);
CREATE TABLE IF NOT EXISTS workout_hr_recovery(
    workout_id VARCHAR, seq INTEGER, ts TIMESTAMPTZ, min DOUBLE, avg DOUBLE, max DOUBLE
);
CREATE TABLE IF NOT EXISTS ingested_workout_files(
    filename VARCHAR PRIMARY KEY, mtime DOUBLE, ingested_at TIMESTAMP DEFAULT current_timestamp
);
"""


def run_duckdb(sql):
    result = subprocess.run(["duckdb", str(DB_PATH), "-c", sql], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"duckdb failed:\n{sql}\n---\n{result.stderr}")
    return result.stdout


def find_candidate_files():
    return sorted(p for p in DIR.glob("*.json") if DAILY_FILE_RE.match(p.name))


def already_ingested(filename, mtime):
    out = run_duckdb(f"SELECT mtime FROM ingested_workout_files WHERE filename = '{filename}';")
    return out.strip() != "" and str(mtime) in out


# Apple omits fields entirely when not applicable to a workout type (rather than
# nulling them), so a file whose workouts never populate e.g. flightsClimbed
# won't even have that key in the inferred struct. Map each output expression to
# the top-level field(s) it depends on, and fall back to NULL when absent.
WORKOUT_FIELD_EXPRS = [
    ("w.isIndoor", {"isIndoor"}),
    ("w.location", {"location"}),
    ("w.temperature.qty", {"temperature"}),
    ("w.humidity.qty", {"humidity"}),
    ("w.intensity.qty", {"intensity"}),
    ("w.distance.qty", {"distance"}),
    ("w.avgHeartRate.qty", {"avgHeartRate"}),
    ("w.heartRate.min.qty", {"heartRate"}),
    ("w.maxHeartRate.qty", {"maxHeartRate"}),
    ("w.avgSpeed.qty", {"avgSpeed"}),
    ("w.maxSpeed.qty", {"maxSpeed"}),
    ("w.elevationUp.qty", {"elevationUp"}),
    ("w.activeEnergyBurned.qty", {"activeEnergyBurned"}),
    ("w.totalEnergy.qty", {"totalEnergy"}),
    ("w.stepCadence.qty", {"stepCadence"}),
    ("w.flightsClimbed.qty", {"flightsClimbed"}),
]


def available_fields(file_literal):
    """Maps each top-level workout field present in this file to its inferred
    DuckDB type. A field that is `null` for every workout in the file (rather
    than omitted) still shows up here, but DuckDB can't infer a real type for
    an all-null/all-empty column and falls back to generic JSON -- which
    doesn't support struct field access (`.qty`) or UNNEST. Callers must
    treat a JSON-typed field as effectively absent."""
    sql = (f"SELECT w.* FROM (SELECT unnest(data.workouts) AS w "
           f"FROM read_json_auto('{file_literal}', sample_size=-1, maximum_object_size=500000000)) t LIMIT 0;")
    result = subprocess.run(["duckdb", str(DB_PATH), "-json", "-c", f"DESCRIBE {sql}"],
                             capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    rows = json.loads(result.stdout.strip()) if result.stdout.strip() else []
    return {r["column_name"]: r["column_type"] for r in rows}


def usable_scalar_fields(available):
    return {name for name, typ in available.items() if typ != "JSON"}


def is_array_field(available, name):
    return name in available and available[name] != "JSON" and available[name].endswith("[]")


def ingest_file(path):
    file_literal = str(path).replace("'", "''")
    available = available_fields(file_literal)

    ids_sql = f"""
    WITH raw AS (SELECT unnest(data.workouts) AS w FROM read_json_auto('{file_literal}', sample_size=-1, maximum_object_size=500000000))
    SELECT w.id AS id FROM raw;
    """
    result = subprocess.run(["duckdb", str(DB_PATH), "-json", "-c", ids_sql], capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr)
    ids = [r["id"] for r in (json.loads(result.stdout.strip()) if result.stdout.strip() else [])]
    delete_ids = ", ".join(f"'{i}'" for i in ids) or "''"

    scalar_available = usable_scalar_fields(available)
    optional_cols = ",\n        ".join(
        expr if fields <= scalar_available else "NULL" for expr, fields in WORKOUT_FIELD_EXPRS
    )

    route_insert = f"""
    WITH raw AS (
        SELECT w.id AS workout_id, unnest(w.route) AS p, generate_subscripts(w.route, 1) AS seq
        FROM (SELECT unnest(data.workouts) AS w FROM read_json_auto('{file_literal}', sample_size=-1, maximum_object_size=500000000))
    )
    INSERT INTO workout_route
    SELECT workout_id, seq, strptime(p.timestamp, '%Y-%m-%d %H:%M:%S %z'),
           p.latitude, p.longitude, p.altitude, p.speed, p.course
    FROM raw;
    """ if is_array_field(available, "route") else "-- no route field in this file"

    hr_insert = f"""
    WITH raw AS (
        SELECT w.id AS workout_id, unnest(w.heartRateData) AS p
        FROM (SELECT unnest(data.workouts) AS w FROM read_json_auto('{file_literal}', sample_size=-1, maximum_object_size=500000000))
    )
    INSERT INTO workout_hr
    SELECT workout_id, strptime(p.date, '%Y-%m-%d %H:%M:%S %z'), p."Min", p."Avg", p."Max"
    FROM raw;
    """ if is_array_field(available, "heartRateData") else "-- no heartRateData field in this file"

    hr_recovery_insert = f"""
    WITH raw AS (
        SELECT w.id AS workout_id, unnest(w.heartRateRecovery) AS p,
               generate_subscripts(w.heartRateRecovery, 1) AS seq
        FROM (SELECT unnest(data.workouts) AS w FROM read_json_auto('{file_literal}', sample_size=-1, maximum_object_size=500000000))
    )
    INSERT INTO workout_hr_recovery
    SELECT workout_id, seq, strptime(p.date, '%Y-%m-%d %H:%M:%S %z'), p."Min", p."Avg", p."Max"
    FROM raw;
    """ if is_array_field(available, "heartRateRecovery") else "-- no heartRateRecovery field in this file"

    sql = f"""
    BEGIN TRANSACTION;

    DELETE FROM workouts WHERE id IN ({delete_ids});
    DELETE FROM workout_route WHERE workout_id IN ({delete_ids});
    DELETE FROM workout_hr WHERE workout_id IN ({delete_ids});
    DELETE FROM workout_hr_recovery WHERE workout_id IN ({delete_ids});

    WITH raw AS (
        SELECT unnest(data.workouts) AS w FROM read_json_auto('{file_literal}', sample_size=-1, maximum_object_size=500000000)
    )
    INSERT INTO workouts
    SELECT
        w.id,
        substr(w.start, 1, 10)::DATE,
        w.name,
        strptime(w.start, '%Y-%m-%d %H:%M:%S %z'),
        strptime(w."end", '%Y-%m-%d %H:%M:%S %z'),
        w.duration,
        {optional_cols}
    FROM raw;

    {route_insert}

    {hr_insert}

    {hr_recovery_insert}

    DELETE FROM ingested_workout_files WHERE filename = '{path.name}';
    INSERT INTO ingested_workout_files VALUES ('{path.name}', {path.stat().st_mtime}, current_timestamp);

    COMMIT;
    """
    run_duckdb(sql)
    return len(ids)


def main():
    run_duckdb(SCHEMA_SQL)
    files = find_candidate_files()
    if not files:
        print(f"No daily workout files found in {DIR}")
        return

    ingested, skipped, total_workouts = 0, 0, 0
    for path in files:
        mtime = path.stat().st_mtime
        if already_ingested(path.name, mtime):
            skipped += 1
            continue
        n = ingest_file(path)
        ingested += 1
        total_workouts += n
        print(f"ingested {path.name} ({n} workout(s))")

    print(f"done: {ingested} file(s) ingested ({total_workouts} workout(s)), {skipped} already up to date")


if __name__ == "__main__":
    main()
