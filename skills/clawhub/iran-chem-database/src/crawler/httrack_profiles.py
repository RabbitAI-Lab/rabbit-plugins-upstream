"""Pre-built HTTrack profile templates per supplier type (spec §3.2)."""
from __future__ import annotations

from src.crawler.httrack_config import HTTRACK_BASE_DIR, HTTrackMirrorConfig


class HTTrackProfiles:
    @staticmethod
    def standard_catalog_site(supplier_id: int, name: str, url: str) -> HTTrackMirrorConfig:
        return HTTrackMirrorConfig(
            supplier_id=supplier_id, project_name=name, urls=[url],
            output_dir=f"{HTTRACK_BASE_DIR}/{name}",
            depth=5, connections_per_second=2.0, sockets=4, max_rate=50000,
        )

    @staticmethod
    def pdf_catalog_site(supplier_id: int, name: str, url: str) -> HTTrackMirrorConfig:
        config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        # NOTE: legacy binary .doc is NOT parsed by the pipeline (fix guide
        # §5.4) and is therefore not advertised here; .docx IS supported.
        config.include_filters = ["+*.pdf", "+*.html", "+*.htm", "+*.xlsx", "+*.xls", "+*.csv", "+*.docx"]
        config.depth = 3
        return config

    @staticmethod
    def large_database_site(supplier_id: int, name: str, url: str) -> HTTrackMirrorConfig:
        config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        config.depth = 8
        config.max_time = 14400
        config.connections_per_second = 1.0
        config.sockets = 2
        return config

    @staticmethod
    def sensitive_site(supplier_id: int, name: str, url: str) -> HTTrackMirrorConfig:
        config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        config.connections_per_second = 0.5
        config.sockets = 1
        config.max_rate = 10000
        config.extra_flags = ["--min-rate=0", "-G", "2:8"]
        return config

    @staticmethod
    def login_required_site(supplier_id: int, name: str, url: str, cookies: str) -> HTTrackMirrorConfig:
        config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        config.extra_flags = [f"--cookies={cookies}"]
        return config

    @staticmethod
    def ir_domain_site(supplier_id: int, name: str, url: str) -> HTTrackMirrorConfig:
        config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        config.extra_flags = ["--charset=UTF-8", "--assume", "asp,php,aspx=text/html"]
        return config

    @staticmethod
    def js_catalogue_site(supplier_id: int, name: str, url: str) -> HTTrackMirrorConfig:
        """JS/API-driven storefronts: shallow HTTrack shell + Playwright capture."""
        config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        config.depth = 1
        config.max_time = 1800
        config.connections_per_second = 1.0
        config.sockets = 1
        config.extra_flags = ["--assume", "asp,php,aspx=text/html"]
        return config

    @staticmethod
    def woo_rest_site(supplier_id: int, name: str, url: str) -> HTTrackMirrorConfig:
        """v2.5: shallow HTTrack mirror for a WooCommerce/WordPress storefront.

        Product data comes from the public REST API / sitemap (see
        src/crawler/woo_rest_engine.py); the shallow mirror only captures HTML
        grade/purity/description text that the API does not expose."""
        config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        config.depth = 2
        config.max_time = 1800
        config.connections_per_second = 1.0
        config.sockets = 2
        return config

    @staticmethod
    def classify_profile(supplier_type: str | None, url: str) -> str:
        """Onboarding classification of a supplier's catalogue format (fix
        guide §6.3): static_html | paginated_database | pdf_excel_catalogue |
        js_catalogue | login_required | no_public_catalogue | blocked."""
        slug = (supplier_type or "").lower()
        if slug in ("login-required", "login_required"):
            return "login_required"
        if "pdf" in slug or "excel" in slug:
            return "pdf_excel_catalogue"
        # v2.5: WooCommerce/WordPress storefronts route to the REST engine
        # (sitemap_wp additionally enumerates sitemap product URLs).
        if "woocommerce" in slug or "woo" in slug or "wordpress" in slug:
            return "woo_rest"
        if "sitemap" in slug:
            return "sitemap_wp"
        if slug in ("marketplace", "large-catalog", "manufacturer"):
            return "paginated_database"
        if "js" in slug or "playwright" in slug:
            return "js_catalogue"
        if url and (url.endswith(".ir") or ".ir/" in url):
            return "static_html"
        return "static_html"

    @staticmethod
    def for_supplier(supplier_type: str, supplier_id: int, name: str, url: str,
                     requires_playwright: bool = False, cookies: str | None = None,
                     profile: str | None = None) -> HTTrackMirrorConfig:
        """Auto-select a profile from supplier metadata or explicit profile."""
        if profile == "js_catalogue" or requires_playwright:
            config = HTTrackProfiles.js_catalogue_site(supplier_id, name, url)
        elif profile in ("woo_rest", "sitemap_wp"):
            # v2.5: WooCommerce/WordPress storefronts are fetched via the
            # public REST API + sitemap (src/crawler/woo_rest_engine.py);
            # HTTrack still runs a shallow mirror for HTML/grade text.
            config = HTTrackProfiles.woo_rest_site(supplier_id, name, url)
        elif profile == "pdf_excel_catalogue":
            config = HTTrackProfiles.pdf_catalog_site(supplier_id, name, url)
        elif profile == "paginated_database":
            config = HTTrackProfiles.large_database_site(supplier_id, name, url)
        elif profile == "login_required":
            config = HTTrackProfiles.login_required_site(supplier_id, name, url, cookies or "")
        else:
            slug = (supplier_type or "").lower()
            if "pdf" in slug:
                config = HTTrackProfiles.pdf_catalog_site(supplier_id, name, url)
            elif slug in ("manufacturer", "marketplace") and name and requires_playwright:
                config = HTTrackProfiles.large_database_site(supplier_id, name, url)
            elif url.endswith(".ir") or ".ir/" in url:
                config = HTTrackProfiles.ir_domain_site(supplier_id, name, url)
            else:
                config = HTTrackProfiles.standard_catalog_site(supplier_id, name, url)
        if cookies:
            config.extra_flags.append(f"--cookies={cookies}")
        return config
