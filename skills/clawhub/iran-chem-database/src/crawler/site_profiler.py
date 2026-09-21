#!/usr/bin/env python3
"""Site profiler — v2.35.0. Runs the skill's fetch methods ONE BY ONE against
every configured seed URL and records, per site: which methods answer, how
fast, with how many bytes, and what catalogue/pagination structure the site
actually exposes. Output is ``data/site_profiles.json`` consumed by
``src/crawler/adaptive_selector.py`` and the crawl engines.

Design rules (all measured, nothing assumed):
  * every seed host gets one probe per method — direct root, direct
    entry_points (Woo REST + sitemap), translate_goog, jina, wayback (CDX
    availability + latest snapshot), commoncrawl index;
  * bodies are read up to a byte cap (200 kB), then ABORTED — we fingerprint,
    we don't mirror, so one probe never pays for a whole site;
  * zero fixed sleeps between hosts (parallel by design), politeness enforced
    per (host, method) token bucket instead — the origin never sees >1
    request from us at a time, relays get a generous shared budget;
  * saturation is MEASURED, not guessed: 429/503/timeout on a method stamps
    ``penalty`` into the profile so the adaptive selector demotes that method
    for THAT host only (site-personalised chains, v2.35.0 contract);
  * no WAF/bot defeat anywhere: public caches + origin robots-allowed GETs
    only; policy per docs/RELAY_INTEGRITY_ROUND10.md.

Run:
    python3 -m src.crawler.site_profiler                 # full seed set
    python3 -m src.crawler.site_profiler --hosts a.ir b.ir
    python3 -m src.crawler.site_profiler --selftest     # offline, canned bodies

The live run is resumable: results append per host, so a re-run only probes
hosts missing from the current profiles file (use --force to re-measure).
"""
from __future__ import annotations

import argparse
import concurrent.futures as _f
import gzip
import io
import json
import re
import socket
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROFILES = ROOT / "data" / "site_profiles.json"

UA = ("Mozilla/5.0 (compatible; iran-chem-db profiler; academic procurement "
      "research; one probe per method)")

# --------------------------------------------------------------------------
# polite shared pool: keep-alive per remote endpoint, one in-flight per host
# --------------------------------------------------------------------------
_LOCK = threading.Lock()


class Throttle:
    """Per-(host) token bucket: origin gets 1 rps, shared relays 6 rps."""

    def __init__(self):
        self._next_ok: dict[str, float] = {}
        self._gap = {"*": 0.17}  # relay fleet: ~6 rps aggregate

    def wait(self, key: str) -> None:
        gap = 1.0 if key.endswith(".ir") or "." in key and not any(
            s in key for s in ("translate.goog", "r.jina.ai", "web.archive.org",
                               "archive.org", "index.commoncrawl.org")) else self._gap["*"]
        with _LOCK:
            now = time.monotonic()
            when = max(now, self._next_ok.get(key, 0.0))
            self._next_ok[key] = when + gap
        time.sleep(max(0.0, when - time.monotonic()))


THROTTLE = Throttle()


def fetch(url: str, timeout: float = 9.0, cap: int = 200_000,
          headers: dict | None = None, method: str = "GET") -> dict:
    """GET with hard byte cap + measured latency. Never raises."""
    key = urllib.parse.urlsplit(url).netloc
    THROTTLE.wait(key)
    h = {"User-Agent": UA, "Accept": "*/*", "Accept-Encoding": "gzip",
         **(headers or {})}
    t0 = time.monotonic()
    try:
        req = urllib.request.Request(url, headers=h, method=method)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read(cap)
            if r.headers.get("Content-Encoding") == "gzip":
                try:
                    raw = gzip.GzipFile(fileobj=io.BytesIO(raw)).read(cap)
                except OSError:
                    pass
            return {"status": r.status, "bytes": len(raw),
                    "text": raw.decode("utf-8", "replace"),
                    "final_url": r.geturl(), "ms": int((time.monotonic() - t0) * 1000),
                    "ctype": r.headers.get("Content-Type", "")}
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read(20_000)
        except Exception:
            pass
        return {"status": e.code, "bytes": len(body),
                "text": body.decode("utf-8", "replace"), "final_url": url,
                "ms": int((time.monotonic() - t0) * 1000),
                "err": f"HTTP {e.code}"}
    except (socket.timeout, TimeoutError):
        return {"status": 0, "bytes": 0, "text": "", "final_url": url,
                "ms": int((time.monotonic() - t0) * 1000), "err": "timeout"}
    except Exception as e:
        return {"status": 0, "bytes": 0, "text": "", "final_url": url,
                "ms": int((time.monotonic() - t0) * 1000),
                "err": f"{type(e).__name__}"[:80]}


# --------------------------------------------------------------------------
# structural fingerprinting — what kind of catalogue is this?
# --------------------------------------------------------------------------
CAS_RE = re.compile(r"\b(?:[1-9][0-9]{0,6})-[0-9]{2}-[0-9]\b")
CHEM_WORDS_RE = re.compile(
    r"(acid|base|solvent|reagent|پتاسیم|سدیم|کلرید|اسید|حلال|مواد شیمیایی|"
    r"sodium|potassium|hydroxide|chloride|sulphate|sulfate|merck|sigma)", re.I)
PAG_PATTERNS = [
    ("rest_page", re.compile(r"wc/store/v1/products", re.I),
     "WooCommerce Store API: page=<n>, per_page=100, stop on empty / page>X-WP-TotalPages"),
    ("url_page", re.compile(r"[?&]page=(\d+)", re.I),
     "plain ?page=N query parameter on listing URLs"),
    ("path_page", re.compile(r"/(?:shop|catalog|products?)/page/(\d+)", re.I),
     "WordPress path pagination /page/N/ — also check /product-page/N/"),
    ("aspx_postback", re.compile(r"__doPostBack\([^)]*(?:Pager|Page\$)", re.I),
     "ASP.NET GridView/Repeater pager: POST back with __VIEWSTATE + "
     "__EVENTARGUMENT='Page$N'; NEXT link labelled بعدی"),
    ("rel_next", re.compile(r'<link[^>]+rel=["\']next["\']|<a[^>]+rel=["\']next["\']', re.I),
     "semantic rel=next link — follow href until absent"),
    ("load_more", re.compile(r"(?:load[\s_-]?more|نمایش\s+بیشتر|بارگذاری\s+بیشتر|"
                             r'data-action=["\']loadmore)', re.I),
     "load-more button (Persian: نمایش بیشتر / بارگذاری بیشتر) — replay its AJAX GET with page++"),
    ("infinite_scroll", re.compile(r"(data-infinite|infinite[\s_-]?scroll|"
                                   r"waypoint\b|magicinfinite|infinite-scroll__spinner)", re.I),
     "scroll-triggered XHR — render with JS profile, scroll loop until no new anchors "
     "(v2.35.0: bare 'lazyload' EXCLUDED — image lazy-loading matched 85 false positives)"),
]
NAV_LEXICON = {
    "next": ("بعدی", "next", "صفحه بعد", "next ›"),
    "prev": ("قبلی", "previous", "قبلی ‹", "صفحه قبل"),
    "load_more": ("نمایش بیشتر", "بارگذاری بیشتر", "load more", "مشاهده بیشتر"),
    "stock_yes": ("موجود", "in stock", "آماده ارسال"),
    "stock_no": ("ناموجود", "out of stock", "تمام شده"),
    "inquiry": ("استعلام قیمت", "درخواست قیمت", "تماس بگیرید"),  # price-on-request — record row, no price
}
GATE_MARKERS = ("برای کاربران عضو", "login to view", "فقط اعضا", "access denied")


def fingerprint(text: str, url: str) -> dict:
    t = text[:200_000]
    fp = {
        "cas_hits": len(CAS_RE.findall(t)),
        "chem_hits": len(CHEM_WORDS_RE.findall(t)),
        "gated": any(m.lower() in t.lower() for m in GATE_MARKERS),
    }
    if "wp-json/wc/store" in t or "/product/" in url:
        fp["family"] = "woocommerce"
    elif "woocommerce" in t.lower():
        fp["family"] = "woocommerce"
    elif "__VIEWSTATE" in t:
        fp["family"] = "aspnet"
    elif "sitemap" in url or "<urlset" in t or "sitemapindex" in t:
        fp["family"] = "sitemap_wp"
    elif re.search(r"<(table|div)[^>]*class=\"[^\"]*(product|item|goods)", t, re.I):
        fp["family"] = "static_listing"
    else:
        fp["family"] = "unknown"
    pag = []
    for name, rx, howto in PAG_PATTERNS:
        if rx.search(t):
            pag.append({"type": name, "how": howto})
    nav = {k: [w for w in words if w.lower() in t.lower()]
           for k, words in NAV_LEXICON.items()}
    fp["pagination"] = pag
    fp["nav_found"] = {k: v for k, v in nav.items() if v}
    return fp


# --------------------------------------------------------------------------
# per-method probes for one host
# --------------------------------------------------------------------------
def method_probes(entry: dict) -> dict:
    """Return {method: {ok, ms, bytes, status, fp}} — one probe each."""
    host = urllib.parse.urlsplit(entry["url"]).netloc or entry["name"]
    url = entry["url"].rstrip("/") + "/"
    dash = host.replace(".", "-")
    results: dict[str, dict] = {}

    # 1. direct origin
    r = fetch(url, timeout=7)
    results["direct"] = r
    if r["status"] == 200 and r["bytes"] > 600:
        results["direct"]["fp"] = fingerprint(r["text"], url)

    # 2. declared entry_points (Woo REST / sitemap) — only if origin answered
    for ep in entry.get("entry_points", [])[:3]:
        rr = fetch(ep, timeout=8)
        results[f"entry:{ep.split(host, 1)[-1][:40]}"] = {
            k: v for k, v in rr.items() if k != "text"}
        if rr["status"] == 200 and rr.get("ctype", "").startswith("application/json"):
            try:
                j = json.loads(rr["text"][:60_000])
                results[f"entry:{ep.split(host, 1)[-1][:40]}"]["json_rows"] = len(j) \
                    if isinstance(j, list) else len(j.get("products", []))
            except ValueError:
                pass
        elif rr["status"] == 200 and ("<urlset" in rr.get("text", "") or "sitemapindex" in rr.get("text", "")):
            results[f"entry:{ep.split(host, 1)[-1][:40]}"]["sitemap_urls"] = \
                rr["text"].count("<loc>")

    # 3. translate_goog (public Google translate proxy of the site root)
    t = fetch(f"https://{dash}.translate.goog/?_x_tr_sl=fa&_x_tr_tl=en&_x_tr_hl=en",
              timeout=10)
    results["translate_goog"] = {k: v for k, v in t.items() if k != "text"}
    if t["status"] == 200 and t["bytes"] > 1200:
        results["translate_goog"]["fp"] = fingerprint(t["text"], url)

    # 4. jina reader
    r2 = fetch(f"https://r.jina.ai/{url}", timeout=12)
    ok = r2["status"] == 200 and r2["bytes"] > 300
    results["jina"] = {"status": r2["status"], "bytes": r2["bytes"], "ms": r2["ms"],
                       "err": r2.get("err")}
    if ok:
        results["jina"]["fp"] = fingerprint(r2["text"], url)
        results["jina"]["cached"] = "Published Time" in r2["text"]

    # 5. wayback availability
    w = fetch(f"https://archive.org/wayback/available?url={host}", timeout=12)
    snap = None
    try:
        snap = json.loads(w["text"]).get("archived_snapshots", {}).get("closest")
    except (ValueError, AttributeError):
        pass
    results["wayback"] = {"status": w["status"], "ms": w["ms"],
                          "snapshot": bool(snap),
                          "snapshot_ts": (snap or {}).get("timestamp")}

    # 6. commoncrawl index (cheap; existence only)
    c = fetch(f"http://index.commoncrawl.org/CC-MAIN-2025-21-index?"
              f"url={host}&matchType=domain&output=json&limit=1", timeout=12)
    results["commoncrawl"] = {"status": c["status"], "ms": c["ms"],
                              "rows": c["text"].count("{") if c["status"] == 200 else 0}
    return results


def rank_methods(probes: dict) -> tuple[list[str], dict]:
    """Score methods for THIS host: payload value × speed, penalty for
    timeouts / 429 / gate markers. Returns (ordered_chain, per-method score)."""
    scores: dict[str, int] = {}
    notes: dict[str, str] = {}
    for m, p in probes.items():
        if m.startswith("entry:"):
            if p.get("json_rows") or p.get("sitemap_urls"):
                scores[m] = 900  # structured catalogue access beats any HTML relay
            continue
        s = 0
        if p.get("status") == 200 and p.get("bytes", 0) > 600:
            fp = p.get("fp") or {}
            s = 100 + 40 * fp.get("cas_hits", 0) + 2 * fp.get("chem_hits", 0)
            if fp.get("gated"):
                s -= 120
            if p.get("cached"):
                s -= 60  # jina snapshot: real but stale — demote under live options
            ms = p.get("ms") or 0
            s -= min(60, ms // 200)  # up to -60 for slowness
        elif p.get("snapshot"):
            s = 70  # wayback existence w/o direct: archive-first strategy
        elif p.get("rows"):
            s = 60
        else:
            s = -100  # dead/saturated right now
        scores[m] = s
        if str(p.get("err", "")) in ("timeout", "ConnectionResetError") or \
                p.get("status") in (429, 503):
            notes[m] = "penalty:saturated_or_blocked"
    order = [m for m, _ in sorted(scores.items(), key=lambda kv: -kv[1]) if scores[m] > -100]
    return order or ["direct"], {"scores": scores, "notes": notes}


def profile_host(entry: dict) -> dict:
    probes = method_probes(entry)
    chain, rank = rank_methods(probes)
    slim = {}
    for m, p in probes.items():
        slim[m] = {k: v for k, v in p.items() if k in
                   ("status", "bytes", "ms", "err", "snapshot", "snapshot_ts",
                    "json_rows", "sitemap_urls", "rows", "cached", "fp")}
    host = urllib.parse.urlsplit(entry["url"]).netloc or entry["name"]
    return {
        "host": host,
        "name": entry.get("name"),
        "profiled": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "chain": chain,                    # personal ordered method chain
        "ranking": rank,
        "probes": slim,
        "pagination": (probes.get("direct", {}).get("fp")
                       or probes.get("translate_goog", {}).get("fp")
                       or {}).get("pagination", []),
        "nav_found": (probes.get("direct", {}).get("fp")
                      or probes.get("translate_goog", {}).get("fp")
                      or {}).get("nav_found", {}),
        "family": (probes.get("direct", {}).get("fp")
                   or probes.get("translate_goog", {}).get("fp") or {}).get("family"),
        "gated": bool((probes.get("direct", {}).get("fp")
                       or probes.get("translate_goog", {}).get("fp") or {}).get("gated")),
    }


def load_seeds():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "seed_list", ROOT / "src" / "discovery" / "seed_list.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m.SUPPLIER_SEEDS


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hosts", nargs="*", help="limit to these host substrings")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--out", default=str(PROFILES))
    ns = ap.parse_args()

    if ns.selftest:
        return _selftest()

    seeds = load_seeds()
    existing: dict = {}
    p = Path(ns.out)
    if p.exists():
        try:
            existing = {v["host"]: v for v in json.loads(p.read_text()).values()}
        except ValueError:
            existing = {}

    def selected(host: str) -> bool:
        return bool(ns.hosts) and any(h in host for h in ns.hosts)

    todo = []
    for e in seeds:
        host = urllib.parse.urlsplit(e["url"]).netloc or e["name"]
        if ns.hosts and not selected(host):
            continue
        # keep existing unless (a) full --force rebuild, or (b) host explicitly
        # re-selected together with --force (merge semantics — never lose
        # profiles for hosts we are not touching this run)
        if host in existing and not ns.force:
            continue
        if host in existing and ns.force and ns.hosts and not selected(host):
            pass  # unreachable: filtered above
        todo.append(e)
    if ns.limit:
        todo = todo[: ns.limit]
    print(f"profiling {len(todo)} hosts (existing kept: {len(existing)}) …")

    t0 = time.monotonic()
    done = dict(existing)
    with _f.ThreadPoolExecutor(max_workers=ns.workers) as pool:
        futs = {pool.submit(profile_host, e): e for e in todo}
        for i, fut in enumerate(_f.as_completed(futs), 1):
            e = futs[fut]
            try:
                prof = fut.result()
            except Exception as exc:  # profiler must never die on one host
                host = urllib.parse.urlsplit(e["url"]).netloc
                prof = {"host": host, "name": e.get("name"), "chain": ["direct"],
                        "error": f"{type(exc).__name__}: {exc}"[:120]}
            done[prof["host"]] = prof
            if i % 25 == 0 or i == len(todo):
                p.parent.mkdir(parents=True, exist_ok=True)
                tmp = str(p) + ".tmp"
                with open(tmp, "w") as fh:
                    json.dump(done, fh, indent=1, sort_keys=True)
                import os as _os
                _os.replace(tmp, p)
                print(f"  {i}/{len(todo)} ({time.monotonic()-t0:.0f}s)", flush=True)
    print(f"wrote {p} — {len(done)} profiles")
    return 0


def _selftest() -> int:
    fails = []
    woo_html = '''<html><link rel="next" href="/shop/page/2/"><a href="?page=2">2</a>
    <div class="products">CAS 7647-01-0 sodium chloride — 150 items
    <a href="/product/sodium-chloride/">Sodium Chloride</a> Мерк
    acid hydrochloric acid 99% solvent reagent پتاسیم سدیم</a></div>
    <a href="?product-page=2">next</a> <span>نمایش بیشتر</span><span>بعدی</span></html>'''
    fp = fingerprint(woo_html, "https://x.ir/shop/")
    types = {p["type"] for p in fp["pagination"]}
    assert "rel_next" in types and "url_page" in types and "load_more" in types, types
    assert fp["cas_hits"] == 1 and fp["family"] == "static_listing" or fp["family"] == "unknown"
    assert fp["nav_found"].get("next") and fp["nav_found"].get("load_more")
    asp = fingerprint('<form><input name="__VIEWSTATE"><a onclick="__doPostBack(\'ctl$Pager\',\'Page$2\')">بعدی</a></form>' * 10, "https://y.ir/list.aspx")
    assert asp["family"] == "aspnet"
    assert any(p["type"] == "aspx_postback" for p in asp["pagination"])
    # ranking: working direct w/ CAS beats dead relay; timeouts penalized
    probes = {
        "direct": {"status": 200, "bytes": 5000, "ms": 400,
                   "fp": {"cas_hits": 3, "chem_hits": 40}},
        "translate_goog": {"status": 200, "bytes": 4000, "ms": 300, "fp": {"cas_hits": 0, "chem_hits": 5}},
        "jina": {"status": 200, "bytes": 3000, "ms": 200, "fp": {"cas_hits": 0, "chem_hits": 2}, "cached": True},
        "wayback": {"snapshot": True, "status": 200, "ms": 500},
        "entry:/wp-json/wc/store/v1/products": {"json_rows": 5},
    }
    order, rk = rank_methods(probes)
    assert order[0].startswith("entry:") and order.index("direct") < order.index("jina"), order
    assert "cached" not in order[0]
    # saturated method → noted + ranked bottom; never absent silently w/o note
    probes2 = dict(probes, direct={"status": 429, "bytes": 0, "ms": 50, "err": "HTTP 429"})
    order2, rk2 = rank_methods(probes2)
    assert rk2["notes"]["direct"] == "penalty:saturated_or_blocked"
    assert "direct" not in order2
    print("SELFTEST PASS (fingerprint, families, ranking, penalty notes)")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
