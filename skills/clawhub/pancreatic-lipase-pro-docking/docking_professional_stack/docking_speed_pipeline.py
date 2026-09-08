#!/usr/bin/env python3
"""
docking_speed_pipeline.py

Speed/capacity optimized professional docking runner.

Design goals:
- Faster throughput without lowering scientific quality by default.
- Uses parallel docking safely: each Vina process gets cpu_per_dock CPUs.
- Checkpoint/resume per ligand.
- Parallel descriptor/PAINS filters.
- Quality presets keep exhaustiveness appropriate.
- Optional prefiltering for very large libraries, but default docks all valid ligands.

Examples:
  python docking_speed_pipeline.py --input ligands.csv --target-pdb 1LPB --mode dry
  python docking_speed_pipeline.py --input ligands.csv --target-pdb 1LPB --mode dock --quality standard --total-cpu 16 --cpu-per-dock 2
  python docking_speed_pipeline.py --input ligands.csv --mode dock --quality high --workers 4 --cpu-per-dock 4
"""
from __future__ import annotations

import argparse, csv, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# Reuse validated functions from the 10x pipeline.
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import docking_10x_pipeline as base  # noqa

RUNS = Path("speed_runs")
QUALITY = {
    "screen": {"exhaustiveness": 4, "note": "fast screening; medium-low pose sampling"},
    "standard": {"exhaustiveness": 8, "note": "balanced professional default"},
    "high": {"exhaustiveness": 16, "note": "slower, better sampling"},
    "ultra": {"exhaustiveness": 32, "note": "very slow; use for finalists"},
}


def write_csv(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Defensive: drop None keys (DictReader artifact when a row has extra commas)
    # and sort string keys.
    key_set = set()
    for r in rows:
        for k in list(r.keys()):
            if k is None or not isinstance(k, str):
                continue
            key_set.add(k)
    keys = sorted(key_set)
    with path.open("w", newline="") as f:
        if keys:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction='ignore')
            w.writeheader(); w.writerows(rows)




def ensure_unique_names(ligs):
    """Avoid output/checkpoint collisions when an input library has duplicate names."""
    counts = {}
    out = []
    for lig in ligs:
        lig = dict(lig)
        name = lig.get("name") or f"lig_{len(out)+1}"
        n = counts.get(name, 0)
        counts[name] = n + 1
        if n:
            lig["original_name"] = name
            lig["name"] = f"{name}__dup{n+1}"
        out.append(lig)
    return out


def rdkit_filters_batch(ligs):  # v100.4: per-ligand try/except
    """Faster descriptor/PAINS calculation: import RDKit and build PAINS catalog once."""
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors, Lipinski, rdMolDescriptors
        from rdkit.Chem.FilterCatalog import FilterCatalog, FilterCatalogParams
        params = FilterCatalogParams()
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_A)
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_B)
        params.AddCatalog(FilterCatalogParams.FilterCatalogs.PAINS_C)
        catalog = FilterCatalog(params)
    except Exception:
        # fallback to dependency-tolerant single-ligand function
        return [base.rdkit_filters(l) for l in ligs]
    rows = []
    for lig in ligs:
        mol = Chem.MolFromSmiles(lig["smiles"])
        if mol is None:
            rows.append({**lig, "valid": False, "filter_error": "invalid SMILES"})
            continue
        mw = Descriptors.MolWt(mol); logp = Descriptors.MolLogP(mol)
        hbd = Lipinski.NumHDonors(mol); hba = Lipinski.NumHAcceptors(mol)
        rotb = Lipinski.NumRotatableBonds(mol); tpsa = rdMolDescriptors.CalcTPSA(mol)
        lipv = int(mw > 500) + int(logp > 5) + int(hbd > 5) + int(hba > 10)
        try:
            pains = [m.GetDescription() for m in catalog.GetMatches(mol)]
        except Exception as e:
            pains = [f"PAINS check failed: {e}"]
        rows.append({
            **lig, "valid": True, "MW": round(mw, 2), "cLogP": round(logp, 2), "HBD": hbd, "HBA": hba,
            "RotB": rotb, "TPSA": round(tpsa, 2), "Lipinski_violations": lipv,
            "Veber_pass": bool(rotb <= 10 and tpsa <= 140), "PAINS_alerts": "; ".join(pains),
            "GI_absorption_hint": "high" if (mw <= 500 and tpsa <= 140 and rotb <= 10) else "low/uncertain",
        })
    return rows


def should_prefilter(row, policy: str) -> tuple[bool, str]:
    """Return dock?, reason. Default policy all_valid does not drop drug-likeness concerns."""
    if row.get("valid") is False:
        return False, "invalid SMILES"
    if policy == "none":
        return True, "no prefilter"
    if policy == "all_valid":
        return row.get("valid") is not False, "valid or unchecked"
    if policy == "druglike":
        try:
            if int(row.get("Lipinski_violations", 0)) > 1:
                return False, "prefilter: >1 Lipinski violation"
        except Exception:
            pass
        if str(row.get("Veber_pass", "True")).lower() == "false":
            return False, "prefilter: Veber fail"
        return row.get("valid") is not False, "druglike prefilter pass"
    if policy == "strict":
        dock, reason = should_prefilter(row, "druglike")
        if not dock:
            return dock, reason
        if row.get("PAINS_alerts"):
            return False, "prefilter: PAINS alert"
        return True, "strict prefilter pass"
    return True, "unknown policy treated as no prefilter"



def gi_fluid_flags(row, gi_mode: str) -> tuple[str, int]:
    """Heuristic GI-fluid suitability flags. Not a replacement for experimental FaSSIF/FeSSIF solubility."""
    if gi_mode == "off":
        return "", 0
    flags = []
    penalty = 0
    def f(key, default=None):
        try: return float(row.get(key, default))
        except Exception: return default
    mw = f("MW"); logp = f("cLogP"); tpsa = f("TPSA"); rotb = f("RotB")
    hbd = f("HBD")
    # Pancreatic lipase acts in intestinal fluid; very hydrophobic molecules may be micelle-sequestered.
    if logp is not None and logp > 5.5:
        flags.append("high cLogP: micelle/lipid sequestration risk"); penalty += 2
    elif logp is not None and logp > 4.5:
        flags.append("moderate micelle-partition risk"); penalty += 1
    if logp is not None and logp < -1:
        flags.append("very hydrophilic: membrane/lipid-interface access risk"); penalty += 1
    if tpsa is not None and tpsa > 160:
        flags.append("very high TPSA: permeability/interface-access concern"); penalty += 2
    elif tpsa is not None and tpsa > 140:
        flags.append("high TPSA: GI absorption/interface concern"); penalty += 1
    if mw is not None and mw > 700:
        flags.append("very high MW: solubility/diffusion concern"); penalty += 2
    elif mw is not None and mw > 500:
        flags.append("high MW: oral/GI property concern"); penalty += 1
    if rotb is not None and rotb > 15:
        flags.append("very flexible: entropy/pose reliability concern"); penalty += 2
    elif rotb is not None and rotb > 10:
        flags.append("flexible: pose reliability concern"); penalty += 1
    if hbd is not None and hbd > 6:
        flags.append("many HBD: solubility/permeability tradeoff"); penalty += 1
    if row.get("PAINS_alerts"):
        flags.append("PAINS/assay interference risk in enzyme assay"); penalty += 2
    # Polyphenol/catechol-like patterns often inhibit nonspecifically or interfere in assays.
    smi = (row.get("smiles") or "").lower()
    if smi.count("o") >= 6 and (logp is not None and logp < 4):
        flags.append("polyphenol-like: nonspecific/oxidation/assay-interference caution"); penalty += 1
    if gi_mode == "strict" and penalty:
        penalty += 1
    return "; ".join(flags), penalty


def merge_rows(filters, dock_rows, skipped, gi_mode="intestinal", ligand_rows=None):
    by = {r["name"]: dict(r) for r in filters}
    # Seed with raw ligand rows first so user-provided columns (reference_ic50_um, notes,
    # etc.) survive even if the descriptor filter step didn't see them.
    if ligand_rows:
        for r in ligand_rows:
            by.setdefault(r["name"], {}).update(r)
    for r in skipped + dock_rows:
        by.setdefault(r["name"], {}).update(r)
    final = []
    for r in by.values():
        status = str(r.get('docking_status','')).lower()
        no_score = r.get('vina_score_kcal_mol') in (None, '', 'None')
        if status in {'dry', 'skipped', 'prefilter_skipped'} and no_score:
            pred, conf, flags = ('not physically docked', 'none', r.get('dock_error','') or 'no Vina score')
        else:
            pred, conf, flags = base.prediction(r)
        gi_flags, gi_penalty = gi_fluid_flags(r, gi_mode)
        combined_flags = "; ".join(x for x in [flags, gi_flags] if x)
        # GI-aware relabeling: good docking but poor GI suitability should not be overclaimed.
        if gi_penalty >= 3 and ("strong" in pred or "moderate" in pred):
            pred = "good docking but GI-fluid suitability concern"
            conf = "low-medium"
        elif gi_penalty >= 5:
            pred = "GI-fluid unreliable candidate"
            conf = "low"
        r["prediction"] = pred
        r["confidence"] = conf
        r["key_flags"] = combined_flags
        r["GI_fluid_penalty"] = gi_penalty
        final.append(r)
    def sort_key(r):
        try: s = float(r.get("vina_score_kcal_mol"))
        except Exception: s = 999.0
        return (s == 999.0, s)
    final.sort(key=sort_key)
    return final


def progress_line(done, total, start, extra=""):
    elapsed = max(0.001, time.time() - start)
    rate = done / elapsed
    eta = (total - done) / rate if rate > 0 else 0
    return f"progress {done}/{total} | {rate:.2f} lig/s | ETA {eta/60:.1f} min {extra}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--target-pdb", default="1LPB")
    ap.add_argument("--mode", choices=["dry", "dock"], default="dry")
    ap.add_argument("--quality", choices=list(QUALITY), default="standard")
    ap.add_argument("--exhaustiveness", type=int, help="override quality preset")
    ap.add_argument("--total-cpu", type=int, default=min(8, max(1, os.cpu_count() or 1)),
                    help="total vina threads across all parallel workers (capped at 8 by default)")
    ap.add_argument("--cpu-per-dock", type=int, default=1,
                    help="threads per individual vina job")
    ap.add_argument("--workers", type=int, help="parallel vina jobs; default total_cpu/cpu_per_dock")
    ap.add_argument("--prefilter", choices=["none", "all_valid", "druglike", "strict"], default="all_valid",
                    help="default all_valid only removes invalid SMILES; stricter modes increase capacity but may miss unusual actives")
    ap.add_argument("--gi-mode", choices=["off", "intestinal", "strict"], default="intestinal",
                    help="GI-fluid-aware scoring for pancreatic/intestinal targets; strict applies stronger penalties")
    ap.add_argument("--limit", type=int, help="test only first N ligands")
    ap.add_argument("--run-id", default=time.strftime("speed_%Y%m%d_%H%M%S"))
    ap.add_argument("--no-html", action="store_true", help="skip HTML report for huge runs to save time")
    ap.add_argument("--quiet", action="store_true", help="minimal console output for lower I/O overhead")
    ap.add_argument("--checkpoint-every", type=int, default=25,
                    help="write partial_results.csv every N completed ligands; lower is safer, higher is faster")
    ap.add_argument("--seed", type=int, default=42,
                    help="random seed passed to Vina via --seed for reproducibility")
    ap.add_argument("--n-poses", type=int, default=5,
                    help="number of poses per ligand written by Vina")
    ap.add_argument("--executive-dashboard", action="store_true",
                    help="generate a polished government/enterprise-style HTML dashboard")
    args = ap.parse_args()

    exhaustiveness = args.exhaustiveness or QUALITY[args.quality]["exhaustiveness"]
    workers = args.workers or max(1, args.total_cpu // max(1, args.cpu_per_dock))
    # Avoid oversubscription by default.
    workers = max(1, min(workers, max(1, args.total_cpu)))

    outdir = RUNS / args.run_id
    outdir.mkdir(parents=True, exist_ok=True)
    ligs = ensure_unique_names(base.read_ligands(Path(args.input)))
    if args.limit:
        ligs = ligs[:args.limit]

    if not args.quiet:
        print(f"Loaded {len(ligs)} ligands")
        print(f"Quality={args.quality}; exhaustiveness={exhaustiveness}; total_cpu={args.total_cpu}; cpu_per_dock={args.cpu_per_dock}; workers={workers}")

    pdb = base.fetch_pdb(args.target_pdb, outdir / "receptor")
    grid = base.infer_grid(pdb, args.target_pdb)
    clean = base.clean_receptor_pdb(pdb, outdir / "receptor")
    native = None
    if args.target_pdb.upper() == "1LPB":
        native = base.extract_native_ligand_pdb(pdb, base.PANCREATIC_LIPASE["native_ligand"], outdir / "receptor")

    # Descriptor filters: batch mode builds PAINS catalog once, much faster for large libraries.
    if not args.quiet: print("Running descriptor/PAINS filters in optimized batch mode...")
    start = time.time()
    filters = rdkit_filters_batch(ligs)
    if not args.quiet: print(progress_line(len(filters), len(ligs), start), flush=True)
    write_csv(outdir / "descriptors.csv", filters)

    dock_queue = []
    skipped = []
    by_name_filter = {r["name"]: r for r in filters}
    for lig in ligs:
        row = by_name_filter.get(lig["name"], lig)
        dock, reason = should_prefilter(row, args.prefilter)
        if dock:
            dock_queue.append(lig)
        else:
            skipped.append({"name": lig["name"], "docking_status": "prefilter_skipped", "dock_error": reason})

    if not args.quiet: print(f"Dock queue: {len(dock_queue)} | skipped by prefilter: {len(skipped)}")

    receptor_pdbqt = None; receptor_prep = "not needed in dry mode"
    dock_rows = []
    if args.mode == "dock":
        receptor_pdbqt, receptor_prep = base.prepare_receptor_pdbqt(clean, outdir / "receptor")
        if not receptor_pdbqt:
            print(f"Receptor preparation failed/skipped: {receptor_prep}")
            dock_rows = [{"name": l["name"], "docking_status": "skipped", "dock_error": receptor_prep} for l in dock_queue]
        else:
            if not args.quiet: print("Starting parallel docking...")
            start = time.time()
            with ThreadPoolExecutor(max_workers=workers) as ex:
                futures = [ex.submit(base.dock_ligand, lig, receptor_pdbqt, grid, outdir,
                                     exhaustiveness, args.cpu_per_dock,
                                     seed=args.seed, n_poses=args.n_poses)
                           for lig in dock_queue]
                for i, fut in enumerate(as_completed(futures), 1):
                    try:
                        row = fut.result()
                    except Exception as e:
                        row = {"name": "unknown", "docking_status": "failed", "dock_error": str(e)}
                    dock_rows.append(row)
                    if i % 10 == 0 or i == len(futures):
                        ok = sum(1 for r in dock_rows if r.get("docking_status") == "ok")
                        if not args.quiet: print(progress_line(i, len(futures), start, f"| ok {ok}"), flush=True)
                    # checkpoint periodically to avoid excessive I/O on large runs
                    if args.checkpoint_every and (i % args.checkpoint_every == 0 or i == len(futures)):
                        final_partial = merge_rows(filters, dock_rows, skipped, args.gi_mode, ligand_rows=ligs)
                        write_csv(outdir / "partial_results.csv", final_partial)
    else:
        dock_rows = [{"name": l["name"], "docking_status": "dry", "vina_score_kcal_mol": None,
                      "dry_run": True} for l in dock_queue]
        skipped = [dict(r, dry_run=True) for r in skipped]

    final = merge_rows(filters, dock_rows, skipped, args.gi_mode, ligand_rows=ligs)
    # Explicit dry_run column on every row so CSVs are self-describing.
    for r in final:
        if args.mode != "dock":
            r["dry_run"] = True
        r.setdefault("dry_run", False)
    meta = {
        "target_pdb": args.target_pdb.upper(), "grid": grid, "mode": args.mode, "dry_mode": args.mode != "dock",
        "quality": args.quality, "quality_note": QUALITY[args.quality]["note"], "exhaustiveness": exhaustiveness,
        "seed": args.seed, "n_poses": args.n_poses,
        "total_cpu": args.total_cpu, "cpu_per_dock": args.cpu_per_dock, "workers": workers,
        "prefilter": args.prefilter, "gi_mode": args.gi_mode, "receptor_prep": receptor_prep,
        "native_ligand_file": str(native) if native else None,
        "ligands_loaded": len(ligs), "dock_queue": len(dock_queue), "prefilter_skipped": len(skipped),
        "checkpoint_every": args.checkpoint_every,
        "numbering_note": "Grid centered on co-crystallized MUP ligand centroid in 1LPB; catalytic triad in deposited PDB indices Ser152/Asp176/His263. Mature-protein (UniProt P16233) numbering is +1 offset (Ser153/Asp177/His263). Coordinates are identical.",
        "tools": {"vina": base.which("vina"), "obabel": base.which("obabel"), "mk_prepare_receptor.py": base.which("mk_prepare_receptor.py")},
    }
    (outdir / "metadata.json").write_text(json.dumps(meta, indent=2))
    write_csv(outdir / "final_ranked_results.csv", final)
    if not args.no_html:
        base.write_html(outdir / "report.html", meta, final)
    if args.executive_dashboard:
        try:
            import generate_executive_dashboard as ged
            ged_path = outdir / "executive_dashboard.html"
            ged_path.write_text(ged.make_html(final, meta,
                "Pancreatic Lipase Inhibition Program — Executive Screening Dashboard",
                "Decision-ready virtual-screening output with docking, GI-fluid suitability, risk flags, and candidate prioritization."), encoding="utf-8")
        except Exception as e:
            print(f"Executive dashboard generation failed: {e}")
    if not args.quiet:
        print(f"Wrote {outdir/'final_ranked_results.csv'}")
        if not args.no_html: print(f"Wrote {outdir/'report.html'}")
        if args.executive_dashboard: print(f"Wrote {outdir/'executive_dashboard.html'}")
    else:
        print(outdir / "final_ranked_results.csv")

if __name__ == "__main__":
    main()
