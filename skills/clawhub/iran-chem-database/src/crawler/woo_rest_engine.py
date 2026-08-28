"""WooCommerce REST + sitemap fetch engine (added v2.5).

Field finding (2026-08 fingerprinting of the 35-supplier seed list): the
majority of catalog-carrying Iranian supplier sites are WordPress/WooCommerce
storefronts (Chemical Iran, Iran Petrochemical, ArChem, Karina Polymer,
Akbarieh, Pishtaz Teb, Exir, Temad, Mojallali). Mirroring them with HTTrack is
slow and wasteful — WooCommerce exposes a PUBLIC, unauthenticated product API:

    GET /wp-json/wc/store/v1/products?per_page=100&page=N

This engine fetches that API (with a WordPress core REST fallback) and the
sitemap(s), and writes the raw JSON responses into the supplier's local mirror
directory. The existing, local-file-only JSONCatalogueParser then consumes
them exactly like any other mirrored file — so the "parser never hits the
network" invariant is preserved.

Stdlib only (urllib / json / xml.etree / re / pathlib) — no new dependencies.
Polite by default: browser-like UA, per-page delay, hard page/time budget.
"""
from __future__ import annotations

import json
import logging
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)

DEFAULT_UA = "IranChemDB/2.5 (Research Chemical Database crawler; contact@iranchem.db)"

# Public WooCommerce Store API endpoint (no auth key required).
STORE_API_PATH = "/wp-json/wc/store/v1/products"
# WordPress core REST fallback for a product custom post type (often 404).
WP_PRODUCT_PATH = "/wp-json/wp/v2/product"

SITEMAP_CANDIDATES = (
    "/sitemap.xml",
    "/sitemap_index.xml",
    "/wp-sitemap.xml",
    "/product-sitemap.xml",
    "/products-sitemap.xml",
)

# Product-ish URL tokens used to filter sitemap <loc> entries.
_PRODUCT_TOKENS = ("/product/", "/product?", "/products/", "/محصول", "product_id", "p=")
_SKIP_TOKENS = ("/product-category/", "/category/", "/tag/", "/page/", "/wp-content/", "/shop/")


def _url(path: str, base: str) -> str:
    if path.startswith("http"):
        return path
    return base.rstrip("/") + "/" + path.lstrip("/")


def _get(url: str, timeout: int, user_agent: str) -> bytes:
    """GET with retry/backoff on transient errors (v2.9)."""
    from src.utils.http_util import get_bytes
    return get_bytes(url, timeout=timeout, user_agent=user_agent,
                     accept="application/json, text/html;q=0.9, */*;q=0.8")


class WooRESTEngine:
    def __init__(self, base_dir: str, timeout: int = 30, delay: float = 0.4,
                 max_pages: int = 200, user_agent: str = DEFAULT_UA):
        self.base_dir = Path(base_dir)
        self.timeout = timeout
        self.delay = delay
        self.max_pages = max_pages
        self.user_agent = user_agent

    # ── WooCommerce Store API ──────────────────────────────────────────────
    def fetch_store_api(self, base_url: str, output_dir: str) -> dict:
        """Paginate the public Store API and persist each page as local JSON.

        Returns {"products": N, "pages": P, "endpoint": url} or {"error": ...}.
        """
        out = Path(output_dir) / "woo-api"
        out.mkdir(parents=True, exist_ok=True)
        for endpoint in (STORE_API_PATH, WP_PRODUCT_PATH):
            products = 0
            pages = 0
            for page in range(1, self.max_pages + 1):
                url = _url(endpoint, base_url) + f"?per_page=100&page={page}"
                try:
                    raw = _get(url, self.timeout, self.user_agent)
                except urllib.error.HTTPError as exc:
                    if page == 1 and exc.code in (401, 403, 404):
                        break  # try next endpoint
                    if exc.code == 400:  # ran past the last page (or bad params)
                        break
                    logger.warning("Store API %s HTTP %s (page %s)", endpoint, exc.code, page)
                    break
                except Exception as exc:  # noqa: BLE001
                    logger.warning("Store API %s failed: %s", endpoint, exc)
                    break
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError:
                    break
                items = data if isinstance(data, list) else data.get("products", []) or []
                if not items:
                    break
                (out / f"page-{page:04d}.json").write_text(
                    json.dumps(items, ensure_ascii=False), "utf-8")
                products += len(items)
                pages += 1
                if len(items) < 100:
                    break
                time.sleep(self.delay)
            if pages:
                return {"products": products, "pages": pages,
                        "endpoint": _url(endpoint, base_url)}
        return {"products": 0, "pages": 0, "error": "store-api-unavailable"}

    # ── Sitemap enumeration ────────────────────────────────────────────────
    def fetch_sitemap(self, base_url: str, output_dir: str) -> dict:
        """Download known sitemap URLs and persist product page URLs as JSON.

        Returns {"sitemaps_found": N, "product_urls": M}."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)
        urls: List[str] = []
        found = 0
        for cand in SITEMAP_CANDIDATES:
            url = _url(cand, base_url)
            try:
                raw = _get(url, self.timeout, self.user_agent)
            except Exception:  # noqa: BLE001
                continue
            found += 1
            urls.extend(self._parse_sitemap(raw))
        # de-dupe, keep order
        urls = list(dict.fromkeys(urls))
        (out / "sitemap-products.json").write_text(
            json.dumps([{"url": u} for u in urls], ensure_ascii=False, indent=2), "utf-8")
        return {"sitemaps_found": found, "product_urls": len(urls)}

    @staticmethod
    def _parse_sitemap(raw: bytes) -> List[str]:
        try:
            text = raw.decode("utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            return []
        try:
            root = ET.fromstring(text)
        except ET.ParseError:
            return []
        out: List[str] = []
        for loc in root.iter():
            if loc.tag.endswith("loc") and loc.text:
                u = loc.text.strip()
                if any(t in u for t in _PRODUCT_TOKENS) and not any(t in u for t in _SKIP_TOKENS):
                    out.append(u)
        if not out:  # no product tokens — keep all locs as a best effort
            for loc in root.iter():
                if loc.tag.endswith("loc") and loc.text:
                    out.append(loc.text.strip())
        return out

    # ── Combined driver used by the crawl task ─────────────────────────────
    def fetch_for_supplier(self, base_url: str, output_dir: str, profile: str) -> dict:
        stats: dict = {"profile": profile}
        if profile == "woo_rest":
            stats["store_api"] = self.fetch_store_api(base_url, output_dir)
        elif profile == "sitemap_wp":
            stats["sitemap"] = self.fetch_sitemap(base_url, output_dir)
            stats["store_api"] = self.fetch_store_api(base_url, output_dir)
        return stats
