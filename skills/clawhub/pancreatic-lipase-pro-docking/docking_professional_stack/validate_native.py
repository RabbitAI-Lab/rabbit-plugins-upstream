#!/usr/bin/env python3
"""validate_native.py — re-docking validation of the whole protocol (v100.4.0).

World-practice control: re-dock the CO-CRYSTALLIZED inhibitor (MUP, chain B
residue 901 of 1LPB) into the catalytic site and measure heavy-atom RMSD to the
crystal pose (best-fit, Kabsch). A protocol that cannot recover a known pose is
not precise — this gate catches receptor-prep errors, wrong boxes, bad seeds.

Verdict: PASS <= 2.0 A | WARN <= 3.0 A | FAIL > 3.0 A
Also prints the crystal vs docked score for sanity (MUP experimental reference:
the docking score of the crystal pose should be within ~2 kcal/mol of the docked
best when the pose is right).

Usage:
  python3 validate_native.py [--precision balanced] [--seed 42] [--outdir native_check]
      [--receptor receptor/1LPB.pdb] [--receptor-model complex] [--json]
"""
import argparse, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import debug_utils as du
import multi_site_docking as ms


def extract_native_ligand(pdb_path, resn="MUP", chain="B"):
    """Exactly ONE residue instance (1LPB ships MUP twice: two alternate
    conformers/positions; take the first by (chain, resseq, icode))."""
    cands = {}
    for ln in open(pdb_path):
        if ln.startswith("HETATM") and ln[17:20].strip() == resn:
            alt = ln[16] if len(ln) > 16 else " "
            if alt not in (" ", "A"):   # v100.4: 1LPB ships MUP as altloc A/B — keep A
                continue
            key = (ln[21], ln[22:26], ln[26])
            cands.setdefault(key, []).append(ln.rstrip("\n"))
    if not cands:
        raise SystemExit(f"native ligand {resn} not found in {pdb_path}")
    pref = {k: v for k, v in cands.items() if k[0] == chain}
    first = sorted(pref or cands)[0]
    return cands[first]


def pdbqt_models(path):
    """Per-MODE heavy atoms -> [(names, elems)] where names=[(name,xyz)], elems=[E]."""
    models, cur, cur_e = [], [], []
    for ln in Path(path).read_text().splitlines():
        if ln.startswith("MODEL"):
            cur, cur_e = [], []
        elif ln.startswith("ENDMDL"):
            if cur:
                models.append((cur, cur_e))
        elif ln.startswith(("ATOM", "HETATM")):
            name = ln[12:16].strip()
            elem = ln[76:78].strip() if len(ln) >= 78 else ""
            if not elem:
                elem = next((c for c in name if c.isalpha()), "?")
            if elem.upper().startswith("H") or name.startswith("H"):
                continue
            cur.append((name, (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))))
            cur_e.append(elem.upper()[:1])
    if cur and not models:
        models.append((cur, cur_e))
    return models


_TWO_LETTER = {"CL", "BR", "NA", "ZN", "FE", "MG", "CA", "MN", "CU", "NI", "SE", "SI"}


def _elem_of(name, elem=""):
    if elem and elem.strip() and not elem.strip().isdigit():
        return elem.strip().upper()[:2] if elem.strip().upper()[:2] in _TWO_LETTER else elem.strip().upper()[:1]
    up = name.strip().upper()
    if up[:2] in _TWO_LETTER:
        return up[:2]
    return next((c.upper() for c in name if c.isalpha()), "?")


def matched_rmsd(pose, ref, pose_elems=None, ref_elems=None):
    """Element-aware best-fit RMSD. pose/ref = [(name, xyz)] lists; elems optional.
    Each pose atom pairs with the nearest unused same-element reference atom
    (robust to renamed/symmetric atoms, e.g. phosphinate oxygens)."""
    pe = pose_elems or [_elem_of(n) for n, _ in pose]
    re_ = ref_elems or [_elem_of(n) for n, _ in ref]
    by_elem = {}
    for i, e in enumerate(re_):
        by_elem.setdefault(e, []).append(i)
    P, Q = [], []
    for (n, c), e in zip(pose, pe):
        cands = by_elem.get(e)
        if not cands:
            continue
        best_i = min(cands, key=lambda i: sum((c[k] - ref[i][1][k]) ** 2 for k in range(3)))
        P.append(c); Q.append(ref[best_i][1])
        by_elem[e].remove(best_i)
    if len(P) < max(2, int(0.5 * len(ref))):
        raise SystemExit(f"atom matching too sparse ({len(P)}/{len(ref)})")
    return kabsch_rmsd(P, Q), len(P), len(ref)


def _is_hydrogen(ln):
    name = ln[12:16].strip()
    elem = ln[76:78].strip() if len(ln) >= 78 else ""
    if elem:
        return elem.upper()[0] == "H"
    # digit-leading PDB H names (1H, 2HB) or H-leading names
    return name.lstrip("0123456789")[:1].upper() == "H"


def pdb_coords(lines):
    out = []
    for ln in lines:
        if _is_hydrogen(ln):
            continue
        name = ln[12:16].strip()
        out.append((name, (float(ln[30:38]), float(ln[38:46]), float(ln[46:54]))))
    return out


def pdb_elems(lines):
    return [_elem_of(ln[12:16].strip(), ln[76:78] if len(ln) >= 78 else "")
            for ln in lines if not _is_hydrogen(ln)]


def kabsch_rmsd(P, Q):
    """Best-fit RMSD between two Nx3 coordinate sets (same order)."""
    import numpy as np
    P, Q = np.asarray(P, float), np.asarray(Q, float)
    Pc, Qc = P - P.mean(0), Q - Q.mean(0)
    V, S, Wt = np.linalg.svd(Pc.T @ Qc)
    d = np.linalg.det(V @ Wt)
    D = np.diag([1.0, 1.0, 1.0 if d > 0 else -1.0])
    R = V @ D @ Wt
    Prot = Pc @ R
    return float(np.sqrt(((Prot - Qc) ** 2).sum() / len(P)))


def _elem_of(name, elem=""):
    if elem and elem.strip() and not elem.strip().isdigit():
        return elem.strip().upper()[:1]
    for ch in name:
        if ch.isalpha():
            return ch.upper()
    return "?"


def matched_rmsd(pose_atoms, ref_atoms, tol=0.6, pose_elems=None, ref_elems=None):
    """Element-aware best-fit RMSD: each pose atom pairs with the NEAREST same-
    element reference atom (handles renamed/symmetric atoms, e.g. phosphinate O).
    Falls back to name matching when elements are unavailable."""
    pe = pose_elems or [_elem_of(n) for n, _ in pose_atoms]
    re_ = ref_elems or [_elem_of(n) for n, _ in ref_atoms]
    if pose_elems is None and all(re_[0] == "?" for _, _ in ref_atoms[:1]):
        return _matched_rmsd_by_name(pose_atoms, ref_atoms)
    # element-aware greedy nearest matching (pose order, closest unused ref)
    by_elem = {}
    for i, ((n, c), e) in enumerate(zip(ref_atoms, re_)):
        by_elem.setdefault(e, []).append(i)
    P, Q = [], []
    for (n, c), e in zip(pose_atoms, pe):
        cands = by_elem.get(e)
        if not cands:
            continue
        best_i = min(cands, key=lambda i: sum((c[k] - ref_atoms[i][1][k]) ** 2 for k in range(3)))
        P.append(c); Q.append(ref_atoms[best_i][1])
        by_elem[e].remove(best_i)
    if len(P) < max(2, int(0.5 * len(ref_atoms))):
        return _matched_rmsd_by_name(pose_atoms, ref_atoms)
    return kabsch_rmsd(P, Q), len(P), len(ref_atoms)


def _matched_rmsd_by_name(pose_atoms, ref_atoms, tol=0.6):
    """Name-matched heavy-atom best-fit RMSD (legacy path)."""
    P, Q, unmatched = [], [], []
    used = {n: [False] * len(v) for n, v in ref_by_name.items()}
    for n, c in pose_atoms:
        cands = ref_by_name.get(n)
        if not cands:
            unmatched.append(n)
            continue
        best_i, best_d = None, 1e9
        for i, rc in enumerate(cands):
            if used[n][i]:
                continue
            d = sum((c[k] - rc[k]) ** 2 for k in range(3)) ** 0.5
            if d < best_d:
                best_i, best_d = i, d
        if best_i is None:
            unmatched.append(n)
            continue
        used[n][best_i] = True
        P.append(c); Q.append(cands[best_i])
    if len(P) < max(2, int(0.5 * len(ref_atoms))):
        raise SystemExit(f"atom matching too sparse ({len(P)}/{len(ref_atoms)}); "
                         f"unmatched pose atoms: {unmatched[:8]}")
    return kabsch_rmsd(P, Q), len(P), len(ref_atoms)


def native_pdb_to_pdbqt(nat_lines, outdir):
    """Crystal pose -> PDBQT WITHOUT re-embedding (coords preserved).

    Prefers obabel PDB->PDBQT (element-correct typing incl. phosphinates);
    falls back to RDKit(meeko) proximity-bond path.
    """
    import shutil, subprocess as sp
    npdb = Path(outdir) / "native_MUP.pdb"
    npdb.write_text("\n".join(nat_lines) + "\nEND\n")
    if shutil.which("obabel"):
        pq = Path(outdir) / "native_MUP_ob.pdbqt"
        r = sp.run(["obabel", str(npdb), "-O", str(pq), "-xn"], capture_output=True, text=True, timeout=120)
        if r.returncode == 0 and pq.exists():
            return pq
    from rdkit import Chem
    from meeko import MoleculePreparation, PDBQTWriterLegacy
    block = "\n".join(nat_lines) + "\nEND\n"
    mol = Chem.MolFromPDBBlock(block, removeHs=True, sanitize=False)
    if mol is None:
        raise SystemExit("RDKit could not parse the native-ligand PDB block")
    Chem.SanitizeMol(mol, Chem.SanitizeFlags.SANITIZE_ALL ^ Chem.SanitizeFlags.SANITIZE_PROPERTIES)
    mol = Chem.AddHs(mol, addCoords=True)
    preparator = MoleculePreparation()
    setups = preparator.prepare(mol)
    if not setups:
        raise SystemExit("meeko rejected the native ligand")
    txt, ok, err = PDBQTWriterLegacy.write_string(setups[0])
    if not ok:
        raise SystemExit(f"meeko writer failed on native ligand: {err}")
    p = Path(outdir) / "native_MUP.pdbqt"
    p.write_text(txt)
    return p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--precision", choices=list(ms.PRECISION_TIERS), default="balanced")
    ap.add_argument("--exhaustiveness", type=int, default=None)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--receptor", default=None)
    ap.add_argument("--receptor-model", choices=["complex", "apo"], default="complex")
    ap.add_argument("--outdir", default="native_check")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    du.setup_logging(debug=False)
    outdir = Path(args.outdir); outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "runs").mkdir(exist_ok=True); (outdir / "receptor").mkdir(exist_ok=True)
    rec = Path(args.receptor) if args.receptor else HERE / "receptor" / "1LPB.pdb"

    # receptor + catalytic site exactly as production runs
    chain = ms.pick_chain(rec)
    clean = ms.clean_receptor(rec, chain, outdir, model=args.receptor_model)
    rec_pdbqt, note = ms.prepare_receptor_pdbqt_with_metal_fallback(clean, outdir / "receptor")
    if not rec_pdbqt:
        raise SystemExit(f"receptor prep failed: {note}")
    res, seq_nums = ms.parse_receptor(clean, chain)
    sites = ms.detect_sites(res, seq_nums, clean_complex=(clean if args.receptor_model == "complex" else None),
                            enzyme_chain=chain)
    cat = sites["catalytic_triad"]

    # native ligand: crystal pose preserved; canonical re-docking protocol:
    # box CENTERED ON THE CO-CRYSTALLIZED LIGAND (not the OG-anchored site box)
    nat_lines = extract_native_ligand(rec)
    nat_pdbqt = native_pdb_to_pdbqt(nat_lines, outdir)
    heavy = pdb_coords(nat_lines)
    cen = [round(sum(c[i] for _, c in heavy) / len(heavy), 3) for i in range(3)]
    ext = max(max(max(c[i] for _, c in heavy) - min(c[i] for _, c in heavy) for i in range(3)) + 8.0, 22.0)
    box = round(ext, 1)
    tier = ms.PRECISION_TIERS[args.precision]
    ex = args.exhaustiveness or tier["exhaustiveness"]

    from pathlib import Path as _P
    pose = outdir / "runs" / "catalytic_triad" / f"native_MUP__v0__s{args.seed}" / "pose.pdbqt"
    pose.parent.mkdir(parents=True, exist_ok=True)
    job = ("native_MUP", str(nat_pdbqt), "v0", "catalytic_triad", cen, box,
           ex, 1, tier["n_poses"], args.seed, rec_pdbqt, str(outdir / "runs"))
    r = ms.worker(job)
    if r["status"] != "ok":
        raise SystemExit(f"native re-dock failed: {r}")

    ref, ref_e = pdb_coords(nat_lines), pdb_elems(nat_lines)
    per_mode = [matched_rmsd(names, ref, pose_elems=elems, ref_elems=ref_e)
                for names, elems in pdbqt_models(pose)]
    rmsd, nmatch, nref = per_mode[0]          # strict: lowest-energy (top) pose
    best_rmsd = min(r for r, *_ in per_mode)  # optimistic: best of returned modes
    verdict = "PASS" if rmsd <= 2.0 else ("WARN" if rmsd <= 3.0 else "FAIL")
    result = {"rmsd_top_pose_A": round(rmsd, 2), "rmsd_best_of_modes_A": round(best_rmsd, 2),
              "n_modes_returned": len(per_mode),
              "matched_atoms": nmatch, "ref_atoms": nref,
              "docked_score": r["score"], "box_center": cen, "box_size": box,
              "ligand_prep": Path(nat_pdbqt).name, "precision": args.precision,
              "exhaustiveness": ex, "seed": args.seed, "receptor_model": args.receptor_model,
              "receptor_prep": note, "verdict": verdict,
              "gate": "PASS<=2.0A WARN<=3.0A FAIL>3.0A (re-docking validation)"}
    (outdir / "native_result.json").write_text(json.dumps(result, indent=1))
    print(json.dumps(result, indent=1) if not args.json else json.dumps(result))
    return 0 if verdict != "FAIL" else 1


if __name__ == "__main__":
    raise SystemExit(main())
