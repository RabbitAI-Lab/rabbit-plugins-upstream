"""Chemical validation pipeline: RDKit + PubChem cross-reference (spec §4.5).

v2.4.0 fixes:
  * validated CAS is WRITTEN BACK to the record (invalid CAS values were
    previously persisted to the database verbatim);
  * CAS-only records can be resolved to structure (SMILES/InChIKey/formula/MW)
    through a cached, rate-limited PubChem lookup — closing the identity gap
    where one listing had a structure and another (same chemical) had only a
    CAS, which produced duplicate molecule rows in exports.
"""
from __future__ import annotations

import hashlib
import time
from typing import Optional

from src.database.identity import is_valid_cas, normalize_identity_title
from src.utils.chemistry_utils import (
    canonicalize_smiles,
    name_to_compound,
    smiles_to_formula,
    smiles_to_inchikey,
    smiles_to_mw,
)

_resolution_cache: dict = {}
_resolution_errors: dict = {}


def clear_resolution_cache() -> None:
    _resolution_cache.clear()
    _resolution_errors.clear()


def _resolve_cas_structure(cas: str) -> Optional[dict]:
    """Resolve a CAS number to structure data via PubChem (cached + retried).

    Returns {canonical_smiles, inchi, inchi_key, molecular_formula,
    molecular_weight, pubchem_cid} or None. Lookup failures are recorded
    distinctly so they are not mistaken for 'no such chemical'.
    """
    if cas in _resolution_cache:
        return _resolution_cache[cas]
    try:
        import pubchempy as pcp
    except ImportError:
        return None

    result: Optional[dict] = None
    err: Optional[str] = None
    for attempt in range(3):
        try:
            time.sleep(0.25)
            compounds = pcp.get_compounds(cas, "name")
            if compounds:
                c = compounds[0]
                smiles = (getattr(c, "connectivity_smiles", None)
                          or getattr(c, "canonical_smiles", None))
                result = {
                    "canonical_smiles": smiles,
                    "inchi": getattr(c, "inchi", None),
                    "inchi_key": getattr(c, "inchikey", None),
                    "molecular_formula": getattr(c, "molecular_formula", None),
                    "molecular_weight": float(getattr(c, "molecular_weight", 0) or 0) or None,
                    "pubchem_cid": int(getattr(c, "cid", 0) or 0) or None,
                }
            break
        except Exception as exc:  # noqa: BLE001
            err = f"{type(exc).__name__}:{str(exc)[:120]}"
            time.sleep(1.5 * (attempt + 1))
    if err:
        _resolution_errors[cas] = err
    else:
        _resolution_cache[cas] = result
    return result


def _resolve_cas_enabled() -> bool:
    try:
        from src.config import get_config
        parsing = get_config().as_dict().get("parsing", {}) or {}
        return bool(parsing.get("resolve_cas_structures", True))
    except Exception:  # noqa: BLE001
        return True


class ChemicalValidator:
    """Validates and enriches a molecule record; garbage must not enter the DB."""

    def __init__(self, resolve_cas: bool | None = None):
        self.resolve_cas = _resolve_cas_enabled() if resolve_cas is None else resolve_cas

    def validate(self, record: dict) -> Optional[dict]:
        """Return an enriched record dict, or None if the record is unusable."""
        out = dict(record)
        problems = []

        # 1) CAS checksum — and WRITE BACK the validated value so invalid CAS
        #    strings never reach the database/export.
        cas = record.get("cas_number")
        if cas:
            if is_valid_cas(str(cas)):
                cas = str(cas).strip()
                out["cas_number"] = cas
            else:
                problems.append("invalid-cas")
                cas = None
                out["cas_number"] = None

        # 2) SMILES canonicalization / structure validation
        smiles = record.get("canonical_smiles") or record.get("smiles")
        if smiles:
            canon = canonicalize_smiles(str(smiles))
            if canon is None:
                problems.append("invalid-smiles")
            else:
                out["canonical_smiles"] = canon
                out["inchi_key"] = out.get("inchi_key") or smiles_to_inchikey(canon)
                out["molecular_formula"] = out.get("molecular_formula") or smiles_to_formula(canon)
                out["molecular_weight"] = out.get("molecular_weight") or smiles_to_mw(canon)

        # 3) CAS → structure resolution (dedup hardening): a CAS-only listing
        #    of a chemical that other listings carry WITH a structure should
        #    unify onto the same InChIKey identity instead of a cas: identity.
        if self.resolve_cas and cas and not (
                out.get("canonical_smiles") or out.get("inchi_key") or out.get("inchi")):
            resolved = _resolve_cas_structure(cas)
            if resolved:
                for k in ("pubchem_cid", "canonical_smiles", "inchi", "inchi_key",
                          "molecular_formula", "molecular_weight"):
                    if resolved.get(k) and not out.get(k):
                        out[k] = resolved[k]
            elif cas in _resolution_errors:
                out["_cas_resolution_error"] = _resolution_errors[cas]

        # 4) Name resolution via PubChem if we have neither SMILES nor CAS.
        #    The query uses the NORMALIZED title (pack sizes/% stripped) so
        #    "Ethanol 96% 1 lit" resolves like "ethanol" and unifies onto the
        #    same structure identity as other listings of the same chemical.
        if not (out.get("canonical_smiles") or cas or out.get("inchi_key")):
            name = record.get("iupac_name") or record.get("common_name") or record.get("name")
            if not name:
                name = record.get("title")
            if name:
                query = normalize_identity_title(str(name)) or str(name)
                resolved = name_to_compound(query)
                if resolved:
                    for k in ("pubchem_cid", "canonical_smiles", "inchi", "inchi_key",
                              "molecular_formula", "molecular_weight"):
                        if resolved.get(k) and not out.get(k):
                            out[k] = resolved[k]
                else:
                    # retry with the raw title (normalization may have stripped
                    # the identifying part of a compound name)
                    resolved = name_to_compound(str(name))
                    if resolved:
                        for k in ("pubchem_cid", "canonical_smiles", "inchi", "inchi_key",
                                  "molecular_formula", "molecular_weight"):
                            if resolved.get(k) and not out.get(k):
                                out[k] = resolved[k]

        # 5) A record with NO identifiable chemistry is garbage
        if not any(out.get(k) for k in ("cas_number", "canonical_smiles", "inchi_key", "inchi")):
            return None

        out["_validation_problems"] = problems
        out["_validation_status"] = "ok" if not problems else "warning"
        return out

    @staticmethod
    def raw_hash(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()
