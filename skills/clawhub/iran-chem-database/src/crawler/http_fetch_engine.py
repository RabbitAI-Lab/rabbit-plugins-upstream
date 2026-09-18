"""Multi-tool HTTP fetch fallback engine (added v2.8).

HTTrack is the primary mirror engine, but it can be missing, its default
User-Agent can be blocked by a site, or a catalog may need only a few pages
(REST/sitemap entry points). This engine provides graceful fallbacks using the
plain HTTP tools available on any Linux box:

  * python — stdlib urllib fetch (always available, no binary needed);
  * curl   — single-page fetch with browser UA + redirect follow;
  * wget   — single-page fetch, and optionally a recursive mirror
             (`wget -r -k -p`) as a last-resort site downloader.

Every tool is detected at runtime (shutil.which); a missing tool is skipped,
never an error. Fetched pages are written into the supplier's local mirror
directory under `fetch-fallback/<tool>/` with the correct extension (.html,
.json, .pdf, ...) so the existing local-file-only parser consumes them exactly
like HTTrack mirrors. Stdlib only; no new dependencies.
"""
from __future__ import annotations

import logging
import re
import shutil
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple

logger = logging.getLogger(__name__)

DEFAULT_UA = "IranChemDB/2.8 (Research Chemical Database crawler; contact@iranchem.db)"
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# Minimum accepted payload size (bytes) — smaller is an error page / redirect stub.
MIN_SAVED_BYTES = 300

# Content-Type -> file extension mapping for python/urllib fetches.
_CONTENT_TYPE_EXT = {
    "text/html": ".html",
    "application/json": ".json",
    "application/pdf": ".pdf",
    "text/plain": ".txt",
    "text/markdown": ".md",
    "text/csv": ".csv",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
    "application/vnd.ms-excel": ".xls",
}


def _slug(url: str) -> str:
    host = urllib.parse.urlparse(url).netloc.replace("www.", "")
    path = urllib.parse.urlparse(url).path.strip("/").replace("/", "_")
    base = (host + ("-" + path if path else "")) or "page"
    return re.sub(r"[^a-z0-9.\-]", "_", base.lower())[:120]


def _ext_from_url(url: str) -> str:
    """Guess a parseable file extension from the URL path (else .html)."""
    path = urllib.parse.urlparse(url).path.lower()
    for ext in (".json", ".pdf", ".xlsx", ".xls", ".csv", ".md", ".txt"):
        if path.endswith(ext):
            return ext
    return ".html"


def _ext_from_content_type(ct: str) -> str:
    ct = (ct or "").split(";")[0].strip().lower()
    return _CONTENT_TYPE_EXT.get(ct, ".html")


def _run(cmd: List[str], timeout: int) -> Tuple[int, str]:
    """Run a command; return (returncode, stderr-tail). Never raises."""
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stderr or "")[-500:]
    except FileNotFoundError:
        return 127, "binary not found"
    except subprocess.TimeoutExpired:
        return 124, "timeout"
    except Exception as exc:  # noqa: BLE001
        return 1, f"{type(exc).__name__}"


class HTTPFetchEngine:
    """Single-page + recursive fetch fallbacks via python/curl/wget."""

    def __init__(self, base_dir: str, timeout: int = 40, delay: float = 0.3,
                 user_agent: str = DEFAULT_UA, browser_ua: str = BROWSER_UA,
                 min_saved_bytes: int = MIN_SAVED_BYTES):
        self.base_dir = Path(base_dir)
        self.timeout = timeout
        self.delay = delay
        self.user_agent = user_agent
        self.browser_ua = browser_ua
        self.min_saved_bytes = min_saved_bytes

    # ── tool detection ─────────────────────────────────────────────────────
    def available_tools(self) -> List[str]:
        """Return the installed tools among python/curl/wget (python is implicit)."""
        tools = ["python"]
        for t in ("curl", "wget"):
            if shutil.which(t):
                tools.append(t)
        return tools

    # ── single-page fetchers ───────────────────────────────────────────────
    def fetch_page_python(self, url: str, output_dir: str) -> dict:
        """stdlib urllib fetch (no external binary)."""
        out = Path(output_dir) / "fetch-fallback" / "python"
        out.mkdir(parents=True, exist_ok=True)
        try:
            from src.utils.http_util import get_bytes
            data = get_bytes(url, timeout=self.timeout, user_agent=self.user_agent,
                             accept="text/html, application/json, application/pdf, */*")
            ct = ""  # content type is not exposed by get_bytes; infer from URL
            status = 200
        except urllib.error.HTTPError as exc:
            return {"tool": "python", "saved": 0, "error": f"http-{exc.code}"}
        except Exception as exc:  # noqa: BLE001
            return {"tool": "python", "saved": 0, "error": type(exc).__name__}
        return self._save(out, url, data, ct, status)

    def fetch_page_curl(self, url: str, output_dir: str) -> dict:
        """curl -L --max-time with browser UA (site may block the crawler UA)."""
        if not shutil.which("curl"):
            return {"tool": "curl", "saved": 0, "error": "curl-not-installed"}
        out = Path(output_dir) / "fetch-fallback" / "curl"
        out.mkdir(parents=True, exist_ok=True)
        ext = _ext_from_url(url)
        path = out / f"{_slug(url)}{ext}"
        cmd = ["curl", "-sS", "-L", "--max-time", str(self.timeout),
               "-A", self.browser_ua, "-o", str(path), "--write-out", "%{http_code}", url]
        rc, err = _run(cmd, self.timeout + 5)
        if rc != 0:
            return {"tool": "curl", "saved": 0, "error": f"rc-{rc}"}
        return self._check(path, url, "curl", rc)

    def fetch_page_wget(self, url: str, output_dir: str) -> dict:
        """wget single-page fetch (spider-safe: --tries=2, quiet)."""
        if not shutil.which("wget"):
            return {"tool": "wget", "saved": 0, "error": "wget-not-installed"}
        out = Path(output_dir) / "fetch-fallback" / "wget"
        out.mkdir(parents=True, exist_ok=True)
        ext = _ext_from_url(url)
        path = out / f"{_slug(url)}{ext}"
        cmd = ["wget", "-q", "-T", str(self.timeout), "--tries=2",
               "-U", self.browser_ua, "-O", str(path), url]
        rc, err = _run(cmd, self.timeout + 5)
        if rc != 0:
            return {"tool": "wget", "saved": 0, "error": f"rc-{rc}"}
        return self._check(path, url, "wget", rc)

    # ── recursive mirror ───────────────────────────────────────────────────
    def mirror_recursive_wget(self, url: str, output_dir: str, depth: int = 3) -> dict:
        """Last-resort site download via `wget -r -k -p` (like a light mirror)."""
        if not shutil.which("wget"):
            return {"tool": "wget-recursive", "saved": 0, "error": "wget-not-installed"}
        out = Path(output_dir) / "fetch-fallback" / "wget-mirror"
        out.mkdir(parents=True, exist_ok=True)
        cmd = ["wget", "-q", "-r", "-l", str(depth), "-k", "-p", "-E", "-nc", "-np",
               "--wait=0.3", "-T", str(self.timeout), "--tries=2",
               "-U", self.browser_ua, "-P", str(out), url]
        rc, err = _run(cmd, self.timeout * 4)
        files = list(out.rglob("*")) if out.exists() else []
        html = [f for f in files if f.suffix.lower() in (".html", ".htm")]
        if not html:
            return {"tool": "wget-recursive", "saved": 0, "error": f"rc-{rc}"}
        return {"tool": "wget-recursive", "saved": len(html), "total_files": len(files)}

    # ── orchestrator ───────────────────────────────────────────────────────
    def fetch_page(self, url: str, output_dir: str,
                   tools: Optional[List[str]] = None) -> dict:
        """Fetch one page with the first working tool (python → curl → wget).

        Returns the winning tool's stats dict."""
        tools = tools or self.available_tools()
        for t in tools:
            try:
                if t == "python":
                    r = self.fetch_page_python(url, output_dir)
                elif t == "curl":
                    r = self.fetch_page_curl(url, output_dir)
                elif t == "wget":
                    r = self.fetch_page_wget(url, output_dir)
                else:
                    continue
            except Exception as exc:  # noqa: BLE001
                r = {"tool": t, "saved": 0, "error": type(exc).__name__}
            if r.get("saved"):
                time.sleep(self.delay)
                return r
            time.sleep(self.delay)
        return {"tool": None, "saved": 0, "error": "all-tools-failed"}

    def fetch_for_supplier(self, url: str, output_dir: str,
                           entry_points: Optional[List[str]] = None,
                           tools: Optional[List[str]] = None,
                           wget_recursive: bool = False,
                           wget_recursive_depth: int = 3) -> dict:
        """Fetch a supplier's homepage + entry points via the fallback chain.

        Returns {"homepage": {...}, "entry_points": [...], "recursive": {...},
                 "total_saved": N}."""
        stats: dict = {"entry_points": []}
        total = 0
        stats["homepage"] = self.fetch_page(url, output_dir, tools)
        total += int(stats["homepage"].get("saved", 0) or 0)
        for ep in (entry_points or []):
            r = self.fetch_page(ep, output_dir, tools)
            stats["entry_points"].append(r)
            total += int(r.get("saved", 0) or 0)
        if wget_recursive:
            stats["recursive"] = self.mirror_recursive_wget(
                url, output_dir, wget_recursive_depth)
            total += int(stats["recursive"].get("saved", 0) or 0)
        stats["total_saved"] = total
        return stats

    # ── helpers ────────────────────────────────────────────────────────────
    def _save(self, out: Path, url: str, data: bytes, content_type: str, status: int) -> dict:
        if status not in (200, 201):
            return {"tool": "python", "saved": 0, "error": f"http-{status}"}
        if len(data) < self.min_saved_bytes:
            return {"tool": "python", "saved": 0, "error": "too-small"}
        ext = _ext_from_content_type(content_type) if "html" in content_type or "json" in content_type \
            else _ext_from_url(url)
        path = out / f"{_slug(url)}{ext}"
        path.write_bytes(data)
        return {"tool": "python", "saved": 1, "bytes": len(data), "status": status}

    def _check(self, path: Path, url: str, tool: str, rc: int) -> dict:
        if not path.exists():
            return {"tool": tool, "saved": 0, "error": "no-file"}
        size = path.stat().st_size
        if size < self.min_saved_bytes:
            path.unlink(missing_ok=True)
            return {"tool": tool, "saved": 0, "error": "too-small"}
        return {"tool": tool, "saved": 1, "bytes": size}
