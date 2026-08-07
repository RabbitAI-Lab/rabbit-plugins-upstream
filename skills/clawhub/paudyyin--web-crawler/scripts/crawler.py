"""
BFS website crawler with Playwright rendering.
Supports same-domain filtering, content cleaning, and checkpoint/resume.
"""

import asyncio
import json
import os
import sys
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse
from typing import Optional

# Add scripts dir to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from content_cleaner import ContentCleaner


def find_system_browser() -> Optional[str]:
    """Find system-installed Chrome or Edge browser."""
    candidates = [
        # Chrome
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        # Edge
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        # Linux
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        # macOS
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


class SiteCrawler:
    """BFS crawler for websites."""

    def __init__(
        self,
        start_url: str,
        max_pages: int = 50,
        same_domain: bool = True,
        output_dir: str = None,
        headless: bool = True,
    ):
        self.start_url = start_url
        self.max_pages = max_pages
        self.same_domain = same_domain
        self.start_domain = urlparse(start_url).netloc
        self.headless = headless

        # Output setup
        if output_dir is None:
            output_dir = str(Path(__file__).parent.parent.parent / "crawl_results")
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # State
        self.visited = set()
        self.queue = deque()  # (url, depth)
        self.results = []
        self.cleaner = ContentCleaner()

        # Checkpoint file
        domain_safe = self.start_domain.replace(":", "_").replace(".", "_")
        self.checkpoint_file = self.output_dir / f"checkpoint_{domain_safe}.json"
        self.results_file = self.output_dir / f"crawl_{domain_safe}.json"

    def _load_checkpoint(self):
        """Load previously crawled state for resume."""
        if self.checkpoint_file.exists():
            with open(self.checkpoint_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.visited = set(data.get("visited", []))
            self.results = data.get("results", [])
            # Rebuild queue from last results' discovered links
            pending = data.get("pending", [])
            self.queue = deque((item["url"], item["depth"]) for item in pending)
            print(f"[resume] Loaded checkpoint: {len(self.visited)} visited, {len(self.queue)} pending")

    def _save_checkpoint(self):
        """Save current state for resume."""
        pending = [{"url": url, "depth": depth} for url, depth in self.queue]
        data = {
            "visited": list(self.visited),
            "results": self.results,
            "pending": pending,
        }
        with open(self.checkpoint_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def _is_valid_url(self, url: str) -> bool:
        """Check if URL should be crawled."""
        parsed = urlparse(url)
        # Only http(s)
        if parsed.scheme not in ("http", "https"):
            return False
        # Same domain filter
        if self.same_domain and parsed.netloc != self.start_domain:
            return False
        # Skip common non-page resources
        skip_ext = {".pdf", ".jpg", ".jpeg", ".png", ".gif", ".svg", ".css", ".js",
                    ".zip", ".tar", ".gz", ".mp3", ".mp4", ".avi", ".doc", ".xls"}
        path_lower = parsed.path.lower()
        if any(path_lower.endswith(ext) for ext in skip_ext):
            return False
        # Skip fragments-only URLs
        if not parsed.path and not parsed.query:
            return False
        return True

    def _normalize_url(self, url: str) -> str:
        """Normalize URL by removing fragment and trailing slash."""
        parsed = urlparse(url)
        # Remove fragment
        normalized = parsed._replace(fragment="")
        # Remove trailing slash (except for root)
        path = normalized.path
        if path != "/" and path.endswith("/"):
            path = path.rstrip("/")
            normalized = normalized._replace(path=path)
        return normalized.geturl()

    async def _discover_links(self, page) -> list:
        """Extract all links from current page."""
        try:
            links = await page.eval_on_selector_all(
                "a[href]",
                "elements => elements.map(e => e.href)"
            )
            return links
        except Exception:
            return []

    async def _crawl_page(self, playwright, url: str, depth: int):
        """Crawl a single page."""
        # Try system browser first, fall back to Playwright's bundled browser
        launch_opts = {"headless": self.headless}
        sys_browser = find_system_browser()
        if sys_browser:
            launch_opts["executable_path"] = sys_browser
        browser = await playwright.chromium.launch(**launch_opts)
        try:
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            )
            page = await context.new_page()
            page.set_default_timeout(30000)

            print(f"[crawl] depth={depth} {url}")
            response = await page.goto(url, wait_until="networkidle", timeout=60000)

            if response and response.status >= 400:
                print(f"[skip] HTTP {response.status}: {url}")
                return []

            html = await page.content()
            # Clean content
            content = self.cleaner.clean(html, url=url)
            # Discover links
            raw_links = await self._discover_links(page)

            result = {
                "url": url,
                "title": content["title"],
                "text": content["text"],
                "depth": depth,
                "publish_time": content.get("publish_time"),
            }
            self.results.append(result)
            self.visited.add(url)

            # Process discovered links
            new_links = []
            for link in raw_links:
                normalized = self._normalize_url(link)
                if self._is_valid_url(normalized) and normalized not in self.visited:
                    new_links.append((normalized, depth + 1))

            return new_links
        except Exception as e:
            print(f"[error] {url}: {e}")
            self.visited.add(url)  # Mark as visited to avoid retry
            return []
        finally:
            await browser.close()

    async def crawl(self, resume: bool = True):
        """Run the BFS crawl."""
        from playwright.async_api import async_playwright

        if resume:
            self._load_checkpoint()

        if not self.queue and self.start_url not in self.visited:
            self.queue.append((self._normalize_url(self.start_url), 0))

        async with async_playwright() as pw:
            while self.queue and len(self.visited) < self.max_pages:
                url, depth = self.queue.popleft()
                if url in self.visited:
                    continue

                new_links = await self._crawl_page(pw, url, depth)
                for link_url, link_depth in new_links:
                    if link_url not in self.visited:
                        self.queue.append((link_url, link_depth))

                # Save checkpoint after each page
                self._save_checkpoint()

        # Final save
        self._save_results()
        print(f"[done] Crawled {len(self.results)} pages")

    def _save_results(self):
        """Save final results to JSON."""
        with open(self.results_file, "w", encoding="utf-8") as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        print(f"[save] Results: {self.results_file}")


async def main():
    """CLI entry point."""
    import argparse
    parser = argparse.ArgumentParser(description="BFS website crawler")
    parser.add_argument("url", help="Starting URL")
    parser.add_argument("--max-pages", type=int, default=50, help="Max pages to crawl")
    parser.add_argument("--no-same-domain", action="store_true", help="Allow cross-domain")
    parser.add_argument("--output-dir", help="Output directory")
    parser.add_argument("--no-headless", action="store_true", help="Show browser")
    parser.add_argument("--no-resume", action="store_true", help="Start fresh")

    args = parser.parse_args()

    crawler = SiteCrawler(
        start_url=args.url,
        max_pages=args.max_pages,
        same_domain=not args.no_same_domain,
        output_dir=args.output_dir,
        headless=not args.no_headless,
    )
    await crawler.crawl(resume=not args.no_resume)


if __name__ == "__main__":
    asyncio.run(main())
