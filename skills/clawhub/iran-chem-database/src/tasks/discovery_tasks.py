"""Scheduled discovery tasks."""
from __future__ import annotations

from celery import shared_task
from sqlalchemy import select

from src.config import get_config
from src.discovery.engine import SupplierDiscoveryEngine
from src.database.models import Supplier
from src.database.session import get_db_session


@shared_task
def weekly_discovery():
    cfg = get_config()
    engine = SupplierDiscoveryEngine()
    candidates = engine.run_full_discovery()

    db = get_db_session()
    try:
        new_count = 0
        for cand in candidates:
            exists = db.execute(select(Supplier).where(Supplier.website_url == cand.url)).scalar_one_or_none()
            if exists is None:
                db.add(Supplier(
                    company_name_en=cand.name,
                    website_url=cand.url,
                    discovery_method=cand.source,
                    is_verified=True,
                    verification_score=cand.confidence,
                    crawl_frequency_hrs=cfg.sync.medium_priority_interval_hours,
                ))
                new_count += 1
        db.commit()
        return {"new_suppliers": new_count, "total_candidates": len(candidates)}
    finally:
        db.close()
