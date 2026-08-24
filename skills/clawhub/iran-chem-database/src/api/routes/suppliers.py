"""Supplier endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.api.schemas import SupplierOut
from src.database.models import HTTrackMirror, Supplier
from src.database.queries import list_suppliers
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1/suppliers", tags=["suppliers"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


def _to_out(s: Supplier) -> SupplierOut:
    return SupplierOut(
        supplier_id=s.supplier_id, company_name_en=s.company_name_en,
        company_name_fa=s.company_name_fa, website_url=s.website_url,
        supplier_type=s.supplier_type, city=s.city, province=s.province,
        status=s.status, is_verified=s.is_verified,
        verification_score=s.verification_score, total_products=s.total_products,
        last_crawled=s.last_crawled.isoformat() if s.last_crawled else None,
    )


@router.get("")
def suppliers(status: str = "", page: int = Query(1, ge=1), limit: int = Query(50, le=200),
              db: Session = Depends(get_db)):
    rows, total = list_suppliers(db, status or None, page, limit)
    return {"total": total, "suppliers": [_to_out(s) for s in rows]}


@router.get("/{supplier_id}")
def supplier_detail(supplier_id: int, db: Session = Depends(get_db)):
    s = db.get(Supplier, supplier_id)
    if s is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return _to_out(s)


@router.get("/{supplier_id}/mirror-status")
def supplier_mirror_status(supplier_id: int, db: Session = Depends(get_db)):
    mirror = db.execute(
        select(HTTrackMirror).where(HTTrackMirror.supplier_id == supplier_id)
    ).scalar_one_or_none()
    if mirror is None:
        return {"supplier_id": supplier_id, "mirror": None}
    return {
        "supplier_id": supplier_id,
        "mirror": {
            "mirror_id": mirror.mirror_id, "mirror_path": mirror.mirror_path,
            "total_files": mirror.total_files, "html_files": mirror.html_files,
            "pdf_files": mirror.pdf_files, "excel_files": mirror.excel_files,
            "mirror_size_bytes": mirror.mirror_size_bytes,
            "last_update_date": mirror.last_update_date.isoformat() if mirror.last_update_date else None,
            "files_new_last_run": mirror.files_new_last_run,
            "files_modified_last_run": mirror.files_modified_last_run,
            "files_removed_last_run": mirror.files_removed_last_run,
            "httrack_return_code": mirror.httrack_return_code,
            "uses_playwright_fallback": mirror.uses_playwright_fallback,
        },
    }
