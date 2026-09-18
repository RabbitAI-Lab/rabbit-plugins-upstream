"""Free-access fallback engine (added v2.6).

Field-verified 2026-08-21: Iranian supplier hosts that geo-block foreign
datacenter IPs at the TLS handshake remain reachable through free, third-party
fetchers whose own IPs are not on the blocklist. Live tests on 12 blocked sites
(rockchemie.com, abnoos.com, artinkimya.com, pakshoo.com, pgsoc.ir,
tebgostar.com, novichem.ir, basparsazan.com, mahdistejarat.com, irandaru.com,
shimico.com, parsisotope.com):

  * Jina Reader      https://r.jina.ai/<url>                  -> markdown text  (9/12 sites)
  * Wayback Machine  https://web.archive.org/web/<ts>id_/<url>  (CDX API lists snapshots) (10/12)
  * SPN2 (Save Now)  https://web.archive.org/save/<url>        -> FORCE a fresh capture (v2.7.1)
  * Common Crawl     https://index.commoncrawl.org + data.commoncrawl.org -> recent full HTML (v2.7)
  * Google Translate https://translate.google.com/translate?u=<url> (9/12)
  * archive.today    https://archive.ph/newest/<url>          -> archived snapshot (v2.6.1)
  * thum.io          https://image.thum.io/get/...            -> rendered PNG screenshot (v2.7)

Every site is covered by at least one method. This engine fetches public
catalog pages through those front-ends and stores the result inside the
supplier's local mirror directory, so the existing local-file-only parser
consumes them exactly like any other mirrored file. Stdlib only (urllib/json/
xml), no credentials, polite (UA, per-request delay, page/time budgets).
"""
from __future__ import annotations

import gzip
import json
import logging
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import List, Optional, Tuple

from src.utils.http_util import get_bytes

logger = logging.getLogger(__name__)

DEFAULT_UA = "IranChemDB/2.7 (Research Chemical Database crawler; contact@iranchem.db)"

# Jina Reader returns the page as markdown text (free, keyless).
JINA_BASE = "https://r.jina.ai/"
# Wayback CDX API enumerates archived snapshots; web/…/id_/… serves the raw page.
WAYBACK_CDX = "http://web.archive.org/cdx/search/cdx"
WAYBACK_VIEW = "https://web.archive.org/web/{ts}id_/{url}"
# v2.7.1 — Wayback "Save Page Now" (SPN2): force the Internet Archive crawler
# to fetch the page FRESH from its own (allowed) IPs, then read the new capture.
SPN2_SAVE = "https://web.archive.org/save/{url}"
SPN2_TS_RE = r"web\.archive\.org/web/(\d{14})"
# Common Crawl index API + WARC store (S3 — not geo-blocked). v2.7.
COMMONCRAWL_COLLINFO = "https://index.commoncrawl.org/collinfo.json"
COMMONCRAWL_INDEX = "https://index.commoncrawl.org/{idx}-index?url={site}%2A&output=json"
COMMONCRAWL_DATA = "https://data.commoncrawl.org/"
# Google Translate fetches the page server-side and renders it in a frame.
TRANSLATE_URL = "https://translate.google.com/translate?sl=auto&tl=en&u={u}"
# v2.6.1 — archive.today family (archive.ph / archive.today / archive.is are
# mirrors of the same service). Serves existing snapshots; blocks many
# datacenter IPs but is reachable from residential/operator networks. The
# `newest` endpoint redirects to the newest snapshot if one exists.
ARCHIVE_TODAY_HOSTS = ("https://archive.ph", "https://archive.today", "https://archive.is")
ARCHIVE_TODAY_NEWEST = "{host}/newest/{url}"
ARCHIVE_TODAY_SEARCH = "{host}/{url}"
# v2.7 — thum.io free screenshot service renders the page server-side to a PNG.
THUMIO = "https://image.thum.io/get/width/1200/noanimate/{url}"

# Default method order for a geo-blocked supplier when no per-site preference
# is configured (see free_access_preference() in src/discovery/seed_list.py).
# "screenshot" is intentionally NOT in the default list — it produces an image
# (visual evidence) that the text parser cannot read; enable it explicitly.
DEFAULT_FREE_ACCESS_METHODS = ["jina", "wayback", "commoncrawl", "spn2", "translate", "archivetoday"]


def _slug(url: str) -> str:
    host = urllib.parse.urlparse(url).netloc.replace("www.", "")
    return re.sub(r"[^a-z0-9.\-]", "_", host.lower())[:80] or "site"


def _get(url: str, timeout: int, user_agent: str, headers: Optional[dict] = None) -> bytes:
    """GET with retry/backoff on transient errors (v2.9)."""
    return get_bytes(url, timeout=timeout, user_agent=user_agent,
                     accept="text/html, text/markdown, application/json;q=0.9, */*;q=0.8",
                     headers=headers)


class FreeAccessEngine:
    """Fetch geo-blocked public pages through free third-party front-ends."""

    def __init__(self, base_dir: str, timeout: int = 40, delay: float = 0.5,
                 max_wayback_pages: int = 25, max_commoncrawl_pages: int = 25,
                 user_agent: str = DEFAULT_UA):
        self.base_dir = Path(base_dir)
        self.timeout = timeout
        self.delay = delay
        self.max_wayback_pages = max_wayback_pages
        self.max_commoncrawl_pages = max_commoncrawl_pages
        self.user_agent = user_agent

    # ── method 1: Jina Reader ──────────────────────────────────────────────
    def fetch_via_jina(self, url: str, output_dir: str) -> dict:
        """Fetch a page through Jina Reader (markdown) into output_dir."""
        out = Path(output_dir) / "free-access" / "jina"
        out.mkdir(parents=True, exist_ok=True)
        try:
            raw = _get(JINA_BASE + url, self.timeout, self.user_agent)
        except Exception as exc:  # noqa: BLE001
            return {"method": "jina", "saved": 0, "error": f"{type(exc).__name__}"}
        text = raw.decode("utf-8", errors="replace")
        if len(text) < 300:  # jina returns a short error note on failure
            return {"method": "jina", "saved": 0, "error": "empty-or-blocked"}
        path = out / f"{_slug(url)}.md"
        path.write_text(text, "utf-8")
        time.sleep(self.delay)
        return {"method": "jina", "saved": 1, "bytes": len(raw)}

    # ── method 2: Wayback Machine ──────────────────────────────────────────
    @staticmethod
    def _parse_cdx_rows(raw: bytes) -> List[Tuple[str, str]]:
        try:
            data = json.loads(raw.decode("utf-8", errors="replace"))
        except Exception:  # noqa: BLE001
            return []
        rows: List[Tuple[str, str]] = []
        for r in data[1:]:  # first row is the header
            if isinstance(r, list) and len(r) >= 2 and r[0] and r[1]:
                rows.append((str(r[0]), str(r[1])))
        return rows

    def list_wayback_snapshots(self, site: str, limit: int = 1000) -> List[Tuple[str, str]]:
        query = urllib.parse.urlencode({
            "url": f"{site}*", "output": "json", "filter": "statuscode:200",
            "collapse": "urlkey", "fl": "timestamp,original", "limit": str(limit),
        })
        raw = _get(f"{WAYBACK_CDX}?{query}", self.timeout, self.user_agent)
        return self._parse_cdx_rows(raw)

    def fetch_via_wayback(self, url: str, output_dir: str) -> dict:
        """Enumerate archived pages for the site and mirror the most recent ones."""
        out = Path(output_dir) / "free-access" / "wayback"
        out.mkdir(parents=True, exist_ok=True)
        host = urllib.parse.urlparse(url).netloc
        try:
            snapshots = self.list_wayback_snapshots(host)
        except Exception as exc:  # noqa: BLE001
            return {"method": "wayback", "saved": 0, "error": f"{type(exc).__name__}"}
        if not snapshots:
            return {"method": "wayback", "saved": 0, "error": "no-snapshots"}

        # newest first; prefer product-ish URLs, keep the homepage too
        snapshots.sort(reverse=True)
        seen: set = set()
        saved = 0
        for ts, orig in snapshots:
            key = orig.split("?")[0]
            if key in seen:
                continue
            seen.add(key)
            if saved >= self.max_wayback_pages:
                break
            try:
                raw = _get(WAYBACK_VIEW.format(ts=ts, url=orig), self.timeout, self.user_agent)
            except Exception:  # noqa: BLE001
                continue
            if len(raw) < 500:
                continue
            fn = out / f"{ts}-{_slug(orig)}.html"
            fn.write_bytes(raw)
            saved += 1
            time.sleep(self.delay)
        return {"method": "wayback", "saved": saved, "snapshots": len(snapshots)}

    # ── method 2a: Wayback "Save Page Now" (force a fresh capture) ─────────
    def fetch_via_spn2(self, url: str, output_dir: str) -> dict:
        """Force a FRESH capture via the Internet Archive, then read it.

        v2.7.1 — invented via an adversarial reasoning-team debate and verified
        live (rockchemie.com captured 2026-08-22, full HTML). The Save Page Now
        endpoint makes the IA crawler fetch the page from its own IPs — which
        the geo-blocking Iranian hosts allow — so a blocked site is captured
        on demand and read back from web.archive.org. Polite use: one capture
        per supplier per crawl cycle."""
        out = Path(output_dir) / "free-access" / "spn2"
        out.mkdir(parents=True, exist_ok=True)
        try:
            raw = _get(SPN2_SAVE.format(url=url), self.timeout, self.user_agent)
        except urllib.error.HTTPError as exc:
            # IA's save endpoint intermittently returns 5xx/520 — report it,
            # do not treat as fatal.
            return {"method": "spn2", "saved": 0, "error": f"save-http-{exc.code}"}
        except Exception as exc:  # noqa: BLE001
            return {"method": "spn2", "saved": 0, "error": f"{type(exc).__name__}"}
        text = raw.decode("utf-8", errors="replace")
        m = re.search(SPN2_TS_RE, text)
        if not m:
            # "already saved" or "blocked" pages don't yield a fresh timestamp
            return {"method": "spn2", "saved": 0, "error": "no-timestamp"}
        ts = m.group(1)
        time.sleep(self.delay)
        try:
            page = _get(WAYBACK_VIEW.format(ts=ts, url=url), self.timeout, self.user_agent)
        except Exception as exc:  # noqa: BLE001
            return {"method": "spn2", "saved": 0, "error": f"readback-{type(exc).__name__}"}
        if len(page) < 500:
            return {"method": "spn2", "saved": 0, "error": "empty-capture"}
        path = out / f"{ts}-{_slug(url)}.html"
        path.write_bytes(page)
        return {"method": "spn2", "saved": 1, "bytes": len(page), "timestamp": ts}

    # ── method 2b: Common Crawl (recent full-HTML captures) ────────────────
    def list_commoncrawl_indexes(self, limit: int = 3) -> List[str]:
        """Return the newest Common Crawl index ids (e.g. CC-MAIN-2026-30)."""
        raw = _get(COMMONCRAWL_COLLINFO, self.timeout, self.user_agent)
        coll = json.loads(raw.decode("utf-8", errors="replace"))
        return [c["id"] for c in coll[:limit]]

    def list_commoncrawl_captures(self, site: str) -> List[dict]:
        """Return real (non-diagnostic) page captures for a site, newest first."""
        site = site.replace("www.", "")
        try:
            indexes = self.list_commoncrawl_indexes()
        except Exception:  # noqa: BLE001
            return []
        for idx in indexes:
            try:
                raw = _get(COMMONCRAWL_INDEX.format(idx=idx, site=site),
                           self.timeout, self.user_agent)
            except Exception:  # noqa: BLE001
                continue
            try:
                rows = [json.loads(l) for l in raw.decode("utf-8", errors="replace").splitlines() if l.strip()]
            except Exception:  # noqa: BLE001
                continue
            rows = [r for r in rows if "crawldiagnostics" not in r.get("filename", "")]
            if rows:
                rows.sort(key=lambda r: r.get("timestamp", ""), reverse=True)
                return rows
        return []

    @staticmethod
    def _extract_warc_payload(record: bytes) -> bytes:
        """Extract the HTTP response body from a WARC 'response' record.

        Layout: WARC/1.0 headers \\r\\n\\r\\n HTTP/1.x status + headers \\r\\n\\r\\n body.
        Handles chunked transfer-encoding and gzip content-encoding.
        """
        warc_hdr_end = record.find(b"\r\n\r\n")
        if warc_hdr_end == -1:
            return b""
        http_start = warc_hdr_end + 4
        http_hdr_end = record.find(b"\r\n\r\n", http_start)
        if http_hdr_end == -1:
            return b""
        http_headers = record[http_start:http_hdr_end].decode("utf-8", errors="replace")
        body = record[http_hdr_end + 4:]
        # chunked transfer-encoding?
        if re.match(rb"^[0-9a-fA-F]+\r\n", body):
            out = bytearray()
            i = 0
            n = len(body)
            while i < n:
                eol = body.find(b"\r\n", i)
                if eol == -1:
                    break
                try:
                    size = int(body[i:eol], 16)
                except ValueError:
                    break
                if size == 0:
                    break
                out += body[eol + 2:eol + 2 + size]
                i = eol + 2 + size + 2
            body = bytes(out)
        # gzip content-encoding?
        if "content-encoding: gzip" in http_headers.lower():
            try:
                body = gzip.decompress(body)
            except Exception:  # noqa: BLE001
                pass
        return body

    def fetch_via_commoncrawl(self, url: str, output_dir: str) -> dict:
        """Fetch the most recent Common Crawl captures of a site as full HTML.

        The index API lists captures; each WARC record is fetched with a tiny
        HTTP Range request (the WARC store is S3 — not geo-blocked) and the
        HTML body is extracted and saved locally."""
        out = Path(output_dir) / "free-access" / "commoncrawl"
        out.mkdir(parents=True, exist_ok=True)
        host = urllib.parse.urlparse(url).netloc.replace("www.", "")
        try:
            captures = self.list_commoncrawl_captures(host)
        except Exception as exc:  # noqa: BLE001
            return {"method": "commoncrawl", "saved": 0, "error": f"{type(exc).__name__}"}
        if not captures:
            return {"method": "commoncrawl", "saved": 0, "error": "no-captures"}

        seen: set = set()
        saved = 0
        for rec in captures:
            if saved >= self.max_commoncrawl_pages:
                break
            fn = rec.get("filename", "")
            off = int(rec.get("offset", 0))
            ln = int(rec.get("length", 0))
            if not fn or ln <= 0:
                continue
            key = rec.get("url", "").split("?")[0]
            if key in seen:
                continue
            seen.add(key)
            try:
                member = get_bytes(COMMONCRAWL_DATA + fn, timeout=self.timeout,
                                   user_agent=self.user_agent,
                                   headers={"Range": f"bytes={off}-{off + ln - 1}"})
                # the .warc.gz file is a concatenation of gzip members; the
                # range we fetched is one complete member — gunzip it first.
                record = gzip.decompress(member)
                payload = self._extract_warc_payload(record)
            except Exception:  # noqa: BLE001
                continue
            if len(payload) < 400:
                continue
            ts = rec.get("timestamp", "0")
            fn_out = out / f"{ts}-{_slug(key)}.html"
            fn_out.write_bytes(payload)
            saved += 1
            time.sleep(self.delay)
        return {"method": "commoncrawl", "saved": saved, "captures": len(captures)}

    # ── method 5: screenshot (visual evidence only) ────────────────────────
    def fetch_via_screenshot(self, url: str, output_dir: str) -> dict:
        """Render the page to a PNG via thum.io (free screenshot service).

        NOTE: the output is an image — it is saved for visual verification and
        manual adjudication, not for the text parser. Not in the default
        method list; enable explicitly via config or per-site preference."""
        out = Path(output_dir) / "free-access" / "screenshot"
        out.mkdir(parents=True, exist_ok=True)
        try:
            raw = _get(THUMIO.format(url=url), 90, self.user_agent)
        except Exception as exc:  # noqa: BLE001
            return {"method": "screenshot", "saved": 0, "error": f"{type(exc).__name__}"}
        if not raw.startswith(b"\x89PNG") and not raw.startswith(b"\xff\xd8\xff"):
            return {"method": "screenshot", "saved": 0, "error": "not-an-image"}
        if len(raw) < 20000:  # tiny image = service error placeholder
            return {"method": "screenshot", "saved": 0, "error": "placeholder-image"}
        path = out / f"{_slug(url)}.png"
        path.write_bytes(raw)
        time.sleep(self.delay)
        return {"method": "screenshot", "saved": 1, "bytes": len(raw)}

    # ── method 3: Google Translate proxy ───────────────────────────────────
    def fetch_via_translate(self, url: str, output_dir: str) -> dict:
        """Fetch a page through Google Translate (server-side fetch)."""
        out = Path(output_dir) / "free-access" / "translate"
        out.mkdir(parents=True, exist_ok=True)
        try:
            raw = _get(TRANSLATE_URL.format(u=urllib.parse.quote(url, safe="")),
                       self.timeout, self.user_agent)
        except Exception as exc:  # noqa: BLE001
            return {"method": "translate", "saved": 0, "error": f"{type(exc).__name__}"}
        if len(raw) < 2000:
            return {"method": "translate", "saved": 0, "error": "empty-or-blocked"}
        path = out / f"{_slug(url)}.html"
        path.write_bytes(raw)
        time.sleep(self.delay)
        return {"method": "translate", "saved": 1, "bytes": len(raw)}

    # ── method 4: archive.today ────────────────────────────────────────────
    def fetch_via_archive_today(self, url: str, output_dir: str) -> dict:
        """Fetch the newest archive.today snapshot of a page, if one exists.

        archive.today blocks many datacenter IPs (SSL handshake failure) but is
        reachable from residential/operator networks. The `/newest/` endpoint
        redirects to the newest snapshot; if no snapshot exists the service
        returns a "No results" page, which we treat as a miss."""
        out = Path(output_dir) / "free-access" / "archivetoday"
        out.mkdir(parents=True, exist_ok=True)
        for host in ARCHIVE_TODAY_HOSTS:
            try:
                raw = _get(ARCHIVE_TODAY_NEWEST.format(host=host, url=url),
                           self.timeout, self.user_agent)
            except Exception:  # noqa: BLE001
                continue
            text = raw.decode("utf-8", errors="replace")
            # "No results" page = no snapshot for this URL; a real snapshot is
            # a full HTML document much larger than the search shell.
            if len(raw) < 800 or "No results" in text:
                continue
            path = out / f"{_slug(url)}.html"
            path.write_bytes(raw)
            time.sleep(self.delay)
            return {"method": "archivetoday", "saved": 1, "bytes": len(raw),
                    "host": host}
        return {"method": "archivetoday", "saved": 0,
                "error": "no-snapshot-or-blocked"}

    # ── orchestrator ───────────────────────────────────────────────────────
    def fetch_for_supplier(self, url: str, output_dir: str,
                           methods: Optional[List[str]] = None) -> dict:
        """Run all working free-access methods for one supplier.

        methods: subset of ("jina", "wayback", "commoncrawl", "translate",
        "archivetoday", "screenshot"); default = DEFAULT_FREE_ACCESS_METHODS.
        Returns a per-method dict plus "total_saved": N."""
        methods = methods or DEFAULT_FREE_ACCESS_METHODS
        stats: dict = {}
        total = 0
        for m in methods:
            try:
                if m == "jina":
                    r = self.fetch_via_jina(url, output_dir)
                elif m == "wayback":
                    r = self.fetch_via_wayback(url, output_dir)
                elif m == "spn2":
                    r = self.fetch_via_spn2(url, output_dir)
                elif m == "commoncrawl":
                    r = self.fetch_via_commoncrawl(url, output_dir)
                elif m == "translate":
                    r = self.fetch_via_translate(url, output_dir)
                elif m == "archivetoday":
                    r = self.fetch_via_archive_today(url, output_dir)
                elif m == "screenshot":
                    r = self.fetch_via_screenshot(url, output_dir)
                else:
                    continue
                stats[m] = r
                total += int(r.get("saved", 0) or 0)
            except Exception as exc:  # noqa: BLE001
                stats[m] = {"method": m, "saved": 0, "error": f"{type(exc).__name__}"}
        stats["total_saved"] = total
        return stats

    # ── v2.16: exhaustive ordered failover with method cache (F4) ──────────
    def _relay(self, m: str, url: str, output_dir: str) -> dict:
        if m == "jina":
            return self.fetch_via_jina(url, output_dir)
        if m == "wayback":
            return self.fetch_via_wayback(url, output_dir)
        if m == "spn2":
            return self.fetch_via_spn2(url, output_dir)
        if m == "commoncrawl":
            return self.fetch_via_commoncrawl(url, output_dir)
        if m == "translate":
            return self.fetch_via_translate(url, output_dir)
        if m == "archivetoday":
            return self.fetch_via_archive_today(url, output_dir)
        if m == "screenshot":
            return self.fetch_via_screenshot(url, output_dir)
        return {"method": m, "saved": 0, "error": "unknown_method"}

    def fetch_with_failover(self, url: str, output_dir: str,
                            methods: Optional[List[str]] = None,
                            host_key: Optional[str] = None,
                            cache_path: Optional[str] = None) -> dict:
        """Exhaustive ordered relay failover (strategy F4).

        Tries the free-access relays IN ORDER (jina -> wayback ->
        commoncrawl -> translate -> archivetoday) and STOPS at the first
        method that saves a page. When ``host_key`` + ``cache_path`` are
        given, the last working method per host is cached (JSON) and tried
        FIRST on subsequent runs — the per-supplier ``free_access_methods``
        fingerprints become self-maintaining.

        Returns the full per-method stats plus ``method_used`` (the relay
        that delivered the page, or None when all failed).
        """
        from urllib.parse import urlparse
        methods = methods or list(DEFAULT_FREE_ACCESS_METHODS)
        host_key = host_key or urlparse(url).netloc
        cache: dict = {}
        if cache_path and os.path.exists(cache_path):
            try:
                cache = json.load(open(cache_path, encoding="utf-8"))
            except (OSError, ValueError):
                cache = {}
        cached_method = (cache.get(host_key) or {}).get("method")
        ordered = [m for m in methods]
        if cached_method and cached_method in ordered:
            ordered.remove(cached_method)
            ordered.insert(0, cached_method)
        stats: dict = {"method_used": None}
        for m in ordered:
            try:
                r = self._relay(m, url, output_dir)
            except Exception as exc:  # noqa: BLE001
                r = {"method": m, "saved": 0,
                     "error": f"{type(exc).__name__}"}
            stats[m] = r
            if int(r.get("saved", 0) or 0) > 0:
                stats["method_used"] = m
                if cache_path:
                    try:
                        cache[host_key] = {"method": m,
                                           "ts": time.time()}
                        os.makedirs(os.path.dirname(cache_path) or ".",
                                    exist_ok=True)
                        tmp = cache_path + ".tmp"
                        with open(tmp, "w", encoding="utf-8") as fh:
                            json.dump(cache, fh, indent=1)
                        os.replace(tmp, cache_path)
                    except OSError:
                        pass
                break
        stats["total_saved"] = sum(int(s.get("saved", 0) or 0)
                                   for k, s in stats.items()
                                   if isinstance(s, dict) and k != "method_used")
        return stats
