"""Offering-history tracking helpers (spec §5.1 offering_history)."""
from __future__ import annotations

from datetime import datetime

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.database.models import OfferingHistory


class ChangeTracker:
    def __init__(self, session: Session):
        self.db = session

    def record(self, offering_id: int | None, molecule_id: int | None,
               supplier_id: int | None, change_type: str,
               old_values: dict | None = None, new_values: dict | None = None,
               detected_via: str = "manual") -> OfferingHistory:
        entry = OfferingHistory(
            offering_id=offering_id, molecule_id=molecule_id, supplier_id=supplier_id,
            change_type=change_type, old_values=old_values, new_values=new_values,
            detected_via=detected_via, changed_at=datetime.now(),
        )
        self.db.add(entry)
        return entry

    def recent(self, limit: int = 100) -> list[OfferingHistory]:
        return list(self.db.execute(
            select(OfferingHistory).order_by(OfferingHistory.changed_at.desc()).limit(limit)
        ).scalars())
