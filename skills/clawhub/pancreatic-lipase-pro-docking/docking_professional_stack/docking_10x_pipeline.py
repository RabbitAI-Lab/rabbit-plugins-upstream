#!/usr/bin/env python3
"""
docking_10x_pipeline.py

A professional, checkpointed docking/screening orchestrator scaffold.
It is designed to make the assistant operationally ready for serious docking work:
- receptor fetching and active-site inference
- ligand descriptor filters + PAINS alerts
- optional receptor/ligand preparation using external tools
- optional docking using AutoDock Vina
- resumable per-ligand execution
- consensus ranking
- HTML report generation

This script is intentionally dependency-tolerant: it runs filters/reporting with RDKit if
available, and clearly reports missing external executables for real docking.

Typical:
  python docking_10x_pipeline.py --target-pdb 1LPB --input ligands.csv --mode dry
  python docking_10x_pipeline.py --target-pdb 1LPB --input ligands.csv --mode dock --exhaustiveness 8 --cpu 8
"""
from __future__ import annotations

import argparse, csv, html, json, os, re, shutil, subprocess, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from statistics import mean

RUNS = Path("10x_runs")
DEFAULT_BOX = (22.0, 22.0, 22.0)
PANCREATIC_LIPASE = {
    "pdb": "1LPB",
    # NOTE: PDB 1LPB is a human pancreatic lipase + colipase + inhibitor (MUP)
    # closed-lid complex. Different publications and UniProt use different
    # residue-numbering conventions for the catalytic triad: deposited PDB
    # indices are Ser152/Asp176/His263; many enzymology references (and some
    # SAR papers) use the mature-protein (UniProt P16233) numbering which is
    # offset by +1 (Ser153/Asp177/His263). The actual atomic coordinates are
    # identical; this is purely a convention difference to keep in mind when
    # mapping literature residue numbers to the PDB.
    "native_ligand": "MUP",
    "triad": [152, 176, 263],
    "triad_mature_numbering": [153, 177, 263],
    "key_residues": [77, 114, 152, 153, 176, 213, 215, 256, 263, 264],
    "description": "Human pancreatic lipase active-site model; MUP/catalytic triad pocket.",
}


def which(cmd: str) -> str | None:
    return shutil.which(cmd)


def run(cmd, timeout=None, cwd=None):
    p = subprocess.run(cmd, text=True, capture_output=True, timeout=timeout, cwd=cwd)
    return p.returncode, p.stdout, p.stderr


def read_ligands(path: Path):
    with path.open(newline="") as f:
        rows = list(csv.DictReader(f))
    ligs = []
    for i, r in enumerate(rows, 1):
        # csv.DictReader puts unparseable extra columns under key=None when a row
        # has more commas than the header; join them back into a `_extra` field
        # rather than letting a None key propagate.
        extras = r.pop(None, None)
        name = (r.get("name") or r.get("id") or f"lig_{i}").strip()
        smiles = (r.get("smiles") or r.get("SMILES") or r.get("canonical_smiles") or "").strip()
        if not smiles:
            continue
        entry = {"name": name, "smiles": smiles}
        # Carry through all extra columns (reference_ic50_um, notes, etc.) verbatim.
        for k, v in r.items():
            if k in {"name", "id", "smiles", "SMILES", "canonical_smiles"}:
                continue
            if v is None or v == "":
                continue
            entry[k] = v
        if extras:
            existing_notes = entry.get("notes", "")
            joined = ",".join(extras) if isinstance(extras, list) else str(extras)
            entry["notes"] = (existing_notes + "," + joined).strip(",") if existing_notes else joined
        ligs.append(entry)
    return ligs


def safe_name(s):
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", s)[:100]


def fetch_pdb(pdb_id: str, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    pdb = outdir / f"{pdb_id.upper()}.pdb"
    if not pdb.exists():
        url = f"https://files.rcsb.org/download/{pdb_id.upper()}.pdb"
        urllib.request.urlretrieve(url, pdb)
    return pdb


def parse_atoms(pdb: Path):
    atoms = []
    for line in pdb.read_text(errors="ignore").splitlines():
        if line.startswith(("ATOM  ", "HETATM")):
            try:
                atoms.append({
                    "record": line[:6].strip(), "atom": line[12:16].strip(), "resn": line[17:20].strip(),
                    "chain": line[21].strip(), "resi": int(line[22:26]),
                    "x": float(line[30:38]), "y": float(line[38:46]), "z": float(line[46:54]), "line": line,
                })
            except Exception:
                continue
    return atoms


def centroid(coords):
    return tuple(round(mean([c[i] for c in coords]), 3) for i in range(3))


def infer_grid(pdb: Path, target_pdb: str):
    atoms = parse_atoms(pdb)
    spec = PANCREATIC_LIPASE if target_pdb.upper() == "1LPB" else None
    if spec:
        lig = spec["native_ligand"]
        coords = [(a["x"], a["y"], a["z"]) for a in atoms if a["record"] == "HETATM" and a["resn"] == lig]
        if coords:
            return {"center": centroid(coords), "method": f"native ligand {lig} centroid", "box": DEFAULT_BOX}
        triad = set(spec["triad"])
        coords = [(a["x"], a["y"], a["z"]) for a in atoms if a["record"] == "ATOM" and a["resi"] in triad]
        if coords:
            return {"center": centroid(coords), "method": "catalytic triad centroid", "box": DEFAULT_BOX}
    # generic fallback: all HETATM non-water centroid
    coords = [(a["x"], a["y"], a["z"]) for a in atoms if a["record"] == "HETATM" and a["resn"] not in {"HOH", "WAT"}]
    if coords:
        return {"center": centroid(coords), "method": "all non-water HETATM centroid", "box": DEFAULT_BOX}
    raise RuntimeError("Could not infer grid center. Provide a prepared grid manually.")


def extract_native_ligand_pdb(pdb: Path, ligand_resn: str, outdir: Path) -> Path | None:
    lines = [a["line"] for a in parse_atoms(pdb) if a["record"] == "HETATM" and a["resn"] == ligand_resn]
    if not lines:
        return None
    out = outdir / f"native_{ligand_resn}.pdb"
    out.write_text("\n".join(lines) + "\nEND\n")
    return out


def clean_receptor_pdb(pdb: Path, outdir: Path) -> Path:
    out = outdir / "receptor_clean.pdb"
    lines = [line for line in pdb.read_text(errors="ignore").splitlines() if line.startswith("ATOM  ")]
    out.write_text("\n".join(lines) + "\nEND\n")
    return out


def rdkit_filters(lig):
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors
        from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams
    except Exception as e:
        return {**lig, "valid": None, "filter_error": f"RDKit unavailable: {e}"}
    mol = Chem.MolFromSmiles(lig["smiles"])
    if mol is None:
        return {**lig, "valid": False, "filter_error": "invalid SMILES"}
    mw = Descriptors.MolWt(mol); logp = Descriptors.MolLogP(mol)
    hbd = Lipinski.NumHDonors(mol); hba = Lipinski.NumHAcceptors(mol)
    rotb = Lipinski.NumRotatableBonds(mol); tpsa = rdMolDescriptors.CalcTPSA(mol)
    lipv = int(mw > 500) + int(logp > 5) + int(hbd > 5) + int(hba > 10)
    pains = []
    try:
        params = FilterCatalogParams()
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_A)
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_B)
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_C)
        catalog = FilterCatalog(params)
        matches = catalog.GetMatches(mol)
        pains = [m.GetDescription() for m in matches]
    except Exception as e:
        pains = [f"PAINS check failed: {e}"]
    return {
        **lig, "valid": True, "MW": round(mw, 2), "cLogP": round(logp, 2), "HBD": hbd, "HBA": hba,
        "RotB": rotb, "TPSA": round(tpsa, 2), "Lipinski_violations": lipv,
        "Veber_pass": bool(rotb <= 10 and tpsa <= 140), "PAINS_alerts": "; ".join(pains),
        "GI_absorption_hint": "high" if (mw <= 500 and tpsa <= 140 and rotb <= 10) else "low/uncertain",
    }


def prepare_receptor_pdbqt(clean_pdb: Path, outdir: Path):
    pdbqt = outdir / "receptor.pdbqt"
    if pdbqt.exists():
        return pdbqt, "cached"
    # mk_prepare_receptor from Meeko: use --read_pdb (does not require ProDy).
    # Earlier versions used -i/--read_with_prody which fails if ProDy is not installed.
    if which("mk_prepare_receptor.py"):
        rc, so, se = run(["mk_prepare_receptor.py", "--read_pdb", str(clean_pdb),
                          "-o", str(outdir / "receptor"), "-p"], timeout=600)
        if rc == 0 and pdbqt.exists():
            return pdbqt, "meeko"
        # Fallback: try the prody-requiring flag only if prody appears available.
        if which("python"):
            rc2, so2, se2 = run([sys.executable, "-c", "import prody"], timeout=30)
            if rc2 == 0:
                rc, so, se = run(["mk_prepare_receptor.py", "-i", str(clean_pdb),
                                  "-o", str(outdir / "receptor"), "-p"], timeout=600)
                if rc == 0 and pdbqt.exists():
                    return pdbqt, "meeko+prody"
        return None, f"mk_prepare_receptor failed: {se[-500:]}"
    if which("obabel"):
        rc, so, se = run(["obabel", str(clean_pdb), "-O", str(pdbqt), "-xh"], timeout=600)
        if rc == 0 and pdbqt.exists():
            return pdbqt, "openbabel fallback"
        return None, f"obabel receptor failed: {se[-500:]}"
    return None, "missing mk_prepare_receptor.py and obabel"


def prepare_ligand_pdbqt(lig, outdir: Path):
    """Prepare ligand PDBQT.

    Priority:
    1. Open Babel CLI if available.
    2. Pure Python fallback: RDKit 3D conformer + Meeko PDBQT writer.

    This fallback is critical for Arena-like sandboxes where `obabel` may not be
    installed but pip packages (`rdkit`, `meeko`) can be installed automatically.
    """
    ligdir = outdir / "ligands" / safe_name(lig["name"])
    ligdir.mkdir(parents=True, exist_ok=True)
    smi = ligdir / "ligand.smi"; mol2 = ligdir / "ligand.mol2"; pdbqt = ligdir / "ligand.pdbqt"
    if pdbqt.exists():
        return pdbqt, "cached"
    smi.write_text(f"{lig['smiles']}\t{lig['name']}\n")

    if which("obabel"):
        rc, so, se = run(["obabel", str(smi), "-O", str(mol2), "--gen3d", "--best", "--addhydrogens"], timeout=600)
        if rc == 0:
            rc, so, se = run(["obabel", str(mol2), "-O", str(pdbqt), "--partialcharge", "gasteiger"], timeout=300)
            if rc == 0:
                return pdbqt, "openbabel"
        # If Open Babel exists but fails, still try RDKit/Meeko below.
        obabel_err = se[-500:]
    else:
        obabel_err = "obabel not found"

    # Pure Python fallback: RDKit conformer generation + Meeko PDBQT writer.
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem
        from meeko import MoleculePreparation, PDBQTWriterLegacy
        mol = Chem.MolFromSmiles(lig["smiles"])
        if mol is None:
            return None, "RDKit could not parse SMILES"
        mol = Chem.AddHs(mol)
        params = AllChem.ETKDGv3()
        params.randomSeed = 0xC0FFEE
        if AllChem.EmbedMolecule(mol, params) != 0:
            return None, "RDKit 3D embedding failed"
        try:
            if AllChem.MMFFHasAllMoleculeParams(mol):
                AllChem.MMFFOptimizeMolecule(mol, maxIters=500)
            else:
                AllChem.UFFOptimizeMolecule(mol, maxIters=500)
        except Exception:
            pass
        preparator = MoleculePreparation()
        setups = preparator.prepare(mol)
        if not setups:
            return None, "Meeko ligand preparation returned no setups"
        pdbqt_string, ok, err = PDBQTWriterLegacy.write_string(setups[0])
        if not ok:
            return None, f"Meeko PDBQT writer failed: {err}"
        pdbqt.write_text(pdbqt_string)
        return pdbqt, "rdkit+meeko fallback"
    except Exception as e:
        return None, f"ligand prep failed: OpenBabel=({obabel_err}); RDKit/Meeko=({e})"


def parse_vina_score(log: Path):
    if not log.exists(): return None
    for line in log.read_text(errors="ignore").splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[0] == "1":
            try: return float(parts[1])
            except Exception: pass
    return None


def dock_ligand(lig, receptor_pdbqt: Path, grid, outdir: Path, exhaustiveness: int, cpu: int,
                seed: int = 42, n_poses: int = 5):
    ddir = outdir / "dock" / safe_name(lig["name"])
    ddir.mkdir(parents=True, exist_ok=True)
    done = ddir / "done.json"
    if done.exists():
        return json.loads(done.read_text())
    if not which("vina"):
        result = {"name": lig["name"], "docking_status": "skipped", "dock_error": "missing vina"}
        done.write_text(json.dumps(result, indent=2)); return result
    lp, prep = prepare_ligand_pdbqt(lig, outdir)
    if not lp:
        result = {"name": lig["name"], "docking_status": "failed", "dock_error": prep}
        done.write_text(json.dumps(result, indent=2)); return result
    out_pose = ddir / "pose.pdbqt"; log = ddir / "vina.log"
    cx, cy, cz = grid["center"]; sx, sy, sz = grid["box"]
    cmd = ["vina", "--receptor", str(receptor_pdbqt), "--ligand", str(lp),
           "--center_x", str(cx), "--center_y", str(cy),
           "--center_z", str(cz), "--size_x", str(sx), "--size_y", str(sy), "--size_z", str(sz),
           "--exhaustiveness", str(exhaustiveness), "--cpu", str(cpu),
           "--seed", str(seed), "--num_modes", str(n_poses),
           "--out", str(out_pose)]
    rc, so, se = run(cmd, timeout=1800)
    log.write_text(so + "\n" + se)
    result = {"name": lig["name"], "docking_status": "ok" if rc == 0 else "failed",
              "vina_score_kcal_mol": parse_vina_score(log),
              "pose_file": str(out_pose), "vina_log": str(log),
              "dock_error": se[-500:] if rc else "",
              "seed": seed, "exhaustiveness": exhaustiveness, "n_poses_requested": n_poses}
    done.write_text(json.dumps(result, indent=2))
    return result


def prediction(row):
    try: score = float(row.get("vina_score_kcal_mol"))
    except Exception: score = None
    flags = []
    try:
        if int(row.get("Lipinski_violations", 0)) > 1: flags.append("Lipinski concern")
    except Exception: pass
    if str(row.get("Veber_pass", "True")).lower() == "false": flags.append("Veber concern")
    if row.get("PAINS_alerts"): flags.append("PAINS alert")
    if score is None:
        return "undetermined", "low", "; ".join(flags)
    if score <= -9: pred = "strong predicted binder"
    elif score <= -7: pred = "moderate predicted binder"
    elif score <= -5.5: pred = "weak-to-moderate predicted binder"
    else: pred = "weak predicted binder"
    conf = "medium"
    if flags:
        conf = "low-medium" if "strong" in pred or "moderate" in pred else "low"
    return pred, conf, "; ".join(flags)


def write_csv(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    keys = sorted({k for r in rows for k in r.keys()}) if rows else []
    with path.open("w", newline="") as f:
        if keys:
            w = csv.DictWriter(f, fieldnames=keys); w.writeheader(); w.writerows(rows)


def write_html(path: Path, metadata: dict, rows):
    css = """
    body{font-family:Arial,sans-serif;margin:24px;color:#172033} h1{color:#123} table{border-collapse:collapse;width:100%;font-size:13px}
    th,td{border:1px solid #d6dbe5;padding:6px;vertical-align:top} th{background:#edf2f7} .low{color:#a33}.medium{color:#965}.high{color:#185}
    .note{background:#fff8db;border:1px solid #eadc92;padding:12px;border-radius:8px}.meta{background:#eef7ff;padding:12px;border-radius:8px}
    """
    cols = ["rank", "name", "vina_score_kcal_mol", "prediction", "confidence", "key_flags", "MW", "cLogP", "TPSA", "Lipinski_violations", "Veber_pass", "PAINS_alerts", "GI_absorption_hint"]
    lines = [f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>", "<h1>Professional Docking Report</h1>"]
    lines.append("<div class='meta'><b>Metadata</b><pre>" + html.escape(json.dumps(metadata, indent=2)) + "</pre></div>")
    lines.append("<div class='note'><b>Scientific caution:</b> docking predicts binding hypotheses, not confirmed inhibition. Experimental enzymatic validation is required.</div>")
    lines.append("<h2>Ranked results</h2><table><tr>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr>")
    for i, r in enumerate(rows, 1):
        r = {**r, "rank": i}
        lines.append("<tr>" + "".join(f"<td>{html.escape(str(r.get(c,'')))}</td>" for c in cols) + "</tr>")
    lines.append("</table></body></html>")
    path.write_text("\n".join(lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="CSV with columns name,smiles")
    ap.add_argument("--target-pdb", default="1LPB")
    ap.add_argument("--mode", choices=["dry", "dock"], default="dry")
    ap.add_argument("--run-id", default=time.strftime("10x_%Y%m%d_%H%M%S"))
    ap.add_argument("--exhaustiveness", type=int, default=8)
    ap.add_argument("--cpu", type=int, default=min(8, max(1, os.cpu_count() or 1)),
                    help="Vina threads per ligand (capped at 8 by default to avoid oversubscription)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--n-poses", type=int, default=5, dest="n_poses")
    args = ap.parse_args()

    outdir = RUNS / args.run_id
    outdir.mkdir(parents=True, exist_ok=True)
    ligs = read_ligands(Path(args.input))
    pdb = fetch_pdb(args.target_pdb, outdir / "receptor")
    grid = infer_grid(pdb, args.target_pdb)
    clean = clean_receptor_pdb(pdb, outdir / "receptor")
    native = None
    if args.target_pdb.upper() == "1LPB":
        native = extract_native_ligand_pdb(pdb, PANCREATIC_LIPASE["native_ligand"], outdir / "receptor")

    # filters in parallel
    filter_rows = []
    with ThreadPoolExecutor(max_workers=min(16, max(1, len(ligs)))) as ex:
        for fut in as_completed([ex.submit(rdkit_filters, l) for l in ligs]):
            filter_rows.append(fut.result())
    by_name = {r["name"]: r for r in filter_rows}

    dock_rows = []
    receptor_pdbqt = None; receptor_prep = "not needed in dry mode"
    if args.mode == "dock":
        receptor_pdbqt, receptor_prep = prepare_receptor_pdbqt(clean, outdir / "receptor")
        if receptor_pdbqt:
            for lig in ligs:  # one-by-one for reproducibility/checkpointing
                dock_rows.append(dock_ligand(lig, receptor_pdbqt, grid, outdir,
                                             args.exhaustiveness, args.cpu,
                                             seed=args.seed, n_poses=args.n_poses))
        else:
            dock_rows = [{"name": l["name"], "docking_status": "skipped", "dock_error": receptor_prep} for l in ligs]
    else:
        dock_rows = [{"name": l["name"], "docking_status": "dry", "vina_score_kcal_mol": None,
                      "dry_run": True} for l in ligs]

    for d in dock_rows:
        by_name.setdefault(d["name"], {}).update(d)
    final = []
    for r in by_name.values():
        pred, conf, flags = prediction(r)
        r["prediction"] = pred; r["confidence"] = conf; r["key_flags"] = flags
        # Stamp dry_run explicitly so downstream consumers/auditors can detect previews.
        if args.mode != "dock":
            r["dry_run"] = True
        final.append(r)
    final.sort(key=lambda r: (r.get("vina_score_kcal_mol") in (None, "", "None"), float(r.get("vina_score_kcal_mol") or 999)))

    meta = {"target_pdb": args.target_pdb.upper(), "grid": grid, "mode": args.mode,
            "dry_mode": args.mode != "dock", "exhaustiveness": args.exhaustiveness,
            "cpu": args.cpu, "seed": args.seed, "n_poses": args.n_poses,
            "receptor_prep": receptor_prep, "native_ligand_file": str(native) if native else None,
            "numbering_note": "Catalytic triad in 1LPB PDB indices: Ser152/Asp176/His263; mature-protein (UniProt P16233) numbering is +1 offset (Ser153/Asp177/His263). Coordinates are identical; pick one convention and state it explicitly.",
            "tools": {"vina": which("vina"), "obabel": which("obabel"), "mk_prepare_receptor.py": which("mk_prepare_receptor.py")}}
    (outdir / "metadata.json").write_text(json.dumps(meta, indent=2))
    write_csv(outdir / "final_ranked_results.csv", final)
    write_html(outdir / "report.html", meta, final)
    print(f"Run directory: {outdir}")
    print(f"Grid: {grid}")
    print(f"Wrote: {outdir/'final_ranked_results.csv'}")
    print(f"Wrote: {outdir/'report.html'}")

if __name__ == "__main__":
    main()
