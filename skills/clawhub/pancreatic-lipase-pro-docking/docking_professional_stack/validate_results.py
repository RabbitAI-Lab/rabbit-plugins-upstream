#!/usr/bin/env python3
"""validate_results.py — post-run validation of multi-site results CSVs.

Best practices: verify outputs are decision-grade (no silent failures),
sanity-check score ranges, require per-site coverage, and exit non-zero
when problems are found so CI / pipelines can gate on it.

Usage:
  python3 validate_results.py --results dock_results/results_all_sites.csv
      [--runs-dir dock_results/runs] [--sites 5] [--max-score -2.0]
"""
import argparse, csv, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import debug_utils as du


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True, help="results_all_sites.csv")
    ap.add_argument("--runs-dir", default=None, help="runs/ dir to check vina.logs exist")
    ap.add_argument("--sites", type=int, default=5, help="expected number of sites")
    ap.add_argument("--max-score", type=float, default=-2.0,
                    help="worst acceptable 'ok' score (sanity upper bound, kcal/mol)")
    ap.add_argument("--min-score", type=float, default=-15.0,
                    help="best possible score (sanity lower bound, kcal/mol; v100.4: configurable)")
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--log-file", default=None)
    args = ap.parse_args()

    du.setup_logging(debug=args.debug, log_file=args.log_file)
    du.install_exception_hook()
    log = du.LOG

    du.require_file(args.results, "results CSV")
    rows = list(csv.DictReader(open(args.results)))
    problems, warnings = [], []

    if not rows:
        problems.append("results CSV is empty")

    ok_rows = [r for r in rows if r.get("status") == "ok" and r.get("score")]
    failed = [r for r in rows if r.get("status") not in ("ok", "failed", "error", "skipped")]
    if failed:
        problems.append(f"invalid status values: {sorted(set(r['status'] for r in failed))}")

    # score sanity: ok rows must have numeric scores in a plausible range
    bad_score = 0
    for r in ok_rows:
        try:
            v = float(r["score"])
        except (TypeError, ValueError):
            bad_score += 1
            continue
        import math
        if math.isnan(v) or math.isinf(v) or not (args.min_score < v < args.max_score):
            bad_score += 1
            log.warning("implausible score %s for %s @ %s", r["score"], r["name"], r["site"])
    if bad_score:
        problems.append(f"{bad_score} 'ok' rows have missing/implausible scores (fail-closed violation)")

    # v100.4: flag unstable replicates (multi-seed disagreement) as warnings
    unstable = [r for r in ok_rows if r.get("stability", "").startswith("unstable")]
    if unstable:
        warnings.append(f"{len(unstable)} (name,site) pairs have seed-disagreement sd>0.5 kcal/mol "
                        f"(poses not reproducible across seeds; treat rankings with caution)")

    # per-site coverage (each site should have ~equal docked counts)
    from collections import Counter
    by_site = Counter(r["site"] for r in ok_rows)
    if len(by_site) < args.sites:
        problems.append(f"only {len(by_site)}/{args.sites} sites have scored results: {dict(by_site)}")
    counts = list(by_site.values())
    if counts and (max(counts) - min(counts)) > 0.3 * max(counts):
        warnings.append(f"unbalanced per-site coverage: {dict(by_site)}")

    # fail-closed check: any row marked ok but score empty?
    empty_ok = [r for r in rows if r.get("status") == "ok" and not r.get("score")]
    if empty_ok:
        problems.append(f"{len(empty_ok)} rows marked 'ok' without a score (silent fake!)")

    # runs-dir: check vina.log files exist for ok rows (best effort)
    if args.runs_dir:
        runs = Path(args.runs_dir)
        missing_log = 0
        for r in ok_rows[:200]:
            lg = runs / r["site"] / r["name"] / "vina.log"
            if not lg.exists():
                missing_log += 1
        if missing_log:
            warnings.append(f"{missing_log} ok rows lack vina.log (sampled first 200)")

    # summary output (structured)
    summary = {
        "rows": len(rows), "ok": len(ok_rows),
        "failed": sum(1 for r in rows if r.get("status") == "failed"),
        "skipped": sum(1 for r in rows if r.get("status") == "skipped"),
        "errors": sum(1 for r in rows if r.get("status") == "error"),
        "sites_covered": len(by_site),
        "problems": problems, "warnings": warnings,
    }
    print(json.dumps(summary, indent=2))
    if problems:
        print("RESULT: FAIL")
        for p in problems:
            print("  -", p)
        return 2
    print("RESULT: PASS")
    for w in warnings:
        print("  note:", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
