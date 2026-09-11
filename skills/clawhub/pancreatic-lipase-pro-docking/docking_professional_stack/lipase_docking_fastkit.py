#!/usr/bin/env python3
"""
FastKit: template pipeline for human pancreatic lipase inhibition docking.

Purpose: a simple, reusable workflow that can screen ligands against human pancreatic
lipase quickly when dependencies are installed. It runs ligand preparation, molecular
docking one-by-one, and parallel in-silico property filters.

Core target defaults:
- Human pancreatic lipase PDB: 1LPB
- Catalytic triad: Ser152, Asp176, His263
- Grid center: co-crystallized ligand centroid if found, otherwise catalytic triad centroid

Required external tools for real docking:
- AutoDock Vina executable: vina
- Open Babel executable: obabel
Optional but recommended:
- RDKit Python package for descriptors/PAINS-like filters

Example:
  python lipase_docking_fastkit.py --demo --mode dry
  python lipase_docking_fastkit.py --input ligands.csv --mode dock --exhaustiveness 4 --cpu 4

CSV format:
  name,smiles
  orlistat,CCCCCCCCCCCC[C@H](OC(=O)[C@H](CC(C)C)NC=O)C1OC1=O
"""

from __future__ import annotations
import argparse, csv, json, os, shutil, subprocess, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from statistics import mean

ROOT = Path("lipase_run")
PDB_ID = "1LPB"
PDB_URL = f"https://files.rcsb.org/download/{PDB_ID}.pdb"
DEFAULT_BOX_SIZE = (22.0, 22.0, 22.0)
CATALYTIC_RESIDUES = {152, 176, 263}
DEMO_LIGANDS = [
    # Use as pipeline smoke-test examples, not as final scientific claims.
    ("orlistat_control", "CCCCCCCCCCCC[C@H](OC(=O)[C@H](CC(C)C)NC=O)C1OC1=O"),
    ("quercetin", "O=c1c(O)c(-c2ccc(O)c(O)c2)oc2cc(O)cc(O)c12"),
    ("kaempferol", "O=c1c(O)c(-c2ccc(O)cc2)oc2cc(O)cc(O)c12"),
]


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def run(cmd, cwd=None, timeout=300):
    print("$", " ".join(map(str, cmd)))
    return subprocess.run(cmd, cwd=cwd, check=True, text=True, capture_output=True, timeout=timeout)


def download_receptor() -> Path:
    ROOT.mkdir(exist_ok=True)
    pdb = ROOT / f"{PDB_ID}.pdb"
    if not pdb.exists():
        print(f"Downloading {PDB_ID} from RCSB...")
        urllib.request.urlretrieve(PDB_URL, pdb)
    return pdb


def parse_pdb_atoms(pdb: Path):
    atoms = []
    for line in pdb.read_text(errors="ignore").splitlines():
        if line.startswith(("ATOM  ", "HETATM")):
            try:
                rec = line[:6].strip()
                resn = line[17:20].strip()
                chain = line[21].strip()
                resi = int(line[22:26])
                x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
                atoms.append((rec, resn, chain, resi, x, y, z, line))
            except Exception:
                pass
    return atoms


def centroid(coords):
    return tuple(round(mean([c[i] for c in coords]), 3) for i in range(3))


def choose_grid_center(pdb: Path):
    atoms = parse_pdb_atoms(pdb)
    # Prefer co-crystallized inhibitor/ligand MUP if present; this captures the known binding pocket.
    mup = [(x, y, z) for rec, resn, chain, resi, x, y, z, line in atoms if rec == "HETATM" and resn == "MUP"]
    if mup:
        return centroid(mup), "MUP ligand centroid"
    triad = [(x, y, z) for rec, resn, chain, resi, x, y, z, line in atoms if rec == "ATOM" and resi in CATALYTIC_RESIDUES]
    if triad:
        return centroid(triad), "Ser152/Asp176/His263 centroid"
    raise RuntimeError("Could not infer active site center from receptor.")


def clean_protein_pdb(pdb: Path) -> Path:  # v100.4: drop altloc B+, keep first altLoc
    """Remove waters and non-protein HETATMs; keep ATOM records only for simple conversion."""
    out = ROOT / "receptor_clean.pdb"
    lines = []
    for line in pdb.read_text(errors="ignore").splitlines():
        if line.startswith("ATOM  "):
            alt = line[16] if len(line) > 16 else " "
            if alt not in (" ", "A"):
                continue
            lines.append(line)
    out.write_text("\n".join(lines) + "\n")
    return out


def prepare_receptor_pdbqt(pdb: Path) -> Path:
    pdbqt = ROOT / "receptor.pdbqt"
    if pdbqt.exists():
        return pdbqt
    clean = clean_protein_pdb(pdb)
    if have("mk_prepare_receptor.py"):
        # Meeko receptor preparation if available.
        run(["mk_prepare_receptor.py", "-i", str(clean), "-o", str(ROOT / "receptor"), "-p"])
        if pdbqt.exists():
            return pdbqt
    if have("obabel"):
        # Simple fallback. For publication-grade work, inspect protonation/charges manually.
        run(["obabel", str(clean), "-O", str(pdbqt), "-xh"])
        return pdbqt
    raise RuntimeError("Need mk_prepare_receptor.py or obabel to prepare receptor PDBQT.")


def load_ligands(args):
    if args.demo:
        return DEMO_LIGANDS
    if not args.input:
        raise SystemExit("Provide --input ligands.csv or use --demo")
    ligs = []
    with open(args.input, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ligs.append((row.get("name") or row.get("id") or f"lig_{len(ligs)+1}", row["smiles"]))
    return ligs


def rdkit_properties(name, smiles):
    """Parallelizable in-silico property tests. Falls back gracefully if RDKit is absent."""
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return {"name": name, "smiles": smiles, "valid": False, "error": "bad_smiles"}
        mw = Descriptors.MolWt(mol)
        logp = Descriptors.MolLogP(mol)
        hbd = Lipinski.NumHDonors(mol)
        hba = Lipinski.NumHAcceptors(mol)
        rotb = Lipinski.NumRotatableBonds(mol)
        tpsa = rdMolDescriptors.CalcTPSA(mol)
        lipinski_viol = int(mw > 500) + int(logp > 5) + int(hbd > 5) + int(hba > 10)
        veber_pass = (rotb <= 10 and tpsa <= 140)
        # A rough oral/intestinal heuristic, not a substitute for ADMET software.
        gi_absorption_hint = "high" if (tpsa <= 140 and rotb <= 10 and mw <= 500) else "low/uncertain"
        return {
            "name": name, "smiles": smiles, "valid": True,
            "MW": round(mw, 2), "cLogP": round(logp, 2), "HBD": hbd, "HBA": hba,
            "RotB": rotb, "TPSA": round(tpsa, 2),
            "Lipinski_violations": lipinski_viol, "Veber_pass": veber_pass,
            "GI_absorption_hint": gi_absorption_hint,
        }
    except Exception as e:
        return {"name": name, "smiles": smiles, "valid": None, "warning": f"RDKit unavailable or failed: {e}"}


def prepare_ligand(name, smiles) -> Path:
    safe = "".join(c if c.isalnum() or c in "_-" else "_" for c in name)[:80]
    ligdir = ROOT / "ligands" / safe
    ligdir.mkdir(parents=True, exist_ok=True)
    smi = ligdir / f"{safe}.smi"
    mol2 = ligdir / f"{safe}.mol2"
    pdbqt = ligdir / f"{safe}.pdbqt"
    smi.write_text(f"{smiles}\t{name}\n")
    if not have("obabel"):
        raise RuntimeError("Need obabel for ligand 3D/PDBQT preparation.")
    run(["obabel", str(smi), "-O", str(mol2), "--gen3d", "--best", "--addhydrogens"], timeout=300)
    run(["obabel", str(mol2), "-O", str(pdbqt), "--partialcharge", "gasteiger"], timeout=120)
    return pdbqt


def dock_one(name, smiles, receptor_pdbqt, center, size, exhaustiveness, cpu):
    safe = "".join(c if c.isalnum() or c in "_-" else "_" for c in name)[:80]
    out_pdbqt = ROOT / "docked" / f"{safe}_out.pdbqt"
    log = ROOT / "docked" / f"{safe}_vina.log"
    out_pdbqt.parent.mkdir(exist_ok=True)
    lig_pdbqt = prepare_ligand(name, smiles)
    cmd = [
        "vina", "--receptor", str(receptor_pdbqt), "--ligand", str(lig_pdbqt),
        "--center_x", str(center[0]), "--center_y", str(center[1]), "--center_z", str(center[2]),
        "--size_x", str(size[0]), "--size_y", str(size[1]), "--size_z", str(size[2]),
        "--exhaustiveness", str(exhaustiveness), "--cpu", str(cpu),
        "--out", str(out_pdbqt),
    ]
    run(cmd, timeout=900)
    score = None
    txt = log.read_text(errors="ignore") if log.exists() else ""
    for line in txt.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0] == "1":
            try:
                score = float(parts[1])
                break
            except Exception:
                pass
    return {"name": name, "vina_score_kcal_mol": score, "pose": str(out_pdbqt), "log": str(log)}


def prediction_label(score):
    if score is None:
        return "undetermined"
    if score <= -9.0:
        return "strong predicted binder"
    if score <= -7.0:
        return "moderate predicted binder"
    if score <= -5.5:
        return "weak-to-moderate predicted binder"
    return "weak predicted binder"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="CSV with columns name,smiles")
    ap.add_argument("--demo", action="store_true", help="Use three demo ligands for smoke testing")
    ap.add_argument("--mode", choices=["dry", "dock"], default="dry", help="dry=properties/grid only; dock=run Vina")
    ap.add_argument("--exhaustiveness", type=int, default=4)
    ap.add_argument("--cpu", type=int, default=max(1, os.cpu_count() or 1))
    ap.add_argument("--box", nargs=3, type=float, default=DEFAULT_BOX_SIZE)
    args = ap.parse_args()

    ROOT.mkdir(exist_ok=True)
    ligands = load_ligands(args)
    pdb = download_receptor()
    center, center_method = choose_grid_center(pdb)

    print(f"Target: human pancreatic lipase {PDB_ID}")
    print(f"Grid center: {center} ({center_method}); size={tuple(args.box)}")

    # Run in-silico property tests concurrently.
    props = []
    with ThreadPoolExecutor(max_workers=min(8, len(ligands) or 1)) as ex:
        futs = [ex.submit(rdkit_properties, n, s) for n, s in ligands]
        for fut in as_completed(futs):
            props.append(fut.result())

    docked = []
    if args.mode == "dock":
        if not have("vina"):
            raise RuntimeError("AutoDock Vina executable 'vina' not found.")
        receptor = prepare_receptor_pdbqt(pdb)
        # Docking intentionally runs one-by-one to keep logs/reproducibility clean.
        for name, smiles in ligands:
            docked.append(dock_one(name, smiles, receptor, center, tuple(args.box), args.exhaustiveness, args.cpu))
    else:
        docked = [{"name": n, "vina_score_kcal_mol": None, "note": "dry run: docking not executed"} for n, s in ligands]

    by_name = {p["name"]: p for p in props}
    rows = []
    for d in docked:
        row = {**by_name.get(d["name"], {}), **d}
        row["prediction"] = prediction_label(row.get("vina_score_kcal_mol"))
        rows.append(row)

    rows.sort(key=lambda r: (r.get("vina_score_kcal_mol") is None, r.get("vina_score_kcal_mol") or 999))
    out_json = ROOT / "results.json"
    out_csv = ROOT / "results.csv"
    out_json.write_text(json.dumps({"target": PDB_ID, "grid_center": center, "center_method": center_method, "results": rows}, indent=2))
    keys = sorted({k for r in rows for k in r.keys()})
    with out_csv.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {out_csv} and {out_json}")
    for r in rows:
        print(f"{r['name']}: score={r.get('vina_score_kcal_mol')} prediction={r['prediction']} LipinskiViol={r.get('Lipinski_violations')}")


if __name__ == "__main__":
    main()
