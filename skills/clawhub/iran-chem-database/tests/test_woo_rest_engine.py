"""v2.5 regression tests — WooCommerce REST engine, seed metadata, profiles."""
from src.crawler.httrack_profiles import HTTrackProfiles
from src.crawler.woo_rest_engine import WooRESTEngine
from src.discovery.engine import SupplierDiscoveryEngine
from src.discovery.seed_list import SUPPLIER_SEEDS


def test_seed_list_is_fingerprinted():
    """Every seed entry must be a dict carrying status + profile + notes."""
    for item in SUPPLIER_SEEDS:
        assert isinstance(item, dict), f"expected dict, got {item!r}"
        assert item["url"].startswith("http")
        assert item["status"] in ("active", "inactive")
        assert "profile" in item
        assert "notes" in item


def test_dead_domains_are_inactive():
    inactive = {s["url"]: s for s in SUPPLIER_SEEDS if s["status"] == "inactive"}
    # fingerprint evidence: these domains no longer resolve / are parked /
    # carry no molecule catalog
    for dead in ("https://www.cadoos.com", "https://www.asco.co.ir",
                 "https://www.dppc.ir", "https://www.atdm.ir"):
        assert dead in inactive, f"{dead} should be seeded inactive"


def test_woocommerce_sites_get_woo_rest_profile():
    woo = {s["url"]: s for s in SUPPLIER_SEEDS if s["profile"] in ("woo_rest", "sitemap_wp")}
    for u in ("https://www.temad.com", "https://www.drm-chem.com",
              "https://www.chemicaliran.com", "https://www.iranpetrochemical.net"):
        assert u in woo, f"{u} should route to the REST/sitemap engine"


def test_v220_research_grade_gap_sellers_are_seeded():
    """v2.20–v2.21: live-probed research-grade sellers must stay admitted."""
    by_url = {s["url"]: s for s in SUPPLIER_SEEDS}
    expected = {
        "https://hsdlifescience.com": "sitemap_wp",
        "https://imengostarshimi.com": "static_html",
        "https://nirvanashimi.com": "woo_rest",
        "https://arzanazma.com": "woo_rest",
        "https://novashimi.ir": "static_html",
        "https://shimimerck.ir": "sitemap_wp",
        "https://radkimia.ir": "static_html",
        "https://www.neutronpharmachemical.com": "static_html",
    }
    geo_blocked = {
        "https://hsdlifescience.com", "https://imengostarshimi.com",
        "https://nirvanashimi.com", "https://arzanazma.com",
        "https://novashimi.ir", "https://radkimia.ir",
    }
    for url, profile in expected.items():
        assert url in by_url, f"{url} missing from SUPPLIER_SEEDS"
        item = by_url[url]
        assert item["status"] == "active"
        assert item["profile"] == profile
        if url in geo_blocked:
            assert item.get("free_access_methods"), f"{url} needs free_access_methods (geo-blocked)"


def test_seed_candidates_carry_metadata():
    engine = SupplierDiscoveryEngine()
    cands = {c.url: c for c in engine.seed_suppliers()}
    temad = cands["https://www.temad.com"]
    assert temad.extra["profile"] == "woo_rest"
    assert temad.extra["status"] == "active"
    assert temad.extra["entry_points"], "Temad should have REST entry points"


def test_classify_profile_maps_woocommerce():
    assert HTTrackProfiles.classify_profile("woocommerce", "https://x.com") == "woo_rest"
    assert HTTrackProfiles.classify_profile("wordpress-woo", "https://x.com") == "woo_rest"
    assert HTTrackProfiles.classify_profile("sitemap", "https://x.com") == "sitemap_wp"
    assert HTTrackProfiles.classify_profile("distributor", "https://x.ir") == "static_html"


def test_for_supplier_woo_profile_is_shallow():
    cfg = HTTrackProfiles.for_supplier("woocommerce", 1, "acme", "https://acme.com",
                                       profile="woo_rest")
    assert cfg.depth == 2
    assert cfg.connections_per_second == 1.0


def test_sitemap_parse_keeps_product_urls():
    xml = b"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://x.com/product/methanol/</loc></url>
  <url><loc>https://x.com/product-category/solvents/</loc></url>
  <url><loc>https://x.com/about/</loc></url>
</urlset>"""
    urls = WooRESTEngine._parse_sitemap(xml)
    # product page kept; category + about filtered out
    assert any("/product/methanol" in u for u in urls)
    assert not any("product-category" in u for u in urls)
    assert not any("/about/" in u for u in urls)
