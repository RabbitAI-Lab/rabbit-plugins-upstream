"""PlaywrightFallbackEngine — JS-rendering fallback for HTTrack (spec §3.1).

HTTrack does not execute JavaScript. When a supplier site is JS-rendered and the
HTTrack mirror is empty or incomplete, Playwright renders each catalog page and
saves the HTML INTO the same mirror directory structure, so the parser pipeline
stays unified (local files only).
"""
from __future__ import annotations

import logging
from pathlib import Path
from typing import List
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


class PlaywrightFallbackEngine:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)

    def render_and_save(self, supplier_config, catalog_urls: List[str]) -> dict:
        """Synchronous entry point that runs the async browser routine.

        Never raises: degrades gracefully when Playwright or its Chromium browser
        is unavailable (HTTrack remains the primary engine regardless).
        """
        try:
            import asyncio
            return asyncio.run(self._render_and_save_async(supplier_config, catalog_urls))
        except ImportError as exc:
            logger.error("Playwright not installed: %s", exc)
            return {"rendered": 0, "error": "playwright-not-installed"}
        except Exception as exc:  # noqa: BLE001 (browser missing / launch failure)
            logger.error("Playwright render failed: %s", exc)
            return {"rendered": 0, "error": f"playwright-render-failed: {type(exc).__name__}"}

    async def _render_and_save_async(self, supplier_config, catalog_urls: List[str]) -> dict:
        from playwright.async_api import async_playwright

        saved = 0
        errors: List[str] = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                user_agent=supplier_config.user_agent, locale="fa-IR"
            )
            page = await context.new_page()
            for url in catalog_urls:
                try:
                    await page.goto(url, wait_until="networkidle", timeout=30000)
                    await self._handle_infinite_scroll(page)
                    await self._click_load_more_buttons(page)
                    content = await page.content()
                    save_path = self.url_to_mirror_path(url, supplier_config.output_dir)
                    save_path.parent.mkdir(parents=True, exist_ok=True)
                    save_path.write_text(content, encoding="utf-8")
                    saved += 1
                    logger.info("Playwright rendered and saved: %s -> %s", url, save_path)
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"{url}: {exc}")
                    logger.error("Playwright failed for %s: %s", url, exc)
            await browser.close()
        return {"rendered": saved, "errors": errors}

    @staticmethod
    @staticmethod
    def url_to_mirror_path(url: str, output_dir: str) -> Path:
        """Convert a URL to a local path matching HTTrack's directory convention.

        Sanitized (v2.4.0): `..` segments are rejected, userinfo/port are
        stripped from the host, and host/path characters are whitelisted so a
        malicious or malformed URL can never write outside the mirror dir.
        """
        import re as _re
        parsed = urlparse(url)
        if parsed.username or parsed.password:
            raise ValueError(f"unsafe mirror URL (credentials embedded): {url!r}")
        host = (parsed.hostname or "").lower()
        if not host or not _re.fullmatch(r"[a-z0-9.-]+", host):
            raise ValueError(f"unsafe mirror host: {parsed.netloc!r}")
        raw_path = parsed.path.strip("/")
        segs = [s for s in raw_path.split("/") if s not in ("", ".")]
        if any(s == ".." for s in segs):
            raise ValueError(f"unsafe mirror path (traversal): {url!r}")
        segs = [s for s in segs if _re.fullmatch(r"[A-Za-z0-9._%\-]+", s)]
        path = "/".join(segs)
        if not path or path.endswith("/"):
            path = path + "index.html"
        elif "." not in path.split("/")[-1]:
            path = path + "/index.html"
        return Path(output_dir) / host / path

    async def _handle_infinite_scroll(self, page) -> None:
        prev_height = 0
        for _ in range(50):
            current_height = await page.evaluate("document.body.scrollHeight")
            if current_height == prev_height:
                break
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_timeout(2000)
            prev_height = current_height

    async def _click_load_more_buttons(self, page) -> None:
        selectors = [
            'button:has-text("Load More")', 'button:has-text("Show More")',
            'button:has-text("بیشتر")', 'button:has-text("نمایش بیشتر")',
            'a:has-text("Next")', 'a:has-text("بعدی")',
            ".load-more", "#load-more", ".pagination a.next",
        ]
        for selector in selectors:
            while True:
                try:
                    btn = await page.query_selector(selector)
                    if btn and await btn.is_visible():
                        await btn.click()
                        await page.wait_for_timeout(3000)
                    else:
                        break
                except Exception:  # noqa: BLE001
                    break
