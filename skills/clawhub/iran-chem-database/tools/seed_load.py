#!/usr/bin/env python3
"""Seed-baseline CLI for iran-chem-database (v2.19.0).

Usage:
  python3 -m tools.seed_load status
  python3 -m tools.seed_load search "melamine"          # name / CAS / InChIKey
  python3 -m tools.seed_load diff <new_rows.json>       # new rows vs baseline
  python3 -m tools.seed_load export-sqlite [out.db]     # database starting point
  python3 -m tools.seed_load preload-cache              # 0-network re-parses

The baseline lives in data/seed_export/ (1041 CID-unique confirmed-organic
rows as of v2.19.0, plus retained historical seed files). It is a STARTING
POINT — never a claim of market completeness.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utils import seed_db  # noqa: E402


def _print_rows(rows, limit=20):
    for r in rows[:limit]:
        sups = [s.strip() for s in (r.get("suppliers") or "").split("; ")
                if s.strip()]
        sup = (sups[0][:34] + (f" +{len(sups) - 1} more" if len(sups) > 1 else "")) \
            if sups else ""
        print(f"  {r.get('molecule', '')[:38]:40s} CAS={r.get('cas') or '':10s} "
              f"CID={r.get('pubchem_cid') or '':8s} "
              f"{r.get('organic_status', ''):18s} {sup}")
    if len(rows) > limit:
        print(f"  ... and {len(rows) - limit} more")


def main(argv):
    cmd = argv[0] if argv else "status"

    if cmd == "status":
        idx = seed_db.build_index()
        s = idx.stats()
        man = seed_db.load_seed_manifest()
        mv_path = os.path.join(seed_db.SEED_DIR,
                               "iran_organic_molecules_market_verified.csv")
        mv_man = seed_db.load_seed_manifest(mv_path) \
            if os.path.exists(mv_path) else {}
        exp_path = os.path.join(seed_db.SEED_DIR,
                                "iran_organic_molecules_expanded.csv")
        exp_man = seed_db.load_seed_manifest(exp_path) \
            if os.path.exists(exp_path) else {}
        v219_path = os.path.join(seed_db.SEED_DIR,
                                 "iran_organic_molecules_catalogue_verified_2026-08-25.csv")
        v219_man = seed_db.load_seed_manifest(v219_path) \
            if os.path.exists(v219_path) else {}
        cur_path = os.path.join(seed_db.SEED_DIR,
                                "iran_organic_molecules_parallel_ai_2026-08-24.csv")
        cur_man = seed_db.load_seed_manifest(cur_path) \
            if os.path.exists(cur_path) else {}
        print("Seed baseline (data/seed_export):")
        if v219_man:
            print(f"  CURRENT (v2.19.0 catalogue-verified, PRIMARY): "
                  f"{v219_man.get('rows', '?')} rows, "
                  f"exported {v219_man.get('exported_at', '?')}")
        if cur_man:
            print(f"  PRIOR (2026-08-24 parallel-AI): "
                  f"{cur_man.get('rows', '?')} rows, "
                  f"exported {cur_man.get('exported_at', '?')}")
        if mv_man:
            _sk = str(mv_man.get("skill", ""))
            _ver = _sk.split("@", 1)[1].split()[0] if "@" in _sk else "?"
            print(f"  MARKET-VERIFIED (v{_ver}, PRIMARY): "
                  f"{mv_man.get('rows', '?')} rows, "
                  f"exported {mv_man.get('exported_at', '?')}")
            comp = mv_man.get("composition") or {}
            if comp:
                print(f"    composition: {comp}")
            crawl = mv_man.get("crawl") or {}
            if crawl:
                print(f"    crawl: {crawl.get('telegram_posts_mirrored', crawl.get('telegram_posts_parsed', '?'))} telegram posts "
                      f"from {str(crawl.get('telegram_channels_mirrored', '?'))[:60]} "
                      f"+ web supplier feeds")
        if exp_man:
            print(f"  EXPANDED (v2.15): {exp_man.get('rows', '?')} rows, "
                  f"exported {exp_man.get('exported_at', '?')}")
            print(f"    scope: {exp_man.get('scope', '?')[:110]}...")
            ss = exp_man.get("source_sets") or {}
            if ss:
                print(f"    source sets ({len(ss)}):")
                for name, desc in list(ss.items())[:12]:
                    print(f"      - {name}: {str(desc)[:80]}")
        print(f"  legacy (v2.14):  exported {man.get('exported_at', '?')}")
        print(f"  rows (deduped): {s['rows']}  (confirmed-organic={s['organic_rows']}, "
              f"unknown={s['unknown_rows']}, inorganic={s['inorganic_rows']})")
        print(f"  unique names:     {s['unique_names']}")
        print(f"  unique CAS:       {s['unique_cas']}")
        print(f"  unique InChIKeys: {s['unique_inchikeys']}")
        print(f"  unique CIDs:      {s['unique_cids']}")
        cov_path = os.path.join(seed_db.SEED_DIR, "coverage_report.json")
        if os.path.exists(cov_path):
            cov = json.load(open(cov_path))
            tg = cov.get("telegram", {})
            n_ch = len(tg)
            posts = sum(d.get("posts_parsed", 0) for d in tg.values())
            print(f"  legacy sources:   {n_ch} telegram channels ({posts} posts) "
                  f"+ supplier web catalogs (see coverage_report.json)")
        return 0

    if cmd == "search":
        if len(argv) < 2:
            print("usage: seed_load search <name|CAS|InChIKey>")
            return 2
        idx = seed_db.build_index()
        rows = idx.lookup(argv[1])
        if not rows:
            print(f"NOT in seed baseline: {argv[1]!r} — this may be a NEW molecule.")
            return 1
        print(f"{len(rows)} seed row(s) match {argv[1]!r}:")
        _print_rows(rows)
        return 0

    if cmd == "diff":
        if len(argv) < 2:
            print("usage: seed_load diff <new_rows.json>")
            return 2
        new = json.load(open(argv[1]))
        idx = seed_db.build_index()
        fresh = seed_db.diff_against(idx, new)
        print(f"{len(new)} new row(s): {len(fresh)} NOT in seed baseline, "
              f"{len(new) - len(fresh)} already known.")
        for r in fresh[:20]:
            print(f"  NEW: {str(r.get('canonical_name') or r.get('molecule'))[:40]:42s} "
                  f"CAS={r.get('cas_number') or r.get('cas') or ''}")
        return 0

    if cmd == "export-sqlite":
        out = argv[1] if len(argv) > 1 else os.path.join(
            os.getcwd(), "iran_chem_seed.db")
        path = seed_db.export_sqlite(out)
        idx = seed_db.build_index()
        print(f"SQLite seed database written: {path}")
        print(f"  molecules: {idx.stats()['rows']} rows "
              f"({idx.stats()['unique_names']} unique names)")
        print("  tables: molecules, molecule_suppliers, export_manifest")
        return 0

    if cmd == "preload-cache":
        n = seed_db.preload_pubchem_cache()
        print(f"PubChem cache primed from seed baseline: {n} entries at "
              f"{seed_db._pubchem_cache_path()}")
        print("Re-parsing seeded molecules now costs ZERO network calls.")
        return 0

    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
