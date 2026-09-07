#!/usr/bin/env python3
"""redock_high.py — re-dock top-N molecules at HIGH exhaustiveness + compare.

Usage:
  python3 redock_high.py --results dock_results/results_all_sites.csv --top 10
      [--exhaustiveness 24] [--n-seeds 3] [--n-poses 10] [--workers 2]
      [--receptor receptor.pdb] [--sites-file sites.json]
      [--outdir dock_results_ex16] [--seed 42]

Writes:
  <outdir>/results_ex16.csv            per-molecule x site ex16 scores
  <outdir>/comparison_ex2_vs_ex16.csv  delta table (ex2 vs ex16)
"""
import argparse, csv, json, sys, time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import multi_site_docking as ms
import debug_utils as du


def worker(job):
    return ms.worker(job)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--results", required=True, help="ex2 results CSV (results_all_sites.csv)")
    ap.add_argument("--ligands", default=None, help="ligand CSV with name,smiles (default: auto-detect molecules_resolved.csv)")
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--exhaustiveness", type=int, default=24)
    ap.add_argument("--n-seeds", type=int, default=3, help="replicate seeds = seed+i*7919 (independent RNG streams; v100.4)")
    ap.add_argument("--n-poses", type=int, default=10)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--cpu-per-dock", type=int, default=1)
    ap.add_argument("--receptor", default=None)
    ap.add_argument("--sites-file", default=None)
    ap.add_argument("--outdir", default="dock_results_ex16")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--log-file", default=None)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    import os
    du.setup_logging(debug=args.debug, log_file=args.log_file)
    du.install_exception_hook()
    os.environ["PATH"] = "/home/user/out/plenv/bin:" + os.environ.get("PATH", "")
    if args.check:
        return du.print_env_check()

    # top-N by best score across sites
    scores = {}
    for r in csv.DictReader(open(args.results)):
        if r["status"] == "ok" and r["score"]:
            scores.setdefault(r["name"], {})[r["site"]] = float(r["score"])
    top = sorted(scores, key=lambda n: min(scores[n].values()))[: args.top]
    print(f"re-docking top {len(top)}: {', '.join(top)}", flush=True)

    # ligand SMILES: --ligands CSV, else molecules_resolved.csv next to results/ or in CWD
    lig_csv = Path(args.ligands) if args.ligands else None
    if lig_csv is None:
        for cand in (Path(args.results).parent.parent / "molecules_resolved.csv",
                     Path("molecules_resolved.csv")):
            if cand.exists():
                lig_csv = cand
                break
    smiles_of = {}
    if lig_csv and lig_csv.exists():
        for r in csv.DictReader(open(lig_csv)):
            smiles_of[r["name"]] = r["smiles"]
    missing = [n for n in top if n not in smiles_of]
    if missing:
        print("NO SMILES for:", missing, "-> pass --ligands <csv with name,smiles>")

    # v100.4: chemprep variants (pH protonation + tautomer + stereo) + replicate seeds
    import chemprep
    prepped = {}
    for n in top:
        if n in smiles_of:
            meta = chemprep.prep_ligand_variants(n, smiles_of[n], ligprep)
            prepped[n] = meta["variants"]
    seeds = [args.seed + k * 7919 for k in range(max(1, args.n_seeds))]

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "receptor").mkdir(parents=True, exist_ok=True)   # meeko does NOT create it
    (outdir / "ligprep").mkdir(parents=True, exist_ok=True)
    (outdir / "runs").mkdir(parents=True, exist_ok=True)

    # sites
    if args.sites_file and Path(args.sites_file).exists():
        sites = json.loads(Path(args.sites_file).read_text())
    else:
        rec = Path(args.receptor) if args.receptor else HERE / "receptor" / "1LPB.pdb"
        chain = ms.pick_chain(rec)
        clean = ms.clean_receptor(rec, chain, outdir)
        res, seq_nums = ms.parse_receptor(clean, chain)
        sites = ms.detect_sites(res, seq_nums)
        (outdir / "sites.json").write_text(json.dumps(sites, indent=1))
    print("sites:", list(sites.keys()), flush=True)

    # receptor + ligand prep (once)
    rec = Path(args.receptor) if args.receptor else HERE / "receptor" / "1LPB.pdb"
    chain = ms.pick_chain(rec)
    clean = ms.clean_receptor(rec, chain, outdir)
    receptor_pdbqt, _ = ms.base.prepare_receptor_pdbqt(clean, outdir / "receptor")
    receptor_pdbqt = str(receptor_pdbqt)
    du.record_versions(outdir, {"exhaustiveness": args.exhaustiveness,
                                "n_poses": args.n_poses, "seed": args.seed,
                                "top": args.top, "cmdline": " ".join(sys.argv)})
    ligprep = outdir / "ligprep"
    prepped = {}
    for n in top:
        if n in smiles_of:
            lp, _ = ms.base.prepare_ligand_pdbqt({"name": n, "smiles": smiles_of[n]}, ligprep)
            if lp:
                prepped[n] = str(lp)

    res_csv = outdir / "results_ex16.csv"
    done = set()
    if res_csv.exists():
        for r in csv.DictReader(open(res_csv)):
            if r.get("status") == "ok":
                done.add((r["name"], r["site"], r["variant"], r["seed"]))
    jobs = [(n, vp, f"v{vi}", site, spec["center"], spec["box"],
             args.exhaustiveness, args.cpu_per_dock, args.n_poses, seed,
             receptor_pdbqt, str(outdir / "runs"))
            for n in top if n in prepped
            for vi, vp in enumerate(prepped[n])
            for site, spec in sites.items()
            for seed in seeds if (n, site, f"v{vi}", str(seed)) not in done]
    print(f"pending: {len(jobs)} jobs ({len(top)} ligands x {len(sites)} sites x "
          f"{len(seeds)} seeds x variants)", flush=True)

    import statistics as _st
    t0 = time.time()
    new = not res_csv.exists()
    with open(res_csv, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "site", "variant", "seed", "status",
                                          "score", "rmsd_lb", "rmsd_ub", "n_modes", "time_s"])
        if new or res_csv.stat().st_size == 0:
            w.writeheader()
        if args.workers > 1:
            with ProcessPoolExecutor(max_workers=args.workers) as ex:
                for row in ex.map(worker, jobs, chunksize=2):
                    w.writerow(row); f.flush()
        else:
            for job in jobs:
                w.writerow(worker(job)); f.flush()
    # aggregate per (name, site): best + seed agreement
    agg = {}
    for r in csv.DictReader(open(res_csv)):
        if r["status"] == "ok" and r["score"]:
            agg.setdefault((r["name"], r["site"]), []).append(float(r["score"]))
    comp = outdir / f"comparison_vs_{Path(args.results).stem}.csv"
    with open(comp, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "site", "best_exhigh", "n_replicates", "mean", "sd", "stability"])
        for (n, s), sc in sorted(agg):
            sd = _st.pstdev(sc) if len(sc) > 1 else 0.0
            w.writerow([n, s, min(sc), len(sc), round(_st.mean(sc), 2), round(sd, 2),
                        "stable" if sd <= 0.5 else "unstable(sd>0.5)"])
    print(f"comparison -> {comp}", flush=True)
    print(f"re-dock done in {time.time()-t0:.0f}s", flush=True)

    # comparison
    ex2 = {(r["name"], r["site"]): float(r["score"])
           for r in csv.DictReader(open(args.results)) if r["status"] == "ok" and r["score"]}
    ex16 = {(r["name"], r["site"]): float(r["score"])
            for r in csv.DictReader(open(res_csv)) if r["status"] == "ok" and r["score"]}
    with open(outdir / "comparison_ex2_vs_ex16.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "site", "ex2", "ex16", "delta"])
        for (n, s), v16 in sorted(ex16.items(), key=lambda kv: kv[1]):
            v2 = ex2.get((n, s))
            w.writerow([n, s, v2 if v2 is not None else "", v16,
                        round(v16 - v2, 2) if v2 is not None else ""])
    deltas = [v16 - ex2[k] for k, v16 in ex16.items() if k in ex2]
    if deltas:
        print(f"comparison: {len(deltas)} pairs, mean delta {sum(deltas)/len(deltas):+.2f} kcal/mol "
              f"(negative = deeper pose found at ex{args.exhaustiveness})", flush=True)
    print("->", outdir / "comparison_ex2_vs_ex16.csv", flush=True)


if __name__ == "__main__":
    raise SystemExit(main())
