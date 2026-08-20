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
        config.include_filters = ["+*.pdf", "+*.html", "+*.htm", "+*.xlsx", "+*.xls", "+*.csv", "+*.doc", "+*.docx"]
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
    def for_supplier(supplier_type: str, supplier_id: int, name: str, url: str,
                     requires_playwright: bool = False, cookies: str | None = None) -> HTTrackMirrorConfig:
        """Auto-select a profile from supplier metadata."""
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
