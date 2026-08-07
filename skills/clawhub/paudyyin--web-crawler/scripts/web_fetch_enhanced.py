#!/usr/bin/env python3
"""
web_fetch_enhanced.py - JS-rendering enhanced web fetcher.

Uses Playwright for JS-rendered pages, falls back to requests + BeautifulSoup
when Playwright is unavailable. Outputs clean markdown.

Usage:
    python web_fetch_enhanced.py <url> [options]
    python web_fetch_enhanced.py https://example.com --wait networkidle --timeout 30000
    python web_fetch_enhanced.py https://example.com --selector "article.main" --remove "nav,footer"
"""

import argparse
import json
import logging
import os
import re
import sys
import tempfile
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

import requests

logger = logging.getLogger(__name__)


def find_system_browser() -> Optional[str]:
    """Find system-installed Chrome or Edge browser."""
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None

# Default selectors to remove (nav, sidebar, footer, ads, cookies, etc.)
DEFAULT_REMOVE_SELECTORS = [
    "nav",
    "header",
    "footer",
    "aside",
    ".sidebar",
    ".side-bar",
    "#sidebar",
    ".nav",
    ".navigation",
    ".menu",
    ".advertisement",
    ".ads",
    ".ad",
    ".advert",
    "[role='navigation']",
    "[role='banner']",
    "[role='complementary']",
    "[role='contentinfo']",
    ".cookie-banner",
    ".cookie-consent",
    ".popup",
    ".modal",
    ".overlay",
    ".social-share",
    ".share-buttons",
    ".newsletter-signup",
    "#newsletter",
    ".breadcrumb",
    ".pagination",
    "script",
    "style",
    "noscript",
    "iframe:not([src*='youtube']):not([src*='vimeo'])",
]


class WebFetchEnhanced:
    """Enhanced web fetcher with JS rendering support and fallback."""

    def __init__(self):
        self._playwright_available = None

    def _check_playwright(self) -> bool:
        """Check if Playwright is available and browsers are installed."""
        if self._playwright_available is not None:
            return self._playwright_available
        try:
            from playwright.sync_api import sync_playwright
            p = sync_playwright().start()
            try:
                launch_opts = {"headless": True}
                sys_browser = find_system_browser()
                if sys_browser:
                    launch_opts["executable_path"] = sys_browser
                browser = p.chromium.launch(**launch_opts)
                browser.close()
                self._playwright_available = True
            except Exception:
                self._playwright_available = False
            finally:
                p.stop()
        except ImportError:
            self._playwright_available = False
        return self._playwright_available

    def fetch(
        self,
        url: str,
        wait_until: str = "load",
        timeout: int = 30000,
        selector: Optional[str] = None,
        remove_selector: Optional[str] = None,
        js: Optional[str] = None,
        use_playwright: Optional[bool] = None,
        extra_headers: Optional[dict] = None,
    ) -> str:
        """
        Fetch a URL and return content as markdown.

        Args:
            url: The URL to fetch.
            wait_until: When to consider navigation done.
                "load" | "domcontentloaded" | "networkidle"
            timeout: Navigation timeout in milliseconds.
            selector: Only extract content within this CSS selector.
            remove_selector: Additional CSS selectors to remove (comma-separated).
            js: JavaScript code to execute after page load.
            use_playwright: Force use/skip Playwright. None = auto-detect.
            extra_headers: Additional HTTP headers.

        Returns:
            Markdown string of the page content.
        """
        if use_playwright is None:
            use_playwright = self._check_playwright()

        if use_playwright:
            try:
                return self._fetch_with_playwright(
                    url=url,
                    wait_until=wait_until,
                    timeout=timeout,
                    selector=selector,
                    remove_selector=remove_selector,
                    js=js,
                    extra_headers=extra_headers,
                )
            except Exception as e:
                logger.warning(f"Playwright failed ({e}), falling back to requests")
                return self._fetch_with_requests(
                    url=url,
                    selector=selector,
                    remove_selector=remove_selector,
                    extra_headers=extra_headers,
                )
        else:
            return self._fetch_with_requests(
                url=url,
                selector=selector,
                remove_selector=remove_selector,
                extra_headers=extra_headers,
            )

    def _fetch_with_playwright(
        self,
        url: str,
        wait_until: str = "load",
        timeout: int = 30000,
        selector: Optional[str] = None,
        remove_selector: Optional[str] = None,
        js: Optional[str] = None,
        extra_headers: Optional[dict] = None,
    ) -> str:
        """Fetch using Playwright for JS-rendered pages."""
        from playwright.sync_api import sync_playwright

        wait_until_map = {
            "load": "load",
            "domcontentloaded": "domcontentloaded",
            "networkidle": "networkidle",
        }
        pw_wait_until = wait_until_map.get(wait_until, "load")

        with sync_playwright() as p:
            launch_opts = {"headless": True}
            sys_browser = find_system_browser()
            if sys_browser:
                launch_opts["executable_path"] = sys_browser
            browser = p.chromium.launch(**launch_opts)
            context = browser.new_context(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                viewport={"width": 1280, "height": 720},
                extra_http_headers=extra_headers or {},
            )
            page = context.new_page()

            try:
                page.goto(url, wait_until=pw_wait_until, timeout=timeout)

                # Execute custom JS if provided
                if js:
                    page.evaluate(js)

                # Remove unwanted elements
                selectors_to_remove = list(DEFAULT_REMOVE_SELECTORS)
                if remove_selector:
                    selectors_to_remove.extend(
                        s.strip() for s in remove_selector.split(",") if s.strip()
                    )

                for sel in selectors_to_remove:
                    try:
                        page.eval_on_selector_all(sel, "els => els.forEach(el => el.remove())")
                    except Exception:
                        pass  # Selector not found, that's fine

                # Get the HTML content
                if selector:
                    element = page.query_selector(selector)
                    if element:
                        html = element.inner_html()
                    else:
                        logger.warning(f"Selector '{selector}' not found, using full page")
                        html = page.content()
                else:
                    html = page.content()

                # Get page title
                title = page.title()

            finally:
                browser.close()

        return self._html_to_markdown(html, title=title, url=url)

    def _fetch_with_requests(
        self,
        url: str,
        selector: Optional[str] = None,
        remove_selector: Optional[str] = None,
        extra_headers: Optional[dict] = None,
    ) -> str:
        """Fallback: fetch using requests + BeautifulSoup."""
        from bs4 import BeautifulSoup

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        }
        if extra_headers:
            headers.update(extra_headers)

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # Handle encoding
        if response.encoding and response.encoding.lower() != "utf-8":
            response.encoding = response.apparent_encoding or response.encoding

        soup = BeautifulSoup(response.text, "html.parser")

        # Get title before removing elements
        title = ""
        title_tag = soup.find("title")
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Remove unwanted elements
        selectors_to_remove = list(DEFAULT_REMOVE_SELECTORS)
        if remove_selector:
            selectors_to_remove.extend(
                s.strip() for s in remove_selector.split(",") if s.strip()
            )

        for sel in selectors_to_remove:
            try:
                for element in soup.select(sel):
                    element.decompose()
            except Exception:
                pass

        # Extract content
        if selector:
            target = soup.select_one(selector)
            if target:
                html = str(target)
            else:
                logger.warning(f"Selector '{selector}' not found, using full page")
                html = str(soup)
        else:
            # Try to find main content area
            main_content = (
                soup.find("main")
                or soup.find("article")
                or soup.find(attrs={"role": "main"})
                or soup.find(class_=re.compile(r"(content|article|post|entry)", re.I))
                or soup.find("body")
                or soup
            )
            html = str(main_content)

        return self._html_to_markdown(html, title=title, url=url)

    def _html_to_markdown(self, html: str, title: str = "", url: str = "") -> str:
        """Convert HTML to clean markdown."""
        from markdownify import markdownify as md

        # Convert to markdown
        markdown = md(
            html,
            heading_style="ATX",
            bullets="-",
            strip=["img"],  # Strip images by default for cleaner output
        )

        # Clean up the markdown
        markdown = self._clean_markdown(markdown)

        # Add title and source info (avoid duplicating title if it's already the first heading)
        parts = []
        first_heading_match = re.match(r"^#\s+(.+)", markdown.strip())
        title_already_in_content = (
            first_heading_match
            and title
            and first_heading_match.group(1).strip().lower() == title.strip().lower()
        )

        if title and not title_already_in_content:
            parts.append(f"# {title}\n")
        if url:
            parts.append(f"> Source: {url}\n")
        parts.append(markdown)

        return "\n".join(parts)

    def _clean_markdown(self, text: str) -> str:
        """Clean up markdown output."""
        # Remove excessive blank lines (3+ → 2)
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove leading/trailing whitespace on each line
        lines = [line.strip() for line in text.split("\n")]
        text = "\n".join(lines)

        # Remove empty headings
        text = re.sub(r"^#{1,6}\s*$", "", text, flags=re.MULTILINE)

        # Remove consecutive blank lines again after cleanup
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Enhanced web fetcher with JS rendering support",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python web_fetch_enhanced.py https://example.com
  python web_fetch_enhanced.py https://spa-app.com --wait networkidle
  python web_fetch_enhanced.py https://example.com --selector "article"
  python web_fetch_enhanced.py https://example.com --remove "nav,footer,.ads"
  python web_fetch_enhanced.py https://example.com --js "window.scrollTo(0, 10000)"
  python web_fetch_enhanced.py https://example.com --no-playwright
  python web_fetch_enhanced.py https://example.com --output result.md
        """,
    )

    parser.add_argument("url", help="URL to fetch")
    parser.add_argument(
        "--wait",
        choices=["load", "domcontentloaded", "networkidle"],
        default="load",
        help="When to consider navigation complete (default: load)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30000,
        help="Navigation timeout in ms (default: 30000)",
    )
    parser.add_argument(
        "--selector",
        help="Only extract content within this CSS selector",
    )
    parser.add_argument(
        "--remove",
        dest="remove_selector",
        help="Additional CSS selectors to remove (comma-separated)",
    )
    parser.add_argument(
        "--js",
        help="JavaScript to execute after page load",
    )
    parser.add_argument(
        "--no-playwright",
        action="store_true",
        help="Force fallback mode (requests + BeautifulSoup)",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON with metadata",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging",
    )

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    fetcher = WebFetchEnhanced()

    try:
        result = fetcher.fetch(
            url=args.url,
            wait_until=args.wait,
            timeout=args.timeout,
            selector=args.selector,
            remove_selector=args.remove_selector,
            js=args.js,
            use_playwright=not args.no_playwright if args.no_playwright else None,
        )

        if args.json:
            output = json.dumps(
                {
                    "url": args.url,
                    "content": result,
                    "length": len(result),
                    "mode": "playwright" if not args.no_playwright else "requests",
                },
                ensure_ascii=False,
                indent=2,
            )
        else:
            output = result

        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
            print(f"Saved to {args.output}", file=sys.stderr)
        else:
            print(output)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
