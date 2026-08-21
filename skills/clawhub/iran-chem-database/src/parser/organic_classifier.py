"""Explicit organic-molecule classification (fix guide §8).

Never rely on informal name-based guesses. Priority:
  1. structure (RDKit from SMILES/InChI/InChIKey) — authoritative;
  2. CAS resolution through an approved data source (PubChem);
  3. name resolution through PubChem;
  4. otherwise mark `organic_status = unknown` (never silently excluded).

Output fields (stored on Molecule):
  organic_status    : true | false | unknown
  organic_reason    : structure | cas_resolution | name_resolution | manual
  organic_confidence: 0.0–1.0
"""
from __future__ import annotations

import re
from typing import Optional, Tuple

# Carbon-bearing INORGANIC compounds are NOT organic even though they contain
# carbon atoms: oxides, carbonates/bicarbonates, cyanides/thiocyanates/cyanates,
# carbides, carbonyl complexes, CO/CO2/CS2/HCN, and elemental carbon forms.
INORGANIC_FORMULA_PATTERN = re.compile(
    r"^(C|CO|CO2|CS2|COS|HCN|H2CO3|HCNO|HNCO|CN|OCN|SCN|C2N2|"
    r"NaCN|KCN|NaSCN|KSCN|NH4SCN|NaHCO3|KHCO3|NH4HCO3|Na2CO3|K2CO3|"
    r"CaCO3|MgCO3|NH4CN)$",
    re.I,
)
INORGANIC_FRAGMENT_PATTERN = re.compile(r"(CO3|HCO3|CN|SCN|OCN|NCO|C2N2)", re.I)

# Carbon is organic ONLY when it is a carbon ATOM, not part of element symbols
# (Ca, Cs, Cd, Ce, Cl, Cu, Cr, Co, Cm, Cf) or two-letter fragments above.
_NON_CARBON_ELEMENTS = {"Ca", "Cs", "Cd", "Ce", "Cl", "Cu", "Cr", "Co", "Cm", "Cf", "Cn"}


def formula_has_carbon_atom(formula: Optional[str]) -> bool:
    """True when `formula` contains at least one carbon ATOM (element tokenization)."""
    if not formula:
        return False
    f = str(formula).replace(" ", "").replace("\u200c", "")
    tokens = re.findall(r"[A-Z][a-z]?", f)
    for tok in tokens:
        if tok == "C":
            return True
    return False


def _from_formula(formula: str) -> Tuple[bool, str, float]:
    f = str(formula).replace(" ", "").replace("\u200c", "")
    if INORGANIC_FORMULA_PATTERN.match(f) or INORGANIC_FRAGMENT_PATTERN.search(f):
        return False, "structure", 0.98
    if formula_has_carbon_atom(f):
        return True, "structure", 0.98
    return False, "structure", 0.98


def _from_rdkit(smiles: Optional[str] = None, inchi: Optional[str] = None) -> Optional[Tuple[bool, str, float]]:
    try:
        from rdkit import Chem
    except ImportError:
        return None
    mol = None
    try:
        if smiles:
            mol = Chem.MolFromSmiles(str(smiles))
        if mol is None and inchi:
            mol = Chem.MolFromInchi(str(inchi))
    except Exception:  # noqa: BLE001
        return None
    if mol is None:
        return None
    # count carbon atoms in the molecule
    n_carbon = sum(1 for a in mol.GetAtoms() if a.GetAtomicNum() == 6)
    n_total = mol.GetNumAtoms()
    if n_carbon == 0:
        return False, "structure", 0.99
    # edge case: only carbon (elemental carbon is inorganic in catalogue terms)
    if n_carbon == n_total:
        return False, "structure", 0.9
    return True, "structure", 0.99


import time as _time

_lookup_cache: dict = {}
_LOOKUP_ERRORS: dict = {}


def _cached(key: str, fn):
    if key in _lookup_cache:
        return _lookup_cache[key]
    value, err = fn()
    if err:
        _LOOKUP_ERRORS[key] = err
    else:
        _lookup_cache[key] = value
    return value


def _lookup_with_retry(fn, retries: int = 3, backoff: float = 1.5, rate_pause: float = 0.25):
    """Retry/backoff + a small inter-call pause to be polite to PubChem."""
    err: str | None = None
    for attempt in range(retries):
        try:
            _time.sleep(rate_pause)
            result = fn()
            if result is not None:
                return result, None
            if attempt < retries - 1:
                _time.sleep(backoff * (attempt + 1))
        except Exception as exc:  # noqa: BLE001
            err = f"{type(exc).__name__}:{str(exc)[:120]}"
            if attempt < retries - 1:
                _time.sleep(backoff * (attempt + 1))
    return None, err


def _cas_lookup(cas: str) -> Optional[Tuple[bool, str, float]]:
    """Resolve a valid CAS number via PubChem and classify from the structure."""
    try:
        import pubchempy as pcp
    except ImportError:
        return None

    def attempt():
        try:
            compounds = pcp.get_compounds(cas, "name")
            if not compounds:
                return None
            c = compounds[0]
            formula = getattr(c, "molecular_formula", None)
            smiles = getattr(c, "connectivity_smiles", None) or getattr(c, "canonical_smiles", None)
            inchi = getattr(c, "inchi", None)
            struct = _from_rdkit(smiles, inchi)
            if struct is not None:
                return (struct[0], "cas_resolution", min(struct[2], 0.9))
            if formula:
                ok, _reason, conf = _from_formula(formula)
                return (ok, "cas_resolution", min(conf, 0.9))
            return None
        except Exception:  # noqa: BLE001
            raise
    return _cached(f"cas:{cas}", lambda: _lookup_with_retry(attempt))


def _name_lookup(name: str) -> Optional[Tuple[bool, str, float]]:
    try:
        import pubchempy as pcp
    except ImportError:
        return None

    def attempt():
        try:
            compounds = pcp.get_compounds(str(name), "name")
            if not compounds:
                return None
            c = compounds[0]
            formula = getattr(c, "molecular_formula", None)
            smiles = getattr(c, "connectivity_smiles", None) or getattr(c, "canonical_smiles", None)
            inchi = getattr(c, "inchi", None)
            struct = _from_rdkit(smiles, inchi)
            if struct is not None:
                return (struct[0], "name_resolution", min(struct[2], 0.7))
            if formula:
                ok, _reason, conf = _from_formula(formula)
                return (ok, "name_resolution", min(conf, 0.7))
            return None
        except Exception:  # noqa: BLE001
            raise
    return _cached(f"name:{str(name)[:120]}", lambda: _lookup_with_retry(attempt))


class OrganicClassifier:
    """Classifies catalogue records as organic / inorganic / unknown."""

    def __init__(self, network: bool = True):
        self.network = network

    def classify(self, record: dict) -> Tuple[str, Optional[str], Optional[float]]:
        """Return (organic_status, organic_reason, organic_confidence)."""
        return self.classify_detailed(record)[:3]

    def classify_detailed(self, record: dict) -> Tuple[str, Optional[str], Optional[float], Optional[str]]:
        """Return (status, reason, confidence, lookup_error).

        Lookup failures are reported distinctly (remediation §6): a record
        that could not be resolved because PubChem was unreachable is not
        treated the same as a record with no resolvable identity.
        """
        formula = record.get("molecular_formula")
        smiles = record.get("canonical_smiles") or record.get("smiles")
        inchi = record.get("inchi")
        cas = str(record.get("cas_number") or "").strip()
        name = record.get("iupac_name") or record.get("common_name") or record.get("name") or record.get("title")

        # 1) Structure first
        if smiles or inchi:
            r = _from_rdkit(smiles, inchi)
            if r is not None:
                return ("true" if r[0] else "false"), r[1], r[2], None
        if formula:
            ok, reason, conf = _from_formula(formula)
            return ("true" if ok else "false"), reason, conf, None

        # 2) CAS resolution
        if self.network and cas:
            key = f"cas:{cas}"
            r = _cas_lookup(cas)
            if r is not None:
                return ("true" if r[0] else "false"), r[1], r[2], None
            if key in _LOOKUP_ERRORS:
                return "unknown", "cas_resolution", None, _LOOKUP_ERRORS[key]

        # 3) Name resolution
        if self.network and name:
            key = f"name:{str(name)[:120]}"
            r = _name_lookup(str(name))
            if r is not None:
                return ("true" if r[0] else "false"), r[1], r[2], None
            if key in _LOOKUP_ERRORS:
                return "unknown", "name_resolution", None, _LOOKUP_ERRORS[key]

        # 4) Unknown — never guess, never silently exclude
        return "unknown", None, None, None

    @staticmethod
    def clear_cache() -> None:
        _lookup_cache.clear()
        _LOOKUP_ERRORS.clear()
