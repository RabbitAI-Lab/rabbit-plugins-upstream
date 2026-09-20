"""Link analysis — extract outbound supplier links from a mirrored site (spec §2.2)."""
from __future__ import annotations

import re
from pathlib import Path
from typing import List
from urllib.parse import urlparse


class LinkAnalyzer:
    def analyze_mirror(self, mirror_dir: str, exclude_domains: set[str] | None = None) -> List[str]:
        base = Path(mirror_dir)
        if not base.exists():
            return []
        excluded = exclude_domains or set()
        found: List[str] = []
        for html in base.rglob("*.html"):
            try:
                text = html.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for href in re.findall(r'href=["\'](https?://[^"\'>\s]+)["\']', text):
                parsed = urlparse(href)
                host = parsed.netloc
                if host and host not in excluded and not host.startswith("localhost"):
                    found.append(f"{parsed.scheme}://{host}")
        return list(dict.fromkeys(found))
