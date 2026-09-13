#!/usr/bin/env python3
"""Validate that a result directory contains real docking outputs, not dry-mode placeholders."""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path

def fnum(x):
    try:
        if x in (None,'','None','nan'): return None
        return float(x)
    except Exception:
        return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--run-dir', required=True, help='Directory containing final_ranked_results.csv and metadata.json')
    ap.add_argument('--require-score-fraction', type=float, default=0.8)
    args=ap.parse_args()
    d=Path(args.run_dir)
    results=d/'final_ranked_results.csv'; meta=d/'metadata.json'
    if not results.exists(): raise SystemExit(f'FAIL: missing {results}')
    rows=list(csv.DictReader(results.open()))
    md=json.loads(meta.read_text()) if meta.exists() else {}
    scores=[r for r in rows if fnum(r.get('vina_score_kcal_mol')) is not None]
    dry=md.get('dry_mode') or str(md.get('mode','')).lower()=='dry'
    frac=len(scores)/len(rows) if rows else 0
    problems=[]
    if dry: problems.append('metadata says dry mode')
    if frac < args.require_score_fraction: problems.append(f'only {frac:.1%} rows have numeric Vina scores')
    if not rows: problems.append('no result rows')
    if problems:
        print('NOT REAL DOCKING / NOT DECISION-GRADE:')
        for p in problems: print('-', p)
        raise SystemExit(2)
    print('PASS: result directory contains numeric docking scores for sufficient rows.')
if __name__=='__main__': main()
