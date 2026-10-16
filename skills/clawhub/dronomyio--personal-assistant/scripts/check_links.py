#!/usr/bin/env python3
"""Polite broken-link checker for your own sites (stdlib only).

Usage:
    python3 check_links.py --sites-file sites.json            # all sites in file
    python3 check_links.py --sites-file sites.json mysite     # one site by slug

sites.json format:
    {"mysite": "https://example.com", "blog": "https://blog.example.com"}

Writes per-site JSON to <out-dir>/<slug>/reports/YYYY-MM-DD.json
(default out-dir: ~/workspace/site-health).
Covers internal links found in server-rendered HTML. Heavily JS-rendered
pages are a lower bound — noted in reports.
"""
import argparse
import json
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from html.parser import HTMLParser
from datetime import datetime, timezone
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (compatible; SiteHealthBot/1.0)"}


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for k, v in attrs:
                if k == "href" and v and v.strip():
                    self.links.add(v.strip())


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            ctype = r.headers.get("Content-Type", "")
            body = r.read(2_000_000) if "text/html" in ctype else b""
            return r.status, ctype, body, ""
    except urllib.error.HTTPError as e:
        return e.code, "", b"", ""
    except Exception as e:
        return -1, "", b"", str(e)[:150]


def check_url(url, timeout=20):
    try:
        req = urllib.request.Request(url, headers=UA, method="HEAD")
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, ""
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 501):
            st, _, _, err = fetch(url, timeout)
            return st, err
        return e.code, ""
    except Exception:
        st, _, _, err = fetch(url, timeout)
        return (st, err) if st != -1 else (-1, "fetch failed")


def norm(url):
    return urllib.parse.urldefrag(url)[0].rstrip("/")


def crawl(site_url, max_pages=25, delay=0.3):
    host = urllib.parse.urlparse(site_url).netloc
    seen, queue, checked = set(), [site_url], set()
    broken, page_status = [], {}
    while queue and len(seen) < max_pages:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        st, ctype, body, err = fetch(url)
        page_status[url] = {"status": st, "error": err}
        if st != 200:
            broken.append({"url": url, "status": st, "error": err, "found_on": "crawl"})
        elif "text/html" in ctype and body:
            ext = LinkExtractor()
            try:
                ext.feed(body.decode("utf-8", "ignore"))
            except Exception:
                pass
            for href in ext.links:
                if href.startswith(("mailto:", "tel:", "javascript:", "data:")):
                    continue
                absu = norm(urllib.parse.urljoin(url, href))
                p = urllib.parse.urlparse(absu)
                if p.scheme not in ("http", "https") or p.netloc != host:
                    continue
                if absu in checked or absu in seen:
                    continue
                checked.add(absu)
                cs, cerr = check_url(absu)
                if cs != 200:
                    broken.append({"url": absu, "status": cs, "error": cerr, "found_on": url})
                elif absu not in queue and len(seen) + len(queue) < max_pages:
                    queue.append(absu)
        time.sleep(delay)
    return {
        "site": site_url,
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "pages_crawled": len(seen),
        "links_checked": len(checked),
        "broken": broken,
        "page_status": page_status,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sites-file", required=True,
                    help="JSON file mapping slug -> site URL")
    ap.add_argument("slug", nargs="?", default=None,
                    help="check one site by slug (default: all)")
    ap.add_argument("--out-dir", default=str(Path.home() / "workspace" / "site-health"))
    a = ap.parse_args()

    sites = json.loads(Path(a.sites_file).read_text())
    if a.slug:
        if a.slug not in sites:
            print(f"unknown slug {a.slug!r}; known: {sorted(sites)}", file=sys.stderr)
            sys.exit(1)
        targets = [(a.slug, sites[a.slug])]
    else:
        targets = list(sites.items())
    base = Path(a.out_dir)
    for slug, site_url in targets:
        print(f"crawling {site_url} ...", flush=True)
        rep = crawl(site_url)
        outdir = base / slug / "reports"
        outdir.mkdir(parents=True, exist_ok=True)
        day = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        (outdir / f"{day}.json").write_text(json.dumps(rep, indent=1))
        print(
            f"  {rep['pages_crawled']} pages, {rep['links_checked']} links, "
            f"{len(rep['broken'])} broken -> {outdir}/{day}.json",
            flush=True,
        )


if __name__ == "__main__":
    main()
