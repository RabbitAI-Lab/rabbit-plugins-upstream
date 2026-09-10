"""Coverage endpoint (remediation §4).

Status comes from the LATEST persisted run per supplier; queued/running counts
are real. A partial crawl followed by a successful one reports success.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.api.coverage_logic import coverage_snapshot
from src.database.session import get_db_session

router = APIRouter(prefix="/api/v1", tags=["coverage"])


def get_db() -> Session:
    db = get_db_session()
    try:
        yield db
    finally:
        db.close()


@router.get("/coverage")
def coverage(db: Session = Depends(get_db)):
    return coverage_snapshot(db)


@router.get("/jobs")
def jobs(db: Session = Depends(get_db)):
    """Recent persisted crawl-run states (remediation §2)."""
    from sqlalchemy import desc, select
    from src.database.models import CrawlRunState
    rows = db.execute(
        select(CrawlRunState).order_by(desc(CrawlRunState.run_id)).limit(100)
    ).scalars().all()
    return {"jobs": [
        {"run_id": r.run_id, "supplier_id": r.supplier_id, "task_id": r.task_id,
         "state": r.state, "reason": r.reason,
         "queued_at": r.queued_at.isoformat() if r.queued_at else None,
         "started_at": r.started_at.isoformat() if r.started_at else None,
         "finished_at": r.finished_at.isoformat() if r.finished_at else None}
        for r in rows
    ]}
