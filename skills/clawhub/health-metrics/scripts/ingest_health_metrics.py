#!/usr/bin/env python3
"""Ingest Apple Health Auto Export daily JSON files into a local DuckDB store.

Only files matching HealthMetrics-YYYY-MM-DD.json are read (per-minute raw
samples). Weekly/monthly/yearly rollup files are ignored on purpose. Only
metrics in lib/metrics.py's whitelist are kept; everything else (nutrition,
weight, height, mindful minutes, swimming/underwater, ...) is dropped.

Idempotent: re-running is cheap (skips files whose mtime hasn't changed) and
safe (re-ingesting a file replaces that whole day's rows rather than
appending duplicates).
"""
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.metrics import ALL_QTY, ALL_HR, ALL_SLEEP
from lib.query import db_path

# Source folder is configurable via $HEALTH_METRICS_DIR; defaults to the standard
# Apple Health Auto Export iCloud location under the current user's home.
SOURCE_DIR = Path(os.environ.get(
    "HEALTH_METRICS_DIR",
    Path.home() / "Library/Mobile Documents/iCloud~com~ifunography~HealthExport"
                  "/Documents/iCloud Drive HealthMetrics",
))
DB_PATH = db_path()
DAILY_FILE_RE = re.compile(r"^HealthMetrics-\d{4}-\d{2}-\d{2}\.json$")

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS samples_qty(
    date DATE, ts TIMESTAMPTZ, metric VARCHAR, unit VARCHAR, qty DOUBLE, source VARCHAR
);
CREATE TABLE IF NOT EXISTS samples_hr(
    date DATE, ts TIMESTAMPTZ, metric VARCHAR, unit VARCHAR,
    min DOUBLE, avg DOUBLE, max DOUBLE, source VARCHAR
);
CREATE TABLE IF NOT EXISTS sleep_sessions(
    date DATE, ts TIMESTAMPTZ,
    in_bed_start TIMESTAMPTZ, in_bed_end TIMESTAMPTZ,
    sleep_start TIMESTAMPTZ, sleep_end TIMESTAMPTZ,
    core DOUBLE, deep DOUBLE, rem DOUBLE, awake DOUBLE,
    asleep DOUBLE, in_bed DOUBLE, total_sleep DOUBLE, source VARCHAR
);
CREATE TABLE IF NOT EXISTS ingested_files(
    filename VARCHAR PRIMARY KEY, mtime DOUBLE, ingested_at TIMESTAMP DEFAULT current_timestamp
);
"""


def sql_str_list(names):
    return "(" + ", ".join(f"'{n}'" for n in sorted(names)) + ")"


def run_duckdb(sql):
    result = subprocess.run(
        ["duckdb", str(DB_PATH), "-c", sql],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"duckdb failed:\n{sql}\n---\n{result.stderr}")
    return result.stdout


def find_candidate_files():
    return sorted(p for p in SOURCE_DIR.glob("*.json") if DAILY_FILE_RE.match(p.name))


def already_ingested(filename, mtime):
    out = run_duckdb(
        f"SELECT mtime FROM ingested_files WHERE filename = '{filename}';"
    )
    return out.strip() != "" and str(mtime) in out


def ingest_file(path):
    day = path.stem.replace("HealthMetrics-", "")  # YYYY-MM-DD
    file_literal = str(path).replace("'", "''")

    sql = f"""
    BEGIN TRANSACTION;

    DELETE FROM samples_qty WHERE date = DATE '{day}';
    DELETE FROM samples_hr WHERE date = DATE '{day}';
    DELETE FROM sleep_sessions WHERE date = DATE '{day}';

    WITH raw AS (
        SELECT unnest(data.metrics) AS m
        FROM read_json_auto('{file_literal}', sample_size=-1)
    ),
    rows AS (
        SELECT m.name AS metric, m.units AS unit, unnest(m.data) AS d
        FROM raw
    )
    INSERT INTO samples_qty
    SELECT
        substr(d.date, 1, 10)::DATE AS date,
        strptime(d.date, '%Y-%m-%d %H:%M:%S %z') AS ts,
        metric, unit, d.qty AS qty, d.source AS source
    FROM rows
    WHERE metric IN {sql_str_list(ALL_QTY)};

    WITH raw AS (
        SELECT unnest(data.metrics) AS m
        FROM read_json_auto('{file_literal}', sample_size=-1)
    ),
    rows AS (
        SELECT m.name AS metric, m.units AS unit, unnest(m.data) AS d
        FROM raw
    )
    INSERT INTO samples_hr
    SELECT
        substr(d.date, 1, 10)::DATE AS date,
        strptime(d.date, '%Y-%m-%d %H:%M:%S %z') AS ts,
        metric, unit, d."Min" AS min, d."Avg" AS avg, d."Max" AS max, d.source AS source
    FROM rows
    WHERE metric IN {sql_str_list(ALL_HR)};

    WITH raw AS (
        SELECT unnest(data.metrics) AS m
        FROM read_json_auto('{file_literal}', sample_size=-1)
    ),
    rows AS (
        SELECT m.name AS metric, unnest(m.data) AS d
        FROM raw
    )
    INSERT INTO sleep_sessions
    SELECT
        substr(d.date, 1, 10)::DATE AS date,
        strptime(d.date, '%Y-%m-%d %H:%M:%S %z') AS ts,
        strptime(d.inBedStart, '%Y-%m-%d %H:%M:%S %z') AS in_bed_start,
        strptime(d.inBedEnd, '%Y-%m-%d %H:%M:%S %z') AS in_bed_end,
        strptime(d.sleepStart, '%Y-%m-%d %H:%M:%S %z') AS sleep_start,
        strptime(d.sleepEnd, '%Y-%m-%d %H:%M:%S %z') AS sleep_end,
        d.core, d.deep, d.rem, d.awake, d.asleep, d.inBed AS in_bed,
        d.totalSleep AS total_sleep, d.source
    FROM rows
    WHERE metric IN {sql_str_list(ALL_SLEEP)};

    DELETE FROM ingested_files WHERE filename = '{path.name}';
    INSERT INTO ingested_files VALUES ('{path.name}', {path.stat().st_mtime}, current_timestamp);

    COMMIT;
    """
    run_duckdb(sql)


def main():
    run_duckdb(SCHEMA_SQL)
    files = find_candidate_files()
    if not files:
        print(f"No daily files found in {SOURCE_DIR}")
        return

    ingested, skipped = 0, 0
    for path in files:
        mtime = path.stat().st_mtime
        if already_ingested(path.name, mtime):
            skipped += 1
            continue
        ingest_file(path)
        ingested += 1
        print(f"ingested {path.name}")

    print(f"done: {ingested} file(s) ingested, {skipped} already up to date")


if __name__ == "__main__":
    main()
