#!/usr/bin/env python3
"""
select_top_diverse_hits.py

Select top hits while preserving chemical diversity and similarity-cluster coverage.
Use after merge_screen_results.py.

Strategy:
- Sort by docking score, then lower GI penalty and fewer Lipinski issues.
- Keep up to N per cluster.
- Enforce optional diversity cutoff by Tanimoto similarity.
- Fallback to approximate SMILES shingle similarity if RDKit unavailable.

Example:
  python select_top_diverse_hits.py --input merged_results.csv --out top_diverse_hits.csv --top-n 200 --per-cluster 5 --diversity-cutoff 0.85
"""
from __future__ import annotations
import argparse, csv
from collections import defaultdict


def read_csv(path):
    with open(path, newline='') as f: return list(csv.DictReader(f))

def write_csv(path, rows):
    keys=['name','smiles','vina_score_kcal_mol','prediction','confidence','cluster_id','global_rank','GI_fluid_penalty','key_flags']
    extra=sorted({k for r in rows for k in r.keys()}-set(keys))
    with open(path,'w',newline='') as f:
        w=csv.DictWriter(f, fieldnames=keys+extra, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)

def score_key(r):  # v100.4: NaN/inf-safe
    try: s=float(r.get('vina_score_kcal_mol'))
    except Exception: s=999.0
    try: gi=int(float(r.get('GI_fluid_penalty') or 0))
    except Exception: gi=0
    try: lip=int(float(r.get('Lipinski_violations') or 0))
    except Exception: lip=0
    return (s==999.0, s, gi, lip)

class Similarity:
    def __init__(self):
        self.rdkit=False
        try:
            from rdkit import Chem, DataStructs
            from rdkit.Chem import AllChem
            self.Chem=Chem; self.DataStructs=DataStructs; self.AllChem=AllChem; self.rdkit=True
        except Exception:
            pass
    def fp(self,smi):
        if self.rdkit:
            m=self.Chem.MolFromSmiles(smi or '')
            return self.AllChem.GetMorganFingerprintAsBitVect(m,2,nBits=2048) if m else None
        s=smi or ''; k=3
        return {s[i:i+k] for i in range(max(1,len(s)-k+1))} or {s}
    def sim(self,a,b):
        if a is None or b is None: return 0.0
        if self.rdkit:
            return float(self.DataStructs.TanimotoSimilarity(a,b))
        u=len(a|b); return len(a&b)/u if u else 0.0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', default='top_diverse_hits.csv')
    ap.add_argument('--top-n', type=int, default=200)
    ap.add_argument('--per-cluster', type=int, default=5)
    ap.add_argument('--diversity-cutoff', type=float, default=0.90, help='skip new hit if similarity to selected hit exceeds this')
    ap.add_argument('--min-score', type=float, default=None, help='optional max acceptable docking score, e.g. -6')
    args=ap.parse_args()
    rows=read_csv(args.input)
    if args.min_score is not None:
        def ok(r):
            try: return float(r.get('vina_score_kcal_mol')) <= args.min_score
            except Exception: return False
        rows=[r for r in rows if ok(r)]
    rows.sort(key=score_key)
    sim=Similarity(); selected=[]; selected_fps=[]; cluster_counts=defaultdict(int)
    for r in rows:
        if len(selected)>=args.top_n: break
        cid=r.get('cluster_id') or 'unknown'
        if cluster_counts[cid]>=args.per_cluster: continue
        fp=sim.fp(r.get('smiles'))
        too_close=False
        for sfp in selected_fps:
            if sim.sim(fp,sfp) >= args.diversity_cutoff:
                too_close=True; break
        if too_close: continue
        selected.append(r); selected_fps.append(fp); cluster_counts[cid]+=1
    for i,r in enumerate(selected,1): r['diverse_rank']=i
    write_csv(args.out, selected)
    print(f'Selected {len(selected)} diverse hits -> {args.out}')
    print(f'Similarity engine: {"RDKit Morgan/Tanimoto" if sim.rdkit else "fallback SMILES shingle"}')

if __name__=='__main__': main()
