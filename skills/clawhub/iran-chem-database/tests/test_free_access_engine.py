"""v2.6 regression tests — free-access engine (Jina/Wayback/Translate/archivetoday)
+ markdown parser + per-site preference lookup."""
import json
from pathlib import Path

from src.crawler.free_access_engine import (
    FreeAccessEngine, DEFAULT_FREE_ACCESS_METHODS, ARCHIVE_TODAY_HOSTS,
)
from src.discovery.seed_list import free_access_preference
from src.parser.markdown_parser import MarkdownCatalogParser


def test_cdx_rows_parsed():
    raw = json.dumps([
        ["timestamp", "original"],
        ["20250101000000", "https://example.ir/product/methanol"],
        ["20240101000000", "https://example.ir/"],
    ]).encode()
    rows = FreeAccessEngine._parse_cdx_rows(raw)
    assert len(rows) == 2
    assert rows[0][1].endswith("/product/methanol")


def test_cdx_rows_empty_on_garbage():
    assert FreeAccessEngine._parse_cdx_rows(b"not json") == []


def test_slug_normalizes_host():
    from src.crawler.free_access_engine import _slug
    assert _slug("https://www.Rock-Chemie.com/") == "rock-chemie.com"


def test_markdown_parser_extracts_cas(tmp_path):
    md = tmp_path / "page.md"
    md.write_text(
        "# Products\n\nMethanol, HPLC grade, CAS 67-56-1, purity 99.9%\n\n"
        "Acetone (CAS 67-64-1) 99.5%\n\n"
        "No chemical here, just text.\n\n"
        "![](https://example.com/img.png)\n\nContact us\n",
        "utf-8",
    )
    out = MarkdownCatalogParser().parse_file(str(md), supplier_id=7)
    cas_set = {r["cas_number"] for r in out}
    assert "67-56-1" in cas_set
    assert "67-64-1" in cas_set
    assert all(r["_extraction_method"] == "markdown-text" for r in out)


def test_markdown_parser_ignores_boilerplate(tmp_path):
    md = tmp_path / "page.md"
    md.write_text("Title: Home\nURL Source: https://x.ir\n\nCopyright 2026\n", "utf-8")
    assert MarkdownCatalogParser().parse_file(str(md), 1) == []


def test_markdown_parser_skips_non_markdown():
    p = MarkdownCatalogParser()
    assert p.parse_file("no_such_file.md", 1) == []
    # a .json file must not be parsed by this parser
    assert p.parse_file("data.json", 1) == []


def test_default_methods_include_archivetoday():
    assert "archivetoday" in DEFAULT_FREE_ACCESS_METHODS
    # v2.7.1: jina, wayback, commoncrawl, spn2, translate, archivetoday
    assert len(DEFAULT_FREE_ACCESS_METHODS) == 6


def test_archive_today_hosts_configured():
    assert ARCHIVE_TODAY_HOSTS
    assert all(h.startswith("https://archive.") for h in ARCHIVE_TODAY_HOSTS)


def test_free_access_preference_wayback_only_sites():
    # hardest-blocked sites: Jina/Translate both fail -> archives only
    # (v2.7 adds Common Crawl as a second source)
    assert free_access_preference("https://www.novichem.ir/") == ["wayback", "commoncrawl", "spn2"]
    assert free_access_preference("https://www.pgsoc.ir/") == ["wayback", "commoncrawl", "spn2"]
    assert free_access_preference("https://www.mahdistejarat.com/") == ["wayback", "commoncrawl", "spn2"]


def test_free_access_preference_full_trio_sites():
    assert free_access_preference("https://www.artinkimya.com/") == ["jina", "wayback", "translate", "spn2"]
    # rockchemie has Common Crawl captures, so commoncrawl is inserted
    assert free_access_preference("https://www.rockchemie.com/") == ["jina", "wayback", "commoncrawl", "translate", "spn2"]
    assert free_access_preference("https://www.pakshoo.com/") == ["jina", "wayback", "translate", "spn2"]


def test_free_access_preference_specific_site():
    assert free_access_preference("https://www.basparsazan.com/") == ["jina", "translate", "spn2"]
    assert free_access_preference("https://www.tebgostar.com/") == ["jina", "translate", "wayback", "spn2"]


def test_free_access_preference_unknown_domain_falls_back():
    assert free_access_preference("https://example.com/") == DEFAULT_FREE_ACCESS_METHODS


def test_free_access_preference_www_and_apex_equivalent():
    assert free_access_preference("https://www.novichem.ir") == free_access_preference("https://novichem.ir")


# ── v2.7: Common Crawl + screenshot ─────────────────────────────────────────
def test_default_methods_include_commoncrawl():
    assert "commoncrawl" in DEFAULT_FREE_ACCESS_METHODS
    assert "screenshot" not in DEFAULT_FREE_ACCESS_METHODS  # opt-in, image-only


def test_warc_payload_extraction_plain():
    record = (b"WARC/1.0\r\nWARC-Type: response\r\nContent-Length: 999\r\n\r\n"
              b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
              b"<html><body>Rock Chemie 700 products</body></html>")
    body = FreeAccessEngine._extract_warc_payload(record)
    assert b"Rock Chemie" in body
    assert b"HTTP/1.1" not in body


def test_warc_payload_extraction_chunked():
    body_chunked = b"1c\r\n<html><body>rockchemie</body>\r\n0\r\n\r\n"
    record = (b"WARC/1.0\r\nWARC-Type: response\r\n\r\n"
              b"HTTP/1.1 200 OK\r\nTransfer-Encoding: chunked\r\n\r\n" + body_chunked)
    body = FreeAccessEngine._extract_warc_payload(record)
    assert b"rockchemie" in body
    assert b"1c\r\n" not in body  # chunk framing removed


def test_warc_payload_extraction_gzip():
    import gzip
    html = b"<html><body>artinkimya catalog</body></html>"
    gz = gzip.compress(html)
    record = (b"WARC/1.0\r\n\r\n"
              b"HTTP/1.1 200 OK\r\nContent-Encoding: gzip\r\n\r\n" + gz)
    body = FreeAccessEngine._extract_warc_payload(record)
    assert b"artinkimya" in body


def test_free_access_preference_commoncrawl_sites():
    # pgsoc.ir: wayback-only now has a Common Crawl second source
    assert free_access_preference("https://www.pgsoc.ir/") == ["wayback", "commoncrawl", "spn2"]
    assert free_access_preference("https://www.novichem.ir/") == ["wayback", "commoncrawl", "spn2"]
    # rockchemie has CC captures (27) in addition to the live trio
    assert "commoncrawl" in free_access_preference("https://www.rockchemie.com/")


def test_commoncrawl_index_url_format():
    from src.crawler.free_access_engine import COMMONCRAWL_INDEX
    assert "%2A" in COMMONCRAWL_INDEX  # wildcard path
    assert COMMONCRAWL_INDEX.startswith("https://index.commoncrawl.org/")


# ── v2.7.1: SPN2 (Save Page Now) ────────────────────────────────────────────
def test_default_methods_include_spn2():
    assert "spn2" in DEFAULT_FREE_ACCESS_METHODS
    assert len(DEFAULT_FREE_ACCESS_METHODS) == 6


def test_free_access_preference_always_includes_spn2():
    # even wayback-only sites get spn2 appended (forces a fresh capture)
    assert free_access_preference("https://www.novichem.ir/")[-1] == "spn2"
    assert free_access_preference("https://www.rockchemie.com/")[-1] == "spn2"


def test_spn2_timestamp_regex():
    import re
    from src.crawler.free_access_engine import SPN2_TS_RE
    m = re.search(SPN2_TS_RE, "web.archive.org/web/20260822015418/https://www.rockchemie.com/")
    assert m and m.group(1) == "20260822015418"
