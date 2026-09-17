"""Export endpoint — CSV / JSON / SDF + JSON manifest (remediation §3/§4/§5/§6).

  * `/api/v1/export?format=csv&shape=offerings` — one row per supplier
    offering (default), NOT page-limited;
  * `/api/v1/export?format=csv&shape=molecules` — one row per unique
    molecule (deduplicated by source identity) with supplier list/count;
  * `organic_status=true|false|unknown|all` — server-side organic filter;
    `true` is labeled **confirmed organic** everywhere, never "all organic";
  * `require_complete_coverage=true` — HTTP 409 until every configured
    supplier has a terminal crawl state (remediation §3/§4);
  * `format=manifest` — machine-readable JSON manifest for the CSV that
    would be produced with the same parameters, including SHA-256, row
    counts, coverage snapshot, version and scope statement.

Fallback identities are exposed via `source_identity` and are NEVER labeled
as InChIKeys; `inchi_key` only ever holds a real 27-character InChIKey.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json as _json
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse, Response
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.coverage_logic import coverage_snapshot
from src.database.models import Molecule, Supplier, SupplierOffering
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1/export", tags=["export"])

OFFERING_COLUMNS = [
    "source_identity", "inchi_key", "iupac_name", "cas_number", "molecular_formula",
    "molecular_weight", "canonical_smiles", "pubchem_cid",
    "organic_status", "organic_reason", "organic_confidence",
    "classification_review_required",
    "supplier", "supplier_product_code", "brand", "grade", "purity", "price_min",
    "currency", "availability_status", "is_currently_available", "product_url",
]
MOLECULE_COLUMNS = [
    "source_identity", "inchi_key", "iupac_name", "cas_number", "molecular_formula",
    "molecular_weight", "canonical_smiles", "inchi", "pubchem_cid",
    "organic_status", "organic_reason", "organic_confidence",
    "classification_review_required",
    "n_suppliers", "suppliers",
]

APP_VERSION = "2.9.0"


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


def _collect(db: Session, shape: str, organic_status: str | None,
             available: bool | None):
    stmt = select(Molecule)
    if organic_status and organic_status != "all":
        stmt = stmt.where(Molecule.organic_status == organic_status)
    molecules = db.execute(stmt).scalars().all()
    offerings = db.execute(select(SupplierOffering)).scalars().all()
    if available is not None:
        offerings = [o for o in offerings if o.is_currently_available == available]
    suppliers = {s.supplier_id: s for s in db.execute(select(Supplier)).scalars().all()}
    return molecules, offerings, suppliers


def _meta(db: Session, shape: str, organic_status: str | None,
          available: bool | None, row_count: int, csv_sha256: str | None) -> dict:
    cov = coverage_snapshot(db)
    return {
        "export_timestamp": datetime.now(timezone.utc).isoformat(),
        "application": "iran-chem-database",
        "version": APP_VERSION,
        "filters": {"organic_status": organic_status or "all", "available": available},
        "shape": shape,
        "row_count": row_count,
        "csv_sha256": csv_sha256,
        "coverage": cov,
        "scope": ("Dated, auditable, best-effort index of confirmed and unresolved "
                  "chemical offerings discovered in configured public Iranian supplier "
                  "catalogues. Not a claim of national market availability; supplier "
                  "websites are incomplete, change frequently, and some catalogues are "
                  "not publicly machine-readable. organic_status=true means CONFIRMED "
                  "ORGANIC — unresolved entries are reported as unknown, never silently "
                  "discarded."),
    }


def _build_csv(db: Session, shape: str, organic_status: str | None,
               available: bool | None) -> tuple[str, int, dict]:
    molecules, offerings, suppliers = _collect(db, shape, organic_status, available)
    mols_by_id = {m.molecule_id: m for m in molecules}

    if shape == "molecules":
        off_by_mol: dict[int, list] = {}
        for o in offerings:
            off_by_mol.setdefault(o.molecule_id, []).append(o)
        rows = []
        for m in molecules:
            offs = off_by_mol.get(m.molecule_id, [])
            sup_names = sorted({suppliers[o.supplier_id].company_name_en or suppliers[o.supplier_id].website_url
                                for o in offs if o.supplier_id in suppliers})
            rows.append([
                m.source_identity, m.inchi_key or "", m.iupac_name or "", m.cas_number or "",
                m.molecular_formula or "", m.molecular_weight or "", m.canonical_smiles or "",
                m.inchi or "", m.pubchem_cid or "",
                m.organic_status, m.organic_reason or "", m.organic_confidence or "",
                m.classification_review_required,
                len(offs), "; ".join(sup_names),
            ])
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(MOLECULE_COLUMNS)
        w.writerows(rows)
        return buf.getvalue(), len(rows), mols_by_id

    rows = []
    for o in offerings:
        m = mols_by_id.get(o.molecule_id)
        sup = suppliers.get(o.supplier_id)
        if m is None:
            continue
        rows.append([
            m.source_identity, m.inchi_key or "", m.iupac_name or "", m.cas_number or "",
            m.molecular_formula or "", m.molecular_weight or "", m.canonical_smiles or "",
            m.pubchem_cid or "", m.organic_status, m.organic_reason or "", m.organic_confidence or "",
            m.classification_review_required,
            sup.company_name_en or sup.website_url if sup else "", o.supplier_product_code or "",
            o.brand or "", o.grade or "", o.purity or "", o.price_min or "",
            o.currency or "", o.availability_status or "", o.is_currently_available, o.product_url or "",
        ])
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(OFFERING_COLUMNS)
    w.writerows(rows)
    return buf.getvalue(), len(rows), mols_by_id


@router.get("")
def export(format: str = "csv", shape: str = "offerings",
           organic_status: str | None = None, available: bool | None = None,
           require_complete_coverage: bool = False,
           db: Session = Depends(get_db)):
    if format == "manifest":
        csv_body, row_count, _ = _build_csv(db, shape, organic_status, available)
        sha = hashlib.sha256(csv_body.encode("utf-8")).hexdigest()
        return JSONResponse(_meta(db, shape, organic_status, available, row_count, sha))

    if shape not in ("offerings", "molecules"):
        raise HTTPException(status_code=422, detail="shape must be 'offerings' or 'molecules'")
    if organic_status and organic_status not in ("true", "false", "unknown", "all"):
        raise HTTPException(status_code=422, detail="organic_status must be true|false|unknown|all")

    # Coverage gate (remediation §3/§4)
    if require_complete_coverage:
        cov = coverage_snapshot(db)
        if not cov["export_readiness"]["ready_for_complete_configured_supplier_export"]:
            raise HTTPException(
                status_code=409,
                detail={"error": "configured supplier crawl is not complete",
                        "blocking_reasons": cov["export_readiness"]["blocking_reasons"],
                        "hint": "Omit require_complete_coverage to export anyway "
                                "(warnings included in metadata), or wait for /api/v1/coverage."})

    csv_body, row_count, _ = _build_csv(db, shape, organic_status, available)
    sha = hashlib.sha256(csv_body.encode("utf-8")).hexdigest()
    meta = _meta(db, shape, organic_status, available, row_count, sha)

    if format == "csv":
        header_line = f"# export_metadata: {_json.dumps(meta, default=str)}\r\n"
        return Response(header_line + csv_body, media_type="text/csv",
                        headers={"Content-Disposition":
                                 f"attachment; filename=iran_chem_{shape}_{organic_status or 'all'}.csv"})
    if format == "sdf":
        molecules, _, _ = _collect(db, shape, organic_status, available)
        blocks = []
        for m in molecules:
            if m.canonical_smiles:
                try:
                    from rdkit import Chem
                    mol = Chem.MolFromSmiles(m.canonical_smiles)
                    if mol:
                        mol.SetProp("_Name", m.iupac_name or m.source_identity)
                        mol.SetProp("CAS", m.cas_number or "")
                        blocks.append(Chem.MolToMolBlock(mol))
                except Exception:  # noqa: BLE001
                    continue
        return Response("\n".join(blocks) + "\n", media_type="chemical/x-mdl-sdfile")

    # JSON (default)
    import csv as _csv
    reader = _csv.DictReader(io.StringIO(csv_body))
    return {"metadata": meta, shape: list(reader)}
