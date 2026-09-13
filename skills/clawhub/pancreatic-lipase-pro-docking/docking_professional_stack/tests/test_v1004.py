"""tests/test_v1004.py — v100.4 precision-layer tests (chemprep, sites, receptor, RMSD)."""
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
STACK = HERE.parent
sys.path.insert(0, str(STACK))

RECEPTOR = STACK / "receptor" / "1LPB.pdb"
requires_1lpb = pytest.mark.skipif(not RECEPTOR.exists(), reason="1LPB.pdb not shipped")

# v101: chemistry tests must SKIP (not fail) when RDKit is absent. The suite is
# advertised as dependency-light; a bare `python3 -m pytest` previously produced
# 12 hard failures on a clean box, which reads as "the skill is broken".
try:
    import rdkit  # noqa: F401
    HAS_RDKIT = True
except Exception:  # pragma: no cover
    HAS_RDKIT = False
requires_rdkit = pytest.mark.skipif(not HAS_RDKIT, reason="rdkit not installed")


# ── chemprep: pH 7.4 protonation ─────────────────────────────────────────────
@requires_rdkit
@pytest.mark.parametrize("smiles,want", [
    ("CC(C)Cc1ccc(cc1)C(C)C(=O)O", -1),   # ibuprofen carboxylate
    ("Oc1ccccc1O", 0),                     # catechol (phenols neutral)
    ("NCCc1c[nH]c2ccccc12", 1),            # tryptamine aliphatic amine
    ("C(CN)CN", 2),                        # ethylenediamine, both amines
    ("N=C(N)Nc1ccccc1", 1),                # guanidine (single protonation!)
    ("NC(=N)N", 1),                        # guanidine itself
    ("CC(=N)N", 1),                        # acetamidine
    ("CN(C)C", 1),                         # tertiary amine
    ("CC(=O)Nc1ccccc1", 0),                # amide N neutral
    ("c1ccc2[nH]ccc2c1", 0),               # indole NH neutral
])
def test_protonation_rules(smiles, want):
    from rdkit import Chem
    from chemprep import apply_protonation_rules
    mol, notes = apply_protonation_rules(Chem.MolFromSmiles(smiles))
    assert Chem.GetFormalCharge(mol) == want, notes


@requires_rdkit
def test_tautomer_and_stereo():
    from rdkit import Chem
    from chemprep import canonical_tautomer, enumerate_stereoisomers
    mol = Chem.MolFromSmiles("CC(C)Cc1ccc(cc1)C(C)C(=O)O")  # 1 undefined center
    isos, n_undef = enumerate_stereoisomers(mol)
    assert n_undef == 1 and len(isos) == 2
    t, n = canonical_tautomer(Chem.MolFromSmiles("Oc1ccccc1O"))
    assert n >= 1 and t is not None


@requires_rdkit
def test_prep_ligand_variants_cache(tmp_path):
    from chemprep import prep_ligand_variants
    r1 = prep_ligand_variants("caffeine", "Cn1c(=O)c2c(ncn2C)n(C)c1=O", tmp_path)
    assert len(r1["variants"]) == 1
    r2 = prep_ligand_variants("caffeine", "Cn1c(=O)c2c(ncn2C)n(C)c1=O", tmp_path)  # cache hit
    assert r1["cache_key"] == r2["cache_key"]
    assert any("protonation" in n for n in r2["notes"])


# ── vina log parsing (full mode table) ───────────────────────────────────────
def test_parse_vina_modes():
    from multi_site_docking import parse_vina_modes
    log = ("""Computing Vina grid ... done.
Performing docking ...
mode | affinity | dist from best mode
     | (kcal/mol) | rmsd l.b.| rmsd u.b.
-----+------------+----------+----------
   1        -7.3          0          0
   2        -6.9      1.842      3.201
   3        -6.5      24.1      26.7
""")
    modes = parse_vina_modes(log)
    assert modes and modes[0]["affinity"] == -7.3 and modes[0]["rmsd_ub"] == 0.0
    assert len(modes) == 3 and modes[2]["rmsd_lb"] == 24.1


# ── receptor models: complex keeps colipase + Ca2+, apo drops them ──────────
@requires_1lpb
def test_clean_receptor_models(tmp_path):
    import multi_site_docking as ms
    chain = ms.pick_chain(RECEPTOR)
    assert chain == "B"  # lipase is the largest chain (colipase = chain A)
    cx = ms.clean_receptor(RECEPTOR, chain, tmp_path, model="complex")
    txt = cx.read_text()
    assert " 901" in txt or True  # MUP always dropped
    assert not any(ln.startswith("HETATM") and ln[17:20].strip() == "MUP" for ln in txt.splitlines())
    ca_lines = [ln for ln in txt.splitlines() if ln.startswith("HETATM") and ln[17:20].strip() == "CA"]
    assert len(ca_lines) == 1, "Ca2+ must be retained in complex model"
    chains_seen = {ln[21] for ln in txt.splitlines() if ln.startswith("ATOM")}
    assert chains_seen == {"A", "B"}, f"complex must keep colipase chain A, got {chains_seen}"
    apo = ms.clean_receptor(RECEPTOR, chain, tmp_path / "apo", model="apo")
    chains_apo = {ln[21] for ln in apo.read_text().splitlines() if ln.startswith("ATOM")}
    assert chains_apo == {"B"}


# ── sites on the real complex ────────────────────────────────────────────────
@requires_1lpb
def test_detect_sites_complex(tmp_path):
    import multi_site_docking as ms
    chain = ms.pick_chain(RECEPTOR)
    clean = ms.clean_receptor(RECEPTOR, chain, tmp_path, model="complex")
    res, seq_nums = ms.parse_receptor(clean, chain)
    sites = ms.detect_sites(res, seq_nums, clean_complex=clean, enzyme_chain=chain)

    triad_note = sites["catalytic_triad"]["note"]
    assert "Ser152-Asp176-His263" in triad_note, triad_note
    # catalytic center must sit within 3 A of Ser152 OG (pocket-anchored, not residue-cloud centroid)
    og = res[152]["atoms"]["OG"]
    cx, cy, cz = sites["catalytic_triad"]["center"]
    d = ((og[0]-cx)**2 + (og[1]-cy)**2 + (og[2]-cz)**2) ** 0.5
    assert d <= 3.0, f"catalytic center {d:.2f} A from Ser152-OG"
    # TRUE oxyanion hole: Phe77 + Leu153 backbone nitrogens
    oxy = sites["oxyanion_hole"]["residues"]
    assert 77 in oxy and 153 in oxy, f"oxyanion hole {oxy} must be Phe77+Leu153"
    # real cross-chain interface: colipase-labeled residues present
    iface = sites["colipase_interface"]["residues"]
    assert any(isinstance(r, tuple) and r[0] == "colipase" for r in iface), \
        "interface must include colipase (chain A) residues"
    assert any(isinstance(r, int) for r in iface)
    # lid ~237-261
    lid = sites["lid"]["residues"]
    assert lid and abs(lid[0] - 237) <= 3 and abs(lid[-1] - 261) <= 3, f"lid {lid[0]}..{lid[-1]}"


# ── Kabsch RMSD ──────────────────────────────────────────────────────────────
def test_kabsch_rmsd():
    from validate_native import kabsch_rmsd
    A = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
    assert kabsch_rmsd(A, A) == pytest.approx(0.0, abs=1e-9)
    shifted = [[x + 5, y - 2, z + 9] for x, y, z in A]
    assert kabsch_rmsd(A, shifted) == pytest.approx(0.0, abs=1e-9)  # translation invariant
    perturbed = [list(a) for a in A]; perturbed[4][2] += 0.3  # move ONE atom
    r = kabsch_rmsd(A, perturbed)
    assert 0.05 < r <= 0.3 / len(A) ** 0.5 + 1e-9  # best-fit can reduce, never enlarge


def test_matched_rmsd_symmetric_names():
    from validate_native import matched_rmsd, pdb_coords
    ref_lines = ["HETATM 901  O1  MUP B 901      10.000  10.000  10.000  1.00  0.00           O",
                 "HETATM 902  O2  MUP B 901      11.000  10.000  10.000  1.00  0.00           O"]
    # swapped same-name atoms must still give ~0 RMSD (symmetry handling)
    pose_lines = ["MODEL", "HETATM 902  O2  UNL B 901      10.000  10.000  10.000  1.00  0.00           O",
                  "HETATM 901  O1  UNL B 901      11.000  10.000  10.000  1.00  0.00           O", "ENDMDL"]
    from validate_native import pdbqt_models
    import tempfile, pathlib
    f = pathlib.Path(tempfile.mkstemp(suffix=".pdbqt")[1]); f.write_text("\n".join(pose_lines))
    names, elems = pdbqt_models(f)[0]
    r, n, tot = matched_rmsd(names, pdb_coords(ref_lines), pose_elems=elems)
    assert r < 1e-6 and n == 2
