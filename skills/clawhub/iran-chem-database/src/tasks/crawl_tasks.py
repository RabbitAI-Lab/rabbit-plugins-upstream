"""Crawl tasks: HTTrack mirror → parse → classify → validate → sync (spec §3.3)."""
from __future__ import annotations

import asyncio
from datetime import datetime

from celery import shared_task
from sqlalchemy import select

from src.config import get_config
from src.crawler.httrack_engine import HTTrackMirrorEngine
from src.crawler.httrack_profiles import HTTrackProfiles
from src.crawler.playwright_fallback import PlaywrightFallbackEngine
from src.database.live_sync import LiveSyncEngine
from src.database.models import CrawlLog, HTTrackMirror, Supplier
from src.database.session import get_db_session
from src.parser.product_extractor import MoleculeExtractorPipeline


@shared_task(bind=True, max_retries=3)
def mirror_and_extract_supplier(self, supplier_id: int):
    cfg = get_config()
    db = get_db_session()
    try:
        supplier = db.get(Supplier, supplier_id)
        if supplier is None:
            return {"error": "supplier-not-found"}

        config = HTTrackProfiles.for_supplier(
            supplier.supplier_type, supplier.supplier_id,
            supplier.httrack_project_name or (supplier.company_name_en or "supplier"),
            supplier.website_url,
            requires_playwright=bool(supplier.requires_playwright),
        )
        config.output_dir = supplier.httrack_mirror_path or config.output_dir

        engine = HTTrackMirrorEngine(cfg.httrack.base_mirror_dir)
        mirror_stats = engine.mirror_supplier(config)

        # Playwright fallback for JS-heavy sites with no mirrored HTML
        if supplier.requires_playwright or mirror_stats.get("html_files", 0) == 0:
            fallback = PlaywrightFallbackEngine(cfg.httrack.base_mirror_dir)
            fallback.render_and_save(config, [supplier.website_url])

        if mirror_stats.get("is_update"):
            files_to_parse = engine.get_changed_files(config)
            files_removed = engine.get_removed_files(config)
        else:
            files_to_parse = engine.get_all_parseable_files(config)
            files_removed = []

        sync = LiveSyncEngine(db)
        extractor = MoleculeExtractorPipeline(db_sync=sync)
        extraction_results = extractor.process_files(
            files=files_to_parse, supplier_id=supplier_id,
            mirror_base_path=config.output_dir,
        )

        if files_removed:
            sync.mark_discontinued(supplier_id, files_removed)

        def _as_dt(value) -> datetime:
            try:
                return datetime.fromisoformat(value) if value else datetime.now()
            except (TypeError, ValueError):
                return datetime.now()

        db.add(CrawlLog(
            supplier_id=supplier_id,
            crawl_start=_as_dt(mirror_stats.get("start_time")),
            crawl_end=_as_dt(mirror_stats.get("end_time")),
            crawl_type="httrack_update" if mirror_stats.get("is_update") else "initial_mirror",
            pages_crawled=mirror_stats.get("total_files"),
            products_found=extraction_results["total_found"],
            products_new=extraction_results["new_count"],
            products_updated=extraction_results["updated_count"],
            products_removed=len(files_removed),
            errors={"parse_errors": extraction_results["errors"][:20]} if extraction_results["errors"] else None,
            status="success" if mirror_stats.get("return_code") == 0 else "partial",
        ))

        supplier.httrack_last_update = datetime.now()
        supplier.httrack_mirror_size_bytes = mirror_stats.get("mirror_size_bytes")
        supplier.httrack_total_files = mirror_stats.get("total_files")
        supplier.total_products = extraction_results["total_found"]
        supplier.last_crawled = datetime.now()

        # Update mirror record
        mirror = db.execute(
            select(HTTrackMirror).where(HTTrackMirror.supplier_id == supplier_id)
        ).scalar_one_or_none()
        if mirror is None:
            mirror = HTTrackMirror(supplier_id=supplier_id, mirror_path=config.output_dir,
                                   project_name=config.project_name)
            db.add(mirror)
        mirror.last_update_date = datetime.now()
        mirror.total_files = mirror_stats.get("total_files")
        mirror.html_files = mirror_stats.get("html_files")
        mirror.pdf_files = mirror_stats.get("pdf_files")
        mirror.excel_files = mirror_stats.get("excel_files")
        mirror.mirror_size_bytes = mirror_stats.get("mirror_size_bytes")
        mirror.httrack_return_code = mirror_stats.get("return_code")
        changes = mirror_stats.get("changes")
        if changes:
            mirror.last_changes_json = {k: len(v) for k, v in changes.items() if isinstance(v, list)}
            mirror.files_new_last_run = len(changes.get("new", []))
            mirror.files_modified_last_run = len(changes.get("modified", []))
            mirror.files_removed_last_run = len(changes.get("removed", []))

        sync.commit()
        return {"supplier_id": supplier_id, "products_found": extraction_results["total_found"]}
    finally:
        db.close()


@shared_task
def mirror_all_suppliers():
    """Iterate active suppliers and trigger mirrors whose interval elapsed."""
    db = get_db_session()
    try:
        suppliers = db.execute(select(Supplier).where(Supplier.status == "active")).scalars().all()
        for supplier in suppliers:
            last = supplier.last_crawled or datetime.min
            hours = (datetime.now() - last).total_seconds() / 3600
            if hours >= supplier.crawl_frequency_hrs:
                mirror_and_extract_supplier.delay(supplier.supplier_id)
        return {"queued": len(suppliers)}
    finally:
        db.close()


@shared_task
def full_discovery_and_mirror_cycle():
    """Weekly mega-task: discover new suppliers, mirror them, update existing."""
    from src.discovery.engine import SupplierDiscoveryEngine
    db = get_db_session()
    try:
        discovery = SupplierDiscoveryEngine()
        candidates = discovery.run_full_discovery()
        for cand in candidates:
            existing = db.execute(select(Supplier).where(Supplier.website_url == cand.url)).scalar_one_or_none()
            if existing is None:
                db.add(Supplier(
                    company_name_en=cand.name, website_url=cand.url,
                    discovery_method=cand.source, is_verified=True,
                    verification_score=cand.confidence,
                ))
        db.commit()
        mirror_all_suppliers.delay()
        return {"discovered": len(candidates)}
    finally:
        db.close()
