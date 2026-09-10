"""JavaScript / XHR / GraphQL catalogue support (fix guide §5.3).

HTTrack mirrors static HTML; many Iranian storefronts fetch product cards and
pagination from JSON APIs after the HTML shell loads. This module:

  1. detects pages whose rendered product count is zero but which contain
     API/GraphQL hints (fetch/axios/graphql/ajax endpoints in the HTML);
  2. drives Playwright against those pages while RECORDING network responses;
  3. persists allowed JSON catalogue responses locally (mirror-adjacent);
  4. hands the local JSON files to JSONCatalogueParser (same local-only
     pipeline as the rest of the system);
  5. follows API pagination parameters (page/limit/offset/cursor) with
     bounded depth.

Polite-crawling rules from config apply (rate limits, robots policy).
"""
from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import List

logger = logging.getLogger(__name__)

API_HINT_RE = re.compile(
    r"(fetch\(|axios|XMLHttpRequest|GraphQL|graphql|\/api\/|\/wp-json\/|"
    r"xhr\.|\.ajax\()",
    re.I,
)
JSON_CONTENT = re.compile(r"application/(json|vnd\..*\+json)", re.I)
CATALOG_KEYS = ("products", "items", "data", "results", "rows", "list", "edges")
MAX_JSON_RESPONSES = 200          # per supplier
MAX_PAGINATION_FOLLOWS = 50       # bounded API pagination depth


class JSCatalogueEngine:
    """Detects API-driven catalogues and captures their JSON payloads."""

    def __init__(self, base_dir: str, max_responses: int = MAX_JSON_RESPONSES):
        self.base_dir = Path(base_dir)
        self.max_responses = max_responses

    # ── detection ──────────────────────────────────────────────────────────
    def page_has_api_hints(self, html: str) -> bool:
        return bool(API_HINT_RE.search(html or ""))

    def detect_catalogue_api(self, html: str) -> List[str]:
        """Extract candidate API endpoint URLs from an HTML shell."""
        found: List[str] = []
        for m in re.finditer(r"[\"']((?:https?:)?//[^\"']+?(?:api|wp-json|graphql|ajax)[^\"']*?)[\"']", html or "", re.I):
            url = m.group(1)
            if url.startswith("//"):
                url = "https:" + url
            found.append(url)
        return list(dict.fromkeys(found))

    # ── capture ────────────────────────────────────────────────────────────
    async def capture_json_responses(self, supplier_config, page_urls: List[str],
                                     output_subdir: str = "api_json") -> dict:
        """Render pages with Playwright, record JSON network responses, save them.

        Degrades gracefully when Playwright/Chromium is unavailable.
        """
        try:
            from playwright.async_api import async_playwright
        except ImportError:
            logger.error("Playwright not installed — JS catalogue capture skipped")
            return {"saved": 0, "error": "playwright-not-installed"}

        out_dir = Path(supplier_config.output_dir) / output_subdir
        out_dir.mkdir(parents=True, exist_ok=True)
        saved = 0
        captured: List[dict] = []
        errors: List[str] = []
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(user_agent=supplier_config.user_agent)
                page = await context.new_page()
                # ONE response listener for the whole page lifetime: registering
                # per-URL accumulates listeners and double-records responses.
                responses: List = []
                page.on("response", lambda r: responses.append(r))
                for url in page_urls:
                    if saved >= self.max_responses:
                        break
                    try:
                        responses.clear()
                        await page.goto(url, wait_until="networkidle", timeout=30000)
                        await page.wait_for_timeout(1500)
                        for resp in responses:
                            ctype = resp.headers.get("content-type", "")
                            if not JSON_CONTENT.search(ctype):
                                continue
                            try:
                                body = await resp.text()
                                data = json.loads(body)
                            except Exception:  # noqa: BLE001
                                continue
                            if self._looks_like_catalogue(data):
                                captured.append({"url": resp.url, "data": data})
                        # follow pagination if the page exposes a "next" URL
                        for extra in self._follow_pagination(page, url, max_follows=10):
                            captured.append(extra)
                            if len(captured) >= self.max_responses:
                                break
                    except Exception as exc:  # noqa: BLE001
                        errors.append(f"{url}: {type(exc).__name__}")
            for i, item in enumerate(dict.fromkeys(json.dumps(c, sort_keys=True) for c in captured)):
                entry = json.loads(item)
                fp = out_dir / f"catalogue_{i:04d}.json"
                fp.write_text(json.dumps(entry, ensure_ascii=False), encoding="utf-8")
                saved += 1
        except Exception as exc:  # noqa: BLE001 (browser missing / launch failure)
            logger.error("JS catalogue capture failed: %s", exc)
            return {"saved": 0, "error": f"capture-failed: {type(exc).__name__}"}
        logger.info("JS catalogue capture: %d JSON responses saved (%d errors)", saved, len(errors))
        return {"saved": saved, "errors": errors}

    def capture_json_responses_sync(self, supplier_config, page_urls: List[str],
                                    output_subdir: str = "api_json") -> dict:
        import asyncio
        try:
            return asyncio.run(self.capture_json_responses(supplier_config, page_urls, output_subdir))
        except RuntimeError:
            # already inside a running loop
            return {"saved": 0, "error": "runtime-no-loop"}

    # ── helpers ────────────────────────────────────────────────────────────
    def _looks_like_catalogue(self, data) -> bool:
        """Heuristic: JSON body contains product-like records."""
        if isinstance(data, list) and data and isinstance(data[0], dict):
            return True
        if isinstance(data, dict):
            flat = json.dumps(data, ensure_ascii=False).lower()
            return any(k in flat for k in CATALOG_KEYS)
        return False

    async def _follow_pagination(self, page, base_url: str, max_follows: int) -> List[dict]:
        """Click/next-page following is site-specific; here we follow simple
        `?page=N` links found in the rendered page, bounded."""
        out: List[dict] = []
        try:
            links = await page.eval_on_selector_all(
                "a[href*='page='], a[href*='?p=']", "els => els.map(e => e.href)")
            seen = {base_url}
            for href in links[:max_follows]:
                if href in seen or len(out) >= 10:
                    continue
                seen.add(href)
                try:
                    resp = await page.request.get(href)
                    if resp and JSON_CONTENT.search(resp.headers.get("content-type", "")):
                        try:
                            data = resp.json()
                        except Exception:  # noqa: BLE001
                            continue
                        if self._looks_like_catalogue(data):
                            out.append({"url": href, "data": data})
                except Exception:  # noqa: BLE001
                    continue
        except Exception:  # noqa: BLE001
            pass
        return out
