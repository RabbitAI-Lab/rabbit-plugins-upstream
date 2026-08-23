"""Integration test for the database layer (requires PostgreSQL).

Skipped automatically when DATABASE_URL is not reachable, so the suite stays
green on machines without a running Postgres.
"""
import pytest
from sqlalchemy.exc import OperationalError

from src.database.models import Base


@pytest.fixture(scope="module")
def db_session():
    from src.database.session import get_engine, get_session_factory
    engine = get_engine()
    try:
        conn = engine.connect()
        conn.close()
    except Exception:
        pytest.skip("PostgreSQL not reachable")
    Base.metadata.create_all(engine)
    session = get_session_factory()()
    from src.database.models import (CrawlLog, CrawlRunState, Molecule, OfferingHistory,
                                     RejectedCatalogueItem, Supplier, SupplierOffering)
    for model in (OfferingHistory, CrawlRunState, SupplierOffering, RejectedCatalogueItem,
                  CrawlLog, Molecule, Supplier):
        session.execute(model.__table__.delete())
    session.add(Supplier(supplier_id=1, company_name_en="Test Supplier",
                         website_url="https://example-chem.ir", status="active"))
    session.commit()
    yield session
    session.close()


def test_upsert_new_molecule(db_session):
    from src.database.live_sync import LiveSyncEngine
    sync = LiveSyncEngine(db_session)
    result = sync.upsert_molecule(
        {"inchi_key": "TESTKEY00000000000000000001", "iupac_name": "test molecule",
         "cas_number": "64-17-5", "grade": "ACS Reagent"}, supplier_id=1)
    assert result in ("new", "updated")
    sync.commit()


def test_mark_discontinued(db_session):
    from src.database.live_sync import LiveSyncEngine
    sync = LiveSyncEngine(db_session)
    count = sync.mark_discontinued(1, ["nonexistent-file.html"])
    assert count == 0
