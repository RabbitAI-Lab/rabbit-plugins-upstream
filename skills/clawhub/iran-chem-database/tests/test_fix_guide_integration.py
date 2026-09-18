"""Integration tests for the fix-guide changes (requires PostgreSQL;
skipped automatically when DATABASE_URL is unreachable)."""
import pytest
from sqlalchemy import select

from src.database.models import Base, Molecule, RejectedCatalogueItem


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
    for sid, name in ((1, "Test Supplier One"), (42, "Acme Lab Chemicals")):
        session.add(Supplier(supplier_id=sid, company_name_en=name,
                             website_url=f"https://example-{sid}.ir", status="active"))
    session.commit()
    yield session
    session.close()


def test_cas_only_record_inserts(db_session):
    """THE original defect: a CAS-only record used to overflow VARCHAR(27)."""
    from src.database.live_sync import LiveSyncEngine
    sync = LiveSyncEngine(db_session)
    result = sync.upsert_molecule(
        {"cas_number": "67-64-1", "title": "Acetone", "grade": "HPLC Grade"},
        supplier_id=42)
    assert result in ("new", "updated")
    sync.commit()
    mol = db_session.execute(
        select(Molecule).where(Molecule.cas_number == "67-64-1")
    ).scalar_one_or_none()
    assert mol is not None
    assert mol.source_identity == "cas:67-64-1"
    assert mol.inchi_key is None          # never a fake InChIKey
    assert mol.organic_status == "unknown"


def test_real_inchikey_record(db_session):
    from src.database.live_sync import LiveSyncEngine
    sync = LiveSyncEngine(db_session)
    sync.upsert_molecule(
        {"inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "iupac_name": "ethanol",
         "canonical_smiles": "CCO", "organic_status": "true",
         "organic_reason": "structure", "grade": "ACS"},
        supplier_id=42)
    sync.commit()
    mol = db_session.execute(
        select(Molecule).where(Molecule.inchi_key == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N")
    ).scalar_one_or_none()
    assert mol is not None and mol.source_identity.startswith("inchikey:")


def test_rejection_audit_recorded(db_session):
    from src.database.live_sync import LiveSyncEngine
    sync = LiveSyncEngine(db_session)
    sync.record_rejection(
        {"title": "Industrial bitumen mix", "grade": "Industrial grade",
         "supplier_id": 42, "source_file": "catalog/page1.html"},
        stage="grade", reason="excluded-grade-marker")
    sync.commit()
    row = db_session.execute(select(RejectedCatalogueItem)).scalars().first()
    assert row is not None
    assert row.rejection_stage == "grade"
    assert row.rejection_reason == "excluded-grade-marker"
    assert row.raw_title == "Industrial bitumen mix"


def test_export_offerings_shape(db_session):
    """CSV export is complete (not page-limited) and carries metadata."""
    from fastapi.testclient import TestClient
    from src.api.app import app
    from src.database.session import get_session_factory

    factory = get_session_factory()

    def override_db():
        s = factory()
        try:
            yield s
        finally:
            s.close()

    app.dependency_overrides.clear()
    # override the export route's get_db
    from src.api.routes import export as export_mod
    app.dependency_overrides[export_mod.get_db] = override_db
    client = TestClient(app)
    resp = client.get("/api/v1/export?format=csv&shape=offerings")
    assert resp.status_code == 200
    body = resp.text
    assert "export_metadata" in body
    assert "source_identity" in body
    assert "organic_status" in body
    # acetone row must be present (never truncated)
    assert "67-64-1" in body
    app.dependency_overrides.clear()


def test_export_molecules_shape_and_organic_filter(db_session):
    from fastapi.testclient import TestClient
    from src.api.app import app
    from src.api.routes import export as export_mod
    from src.database.session import get_session_factory

    factory = get_session_factory()

    def override_db():
        s = factory()
        try:
            yield s
        finally:
            s.close()

    app.dependency_overrides[export_mod.get_db] = override_db
    client = TestClient(app)
    resp = client.get("/api/v1/export?format=csv&shape=molecules&organic_status=true")
    assert resp.status_code == 200
    body = resp.text
    assert "n_suppliers" in body
    assert "LFQSCWFLJHTTHZ-UHFFFAOYSA-N" in body
    assert "67-64-1" not in body  # acetone has organic_status unknown → filtered out
    app.dependency_overrides.clear()


def test_coverage_endpoint(db_session):
    from fastapi.testclient import TestClient
    from src.api.app import app
    from src.api.routes import coverage as cov_mod
    from src.database.session import get_session_factory

    factory = get_session_factory()

    def override_db():
        s = factory()
        try:
            yield s
        finally:
            s.close()

    app.dependency_overrides[cov_mod.get_db] = override_db
    client = TestClient(app)
    resp = client.get("/api/v1/coverage")
    assert resp.status_code == 200
    data = resp.json()
    for key in ("generated_at", "scope", "inclusion_mode", "suppliers",
                "records", "export_readiness"):
        assert key in data
    assert data["suppliers"]["configured"] >= 1
    assert data["records"]["accepted_molecules"] >= 2
    assert data["export_readiness"]["ready_for_complete_configured_supplier_export"] is False
    app.dependency_overrides.clear()


def test_manifest_and_coverage_gate(db_session):
    """format=manifest returns JSON with row count + SHA-256 (remediation §3/§4)."""
    from fastapi.testclient import TestClient
    from src.api.app import app
    from src.api.routes import export as export_mod
    from src.database.session import get_session_factory

    factory = get_session_factory()

    def override_db():
        s = factory()
        try:
            yield s
        finally:
            s.close()

    app.dependency_overrides[export_mod.get_db] = override_db
    client = TestClient(app)

    resp = client.get("/api/v1/export?format=manifest&shape=molecules&organic_status=all")
    assert resp.status_code == 200
    manifest = resp.json()
    assert manifest["row_count"] >= 1
    assert len(manifest["csv_sha256"]) == 64
    assert "coverage" in manifest and "scope" in manifest

    # gating: coverage incomplete -> 409
    resp = client.get("/api/v1/export?format=csv&require_complete_coverage=true")
    assert resp.status_code == 409
    assert "blocking_reasons" in resp.json()["detail"]
    app.dependency_overrides.clear()
