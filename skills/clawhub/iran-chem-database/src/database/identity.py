"""Identity handling for molecule records — replaces the former CAS-only defect.

The old code stored "fallback-<20 hex>" (29 chars) in Molecule.inchi_key,
which PostgreSQL rejected (VARCHAR(27)). More fundamentally, a fallback hash
is not an InChIKey and must never be presented as one.

Identity precedence (fix guide §3.3):
  1. valid InChIKey (structure-derived, 27 chars);
  2. normalized CAS Registry Number;
  3. deterministic supplier key: "supplier:<id>:<product code>";
  4. deterministic fallback hash (exactly 27 chars), stored in
     source_identity only, never exposed as an InChIKey.

Dedup hardening (v2.4.0): fallback keys are computed from a NORMALIZED title
(lowercased, pack-size/percentage tokens and parentheticals stripped) so the
same chemical listed with different pack sizes does not fragment into
multiple molecule rows. Cross-identity unification (CAS/InChIKey merge) is
performed by LiveSyncEngine at upsert time.
"""
from __future__ import annotations

import hashlib
import re
from typing import Optional

_CAS_RE = re.compile(r"^(\d{2,7})-(\d{2})-(\d)$")
_INCHIKEY_RE = re.compile(r"^[A-Z]{14}-[A-Z]{10}-[A-Z]$")

# Pack-size / concentration tokens that describe an OFFERING, not a molecule.
# NOTE: `%` is a non-word character, so `%\b` never matches — percentages get a
# lookahead boundary instead of \b (bug found by the dedup regression test).
_D = "0-9\u0660-\u0669\u06F0-\u06F9"  # ASCII + Persian/Arabic-Indic digits
_PACK_TOKEN_RE = re.compile(
    # percentages (incl. Arabic percent sign ٪) — lookahead boundary,
    # because `%` is a non-word char and `%` never matches
    rf"([{_D}][{_D},.]*\s*(?:%|٪|\u066a)(?![{_D}A-Za-z]))|"
    # pack sizes ("1 lit", "250 gr", "۲/۵ لیتری", "1000 میلی لیتر")
    rf"([{_D}][{_D},./]*\s*(?:kg|gr?|mg|ml|lit|l|cc)\b)|"
    rf"([{_D}][{_D},./]*\s*(?:لیتر|کیلوگرم|کیلو|گرم|میلی\s?لیتر|میلی\s?گرم)[یي]?(?![\u0600-\u06FF]))|"
    # empty parentheses and bracketed annotations
    r"(\(\s*\))|(\[[^\]]*\])",
    re.I,
)


def is_valid_inchikey(value: Optional[str]) -> bool:
    """True when `value` is a plausible real InChIKey (format + checksum-ish shape)."""
    if not value:
        return False
    return bool(_INCHIKEY_RE.match(str(value).strip()))


def is_valid_cas(value: Optional[str]) -> bool:
    """CAS format + checksum validation."""
    if not value:
        return False
    m = _CAS_RE.match(str(value).strip())
    if not m:
        return False
    digits = m.group(1) + m.group(2)
    check = int(m.group(3))
    total = 0
    for i, ch in enumerate(reversed(digits)):
        total += int(ch) * (i + 1)
    return total % 10 == check


def normalize_cas(value: Optional[str]) -> str:
    """Return the cleaned CAS string (whitespace-stripped) when valid, else ''."""
    if not is_valid_cas(value):
        return ""
    return str(value).strip()


def normalize_identity_title(title: Optional[str]) -> str:
    """Normalize a title for the fallback identity basis (dedup hardening).

    Lowercases, strips pack-size/percentage tokens, parentheticals and
    punctuation noise so "Ethanol 96% 1 lit" and "ethanol" share one basis
    while genuinely different chemicals still differ.
    """
    if not title:
        return ""
    t = str(title)
    t = re.sub(r"[\u064a\u0643]", lambda m: {"\u064a": "\u06cc", "\u0643": "\u06a9"}[m.group(0)], t)
    t = _PACK_TOKEN_RE.sub(" ", t)
    t = t.replace("\u200c", " ").replace("\u200f", "").replace("\u200e", "")
    t = re.sub(r"[()\[\]{}<>]", " ", t)
    t = re.sub(r"\s+", " ", t).strip().lower()
    return t


def fallback_identity(basis: str) -> str:
    """Deterministic 27-character identity for records without structure/CAS.

    Exactly 27 chars so it can never overflow the legacy VARCHAR(27) column,
    and prefixed distinctly from any real InChIKey (InChIKeys are uppercase
    letters + digits in a fixed pattern; this prefix starts with lowercase).
    """
    digest = hashlib.sha256(basis.encode("utf-8")).hexdigest()
    return "fallback-" + digest[:18]  # 9 + 18 = 27 characters


def identity_strength(identity: str) -> int:
    """Rank identities: inchikey (4) > cas (3) > supplier+code (2) > fallback (1)."""
    if identity.startswith("inchikey:"):
        return 4
    if identity.startswith("cas:"):
        return 3
    if identity.startswith("sup:"):
        return 2
    return 1


def build_source_identity(record: dict, supplier_id: Optional[int] = None) -> tuple[str, Optional[str]]:
    """Return (source_identity, inchi_key) for a record.

    inchi_key is ONLY ever a real InChIKey; everything else lives in
    source_identity. Both are deterministic across runs.
    """
    inchi_key = record.get("inchi_key") or record.get("inchiKey")
    if is_valid_inchikey(inchi_key):
        ik = str(inchi_key).strip()
        return f"inchikey:{ik}", ik

    cas = normalize_cas(record.get("cas_number"))
    if cas:
        return f"cas:{cas}", None

    supplier_code = record.get("supplier_product_code") or record.get("product_code") or record.get("sku")
    if supplier_code and supplier_id is not None:
        return f"sup:{supplier_id}:{str(supplier_code)[:80]}", None

    basis = (
        str(record.get("cas_number") or "") + "|" +
        normalize_identity_title(record.get("title") or record.get("name") or
                                 record.get("iupac_name") or "") + "|" +
        str(record.get("molecular_formula") or "")
    )
    return fallback_identity(basis), None
