"""B2B directory crawling via HTTrack, then local parse for supplier URLs (spec §2.2)."""
from __future__ import annotations

import re
from pathlib import Path
from typing import List
from urllib.parse import urlparse

from src.crawler.httrack_engine import HTTrackMirrorEngine


class DirectoryCrawler:
    def __init__(self, mirror_base_dir: str = "/var/lib/iran_chem_db/mirrors"):
        self.base_dir = Path(mirror_base_dir) / "_directories"
        # v2.9: degrade gracefully when httrack is missing — directory
        # discovery is optional and must not crash the discovery engine.
        self.engine = HTTrackMirrorEngine(str(self.base_dir), require_httrack=False)

    def mirror_directory(self, directory_url: str, depth: int = 2, timeout: int = 120) -> dict:
        parsed = urlparse(directory_url)
        project = re.sub(r"[^a-z0-9]+", "_", parsed.netloc.lower()).strip("_")
        out_dir = str(self.base_dir / project)
        result = self.engine.mirror_using_url_list([directory_url], out_dir, project,
                                                   timeout=timeout, depth=depth)
        result["output_dir"] = out_dir
        return result

    def extract_supplier_urls(self, mirror_dir: str) -> List[str]:
        """Walk the local mirror and extract outbound supplier URLs."""
        found: List[str] = []
        base = Path(mirror_dir)
        if not base.exists():
            return found
        for html in base.rglob("*.html"):
            try:
                text = html.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            hrefs = re.findall(r'href=["\'](https?://[^"\'>\s]+)["\']', text)
            for href in hrefs:
                parsed = urlparse(href)
                if parsed.netloc and not _is_directory_host(parsed.netloc):
                    found.append(f"{parsed.scheme}://{parsed.netloc}")
        return list(dict.fromkeys(found))


def _is_directory_host(host: str) -> bool:
    directory_hosts = {"shimico.com", "b2bmap.com", "lookchem.com", "chemnet.com",
                       "chemicals1.com", "ensun.io", "kompass.com", "tradeford.com",
                       "exporthub.com", "alibaba.com", "tradewheel.com", "ec21.com",
                       "made-in-china.com", "volza.com"}
    return any(host == d or host.endswith("." + d) for d in directory_hosts)
