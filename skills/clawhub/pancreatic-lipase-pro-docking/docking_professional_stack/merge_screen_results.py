#!/usr/bin/env python3
"""
merge_screen_results.py

Merge results from many subchunk docking runs into one ranked table.
Designed for outputs produced by library_chunker.py + docking_speed_pipeline.py.

Example:
  python merge_screen_results.py --root chunks_10k --out merged_results.csv
"""
from __future__ import annotations
import argparse, csv, json
from pathlib import Path


def read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    keys = sorted({k for r in rows for k in r.keys()}) if rows else []
    with path.open("w", newline="") as f:
        if keys:
            w=csv.DictWriter(f, fieldnames=keys, extrasaction='ignore')
            w.writeheader(); w.writerows(rows)


def score_float(r):
    try: return float(r.get('vina_score_kcal_mol'))
    except Exception: return 999.0


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--root', default='.', help='chunk directory containing speed_runs or result CSVs')
    ap.add_argument('--out', default='merged_results.csv')
    ap.add_argument('--dedupe', action='store_true', default=True)
    args=ap.parse_args()
    root=Path(args.root)
    files=list(root.glob('speed_runs/*/final_ranked_results.csv')) + list(root.glob('**/speed_runs/*/final_ranked_results.csv')) + list(root.glob('**/final_ranked_results.csv'))
    # Remove duplicates while preserving order
    seen=set(); uniq=[]
    for f in files:
        rp=f.resolve()
        if rp not in seen:
            seen.add(rp); uniq.append(f)
    rows=[]
    for f in uniq:
        for r in read_csv(f):
            r['source_result_file']=str(f)
            rows.append(r)
    if args.dedupe:
        best={}
        for r in rows:
            key=(r.get('name') or '', r.get('smiles') or '')
            if key not in best or score_float(r) < score_float(best[key]):
                best[key]=r
        rows=list(best.values())
    rows.sort(key=lambda r: (score_float(r)==999.0, score_float(r)))
    for i,r in enumerate(rows,1): r['global_rank']=i
    write_csv(args.out, rows)
    summary={'files_found':len(uniq),'rows_merged':len(rows),'out':args.out}
    Path(str(args.out)+'.summary.json').write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))

if __name__=='__main__': main()
