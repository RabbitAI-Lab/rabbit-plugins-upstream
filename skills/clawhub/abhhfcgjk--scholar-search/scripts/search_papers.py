#!/usr/bin/env python3
"""Search academic papers on Semantic Scholar and arXiv, dedupe, and save JSON with BibTeX citations.

Setup:
    python3 -m pip install -r ../requirements.txt

Optional (higher Semantic Scholar rate limits, 100 req/min instead of the shared pool):
    export SEMANTIC_SCHOLAR_API_KEY=<key from https://www.semanticscholar.org/product/api>

Examples:
    python3 scripts/search_papers.py "retrieval augmented generation" -o papers.json
    python3 scripts/search_papers.py "attention is all you need" --year 2017 --bib-file refs.bib
    python3 scripts/search_papers.py "retrieval augmented generation" --engine arxiv
    python3 scripts/search_papers.py "vision transformers" --min-citations 500 --sort-citations

Engines:
    both (default)              Searches Semantic Scholar and arXiv, then drops any arXiv result
                                that duplicates a Semantic Scholar hit (matched by arXiv ID, DOI, or title).
    semantic-scholar            Citation counts available; relevance-ranked.
    arxiv                       arXiv search query syntax (ti:, au:, abs:, all:); no citation counts.

Output JSON shape:
    {
      "query": "...",
      "searched_at": "...",
      "count": N,
      "engine": "semantic-scholar+arxiv" | "semantic-scholar" | "arxiv",
      "results": [
        {
          "paper_id": "...",
          "title": "...",
          "authors": [...],
          "year": 2017,
          "venue": "...",
          "journal": "...",
          "conference": "...",
          "citation_count": 12345,
          "url": "https://...",
          "abstract": "...",
          "doi": "...",
          "arxiv_id": "...",
          "bibtex": "@article{...}",
          "bibtex_source": "doi.org" | "arxiv" | "generated"
        }
      ]
    }

Requires: requests, beautifulsoup4 (see requirements.txt).
"""

import argparse
import json
import os
import re
import sys
import time
import warnings
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

GRAPH_API = "https://api.semanticscholar.org/graph/v1/paper/search"
DOI_URL = "https://doi.org"
ARXIV_API = "https://export.arxiv.org/api/query"
USER_AGENT = "search-papers-skill/1.0"
DEFAULT_FIELDS = "paperId,title,authors,year,venue,citationCount,externalIds,url,abstract"


def make_session(timeout=60):
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    retry = Retry(
        total=4,
        connect=2,
        status_forcelist=[429, 500, 502, 503, 504],
        backoff_factor=1.5,
        respect_retry_after_header=True,
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.timeout = timeout
    return session


def search(session, query, limit, offset, year, venue, api_key):
    params = {
        "query": query,
        "limit": limit,
        "offset": offset,
        "fields": DEFAULT_FIELDS,
    }
    if year:
        params["year"] = year
    if venue:
        params["venue"] = venue
    headers = {"x-api-key": api_key} if api_key else {}
    resp = session.get(GRAPH_API, params=params, headers=headers)
    resp.raise_for_status()
    return resp.json()


def fetch_bibtex_doi(session, doi):
    """Fetch BibTeX via DOI content negotiation (doi.org -> Crossref/DataCite)."""
    resp = session.get(f"{DOI_URL}/{doi}", headers={"Accept": "application/x-bibtex"})
    if not resp.ok:
        return None
    text = resp.text.strip()
    return text if text.startswith("@") else None


def parse_arxiv_entry(entry):
    def text_of(tag):
        node = entry.find(tag)
        return " ".join(node.get_text().split()) if node else ""

    authors = []
    for author in entry.find_all("author"):
        name = author.find("name")
        if name and name.get_text().strip():
            authors.append(" ".join(name.get_text().split()))
    published = text_of("published")
    year = int(published[:4]) if published[:4].isdigit() else None
    arxiv_id = ""
    id_url = text_of("id")
    match = re.search(r"/abs/([^/]+)$", id_url)
    if match:
        arxiv_id = match.group(1)
    primary = entry.find("arxiv:primary_category")
    journal_ref = text_of("arxiv:journal_ref")
    return {
        "paper_id": arxiv_id,
        "title": text_of("title"),
        "authors": authors,
        "year": year,
        "venue": journal_ref or "",
        "citation_count": None,
        "url": id_url,
        "abstract": text_of("summary"),
        "doi": text_of("arxiv:doi") or None,
        "arxiv_id": arxiv_id,
        "journal": journal_ref or None,
        "conference": None,
        "primary_class": primary.get("term") if primary else "",
    }


def arxiv_query(session, params):
    resp = session.get(ARXIV_API, params=params)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    return [parse_arxiv_entry(e) for e in soup.find_all("entry")]


def search_arxiv(session, query, limit, offset, year):
    papers = arxiv_query(
        session,
        {
            "search_query": query,
            "start": offset,
            "max_results": limit,
            "sortBy": "relevance",
            "sortOrder": "descending",
        },
    )
    if year:
        papers = [p for p in papers if year_in_range(p.get("year"), year)]
    return papers


def fetch_arxiv_meta(session, arxiv_id):
    papers = arxiv_query(session, {"id_list": arxiv_id, "max_results": 1})
    return papers[0] if papers else None


def year_in_range(year, spec):
    if not year:
        return False
    if "-" in spec:
        lo, _, hi = spec.partition("-")
        lo = int(lo) if lo.isdigit() else None
        hi = int(hi) if hi.isdigit() else None
        if lo and year < lo:
            return False
        if hi and year > hi:
            return False
        return True
    if spec.isdigit():
        return year == int(spec)
    return True


def clean(value):
    if not value:
        return ""
    return (
        value.replace("\\", r"\\")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("%", r"\%")
        .replace("&", r"\&")
        .replace("#", r"\#")
        .replace("_", r"\_")
    )


def bibtex_key(entry, index):
    surname = ""
    if entry.get("authors"):
        surname = entry["authors"][0].rsplit(" ", 1)[-1]
    base = re.sub(r"[^A-Za-z0-9]", "", surname).lower()
    year = entry.get("year")
    if base and year:
        return f"{base}{year}"
    if base:
        return base
    return f"item{index + 1}"


def build_metadata_bibtex(entry, index):
    title = entry.get("title") or "Untitled"
    authors = entry.get("authors") or []
    author_str = " and ".join(clean(a) for a in authors) if authors else "Anonymous"
    year = entry.get("year")
    venue = entry.get("venue")
    etype = "article" if venue else "misc"
    fields = [f"author = {{{author_str}}}", f"title = {{{clean(title)}}}"]
    if venue:
        fields.append(f"journal = {{{clean(venue)}}}")
    if year:
        fields.append(f"year = {{{year}}}")
    if entry.get("doi"):
        fields.append(f"doi = {{{clean(entry['doi'])}}}")
    if entry.get("url"):
        fields.append(f"url = {{{clean(entry['url'])}}}")
    body = ",\n".join(f"  {f}" for f in fields)
    return f"@{etype}{{{bibtex_key(entry, index)},\n{body}\n}}"


def build_arxiv_bibtex(meta):
    authors = meta.get("authors") or []
    author_str = " and ".join(clean(a) for a in authors) if authors else "Anonymous"
    fields = [
        f"author = {{{author_str}}}",
        f"title = {{{clean(meta.get('title') or 'Untitled')}}}",
    ]
    if meta.get("year"):
        fields.append(f"year = {{{meta['year']}}}")
    if meta.get("journal"):
        fields.append(f"journal = {{{clean(meta['journal'])}}}")
    if meta.get("doi"):
        fields.append(f"doi = {{{clean(meta['doi'])}}}")
    if meta.get("arxiv_id"):
        fields.append(f"eprint = {{{meta['arxiv_id']}}}")
        fields.append("archivePrefix = {arXiv}")
        fields.append(f"url = {{https://arxiv.org/abs/{meta['arxiv_id']}}}")
    if meta.get("primary_class"):
        fields.append(f"primaryClass = {{{meta['primary_class']}}}")
    etype = "article" if meta.get("journal") else "misc"
    body = ",\n".join(f"  {f}" for f in fields)
    return f"@{etype}{{{bibtex_key(meta, 0)},\n{body}\n}}"


def parse_bibtex_venue(bibtex):
    journal = None
    conference = None
    m = re.search(r"\bjournal\s*=\s*\{([^}]*)\}", bibtex)
    if m:
        journal = m.group(1).strip()
    m = re.search(r"\bbooktitle\s*=\s*\{([^}]*)\}", bibtex)
    if m:
        conference = m.group(1).strip()
    return journal, conference


def normalize(p):
    ext = p.get("externalIds") or {}
    authors = p.get("authors") or []
    if authors and isinstance(authors[0], dict):
        authors = [a.get("name") for a in authors if a.get("name")]
    return {
        "paper_id": p.get("paperId") or p.get("arxiv_id"),
        "title": p.get("title"),
        "authors": authors,
        "year": p.get("year"),
        "venue": p.get("venue") or "",
        "journal": p.get("journal"),
        "conference": p.get("conference"),
        "citation_count": p.get("citationCount", p.get("citation_count")),
        "url": p.get("url"),
        "abstract": p.get("abstract"),
        "doi": ext.get("DOI") or p.get("doi"),
        "arxiv_id": ext.get("ArXiv") or p.get("arxiv_id"),
    }


def normalize_title(title):
    return re.sub(r"[^a-z0-9]+", "", (title or "").lower())


def strip_version(arxiv_id):
    return re.sub(r"v\d+$", "", arxiv_id or "").lower()


def is_same_paper(ss_entry, arxiv_entry):
    """True if the arXiv result duplicates the Semantic Scholar result (arXiv ID, DOI, or title)."""
    ss_arxiv = strip_version(ss_entry.get("arxiv_id"))
    arx_arxiv = strip_version(arxiv_entry.get("arxiv_id"))
    if ss_arxiv and arx_arxiv and ss_arxiv == arx_arxiv:
        return True
    ss_doi = (ss_entry.get("doi") or "").lower().rstrip(".")
    arx_doi = (arxiv_entry.get("doi") or "").lower().rstrip(".")
    if ss_doi and arx_doi and ss_doi == arx_doi:
        return True
    ss_title = normalize_title(ss_entry.get("title"))
    arx_title = normalize_title(arxiv_entry.get("title"))
    return bool(ss_title and arx_title and ss_title == arx_title)


def collect_semantic_scholar(session, query, limit, offset, year, venue, api_key, delay):
    papers = []
    while len(papers) < limit:
        want = min(100, limit - len(papers))
        try:
            data = search(session, query, want, offset, year, venue, api_key)
            batch = [p for p in (data.get("data") or []) if p.get("title")]
            total = data.get("total") or 0
        except requests.RequestException as exc:
            sys.exit(f"Semantic Scholar search failed: {exc}")
        if not batch:
            break
        papers.extend(batch)
        offset += len(batch)
        if len(batch) < want or offset >= total:
            break
        time.sleep(delay)
    return papers[:limit]


def collect_arxiv(session, query, limit, offset, year, delay):
    papers = []
    while len(papers) < limit:
        want = min(100, limit - len(papers))
        try:
            batch = search_arxiv(session, query, want, offset, year)
            total = len(batch)
        except requests.RequestException as exc:
            sys.exit(f"arXiv search failed: {exc}")
        if not batch:
            break
        papers.extend(batch)
        offset += len(batch)
        if len(batch) < want or offset >= total:
            break
        time.sleep(delay)
    return papers[:limit]


def main():
    parser = argparse.ArgumentParser(
        description="Search Semantic Scholar or arXiv and save JSON with BibTeX citations."
    )
    parser.add_argument("query", help="Search query (plain text)")
    parser.add_argument("-o", "--out", default="papers.json", help="Output JSON file")
    parser.add_argument(
        "--max",
        type=int,
        default=100,
        help="Total number of results to collect (default 100)",
    )
    parser.add_argument(
        "--offset", type=int, default=0, help="Skip the first N results"
    )
    parser.add_argument(
        "--year", help="Publication year filter, e.g. '2017' or '2017-2020'"
    )
    parser.add_argument("--venue", help="Exact venue filter (semantic-scholar only)")
    parser.add_argument(
        "--engine",
        choices=["both", "semantic-scholar", "arxiv"],
        default="both",
        help="Search engine(s) to use (default both: Semantic Scholar + arXiv, arXiv duplicates dropped)",
    )
    parser.add_argument(
        "--min-citations", type=int, help="Keep only papers with at least N citations"
    )
    parser.add_argument(
        "--sort-citations",
        action="store_true",
        help="Sort results by citation count, descending",
    )
    parser.add_argument(
        "--no-cite",
        action="store_true",
        help="Skip BibTeX lookup (doi.org / arXiv); build BibTeX from metadata instead. Avoids extra API calls.",
    )
    parser.add_argument(
        "--bib-file", help="Custom path for the BibTeX output (default: same name as --out with .bib extension)"
    )
    parser.add_argument(
        "--delay", type=float, default=1.0, help="Seconds to sleep between API calls"
    )
    parser.add_argument(
        "--timeout", type=float, default=60, help="Request timeout in seconds"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Print per-paper progress to stderr"
    )
    args = parser.parse_args()

    session = make_session(timeout=args.timeout)
    api_key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")

    engine = args.engine
    ss_entries = []
    arxiv_entries = []
    if engine in ("both", "semantic-scholar"):
        ss_entries = [
            normalize(p)
            for p in collect_semantic_scholar(
                session,
                args.query,
                args.max,
                args.offset,
                args.year,
                args.venue,
                api_key,
                args.delay,
            )
        ]
    if engine in ("both", "arxiv"):
        arxiv_limit = (
            args.max if engine == "arxiv" else max(0, args.max - len(ss_entries))
        )
        arxiv_entries = [
            normalize(p)
            for p in collect_arxiv(
                session,
                args.query,
                arxiv_limit,
                args.offset,
                args.year,
                args.delay,
            )
        ]

    if engine == "both":
        dup = set()
        for i, arx in enumerate(arxiv_entries):
            if any(is_same_paper(ss, arx) for ss in ss_entries):
                dup.add(i)
        extras = [a for i, a in enumerate(arxiv_entries) if i not in dup]
        entries = (ss_entries + extras)[: args.max]
        engine_label = "semantic-scholar+arxiv"
    else:
        entries = ss_entries + arxiv_entries
        engine_label = engine
    if args.min_citations is not None:
        entries = [
            e
            for e in entries
            if e["citation_count"] is None
            or e["citation_count"] >= args.min_citations
        ]
    if args.sort_citations:
        entries.sort(key=lambda e: e["citation_count"] or 0, reverse=True)

    if not entries:
        sys.exit("No results found. Try a different query or relax the filters.")

    for i, entry in enumerate(entries):
        if args.verbose:
            print(
                f"[{i + 1}/{len(entries)}] {entry['title'][:70]}",
                file=sys.stderr,
            )
        if args.no_cite:
            bibtex = build_metadata_bibtex(entry, i)
            source = "generated"
        else:
            bibtex = None
            source = None
            if entry.get("doi"):
                try:
                    bibtex = fetch_bibtex_doi(session, entry["doi"])
                    source = "doi.org"
                except requests.RequestException as exc:
                    if args.verbose:
                        print(
                            f"  [warn] doi.org failed for {entry['title']}: {exc}",
                            file=sys.stderr,
                        )
            if not bibtex and entry.get("arxiv_id"):
                try:
                    meta = fetch_arxiv_meta(session, entry["arxiv_id"])
                    if meta and meta.get("title"):
                        bibtex = build_arxiv_bibtex(meta)
                        source = "arxiv"
                        if meta.get("doi") and not entry.get("doi"):
                            entry["doi"] = meta["doi"]
                        if meta.get("journal") and not entry.get("journal"):
                            entry["journal"] = meta["journal"]
                except requests.RequestException as exc:
                    if args.verbose:
                        print(
                            f"  [warn] arXiv failed for {entry['title']}: {exc}",
                            file=sys.stderr,
                        )
            if not bibtex:
                bibtex = build_metadata_bibtex(entry, i)
                source = "generated"
        entry["bibtex"] = bibtex
        entry["bibtex_source"] = source
        journal, conference = parse_bibtex_venue(bibtex)
        if journal:
            entry["journal"] = journal
        if conference:
            entry["conference"] = conference
        time.sleep(args.delay)

    payload = {
        "query": args.query,
        "searched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(entries),
        "engine": engine_label,
        "results": entries,
    }
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
    print(f"Saved {len(entries)} results to {os.path.abspath(args.out)}")

    bib_path = args.bib_file or os.path.splitext(args.out)[0] + ".bib"
    bibs = [e["bibtex"] for e in entries if e.get("bibtex")]
    with open(bib_path, "w", encoding="utf-8") as fh:
        fh.write("\n\n".join(bibs) + "\n")
    print(f"Saved {len(bibs)} BibTeX entries to {os.path.abspath(bib_path)}")


if __name__ == "__main__":
    main()
