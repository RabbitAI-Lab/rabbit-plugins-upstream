"""Seed list — known Iranian chemical suppliers & B2B directories.

v2.5: entries are dicts (not bare (name, url) tuples) carrying a fingerprint
derived from a 2026-08 live probe of every URL:

  * status    — "active" | "inactive" (dead/parked/no-molecule-catalog)
  * profile   — crawl profile hint: woo_rest | sitemap_wp | playwright_js |
                httrack_deep | static_html | pdf_catalog | skip_*
  * notes     — why (geo-blocked, WAF, etc.)
  * entry_points — concrete REST/sitemap/catalog URLs to try first

v2.6.1: each geo-blocked entry also carries `free_access_methods` — the
field-verified ordered list of free fetchers that actually reach that site
(jina / wayback / translate / archivetoday). This lets the crawler skip
dead/parked domains immediately, route WooCommerce storefronts to the public
REST API, and read geo-blocked hosts through the working free front-ends.
"""
from __future__ import annotations

from urllib.parse import urlparse

# name, url, status, profile, notes, entry_points, (optional) free_access_methods
SUPPLIER_SEEDS = [
    {"name": "Chemical Iran", "url": "https://www.chemicaliran.com",
     "status": "active", "profile": "woo_rest",
     "notes": "WordPress/WooCommerce behind BitNinja WAF; slow rate, browser UA",
     "entry_points": ["https://www.chemicaliran.com/wp-json/wc/store/v1/products",
                      "https://www.chemicaliran.com/sitemap.xml"]},
    {"name": "Iran Petrochemical", "url": "https://www.iranpetrochemical.net",
     "status": "active", "profile": "sitemap_wp",
     "notes": "WordPress/WooCommerce (nginx); sitemap.xml + product categories",
     "entry_points": ["https://www.iranpetrochemical.net/wp-json/wc/store/v1/products",
                      "https://www.iranpetrochemical.net/sitemap.xml"]},
    {"name": "Rock Chemie Co.", "url": "https://www.rockchemie.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP (TLS handshake fail); needs Iranian proxy",
     "entry_points": [],
     "free_access_methods": ["jina", "wayback", "commoncrawl", "translate"]},
    {"name": "ArChem", "url": "https://www.archemco.com",
     "status": "active", "profile": "woo_rest",
     "notes": "WordPress/WooCommerce (Apache/2); raw chemical materials",
     "entry_points": ["https://www.archemco.com/wp-json/wc/store/v1/products"]},
    {"name": "Abnoos Chemical Complex", "url": "https://www.abnoos.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy",
     "entry_points": [],
     "free_access_methods": ["jina", "wayback", "translate"]},
    {"name": "Puricals", "url": "https://www.puricals.com",
     "status": "inactive", "profile": "skip_inorganic",
     "notes": "Water/wastewater treatment chems (PAC, FeCl3, Al2(SO4)3, NaOCl, HCl, NaOH) — mostly INORGANIC, no research-grade organic catalog",
     "entry_points": []},
    {"name": "Cadoos International Petrochemical (INTPCC)", "url": "https://www.cadoos.com",
     "status": "inactive", "profile": "skip_parked",
     "notes": "Domain PARKED / for sale (HugeDomains)",
     "entry_points": []},
    {"name": "DPPC / Pharma Chem", "url": "https://www.dppc.ir",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Pars Gilsonite Reshad Co.", "url": "https://www.parsgilsonite.com",
     "status": "active", "profile": "static_html",
     "notes": "Static site; single product line (gilsonite / natural bitumen)",
     "entry_points": []},
    {"name": "Artin Kimya", "url": "https://www.artinkimya.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy",
     "entry_points": [],
     "free_access_methods": ["jina", "wayback", "translate"]},
    {"name": "Novichem Co.", "url": "https://www.novichem.ir",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy; hardest-blocked — Jina/Translate both fail, Wayback + Common Crawl only",
     "entry_points": [],
     "free_access_methods": ["wayback", "commoncrawl"]},
    {"name": "Karina Polymer", "url": "https://www.karinapolymer.com",
     "status": "active", "profile": "woo_rest",
     "notes": "WordPress/WooCommerce; polymer compounds; JSON-LD",
     "entry_points": ["https://www.karinapolymer.com/wp-json/wc/store/v1/products"]},
    {"name": "BASPARSAZAN IRANIAN Company", "url": "https://www.basparsazan.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy",
     "entry_points": [],
     "free_access_methods": ["jina", "translate"]},
    {"name": "Paksho Industrial Group", "url": "https://www.pakshoo.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy; consumer/industrial group",
     "entry_points": [],
     "free_access_methods": ["jina", "wayback", "translate"]},
    {"name": "ASCO", "url": "https://www.asco.co.ir",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Mahdis Tejarat Trading Company", "url": "https://www.mahdistejarat.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy; trading company; weak free access — Wayback + Common Crawl",
     "entry_points": [],
     "free_access_methods": ["wayback", "commoncrawl"]},
    {"name": "Chemical Mine World Co.", "url": "https://www.chemicalmineworld.com",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Lazak Mehregan International Commercial Co.", "url": "https://www.lazakmehregan.com",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Akbarieh Company", "url": "https://www.akbarieh.com",
     "status": "active", "profile": "woo_rest",
     "notes": "WordPress/WooCommerce (Apache)",
     "entry_points": ["https://www.akbarieh.com/wp-json/wc/store/v1/products"]},
    {"name": "Gulf Petrochemical", "url": "https://www.gulfpetrochemical.com",
     "status": "active", "profile": "httrack_deep",
     "notes": "No CMS signature on first page; custom PHP likely — deep mirror",
     "entry_points": []},
    {"name": "Fluid Tamin Rahaam Company", "url": "https://www.fluidtamin.com",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Pars Isotope Co.", "url": "https://www.parsisotope.com",
     "status": "inactive", "profile": "skip_no_catalog",
     "notes": "RADIOPHARMACEUTICAL kits (MIBI, Lu-177-PSMA, MDP, generators) — not a molecule catalog",
     "entry_points": []},
    {"name": "Pishtaz Teb Zaman Diagnostics", "url": "https://www.pishtazteb.com",
     "status": "active", "profile": "woo_rest",
     "notes": "WordPress/WooCommerce /shop/; IVD kits (ELISA, biochemistry, molecular, rapid tests)",
     "entry_points": ["https://www.pishtazteb.com/wp-json/wc/store/v1/products"]},
    {"name": "Raeis Industrial Group", "url": "https://www.raeisgroup.com",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Barzin International Group", "url": "https://www.barzingroup.com",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "ATDM", "url": "https://www.atdm.ir",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Mobtakeran Shimi", "url": "https://www.mobtakeranshimi.com",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Teb Gostar Noor Pars", "url": "https://www.tebgostar.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy; lab equipment & chemicals",
     "entry_points": [],
     "free_access_methods": ["jina", "translate", "wayback"]},
    {"name": "Kimia Eksir Company", "url": "https://www.kimiaeksir.com",
     "status": "inactive", "profile": "skip_dead",
     "notes": "Domain does not resolve (DNS fail)",
     "entry_points": []},
    {"name": "Mojallali Group", "url": "https://www.drm-chem.com",
     "status": "active", "profile": "sitemap_wp",
     "notes": "WordPress/WooCommerce; 427 products; EN/FA; per-product PDF datasheet/CoA/SDS; ACS/USP/BP/EP grades",
     "entry_points": ["https://www.drm-chem.com/wp-json/wc/store/v1/products",
                      "https://www.drm-chem.com/sitemap_index.xml",
                      "https://www.drm-chem.com/product-sitemap.xml"]},
    {"name": "Exir Pharmaceutical Co.", "url": "https://www.exir.co.ir",
     "status": "active", "profile": "woo_rest",
     "notes": "WordPress/WooCommerce /shop/; finished pharma (tablets, syrups, antibiotics, sterile)",
     "entry_points": ["https://www.exir.co.ir/wp-json/wc/store/v1/products",
                      "https://www.exir.co.ir/shop/"]},
    {"name": "Sobhan Oncology", "url": "https://www.sobhanoncology.ir",
     "status": "active", "profile": "playwright_js",
     "notes": "Custom site behind WCDN WAF; JS-rendered catalog — Playwright + XHR capture",
     "entry_points": []},
    {"name": "Iran Daru Pharmaceutical", "url": "https://www.irandaru.com",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy; pharma",
     "entry_points": [],
     "free_access_methods": ["jina", "wayback", "commoncrawl", "translate"]},
    {"name": "Temad", "url": "https://www.temad.com",
     "status": "active", "profile": "woo_rest",
     "notes": "WordPress/WooCommerce API catalog /product-category/api_fa/*; 26 export APIs; 15 knowledge-based; pharma APIs (addiction, diabetes, corticosteroids, CV, antibiotics, CNS…)",
     "entry_points": ["https://www.temad.com/wp-json/wc/store/v1/products",
                      "https://www.temad.com/product-category/api_fa/"]},
    {"name": "Persian Gulf Star Oil Company", "url": "https://www.pgsoc.ir",
     "status": "active", "profile": "static_html",
     "notes": "GEO-BLOCKED from foreign IP; needs Iranian proxy; refinery/petrochemical; Wayback + Common Crawl only",
     "entry_points": [],
     "free_access_methods": ["wayback", "commoncrawl"]},
]

DIRECTORY_SEEDS = [
    "https://www.shimico.com/companies/",
    "https://www.b2bmap.com/iran",
    "https://www.lookchem.com/iran/",
    "https://www.chemnet.com/iran/",
    "https://www.chemicals1.com/iran",
    "https://www.chemicalbusinessdirectory.com/iran",
    "https://www.ensun.io/chemical-manufacturing/iran",
    "https://www.volza.com/iran-reagent-exporters",
    "https://www.kompass.com/iran/chemicals",
    "https://www.tradeford.com/iran-chemicals",
    "https://www.exporthub.com/iran-chemicals",
    "https://www.alibaba.com/iran-chemicals",
    "https://www.tradewheel.com/iran/chemicals",
    "https://www.ec21.com/iran-chemicals",
    "https://www.made-in-china.com/iran-chemicals",
]


def free_access_preference(url: str) -> list:
    """Return the ordered free-access method list for a supplier URL.

    v2.6.1: each geo-blocked seed site carries a field-verified method
    preference (e.g. novichem.ir is Wayback-only; artinkimya.com works with
    jina+wayback+translate). Unknown domains fall back to
    DEFAULT_FREE_ACCESS_METHODS from src/crawler/free_access_engine.
    """
    from src.crawler.free_access_engine import DEFAULT_FREE_ACCESS_METHODS
    host = (urlparse(url).netloc or url).replace("www.", "").lower()
    for item in SUPPLIER_SEEDS:
        item_host = (urlparse(item["url"]).netloc or "").replace("www.", "").lower()
        if host and host == item_host:
            pref = item.get("free_access_methods") or DEFAULT_FREE_ACCESS_METHODS
            break
    else:
        pref = DEFAULT_FREE_ACCESS_METHODS
    # v2.7.1: SPN2 forces a fresh capture and works for every site (the IA
    # crawler fetches from allowed IPs) — append it when a site does not list it.
    if "spn2" not in pref:
        pref = list(pref) + ["spn2"]
    return pref
