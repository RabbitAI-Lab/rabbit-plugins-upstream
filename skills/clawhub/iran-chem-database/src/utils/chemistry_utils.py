"""Chemistry helpers: CAS validation, RDKit canonicalization, InChIKey, PubChem."""
from __future__ import annotations

import re
from typing import Optional


def is_valid_cas(cas: str) -> bool:
    """Validate a CAS Registry Number (including checksum).

    Format: up to 7 digits, hyphen, 2 digits, hyphen, 1 check digit.
    Check digit = (sum of digits weighted right-to-left) mod 10.
    """
    if not cas:
        return False
    m = re.fullmatch(r"(\d{2,7})-(\d{2})-(\d)", cas.strip())
    if not m:
        return False
    digits = m.group(1) + m.group(2)
    check = int(m.group(3))
    total = 0
    for i, ch in enumerate(reversed(digits)):
        total += int(ch) * (i + 1)
    return total % 10 == check


def cas_to_inchikey(cas: str) -> Optional[str]:
    """Resolve a CAS number to an InChIKey via PubChem (network call)."""
    try:
        import pubchempy as pcp
        compounds = pcp.get_compounds(cas, "name")
        if compounds:
            return getattr(compounds[0], "inchikey", None)
    except Exception:
        pass
    return None


def name_to_compound(name: str) -> Optional[dict]:
    """Resolve a chemical name/CAS to {cas, smiles, inchi, inchikey, formula, mw} via PubChem."""
    try:
        import pubchempy as pcp
        compounds = pcp.get_compounds(name, "name")
        if not compounds:
            return None
        c = compounds[0]
        return {
            "pubchem_cid": int(getattr(c, "cid", 0) or 0),
            "cas": _find_cas(c),
            "smiles": getattr(c, "connectivity_smiles", None) or getattr(c, "canonical_smiles", None),
            "inchi": getattr(c, "inchi", None),
            "inchi_key": getattr(c, "inchikey", None),
            "formula": getattr(c, "molecular_formula", None),
            "mw": float(getattr(c, "molecular_weight", 0) or 0),
        }
    except Exception:
        return None


def _find_cas(compound) -> Optional[str]:
    try:
        for syn in getattr(compound, "synonyms", []) or []:
            m = re.fullmatch(r"\d{2,7}-\d{2}-\d", str(syn))
            if m:
                return str(syn)
    except Exception:
        pass
    return None


def canonicalize_smiles(smiles: str) -> Optional[str]:
    """Canonicalize a SMILES string with RDKit. Returns None if invalid."""
    try:
        from rdkit import Chem
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        return Chem.MolToSmiles(mol)
    except Exception:
        return None


def smiles_to_inchikey(smiles: str) -> Optional[str]:
    """Generate an InChIKey from SMILES via RDKit."""
    try:
        from rdkit import Chem
        from rdkit.Chem import inchi as rd_inchi
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        inchi = rd_inchi.MolToInchi(mol)
        return rd_inchi.InchiToInchiKey(inchi)
    except Exception:
        return None


def smiles_to_formula(smiles: str) -> Optional[str]:
    """Molecular formula from SMILES via RDKit."""
    try:
        from rdkit import Chem
        from rdkit.Chem import rdMolDescriptors
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        return rdMolDescriptors.CalcMolFormula(mol)
    except Exception:
        return None


def smiles_to_mw(smiles: str) -> Optional[float]:
    """Exact molecular weight from SMILES via RDKit."""
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors
        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            return None
        return Descriptors.ExactMolWt(mol)
    except Exception:
        return None
