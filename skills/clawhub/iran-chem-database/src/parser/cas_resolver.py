"""CAS Registry Number validation and resolution (spec §4.5)."""
from __future__ import annotations

import re
from typing import Optional

from src.utils.chemistry_utils import is_valid_cas, name_to_compound

_CAS_RE = re.compile(r"\b\d{2,7}-\d{2}-\d\b")


def extract_cas_numbers(text: str) -> list[str]:
    """Extract all CAS-looking tokens from arbitrary text."""
    return list(dict.fromkeys(_CAS_RE.findall(text or "")))


def resolve_cas(cas: str) -> Optional[dict]:
    """Resolve a CAS number to chemical identifiers via PubChem."""
    if not is_valid_cas(cas):
        return None
    return name_to_compound(cas)


def validate_or_resolve(record: dict) -> Optional[dict]:
    """Given a record with cas/name/smiles, fill in the missing identifiers.

    Priority: valid CAS > SMILES (RDKit) > name (PubChem).
    """
    cas = record.get("cas_number")
    if cas and is_valid_cas(str(cas)):
        resolved = name_to_compound(str(cas))
        if resolved:
            return {**record, **{k: v for k, v in resolved.items() if v}}
    smiles = record.get("canonical_smiles") or record.get("smiles")
    if smiles:
        return record  # handled by chemical_validator
    name = record.get("iupac_name") or record.get("common_name") or record.get("name")
    if name:
        resolved = name_to_compound(str(name))
        if resolved:
            return {**record, **{k: v for k, v in resolved.items() if v}}
    return record
