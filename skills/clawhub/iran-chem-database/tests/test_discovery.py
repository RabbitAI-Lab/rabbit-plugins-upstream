"""Tests for the discovery engine + seed list + validator."""
from src.discovery.engine import SupplierDiscoveryEngine, DISCOVERY_QUERIES
from src.discovery.seed_list import DIRECTORY_SEEDS, SUPPLIER_SEEDS
from src.discovery.validator import SupplierValidator


def test_seed_list_size():
    assert len(SUPPLIER_SEEDS) >= 58   # spec lists 58 direct suppliers (v2.21)
    assert len(DIRECTORY_SEEDS) >= 15  # spec lists 15 B2B directories


def test_seed_candidates_have_urls():
    engine = SupplierDiscoveryEngine()
    candidates = engine.seed_suppliers()
    assert all(c.url.startswith("http") for c in candidates)


def test_persian_queries_present():
    assert any("شیمیایی" in q for q in DISCOVERY_QUERIES)
    assert any("Iran chemical supplier" in q for q in DISCOVERY_QUERIES)


def test_validator_ir_domain_alone_is_insufficient():
    """v2.11: a .ir TLD alone no longer admits a supplier.

    Country-of-origin best practice requires cross-referencing at least two
    INDEPENDENT signals, so a bare ccTLD (with an unreachable/empty homepage
    contributing no further evidence) must score 0 rather than 40.
    """
    v = SupplierValidator()
    assert v.score("https://example.ir") == 0.0


def test_validator_ir_domain_plus_second_signal_is_admitted(monkeypatch):
    """…but a .ir domain corroborated by Iranian contact details is admitted."""
    v = SupplierValidator()
    monkeypatch.setattr(
        v, "_fetch_homepage",
        lambda url: "مواد شیمیایی reagent تهران ایران تلفن 021-88776655")
    assert v.score("https://example.ir") >= 60


def test_validator_scores_empty_zero():
    assert SupplierValidator().score("") == 0.0


def test_academic_citation_extraction():
    engine = SupplierDiscoveryEngine()
    texts = ["All reagents were purchased from Pars Isotope Co. (Karaj, Iran) and used as received."]
    found = engine.discover_via_academic_citations(texts)
    assert found and found[0].name.strip() == "Pars Isotope Co."


def test_business_registry_isic_filter():
    engine = SupplierDiscoveryEngine()
    rows = [
        {"name": "ChemCo", "isic_code": "2011", "website": "https://chemco.ir"},
        {"name": "Bakery", "isic_code": "1071", "website": "https://bakery.ir"},
    ]
    found = engine.discover_via_iran_business_registries(rows)
    assert len(found) == 1
    assert found[0].name == "ChemCo"
