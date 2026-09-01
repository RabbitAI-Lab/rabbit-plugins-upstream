"""Search-engine discovery — SerpAPI / Google CSE / Bing (spec §2.2)."""
from __future__ import annotations

import os
import re
from typing import List
from urllib.parse import urlparse


class SearchEngineDiscovery:
    """Query search engines (English + Persian) for supplier URLs.

    Works without API keys using a direct search-engine fallback; with a key it
    uses SerpAPI. Each result's domain is extracted and normalized.
    """

    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or os.environ.get("SEARCH_API_KEY", "")

    def search(self, query: str, limit: int = 10) -> List[str]:
        if self.api_key:
            urls = self._search_serpapi(query, limit)
        else:
            urls = self._search_fallback(query, limit)
        return self._normalize(urls)

    def _search_serpapi(self, query: str, limit: int) -> List[str]:
        import requests
        resp = requests.get(
            "https://serpapi.com/search.json",
            params={"engine": "google", "q": query, "num": limit, "api_key": self.api_key},
            timeout=30,
        )
        resp.raise_for_status()
        return [r.get("link", "") for r in resp.json().get("organic_results", [])]

    def _search_fallback(self, query: str, limit: int) -> List[str]:
        """Key-less fallback: scrape the text result links from DuckDuckGo HTML."""
        import requests
        try:
            resp = requests.get(
                "https://html.duckduckgo.com/html/",
                params={"q": query},
                headers={"User-Agent": "IranChemDB/1.0 discovery"},
                timeout=30,
            )
            resp.raise_for_status()
            # ddg redirects contain the target in uddg= param
            links = re.findall(r"uddg=([^&\"']+)", resp.text)
            from urllib.parse import unquote
            return [unquote(l) for l in links[:limit]]
        except Exception:  # noqa: BLE001
            return []

    @staticmethod
    def _normalize(urls: List[str]) -> List[str]:
        out = []
        for u in urls:
            if not u:
                continue
            parsed = urlparse(u)
            if parsed.scheme in ("http", "https") and parsed.netloc:
                out.append(f"{parsed.scheme}://{parsed.netloc}")
        return list(dict.fromkeys(out))
