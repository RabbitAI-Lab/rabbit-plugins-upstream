"""Tests for multi-site detection (parse_receptor + detect_sites).

Builds a synthetic PDB with a known catalytic triad at H-bond geometry and
verifies detection; also verifies the false-positive cluster is rejected, and
(towards the end) checks the real 1LPB receptor when available.
"""
import pytest

import multi_site_docking as ms


def atom_line(serial, name, aa, resnum, x, y, z, chain="A"):
    return (f"ATOM  {serial:5d}  {name:<4s}{aa:>3s} {chain}{resnum:4d}    "
            f"{x:8.3f}{y:8.3f}{z:8.3f}  1.00 20.00           {name[0]:>2s}\n")


def build_synthetic_pdb(path, ser_res=100, asp_res=101, his_res=102,
                        og_ne2=3.0, od1_nd1=3.0, n_res=300):
    """Create a chain of n_res residues (CA only) with a triad at the given geometry.

    Geometry: Ser-OG at (0,0,0); His-NE2 at (og_ne2,0,0); Asp-OD1 at (0,od1_nd1,0)
    and OD2 nearby; His-ND1 at (0,od1_nd1-0.5,0) is not needed — detector uses
    NE2/ND1 of the SAME His: ND1 placed ~2.1A from NE2 (imidazole ring).
    """
    lines = []
    serial = 1
    base_y = 50.0
    ser_x = float(ser_res) * 3.0
    for r in range(1, n_res + 1):
        aa = "GLY"
        # triad residues share the Ser backbone x so side-chain geometry is the
        # only thing the detector sees (avoids the 3A/residue chain spacing)
        x = ser_x if r in (ser_res, asp_res, his_res) else float(r) * 3.0
        y = base_y
        z = 0.0
        if r in (ser_res - 2, ser_res - 1, ser_res + 1, ser_res + 2) and r not in (asp_res, his_res):
            aa = "LEU"  # hydrophobic neighbors so the pocket site is non-empty
        if r == ser_res:
            aa = "SER"
            lines.append(atom_line(serial, "N", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "CA", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "C", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "O", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "CB", aa, r, x, y, z + 1.5)); serial += 1
            lines.append(atom_line(serial, "OG", aa, r, x, y, z + 2.0)); serial += 1
        elif r == asp_res:
            aa = "ASP"
            lines.append(atom_line(serial, "N", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "CA", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "C", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "O", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "CB", aa, r, x, y, z + 1.5)); serial += 1
            lines.append(atom_line(serial, "CG", aa, r, x, y, z + 2.0)); serial += 1
            lines.append(atom_line(serial, "OD1", aa, r, x, y + od1_nd1, z + 2.0)); serial += 1
            lines.append(atom_line(serial, "OD2", aa, r, x, y + od1_nd1 + 1.0, z + 2.0)); serial += 1
        elif r == his_res:
            aa = "HIS"
            lines.append(atom_line(serial, "N", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "CA", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "C", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "O", aa, r, x, y, z)); serial += 1
            lines.append(atom_line(serial, "CB", aa, r, x, y, z + 1.5)); serial += 1
            lines.append(atom_line(serial, "CG", aa, r, x + 1.0, y, z + 2.0)); serial += 1
            lines.append(atom_line(serial, "ND1", aa, r, x + og_ne2 - 2.1, y, z + 2.0)); serial += 1
            lines.append(atom_line(serial, "CD2", aa, r, x + og_ne2 + 1.0, y, z + 2.0)); serial += 1
            lines.append(atom_line(serial, "CE1", aa, r, x + og_ne2 - 1.0, y, z + 2.0)); serial += 1
            lines.append(atom_line(serial, "NE2", aa, r, x + og_ne2, y, z + 2.0)); serial += 1
        else:
            lines.append(atom_line(serial, "CA", aa, r, x, y, z)); serial += 1
    path.write_text("".join(lines))
    return path


def test_detect_sites_finds_true_triad(tmp_path):
    pdb = build_synthetic_pdb(tmp_path / "syn.pdb")
    res, seq = ms.parse_receptor(pdb, "A")
    sites = ms.detect_sites(res, seq)
    triad = sites["catalytic_triad"]["residues"]
    assert triad[0] == 100 and triad[1] == 101 and triad[2] == 102
    # oxyanion: ser+1 and ser+26
    # v100.4: oxyanion hole is geometric (top-2 backbone N near Ser-OG, triad excluded);
    # on the synthetic receptor exact ids depend on geometry — structural truth is
    # covered by test_v1004.test_detect_sites_complex on real 1LPB (Phe77+Leu153).
    oxy = sites["oxyanion_hole"]["residues"]
    assert isinstance(oxy, list) and 1 <= len(oxy) <= 2 and all(isinstance(r, int) for r in oxy)
    # lid window
    assert sites["lid"]["residues"][0] == 187
    # v100.4: renamed colipase_cterm -> colipase_interface (real cross-chain
    # contacts when the complex is provided; falls back to enzyme C-term 45)
    assert len(sites["colipase_interface"]["residues"]) == 45
    # centers are within the box
    for v in sites.values():
        assert len(v["center"]) == 3
        assert isinstance(v["box"], int)


def test_detect_sites_rejects_distant_cluster(tmp_path):
    """A Ser/Asp/His >5A apart must NOT be detected as the triad."""
    pdb = build_synthetic_pdb(tmp_path / "bad.pdb", og_ne2=10.0, od1_nd1=8.0)
    res, seq = ms.parse_receptor(pdb, "A")
    with pytest.raises(SystemExit):
        ms.detect_sites(res, seq)


def test_clean_receptor_drops_waters_and_h(tmp_path):
    src = tmp_path / "raw.pdb"
    lines = [
        atom_line(1, "N", "GLY", 1, 0, 0, 0),
        atom_line(2, "CA", "GLY", 1, 1, 0, 0),
        atom_line(3, "H", "GLY", 1, 0.5, 0, 0),
        "HETATM    4  O   HOH A 500       5.000   5.000   5.000  1.00 20.00           O  \n",
    ]
    src.write_text("".join(lines))
    out = ms.clean_receptor(src, "A", tmp_path)
    text = out.read_text()
    assert "HETATM" not in text
    assert text.count("ATOM") == 2  # H dropped


def test_pick_chain_prefers_largest(tmp_path):
    src = tmp_path / "two.pdb"
    lines = [atom_line(i, "CA", "GLY", i, 0, 0, 0, chain="A") for i in range(1, 11)]
    lines += [atom_line(i + 100, "CA", "GLY", i, 1, 1, 1, chain="B") for i in range(1, 21)]
    src.write_text("".join(lines))
    assert ms.pick_chain(src) == "B"


def test_real_1lpb_detection(real_receptor):
    """The session-validated result: Ser152-Asp176-His263 in chain B."""
    if real_receptor is None:
        pytest.skip("1LPB receptor not available")
    chain = ms.pick_chain(real_receptor)
    assert chain == "B"
    res, seq = ms.parse_receptor(real_receptor, chain)
    sites = ms.detect_sites(res, seq)
    assert sites["catalytic_triad"]["residues"] == [152, 176, 263]
    # centers match the validated grid centers
    expected = {
        "catalytic_triad": [7.477, 27.953, 50.845],
        "oxyanion_hole": [12.581, 27.546, 52.613],
        "hydrophobic_pocket": [6.979, 28.565, 53.367],
    }
    for k, c in expected.items():
        got = sites[k]["center"]
        # v100.4: corrected centers (OG-anchored triad, geometric oxyanion hole)
        assert all(abs(g - e) < 0.05 for g, e in zip(got, c)), f"{k}: {got} != {c}"
