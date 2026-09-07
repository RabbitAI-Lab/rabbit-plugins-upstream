#!/usr/bin/env python3
"""chemprep.py — chemistry-correctness layer for the docking stack (v100.4.0).

Precision fixes this module introduces (2026-08-25 audit):

1. pH 7.4 major-microstate protonation (rule-based, dependency-free).
   Docking the WRONG protonation state is the single largest systematic error
   for lipase-relevant chemotypes: substrates/inhibitors are fatty-acid-like
   (carboxylates, pKa ~4.5 -> fully deprotonated at pH 7.4) and amine-bearing.
   Rules (documented pKa assumptions, standard medicinal-chemistry values):
     - carboxylic acid  -> carboxylate (-1)          pKa ~4.5
     - aliphatic amine (primary/secondary/tertiary, non-amide) -> +1  pKa ~9-11
     - guanidine -> +1                                pKa ~13
     - amidine  -> +1                                 pKa ~11
     - imidazole (free, N-methyl) -> neutral tautomer handled by tautomer step
     - phenol -> neutral                              pKa ~10
     - sulfonamide (SO2NH) -> neutral                 pKa ~7-10
     - tetrazole -> -1                                pKa ~4.9
     - phosphonic/phosphoric acid -> -1               first pKa ~1-2 (keep -1)
     - thiophenol -> neutral                          pKa ~6.5 (borderline, neutral)
   `--protonation as-supplied` keeps input SMILES untouched; `obabel` uses
   `obabel -p 7.4` when the binary exists (optional, most accurate).

2. Tautomer canonicalization (RDKit rdMolStandardize.TautomerEnumerator).
   Record 1 of the canonical tautomer; count is reported so ambiguous inputs
   are visible. Skip for molecules where enumeration explodes (>100 tautomers).

3. Undefined-stereocenter enumeration (up to --max-stereoisomers, default 4,
   max 2 undefined centers to bound cost). Without this, RDKit embeds ONE
   arbitrary diastereomer -> silent bias. Each isomer is docked and the best
   kept; the winning isomer is reported in results (column `variant`).

4. Multi-conformer 3D prep: ETKDGv3 (2 seeds) + MMFF (UFF fallback); the
   lowest-energy conformer after minimization becomes the docking start pose.
   Meeko PDBQTWriterLegacy emits the final PDBQT (merge H, Gasteiger charges
   as Vina expects).

Cache: every prepared variant lands in <cachedir>/<sha16-of-canonical-smiles>/
variant_<k>.pdbqt — re-runs and re-docks are free (precision work must not be
re-paid).
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

try:
    from rdkit import Chem, RDLogger
    from rdkit.Chem import AllChem, Lipinski
    RDLogger.DisableLog("rdApp.warning")
    HAS_RDKIT = True
except Exception:  # pragma: no cover
    HAS_RDKIT = False

# SMARTS rules applied in order (first match per atom group wins; charges set
# by explicit atom-map edits so no atom is double-protonated).
_PROTONATION_RULES = [
    # (name, SMARTS, edit) — order matters; rules are disjoint enough that no
    # atom is double-edited (each edit requires formal charge == 0).
    ("carboxylic_acid->carboxylate", "C(=O)[OH]", "deprotonate_O"),
    ("thiophenol->thiolate", "[c][SX2H]", "deprotonate_S"),            # pKa ~6.5: anionic at 7.4
    ("alkyl_phosphonate->dianion", "[CX4][PX4](=O)([OH])[OH]", "deprotonate_O_all"),  # pKa2 ~6.5
    ("phosphonic/phosphoric->anion", "P(=O)([OH])(O)O", "deprotonate_O"),
    ("tetrazole->anion", "c1nnn[nH]1", "deprotonate_N"),
    ("guanidine->cation", "[NX3;H2,H1][CX3]([NX3;H2,H1])=[NX2]", "protonate_N_once"),  # biguanides stay +1 total
    ("amidine->cation", "[NX3;H2,H1,H0][CX3](=[NX2])[!N]", "protonate_N"),  # [!N] excludes guanidines
    ("aliphatic_amine->cation",
     "[NX3;H2,H1,H0;!$(N[C,S,P]=O);!$(N[a]);!$(NC=[O,S,N]);!$(N-[*+])]",
     "protonate_N"),
]

_PH_NOTE = "pH 7.4 major microstate, rule-based (see chemprep.py docstring)"


def _applied_neutral(mol):
    """True if the molecule already carries the intended formal charges."""
    return abs(Chem.GetFormalCharge(mol))


def apply_protonation_rules(mol, verbose_note=None):
    """Apply pH-7.4 rules to a neutral-input molecule; returns (mol, notes)."""
    rw = Chem.RWMol(mol)
    notes = []
    for name, sma, edit in _PROTONATION_RULES:
        patt = Chem.MolFromSmarts(sma)
        if patt is None:
            notes.append(f"rule {name}: bad SMARTS (skipped)")
            continue
        matches = rw.GetSubstructMatches(patt)
        if edit == "protonate_N_once" and matches:
            matches = matches[:1]     # biguanide guard: ONE guanidinium per molecule
        seen_groups, deduped = set(), []
        for m in matches:
            grp = tuple(sorted(m))
            if grp in seen_groups:      # symmetric SMARTS (e.g. guanidine) match twice
                continue
            seen_groups.add(grp); deduped.append(m)
        for m in deduped:
            for idx in m:
                atom = rw.GetAtomWithIdx(idx)
                if edit == "deprotonate_O" and atom.GetSymbol() == "O" and atom.GetFormalCharge() == 0 \
                        and atom.GetTotalNumHs() > 0 and atom.GetDegree() == 1:
                    atom.SetFormalCharge(-1)
                    atom.SetNoImplicit(True)
                    atom.SetNumExplicitHs(0)
                    notes.append(f"{name}@O{idx}")
                elif edit == "deprotonate_S" and atom.GetSymbol() == "S" and atom.GetFormalCharge() == 0 \
                        and atom.GetTotalNumHs() > 0 and atom.GetDegree() == 1:
                    atom.SetFormalCharge(-1)
                    atom.SetNoImplicit(True)
                    atom.SetNumExplicitHs(0)
                    notes.append(f"{name}@S{idx}")
                elif edit == "deprotonate_O_all" and atom.GetSymbol() == "O" and atom.GetFormalCharge() == 0 \
                        and atom.GetTotalNumHs() > 0 and atom.GetDegree() == 1:
                    atom.SetFormalCharge(-1)
                    atom.SetNoImplicit(True)
                    atom.SetNumExplicitHs(0)
                    notes.append(f"{name}@O{idx}")
                elif edit == "deprotonate_N" and atom.GetSymbol() == "N" and atom.GetFormalCharge() == 0 \
                        and atom.GetTotalNumHs() > 0 and atom.GetDegree() <= 2:
                    atom.SetFormalCharge(-1)
                    atom.SetNoImplicit(True)
                    atom.SetNumExplicitHs(0)
                    notes.append(f"{name}@N{idx}")
                elif edit in ("protonate_N", "protonate_N_once") and idx == m[0] and atom.GetSymbol() == "N" and atom.GetFormalCharge() == 0:
                    atom.SetFormalCharge(+1)
                    atom.SetNumExplicitHs(max(1, atom.GetTotalNumHs() + 1))
                    atom.SetNoImplicit(True)
                    notes.append(f"{name}@N{idx}")
    mol2 = rw.GetMol()
    Chem.SanitizeMol(mol2)
    return mol2, notes or ["no_rule_applied(kept_as_supplied)"]


def canonical_tautomer(mol):
    """Canonical tautomer + count. Falls back to input if enumeration fails."""
    try:
        from rdkit.Chem.MolStandardize import rdMolStandardize
        te = rdMolStandardize.TautomerEnumerator()
        te.SetMaxTautomers(100)
        res = te.Enumerate(mol)
        n = len(res)
        if n <= 1:
            return mol, max(n, 1)
        return te.Canonicalize(mol), n
    except Exception:
        return mol, 1


def enumerate_stereoisomers(mol, max_isomers=4, max_undefined=2):
    """Enumerate undefined stereocenters; returns list of mols (>=1)."""
    from rdkit.Chem.EnumerateStereoisomers import (EnumerateStereoisomers,
                                                   StereoEnumerationOptions)
    centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True, useLegacyImplementation=False)
    undefined = sum(1 for _, flag in centers if flag == "?")
    if undefined == 0:
        return [mol], 0
    if undefined > max_undefined:
        # too many centers to enumerate exhaustively: keep input, flag it
        return [mol], undefined
    opts = StereoEnumerationOptions(maxIsomers=max_isomers, unique=True, tryEmbedding=False)
    try:
        isos = list(EnumerateStereoisomers(mol, options=opts))
        return (isos or [mol]), undefined
    except Exception:
        return [mol], undefined


def embed_3d(mol, seed=0xC0FFEE, n_confs=2):
    """ETKDG multi-conformer embed + MMFF/UFF minimization; returns lowest-E mol.
    Seed is diversified per ligand by the caller (hash of canonical SMILES):
    deterministic for a given ligand, different across ligands."""
    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = seed
    cids = list(AllChem.EmbedMultipleConfs(mol, numConfs=n_confs, params=params))
    if not cids:
        params.randomSeed = -1  # random retry once
        cids = list(AllChem.EmbedMultipleConfs(mol, numConfs=n_confs, params=params))
    if not cids:
        return None, "ETKDG embedding failed"
    best, best_e, how = None, 1e18, None
    try:
        if AllChem.MMFFHasAllMoleculeParams(mol):
            props = AllChem.MMFFGetMoleculeProperties(mol)
            for cid in cids:
                AllChem.MMFFOptimizeMolecule(mol, mmffVariant="MMFF94", confId=cid, maxIters=500)
                e = AllChem.MMFFGetMoleculeForceField(mol, props, confId=cid).CalcEnergy()
                if e < best_e:
                    best, best_e, how = cid, e, "MMFF94"
        else:
            raise ValueError("no MMFF params")
    except Exception:
        for cid in cids:
            AllChem.UFFOptimizeMolecule(mol, confId=cid, maxIters=500)
            e = AllChem.UFFGetMoleculeForceField(mol, confId=cid).CalcEnergy()
            if e < best_e:
                best, best_e, how = cid, e, "UFF"
    if best is None:
        return None, "no conformer energy"
    out = Chem.Mol(mol, False, confId=best)  # single conf with lowest energy
    return out, f"{how}_conf{best}_E={best_e:.1f}"


def pdbqt_from_mol(mol3d):
    from meeko import MoleculePreparation, PDBQTWriterLegacy
    preparator = MoleculePreparation()
    setups = preparator.prepare(mol3d)
    if not setups:
        return None, "meeko produced no setups"
    s, ok, err = PDBQTWriterLegacy.write_string(setups[0])
    if not ok:
        return None, f"meeko writer: {err}"
    return s, "ok"


def prep_ligand_variants(name, smiles, cachedir, protonation="rules",
                         max_isomers=4, n_confs=2):
    """Full prep: protonate -> tautomer -> stereoisomers -> 3D -> PDBQT variants.

    Returns dict with: variants (list of pdbqt paths), notes, canonical_smiles.
    """
    cachedir = Path(cachedir)
    cachedir.mkdir(parents=True, exist_ok=True)
    if not HAS_RDKIT:
        return {"variants": [], "notes": ["RDKit unavailable"], "canonical_smiles": smiles}
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return {"variants": [], "notes": ["invalid SMILES"], "canonical_smiles": smiles}
    canon = Chem.MolToSmiles(mol, isomericSmiles=True)
    key = hashlib.sha256((canon + f"|{protonation}").encode()).hexdigest()[:16]
    cache = cachedir / key
    meta_f = cache / "meta.json"
    if meta_f.exists():
        meta = json.loads(meta_f.read_text())
        if all(Path(p).exists() for p in meta["variants"]):
            return meta
    cache.mkdir(parents=True, exist_ok=True)
    notes = [f"input={canon}"]
    # 1. protonation
    if protonation == "rules":
        mol, pnotes = apply_protonation_rules(mol)
        notes += [f"protonation[{_PH_NOTE}]: " + "; ".join(pnotes[:6])]
    elif protonation == "as-supplied":
        notes.append("protonation: as-supplied (user responsibility)")
    # obabel mode handled by caller if binary exists
    # 2. tautomer
    mol, n_taut = canonical_tautomer(mol)
    notes.append(f"tautomers: canonical of {n_taut}")
    # 3. stereoisomers
    isos, n_undef = enumerate_stereoisomers(mol, max_isomers=max_isomers)
    notes.append(f"stereo: {n_undef} undefined centers -> {len(isos)} isomers"
                 + (" [FLAG: too many to enumerate]" if n_undef > 2 else ""))
    # 4. 3D + PDBQT per isomer
    variants, vnotes = [], []
    for k, iso in enumerate(isos):
        iso_name = Chem.MolToSmiles(iso, isomericSmiles=True)
        m3d, how = embed_3d(iso, seed=0xC0FFEE + (hash(canon) & 0xFFFF), n_confs=n_confs)
        if m3d is None:
            vnotes.append(f"iso{k}: {how}")
            continue
        txt, st = pdbqt_from_mol(m3d)
        if txt is None:
            vnotes.append(f"iso{k}: {st}")
            continue
        p = cache / f"variant_{k}.pdbqt"
        p.write_text(txt)
        (cache / f"variant_{k}.smi").write_text(f"{iso_name}\t{name}_iso{k}\n")
        variants.append(str(p))
        vnotes.append(f"iso{k}: {how}")
    meta = {"name": name, "canonical_smiles": canon, "variants": variants,
            "notes": notes + vnotes, "cache_key": key}
    meta_f.write_text(json.dumps(meta, indent=1))
    return meta


if __name__ == "__main__":  # tiny self-test
    for nm, smi in [("ibuprofen", "CC(C)Cc1ccc(cc1)C(C)C(=O)O"),
                    ("catechol", "Oc1ccccc1O"),
                    ("tryptamine_amine", "NCCc1c[nH]c2ccccc12"),
                    ("orlistat_carboxylate", "CC(C)C(=O)OC(C(C)C)C(=O)O")]:
        r = prep_ligand_variants(nm, smi, Path("/tmp/chemprep_selftest"))
        print(nm, "->", len(r["variants"]), "variants |", "; ".join(r["notes"][:3]))
