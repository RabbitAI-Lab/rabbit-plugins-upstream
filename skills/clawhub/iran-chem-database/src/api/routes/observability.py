"""Observability endpoints (remediation §9): rejections + reconciliation."""
from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.database.models import (CrawlLog, Molecule, RejectedCatalogueItem,
                                 Supplier, SupplierOffering)
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1", tags=["observability"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@router.get("/rejections")
def rejections(db: Session = Depends(get_db),
               stage: str | None = None, supplier_id: int | None = None,
               limit: int = Query(100, ge=1, le=500)):
    stmt = select(RejectedCatalogueItem)
    if stage:
        stmt = stmt.where(RejectedCatalogueItem.rejection_stage == stage)
    if supplier_id is not None:
        stmt = stmt.where(RejectedCatalogueItem.supplier_id == supplier_id)
    rows = db.execute(stmt.order_by(RejectedCatalogueItem.rejection_id.desc()).limit(limit)).scalars().all()
    return {"total_returned": len(rows), "rejections": [
        {"rejection_id": r.rejection_id, "supplier_id": r.supplier_id,
         "raw_title": r.raw_title, "cas_number": r.cas_number,
         "stage": r.rejection_stage, "reason": r.rejection_reason,
         "rejected_at": r.rejected_at.isoformat() if r.rejected_at else None}
        for r in rows
    ]}


@router.get("/reconciliation")
def reconciliation(db: Session = Depends(get_db)):
    """Per-supplier data-quality funnel (remediation §9)."""
    suppliers = db.execute(select(Supplier)).scalars().all()
    out = []
    for s in suppliers:
        found = db.execute(select(func.count()).select_from(SupplierOffering)
                           .where(SupplierOffering.supplier_id == s.supplier_id)).scalar_one()
        rej_grade = db.execute(select(func.count()).select_from(RejectedCatalogueItem)
                               .where(RejectedCatalogueItem.supplier_id == s.supplier_id,
                                      RejectedCatalogueItem.rejection_stage == "grade")).scalar_one()
        rej_val = db.execute(select(func.count()).select_from(RejectedCatalogueItem)
                             .where(RejectedCatalogueItem.supplier_id == s.supplier_id,
                                    RejectedCatalogueItem.rejection_stage == "validation")).scalar_one()
        rej_sync = db.execute(select(func.count()).select_from(RejectedCatalogueItem)
                              .where(RejectedCatalogueItem.supplier_id == s.supplier_id,
                                     RejectedCatalogueItem.rejection_stage == "database_sync")).scalar_one()
        uniq = db.execute(select(func.count(func.distinct(SupplierOffering.molecule_id)))
                          .where(SupplierOffering.supplier_id == s.supplier_id)).scalar_one()
        unresolved = db.execute(
            select(func.count())
            .select_from(Molecule)
            .join(SupplierOffering, SupplierOffering.molecule_id == Molecule.molecule_id)
            .where(SupplierOffering.supplier_id == s.supplier_id,
                   Molecule.organic_status == "unknown")
        ).scalar_one()
        last_log = db.execute(
            select(CrawlLog).where(CrawlLog.supplier_id == s.supplier_id)
            .order_by(CrawlLog.log_id.desc()).limit(1)
        ).scalar_one_or_none()
        out.append({
            "supplier_id": s.supplier_id,
            "name": s.company_name_en or s.website_url,
            "crawl_profile": s.crawl_profile,
            "last_crawl_status": last_log.status if last_log else None,
            "partial_reason": (last_log.partial_reason if last_log else None) or s.partial_reason,
            "offerings": found,
            "unique_molecules": uniq,
            "rejected_grade": rej_grade,
            "rejected_validation": rej_val,
            "rejected_sync": rej_sync,
            "unresolved_organic": unresolved,
            "last_successful_product_count": s.last_successful_product_count,
            "last_http_status": s.last_http_status,
        })
    return {"suppliers": out}
