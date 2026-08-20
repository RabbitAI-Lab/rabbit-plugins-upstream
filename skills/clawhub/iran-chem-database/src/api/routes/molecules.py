"""Molecule endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.schemas import MoleculeOut, OfferingOut
from src.database.models import Molecule, Supplier, SupplierOffering
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
        molecule_id=molecule.molecule_id, inchi_key=molecule.inchi_key,
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
    available: bool | None = None, page: int = Query(1, ge=1), limit: int = Query(20, le=100),
):
    rows, total = search_molecules(db, query or None, cas or None, formula or None,
                                   grade or None, supplier_id, min_purity, available, page, limit)
    return {"total": total, "page": page, "molecules": [_to_out(m) for m in rows]}


@router.get("/{inchi_key}")
def get_molecule(inchi_key: str, db: Session = Depends(get_db)):
    molecule = db.execute(
        select(Molecule).where(Molecule.inchi_key == inchi_key)
    ).scalar_one_or_none()
    if molecule is None:
        raise HTTPException(status_code=404, detail="Molecule not found")
    return _to_out(molecule)
