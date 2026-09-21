#!/usr/bin/env python3
"""citecheck.py — verify a citation against a PRIMARY source before you repeat it.

The skill's trust contract says citations are guilty until verified in-session.
Every other tool here checks an answer against evidence you already fetched. This
one checks the citation ITSELF, against the registry that minted it, so a
plausible-looking arXiv id or DOI that does not resolve is caught before it
reaches a user. Stdlib-only (urllib + json), read-only, no state unless --db.

Why this exists: in the audit that produced v3.0.0 this tool caught a real
defect in this skill's own references/verified-grounding.md — arXiv:2303.13537
was cited as "GPTCache" but resolves to a completely different paper, and a
sign error in a correlation coefficient (r <= -0.83 where the source says
r >= 0.83). Both had survived two published versions.

VERDICTS
  CONFIRMED   id resolves and every checked attribute agrees
  MISMATCH    id resolves but a claimed attribute disagrees (title/author/year)
  NOT_FOUND   id does not resolve — the citation is wrong or invented
  UNREACHABLE the registry could not be queried (network blocked); NOT a verdict
              about the citation. Never report UNREACHABLE as verified.

USAGE
  citecheck.py scan --file references/verified-grounding.md [--strict]
  citecheck.py resolve --arxiv 2309.06180 --arxiv 2303.13537
  citecheck.py doi --doi 10.1038/s41586-025-09833-y
  citecheck.py title --query "Chain of Verification" [--year 2024] [--author dhuliawala]
  citecheck.py check --citations-file claims.json

claims.json shape (every field except "id" optional):
  [{"id": "2309.06180", "title_has": "pagedattention",
    "first_author": "kwon", "year": 2023}]

EXIT CODES: 0 ran (read the verdicts) · 2 bad input, or --strict and a
NOT_FOUND/MISMATCH was found · never a traceback.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
from _common import clean_errors, fail  # noqa: E402

ARXIV_API = "https://export.arxiv.org/api/query"
OPENALEX_API = "https://api.openalex.org/works"
NS = {"a": "http://www.w3.org/2005/Atom", "ar": "http://arxiv.org/schemas/atom"}
# Extraction pattern. Deliberately NOT \b-anchored at the end: the arXiv Atom
# feed returns ids WITH a version suffix (".../abs/2211.17192v2"), and \b between
# the last digit and "v" does not exist (both are word characters), so a
# \b-anchored pattern silently matched nothing and reported every real paper as
# NOT_FOUND. Caught by running the tool, not by reading it.
ARXIV_ID = re.compile(r"(?<!\d)(\d{4}\.\d{4,5})(?!\d)")
ARXIV_ID_BARE = re.compile(r"\d{4}\.\d{4,5}")
UA = {"User-Agent": "inference-expert-agents/citecheck 3.0"}
TIMEOUT = 45


class Unreachable(Exception):
    """Network/registry failure — distinct from 'the citation is wrong'."""


def _get(url: str, timeout: int = TIMEOUT) -> bytes:
    try:
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        raise Unreachable(f"HTTP {e.code} from {url.split('?')[0]}") from e
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise Unreachable(f"{type(e).__name__} reaching {url.split('?')[0]}") from e


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "")).strip()


def fetch_arxiv(ids: list[str]) -> dict[str, dict]:
    """One batched request for all ids (arXiv accepts a comma list)."""
    q = urllib.parse.urlencode({"id_list": ",".join(ids), "max_results": 100})
    root = ET.fromstring(_get(f"{ARXIV_API}?{q}"))
    out: dict[str, dict] = {}
    for e in root.findall("a:entry", NS):
        m = ARXIV_ID.search(e.findtext("a:id", "", NS) or "")
        if not m:
            continue
        title = _norm(e.findtext("a:title", "", NS))
        # arXiv returns an empty-ish entry for an id it does not know
        if not title or title.lower().startswith("error"):
            continue
        out[m.group(1)] = {
            "title": title,
            "authors": [_norm(a.findtext("a:name", "", NS))
                        for a in e.findall("a:author", NS)],
            "published": (e.findtext("a:published", "", NS) or "")[:10],
            "comment": _norm(e.findtext("ar:comment", "", NS)),
            "journal_ref": _norm(e.findtext("ar:journal_ref", "", NS)),
        }
    return out


def judge_arxiv(claim: dict, rec: dict | None) -> dict:
    if rec is None:
        return {"verdict": "NOT_FOUND",
                "why": "arXiv has no entry for this id — the citation is wrong or invented"}
    problems = []
    th = (claim.get("title_has") or "").strip().lower()
    if th and th not in rec["title"].lower():
        problems.append(f"real title does not contain {th!r}: {rec['title']!r}")
    fa = (claim.get("first_author") or "").strip().lower()
    if fa:
        real = (rec["authors"][0].lower() if rec["authors"] else "")
        if fa not in real:
            problems.append(f"first author is {rec['authors'][:1] or '(none)'}, not {fa!r}")
    yr = claim.get("year")
    if yr:
        real_year = int(rec["published"][:4]) if rec["published"] else 0
        if real_year and abs(real_year - int(yr)) > 1:
            problems.append(f"submitted {real_year}, claim says {yr}")
    if problems:
        return {"verdict": "MISMATCH", "problems": problems}
    return {"verdict": "CONFIRMED"}


def check_doi(doi: str) -> dict:
    q = urllib.parse.urlencode({"filter": f"doi:{doi}", "per-page": 1})
    data = json.loads(_get(f"{OPENALEX_API}?{q}"))
    hits = data.get("results") or []
    if not hits:
        return {"verdict": "NOT_FOUND", "why": f"no OpenAlex record for doi:{doi}"}
    w = hits[0]
    return {"verdict": "CONFIRMED",
            "title": _norm(w.get("title") or w.get("display_name")),
            "year": w.get("publication_year"),
            "venue": _norm(((w.get("primary_location") or {}).get("source") or {})
                           .get("display_name")),
            "authors": [_norm(a["author"]["display_name"])
                        for a in (w.get("authorships") or [])[:5]]}


def check_title(query: str, year: int | None, author: str | None) -> dict:
    q = urllib.parse.urlencode({"filter": f"title.search:{query}", "per-page": 3})
    data = json.loads(_get(f"{OPENALEX_API}?{q}"))
    hits = data.get("results") or []
    if not hits:
        return {"verdict": "NOT_FOUND", "why": f"no OpenAlex title match for {query!r}"}
    w = hits[0]
    row = {"title": _norm(w.get("title") or w.get("display_name")),
           "year": w.get("publication_year"),
           "venue": _norm(((w.get("primary_location") or {}).get("source") or {})
                          .get("display_name")),
           "cited_by": w.get("cited_by_count"),
           "n_candidates": len(hits)}
    problems = []
    if year and row["year"] and row["year"] != int(year):
        problems.append(f"OpenAlex year {row['year']} vs claimed {year}")
    if author:
        names = " ".join(_norm(a["author"]["display_name"]).lower()
                         for a in (w.get("authorships") or []))
        if author.lower() not in names:
            problems.append(f"author {author!r} not on the best match")
    row["verdict"] = "MISMATCH" if problems else "CONFIRMED"
    if problems:
        row["problems"] = problems
    return row


@clean_errors
def main() -> int:
    ap = argparse.ArgumentParser(
        description="Verify citations against arXiv / OpenAlex before repeating them.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_scan = sub.add_parser("scan", help="find every arXiv id in a file and verify it")
    p_scan.add_argument("--file", required=True)
    p_scan.add_argument("--strict", action="store_true",
                        help="exit 2 if any citation is NOT_FOUND or MISMATCH")

    p_res = sub.add_parser("resolve", help="resolve explicit arXiv ids")
    p_res.add_argument("--arxiv", action="append", required=True)

    p_doi = sub.add_parser("doi", help="resolve a DOI via OpenAlex")
    p_doi.add_argument("--doi", required=True)

    p_t = sub.add_parser("title", help="fuzzy title lookup via OpenAlex")
    p_t.add_argument("--query", required=True)
    p_t.add_argument("--year", type=int)
    p_t.add_argument("--author")

    p_c = sub.add_parser("check", help="verify structured claims from a JSON file")
    p_c.add_argument("--citations-file", required=True)
    p_c.add_argument("--strict", action="store_true")

    a = ap.parse_args()

    if a.cmd == "doi":
        try:
            row = check_doi(a.doi)
        except Unreachable as e:
            row = {"verdict": "UNREACHABLE", "why": str(e)}
        print(json.dumps({"doi": a.doi, **row}, indent=2))
        return 0

    if a.cmd == "title":
        try:
            row = check_title(a.query, a.year, a.author)
        except Unreachable as e:
            row = {"verdict": "UNREACHABLE", "why": str(e)}
        print(json.dumps({"query": a.query, **row}, indent=2))
        return 0

    # the three arXiv-backed commands
    claims: list[dict] = []
    if a.cmd == "scan":
        if not os.path.exists(a.file):
            return fail(f"no such file: {a.file}")
        body = open(a.file, encoding="utf-8", errors="replace").read()
        ids = sorted(set(ARXIV_ID.findall(body)))
        if not ids:
            return fail("no arXiv ids found in that file",
                        hint="looking for the pattern NNNN.NNNNN, e.g. 2309.06180")
        claims = [{"id": i} for i in ids]
    elif a.cmd == "resolve":
        claims = [{"id": i.strip()} for i in a.arxiv if i.strip()]
        if not claims:
            return fail("no arXiv ids given")
    else:  # check
        raw = json.load(open(a.citations_file, encoding="utf-8"))
        if isinstance(raw, dict):
            raw = raw.get("citations") or raw.get("claims")
        if not isinstance(raw, list) or not raw:
            return fail("--citations-file must be a non-empty JSON array",
                        hint='[{"id": "2309.06180", "title_has": "pagedattention", '
                             '"first_author": "kwon", "year": 2023}]')
        claims = raw

    for c in claims:
        if not isinstance(c, dict) or not c.get("id"):
            return fail("every claim needs an 'id'",
                        hint='{"id": "2309.06180", ...}')
        if not ARXIV_ID_BARE.fullmatch(str(c["id"]).strip()):
            return fail(f"{c['id']!r} is not an arXiv id (NNNN.NNNNN)",
                        hint="use the `doi` or `title` subcommand for non-arXiv sources")

    ids = sorted({str(c["id"]).strip() for c in claims})
    try:
        found = fetch_arxiv(ids)
        unreachable = None
    except Unreachable as e:
        found, unreachable = {}, str(e)

    rows = []
    for c in claims:
        cid = str(c["id"]).strip()
        if unreachable:
            rows.append({"id": cid, "verdict": "UNREACHABLE", "why": unreachable})
            continue
        v = judge_arxiv(c, found.get(cid))
        rec = found.get(cid)
        row = {"id": cid, **v}
        if rec:
            row["real_title"] = rec["title"]
            row["real_authors"] = rec["authors"][:3]
            row["real_published"] = rec["published"]
            if rec["comment"]:
                row["real_comment"] = rec["comment"]
        rows.append(row)

    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    strict = getattr(a, "strict", False)
    bad = counts.get("NOT_FOUND", 0) + counts.get("MISMATCH", 0)
    out = {"n_citations": len(rows), "verdicts": counts, "results": rows,
           "strict": strict,
           "note": ("UNREACHABLE means the registry could not be queried; it is not "
                    "evidence that the citation is fine — retry before trusting it."
                    if counts.get("UNREACHABLE") else
                    "verdicts come from export.arxiv.org, fetched in this session")}
    print(json.dumps(out, indent=2))
    if strict and bad:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
