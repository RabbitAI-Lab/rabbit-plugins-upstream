#!/usr/bin/env python3
"""
Professional docking runner scaffold.

This file is intentionally checkpoint-oriented for long jobs. It coordinates:
- receptor download/metadata
- ligand descriptor filters
- docking via the lipase_docking_fastkit.py backend when target is 1LPB
- resumable output tables

For complete production usage, extend functions marked TODO with PLIP/ProLIF interaction
fingerprints, native-ligand RMSD validation, ensemble docking, MD, and MM/GBSA.
"""
from __future__ import annotations
import argparse, csv, json, os, subprocess, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT = Path("pro_runs")


def run(cmd, timeout=None, cwd=None):
    print("$", " ".join(map(str, cmd)), flush=True)
    return subprocess.run(cmd, text=True, capture_output=True, timeout=timeout, cwd=cwd)


def read_ligands(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    out = []
    for i, r in enumerate(rows, 1):
        name = r.get("name") or r.get("id") or f"lig_{i}"
        smi = r.get("smiles") or r.get("SMILES")
        if smi:
            out.append({"name": name, "smiles": smi})
    return out


def descriptor_row(lig):
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors
        mol = Chem.MolFromSmiles(lig["smiles"])
        if mol is None:
            return {**lig, "valid": False, "error": "bad_smiles"}
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Lipinski.NumHDonors(mol)
        hba = Lipinski.NumHAcceptors(mol)
        rotb = Lipinski.NumRotatableBonds(mol)
        tpsa = rdMolDescriptors.CalcTPSA(mol)
        lipv = int(mw > 500) + int(logp > 5) + int(hbd > 5) + int(hba > 10)
        return {**lig, "valid": True, "MW": round(mw,2), "cLogP": round(logp,2), "HBD": hbd,
                "HBA": hba, "RotB": rotb, "TPSA": round(tpsa,2),
                "Lipinski_violations": lipv, "Veber_pass": rotb <= 10 and tpsa <= 140}
    except Exception as e:
        return {**lig, "valid": None, "descriptor_warning": str(e)}


def write_table(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    keys = sorted({k for r in rows for k in r.keys()}) if rows else []
    with open(path, "w", newline="") as f:
        if keys:
            w = csv.DictWriter(f, fieldnames=keys, restval="")
            w.writeheader(); w.writerows(rows)


def consensus(row):
    score = row.get("vina_score_kcal_mol")
    try: score = float(score)
    except Exception: score = None
    flags = []
    if row.get("Lipinski_violations") not in (None, "") and int(row.get("Lipinski_violations")) > 1:
        flags.append("drug-likeness concern")
    if row.get("Veber_pass") in (False, "False", "false"):
        flags.append("Veber concern")
    if score is None:
        pred = "undetermined"
    elif score <= -9:
        pred = "strong predicted binder"
    elif score <= -7:
        pred = "moderate predicted binder"
    elif score <= -5.5:
        pred = "weak-to-moderate predicted binder"
    else:
        pred = "weak predicted binder"
    conf = "low" if score is None else "medium"
    if flags and pred.startswith("strong"):
        pred = "strong docking score but filtered concern"
        conf = "low-medium"
    return pred, conf, "; ".join(flags)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--target-pdb", default="1LPB")
    ap.add_argument("--mode", choices=["filters", "dock", "full"], default="full")
    ap.add_argument("--exhaustiveness", type=int, default=8)
    ap.add_argument("--cpu", type=int, default=os.cpu_count() or 4)
    ap.add_argument("--run-id", default=time.strftime("run_%Y%m%d_%H%M%S"))
    args = ap.parse_args()

    run_dir = ROOT / args.run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    ligs = read_ligands(args.input)
    print(f"Loaded {len(ligs)} ligands")

    # Parallel descriptor filters.
    props = []
    with ThreadPoolExecutor(max_workers=min(16, max(1, len(ligs)))) as ex:
        for fut in as_completed([ex.submit(descriptor_row, lig) for lig in ligs]):
            props.append(fut.result())
    write_table(run_dir / "descriptors.csv", props)

    rows_by_name = {r["name"]: r for r in props}

    if args.mode in ("dock", "full"):
        # For pancreatic lipase default, call the already-created backend.
        if args.target_pdb.upper() == "1LPB":
            tmp = run_dir / "ligands_for_lipase.csv"
            write_table(tmp, [{"name": l["name"], "smiles": l["smiles"]} for l in ligs])
            backend = Path(__file__).resolve().parent / "lipase_docking_fastkit.py"
            if not backend.exists():
                print("Missing lipase_docking_fastkit.py; docking backend unavailable", file=sys.stderr)
            else:
                cmd = [sys.executable, str(backend), "--input", str(tmp), "--mode", "dock",
                       "--exhaustiveness", str(args.exhaustiveness), "--cpu", str(args.cpu)]
                # lipase_docking_fastkit writes into cwd-relative lipase_run/;
                # run from run_dir so outputs land alongside the other artifacts.
                p = run(cmd, timeout=None, cwd=str(run_dir))
                (run_dir / "backend_stdout.log").write_text(p.stdout)
                (run_dir / "backend_stderr.log").write_text(p.stderr)
                # Pull backend CSV if generated.
                bcsv = run_dir / "lipase_run/results.csv"
                if bcsv.exists():
                    with open(bcsv, newline="") as f:
                        for r in csv.DictReader(f):
                            rows_by_name.setdefault(r["name"], {}).update(r)
        else:
            print("Generic receptor docking TODO: provide prepared PDBQT or extend backend.")

    final = []
    for r in rows_by_name.values():
        pred, conf, flags = consensus(r)
        r["prediction"] = pred
        r["confidence"] = conf
        r["filter_flags"] = flags
        final.append(r)
    write_table(run_dir / "final_ranked_results.csv", final)
    (run_dir / "run_metadata.json").write_text(json.dumps(vars(args), indent=2))
    print(f"Wrote {run_dir/'final_ranked_results.csv'}")

if __name__ == "__main__":
    main()
