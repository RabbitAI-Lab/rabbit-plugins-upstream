"""Chemical validation pipeline: RDKit + PubChem cross-reference (spec §4.5)."""
from __future__ import annotations

import hashlib
from typing import Optional

from src.utils.chemistry_utils import (
    canonicalize_smiles,
    is_valid_cas,
    name_to_compound,
    smiles_to_formula,
    smiles_to_inchikey,
    smiles_to_mw,
)


class ChemicalValidator:
    """Validates and enriches a molecule record; garbage must not enter the DB."""

    def validate(self, record: dict) -> Optional[dict]:
        """Return an enriched record dict, or None if the record is unusable."""
        out = dict(record)
        problems = []

        # 1) CAS checksum
        cas = record.get("cas_number")
        if cas and not is_valid_cas(str(cas)):
            problems.append("invalid-cas")
            cas = None

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

        # 3) Name resolution via PubChem if we have neither SMILES nor CAS
        if not (out.get("canonical_smiles") or cas or out.get("inchi_key")):
            name = record.get("iupac_name") or record.get("common_name") or record.get("name")
            if name:
                resolved = name_to_compound(str(name))
                if resolved:
                    for k in ("pubchem_cid", "canonical_smiles", "inchi", "inchi_key",
                              "molecular_formula", "molecular_weight"):
                        if resolved.get(k) and not out.get(k):
                            out[k] = resolved[k]

        # 4) A record with NO identifiable chemistry is garbage
        if not any(out.get(k) for k in ("cas_number", "canonical_smiles", "inchi_key", "inchi")):
            return None

        out["_validation_problems"] = problems
        out["_validation_status"] = "ok" if not problems else "warning"
        return out

    @staticmethod
    def raw_hash(text: str) -> str:
        return hashlib.sha256(text.encode("utf-8", errors="replace")).hexdigest()
