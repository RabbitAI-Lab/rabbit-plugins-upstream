"""Seed-baseline database for iran-chem-database (v2.14.0).

The skill ships a real crawl export under ``data/seed_export/``
(408 unique molecules, 2026-08-23, 12 verified Telegram channels +
supplier web catalogs). It is a STARTING POINT, not a claim of
completeness:

  * ``load_seed_rows()``       — parsed rows (organic + inorganic)
  * ``build_index()``          — O(1) lookup by name / CAS / InChIKey / CID
  * ``lookup()``               — case-insensitive name or exact CAS
  * ``diff_against()``         — which freshly-parsed rows are NEW
  * ``preload_pubchem_cache()``— pre-populates the resolver's on-disk
                                 PubChem cache from the seed rows, so
                                 known molecules cost ZERO network calls
                                 on later crawls
  * ``export_sqlite()``        — a real SQLite database file
                                 (``molecules`` + ``molecule_suppliers``
                                 + ``export_manifest`` tables) as the
                                 starting point for the live PostgreSQL
                                 database

Stdlib only. The CSV format is the skill's own export format
(``# export_metadata:`` first line, then header + rows).
"""
from __future__ import annotations

import csv
import json
import os
import re
import sqlite3
import tempfile
from typing import Dict, Iterable, List, Optional, Set

SEED_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "data", "seed_export")

ORGANIC_CSV = os.path.join(SEED_DIR, "iran_organic_molecules.csv")
ORGANIC_EXPANDED_CSV = os.path.join(
    SEED_DIR, "iran_organic_molecules_expanded.csv")
MARKET_VERIFIED_CSV = os.path.join(
    SEED_DIR, "iran_organic_molecules_market_verified.csv")
INORGANIC_CSV = os.path.join(SEED_DIR, "iran_inorganic_excluded.csv")
COVERAGE_JSON = os.path.join(SEED_DIR, "coverage_report.json")

# Current baseline (2026-08-25 / v2.19.0): 1041 CID-unique confirmed-organic
# molecules (previous seed + live Iranian catalogue harvest). Highest
# priority in load_seed_rows(); older baseline files remain for audit/history.
CURRENT_BASELINE_CSV = os.path.join(
    SEED_DIR, "iran_organic_molecules_catalogue_verified_2026-08-25.csv")
CURRENT_INORGANIC_CSV = os.path.join(
    SEED_DIR, "iran_inorganic_excluded_parallel_ai_2026-08-24.csv")
PARALLEL_AI_CSV = os.path.join(
    SEED_DIR, "iran_organic_molecules_parallel_ai_2026-08-24.csv")

CAS_RE = re.compile(r"^\d{2,7}-\d{2}-\d$")

# The v2.15 expanded export uses a richer schema. Map its column names onto
# the canonical internal names; unknown columns pass through untouched.
COLUMN_ALIASES = {
    "molecule_name": "molecule",
    "cas_number": "cas",
    "molecular_formula": "formula",
    "identity_methods": "identity_method",
    "supplier_name": "suppliers",
    "vendors": "suppliers",  # 2026-08-24 parallel-AI export format
}


def _normalise_row(raw: dict) -> dict:
    out = {}
    for k, v in raw.items():
        k2 = COLUMN_ALIASES.get(k, k)
        out[k2] = v
    # supplier lists use "; " (legacy) or " | " (expanded) — unify on "; "
    if "suppliers" in out:
        out["suppliers"] = (out["suppliers"] or "").replace(" | ", "; ")
    return out


def _read_csv(path: str) -> List[dict]:
    """Read a seed CSV (skips the ``# export_metadata:`` line)."""
    if not os.path.exists(path):
        return []
    rows: List[dict] = []
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh)
        first = next(reader, None)
        if first and first[0].startswith("# export_metadata:"):
            pass  # metadata line — consumed
        else:
            # no metadata line: `first` IS the header
            reader = csv.reader([first] + [])  # not used; re-open below
            return _read_csv_plain(path)
        cols = next(reader, None)
        if not cols:
            return []
        for raw in reader:
            if len(raw) < len(cols):
                continue
            rows.append(_normalise_row(dict(zip(cols, raw))))
    return rows


def _read_csv_plain(path: str) -> List[dict]:
    with open(path, encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        return [_normalise_row(dict(r)) for r in reader]


def _row_key(r: dict) -> str:
    """Stable identity for a seed row (InChIKey > CAS > CID > name)."""
    ik = (r.get("inchi_key") or "").strip().upper()
    if ik:
        return f"ik:{ik}"
    cas = (r.get("cas") or "").strip()
    if CAS_RE.match(cas):
        return f"cas:{cas}"
    cid = (r.get("pubchem_cid") or "").strip()
    if cid.isdigit():
        return f"cid:{cid}"
    return f"name:{(r.get('molecule') or '').strip().lower()}"


def _list_field(s) -> List[str]:
    return [t.strip() for t in str(s or "").replace(" | ", "; ").split("; ")
            if t.strip()]


def _norm_supplier(tok: str) -> str:
    """Canonical supplier key: 'Telegram: Foo' == 'telegram:foo'."""
    t = tok.strip().lower()
    return re.sub(r"^telegram:\s*", "telegram:", t)


def _merge_row(base: dict, other: dict) -> dict:
    """Merge duplicate rows for the same molecule: union of suppliers,
    source URLs and NAME VARIANTS, fill-in of missing scalar fields, max
    evidence count. Name variants are preserved (P1.2: names are attributes
    of the CID-canonical identity, never silently dropped)."""
    seen = {_norm_supplier(t) for t in _list_field(base.get("suppliers"))}
    merged_sup = list(_list_field(base.get("suppliers")))
    for t in _list_field(other.get("suppliers")):
        if _norm_supplier(t) not in seen:
            seen.add(_norm_supplier(t))
            merged_sup.append(t)
    if len(merged_sup) > len(_list_field(base.get("suppliers"))):
        base["suppliers"] = "; ".join(merged_sup)
        base["n_suppliers"] = str(len(merged_sup))
    # track same-molecule name variants (F5: "L-Ascorbic Acid" vs "Vitamin C")
    variants = [v.strip() for v in
                str(base.get("name_variants") or "").split("; ") if v.strip()]
    for name in (base.get("molecule"), base.get("common_name"),
                 other.get("molecule"), other.get("common_name")):
        name = (name or "").strip()
        if name and name not in variants:
            variants.append(name)
    base["name_variants"] = "; ".join(variants)
    bu, ou = _list_field(base.get("source_urls")), _list_field(other.get("source_urls"))
    merged_u = list(dict.fromkeys(bu + ou))
    if len(merged_u) > len(bu):
        base["source_urls"] = " | ".join(merged_u)
    for k, v in other.items():
        if k.startswith("_"):
            continue
        if not str(base.get(k) or "").strip() and str(v or "").strip():
            base[k] = v
    try:
        be = int(str(base.get("evidence_record_count") or "1") or "1")
        oe = int(str(other.get("evidence_record_count") or "1") or "1")
        if oe > be:
            base["evidence_record_count"] = str(oe)
    except ValueError:
        pass
    return base


def load_seed_manifest(path: str = ORGANIC_CSV) -> dict:
    """The ``# export_metadata:`` manifest of a seed CSV ({} if absent).

    The line is CSV-quoted (embedded double quotes are doubled), so we
    unquote before parsing.
    """
    try:
        with open(path, encoding="utf-8") as fh:
            first = fh.readline()
    except OSError:
        return {}
    first = first.strip()
    if first.startswith('"') and first.endswith('"'):
        first = first[1:-1]
    prefix = "# export_metadata:"
    if not first.startswith(prefix):
        return {}
    payload = first[len(prefix):].strip().strip('"')
    payload = payload.replace('""', '"')
    try:
        return json.loads(payload)
    except ValueError:
        return {}


def load_seed_rows() -> List[dict]:
    """All seed rows, deduped to one row per molecule.

    Loads (in order): the v2.16 market-verified export (651 rows, every row
    backed by a real crawled listing — the PRIMARY baseline), the v2.15
    expanded export (480 rows, 9 source sets), the v2.14 legacy export
    (334 rows incl. 124 unknown-flagged), and the inorganic exclusion file.
    Rows for the same molecule (same InChIKey/CAS/CID) are merged: supplier
    and source-URL evidence is unioned, name variants preserved, missing
    fields filled in. The first file to admit a molecule wins on conflicting
    scalar fields (market-verified data is the newest and evidence-checked).

    Each row keeps the canonical column names (molecule, common_name, cas,
    pubchem_cid, inchi_key, formula, molecular_weight, canonical_smiles,
    iupac_name, organic_status, identity_method, kind, grade, brand, sku,
    purity_percent, pack_size, availability, price, n_suppliers, suppliers,
    n_source_records, source_urls, date_range, text_evidence) plus — for the
    expanded export — category, research_grade_candidate,
    research_grade_signal, supplier_platform, supplier_country_evidence,
    catalogue_presence, availability_status, source_product_titles,
    evidence_record_count.
    """
    sources = (
        (CURRENT_BASELINE_CSV, "iran_organic_molecules_catalogue_verified_2026-08-25.csv"),
        (PARALLEL_AI_CSV, "iran_organic_molecules_parallel_ai_2026-08-24.csv"),
        (MARKET_VERIFIED_CSV, "iran_organic_molecules_market_verified.csv"),
        (ORGANIC_EXPANDED_CSV, "iran_organic_molecules_expanded.csv"),
        (ORGANIC_CSV, "iran_organic_molecules.csv"),
        (CURRENT_INORGANIC_CSV, "iran_inorganic_excluded_parallel_ai_2026-08-24.csv"),
        (INORGANIC_CSV, "iran_inorganic_excluded.csv"),
    )
    merged: Dict[str, dict] = {}
    order: List[str] = []
    for path, tag in sources:
        for raw in _read_csv(path):
            raw["_seed_file"] = tag
            k = _row_key(raw)
            if k in merged:
                _merge_row(merged[k], raw)
            else:
                merged[k] = raw
                order.append(k)
    return [merged[k] for k in order]


class SeedIndex:
    """O(1) lookup over seed rows by normalised name, CAS, InChIKey, CID."""

    def __init__(self, rows: Optional[Iterable[dict]] = None):
        self.rows: List[dict] = list(rows) if rows is not None else load_seed_rows()
        self.by_name: Dict[str, List[dict]] = {}
        self.by_cas: Dict[str, List[dict]] = {}
        self.by_inchikey: Dict[str, List[dict]] = {}
        self.by_cid: Dict[int, List[dict]] = {}
        for r in self.rows:
            # index every human-facing name variant for search
            for key in (r.get("molecule"), r.get("common_name"),
                        r.get("iupac_name")):
                if key:
                    self.by_name.setdefault(key.strip().lower(), []).append(r)
            cas = (r.get("cas") or "").strip()
            if CAS_RE.match(cas):
                self.by_cas.setdefault(cas, []).append(r)
            ik = (r.get("inchi_key") or "").strip()
            if ik:
                self.by_inchikey.setdefault(ik.upper(), []).append(r)
            cid = (r.get("pubchem_cid") or "").strip()
            if cid.isdigit():
                self.by_cid.setdefault(int(cid), []).append(r)

    # -- lookups -----------------------------------------------------------
    def lookup(self, query: str) -> List[dict]:
        """Exact CAS, exact InChIKey, or (case-insensitive) name match."""
        q = (query or "").strip()
        if not q:
            return []
        if CAS_RE.match(q):
            return list(self.by_cas.get(q, []))
        if re.fullmatch(r"[A-Z0-9\-]+/[A-Z0-9\-]+/[A-Z0-9\-]+", q.upper()):
            return list(self.by_inchikey.get(q.upper(), []))
        return list(self.by_name.get(q.lower(), []))

    def is_known(self, query: str) -> bool:
        return bool(self.lookup(query))

    def stats(self) -> dict:
        return {
            "rows": len(self.rows),
            "unique_names": len(self.by_name),
            "unique_cas": len(self.by_cas),
            "unique_inchikeys": len(self.by_inchikey),
            "unique_cids": len(self.by_cid),
            # legacy files use "organic"; the expanded export uses
            # "confirmed_organic" — both are confirmed-organic buckets
            "organic_rows": sum(
                1 for r in self.rows
                if r.get("organic_status") in ("organic", "confirmed_organic")),
            "unknown_rows": sum(1 for r in self.rows
                                if r.get("organic_status") == "unknown"),
            "inorganic_rows": sum(1 for r in self.rows
                                  if r.get("organic_status") == "inorganic"),
            "expanded_rows": sum(
                1 for r in self.rows
                if r.get("_seed_file") == "iran_organic_molecules_expanded.csv"
                or "iran_organic_molecules_expanded.csv"
                in (r.get("_seed_file") or "")),
        }


def build_index() -> SeedIndex:
    return SeedIndex()


def diff_against(index: Optional[SeedIndex], new_rows: Iterable[dict]) -> List[dict]:
    """Which freshly-parsed rows are NEW (not in the seed baseline).

    A new row counts as known when any of its identifiers (InChIKey, CAS,
    PubChem CID, lowercased canonical name) already exists in the seed.
    """
    idx = index or build_index()
    out = []
    for r in new_rows:
        ik = (r.get("inchi_key") or "").strip().upper()
        cas = (r.get("cas_number") or r.get("cas") or "").strip()
        cid = str(r.get("pubchem_cid") or "").strip()
        name = (r.get("canonical_name") or r.get("molecule")
                or r.get("common_name") or "").strip().lower()
        known = (
            (ik and ik in idx.by_inchikey)
            or (CAS_RE.match(cas) and cas in idx.by_cas)
            or (cid.isdigit() and int(cid) in idx.by_cid)
            or (name and name in idx.by_name)
        )
        if not known:
            out.append(r)
    return out


# -- PubChem cache preloading ----------------------------------------------

def _pubchem_cache_path() -> str:
    """Same location the resolver uses (ICDB_PUBCHEM_CACHE aware)."""
    return os.environ.get(
        "ICDB_PUBCHEM_CACHE",
        os.path.join(tempfile.gettempdir(), "icdb_pubchem_cache.json"))


def preload_pubchem_cache(rows: Optional[Iterable[dict]] = None,
                          path: Optional[str] = None) -> int:
    """Pre-populate the resolver's PubChem cache from the seed rows.

    After this, ``pubchem_lookup("melamine")`` etc. for any seeded molecule
    answers from disk — re-parsing an already-seen corpus costs ZERO
    network calls. Existing cache entries are preserved and merged.
    Returns the number of cache entries present after the merge.
    """
    rows = list(rows) if rows is not None else load_seed_rows()
    cache_path = path or _pubchem_cache_path()
    cache: dict = {}
    try:
        with open(cache_path, encoding="utf-8") as fh:
            cache = json.load(fh)
    except (OSError, ValueError):
        cache = {}
    added = 0
    for r in rows:
        props = {
            "pubchem_cid": (int(r["pubchem_cid"])
                            if (r.get("pubchem_cid") or "").isdigit() else None),
            "molecular_formula": r.get("formula") or None,
            "molecular_weight": (float(r["molecular_weight"])
                                 if (r.get("molecular_weight") or "").replace(".", "").isdigit()
                                 else None),
            "canonical_smiles": r.get("canonical_smiles") or None,
            "inchi_key": r.get("inchi_key") or None,
            "iupac_name": r.get("iupac_name") or None,
        }
        if not props["pubchem_cid"] and not props["inchi_key"]:
            continue
        for name in (r.get("molecule"), r.get("common_name"),
                     r.get("iupac_name")):
            if not name:
                continue
            key = name.strip().lower()
            if re.search(r"[\u0600-\u06FF]", key):
                continue  # resolver never sends Persian to PubChem
            if key in cache:
                continue
            cache[key] = props
            added += 1
    if added:
        try:
            with open(cache_path, "w", encoding="utf-8") as fh:
                json.dump(cache, fh)
        except OSError:
            pass
    return len(cache)


# -- SQLite export (database starting point) --------------------------------

def export_sqlite(out_path: str,
                  rows: Optional[Iterable[dict]] = None) -> str:
    """Write the seed baseline as a SQLite database file.

    identity_key (TEXT UNIQUE) is the stereoisomer-aware merge identity
    (InChIKey > CAS > CID > name); pubchem_cid is the primary scientific index
    (P1.2: names are attributes of the CID-canonical identity).

    Tables:
      molecules(molecule_id, identity_key, molecule, name_variants,
                common_name, cas, pubchem_cid,
                inchi_key, formula, molecular_weight, canonical_smiles,
                iupac_name, organic_status, identity_method, kind, grade,
                brand, sku, purity_percent, pack_size, availability, price,
                n_source_records, source_urls, date_range, text_evidence,
                category, research_grade_candidate, research_grade_signal,
                supplier_platform, supplier_country_evidence,
                catalogue_presence, availability_status,
                source_product_titles, evidence_record_count, seed_file)
      molecule_suppliers(molecule_id, supplier, source_url)
      export_manifest(key, value)

    Intended as the import seed for the live PostgreSQL database (same
    schema shape as ``src/database/`` models).
    """
    rows = list(rows) if rows is not None else load_seed_rows()
    manifest = load_seed_manifest()
    if os.path.exists(out_path):
        os.remove(out_path)
    con = sqlite3.connect(out_path)
    con.execute("""
        CREATE TABLE molecules (
            molecule_id      INTEGER PRIMARY KEY,
            identity_key     TEXT UNIQUE,
            molecule         TEXT NOT NULL,
            name_variants    TEXT,
            common_name      TEXT,
            cas              TEXT,
            pubchem_cid      INTEGER,
            inchi_key        TEXT,
            formula          TEXT,
            molecular_weight REAL,
            canonical_smiles TEXT,
            iupac_name       TEXT,
            organic_status   TEXT,
            identity_method  TEXT,
            kind             TEXT,
            grade            TEXT,
            brand            TEXT,
            sku              TEXT,
            purity_percent   TEXT,
            pack_size        TEXT,
            availability     TEXT,
            price            TEXT,
            n_source_records INTEGER,
            source_urls      TEXT,
            date_range       TEXT,
            text_evidence    TEXT,
            category         TEXT,
            research_grade_candidate TEXT,
            research_grade_signal TEXT,
            supplier_platform TEXT,
            supplier_country_evidence TEXT,
            catalogue_presence TEXT,
            availability_status TEXT,
            source_product_titles TEXT,
            evidence_record_count INTEGER,
            evidence_url       TEXT,
            evidence_text      TEXT,
            source_type        TEXT,
            record_date        TEXT,
            seed_file        TEXT
        )""")
    con.execute("""
        CREATE TABLE molecule_suppliers (
            molecule_id INTEGER REFERENCES molecules(molecule_id),
            supplier    TEXT,
            source_url  TEXT
        )""")
    con.execute("CREATE TABLE export_manifest (key TEXT PRIMARY KEY, value TEXT)")
    for k, v in manifest.items():
        con.execute("INSERT OR REPLACE INTO export_manifest VALUES (?, ?)",
                    (str(k), json.dumps(v, ensure_ascii=False)
                     if isinstance(v, (dict, list)) else str(v)))
    ncols = con.execute(
        "SELECT COUNT(*) FROM pragma_table_info('molecules')").fetchone()[0]
    insert_sql = ("INSERT INTO molecules VALUES ("
                  + ",".join("?" * ncols) + ")")
    mid = 0
    for r in rows:
        mid += 1
        con.execute(
            insert_sql,
            (mid, _row_key(r),
             r.get("molecule", ""), r.get("name_variants") or None,
             r.get("common_name") or None,
             r.get("cas") or None,
             int(r["pubchem_cid"]) if (r.get("pubchem_cid") or "").isdigit() else None,
             r.get("inchi_key") or None, r.get("formula") or None,
             (float(r["molecular_weight"])
              if (r.get("molecular_weight") or "").replace(".", "").isdigit()
              else None),
             r.get("canonical_smiles") or None, r.get("iupac_name") or None,
             r.get("organic_status") or None, r.get("identity_method") or None,
             r.get("kind") or None, r.get("grade") or None, r.get("brand") or None,
             r.get("sku") or None, r.get("purity_percent") or None,
             r.get("pack_size") or None, r.get("availability") or None,
             r.get("price") or None,
             int(r["n_source_records"]) if (r.get("n_source_records") or "").isdigit()
             else None,
             r.get("source_urls") or None, r.get("date_range") or None,
             r.get("text_evidence") or None,
             r.get("category") or None,
             r.get("research_grade_candidate") or None,
             r.get("research_grade_signal") or None,
             r.get("supplier_platform") or None,
             r.get("supplier_country_evidence") or None,
             r.get("catalogue_presence") or None,
             r.get("availability_status") or None,
             r.get("source_product_titles") or None,
             int(r["evidence_record_count"]) if (r.get("evidence_record_count") or "").isdigit()
             else None,
             r.get("evidence_url") or None,
             r.get("evidence_text") or None,
             r.get("source_type") or None,
             r.get("record_date") or None,
             r.get("_seed_file") or None))
        for sup in (r.get("suppliers") or "").split("; "):
            sup = sup.strip()
            if sup:
                con.execute(
                    "INSERT INTO molecule_suppliers VALUES (?,?,?)",
                    (mid, sup, (r.get("source_urls") or "").split(" | ")[0] or None))
    con.execute("CREATE UNIQUE INDEX idx_mol_identity ON molecules(identity_key)")
    con.execute("CREATE INDEX idx_mol_cas ON molecules(cas)")
    con.execute("CREATE INDEX idx_mol_ik ON molecules(inchi_key)")
    con.execute("CREATE INDEX idx_mol_cid ON molecules(pubchem_cid)")
    con.execute("CREATE INDEX idx_mol_name ON molecules(molecule)")
    con.execute("CREATE INDEX idx_mol_common ON molecules(common_name)")
    con.commit()
    con.close()
    return out_path
