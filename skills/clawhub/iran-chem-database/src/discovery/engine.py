"""SupplierDiscoveryEngine — autonomously discovers Iranian chemical suppliers.

Methods (spec §2.2): search engines, B2B directory crawling via HTTrack, link
analysis of mirrored sites, academic citations, and business registries.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import List, Optional

from src.discovery.seed_list import DIRECTORY_SEEDS, SUPPLIER_SEEDS
from src.discovery.directory_crawler import DirectoryCrawler
from src.discovery.link_analyzer import LinkAnalyzer
from src.discovery.search_engine_discovery import SearchEngineDiscovery
from src.discovery.validator import SupplierValidator

logger = logging.getLogger(__name__)

DISCOVERY_QUERIES = [
    "Iran chemical supplier research grade",
    "Iranian laboratory chemicals supplier",
    "Iran research chemical reagent supplier",
    "خرید مواد شیمیایی آزمایشگاهی ایران",
    "فروش مواد شیمیایی تحقیقاتی",
    "تامین کننده مواد شیمیایی ایران",
    "شرکت مواد شیمیایی آزمایشگاهی تهران",
    "کاتالوگ مواد شیمیایی",
]


@dataclass
class SupplierCandidate:
    url: str
    source: str
    confidence: float = 0.0
    name: Optional[str] = None
    extra: dict = field(default_factory=dict)


class SupplierDiscoveryEngine:
    def __init__(self, mirror_base_dir: str = "/var/lib/iran_chem_db/mirrors"):
        self.validator = SupplierValidator()
        self.directory_crawler = DirectoryCrawler(mirror_base_dir)
        self.link_analyzer = LinkAnalyzer()
        self.search_engine = SearchEngineDiscovery()

    # ── seed list ─────────────────────────────────────────────────────────
    def seed_suppliers(self) -> List[SupplierCandidate]:
        """Return the seed cohort with fingerprint metadata (v2.5).

        Each candidate's `extra` carries status / crawl-profile / notes /
        entry_points so the seeder can persist them and the crawler can skip
        dead domains and route WooCommerce sites to the REST engine."""
        out: List[SupplierCandidate] = []
        for item in SUPPLIER_SEEDS:
            cand = SupplierCandidate(url=item["url"], source="seed", name=item["name"])
            cand.extra = {
                "status": item.get("status", "active"),
                "profile": item.get("profile"),
                "notes": item.get("notes", ""),
                "entry_points": item.get("entry_points") or [],
            }
            out.append(cand)
        return out

    def seed_directories(self) -> List[SupplierCandidate]:
        return [SupplierCandidate(url=u, source="directory-seed") for u in DIRECTORY_SEEDS]

    # ── discovery methods ─────────────────────────────────────────────────
    def discover_via_search_engines(self, queries: Optional[List[str]] = None) -> List[SupplierCandidate]:
        found: List[SupplierCandidate] = []
        for query in (queries or DISCOVERY_QUERIES):
            for url in self.search_engine.search(query):
                found.append(SupplierCandidate(url=url, source="search_engine"))
        return found

    def discover_via_directory_crawling_httrack(self, directories: Optional[List[str]] = None,
                                               timeout: int = 120, max_directories: Optional[int] = None) -> List[SupplierCandidate]:
        """Bounded directory discovery (remediation §2): short per-directory
        timeouts, optional cap on the number of directories per run."""
        from src.config import get_config
        cfg = get_config().as_dict().get("discovery", {}) or {}
        timeout = timeout or int(cfg.get("directory_timeout_seconds", 120))
        if max_directories is None:
            max_directories = int(cfg.get("max_directories_per_run", 3))
        urls: List[str] = []
        for directory_url in (directories or DIRECTORY_SEEDS)[:max_directories]:
            result = self.directory_crawler.mirror_directory(directory_url, timeout=timeout)
            if result.get("timed_out"):
                continue
            urls.extend(self.directory_crawler.extract_supplier_urls(result.get("output_dir", "")))
        return [SupplierCandidate(url=u, source="directory") for u in dict.fromkeys(urls)]

    def discover_via_link_analysis(self, mirror_dir: str) -> List[SupplierCandidate]:
        urls = self.link_analyzer.analyze_mirror(mirror_dir)
        return [SupplierCandidate(url=u, source="link_analysis") for u in urls]

    def discover_via_academic_citations(self, texts: List[str]) -> List[SupplierCandidate]:
        """Extract supplier mentions from paper acknowledgments.

        Pattern: 'reagents were purchased from [SUPPLIER] (Tehran, Iran)'.
        """
        import re
        found: List[SupplierCandidate] = []
        pattern = re.compile(
            r"(?:purchased from|obtained from|supplied by|from)\s+([A-Z][A-Za-z&.\- ]{3,60})"
            r"\s*\(?(?:Tehran|Isfahan|Karaj|Mashhad|Tabriz|Shiraz)?[^)]*Iran",
            re.I,
        )
        for text in texts:
            for m in pattern.findall(text):
                found.append(SupplierCandidate(url="", source="academic_citation", name=m.strip()))
        return found

    def discover_via_iran_business_registries(self, registry_data: List[dict]) -> List[SupplierCandidate]:
        """Filter business-registry rows for chemical wholesale/retail ISIC codes."""
        chem_codes = ("20", "2011", "2012", "2029", "46", "4646", "4675", "21", "2110", "2120")
        found: List[SupplierCandidate] = []
        for row in registry_data:
            isic = str(row.get("isic_code", ""))
            url = row.get("website", "")
            if any(isic.startswith(c) for c in chem_codes) and url:
                found.append(SupplierCandidate(url=url, source="business_registry",
                                               name=row.get("name"), extra={"isic": isic}))
        return found

    # ── validation & full run ─────────────────────────────────────────────
    def validate_supplier(self, url: str) -> float:
        return self.validator.score(url)

    @staticmethod
    def _normalize_url(url: str) -> str:
        """Normalize a URL to scheme://netloc for stable deduplication."""
        from urllib.parse import urlparse
        parsed = urlparse(url if "://" in url else f"https://{url}")
        if parsed.scheme in ("http", "https") and parsed.netloc:
            return f"{parsed.scheme}://{parsed.netloc.lower()}"
        return url

    def run_full_discovery(self) -> List[SupplierCandidate]:
        """Weekly mega-sweep: seeds + search engines + directory crawling."""
        candidates: List[SupplierCandidate] = []
        candidates += self.seed_suppliers()
        candidates += self.discover_via_search_engines()
        candidates += self.discover_via_directory_crawling_httrack()

        scored: List[SupplierCandidate] = []
        rejected_foreign: List[SupplierCandidate] = []
        seen_urls = set()
        for cand in candidates:
            if not cand.url:
                continue
            cand.url = self._normalize_url(cand.url)
            if cand.url in seen_urls:
                continue
            seen_urls.add(cand.url)
            score, verdict, _ = self.validator.verify(cand.url)
            cand.confidence = score
            # v2.11: carry auditable country provenance on every candidate.
            cand.extra = dict(cand.extra or {})
            cand.extra["country"] = verdict.country
            cand.extra["country_confidence"] = verdict.confidence
            cand.extra["country_evidence"] = [e.as_dict() for e in verdict.evidence]
            cand.extra["country_reason"] = verdict.reason
            cand.extra["country_verified_at"] = verdict.verified_at
            if not verdict.admitted:
                logger.info("discovery: EXCLUDED non-Iranian %s (%s)", cand.url, verdict.reason)
                rejected_foreign.append(cand)
                continue
            scored.append(cand)

        min_score = 60  # spec config.yaml: discovery.min_verification_score
        verified = [c for c in scored if c.confidence >= min_score]
        logger.info("discovery: %d candidates -> %d verified (%d excluded as "
                    "non-Iranian by the country gate)",
                    len(scored) + len(rejected_foreign), len(verified),
                    len(rejected_foreign))
        self.last_rejected_foreign = rejected_foreign
        return verified
