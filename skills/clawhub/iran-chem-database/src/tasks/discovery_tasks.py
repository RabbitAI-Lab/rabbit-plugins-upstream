"""Scheduled discovery tasks (remediation §2).

Directory discovery is split into its own task with strict per-directory time
budgets and run caps, so it can never delay the seed-crawling cohort. Seed
crawling uses the 35 curated supplier seeds as the first crawl cohort.
"""
from __future__ import annotations

from celery import shared_task
from pathlib import Path
from sqlalchemy import select

from src.config import get_config
from src.discovery.engine import SupplierCandidate, SupplierDiscoveryEngine
from src.database.models import Supplier
from src.database.session import get_db_session
from src.discovery.country_gate import IRAN


def _insert_candidates(db, candidates) -> int:
    cfg = get_config()
    new_count = 0
    max_new = int((cfg.as_dict().get("discovery", {}) or {}).get("max_new_candidates_per_run", 100))
    for cand in candidates[:max_new]:
        # v2.11 country gate: never persist a non-Iranian supplier.
        if (cand.extra or {}).get("country") != IRAN:
            continue
        exists = db.execute(select(Supplier).where(Supplier.website_url == cand.url)).scalar_one_or_none()
        if exists is None:
            db.add(Supplier(
                company_name_en=cand.name,
                website_url=cand.url,
                country=IRAN,
                discovery_method=cand.source,
                is_verified=True,
                verification_score=cand.confidence,
                crawl_profile=cand.extra.get("crawl_profile") if cand.extra else None,
                crawl_frequency_hrs=cfg.sync.medium_priority_interval_hours,
            ))
            new_count += 1
    db.commit()
    return new_count


@shared_task
def weekly_discovery():
    """Weekly sweep WITHOUT directory crawling (remediation §2): seeds +
    search engines + link analysis over mirrored suppliers + manual curation.
    Every candidate is verified before use; directory discovery runs as a
    separate opt-in task (directory_discovery) so seeding is never delayed."""
    engine = SupplierDiscoveryEngine()

    db = get_db_session()
    try:
        candidates = engine.seed_suppliers()
        try:
            candidates += engine.discover_via_search_engines()
        except Exception:  # noqa: BLE001 (search API may be unconfigured)
            pass

        # link analysis over already-mirrored supplier sites
        mirrors = db.execute(select(Supplier).where(Supplier.httrack_mirror_path.isnot(None))).scalars().all()
        seen = {c.url for c in candidates}
        for sup in mirrors:
            if not sup.httrack_mirror_path:
                continue
            try:
                for url in engine.discover_via_link_analysis(sup.httrack_mirror_path):
                    if url and url not in seen:
                        seen.add(url)
                        candidates.append(SupplierCandidate(url=url, source="link_analysis"))
            except Exception:  # noqa: BLE001
                continue

        # manually curated additions
        curated_path = Path(__file__).resolve().parent.parent.parent / "curated_suppliers.json"
        if curated_path.exists():
            try:
                import json as _json
                for row in _json.load(open(curated_path, encoding="utf-8")):
                    url = str(row.get("website_url") or row.get("url") or "").strip()
                    if url and url not in seen:
                        seen.add(url)
                        candidates.append(SupplierCandidate(
                            url=url, source="manual",
                            name=row.get("name"), extra={"crawl_profile": row.get("crawl_profile")}))
            except Exception:  # noqa: BLE001
                pass

        new_count = _insert_candidates(db, candidates)
        return {"new_suppliers": new_count, "total_candidates": len(candidates)}
    finally:
        db.close()


@shared_task
def directory_discovery():
    """OPT-IN B2B directory discovery with strict budgets (remediation §2).

    Mirrors at most `discovery.max_directories_per_run` directories, each with
    `discovery.directory_timeout_seconds` budget, and inserts at most
    `discovery.max_new_candidates_per_run` verified candidates. Never blocks
    seed crawling; enabled only when
    `discovery.initial_directory_discovery=true` or called explicitly.
    """
    cfg = get_config()
    dcfg = cfg.as_dict().get("discovery", {}) or {}
    timeout = int(dcfg.get("directory_timeout_seconds", 120))
    max_dirs = int(dcfg.get("max_directories_per_run", 3))
    max_new = int(dcfg.get("max_new_candidates_per_run", 100))

    engine = SupplierDiscoveryEngine()
    db = get_db_session()
    try:
        candidates = engine.discover_via_directory_crawling_httrack(
            timeout=timeout, max_directories=max_dirs)
        new_count = 0
        for cand in candidates[:max_new]:
            # v2.11 country gate: never persist a non-Iranian supplier.
            if (cand.extra or {}).get("country") != IRAN:
                continue
            exists = db.execute(select(Supplier).where(Supplier.website_url == cand.url)).scalar_one_or_none()
            if exists is None:
                db.add(Supplier(
                    company_name_en=cand.name, website_url=cand.url,
                    country=IRAN, discovery_method=cand.source, is_verified=True,
                    verification_score=cand.confidence,
                    crawl_frequency_hrs=cfg.sync.medium_priority_interval_hours,
                ))
                new_count += 1
        db.commit()
        return {"new_suppliers": new_count, "directory_candidates": len(candidates),
                "directories_tried": max_dirs, "timeout_seconds": timeout}
    finally:
        db.close()
