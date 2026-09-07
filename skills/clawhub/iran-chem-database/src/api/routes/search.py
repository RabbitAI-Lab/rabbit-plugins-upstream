"""Search endpoints (full-text English + Persian, CAS, SMILES, formula)."""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.queries import search_molecules
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1/molecules/search", tags=["search"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def search(q: str = "", cas: str = "", smiles: str = "", formula: str = "",
           page: int = 1, limit: int = 20, db: Session = Depends(get_db)):
    query = q or None
    if smiles and not query:
        query = smiles
    rows, total = search_molecules(db, query, cas or None, formula or None,
                                   None, None, None, None, page, limit)
    out = []
    for m in rows:
        out.append({
            "inchi_key": m.inchi_key, "iupac_name": m.iupac_name,
            "cas_number": m.cas_number, "molecular_formula": m.molecular_formula,
            "molecular_weight": m.molecular_weight, "canonical_smiles": m.canonical_smiles,
            "offering_count": len(m.offerings),
        })
    return {"total": total, "results": out}
