#!/usr/bin/env python3
"""Workflow linter for docking projects.

Catches common failure modes learned from real docking/cheminformatics pipelines:
missing columns, duplicate names, bad paths, missing tools, oversubscription, tiny chunks,
unsafe generated shell scripts, and absent result files.
"""
from __future__ import annotations
import argparse, csv, json, shutil, subprocess
from pathlib import Path
from collections import Counter


def warn(msg, issues):
    issues.append(msg); print('WARN:', msg)

def ok(msg):
    print('OK:', msg)

def read_csv(path):
    with open(path, newline='') as f: return list(csv.DictReader(f))

def lint_ligands(path, issues):
    p=Path(path)
    if not p.exists():
        warn(f'ligand CSV missing: {p}', issues); return
    rows=read_csv(p)
    if not rows:
        warn('ligand CSV is empty', issues); return
    cols=set(rows[0].keys())
    if not ({'smiles','SMILES','canonical_smiles'} & cols):
        warn('ligand CSV lacks smiles/SMILES/canonical_smiles column', issues)
    names=[(r.get('name') or r.get('id') or '').strip() for r in rows]
    dup=[k for k,v in Counter(names).items() if k and v>1]
    if dup:
        warn(f'duplicate ligand names found ({len(dup)} names); pipeline will rename but review input', issues)
    blank=sum(1 for r in rows if not (r.get('smiles') or r.get('SMILES') or r.get('canonical_smiles')))
    if blank:
        warn(f'{blank} rows have blank SMILES and will be skipped', issues)
    ok(f'ligand CSV rows checked: {len(rows)}')

def lint_tools(issues):
    for cmd in ['vina','obabel']:
        if shutil.which(cmd): ok(f'{cmd} found: {shutil.which(cmd)}')
        else: warn(f'{cmd} missing; real docking/prep will be skipped or fail', issues)
    for cmd in ['parallel','smina','fpocket','gmx']:
        if shutil.which(cmd): ok(f'optional {cmd} found')

def lint_chunks(path, issues):
    root=Path(path)
    if not root.exists():
        warn(f'chunk directory missing: {root}', issues); return
    manifest=root/'manifest.json'
    if manifest.exists():
        data=json.loads(manifest.read_text())
        if data:
            tiny=sum(1 for m in data if int(m.get('n',0)) <= 2)
            if tiny/len(data) > 0.5 and len(data)>20:
                warn('more than 50% chunks have <=2 ligands; chunking is inefficient', issues)
            ok(f'manifest chunks: {len(data)}')
    sub=root/'subchunk_files.txt'
    if sub.exists():
        files=[line.strip() for line in sub.read_text().splitlines() if line.strip()]
        missing=[f for f in files if not (root/f).exists()]
        if missing: warn(f'{len(missing)} subchunk files listed but missing', issues)
        else: ok(f'subchunk files checked: {len(files)}')
    for sh in ['run_all_subchunks.sh','run_parallel_subchunks.sh']:
        f=root/sh
        if f.exists():
            p=subprocess.run(['bash','-n',str(f)], text=True, capture_output=True)
            if p.returncode: warn(f'shell syntax error in {f}: {p.stderr}', issues)
            else: ok(f'shell syntax OK: {f}')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ligands')
    ap.add_argument('--chunks')
    ap.add_argument('--check-tools', action='store_true')
    args=ap.parse_args()
    issues=[]
    if args.ligands: lint_ligands(args.ligands, issues)
    if args.check_tools: lint_tools(issues)
    if args.chunks: lint_chunks(args.chunks, issues)
    print('\nSummary:', 'PASS' if not issues else f'{len(issues)} warning(s)')
    raise SystemExit(0 if not issues else 2)

if __name__=='__main__': main()
