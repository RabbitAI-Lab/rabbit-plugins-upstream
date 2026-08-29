"""Sync maintenance tasks: staleness management (spec §5.2)."""
from __future__ import annotations

from datetime import datetime, timedelta

from celery import shared_task
from sqlalchemy import select

from src.config import get_config
from src.database.models import Supplier
from src.database.session import get_db_session


@shared_task
def staleness_sweep():
    """Force a full re-mirror for suppliers unchanged for 30 days; flag
    suppliers unreachable for 7 days as 'unverified'."""
    cfg = get_config()
    db = get_db_session()
    try:
        now = datetime.now()
        full_remirror_after = timedelta(days=cfg.sync.force_full_remirror_after_days)
        unreachable_after = timedelta(days=cfg.sync.alert_unreachable_after_days)

        suppliers = db.execute(select(Supplier).where(Supplier.status == "active")).scalars().all()
        forced, flagged = 0, 0
        for s in suppliers:
            last = s.httrack_last_update or s.last_crawled
            if last is None:
                continue
            age = now - last
            if age >= full_remirror_after:
                from src.tasks.crawl_tasks import mirror_and_extract_supplier
                mirror_and_extract_supplier.delay(s.supplier_id)
                forced += 1
            elif age >= unreachable_after:
                s.status = "unverified"
                flagged += 1
        db.commit()
        return {"forced_remirror": forced, "flagged_unverified": flagged}
    finally:
        db.close()
