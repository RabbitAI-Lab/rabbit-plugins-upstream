"""Seed the initial supplier list into the database (spec §2.1)."""
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
        for cand in engine.seed_suppliers():
            exists = db.execute(select(Supplier).where(Supplier.website_url == cand.url)).scalar_one_or_none()
            if exists is None:
                db.add(Supplier(
                    company_name_en=cand.name,
                    website_url=cand.url,
                    discovery_method="seed",
                    crawl_frequency_hrs=24,
                ))
                inserted += 1
        db.commit()
        print(f"Seeded {inserted} new suppliers ({(len(engine.seed_suppliers()))} total in seed list).")
    finally:
        db.close()


if __name__ == "__main__":
    main()
