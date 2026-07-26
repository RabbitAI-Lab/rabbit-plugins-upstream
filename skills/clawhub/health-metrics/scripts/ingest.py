#!/usr/bin/env python3
"""Run all ingest steps: health metrics, then workouts.

DB location comes from $HEALTH_DB_PATH (or --db), else a per-user state dir; source
folders from $HEALTH_METRICS_DIR / $HEALTH_WORKOUTS_DIR (see lib/query.py and the
ingest modules for defaults).
"""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))


def main(db=None):
    # Set the env var BEFORE importing the ingest modules -- they resolve their
    # module-level DB_PATH at import time via lib.query.db_path().
    if db:
        os.environ["HEALTH_DB_PATH"] = str(db)
    import ingest_health_metrics
    import ingest_workouts
    print("=== health metrics ===")
    ingest_health_metrics.main()
    print("=== workouts ===")
    ingest_workouts.main()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Run all ingest steps.")
    ap.add_argument("--db", help="Path to the DuckDB file (default: $HEALTH_DB_PATH "
                                 "or ~/.local/state/health-metrics/health.duckdb)")
    args = ap.parse_args()
    main(db=args.db)
