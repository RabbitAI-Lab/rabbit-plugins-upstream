#!/usr/bin/env python3
"""Run all report steps: health metrics summaries, workouts, rings, training load."""
import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import report_health_metrics
import report_workouts
import report_rings
import report_training_load
import report_daily_summary


def main(out_dir=None, db=None):
    # Reports query lazily via lib.query.query() (resolves db_path() per call), so
    # setting the env var here before rendering is sufficient.
    if db:
        os.environ["HEALTH_DB_PATH"] = str(db)
    # When --out-dir is given, mirror the default layout beneath it: the HTML
    # dashboards land directly in <out-dir>, while workouts and the Markdown
    # summaries keep their own subfolders so filenames can't collide. Each
    # stage falls back to its built-in reports/ default when out_dir is None.
    base = Path(out_dir) if out_dir else None
    workouts_dir = str(base / "workouts") if base else None
    summary_dir = str(base / "summary") if base else None

    print("=== health metrics ===")
    report_health_metrics.main(out_dir=out_dir)

    print("=== workouts ===")
    report_workouts.main(out_dir=workouts_dir)

    print("=== rings ===")
    path = report_rings.render(out_dir=out_dir)
    if path:
        print(f"wrote {path}")

    print("=== training load ===")
    path = report_training_load.render(out_dir=out_dir)
    if path:
        print(f"wrote {path}")

    print("=== daily summary (markdown) ===")
    report_daily_summary.main(out_dir=summary_dir)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Regenerate all health reports.")
    ap.add_argument("--out-dir", "-o",
                    help="Base directory for all reports (default: reports/). "
                         "Workout pages go in <out-dir>/workouts/, Markdown summaries in <out-dir>/summary/.")
    ap.add_argument("--db", help="Path to the DuckDB file (default: $HEALTH_DB_PATH "
                                 "or ~/.local/state/health-metrics/health.duckdb)")
    args = ap.parse_args()
    main(args.out_dir, db=args.db)
