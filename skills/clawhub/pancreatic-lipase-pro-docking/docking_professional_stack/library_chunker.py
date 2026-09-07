#!/usr/bin/env python3
"""
library_chunker.py

Mathematically sensible chunking for large docking libraries (e.g., 10,000+ similar molecules).

Purpose:
- Group molecules by chemical similarity using Morgan fingerprints + Butina clustering.
- Split each similarity cluster into balanced execution chunks using estimated docking cost.
- Optionally create nested subchunks for parallel jobs.
- Produce chunk CSVs + manifest + run commands.

Why this helps:
- Similar chunks are easier to review and compare.
- Balanced chunks avoid one worker getting all slow/flexible molecules.
- Nested chunks enable parallel docking across machines/HPC arrays.
- Similarity grouping supports later high-quality redocking/FEP on congeneric series.

Example:
  python library_chunker.py --input ligands.csv --out chunks --target-chunk-size 500 --subchunk-size 100
  bash chunks/run_all_subchunks.sh

Input CSV columns:
  name,smiles
"""
from __future__ import annotations
import argparse, csv, json, math, os, re, statistics
from pathlib import Path
from collections import defaultdict


def safe(s):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", str(s))[:80]


def read_ligands(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    ligs=[]
    for i,r in enumerate(rows,1):
        extras = r.pop(None, None)
        smi=r.get('smiles') or r.get('SMILES') or r.get('canonical_smiles')
        if not smi: continue
        entry={'name': (r.get('name') or r.get('id') or f'lig_{i}').strip(), 'smiles': smi.strip()}
        for k,v in r.items():
            if k in {'name','id','smiles','SMILES','canonical_smiles'}: continue
            if v is None or v == '': continue
            entry[k]=v
        if extras:
            joined = ','.join(extras) if isinstance(extras, list) else str(extras)
            entry.setdefault('notes','')
            entry['notes'] = (entry['notes'] + ',' + joined).strip(',') if entry['notes'] else joined
        ligs.append(entry)
    return ligs


def write_csv(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    keys = ['name','smiles','cluster_id','chunk_id','subchunk_id','estimated_cost']
    extra = sorted({k for r in rows for k in r.keys()} - set(keys))
    with open(path,'w',newline='') as f:
        w=csv.DictWriter(f, fieldnames=keys+extra, extrasaction='ignore')
        w.writeheader(); w.writerows(rows)


def rdkit_cluster(ligs, threshold=0.65, radius=2, nbits=2048):
    try:
        from rdkit import Chem, DataStructs
        from rdkit.Chem import AllChem, Descriptors, Lipinski
        from rdkit.ML.Cluster import Butina
    except Exception as e:
        print(f"WARNING: RDKit unavailable ({e}). Falling back to fast approximate SMILES-token clustering. Install RDKit for chemically rigorous Morgan/Tanimoto chunks.")
        return fallback_smiles_cluster(ligs, threshold=threshold)

    valid=[]; invalid=[]; fps=[]
    for lig in ligs:
        mol=Chem.MolFromSmiles(lig['smiles'])
        if mol is None:
            lig.update({'cluster_id':'invalid','estimated_cost':9999,'valid':False})
            invalid.append(lig); continue
        fp=AllChem.GetMorganFingerprintAsBitVect(mol, radius, nBits=nbits)
        ha=mol.GetNumHeavyAtoms()
        rot=Lipinski.NumRotatableBonds(mol)
        rings=Descriptors.RingCount(mol)
        # Empirical docking cost proxy: heavy atoms + flexibility penalty.
        # Flexible molecules usually cost more search time.
        cost=max(1, ha + 3*rot + 0.5*rings)
        lig.update({'estimated_cost': round(cost,2), 'valid':True, 'heavy_atoms':ha, 'rotatable_bonds':rot, 'ring_count':rings})
        valid.append(lig); fps.append(fp)

    # Butina uses distances for lower triangle. distance = 1 - Tanimoto.
    dists=[]
    nfps=len(fps)
    for i in range(1,nfps):
        sims=DataStructs.BulkTanimotoSimilarity(fps[i], fps[:i])
        dists.extend([1-x for x in sims])
    clusters=Butina.ClusterData(dists, nfps, 1-threshold, isDistData=True)
    clustered=[]
    for cid, idxs in enumerate(clusters):
        for idx in idxs:
            lig=valid[idx]
            lig['cluster_id']=f'C{cid:05d}'
            clustered.append(lig)
    return clustered + invalid



def fallback_smiles_cluster(ligs, threshold=0.65):
    """Dependency-free approximate clustering using character/token shingles.
    This is not as chemically rigorous as Morgan fingerprints, but it preserves speed and still groups many congeneric SMILES reasonably.
    """
    def shingles(s, k=3):
        s=s.strip()
        if len(s)<k: return {s}
        return {s[i:i+k] for i in range(len(s)-k+1)}
    def tanimoto(a,b):
        u=len(a|b); return len(a&b)/u if u else 0.0
    clusters=[]
    reps=[]
    for lig in ligs:
        sh=shingles(lig['smiles'])
        # simple cost proxy without RDKit
        smi=lig['smiles']
        heavy=sum(1 for c in smi if c.isalpha() and c.upper()!='H')
        rot=smi.count('C')//4 + smi.count('c')//8
        rings=sum(ch.isdigit() for ch in smi)//2
        cost=max(1, heavy + 3*rot + 0.5*rings)
        best_i=None; best=0
        for i,rep in enumerate(reps):
            sim=tanimoto(sh,rep)
            if sim>best:
                best=sim; best_i=i
        if best_i is not None and best>=threshold:
            clusters[best_i].append(lig)
        else:
            reps.append(sh); clusters.append([lig])
        lig.update({'estimated_cost':round(cost,2),'valid':True,'fallback_cluster':True})
    out=[]
    for cid,rows in enumerate(clusters):
        for r in rows:
            r['cluster_id']=f'F{cid:05d}'
            out.append(r)
    return out


def split_cluster_balanced(rows, target_chunk_size, max_chunk_cost=None):
    """Split one similarity cluster into balanced chunks. Keeps similar molecules together as much as possible."""
    if not rows: return []
    # Number of chunks by size and optional cost.
    total_cost=sum(float(r.get('estimated_cost',1)) for r in rows)
    n_by_size=math.ceil(len(rows)/target_chunk_size)
    n_by_cost=math.ceil(total_cost/max_chunk_cost) if max_chunk_cost else 1
    n=max(1,n_by_size,n_by_cost)
    # Greedy bin-packing by estimated cost for balanced walltime.
    bins=[{'cost':0.0,'rows':[]} for _ in range(n)]
    for r in sorted(rows, key=lambda x: float(x.get('estimated_cost',1)), reverse=True):
        b=min(bins, key=lambda x: (x['cost'], len(x['rows'])))
        b['rows'].append(r); b['cost'] += float(r.get('estimated_cost',1))
    return bins


def make_chunks(ligs, target_chunk_size=500, subchunk_size=100, max_chunk_cost=None):
    """Create balanced chunks without creating thousands of singleton jobs.

    Earlier version treated every similarity cluster as its own chunk. That is bad for
    diverse libraries: 10,000 singleton clusters would create 10,000 tiny jobs. This
    version keeps large/congeneric clusters together or split into several chunks,
    while packing small clusters together into mixed chunks by estimated docking cost.
    """
    by_cluster=defaultdict(list)
    for lig in ligs:
        by_cluster[lig.get('cluster_id','unknown')].append(lig)

    chunks=[]; manifest=[]; chunk_counter=0

    def add_chunk(rows, cluster_label):
        nonlocal chunk_counter
        if not rows:
            return
        chunk_id=f'chunk_{chunk_counter:05d}'
        sorted_rows=sorted(rows, key=lambda x: float(x.get('estimated_cost',1)), reverse=True)
        for i,r in enumerate(sorted_rows):
            r['chunk_id']=chunk_id
            r['subchunk_id']=f'{chunk_id}_sub_{i//subchunk_size:03d}' if subchunk_size else chunk_id
        chunks.append((chunk_id, sorted_rows))
        manifest.append({
            'chunk_id':chunk_id,
            'cluster_id':cluster_label,
            'n':len(sorted_rows),
            'estimated_cost':round(sum(float(r.get('estimated_cost',1)) for r in sorted_rows),2),
            'subchunks':len(set(r['subchunk_id'] for r in sorted_rows)),
            'mixed_clusters':len(set(r.get('cluster_id','unknown') for r in sorted_rows)),
        })
        chunk_counter+=1

    # 1) Split clusters that exceed chunk size/cost target.
    small_clusters=[]
    for cluster_id, rows in sorted(by_cluster.items(), key=lambda kv: len(kv[1]), reverse=True):
        total_cost=sum(float(r.get('estimated_cost',1)) for r in rows)
        too_big_by_size=len(rows) > target_chunk_size
        too_big_by_cost=bool(max_chunk_cost and total_cost > max_chunk_cost)
        if too_big_by_size or too_big_by_cost:
            bins=split_cluster_balanced(rows, target_chunk_size, max_chunk_cost)
            for b in bins:
                add_chunk(b['rows'], cluster_id)
        else:
            small_clusters.append((cluster_id, rows, total_cost))

    # 2) Pack small clusters together to avoid tiny jobs.
    packed=[]
    for cluster_id, rows, cost in sorted(small_clusters, key=lambda x: x[2], reverse=True):
        placed=False
        # keep clusters intact when possible; choose least-filled compatible bin
        candidates=[]
        for i,b in enumerate(packed):
            new_n=b['n']+len(rows)
            new_cost=b['cost']+cost
            if new_n <= target_chunk_size and (not max_chunk_cost or new_cost <= max_chunk_cost):
                candidates.append((b['cost'], i))
        if candidates:
            _, idx=min(candidates)
            packed[idx]['rows'].extend(rows); packed[idx]['n']+=len(rows); packed[idx]['cost']+=cost; packed[idx]['clusters'].append(cluster_id)
            placed=True
        if not placed:
            packed.append({'rows':list(rows),'n':len(rows),'cost':cost,'clusters':[cluster_id]})
    for b in packed:
        label='mixed:' + ','.join(b['clusters'][:5]) + ('...' if len(b['clusters'])>5 else '')
        add_chunk(b['rows'], label)

    return chunks, manifest


def write_outputs(chunks, manifest, outdir, docking_command_template):
    """Write chunks and self-contained runner scripts.

    Generated runner scripts cd to their own directory and use subchunk paths
    relative to that directory. This makes both of these work:
      bash chunks/run_all_subchunks.sh
      cd chunks && bash run_all_subchunks.sh
    """
    out = Path(outdir)
    out.mkdir(parents=True, exist_ok=True)
    subdir = out / 'subchunks'
    subdir.mkdir(exist_ok=True)
    all_rows = []
    sub_files = []

    for chunk_id, rows in chunks:
        write_csv(out / f'{chunk_id}.csv', rows)
        all_rows.extend(rows)
        by_sub = defaultdict(list)
        for r in rows:
            by_sub[r['subchunk_id']].append(r)
        for sid, srows in by_sub.items():
            fp = subdir / f'{sid}.csv'
            write_csv(fp, srows)
            sub_files.append(Path('subchunks') / f'{sid}.csv')  # relative to outdir

    write_csv(out / 'all_chunked_ligands.csv', all_rows)
    (out / 'manifest.json').write_text(json.dumps(manifest, indent=2))

    # Sequential local runner.
    lines = [
        '#!/usr/bin/env bash',
        'set -euo pipefail',
        'SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
        'cd "$SCRIPT_DIR"',
        'mkdir -p job_logs',
    ]
    for rel in sub_files:
        stem = Path(rel).stem
        cmd = docking_command_template.replace('{input}', str(rel)).replace('{stem}', stem)
        lines.append(f'echo Running {rel}')
        lines.append(f'{cmd} > job_logs/{stem}.log 2>&1')
    (out / 'run_all_subchunks.sh').write_text('\n'.join(lines) + '\n')
    os.chmod(out / 'run_all_subchunks.sh', 0o755)

    # GNU parallel runner for speed.
    (out / 'subchunk_files.txt').write_text('\n'.join(str(p) for p in sub_files) + '\n')
    parallel_cmd = docking_command_template.replace('{input}', '{}').replace('{stem}', '$stem')
    par_lines = [
        '#!/usr/bin/env bash',
        'set -euo pipefail',
        'SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"',
        'cd "$SCRIPT_DIR"',
        'JOBS=${JOBS:-4}',
        'mkdir -p job_logs',
        'if ! command -v parallel >/dev/null 2>&1; then',
        '  echo "GNU parallel not found. Install it or run: bash run_all_subchunks.sh" >&2',
        '  exit 127',
        'fi',
        'cat subchunk_files.txt | parallel -j "$JOBS" --line-buffer \'',
        '  stem=$(basename {} .csv)',
        '  echo Running {}',
        f'  {parallel_cmd} > job_logs/${{stem}}.log 2>&1',
        "'",
    ]
    (out / 'run_parallel_subchunks.sh').write_text('\n'.join(par_lines) + '\n')
    os.chmod(out / 'run_parallel_subchunks.sh', 0o755)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--out', default='chunks')
    ap.add_argument('--similarity-threshold', type=float, default=0.65, help='Butina/Tanimoto threshold; higher = tighter clusters')
    ap.add_argument('--target-chunk-size', type=int, default=500)
    ap.add_argument('--subchunk-size', type=int, default=100)
    ap.add_argument('--max-chunk-cost', type=float, help='optional estimated-cost cap per chunk')
    ap.add_argument('--target-pdb', default='1LPB')
    ap.add_argument('--quality', default='standard')
    ap.add_argument('--total-cpu', default='1', help='CPUs allocated inside each subchunk job; keep low when also using JOBS parallelism')
    ap.add_argument('--cpu-per-dock', default='1')
    ap.add_argument('--gi-mode', default='intestinal')
    args=ap.parse_args()

    ligs=read_ligands(args.input)
    clustered=rdkit_cluster(ligs, threshold=args.similarity_threshold)
    chunks, manifest=make_chunks(clustered, args.target_chunk_size, args.subchunk_size, args.max_chunk_cost)
    pipeline = Path(__file__).resolve().parent / 'docking_speed_pipeline.py'
    template=(
        f"python {pipeline} --input {{input}} --target-pdb {args.target_pdb} --mode dock "
        f"--quality {args.quality} --total-cpu {args.total_cpu} --cpu-per-dock {args.cpu_per_dock} "
        f"--gi-mode {args.gi_mode} --quiet --no-html --run-id {{stem}}"
    )
    write_outputs(chunks, manifest, args.out, template)
    ns=[m['n'] for m in manifest]; costs=[m['estimated_cost'] for m in manifest]
    print(f"Ligands: {len(clustered)}")
    print(f"Chunks: {len(manifest)}; subchunk files written under {args.out}/subchunks")
    if ns:
        print(f"Chunk size mean={statistics.mean(ns):.1f}, max={max(ns)}, min={min(ns)}")
        print(f"Cost mean={statistics.mean(costs):.1f}, max={max(costs):.1f}, min={min(costs):.1f}")
    print(f"Manifest: {args.out}/manifest.json")
    print(f"Run local sequential: bash {args.out}/run_all_subchunks.sh")
    print(f"Run parallel: cd {args.out} && JOBS=8 bash run_parallel_subchunks.sh")

if __name__=='__main__':
    main()
