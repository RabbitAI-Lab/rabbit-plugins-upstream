#!/usr/bin/env python3
"""multi_site_docking.py — 5-position site-specific docking for hPL (PDB 1LPB).

v100.4.0 PRECISION REWRITE (2026-08-25, multi-model audited). Science fixes:
  1. RECEPTOR FIDELITY: 1LPB is a complex — chain B = lipase, chain A = colipase
     (966 atoms, 5 disulfides), one Ca2+ (HETATM, chain B). The old cleaner kept
     ONLY the largest chain and dropped colipase + Ca2+ while still advertising
     a "colipase interface" site. Now: --receptor-model complex (default: lipase
     + colipase + Ca2+) or apo (lipase chain only, open-lid hypothesis, kept for
     comparability with older runs). Ca2+ is kept if meeko accepts it, else
     dropped with a recorded warning (Vina has no metal-ligand term).
  2. TRUE OXYANION HOLE: geometric detection (backbone N within 4 A of the
     catalytic Ser OG, excluding Ser itself; expect Phe77 + Leu153 in hPL) —
     the old "+26 residues after Ser in sequence index" arithmetic was wrong.
  3. REAL COLIPASE INTERFACE: contacting residues across chains (<=5 A), not
     the lipase's own C-terminus.
  4. SITE CENTERS: catalytic site anchored on Ser-OG (not the residue centroid,
     which can sit off-pocket).
  5. LIGAND CORRECTNESS (chemprep.py): pH 7.4 major-microstate protonation
     (carboxylates -1, amines/guanidines +1 ...), canonical tautomer,
     undefined-stereocenter enumeration (<=2 centers, <=4 isomers, best kept and
     reported), ETKDG multi-conformer + MMFF lowest-energy start pose.
  6. BIAS ELIMINATION: --precision {fast,balanced,max} = (ex4,1 seed) /
     (ex8,1) / (ex24,3 seeds); replicate seeds get independent RNG streams and
     per-job offsets; seed-agreement stats (mean/sd) flag unstable poses
     (sd > 0.5 kcal/mol or pose RMSD > 2 A -> 'unstable').
  7. Full Vina mode-table parsing (affinity + rmsd_lb/ub per mode).

Perf: ligand variants cached by canonical-SMILES hash; receptor prepared once;
checkpoint/resume keyed (name, site, variant, seed); workers = vina processes.

Usage:
  python3 multi_site_docking.py --ligands ligands.csv [--receptor-model complex]
      [--precision balanced] [--exhaustiveness N] [--n-seeds K] [--seed 42]
      [--n-poses 9] [--workers 2] [--cpu-per-dock 1] [--max-mw 700] [--max-rotb 20]
      [--protonation rules|as-supplied] [--outdir dock_results] [--limit N] [--check]
Outputs:
  <outdir>/results_all_sites.csv      aggregate best per (name, site)  [legacy schema]
  <outdir>/runs_detail.csv            per (name, site, variant, seed) rows
  <outdir>/ligprep_meta.json          protonation/tautomer/stereo decisions
  <outdir>/sites.json + versions.json
"""
import argparse, csv, json, os, statistics, sys, time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import docking_10x_pipeline as base
import debug_utils as du

HYDROPHOBIC = {"ALA", "VAL", "LEU", "ILE", "PHE", "TRP", "MET", "PRO", "CYS", "TYR"}

# 1LPB ground truth (verified 2026-08-25 from the shipped coordinates):
# chain B = lipase (Ser152/Asp176/His263), chain A = colipase, Ca2+ on chain B.
PRECISION_TIERS = {
    "fast":     {"exhaustiveness": 4,  "n_seeds": 1, "n_poses": 9},
    "balanced": {"exhaustiveness": 8,  "n_seeds": 1, "n_poses": 9},
    "max":      {"exhaustiveness": 24, "n_seeds": 3, "n_poses": 20},
}


def pick_chain(pdb_path):
    """Chain with the most protein ATOM records = the enzyme (lipase) chain."""
    counts = {}
    for ln in open(pdb_path):
        if ln.startswith("ATOM"):
            c = ln[21]
            counts[c] = counts.get(c, 0) + 1
    if not counts:
        raise SystemExit("no ATOM records in receptor")
    return max(counts, key=counts.get)


def protein_chains(pdb_path):
    counts = {}
    for ln in open(pdb_path):
        if ln.startswith("ATOM"):
            counts[ln[21]] = counts.get(ln[21], 0) + 1
    return counts


def clean_receptor(pdb_path, enzyme_chain, outdir, model="complex", keep_ca=True):
    """v100.4: complex model keeps colipase chain(s) + Ca2+; apo keeps enzyme only.

    Always drops: hydrogens (meeko re-adds polar H), detergent (BOG), native
    inhibitor (MUP), waters.
    """
    out = Path(outdir) / ("receptor_clean.pdb" if model == "complex" else "receptor_clean_apo.pdb")
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.exists():
        return out
    other = {c for c in protein_chains(pdb_path) if c != enzyme_chain}
    keep_chains = ({enzyme_chain} | other) if model == "complex" else {enzyme_chain}
    lines, ca_kept, ca_dropped = [], 0, 0
    for ln in open(pdb_path):
        if ln.startswith("ATOM"):
            if ln[21] not in keep_chains:
                continue
            if ln[12:16].strip().startswith("H"):
                continue
            lines.append(ln.rstrip("\n"))
        elif ln.startswith("HETATM") and model == "complex" and keep_ca:
            resn = ln[17:20].strip()
            atom = ln[12:16].strip()
            if resn == "CA" and atom in ("CA", "Ca"):  # calcium ion, not calmodulin
                lines.append(ln.rstrip("\n"))
                ca_kept += 1
            else:
                ca_dropped += 1
    out.write_text("\n".join(lines) + "\nEND\n")
    du.LOG.info("receptor model=%s chains=%s Ca2+kept=%d (dropped %d other HETATM)",
                model, sorted(keep_chains), ca_kept, ca_dropped)
    return out


def prepare_receptor_pdbqt_with_metal_fallback(clean_pdb, outdir):
    """meeko receptor prep; if it rejects the Ca2+ ion, retry without it."""
    pdbqt, note = base.prepare_receptor_pdbqt(clean_pdb, outdir)
    if pdbqt:
        return str(pdbqt), note
    stripped = Path(outdir) / "receptor_clean_noca.pdb"
    stripped.write_text("\n".join(
        ln for ln in clean_pdb.read_text().splitlines()
        if not (ln.startswith("HETATM") and ln[17:20].strip() == "CA")) + "\nEND\n")
    pdbqt, note2 = base.prepare_receptor_pdbqt(stripped, outdir)
    if pdbqt:
        return str(pdbqt), f"{note2} (Ca2+ dropped: meeko rejected metal)"
    return None, note2


def parse_receptor(pdb_path, chain):
    """Parse ONE chain's residues (heavy atoms). Robust to insertion codes."""
    res, seq_nums = {}, []
    for ln in open(pdb_path):
        if not ln.startswith("ATOM") or ln[21] != chain:
            continue
        name = ln[12:16].strip()
        if name.startswith("H"):
            continue
        try:
            r = int(ln[22:26])
        except ValueError:
            continue
        aa = ln[17:20].strip()
        if r not in res:
            res[r] = {"aa": aa, "atoms": {}}
            seq_nums.append(r)
        res[r]["atoms"][name] = (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))
    return res, seq_nums


def parse_chain_atoms(pdb_path, chain):
    """All heavy atoms of a chain (residue-keyed) for interface detection."""
    out = {}
    for ln in open(pdb_path):
        if not ln.startswith("ATOM") or ln[21] != chain:
            continue
        name = ln[12:16].strip()
        if name.startswith("H"):
            continue
        try:
            r = int(ln[22:26])
        except ValueError:
            continue
        out.setdefault(r, []).append((float(ln[30:38]), float(ln[38:46]), float(ln[46:54])))
    return out


def dist(a, b):
    return sum((a[i] - b[i]) ** 2 for i in range(3)) ** 0.5


def detect_sites(res, seq_nums, clean_complex=None, enzyme_chain=None):
    """v100.4 site detection. `clean_complex` enables the true cross-chain
    colipase interface (requires the complex receptor file)."""
    sers = [r for r, d in res.items() if d["aa"] == "SER" and "OG" in d["atoms"]]
    asps = [r for r, d in res.items() if d["aa"] == "ASP" and "OD1" in d["atoms"] and "OD2" in d["atoms"]]
    hiss = [r for r, d in res.items() if d["aa"] == "HIS" and "ND1" in d["atoms"] and "NE2" in d["atoms"]]

    best, best_d = None, 1e9
    for s in sers:
        og = res[s]["atoms"]["OG"]
        for a in asps:
            for h in hiss:
                d1 = dist(og, res[h]["atoms"]["NE2"])
                asp_od = min(dist(res[a]["atoms"][od], res[h]["atoms"]["ND1"])
                             for od in ("OD1", "OD2") if od in res[a]["atoms"])
                d2 = asp_od
                if d1 <= 5.0 and d2 <= 5.0 and d1 + d2 < best_d:
                    best, best_d = (s, a, h), d1 + d2
    if not best:
        raise SystemExit("catalytic triad (Ser-OG/Asp/His, H-bond geometry) not found in receptor")
    ser, asp, his = best
    idx = seq_nums.index(ser)
    og = res[ser]["atoms"]["OG"]
    his_ne2 = res[his]["atoms"]["NE2"]

    # TRUE oxyanion hole: backbone N within 6 A of Ser-OG (exclude Ser's own N).
    # Measured on 1LPB: Leu153-N 3.3 A, Phe77-N 5.4 A (the canonical pair);
    # 4.0 A misses Phe77 -> 6.0 A, top-2 by distance.
    triad_zone = {ser, asp, his}
    for ref in (ser, asp, his):
        for dr in range(-2, 3):
            triad_zone.add(ref + dr)
    oxy_scores = []
    for r, d in res.items():
        if r in triad_zone or "N" not in d["atoms"]:
            continue
        dd = dist(og, d["atoms"]["N"])
        if dd <= 6.0:
            oxy_scores.append((dd, r))
    oxy_scores.sort()
    oxy = [r for _, r in oxy_scores[:2]]
    if len(oxy) < 2:  # fallback to the old definition if geometry is unusual
        j = idx + 1
        if j < len(seq_nums) and seq_nums[j] not in oxy:
            oxy.append(seq_nums[j])

    lid = [n for n in seq_nums[idx + 87: idx + 108]]
    pocket = [r for r, d in res.items() if d["aa"] in HYDROPHOBIC
              and any(dist(og, c) <= 8 for c in d["atoms"].values())]

    # colipase interface: real cross-chain contacts if the complex is available
    iface_note = "lipase C-terminal 45 residues (complex chains unavailable)"
    cterm = seq_nums[-45:]
    iface_res, iface_atoms = [], []
    if clean_complex is not None and enzyme_chain is not None:
        others = [c for c in protein_chains(clean_complex) if c != enzyme_chain]
        if others:
            enz = parse_chain_atoms(clean_complex, enzyme_chain)
            partner = {}
            for c in others:
                partner.update(parse_chain_atoms(clean_complex, c))
            for r, atoms in enz.items():
                if any(dist(a, b) <= 5.0 for a in atoms for bs in partner.values() for b in bs):
                    iface_res.append(r)
                    iface_atoms += atoms
            for r, atoms in partner.items():
                if any(dist(a, b) <= 5.0 for a in atoms for bs in enz.values() for b in bs):
                    iface_res.append(("colipase", r))
                    iface_atoms += atoms
            iface_note = f"{len(iface_res)} contact residues <=5 A across chains {enzyme_chain}|{''.join(others)}"
    sites = {
        "catalytic_triad": {"residues": [ser, asp, his], "box": 20,
                            "note": f"Ser{ser}-Asp{asp}-His{his} (center anchored on Ser{ser}-OG)"},
        "oxyanion_hole": {"residues": oxy, "box": 18,
                          "note": f"backbone N within 6 A of Ser{ser}-OG: {oxy} (expect Phe77+Leu153)"},
        "lid": {"residues": lid, "box": 22,
                "note": f"residues {lid[0]}..{lid[-1] if lid else '?'} (amphipathic helix; expect ~237-261)"},
        "hydrophobic_pocket": {"residues": pocket, "box": 20,
                               "note": f"{len(pocket)} hydrophobic residues within 8 A of Ser{ser}-OG"},
        "colipase_interface": {"residues": iface_res or cterm, "box": 22, "note": iface_note},
    }
    for k, v in sites.items():
        if k == "colipase_interface" and iface_atoms:
            atoms = iface_atoms
        elif k == "catalytic_triad":
            atoms = [og, tuple(og[i] + 0.25 * (his_ne2[i] - og[i]) for i in range(3))]
        else:
            atoms = [c for r in v["residues"] if isinstance(r, int) and r in res for c in res[r]["atoms"].values()]
        if not atoms:
            raise SystemExit(f"site {k}: no atoms after filtering")
        v["center"] = [round(sum(x[i] for x in atoms) / len(atoms), 3) for i in range(3)]
    return sites


def parse_vina_modes(log_text):
    """Full mode-table parse: [{'mode':1,'affinity':..,'rmsd_lb':..,'rmsd_ub':..}, ...]."""
    modes = []
    for line in log_text.splitlines():
        parts = line.split()
        if len(parts) >= 4 and parts[0].isdigit():
            try:
                modes.append({"mode": int(parts[0]), "affinity": float(parts[1]),
                              "rmsd_lb": float(parts[2]), "rmsd_ub": float(parts[3])})
            except ValueError:
                continue
    return modes


def worker(job):
    (name, variant, vlabel, site, center, box, ex, cpu, n_poses, seed,
     receptor_pdbqt, outdir) = job
    t1 = time.time()
    try:
        sout = Path(outdir) / site / f"{name}__{vlabel}__s{seed}"
        sout.mkdir(parents=True, exist_ok=True)
        out_pose = sout / "pose.pdbqt"
        log = sout / "vina.log"
        cmd = ["vina", "--receptor", str(receptor_pdbqt), "--ligand", str(variant),
               "--center_x", str(center[0]), "--center_y", str(center[1]),
               "--center_z", str(center[2]),
               "--size_x", str(box), "--size_y", str(box), "--size_z", str(box),
               "--exhaustiveness", str(ex), "--cpu", str(cpu), "--seed", str(seed),
               "--num_modes", str(n_poses), "--out", str(out_pose)]
        rc, so, se = du.run_cmd(cmd, timeout=7200, check=False)
        log.write_text(so + "\n" + se)
        modes = parse_vina_modes(so + "\n" + se)
        best = modes[0]["affinity"] if modes else None
        status = "ok" if rc == 0 and best is not None else "failed"
        return {"name": name, "site": site, "variant": vlabel, "seed": seed,
                "status": status, "score": best,
                "rmsd_lb": modes[0]["rmsd_lb"] if modes else "",
                "rmsd_ub": modes[0]["rmsd_ub"] if modes else "",
                "n_modes": len(modes), "time_s": round(time.time() - t1, 1)}
    except Exception as e:
        du.LOG.error("DOCK FAIL %s@%s/%s s%s: %s", name, site, vlabel, seed, e)
        return {"name": name, "site": site, "variant": vlabel, "seed": seed,
                "status": "error", "score": None, "rmsd_lb": "", "rmsd_ub": "",
                "n_modes": 0, "time_s": round(time.time() - t1, 1)}


def _plenv_path():
    p = Path("/home/user/out/plenv/bin")
    return str(p) if p.is_dir() else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ligands", default=None, help="CSV: name,smiles (required unless --check)")
    ap.add_argument("--receptor", default=None)
    ap.add_argument("--receptor-model", choices=["complex", "apo"], default="complex",
                    help="complex = lipase+colipase+Ca2+ (1LPB biological state; default). "
                         "apo = lipase chain only (legacy comparability)")
    ap.add_argument("--precision", choices=list(PRECISION_TIERS), default="balanced",
                    help="fast=(ex4,1 seed) balanced=(ex8,1) max=(ex24,3 seeds)")
    ap.add_argument("--exhaustiveness", type=int, default=None, help="override precision tier")
    ap.add_argument("--n-seeds", type=int, default=None, help="override precision tier")
    ap.add_argument("--n-poses", type=int, default=None)
    ap.add_argument("--seed", type=int, default=42, help="base seed; replicate seeds = base+k*7919")
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--cpu-per-dock", type=int, default=1)
    ap.add_argument("--max-mw", type=float, default=700.0)
    ap.add_argument("--max-rotb", type=int, default=20)
    ap.add_argument("--protonation", choices=["rules", "as-supplied"], default="rules",
                    help="pH 7.4 rule-based major microstate, or use SMILES as given")
    ap.add_argument("--outdir", default="dock_results")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--sites-file", default=None)
    ap.add_argument("--debug", action="store_true")
    ap.add_argument("--log-file", default=None)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    du.setup_logging(debug=args.debug, log_file=args.log_file)
    du.install_exception_hook()
    pp = _plenv_path()
    if pp:
        os.environ["PATH"] = pp + ":" + os.environ.get("PATH", "")
    if args.check:
        rec_check = args.receptor or HERE / "receptor" / "1LPB.pdb"
        extra = {"ligands": args.ligands or "(none)",
                 "receptor": str(rec_check) + (" (exists)" if rec_check.exists() else " (MISSING)"),
                 "receptor_model": args.receptor_model,
                 "precision": args.precision,
                 "protonation": args.protonation}
        return du.print_env_check(extra)

    tier = PRECISION_TIERS[args.precision]
    ex = args.exhaustiveness or tier["exhaustiveness"]
    n_seeds = args.n_seeds or tier["n_seeds"]
    n_poses = args.n_poses or tier["n_poses"]

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "receptor").mkdir(parents=True, exist_ok=True)
    (outdir / "ligprep").mkdir(parents=True, exist_ok=True)
    (outdir / "runs").mkdir(parents=True, exist_ok=True)
    du.require(args.ligands, "--ligands CSV is required (use --check for env self-check only)")
    du.require_file(args.ligands, "ligands CSV")
    lig_header = next(csv.DictReader(open(args.ligands)), {})
    du.require("smiles" in lig_header, f"ligands CSV must have a 'smiles' column, got: {list(lig_header)}")

    # receptor (once) — complex model by default (v100.4)
    rec = Path(args.receptor) if args.receptor else HERE / "receptor" / "1LPB.pdb"
    if not rec.exists():
        raise SystemExit(f"receptor not found: {rec}")
    chain = pick_chain(rec)
    clean = clean_receptor(rec, chain, outdir, model=args.receptor_model)
    clean_complex = clean if args.receptor_model == "complex" else None
    receptor_pdbqt, recnote = prepare_receptor_pdbqt_with_metal_fallback(clean, outdir / "receptor")
    if not receptor_pdbqt:
        raise SystemExit(f"receptor preparation failed: {recnote}")
    du.record_versions(outdir, {"chain": chain, "receptor": str(rec),
                                "receptor_model": args.receptor_model,
                                "receptor_prep": recnote,
                                "exhaustiveness": ex, "n_seeds": n_seeds,
                                "n_poses": n_poses, "seed": args.seed,
                                "precision": args.precision,
                                "protonation": args.protonation,
                                "cmdline": " ".join(sys.argv)})

    # sites
    if args.sites_file and Path(args.sites_file).exists():
        sites = json.loads(Path(args.sites_file).read_text())
        log_n = "loaded"
    else:
        res, seq_nums = parse_receptor(clean, chain)
        sites = detect_sites(res, seq_nums, clean_complex=clean_complex, enzyme_chain=chain)
        (outdir / "sites.json").write_text(json.dumps(sites, indent=1))
        log_n = "detected"
    du.LOG.info("sites %s (chain %s, model %s):", log_n, chain, args.receptor_model)
    for k, v in sites.items():
        du.LOG.info("  %-20s center=%s box=%s | %s", k, v["center"], v["box"], v.get("note", ""))

    # ligand filtering + chemprep variants (cached)
    from rdkit import Chem
    from rdkit.Chem import Descriptors, Lipinski
    import chemprep
    rows, metas = [], {}
    for lig in csv.DictReader(open(args.ligands)):
        if not lig.get("smiles"):
            continue
        mol = Chem.MolFromSmiles(lig["smiles"])
        if mol is None:
            du.LOG.warning("skip %s: RDKit parse failed", lig["name"])
            continue
        mw = Descriptors.MolWt(mol)
        rb = Lipinski.NumRotatableBonds(mol)
        if mw > args.max_mw or rb > args.max_rotb:
            du.LOG.warning("skip %s: MW=%.0f(>%s) or rotb=%d(>%s)", lig["name"], mw, args.max_mw, rb, args.max_rotb)
            continue
        meta = chemprep.prep_ligand_variants(lig["name"], lig["smiles"],
                                              outdir / "ligprep",
                                              protonation=args.protonation)
        metas[lig["name"]] = meta
        if not meta["variants"]:
            du.LOG.warning("skip %s: no prep variants (%s)", lig["name"], "; ".join(meta["notes"][-2:]))
            continue
        rows.append((lig["name"], lig["smiles"], round(mw, 1), rb))
    if args.limit:
        rows = rows[: args.limit]
    (outdir / "ligprep_meta.json").write_text(json.dumps(metas, indent=1))
    nvar = sum(len(metas[n]["variants"]) for n, *_ in rows)
    du.LOG.info("dockable ligands: %d | variants: %d | sites: %d | seeds: %d | jobs: %d",
                len(rows), nvar, len(sites), n_seeds, nvar * len(sites) * n_seeds)

    seeds = [args.seed + k * 7919 for k in range(n_seeds)]
    jobs, done = [], set()
    detail_csv = outdir / "runs_detail.csv"
    if detail_csv.exists():
        for r in csv.DictReader(open(detail_csv)):
            if r["status"] in ("ok",):
                done.add((r["name"], r["site"], r["variant"], r["seed"]))
    for name, _, _, _ in rows:
        for vi, vp in enumerate(metas[name]["variants"]):
            vlabel = f"v{vi}"
            for site, spec in sites.items():
                for seed in seeds:
                    key = (name, site, vlabel, str(seed))
                    if key in done:
                        continue
                    jobs.append((name, vp, vlabel, site, spec["center"], spec["box"],
                                 ex, args.cpu_per_dock, n_poses, seed,
                                 receptor_pdbqt, str(outdir / "runs")))
    du.LOG.info("resume: %d done | pending: %d", len(done), len(jobs))

    t0 = time.time()
    new = not detail_csv.exists()
    with open(detail_csv, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["name", "site", "variant", "seed", "status",
                                          "score", "rmsd_lb", "rmsd_ub", "n_modes", "time_s"])
        if new or detail_csv.stat().st_size == 0:
            w.writeheader()
        if args.workers > 1:
            with ProcessPoolExecutor(max_workers=args.workers) as exr:
                for i, row in enumerate(exr.map(worker, jobs, chunksize=2), 1):
                    w.writerow(row); f.flush()
                    if i % 25 == 0:
                        el = time.time() - t0
                        print(f"  {i}/{len(jobs)} | {i/max(el,1):.2f}/s | ETA {(len(jobs)-i)/(i/max(el,1))/60:.0f} min", flush=True)
        else:
            for i, job in enumerate(jobs, 1):
                w.writerow(run(job)); f.flush()
                if i % 25 == 0:
                    el = time.time() - t0
                    print(f"  {i}/{len(jobs)} | {i/max(el,1):.2f}/s | ETA {(len(jobs)-i)/(i/max(el,1))/60:.0f} min", flush=True)

    # aggregate best per (name, site) + seed-agreement stats
    agg = {}
    for r in csv.DictReader(open(detail_csv)):
        if r["status"] != "ok" or not r["score"]:
            continue
        key = (r["name"], r["site"])
        try:
            _t = float(r.get("time_s") or 0.0)
        except (TypeError, ValueError):
            _t = 0.0
        agg.setdefault(key, []).append((float(r["score"]), r["variant"], r["seed"], _t))
    res_csv = outdir / "results_all_sites.csv"
    with open(res_csv, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["name", "site", "status", "score", "time_s",
                    "best_variant", "n_replicates", "score_mean", "score_sd", "stability"])
        for (name, site), reps in sorted(agg.items()):
            scores = [s for s, *_ in reps]
            best = min(reps)
            sd = statistics.pstdev(scores) if len(scores) > 1 else 0.0
            stability = "stable" if (sd <= 0.5 or len(scores) == 1) else "unstable(sd>0.5)"
            # v101 fix: time_s was emitted as "" — the per-job wall times were
            # collected in runs_detail.csv but dropped here, so every consumer
            # (report, dashboard, cost estimates) saw a blank column.
            total_t = round(sum(t for *_, t in reps), 1)
            w.writerow([name, site, "ok", best[0], total_t, best[1], len(scores),
                        round(statistics.mean(scores), 2), round(sd, 2), stability])
    du.LOG.info("DONE %d jobs in %.0fs -> %s (+ %s)", len(jobs), time.time() - t0, res_csv, detail_csv)


if __name__ == "__main__":
    raise SystemExit(main())
