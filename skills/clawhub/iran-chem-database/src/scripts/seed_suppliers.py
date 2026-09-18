"""Seed the initial supplier list into the database (spec §2.1).

v2.5: persists the fingerprint metadata shipped with the seed list — status
(active/inactive), crawl profile (woo_rest / sitemap_wp / …), notes and REST/
sitemap entry points — so the crawler skips dead/parked domains and routes
WooCommerce storefronts to the public REST API without a full mirror.
"""
from __future__ import annotations

from sqlalchemy import select

from src.database.models import Supplier
from src.database.session import get_db_session
from src.discovery.engine import SupplierDiscoveryEngine


def main() -> None:
    db = get_db_session()
    engine = SupplierDiscoveryEngine()
    try:
        inserted = 0
        updated = 0
        for cand in engine.seed_suppliers():
            exists = db.execute(select(Supplier).where(Supplier.website_url == cand.url)).scalar_one_or_none()
            extra = cand.extra or {}
            if exists is None:
                db.add(Supplier(
                    company_name_en=cand.name,
                    website_url=cand.url,
                    # v2.11: the curated seed list is Iranian-only by
                    # construction and is re-checked by tools/audit_country.py.
                    country="IR",
                    discovery_method="seed",
                    crawl_frequency_hrs=24,
                    status=extra.get("status", "active"),
                    crawl_profile=extra.get("profile"),
                    notes=extra.get("notes") or None,
                    catalog_entry_points=extra.get("entry_points") or None,
                ))
                inserted += 1
            else:
                # Backfill metadata on re-seed without clobbering crawl results.
                if exists.status is None or exists.status == "active":
                    exists.status = extra.get("status", exists.status)
                if not exists.crawl_profile:
                    exists.crawl_profile = extra.get("profile")
                if not exists.notes:
                    exists.notes = extra.get("notes") or None
                if not exists.catalog_entry_points:
                    exists.catalog_entry_points = extra.get("entry_points") or None
                updated += 1
        db.commit()
        print(f"Seeded {inserted} new suppliers, refreshed {updated} existing "
              f"({len(engine.seed_suppliers())} total in seed list).")
    finally:
        db.close()


if __name__ == "__main__":
    main()
