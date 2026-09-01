"""Global statistics + recent updates endpoints."""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy import desc, select
from sqlalchemy.orm import Session

from src.database.models import CrawlLog, OfferingHistory
from src.database.queries import global_stats
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1", tags=["stats"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    return global_stats(db)


@router.get("/updates/recent")
def recent_updates(limit: int = 50, db: Session = Depends(get_db)):
    rows = db.execute(
        select(OfferingHistory).order_by(desc(OfferingHistory.changed_at)).limit(limit)
    ).scalars().all()
    return {"updates": [
        {"change_type": h.change_type, "supplier_id": h.supplier_id,
         "molecule_id": h.molecule_id, "changed_at": h.changed_at.isoformat(),
         "detected_via": h.detected_via}
        for h in rows
    ]}


@router.get("/crawl-logs")
def crawl_logs(limit: int = 50, db: Session = Depends(get_db)):
    rows = db.execute(
        select(CrawlLog).order_by(desc(CrawlLog.crawl_start)).limit(limit)
    ).scalars().all()
    return {"logs": [
        {"supplier_id": c.supplier_id, "crawl_type": c.crawl_type,
         "crawl_start": c.crawl_start.isoformat() if c.crawl_start else None,
         "products_found": c.products_found, "products_new": c.products_new,
         "products_updated": c.products_updated, "products_removed": c.products_removed,
         "status": c.status}
        for c in rows
    ]}
