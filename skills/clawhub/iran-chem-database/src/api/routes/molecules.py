"""Molecule endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.schemas import MoleculeOut, OfferingOut
from src.database.models import Molecule
from src.database.queries import search_molecules
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1/molecules", tags=["molecules"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


def _to_out(molecule: Molecule) -> MoleculeOut:
    offerings = []
    for o in molecule.offerings:
        offerings.append(OfferingOut(
            offering_id=o.offering_id, supplier_id=o.supplier_id,
            supplier_name=o.supplier.company_name_en if o.supplier else None,
            brand=o.brand, grade=o.grade, purity=o.purity,
            purity_numeric=o.purity_numeric, pack_sizes=o.pack_sizes,
            price_min=o.price_min, price_max=o.price_max, currency=o.currency,
            availability_status=o.availability_status, product_url=o.product_url,
            is_currently_available=o.is_currently_available,
        ))
    return MoleculeOut(
        molecule_id=molecule.molecule_id, source_identity=molecule.source_identity,
        inchi_key=molecule.inchi_key,
        organic_status=molecule.organic_status or "unknown",
        organic_reason=molecule.organic_reason,
        organic_confidence=molecule.organic_confidence,
        iupac_name=molecule.iupac_name, common_names=molecule.common_names,
        persian_names=molecule.persian_names, cas_number=molecule.cas_number,
        molecular_formula=molecule.molecular_formula, molecular_weight=molecule.molecular_weight,
        canonical_smiles=molecule.canonical_smiles, inchi=molecule.inchi,
        pubchem_cid=molecule.pubchem_cid, appearance=molecule.appearance,
        ghs_pictograms=molecule.ghs_pictograms, hazard_statements=molecule.hazard_statements,
        signal_word=molecule.signal_word, offerings=offerings,
    )


@router.get("")
def list_molecules(
    db: Session = Depends(get_db),
    query: str = "", cas: str = "", formula: str = "", grade: str = "",
    supplier_id: int | None = None, min_purity: float | None = None,
    available: bool | None = None,
    organic_status: str | None = Query(None, pattern="^(true|false|unknown|all)$"),
    page: int = Query(1, ge=1), limit: int = Query(100, ge=1, le=100),
):
    """Paginated molecule listing (remediation §3).

    NEVER use this endpoint for a "complete" CSV — use /api/v1/export.
    Pagination metadata (total_pages/has_more/next_page) is returned so
    clients cannot mistake one page for the whole dataset.
    """
    import math
    rows, total = search_molecules(db, query or None, cas or None, formula or None,
                                   grade or None, supplier_id, min_purity, available,
                                   organic_status, page, limit)
    total_pages = math.ceil(total / limit) if total else 0
    return {
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "has_more": page < total_pages,
        "next_page": page + 1 if page < total_pages else None,
        "export_hint": "This endpoint is paginated. Use /api/v1/export for a complete CSV.",
        "molecules": [_to_out(m) for m in rows],
    }


@router.get("/{identity}")
def get_molecule(identity: str, db: Session = Depends(get_db)):
    molecule = db.execute(
        select(Molecule).where(Molecule.inchi_key == identity)
    ).scalar_one_or_none()
    if molecule is None:
        molecule = db.execute(
            select(Molecule).where(Molecule.source_identity == identity)
        ).scalar_one_or_none()
    if molecule is None:
        raise HTTPException(status_code=404, detail="Molecule not found")
    return _to_out(molecule)
