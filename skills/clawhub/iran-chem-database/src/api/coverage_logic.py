"""Shared coverage/readiness logic (remediation §4).

Status is derived from the LATEST CrawlRunState per supplier (sorted by run_id),
not from ad hoc state transitions. A later `success` correctly supersedes an
earlier `partial`. Queued/running counts come from persisted run states, never
hard-coded zeros.
"""
from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import func, select

from src.database.models import (CrawlRunState, Molecule, RejectedCatalogueItem,
                                 Supplier, SupplierOffering)


def coverage_snapshot(db) -> dict:
    now = datetime.now(timezone.utc)
    suppliers = db.execute(select(Supplier)).scalars().all()
    runs = db.execute(select(CrawlRunState).order_by(CrawlRunState.run_id)).scalars().all()

    # latest run per supplier — a durable, run-id ordered "latest wins" view
    latest: dict[int, CrawlRunState] = {}
    for run in runs:
        if run.supplier_id is not None:
            latest[run.supplier_id] = run

    counts = {"queued": 0, "running": 0, "success": 0, "partial": 0,
              "failed": 0, "skipped": 0, "not_started": 0}
    for s in suppliers:
        run = latest.get(s.supplier_id)
        state = run.state if run else "not_started"
        counts[state] = counts.get(state, 0) + 1

    organic_true = db.execute(select(func.count()).select_from(Molecule)
                              .where(Molecule.organic_status == "true")).scalar_one()
    organic_false = db.execute(select(func.count()).select_from(Molecule)
                               .where(Molecule.organic_status == "false")).scalar_one()
    organic_unknown = db.execute(select(func.count()).select_from(Molecule)
                                 .where(Molecule.organic_status == "unknown")).scalar_one()
    molecules = db.execute(select(func.count()).select_from(Molecule)).scalar_one()
    offerings = db.execute(select(func.count()).select_from(SupplierOffering)).scalar_one()
    rejected_grade = db.execute(select(func.count()).select_from(RejectedCatalogueItem)
                                .where(RejectedCatalogueItem.rejection_stage == "grade")).scalar_one()
    rejected_validation = db.execute(select(func.count()).select_from(RejectedCatalogueItem)
                                     .where(RejectedCatalogueItem.rejection_stage == "validation")).scalar_one()
    rejected_sync = db.execute(select(func.count()).select_from(RejectedCatalogueItem)
                               .where(RejectedCatalogueItem.rejection_stage == "database_sync")).scalar_one()

    complete = counts["queued"] == 0 and counts["running"] == 0 and \
        counts["failed"] == 0 and counts["partial"] == 0 and counts["not_started"] == 0
    blocking = []
    if counts["not_started"]: blocking.append(f"{counts['not_started']} suppliers not started")
    if counts["queued"]: blocking.append(f"{counts['queued']} suppliers queued")
    if counts["running"]: blocking.append(f"{counts['running']} suppliers running")
    if counts["partial"]: blocking.append(f"{counts['partial']} partial supplier crawls")
    if counts["failed"]: blocking.append(f"{counts['failed']} failed suppliers")

    return {
        "generated_at": now.isoformat(),
        "scope": "Best-effort public supplier-catalogue index; not national market coverage.",
        "inclusion_mode": _inclusion_mode(),
        "suppliers": {
            "configured": len(suppliers),
            "queued": counts["queued"],
            "running": counts["running"],
            "success": counts["success"],
            "partial": counts["partial"],
            "failed": counts["failed"],
            "skipped": counts["skipped"],
            "not_started": counts["not_started"],
        },
        "records": {
            "accepted_molecules": molecules,
            "offerings": offerings,
            "rejected_grade": rejected_grade,
            "rejected_validation": rejected_validation,
            "rejected_sync": rejected_sync,
            "organic_true": organic_true,
            "organic_false": organic_false,
            "organic_unknown": organic_unknown,
        },
        "export_readiness": {
            "ready_for_scoped_export": molecules > 0 or offerings > 0,
            "ready_for_complete_configured_supplier_export": complete,
            "blocking_reasons": blocking,
        },
    }


def _inclusion_mode() -> str:
    try:
        from src.config import get_config
        return (get_config().as_dict().get("parsing", {}) or {}).get("inclusion_mode", "lab_or_research")
    except Exception:  # noqa: BLE001
        return "lab_or_research"
