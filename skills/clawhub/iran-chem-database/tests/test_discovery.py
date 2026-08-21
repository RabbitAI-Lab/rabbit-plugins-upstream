"""Tests for the discovery engine + seed list + validator."""
from src.discovery.engine import SupplierDiscoveryEngine, DISCOVERY_QUERIES
from src.discovery.seed_list import DIRECTORY_SEEDS, SUPPLIER_SEEDS
from src.discovery.validator import SupplierValidator


def test_seed_list_size():
    assert len(SUPPLIER_SEEDS) >= 30   # spec lists 35 direct suppliers
    assert len(DIRECTORY_SEEDS) >= 15  # spec lists 15 B2B directories


def test_seed_candidates_have_urls():
    engine = SupplierDiscoveryEngine()
    candidates = engine.seed_suppliers()
    assert all(c.url.startswith("http") for c in candidates)


def test_persian_queries_present():
    assert any("شیمیایی" in q for q in DISCOVERY_QUERIES)
    assert any("Iran chemical supplier" in q for q in DISCOVERY_QUERIES)


def test_validator_scores_ir_domain():
    v = SupplierValidator()
    score = v.score("https://example.ir")
    assert score >= 40  # .ir TLD alone


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
