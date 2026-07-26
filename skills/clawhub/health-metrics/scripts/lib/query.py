"""Thin DuckDB CLI query helper -- no python duckdb package required."""
import json
import os
import subprocess
from pathlib import Path

# The DuckDB file is per-person, sensitive state -- it lives OUTSIDE the skill and
# is never versioned/published. Resolved from $HEALTH_DB_PATH, else a per-user state
# dir. Its parent is created on demand so first ingest can write a fresh database.
DEFAULT_DB_PATH = Path.home() / ".local" / "state" / "health-metrics" / "health.duckdb"


def db_path():
    p = Path(os.environ.get("HEALTH_DB_PATH", DEFAULT_DB_PATH))
    p.parent.mkdir(parents=True, exist_ok=True)
    return p


def query(sql):
    # Resolve at call time (not import time) so a late --db / env change still applies.
    result = subprocess.run(
        ["duckdb", str(db_path()), "-json", "-c", sql],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"duckdb query failed:\n{sql}\n---\n{result.stderr}")
    out = result.stdout.strip()
    return json.loads(out) if out else []
