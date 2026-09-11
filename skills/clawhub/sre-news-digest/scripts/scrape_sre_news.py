#!/usr/bin/env python3
"""
Fetch recent SRE news articles from the RSS feed at https://news.imzye.com/rss.xml.
Outputs a JSON array of {title, url, source, date} to stdout.

Usage:
    python scrape_sre_news.py [days]

Arguments:
    days  Number of most recent days to include (default: 1). Each RSS item
          represents one day of articles, so `days=1` returns today's (or the
          most recently published) list.
"""

import json
import re
import sys
import xml.etree.ElementTree as ET
from html import unescape
from html.parser import HTMLParser
from urllib.parse import urlparse
from urllib.request import urlopen, Request

RSS_URL = "https://news.imzye.com/rss.xml"


# Map common domains to human-readable source names
SOURCE_MAP = {
    "kubernetes.io": "Kubernetes Blog",
    "etcd.io": "etcd Blog",
    "www.datadoghq.com": "Datadog Blog",
    "victoriametrics.com": "VictoriaMetrics Blog",
    "dev.to": "DEV Community",
    "thenewstack.io": "The New Stack",
    "www.infoq.com": "InfoQ",
    "devops.com": "DevOps.com",
    "techcommunity.microsoft.com": "Microsoft Tech Community",
    "aws.amazon.com": "AWS Blog",
    "cloud.google.com": "Google Cloud Blog",
    "www.cncf.io": "CNCF Blog",
    "grafana.com": "Grafana Blog",
    "www.hashicorp.com": "HashiCorp Blog",
    "blog.cloudflare.com": "Cloudflare Blog",
    "www.redhat.com": "Red Hat Blog",
    "cybersecuritynews.com": "Cyber Security News",
    "www.akamai.com": "Akamai Blog",
    "auth0.com": "Auth0 Blog",
    "www.mongodb.com": "MongoDB Blog",
    "forem.com": "Forem",
    "freek.dev": "Freek.dev",
    "www.51sec.org": "51Sec Blog",
    "observability-360.beehiiv.com": "Observability 360",
}


def source_from_url(url):
    """Derive a human-readable source/publication name from a URL."""
    hostname = urlparse(url).hostname or ""
    if hostname in SOURCE_MAP:
        return SOURCE_MAP[hostname]
    # Strip www. prefix and use domain as fallback
    name = hostname.lstrip("www.").split(".")[0] if hostname else "Unknown"
    return name.capitalize()


def title_from_url(url):
    """Extract a human-readable title from a URL path slug."""
    path = urlparse(url).path.rstrip("/")
    slug = path.split("/")[-1] if path else ""
    # Remove common hash/id suffixes (e.g., -21pi, -4d40)
    slug = re.sub(r'-[a-z0-9]{2,5}$', '', slug)
    title = slug.replace("-", " ").replace("_", " ").strip()
    return title.title() if title else url


class DescriptionParser(HTMLParser):
    """Parse an RSS item <description> HTML <ul> list into (title, url) pairs."""

    def __init__(self):
        super().__init__()
        self.articles = []
        self._in_li = False
        self._in_link = False
        self._in_code = False
        self._title_parts = []
        self._url = None

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self._in_li = True
            self._title_parts = []
            self._url = None
        elif tag == "a" and self._in_li:
            href = dict(attrs).get("href")
            if href:
                self._in_link = True
                self._url = href
        elif tag == "code" and self._in_li and not self._in_link:
            self._in_code = True
            self._title_parts.append("`")

    def handle_endtag(self, tag):
        if tag == "a":
            self._in_link = False
        elif tag == "code" and self._in_code:
            self._in_code = False
            self._title_parts.append("`")
        elif tag == "li" and self._in_li:
            self._in_li = False
            raw_title = " ".join("".join(self._title_parts).split())
            if self._url:
                title = unescape(raw_title).strip()
                if not title or title == ">_":
                    title = title_from_url(self._url)
                self.articles.append((title, self._url))

    def handle_data(self, data):
        if self._in_li and not self._in_link:
            self._title_parts.append(data)


def fetch_rss(url=RSS_URL):
    """Fetch the RSS feed and return raw bytes."""
    req = Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; SRENewsDigest/1.0)"
    })
    with urlopen(req, timeout=30) as resp:
        return resp.read()


def parse_feed(data):
    """Parse RSS XML bytes into a list of article dicts (newest day first)."""
    root = ET.fromstring(data)
    articles = []
    for item in root.findall("./channel/item"):
        title = (item.findtext("title") or "").strip()
        description = item.findtext("description") or ""

        # The item title is the ISO date for that day's digest (e.g. 2026-09-08)
        date = title if re.match(r"^\d{4}-\d{2}-\d{2}$", title) else None

        parser = DescriptionParser()
        parser.feed(description)
        for art_title, url in parser.articles:
            article = {
                "title": art_title,
                "url": url,
                "source": source_from_url(url),
            }
            if date:
                article["date"] = date
            articles.append(article)
    return articles


def scrape_sre_news(days=1):
    """Fetch the RSS feed and return articles from the most recent N days."""
    articles = parse_feed(fetch_rss())

    # Deduplicate by URL, preserving order (newest day first)
    seen = set()
    unique = []
    for a in articles:
        if a["url"] not in seen:
            seen.add(a["url"])
            unique.append(a)

    # Keep only the most recent `days` distinct dates
    if days and any("date" in a for a in unique):
        dates = sorted({a["date"] for a in unique if "date" in a}, reverse=True)
        keep_dates = set(dates[:days])
        return [a for a in unique if a.get("date") in keep_dates]

    return unique


if __name__ == "__main__":
    days = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    articles = scrape_sre_news(days)
    print(json.dumps(articles, indent=2, ensure_ascii=False))
    print(f"\n# Total: {len(articles)} articles found", file=sys.stderr)
