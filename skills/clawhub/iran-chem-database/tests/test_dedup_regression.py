"""Dedup & data-integrity regression tests (v2.4.0).

The user-visible bug was the same chemical appearing as MULTIPLE rows in
molecule-shaped exports. Root causes fixed here:
  1. identity fragmentation (inchikey: vs cas: vs fallback: for one chemical)
     → cross-identity merge at upsert time;
  2. fallback keys built from un-normalized titles ("Ethanol 96% 1 lit" vs
     "ethanol") → normalized fallback basis;
  3. offerings keyed only by (molecule, supplier) → distinct product codes
     overwrote each other and were never persisted;
  4. invalid CAS values persisted verbatim.
"""
import pytest
from sqlalchemy import select

from src.database.models import (Base, Molecule, Supplier, SupplierOffering)


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
    from src.database.models import (CrawlLog, CrawlRunState, HTTrackMirror,
                                     OfferingHistory, RejectedCatalogueItem)
    for model in (OfferingHistory, CrawlLog, CrawlRunState, RejectedCatalogueItem,
                  HTTrackMirror, SupplierOffering, Molecule, Supplier):
        session.execute(model.__table__.delete())
    for sid, name in ((1, "Supplier One"), (2, "Supplier Two")):
        session.add(Supplier(supplier_id=sid, company_name_en=name,
                             website_url=f"https://sup-{sid}.ir", status="active"))
    session.commit()
    yield session
    session.close()


def _sync(db_session):
    from src.database.live_sync import LiveSyncEngine
    return LiveSyncEngine(db_session)


def test_structure_and_cas_only_records_merge(db_session):
    """A listing WITH structure and a CAS-only listing of the same chemical
    must become ONE molecule row, not two."""
    sync = _sync(db_session)
    sync.upsert_molecule({
        "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N", "cas_number": "64-17-5",
        "canonical_smiles": "CCO", "title": "Ethanol absolute", "grade": "ACS",
    }, supplier_id=1)
    sync.upsert_molecule({
        "cas_number": "64-17-5", "title": "Ethanol 96%", "grade": "Laboratory",
    }, supplier_id=2)
    sync.commit()

    rows = db_session.execute(select(Molecule)).scalars().all()
    ethanol = [m for m in rows if m.cas_number == "64-17-5"]
    assert len(ethanol) == 1, "same chemical split into multiple molecule rows"
    mol = ethanol[0]
    assert mol.source_identity.startswith("inchikey:")
    assert mol.inchi_key == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"
    assert len(mol.offerings) == 2


def test_same_chemical_different_titles_merge_via_normalized_fallback(db_session):
    """Titles differing only in pack size / parentheses share ONE fallback
    identity (molecule-level dedup; grade stays on the offerings)."""
    sync = _sync(db_session)
    sync.upsert_molecule({
        "title": "Acetone 99% 1 lit", "molecular_formula": "C3H6O",
        "grade": "Laboratory",
    }, supplier_id=1)
    sync.upsert_molecule({
        "title": "acetone (1 L)", "molecular_formula": "C3H6O",
        "grade": "HPLC",
    }, supplier_id=2)
    sync.commit()

    rows = db_session.execute(
        select(Molecule).where(Molecule.molecular_formula == "C3H6O")
    ).scalars().all()
    assert len(rows) == 1, f"fallback fragmentation: {len(rows)} rows"
    assert len(rows[0].offerings) == 2
    grades = sorted(o.grade for o in rows[0].offerings)
    assert "HPLC" in grades and "Laboratory" in grades


def test_two_product_codes_create_two_offerings(db_session):
    """Distinct supplier product codes must become TWO offerings with the
    codes persisted — never one overwriting the other."""
    sync = _sync(db_session)
    for code in ("100983", "100986"):
        sync.upsert_molecule({
            "cas_number": "67-64-1", "title": "Acetone",
            "supplier_product_code": code, "grade": "HPLC Grade",
        }, supplier_id=1)
    sync.commit()

    mol = db_session.execute(
        select(Molecule).where(Molecule.cas_number == "67-64-1")
    ).scalar_one()
    offs = db_session.execute(
        select(SupplierOffering).where(SupplierOffering.molecule_id == mol.molecule_id,
                                       SupplierOffering.supplier_id == 1)
    ).scalars().all()
    assert len(offs) == 2, "product codes collapsed into one offering"
    codes = sorted(o.supplier_product_code for o in offs)
    assert codes == ["100983", "100986"]


def test_invalid_cas_never_stored(db_session):
    sync = _sync(db_session)
    sync.upsert_molecule({
        "cas_number": "64-17-6", "title": "Something with a bad CAS",
        "grade": "Laboratory",
    }, supplier_id=1)
    sync.commit()
    mol = db_session.execute(
        select(Molecule).where(Molecule.source_identity.ilike("fallback-%"))
    ).scalars().all()
    assert all(m.cas_number is None for m in mol)
    bad = db_session.execute(
        select(Molecule).where(Molecule.cas_number == "64-17-6")
    ).scalars().all()
    assert bad == []


def test_validator_writes_back_validated_cas():
    from src.parser.chemical_validator import ChemicalValidator
    v = ChemicalValidator(resolve_cas=False)
    out = v.validate({"title": "x", "cas_number": " 64-17-5 ",
                      "canonical_smiles": "CCO"})
    assert out["cas_number"] == "64-17-5"
    out2 = v.validate({"title": "x", "cas_number": "64-17-6",
                       "canonical_smiles": "CCO"})
    assert out2["cas_number"] is None
    assert "invalid-cas" in out2["_validation_problems"]


def test_cas_resolution_enriches_when_enabled(monkeypatch):
    from src.parser import chemical_validator as cv
    cv.clear_resolution_cache()
    monkeypatch.setattr(cv, "_resolve_cas_structure",
                        lambda cas: {"canonical_smiles": "CCO",
                                     "inchi_key": "LFQSCWFLJHTTHZ-UHFFFAOYSA-N",
                                     "molecular_formula": "C2H6O",
                                     "molecular_weight": 46.07,
                                     "pubchem_cid": 702})
    v = cv.ChemicalValidator(resolve_cas=True)
    out = v.validate({"title": "Ethanol", "cas_number": "64-17-5"})
    assert out["inchi_key"] == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"
    assert out["molecular_formula"] == "C2H6O"
    # and the identity derived from it is the InChIKey identity
    from src.database.identity import build_source_identity
    ident, ik = build_source_identity(out, supplier_id=1)
    assert ident.startswith("inchikey:") and ik == "LFQSCWFLJHTTHZ-UHFFFAOYSA-N"


def test_url_to_mirror_path_blocks_traversal():
    import pytest as _pytest
    from src.crawler.playwright_fallback import PlaywrightFallbackEngine
    with _pytest.raises(ValueError):
        PlaywrightFallbackEngine.url_to_mirror_path(
            "https://evil.com/../../etc/passwd", "/tmp/mirror")
    with _pytest.raises(ValueError):
        PlaywrightFallbackEngine.url_to_mirror_path(
            "https://user:pass@evil.com/ok.html", "/tmp/mirror")
    p = PlaywrightFallbackEngine.url_to_mirror_path(
        "https://shop.ir/catalog/item.html", "/tmp/mirror")
    assert str(p).startswith("/tmp/mirror/shop.ir/")


def test_js_catalogue_listener_registered_once():
    """The response listener must be registered once per page, not per URL."""
    src = open("src/crawler/js_catalogue.py", encoding="utf-8").read()
    capture_fn = src[src.index("async def capture_json_responses"):]
    body_until = capture_fn[:capture_fn.index("async def _follow_pagination")] \
        if "async def _follow_pagination" in capture_fn else capture_fn
    # exactly one registration
    assert body_until.count('page.on("response"') == 1
    assert "saved_limit" not in src  # dead indirection removed
