"""Remediation-plan integration tests (require PostgreSQL; auto-skip elsewhere)."""
import hashlib
import json

import pytest
from sqlalchemy import select

from src.database.models import (Base, CrawlRunState, Molecule, RejectedCatalogueItem,
                                 Supplier, SupplierOffering)


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
    # clean slate
    from src.database.models import (CrawlLog, HTTrackMirror, OfferingHistory,
                                     SupplierOffering, Supplier, Molecule,
                                     RejectedCatalogueItem, CrawlRunState)
    for model in (OfferingHistory, CrawlLog, CrawlRunState, RejectedCatalogueItem,
                  HTTrackMirror, SupplierOffering, Molecule, Supplier):
        session.execute(model.__table__.delete())
    session.add(Supplier(supplier_id=1, company_name_en="Acme Lab Chemicals",
                         website_url="https://acme-lab.ir", status="active"))
    session.add(Supplier(supplier_id=2, company_name_en="Beta Reagents",
                         website_url="https://beta-reagents.ir", status="active"))
    session.commit()
    yield session
    session.close()


def _client():
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
    for mod in ("src.api.routes.molecules", "src.api.routes.export",
                "src.api.routes.coverage", "src.api.routes.observability",
                "src.api.routes.stats"):
        m = __import__(mod, fromlist=["get_db"])
        app.dependency_overrides[m.get_db] = override_db
    return TestClient(app)


@pytest.fixture(scope="module")
def seeded(db_session):
    """>100 molecules so pagination behavior is exercised (remediation §3/§10)."""
    from src.database.live_sync import LiveSyncEngine
    sync = LiveSyncEngine(db_session)
    # 120 molecules: 60 confirmed organic, 30 inorganic, 30 unknown
    for i in range(120):
        cas = f"{100000 + i:07d}"
        # CAS checksum must be valid for identity; synthesize valid CAS-like ids:
        # use simple approach — sequential valid CAS numbers are tedious, so
        # derive identity from supplier code instead (supported path).
        status = "true" if i < 60 else ("false" if i < 90 else "unknown")
        sync.upsert_molecule({
            "title": f"Test chemical {i}",
            "supplier_product_code": f"TC-{i:04d}",
            "molecular_formula": f"C{i % 12 + 1}H{i % 20 + 2}O" if status == "true" else "NaCl",
            "organic_status": status,
            "organic_reason": "structure",
            "grade": "Laboratory",
        }, supplier_id=1)
        db_session.flush()
    sync.commit()
    return db_session


def test_molecules_pagination_metadata(seeded):
    client = _client()
    resp = client.get("/api/v1/molecules?page=1&limit=100")
    assert resp.status_code == 200
    data = resp.json()
    assert data["total"] >= 120
    assert data["limit"] == 100
    assert data["has_more"] is True
    assert data["next_page"] == 2
    assert data["total_pages"] >= 2
    assert "export_hint" in data
    assert len(data["molecules"]) == 100
    # page 2 returns the rest
    resp2 = client.get("/api/v1/molecules?page=2&limit=100")
    assert resp2.json()["has_more"] is False or resp2.json()["total"] - 100 == len(resp2.json()["molecules"])


def test_molecules_organic_filter_and_422(seeded):
    client = _client()
    resp = client.get("/api/v1/molecules?organic_status=true&limit=100")
    data = resp.json()
    assert data["total"] == 60
    assert all(m["organic_status"] == "true" for m in data["molecules"])
    resp = client.get("/api/v1/molecules?organic_status=bogus")
    assert resp.status_code == 422


def test_export_returns_every_matching_row(seeded):
    client = _client()
    resp = client.get("/api/v1/export?format=csv&shape=molecules&organic_status=all")
    assert resp.status_code == 200
    body = resp.text
    rows = [l for l in body.splitlines() if l and not l.startswith("#")]
    assert len(rows) == 1 + 120  # header + 120 rows
    manifest = client.get("/api/v1/export?format=manifest&shape=molecules&organic_status=all").json()
    assert manifest["row_count"] == 120
    # manifest SHA-256 must match the CSV we just downloaded
    csv_body_after_meta = "\r\n".join(body.splitlines()[1:]) + "\r\n"
    # hash the exact CSV bytes the manifest describes (header+rows, no metadata line)
    import io, csv as _csv
    buf = io.StringIO()
    w = _csv.writer(buf)
    w.writerow([c for c in ("source_identity","inchi_key","iupac_name","cas_number","molecular_formula","molecular_weight","canonical_smiles","inchi","pubchem_cid","organic_status","organic_reason","organic_confidence","classification_review_required","n_suppliers","suppliers")])
    for l in rows[1:]:
        w.writerow(next(_csv.reader([l])))
    assert hashlib.sha256(buf.getvalue().encode("utf-8")).hexdigest() == manifest["csv_sha256"]


def test_export_gate_409_when_incomplete(seeded):
    client = _client()
    resp = client.get("/api/v1/export?format=csv&require_complete_coverage=true")
    assert resp.status_code == 409
    assert "blocking_reasons" in resp.json()["detail"]


def test_latest_run_transition_partial_then_success(seeded):
    """A partial crawl followed by success must report success (remediation §4)."""
    from src.tasks.crawl_tasks import _mark_run
    _mark_run(seeded, 1, "queued")
    _mark_run(seeded, 1, "running")
    _mark_run(seeded, 1, "partial", "no-html-mirrored")
    seeded.commit()
    _mark_run(seeded, 1, "queued")
    _mark_run(seeded, 1, "running")
    _mark_run(seeded, 1, "success")
    seeded.commit()

    client = _client()
    cov = client.get("/api/v1/coverage").json()
    assert cov["suppliers"]["success"] == 1
    assert cov["suppliers"]["partial"] == 0

    jobs = client.get("/api/v1/jobs").json()["jobs"]
    states = {j["state"] for j in jobs if j["supplier_id"] == 1}
    assert "success" in states


def test_rejections_endpoint_and_reparse_restores(seeded, tmp_path):
    """Industrial-grade product excluded under research_only, retained under
    all_identifiable_catalogue, and previously rejected items become eligible
    after reparse (remediation §5)."""
    from src.database.live_sync import LiveSyncEngine
    from src.parser.product_extractor import MoleculeExtractorPipeline

    # craft an HTML fixture with an industrial-grade product that has a CAS
    # Formula included so organic classification is deterministic offline
    html = """
    <html><body>
    <table>
      <tr><th>Product</th><th>CAS</th><th>Grade</th><th>Formula</th></tr>
      <tr><td>Industrial bitumen solvent</td><td>67-64-1</td><td>Industrial grade</td><td>C7H16</td></tr>
    </table>
    </body></html>
    """
    f = tmp_path / "catalog.html"
    f.write_text(html)

    # 1) research_only → rejected and audited
    sync = LiveSyncEngine(seeded)
    ex = MoleculeExtractorPipeline(db_sync=sync, inclusion_mode="research_only",
                               organic_network=False)
    r = ex.process_files([str(f)], supplier_id=1, mirror_base_path=str(tmp_path))
    sync.commit()
    assert r["rejected_grade"] >= 1
    rej = seeded.execute(select(RejectedCatalogueItem)).scalars().all()
    assert any(x.rejection_stage == "grade" and "industrial" in (x.raw_title or "").lower() for x in rej)

    # 2) all_identifiable_catalogue → retained with grade preserved
    seeded.execute(RejectedCatalogueItem.__table__.delete())
    seeded.commit()
    sync2 = LiveSyncEngine(seeded)
    ex2 = MoleculeExtractorPipeline(db_sync=sync2, inclusion_mode="all_identifiable_catalogue",
                                    organic_network=False)
    r2 = ex2.process_files([str(f)], supplier_id=1, mirror_base_path=str(tmp_path))
    sync2.commit()
    assert r2["total_found"] >= 1
    mol = seeded.execute(select(Molecule).where(Molecule.cas_number == "67-64-1")).scalar_one_or_none()
    assert mol is not None
    off = seeded.execute(select(SupplierOffering).where(SupplierOffering.molecule_id == mol.molecule_id)).scalar_one()
    assert "industrial" in off.grade.lower()

    # 3) rejections endpoint reports the audit
    client = _client()
    resp = client.get("/api/v1/rejections")
    assert resp.status_code == 200
    assert "rejections" in resp.json()


def test_unknown_organic_not_silently_dropped(seeded):
    """organic_status=unknown records are exported separately (remediation §6)."""
    client = _client()
    resp = client.get("/api/v1/export?format=csv&shape=molecules&organic_status=unknown")
    body = resp.text
    rows = [l for l in body.splitlines() if l and not l.startswith("#")]
    assert len(rows) == 1 + 30  # header + 30 unknown molecules
    assert "classification_review_required" in rows[0]
