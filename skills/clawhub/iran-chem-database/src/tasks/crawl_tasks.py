"""Crawl tasks: HTTrack mirror → parse → classify → validate → sync (spec §3.3).

Remediation-plan changes (§2/§4/§7):
  * every run is persisted in CrawlRunState (queued → running → terminal),
    so /coverage reports REAL queued/running counts and latest-run logic is
    timestamp-driven;
  * mirror_all_suppliers returns honest counts (active/eligible/queued/
    skipped_not_due) and writes queued states;
  * crawl quality checks mark a crawl partial when pagination, product count,
    API capture, or expected catalogue resources are incomplete — not merely
    when HTTrack exits nonzero (remediation §7);
  * supplier rows get last_http_status / last_successful_product_count /
    partial_reason updated per run.
"""
from __future__ import annotations

import logging
from datetime import datetime

from celery import shared_task
from sqlalchemy import desc, select

from src.config import get_config
from src.crawler.httrack_engine import HTTrackMirrorEngine
from src.crawler.httrack_profiles import HTTrackProfiles
from src.crawler.js_catalogue import JSCatalogueEngine
from src.crawler.playwright_fallback import PlaywrightFallbackEngine
from src.database.live_sync import LiveSyncEngine
from src.database.models import CrawlLog, CrawlRunState, HTTrackMirror, Supplier
from src.database.session import get_db_session
from src.parser.product_extractor import MoleculeExtractorPipeline

logger = logging.getLogger(__name__)


def _latest_run(db, supplier_id: int):
    return db.execute(
        select(CrawlRunState).where(CrawlRunState.supplier_id == supplier_id)
        .order_by(desc(CrawlRunState.run_id)).limit(1)
    ).scalar_one_or_none()


def _mark_run(db, supplier_id: int, state: str, reason: str | None = None,
              task_id: str | None = None):
    run = _latest_run(db, supplier_id)
    if run is None or run.state in ("success", "partial", "failed", "skipped"):
        run = CrawlRunState(supplier_id=supplier_id, state=state,
                            task_id=task_id, reason=reason)
        if state == "queued":
            run.queued_at = datetime.now()
        elif state == "running":
            run.started_at = datetime.now()
        else:
            run.started_at = datetime.now()
            run.finished_at = datetime.now()
        db.add(run)
    else:
        run.state = state
        run.reason = reason
        if state == "running" and run.started_at is None:
            run.started_at = datetime.now()
        if state in ("success", "partial", "failed", "skipped"):
            run.finished_at = datetime.now()
    db.flush()
    return run


def _partial_reason(supplier, mirror_stats: dict, extraction_results: dict,
                    api_hints: int, api_json_saved: int) -> str | None:
    """Detect incomplete crawls (remediation §7: a clean process exit is NOT
    proof of a complete catalogue)."""
    reasons = []
    if mirror_stats.get("timed_out"):
        reasons.append("timeout-limit-reached")
    if mirror_stats.get("return_code", 0) not in (0, None):
        reasons.append(f"httrack-rc-{mirror_stats.get('return_code')}")
    if mirror_stats.get("html_files", 0) == 0:
        reasons.append("no-html-mirrored")
    if extraction_results.get("errors"):
        reasons.append(f"parse-errors-{len(extraction_results['errors'])}")
    found = extraction_results.get("total_found", 0)
    if found == 0 and mirror_stats.get("html_files", 0) > 0:
        reasons.append("pages-mirrored-but-zero-products")
    if extraction_results.get("rejected_grade", 0) and found == 0:
        reasons.append("all-products-grade-rejected")
    # pagination completeness (§7)
    if supplier.expected_pagination:
        try:
            pages_expected = int(str(supplier.expected_pagination))
            if mirror_stats.get("html_files", 0) < pages_expected:
                reasons.append(f"pagination-incomplete:{mirror_stats.get('html_files', 0)}/{pages_expected}")
        except ValueError:
            pass
    # API capture expected but nothing saved (§7)
    if api_hints and api_json_saved == 0:
        reasons.append("api-hints-present-but-zero-json-captured")
    # unexpected product-count drop (§9)
    prev = supplier.last_successful_product_count
    if prev and found and found < prev // 2:
        reasons.append(f"product-count-drop:{prev}->{found}")
    return "; ".join(reasons) if reasons else None


def _is_lab_supplier(db, supplier: Supplier) -> bool:
    from src.parser.grade_classifier import GradeClassifier
    gc = GradeClassifier()
    try:
        return gc.is_lab_supplier({
            "company_name_en": supplier.company_name_en,
            "company_name_fa": supplier.company_name_fa,
            "supplier_type": supplier.supplier_type,
            "specializations": supplier.specializations,
            "notes": supplier.notes,
        })
    except Exception:  # noqa: BLE001
        return False


@shared_task(bind=True, max_retries=3)
def mirror_and_extract_supplier(self, supplier_id: int):
    cfg = get_config()
    db = get_db_session()
    task_id = self.request.id if self.request else None
    try:
        supplier = db.get(Supplier, supplier_id)
        if supplier is None:
            return {"error": "supplier-not-found"}

        _mark_run(db, supplier_id, "running", task_id=task_id)
        db.commit()

        profile = supplier.crawl_profile or \
            HTTrackProfiles.classify_profile(supplier.supplier_type, supplier.website_url)
        supplier.crawl_profile = profile

        config = HTTrackProfiles.for_supplier(
            supplier.supplier_type, supplier.supplier_id,
            supplier.httrack_project_name or (supplier.company_name_en or "supplier"),
            supplier.website_url,
            requires_playwright=bool(supplier.requires_playwright) or profile == "js_catalogue",
            profile=profile,
        )
        config.output_dir = supplier.httrack_mirror_path or config.output_dir

        engine = HTTrackMirrorEngine(cfg.httrack.base_mirror_dir)
        mirror_stats = engine.mirror_supplier(config)

        if supplier.requires_playwright or mirror_stats.get("html_files", 0) == 0:
            fallback = PlaywrightFallbackEngine(cfg.httrack.base_mirror_dir)
            fallback.render_and_save(config, [supplier.website_url])

        # JS/API catalogue capture (§7)
        api_hints = 0
        api_json_saved = 0
        try:
            js_engine = JSCatalogueEngine(cfg.httrack.base_mirror_dir)
            for f in engine.get_all_parseable_files(config)[:20]:
                if f.lower().endswith((".html", ".htm", ".php")):
                    try:
                        body = open(f, encoding="utf-8", errors="replace").read()
                    except OSError:
                        continue
                    if js_engine.page_has_api_hints(body):
                        api_hints += 1
            if api_hints:
                res = js_engine.capture_json_responses_sync(
                    config, [supplier.website_url], output_subdir="api_json")
                api_json_saved = res.get("saved", 0)
        except Exception as exc:  # noqa: BLE001
            logger.warning("JS catalogue capture failed for %s: %s", supplier_id, exc)

        if mirror_stats.get("is_update"):
            files_to_parse = engine.get_changed_files(config)
            files_removed = engine.get_removed_files(config)
        else:
            files_to_parse = engine.get_all_parseable_files(config)
            files_removed = []

        sync = LiveSyncEngine(db)
        extractor = MoleculeExtractorPipeline(
            db_sync=sync,
            supplier_is_lab=_is_lab_supplier(db, supplier),
        )
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

        partial_reason = _partial_reason(supplier, mirror_stats, extraction_results,
                                         api_hints, api_json_saved)
        status = ("failed" if mirror_stats.get("return_code", 0) not in (0, None)
                  and mirror_stats.get("error") else
                  ("partial" if partial_reason else "success"))

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
            status=status,
            partial_reason=partial_reason,
        ))

        supplier.httrack_last_update = datetime.now()
        supplier.httrack_mirror_size_bytes = mirror_stats.get("mirror_size_bytes")
        supplier.httrack_total_files = mirror_stats.get("total_files")
        supplier.total_products = extraction_results["total_found"]
        supplier.last_crawled = datetime.now()
        supplier.last_http_status = 200 if mirror_stats.get("html_files", 0) else None
        if status == "success" and extraction_results["total_found"] > 0:
            supplier.last_successful_product_count = extraction_results["total_found"]
        supplier.partial_reason = partial_reason

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

        _mark_run(db, supplier_id, status, partial_reason, task_id=task_id)
        sync.commit()
        return {
            "supplier_id": supplier_id,
            "products_found": extraction_results["total_found"],
            "status": status,
            "partial_reason": partial_reason,
            "api_json_saved": api_json_saved,
            "organic": {
                "true": extraction_results.get("organic_true", 0),
                "false": extraction_results.get("organic_false", 0),
                "unknown": extraction_results.get("organic_unknown", 0),
            },
        }
    except Exception as exc:  # noqa: BLE001
        logger.exception("mirror_and_extract_supplier failed for %s", supplier_id)
        try:
            _mark_run(db, supplier_id, "failed", str(exc)[:290], task_id=task_id)
            db.commit()
        except Exception:  # noqa: BLE001
            pass
        return {"error": str(exc)[:300]}
    finally:
        db.close()


@shared_task
def mirror_all_suppliers():
    """Queue mirrors whose crawl interval elapsed (remediation §2/§4).

    Returns honest counts and persists queued run states so /coverage can
    report them.
    """
    db = get_db_session()
    try:
        suppliers = db.execute(select(Supplier).where(Supplier.status == "active")).scalars().all()
        eligible = 0
        queued = 0
        skipped_not_due = 0
        for supplier in suppliers:
            last = supplier.last_crawled or datetime.min
            hours = (datetime.now() - last).total_seconds() / 3600
            if hours >= supplier.crawl_frequency_hrs:
                eligible += 1
                mirror_and_extract_supplier.delay(supplier.supplier_id)
                _mark_run(db, supplier.supplier_id, "queued")
                queued += 1
            else:
                skipped_not_due += 1
                if _latest_run(db, supplier.supplier_id) is None:
                    _mark_run(db, supplier.supplier_id, "skipped", "not-due")
        db.commit()
        return {
            "active": len(suppliers),
            "eligible": eligible,
            "queued": queued,
            "skipped_not_due": skipped_not_due,
        }
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
