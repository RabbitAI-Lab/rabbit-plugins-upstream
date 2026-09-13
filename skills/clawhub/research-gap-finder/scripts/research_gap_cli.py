#!/usr/bin/env python3
"""Stdlib-only, evidence-bounded research-gap project CLI.

The commands intentionally produce *candidate* gaps. A cue sentence is not proof
that a gap exists, and an identifier is not the same as a web-verified citation.
Use ``validate --check-web`` and a human/methodological review before relying on a
candidate in a proposal.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import html
import io
import json
import os
import re
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

VERSION = "2.1.1"
APP = "research-gap-finder"
SCHEMA_VERSION = "2.1"
MAX_RESPONSE_BYTES = 8 * 1024 * 1024
MAX_JSON_BYTES = 32 * 1024 * 1024
MAX_TEXT_FIELD = 100_000
MAX_PAPERS = 50_000
MAX_GAPS = 50_000

# ── six-type knowledge-gap taxonomy ──────────────────────────────────────────
TAXONOMY = {
    "evidence": ["insufficient evidence", "no evidence", "lack of evidence", "few studies",
                 "limited data", "not well studied", "evidence gap", "data scarcity",
                 "paucity of", "scarcity of", "no studies", "weak evidence",
                 "little is known", "poorly understood", "limited research",
                 "understudied", "not studied", "missing data"],
    "methodological": ["methodological", "small sample", "small sample size", "no control",
                       "control group", "cross-sectional", "self-report", "instrument",
                       "confound", "longitudinal", "reproducibility", "bias", "outdated",
                       "measurement", "sample size", "retrospective", "observational"],
    "population": ["population", "subgroup", "children", "adolescent", "elderly", "pregnant",
                   "minority", "ethnic", "rural", "geographic", "low-income", "patients with",
                   "cohort", "demographic", "sex", "gender", "age group", "underrepresented",
                   "vulnerable"],
    "contextual": ["real-world", "setting", "low-resource", "resource-limited", "community",
                   "primary care", "hospital", "school", "workplace", "context",
                   "implementation setting", "cross-cultural", "cultural", "everyday"],
    "theoretical": ["theoretical", "framework", "mechanism", "theory", "model",
                    "conceptual", "underlying", "pathway", "explanatory", "contradict",
                    "mechanistic", "no consensus", "not well understood"],
    "translational": ["translation", "implementation", "practice", "policy", "clinical uptake",
                      "dissemination", "adoption", "scaling", "guideline", "health system",
                      "barrier", "into practice", "evidence to practice", "uptake"],
}

DIMENSIONS = ["theoretical", "practical", "feasibility", "novelty", "coherence"]
DIM_QUESTIONS = {
    "theoretical": "Advance core concepts / resolve contradictions",
    "practical": "Solve a real problem / inform policy-practice",
    "feasibility": "Data, methods, resources realistically obtainable",
    "novelty": "Genuinely unstudied (vs preprints, trials, grants)",
    "coherence": "Logical next step of the field's trajectory",
}
GAP_CUES = (
    "limitations", "future work", "future research", "further research", "further study",
    "however, these", "more studies", "needed", "remains unclear", "not fully understood",
    "inconclusive", "small sample", "warrants further", "opening question", "remains to be",
    "limited by", "unaddressed", "research gap", "open question", "less is known",
)

DEFAULT_LIMIT = 100
KNOWN_ENGINES = ["openalex", "semantic", "crossref", "europepmc", "pubmed", "arxiv"]
# The default is intentionally bounded; users may opt into all six with --engines.
DEFAULT_ENGINES = ["openalex", "crossref", "europepmc", "arxiv"]
USE_CACHE = True
TIMEOUT = 25
CACHE_WARNINGS = []
REQUEST_URLS = {}


# ── safe, bounded utilities ─────────────────────────────────────────────────
def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")


def now_epoch() -> int:
    return int(time.time())


def clean_text(value, limit=MAX_TEXT_FIELD) -> str:
    """Make external/user text safe for CSV/Markdown/JSON fields and bound it."""
    if value is None:
        return ""
    if isinstance(value, (dict, list, tuple)):
        value = " ".join(str(x) for x in value)
    text = str(value).replace("\x00", " ")
    text = "".join(ch if ch in "\n\r\t" or ord(ch) >= 32 else " " for ch in text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def _atomic_write_text(path: Path, text: str) -> None:
    """Replace a file atomically; replacing a symlink does not follow its target."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix="." + path.name + ".", dir=str(path.parent))
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(str(tmp), str(path))
    finally:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


def write_json(path: Path, data) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False) + "\n"
    _atomic_write_text(path, text)


def _json_from_path(path: Path, max_bytes=MAX_JSON_BYTES):
    size = path.stat().st_size
    if size > max_bytes:
        raise ValueError("JSON file exceeds the configured size limit")
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_json(path: Path, default=None, max_bytes=MAX_JSON_BYTES):
    """Best-effort read for caches and optional files; never executes content."""
    if not path.exists():
        return default
    try:
        return _json_from_path(path, max_bytes)
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError):
        return default


def load_json_strict(path: Path, default=None, max_bytes=MAX_JSON_BYTES):
    if not path.exists():
        return default
    try:
        return _json_from_path(path, max_bytes)
    except json.JSONDecodeError as exc:
        raise ValueError("invalid JSON in " + str(path)) from exc
    except (OSError, UnicodeError, ValueError, TypeError) as exc:
        raise ValueError("cannot read JSON " + str(path) + ": " + str(exc)) from exc


def _safe_project_path(project: Path, value, label="path") -> Path:
    """Resolve a user path and reject traversal/symlink escape from project."""
    root = project.expanduser().resolve()
    candidate = Path(value).expanduser()
    if not candidate.is_absolute():
        candidate = root / candidate
    resolved = candidate.resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"{label} must remain inside the project directory") from exc
    return resolved


def _safe_years(value):
    if value is None:
        return [None, None]
    if not isinstance(value, (list, tuple)) or len(value) != 2:
        raise ValueError("years must contain [start, end]")
    result = []
    for item in value:
        if item in (None, "", 0):
            result.append(None)
        else:
            year = int(item)
            if year < 1 or year > 3000:
                raise ValueError("year must be between 1 and 3000")
            result.append(year)
    if result[0] and result[1] and result[0] > result[1]:
        raise ValueError("year start cannot be after year end")
    return result


def _safe_limit(value) -> int:
    try:
        value = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("limit must be an integer") from exc
    if not 1 <= value <= 1000:
        raise ValueError("limit must be between 1 and 1000")
    return value


def _safe_timeout(value) -> int:
    try:
        value = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("timeout must be an integer") from exc
    if not 1 <= value <= 120:
        raise ValueError("timeout must be between 1 and 120 seconds")
    return value


def norm_title(t: str) -> str:
    text = unicodedata.normalize("NFKC", clean_text(t))
    text = re.sub(r"[^\w\s]+", " ", text, flags=re.UNICODE)
    return re.sub(r"\s+", " ", text).strip().casefold()


def title_key(title: str) -> str:
    stop = {"a", "an", "the", "of", "and", "in", "on", "for", "to", "with", "from",
            "is", "are", "using", "new", "novel"}
    toks = [w for w in norm_title(title).split() if w and w not in stop]
    return " ".join(toks)[:240]


def normalize_doi(value) -> str:
    doi = clean_text(value, 500).strip()
    doi = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I).strip()
    doi = doi.rstrip(".,;:)]}")
    return doi.casefold()


def valid_doi(value) -> bool:
    doi = normalize_doi(value)
    return bool(re.fullmatch(r"10\.\d{4,9}/[^\s\"<>]+", doi))


def paper_identifier(paper: dict) -> str:
    doi = normalize_doi(paper.get("doi", ""))
    if valid_doi(doi):
        return doi
    sid = clean_text(paper.get("source_id", ""), 300).strip()
    source = clean_text(paper.get("source", ""), 40).casefold()
    if not sid:
        return ""
    if source == "pubmed" and sid.isdigit():
        return "PMID:" + sid
    if source == "europepmc":
        return ("PMID:" + sid) if sid.isdigit() else "EPMC:" + sid
    if source == "arxiv":
        return "arXiv:" + sid
    if source == "semantic":
        return "S2:" + sid
    if source == "openalex":
        return "OpenAlex:" + sid
    if source == "crossref" and valid_doi(sid):
        return normalize_doi(sid)
    return source.upper() + ":" + sid if source else sid


def valid_identifier(value) -> bool:
    ident = clean_text(value, 500).strip()
    if valid_doi(ident):
        return True
    return bool(re.fullmatch(r"(?:PMID|EPMC|S2|OpenAlex|ARXIV|CROSSREF):[A-Za-z0-9._:/-]{1,300}", ident, re.I))


def _paper_key(paper: dict) -> str:
    doi = normalize_doi(paper.get("doi", ""))
    if valid_doi(doi):
        return "doi:" + doi
    source = clean_text(paper.get("source", ""), 40).casefold()
    sid = clean_text(paper.get("source_id", ""), 300).casefold()
    if source and sid:
        return "id:" + source + ":" + sid
    title = title_key(paper.get("title", ""))
    year = clean_text(paper.get("year", ""), 10)
    return "title:" + title + "|" + year if title else ""


# ── bounded HTTP and cache ────────────────────────────────────────────────────
def _read_bounded(response, max_bytes=MAX_RESPONSE_BYTES) -> bytes:
    header = response.headers.get("Content-Length")
    if header:
        try:
            if int(header) > max_bytes:
                raise ValueError("API response exceeds the configured size limit")
        except ValueError:
            if header.isdigit():
                raise
    chunks = []
    total = 0
    while True:
        chunk = response.read(min(64 * 1024, max_bytes - total + 1))
        if not chunk:
            break
        total += len(chunk)
        if total > max_bytes:
            raise ValueError("API response exceeds the configured size limit")
        chunks.append(chunk)
    return b"".join(chunks)


def _default_headers(accept="application/json"):
    return {"User-Agent": f"{APP}/{VERSION} (stdlib)", "Accept": accept}


def _http_json(url: str, timeout: int = 25, headers=None) -> dict:
    if urllib.parse.urlparse(url).scheme != "https":
        raise ValueError("only HTTPS scholarly endpoints are allowed")
    req_headers = _default_headers()
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        data = json.loads(_read_bounded(response).decode("utf-8"))
    if not isinstance(data, dict):
        raise ValueError("API JSON response must be an object")
    return data


def _http_text(url: str, timeout: int = 25, headers=None) -> str:
    if urllib.parse.urlparse(url).scheme != "https":
        raise ValueError("only HTTPS scholarly endpoints are allowed")
    req_headers = _default_headers("application/atom+xml,text/xml,text/plain")
    if headers:
        req_headers.update(headers)
    req = urllib.request.Request(url, headers=req_headers)
    with urllib.request.urlopen(req, timeout=timeout) as response:
        return _read_bounded(response).decode("utf-8", "replace")


def _retry_delay(exc, attempt: int) -> float:
    if isinstance(exc, urllib.error.HTTPError):
        raw = exc.headers.get("Retry-After", "") if exc.headers else ""
        try:
            return min(30.0, max(0.0, float(raw)))
        except (TypeError, ValueError):
            pass
    return min(8.0, 1.5 * (2 ** attempt))


def _cache_path(project: Path, url: str) -> Path:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()[:24]
    return _safe_project_path(project, Path(".cache") / (digest + ".json"), "cache path")


def api_get_json(url: str, project: Path, use_cache=None, timeout=None, retries: int = 2) -> dict:
    """Fetch JSON with bounded response size, atomic per-project cache and backoff."""
    if use_cache is None:
        use_cache = USE_CACHE
    if timeout is None:
        timeout = TIMEOUT
    cp = _cache_path(project, url)
    if use_cache and cp.exists():
        cached = load_json(cp, None, MAX_RESPONSE_BYTES)
        if isinstance(cached, dict):
            return cached
        CACHE_WARNINGS.append("ignored corrupt or non-object cache " + cp.name)
    last = None
    for attempt in range(max(0, int(retries)) + 1):
        try:
            data = _http_json(url, timeout)
            if use_cache:
                encoded = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
                if len(encoded.encode("utf-8")) <= MAX_RESPONSE_BYTES:
                    _atomic_write_text(cp, encoded + "\n")
                else:
                    CACHE_WARNINGS.append("response too large to cache for " + cp.name)
            return data
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in (408, 425, 429, 500, 502, 503, 504) or attempt >= retries:
                raise
        except Exception as exc:  # network, decoding, or bounded-response errors
            last = exc
            if attempt >= retries:
                raise
        time.sleep(_retry_delay(last, attempt))
    raise last if last else RuntimeError("retries exhausted")


def api_get_text(url: str, timeout=None, retries: int = 2) -> str:
    if timeout is None:
        timeout = TIMEOUT
    last = None
    for attempt in range(max(0, int(retries)) + 1):
        try:
            return _http_text(url, timeout)
        except urllib.error.HTTPError as exc:
            last = exc
            if exc.code not in (408, 425, 429, 500, 502, 503, 504) or attempt >= retries:
                raise
        except Exception as exc:
            last = exc
            if attempt >= retries:
                raise
        time.sleep(_retry_delay(last, attempt))
    raise last if last else RuntimeError("retries exhausted")


class RateLimiter:
    """Per-engine minimum interval. Backoff is handled by the HTTP helpers."""

    def __init__(self, min_interval: float = 0.4):
        self.min_interval = max(0.0, float(min_interval))
        self._last = {}

    def wait(self, engine: str) -> None:
        now = time.time()
        last = self._last.get(engine, 0.0)
        delta = self.min_interval - (now - last)
        if delta > 0:
            time.sleep(delta)
        self._last[engine] = time.time()


def get_inverted_abstract(inv) -> str:
    if not isinstance(inv, dict):
        return ""
    pos = {}
    for word, idxs in inv.items():
        if not isinstance(idxs, list):
            continue
        for index in idxs[:MAX_TEXT_FIELD]:
            if isinstance(index, int) and 0 <= index <= MAX_TEXT_FIELD:
                pos[index] = clean_text(word, 500)
    return " ".join(pos[i] for i in sorted(pos))[:MAX_TEXT_FIELD]


# ── project structure and persistence ─────────────────────────────────────────
def project_schema() -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "topic": "",
        "pico": {},
        "engines": list(DEFAULT_ENGINES),
        "limit": DEFAULT_LIMIT,
        "years": [None, None],
        "queries": [],
        "use_cache": True,
        "timeout": 25,
        "created": utc(),
    }


def project_paths(project: Path) -> dict:
    return {name: _safe_project_path(project, filename, name) for name, filename in {
        "config": "config.json", "evidence_json": "evidence.json",
        "evidence_csv": "evidence_matrix.csv", "gaps_json": "gaps.json",
        "gaps_csv": "gaps.csv", "report": "report.md", "scores": "scores.json",
        "cache": ".cache",
    }.items()}


def _parse_pico(raw) -> dict:
    if isinstance(raw, dict):
        return {clean_text(k, 80): clean_text(v, 5000) for k, v in raw.items()}
    if isinstance(raw, str) and raw.strip():
        try:
            value = json.loads(raw)
            return _parse_pico(value) if isinstance(value, dict) else {}
        except (ValueError, TypeError):
            return {}
    return {}


def _normalize_config(cfg: dict) -> dict:
    if not isinstance(cfg, dict):
        raise ValueError("config.json must contain an object")
    engines = cfg.get("engines", DEFAULT_ENGINES)
    if isinstance(engines, str):
        engines = [x.strip() for x in engines.split(",") if x.strip()]
    if not isinstance(engines, list):
        raise ValueError("config engines must be a list or comma-separated string")
    engines = [clean_text(x, 40).casefold() for x in engines if clean_text(x, 40)]
    limit = _safe_limit(cfg.get("limit", DEFAULT_LIMIT))
    timeout = _safe_timeout(cfg.get("timeout", 25))
    years = _safe_years(cfg.get("years", [None, None]))
    pico = _parse_pico(cfg.get("pico", {}))
    queries = cfg.get("queries", [])
    if not isinstance(queries, list):
        raise ValueError("config queries must be a list")
    return {
        "schema_version": str(cfg.get("schema_version", SCHEMA_VERSION)),
        "topic": clean_text(cfg.get("topic", ""), 5000),
        "pico": pico,
        "engines": engines or list(DEFAULT_ENGINES),
        "limit": limit,
        "years": years,
        "queries": queries[-1000:],
        "use_cache": bool(cfg.get("use_cache", True)),
        "timeout": timeout,
        "created": clean_text(cfg.get("created", utc()), 80),
    }


def ensure_project(args) -> dict:
    raw_dir = getattr(args, "dir", None)
    if not raw_dir:
        raise ValueError("project directory is required")
    project = Path(raw_dir).expanduser().resolve()
    if project.exists() and not project.is_dir():
        raise ValueError("project path is not a directory")
    project.mkdir(parents=True, exist_ok=True)
    paths = project_paths(project)
    if paths["config"].exists():
        cfg = _normalize_config(load_json_strict(paths["config"]))
    else:
        cfg = project_schema()
        cfg["topic"] = clean_text(getattr(args, "topic", "") or "", 5000)
        cfg["pico"] = _parse_pico(getattr(args, "pico", {}))
        write_json(paths["config"], cfg)
    if not paths["evidence_json"].exists():
        write_json(paths["evidence_json"], {"schema_version": SCHEMA_VERSION, "papers": [], "fetched_at": None})
    if not paths["gaps_json"].exists():
        write_json(paths["gaps_json"], {"schema_version": SCHEMA_VERSION, "gaps": [], "computed_at": None})
    return {"project": project, "paths": paths, "config": cfg}


def load_papers(project: Path) -> list:
    path = project_paths(project)["evidence_json"]
    data = load_json_strict(path, {"papers": []})
    if not isinstance(data, dict) or not isinstance(data.get("papers", []), list):
        raise ValueError("evidence.json must contain a papers list")
    if not all(isinstance(p, dict) for p in data["papers"]):
        raise ValueError("evidence.json contains a non-object paper record")
    papers = data["papers"]
    if len(papers) > MAX_PAPERS:
        raise ValueError("evidence.json contains too many records")
    return papers


DANGEROUS_CSV_PREFIXES = ("=", "+", "-", "@")


def safe_csv_cell(value) -> str:
    """Neutralize spreadsheet formula prefixes in untrusted export data."""
    text = clean_text(value)
    if text.lstrip(" \t\r\n").startswith(DANGEROUS_CSV_PREFIXES):
        return "'" + text
    return text


def _write_csv(path: Path, columns, rows) -> None:
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=columns, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    for row in rows:
        writer.writerow({key: safe_csv_cell(value) for key, value in row.items()})
    _atomic_write_text(path, out.getvalue())


def save_papers(project: Path, papers: list) -> None:
    paths = project_paths(project)
    write_json(paths["evidence_json"], {
        "schema_version": SCHEMA_VERSION, "papers": papers, "fetched_at": utc()
    })
    write_evidence_csv(project, papers)


def write_evidence_csv(project: Path, papers: list) -> None:
    cols = ["id", "title", "authors", "year", "source", "source_id", "doi", "url",
            "abstract", "cited_by", "journal", "design", "population", "setting",
            "findings", "limitations", "gap_statement", "provenance"]
    rows = []
    for paper in papers:
        row = {column: paper.get(column, "") for column in cols}
        row["authors"] = "; ".join(clean_text(x, 500) for x in (paper.get("authors") or []) if x)
        row["provenance"] = json.dumps(paper.get("provenance", []), ensure_ascii=False, sort_keys=True)
        rows.append(row)
    _write_csv(project_paths(project)["evidence_csv"], cols, rows)


def load_gaps(project: Path) -> list:
    path = project_paths(project)["gaps_json"]
    data = load_json_strict(path, {"gaps": []})
    if not isinstance(data, dict) or not isinstance(data.get("gaps", []), list):
        raise ValueError("gaps.json must contain a gaps list")
    if not all(isinstance(g, dict) for g in data["gaps"]):
        raise ValueError("gaps.json contains a non-object gap record")
    gaps = data["gaps"]
    if len(gaps) > MAX_GAPS:
        raise ValueError("gaps.json contains too many records")
    return gaps


def save_gaps(project: Path, gaps: list) -> None:
    paths = project_paths(project)
    write_json(paths["gaps_json"], {
        "schema_version": SCHEMA_VERSION, "gaps": gaps, "computed_at": utc()
    })
    cols = ["id", "statement", "type", "secondary_type", "importance",
            "confidence", "sources", "research_question", "novelty_status",
            "verification", "exploratory"]
    rows = []
    for gap in gaps:
        row = {column: gap.get(column, "") for column in cols}
        importance = gap.get("importance") if isinstance(gap.get("importance"), dict) else {}
        row["importance"] = "; ".join(f"{k}={importance[k]}" for k in sorted(importance))
        row["secondary_type"] = "; ".join(str(x) for x in (gap.get("secondary_type") or []))
        row["sources"] = "; ".join(clean_text(x, 500) for x in (gap.get("sources") or []) if x)
        rows.append(row)
    _write_csv(paths["gaps_csv"], cols, rows)


def emit_paper(engine: str, source_id: str, title: str, authors, year, doi, url,
               abstract="", cited_by=0, journal="") -> dict:
    if isinstance(authors, str):
        authors = [authors]
    author_list = [clean_text(x, 500) for x in (authors or []) if clean_text(x, 500)]
    try:
        count = max(0, min(int(cited_by or 0), 2_000_000_000))
    except (TypeError, ValueError):
        count = 0
    normalized_doi = normalize_doi(doi)
    title = clean_text(title, 10_000)
    source_id = clean_text(source_id, 500)
    return {
        "id": title_key(title) or source_id,
        "title": title,
        "authors": author_list,
        "year": clean_text(year, 10),
        "source": clean_text(engine, 40).casefold(),
        "source_id": source_id,
        "doi": normalized_doi if valid_doi(normalized_doi) else "",
        "url": clean_text(url, 2000),
        "abstract": clean_text(abstract),
        "cited_by": count,
        "journal": clean_text(journal, 2000),
        "design": "", "population": "", "setting": "", "findings": "",
        "limitations": "", "gap_statement": "", "provenance": [],
    }


def _attach_provenance(papers, engine, query, fetched_at):
    for paper in papers:
        if not isinstance(paper, dict):
            continue
        item = {
            "engine": clean_text(engine, 40).casefold(),
            "query": clean_text(query, 5000),
            "retrieved_at": fetched_at,
            "identifier": paper_identifier(paper),
            "record_url": clean_text(paper.get("url", ""), 2000),
            "request_urls": list(REQUEST_URLS.get(engine, [])),
        }
        old = paper.get("provenance") if isinstance(paper.get("provenance"), list) else []
        # Same query/engine/identifier is not duplicated on a rerun.
        if not any(isinstance(x, dict) and
                   x.get("engine") == item["engine"] and
                   x.get("query") == item["query"] and
                   x.get("identifier") == item["identifier"] for x in old):
            old.append(item)
        paper["provenance"] = old[-100:]


# ── scholarly engines ─────────────────────────────────────────────────────────
def _record_request(engine, url):
    """Keep exact, key-free request URLs for reproducible provenance."""
    urls = REQUEST_URLS.setdefault(engine, [])
    if url not in urls:
        urls.append(url)


def _bounded_limit(limit, maximum):
    return max(1, min(_safe_limit(limit), maximum))


def _year_in_range(year, years):
    try:
        value = int(str(year)[:4])
    except (TypeError, ValueError):
        return True
    return (not years[0] or value >= years[0]) and (not years[1] or value <= years[1])


def engine_openalex(project, query, limit, years, rl: RateLimiter) -> list:
    rl.wait("openalex")
    fields = "id,title,authorships,publication_year,doi,primary_location,abstract_inverted_index,cited_by_count"
    params = {"search": clean_text(query, 5000), "per_page": _bounded_limit(limit, 100),
              "sort": "relevance_score:desc", "select": fields}
    filters = []
    if years[0]:
        filters.append(f"from_publication_date:{years[0]}-01-01")
    if years[1]:
        filters.append(f"to_publication_date:{years[1]}-12-31")
    if filters:
        params["filter"] = ",".join(filters)
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    _record_request("openalex", url)
    data = api_get_json(url, project)
    results = data.get("results", [])
    if not isinstance(results, list):
        raise ValueError("OpenAlex results is not a list")
    out = []
    for work in results[:200]:
        if not isinstance(work, dict):
            continue
        authors = []
        for author in work.get("authorships", []) or []:
            if isinstance(author, dict) and isinstance(author.get("author"), dict):
                authors.append(author["author"].get("display_name", ""))
        location = work.get("primary_location") if isinstance(work.get("primary_location"), dict) else {}
        source = location.get("source") if isinstance(location.get("source"), dict) else {}
        out.append(emit_paper(
            "openalex", str(work.get("id", "")).rstrip("/").split("/")[-1],
            work.get("title", work.get("display_name", "")), authors, work.get("publication_year"), work.get("doi", ""),
            work.get("id", ""), get_inverted_abstract(work.get("abstract_inverted_index")),
            work.get("cited_by_count", 0), source.get("display_name", "")))
    return [paper for paper in out if paper.get("title") or paper.get("source_id")]


def engine_semantic(project, query, limit, years, rl: RateLimiter) -> list:
    rl.wait("semantic")
    fields = "paperId,title,authors,year,externalIds,url,abstract,citationCount,venue"
    params = {"query": clean_text(query, 5000), "limit": _bounded_limit(limit, 100), "fields": fields}
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + urllib.parse.urlencode(params)
    _record_request("semantic", url)
    data = api_get_json(url, project)
    results = data.get("data", [])
    if not isinstance(results, list):
        raise ValueError("Semantic Scholar data is not a list")
    out = []
    for record in results[:100]:
        if not isinstance(record, dict) or not _year_in_range(record.get("year"), years):
            continue
        external = record.get("externalIds") if isinstance(record.get("externalIds"), dict) else {}
        doi = external.get("DOI", "")
        authors = [a.get("name", "") for a in (record.get("authors") or [])
                   if isinstance(a, dict)]
        out.append(emit_paper(
            "semantic", record.get("paperId") or external.get("CorpusId", ""),
            record.get("title", ""), authors, record.get("year"), doi,
            record.get("url", ""), record.get("abstract", ""),
            record.get("citationCount", 0), record.get("venue", "")))
    return [paper for paper in out if paper.get("title") or paper.get("source_id")]


def _strip_html(text) -> str:
    return clean_text(re.sub(r"<[^>]*>", " ", str(text or "")))


def engine_crossref(project, query, limit, years, rl: RateLimiter) -> list:
    rl.wait("crossref")
    params = {"query": clean_text(query, 5000), "rows": _bounded_limit(limit, 1000),
              "select": "DOI,title,author,issued,abstract,container-title,URL"}
    filters = []
    if years[0]:
        filters.append(f"from-pub-date:{years[0]}-01-01")
    if years[1]:
        filters.append(f"until-pub-date:{years[1]}-12-31")
    if filters:
        params["filter"] = ",".join(filters)
    url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
    _record_request("crossref", url)
    data = api_get_json(url, project)
    message = data.get("message") if isinstance(data.get("message"), dict) else {}
    items = message.get("items", [])
    if not isinstance(items, list):
        raise ValueError("Crossref items is not a list")
    out = []
    for item in items[:1000]:
        if not isinstance(item, dict):
            continue
        authors = [f"{a.get('given', '')} {a.get('family', '')}".strip()
                   for a in (item.get("author") or []) if isinstance(a, dict)]
        year = None
        date_parts = item.get("issued", {}).get("date-parts", []) if isinstance(item.get("issued"), dict) else []
        if date_parts and isinstance(date_parts[0], list) and date_parts[0]:
            year = date_parts[0][0]
        out.append(emit_paper(
            "crossref", item.get("DOI", ""), (item.get("title") or [""])[0], authors, year,
            item.get("DOI", ""), item.get("URL", "") or ("https://doi.org/" + normalize_doi(item.get("DOI", ""))),
            _strip_html(item.get("abstract", "")), 0,
            (item.get("container-title") or [""])[0]))
    return [paper for paper in out if paper.get("title") or paper.get("source_id")]


def engine_europepmc(project, query, limit, years, rl: RateLimiter) -> list:
    rl.wait("europepmc")
    terms = [clean_text(query, 5000)]
    if years[0] or years[1]:
        lo = f"{years[0] or 1}-01-01"
        hi = f"{years[1] or 3000}-12-31"
        terms.append(f"FIRST_PDATE:[{lo} TO {hi}]")
    params = {"query": " AND ".join(terms), "format": "json", "pageSize": _bounded_limit(limit, 1000)}
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(params)
    _record_request("europepmc", url)
    data = api_get_json(url, project)
    result_list = data.get("resultList") if isinstance(data.get("resultList"), dict) else {}
    results = result_list.get("result", [])
    if not isinstance(results, list):
        raise ValueError("Europe PMC result list is not a list")
    out = []
    for record in results[:1000]:
        if not isinstance(record, dict):
            continue
        pmid = record.get("pmid") or record.get("id", "")
        authors = [x.strip() for x in str(record.get("authorString", "")).split(",") if x.strip()]
        url_id = pmid or record.get("id", "")
        journal_info = record.get("journalInfo") if isinstance(record.get("journalInfo"), dict) else {}
        journal = journal_info.get("journal") if isinstance(journal_info.get("journal"), dict) else {}
        out.append(emit_paper(
            "europepmc", url_id, record.get("title", ""), authors,
            record.get("pubYear"), record.get("doi", ""),
            "https://europepmc.org/article/MED/" + urllib.parse.quote(str(url_id), safe=""),
            record.get("abstractText", ""), record.get("citedByCount", 0), journal.get("title", "")))
    return [paper for paper in out if paper.get("title") or paper.get("source_id")]


def _pubmed_term(query, years):
    term = clean_text(query, 5000)
    if years[0] or years[1]:
        lo = years[0] or 1
        hi = years[1] or 3000
        term += f" AND {lo}/01/01:{hi}/12/31[dp]"
    return term


def engine_pubmed(project, query, limit, years, rl: RateLimiter) -> list:
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
    rl.wait("pubmed")
    es_url = base + "/esearch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "term": _pubmed_term(query, years), "tool": APP,
        "retmax": _bounded_limit(limit, 200), "retmode": "json"})
    _record_request("pubmed", es_url)
    es = api_get_json(es_url, project)
    result = es.get("esearchresult") if isinstance(es.get("esearchresult"), dict) else {}
    ids = [str(x) for x in (result.get("idlist") or []) if str(x).isdigit()][:200]
    if not ids:
        return []
    rl.wait("pubmed")
    su_url = base + "/esummary.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "id": ",".join(ids), "tool": APP, "retmode": "json"})
    _record_request("pubmed", su_url)
    summary = api_get_json(su_url, project)
    records = summary.get("result") if isinstance(summary.get("result"), dict) else {}
    out = []
    for pid in ids:
        item = records.get(pid) if isinstance(records.get(pid), dict) else {}
        if not item or str(item.get("uid", "")) != pid:
            continue
        doi = ""
        for aid in item.get("articleids", []) or []:
            if isinstance(aid, dict) and aid.get("idtype") == "doi":
                doi = aid.get("value", "")
                break
        authors = [a.get("name", "") for a in (item.get("authors") or []) if isinstance(a, dict)]
        out.append(emit_paper(
            "pubmed", pid, item.get("title", ""), authors,
            (item.get("pubdate", "") or "")[:4], doi,
            "https://pubmed.ncbi.nlm.nih.gov/" + pid, "", 0,
            item.get("fulljournalname", "")))
    return out


def engine_arxiv(project, query, limit, years, rl: RateLimiter) -> list:
    rl.wait("arxiv")
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": "all:" + clean_text(query, 5000), "start": 0,
        "max_results": _bounded_limit(limit, 200)})
    _record_request("arxiv", url)
    xml = api_get_text(url)
    # ElementTree is stdlib-only and does not resolve external entities, but reject
    # DTD/entity declarations as a cheap, explicit defense against expansion bombs.
    if "<!doctype" in xml[:10000].casefold() or "<!entity" in xml[:10000].casefold():
        raise ValueError("arXiv XML contains a rejected DTD/entity declaration")
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as exc:
        raise ValueError("malformed arXiv XML") from exc
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for entry in root.findall("a:entry", ns)[:200]:
        title = clean_text(entry.findtext("a:title", "", ns)).strip()
        summary = clean_text(entry.findtext("a:summary", "", ns)).strip()
        aid = (entry.findtext("a:id", "", ns) or "").split("/abs/")[-1]
        authors = [clean_text(a.findtext("a:name", "", ns)) for a in entry.findall("a:author", ns)]
        published = entry.findtext("a:published", "", ns) or ""
        year = published[:4] if published else ""
        if not _year_in_range(year, years):
            continue
        doi = ""
        for link in entry.findall("a:link", ns):
            if link.get("title") == "doi":
                doi = link.get("href", "").replace("https://doi.org/", "")
                break
        out.append(emit_paper("arxiv", aid, title, authors, year, doi,
                              "https://arxiv.org/abs/" + urllib.parse.quote(aid, safe="/._-"),
                              summary, 0, "arXiv"))
    return out


ENGINES = {
    "openalex": engine_openalex,
    "semantic": engine_semantic,
    "crossref": engine_crossref,
    "europepmc": engine_europepmc,
    "pubmed": engine_pubmed,
    "arxiv": engine_arxiv,
}


def dedupe_papers(papers: list) -> list:
    """Merge exact identifiers and conservative title/year aliases.

    A DOI/source identifier is authoritative. A title alias is only used when
    the normalized title matches and the publication year matches (or one side
    has no year), limiting false merges while still joining cross-provider
    records that expose different identifiers.
    """
    seen = {}
    merged = []
    def aliases(paper):
        result = []
        primary = _paper_key(paper)
        if primary:
            result.append(primary)
        title = title_key(paper.get("title", ""))
        year = clean_text(paper.get("year", ""), 10)
        if title:
            result.append("title:" + title + "|" + year)
        return result
    for original in papers:
        if not isinstance(original, dict):
            continue
        paper = dict(original)
        paper["sources"] = list(paper.get("sources") or []) if isinstance(paper.get("sources"), list) else []
        source = clean_text(paper.get("source", ""), 40).casefold()
        if source and source not in paper["sources"]:
            paper["sources"].append(source)
        keys = aliases(paper)
        if not keys:
            continue
        match = next((seen[key] for key in keys if key in seen), None)
        if match is not None:
            current = merged[match]
            for field in ("abstract", "cited_by", "journal", "authors", "url", "doi"):
                if (not current.get(field)) or (field == "cited_by" and paper.get(field, 0) > current.get(field, 0)):
                    current[field] = paper.get(field)
            current["sources"] = sorted(set((current.get("sources") or []) + (paper.get("sources") or [])))
            old_prov = current.get("provenance") if isinstance(current.get("provenance"), list) else []
            new_prov = paper.get("provenance") if isinstance(paper.get("provenance"), list) else []
            current["provenance"] = (old_prov + [x for x in new_prov if x not in old_prov])[-100:]
            for key in keys:
                seen[key] = match
            continue
        paper["sources"] = sorted(set(paper["sources"]))
        index = len(merged)
        merged.append(paper)
        for key in keys:
            seen[key] = index
    return merged


# ── search and extraction ────────────────────────────────────────────────────
def _engine_list(value):
    if isinstance(value, str):
        return [x.strip().casefold() for x in value.split(",") if x.strip()]
    if isinstance(value, list):
        return [clean_text(x, 40).casefold() for x in value if clean_text(x, 40)]
    raise ValueError("engines must be a list or comma-separated string")


def run_search(args) -> int:
    global USE_CACHE, TIMEOUT, CACHE_WARNINGS, REQUEST_URLS
    st = ensure_project(args)
    project, paths, cfg = st["project"], st["paths"], st["config"]
    USE_CACHE = bool(cfg.get("use_cache", True))
    TIMEOUT = _safe_timeout(cfg.get("timeout", 25))
    CACHE_WARNINGS = []
    REQUEST_URLS = {}
    query = clean_text(args.query if args.query is not None else cfg.get("topic", ""), 5000)
    if not query:
        print("ERROR: no query (pass --query or set topic via init)", file=sys.stderr)
        return 1
    engines = _engine_list(args.engines if args.engines is not None else cfg.get("engines", DEFAULT_ENGINES))
    limit = _safe_limit(args.limit if args.limit is not None else cfg.get("limit", DEFAULT_LIMIT))
    years = _safe_years(args.years if args.years is not None else cfg.get("years", [None, None]))
    rl = RateLimiter(0.7)
    new_papers, failures, outcomes = [], [], []
    fetched_at = utc()
    for engine in engines:
        if engine not in ENGINES:
            failures.append(engine)
            outcomes.append({"engine": engine, "ok": False, "error": "unknown engine"})
            continue
        try:
            got = ENGINES[engine](project, query, limit, years, rl)
            if not isinstance(got, list):
                raise ValueError("engine did not return a list")
            got = [p for p in got if isinstance(p, dict)]
            _attach_provenance(got, engine, query, fetched_at)
            new_papers.extend(got)
            outcomes.append({"engine": engine, "ok": True, "records": len(got),
                             "request_urls": list(REQUEST_URLS.get(engine, []))})
            if not getattr(args, "json", False):
                print(f"  [ok] {engine:10s} -> {len(got)} results")
        except Exception as exc:
            failures.append(engine)
            outcomes.append({"engine": engine, "ok": False,
                             "error": f"{type(exc).__name__}: {clean_text(exc, 160)}"})
            if not getattr(args, "json", False):
                print(f"  [!] {engine:10s} {type(exc).__name__}: {clean_text(exc, 100)} — skipped")
    existing = load_papers(project)
    combined = dedupe_papers(existing + new_papers)
    save_papers(project, combined)
    cfg["engines"] = engines
    cfg["limit"] = limit
    cfg["years"] = years
    cfg["queries"] = (cfg.get("queries", []) + [{
        "query": query, "at": fetched_at, "engines": engines, "limit": limit,
        "years": years, "outcomes": outcomes,
    }])[-1000:]
    write_json(paths["config"], _normalize_config(cfg))
    result = {
        "schema_version": SCHEMA_VERSION, "query": query, "engines": engines,
        "limit": limit, "years": years, "outcomes": outcomes,
        "failed_engines": failures, "new_records": len(new_papers),
        "total_records": len(combined), "cache_warnings": CACHE_WARNINGS,
    }
    if getattr(args, "json", False):
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"\n  total evidence records: {len(combined)} (new {len(new_papers)})")
        if failures:
            print("  WARNING: engines unavailable: " + ", ".join(failures) + " — continuing with the rest.")
        if CACHE_WARNINGS:
            print("  WARNING: " + "; ".join(CACHE_WARNINGS[:3]))
    if not new_papers and len(combined) == 0:
        if not getattr(args, "json", False):
            print("  ERROR: no results at all (offline or all engines failed). Run again with network.", file=sys.stderr)
        return 2
    return 0


def cue_statements(text: str, cues=None) -> list:
    if not text:
        return []
    terms = tuple(clean_text(x, 200).casefold() for x in (cues or GAP_CUES) if clean_text(x, 200))
    sentences = re.split(r"(?<=[.!?])\s+", clean_text(text))
    out = []
    for sentence in sentences:
        low = sentence.casefold()
        if any(term in low for term in terms):
            candidate = clean_text(sentence, 500)
            if candidate and candidate not in out:
                out.append(candidate)
    return out[:6]


def _load_cues(project: Path, cuefile) -> list:
    if not cuefile:
        return list(GAP_CUES)
    path = _safe_project_path(project, cuefile, "cuefile")
    data = load_json_strict(path)
    if isinstance(data, dict):
        data = data.get("cues", [])
    if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
        raise ValueError("cuefile must be a JSON list or {\"cues\": [strings]}")
    cues = [clean_text(x, 200) for x in data if clean_text(x, 200)]
    if not cues:
        raise ValueError("cuefile contains no cues")
    return cues


def bootstrap_extract(st, args) -> list:
    papers = load_papers(st["project"])
    cues = _load_cues(st["project"], getattr(args, "cuefile", None))
    outputs = []
    for paper in papers:
        abstract_cues = cue_statements(paper.get("abstract", ""), cues)
        manual = clean_text(paper.get("gap_statement", ""), 500)
        if manual:
            abstract_cues = [manual] + [x for x in abstract_cues if x != manual]
        low_title = clean_text(paper.get("title", "")).casefold()
        if any(word in low_title for word in ("gap", "understud", "unknown", "unexplored", "missing", "lack")):
            abstract_cues.append("Title signals a gap: " + clean_text(paper.get("title", ""), 500))
        identifier = paper_identifier(paper)
        identifiers = [identifier] if identifier and valid_identifier(identifier) else []
        for statement in dict.fromkeys(abstract_cues):
            source_id = clean_text(paper.get("id", ""), 500)
            digest = hashlib.sha256((statement + "\0" + source_id).encode("utf-8")).hexdigest()[:12]
            outputs.append({
                "id": "gap-" + digest,
                "statement": clean_text(statement, 500),
                "type": "", "secondary_type": [], "importance": {}, "confidence": "",
                "sources": identifiers, "invalid_sources": [],
                "source_paper_id": source_id,
                "source_paper_title": clean_text(paper.get("title", ""), 10_000),
                "source_provenance": [{"source": paper.get("source", ""), "identifier": identifier}]
                if identifier else [],
                "research_question": "", "novelty_status": "unchecked", "extracted": utc(),
            })
    return outputs


def run_extract(args) -> int:
    st = ensure_project(args)
    candidates = bootstrap_extract(st, args)
    existing = load_gaps(st["project"])
    seen = {g.get("id") for g in existing}
    for candidate in candidates:
        if candidate["id"] not in seen:
            existing.append(candidate)
            seen.add(candidate["id"])
    save_gaps(st["project"], existing)
    print(f"  evidence records processed: {len(load_papers(st['project']))}")
    print(f"  candidate gap statements: {len(candidates)} (total stored {len(existing)})")
    return 0


# ── classification, validation, ranking and reporting ────────────────────────
def classify_type(statement: str, context: str = ""):
    hay = (clean_text(statement) + " " + clean_text(context)).casefold()
    scores = {kind: sum(1 for pattern in patterns if pattern in hay)
              for kind, patterns in TAXONOMY.items()}
    order = sorted(scores.items(), key=lambda pair: (-pair[1], pair[0]))
    top = order[0]
    second = order[1] if len(order) > 1 else ("", 0)
    if top[1] == 0:
        return "evidence", []
    return top[0], [second[0]] if second[1] > 0 and second[0] != top[0] else []


def _score(value, default=0):
    if isinstance(value, bool):
        return default
    try:
        number = int(value)
    except (TypeError, ValueError):
        return default
    return max(0, min(3, number))


def scores_from_importance(importance) -> int:
    if not isinstance(importance, dict):
        return 0
    return sum(_score(importance.get(d), 0) for d in DIMENSIONS)


def default_importance(novelty_status="unchecked", supported=1) -> dict:
    novel = {"checked_new": 3, "checked_seen": 1, "unchecked": 2}.get(novelty_status, 2)
    practical = 2 if supported >= 2 else 1
    return {"theoretical": 2, "practical": practical, "feasibility": 2,
            "novelty": novel, "coherence": 2, "estimated": True,
            "note": "Baseline heuristic scores; override with independently judged 0-3 values."}


def _validated_importance(value, baseline=None):
    if not isinstance(value, dict):
        raise ValueError("importance override must be an object")
    result = dict(baseline or {})
    for dimension in DIMENSIONS:
        if dimension in value:
            if isinstance(value[dimension], bool) or not isinstance(value[dimension], (int, str)):
                raise ValueError(f"{dimension} score must be an integer from 0 to 3")
            try:
                score = int(value[dimension])
            except ValueError as exc:
                raise ValueError(f"{dimension} score must be an integer from 0 to 3") from exc
            if not 0 <= score <= 3:
                raise ValueError(f"{dimension} score must be from 0 to 3")
            result[dimension] = score
    result["estimated"] = False
    result.pop("total", None)
    result["total"] = scores_from_importance(result)
    return result


def run_classify(args) -> int:
    st = ensure_project(args)
    project = st["project"]
    gaps = load_gaps(project)
    override_path = project_paths(project)["scores"]
    if getattr(args, "scores", None):
        override_path = _safe_project_path(project, args.scores, "scores file")
    overrides = load_json_strict(override_path, {}) if override_path.exists() else {}
    if not isinstance(overrides, dict):
        raise ValueError("scores file must contain an object keyed by gap id")
    controlled = 0
    for gap in gaps:
        gap["type"], gap["secondary_type"] = classify_type(
            gap.get("statement", ""), gap.get("source_paper_title", ""))
        baseline = default_importance(gap.get("novelty_status", "unchecked"),
                                      len(gap.get("sources", []) or []))
        if gap.get("id") in overrides:
            gap["importance"] = _validated_importance(overrides[gap["id"]], baseline)
            controlled += 1
        else:
            gap["importance"] = baseline
        gap["importance"]["total"] = scores_from_importance(gap["importance"])
    save_gaps(project, gaps)
    print(f"  classified {len(gaps)} gap candidate(s) into the six-type taxonomy")
    if not controlled:
        print("  NOTE: importance scores are baseline estimates (estimated=True).")
        print("        Supply per-gap 0-3 scores in scores.json (or --scores) to finalise.")
    return 0


def _identifier_parts(identifier):
    value = clean_text(identifier, 500).strip()
    if valid_doi(value):
        return "doi", normalize_doi(value)
    match = re.fullmatch(r"([A-Za-z]+):([A-Za-z0-9._:/-]{1,300})", value)
    if match:
        return match.group(1).casefold(), match.group(2)
    return "", ""


def resolve_citation(identifier: str, timeout: int = 20, rl=None, project=None) -> bool:
    """Resolve a DOI/accession using its owning key-free scholarly endpoint."""
    kind, value = _identifier_parts(identifier)
    if rl is not None:
        rl.wait(kind or "identifier")
    def get_json(url):
        return api_get_json(url, project, use_cache=True, timeout=timeout) if project else _http_json(url, timeout)
    try:
        if kind == "doi":
            get_json("https://api.crossref.org/works/" + urllib.parse.quote(value, safe=""))
            return True
        if kind == "pmid":
            data = get_json("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?" +
                            urllib.parse.urlencode({"db": "pubmed", "id": value, "tool": APP, "retmode": "json"}))
            return value in (data.get("result") or {})
        if kind == "arxiv":
            text = api_get_text("https://export.arxiv.org/api/query?" +
                                urllib.parse.urlencode({"id_list": value}), timeout)
            return value in text
        if kind == "epmc":
            data = get_json("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" +
                            urllib.parse.urlencode({"query": "EXT_ID:" + value, "format": "json", "pageSize": 1}))
            return int((data.get("hitCount") or 0)) > 0
        # OpenAlex/S2 identifiers are valid provenance identifiers but do not
        # get promoted to a resolved citation by a Crossref DOI check.
        return False
    except Exception:
        return False


def run_validate(args) -> int:
    st = ensure_project(args)
    project = st["project"]
    gaps = load_gaps(project)
    do_web = bool(getattr(args, "check_web", False))
    distribution = {"checked_new": 0, "checked_seen": 0, "unchecked": 0, "unverified": 0}
    validation_rl = RateLimiter(0.7) if do_web else None
    for gap in gaps:
        raw_sources = gap.get("sources") if isinstance(gap.get("sources"), list) else []
        valid_sources, invalid_sources = [], []
        for source in raw_sources:
            source = clean_text(source, 500)
            if valid_identifier(source) and source not in valid_sources:
                valid_sources.append(source)
            elif source:
                invalid_sources.append(source)
        verified = []
        if do_web:
            verified = [source for source in valid_sources
                        if resolve_citation(source, rl=validation_rl, project=project)]
        independent = set()
        for provenance in gap.get("source_provenance", []) or []:
            if isinstance(provenance, dict) and provenance.get("source"):
                independent.add(clean_text(provenance.get("source"), 40).casefold())
        if not independent:
            independent = set(valid_sources)
        all_verified = bool(valid_sources) and len(verified) == len(valid_sources) if do_web else False
        if not valid_sources:
            confidence, verification = "Low", "unverified"
            gap["exploratory"] = True
            novelty_key = "unverified"
        elif do_web and all_verified and len(independent) >= 2:
            confidence, verification, novelty_key = "High", "web-validated", gap.get("novelty_status", "unchecked")
        elif (do_web and verified) or (not do_web and valid_sources):
            confidence, verification, novelty_key = "Medium", ("web-validated" if do_web else "identifier-present"), gap.get("novelty_status", "unchecked")
        else:
            confidence, verification, novelty_key = "Low", "unverified", "unverified"
            gap["exploratory"] = True
        gap["sources"] = valid_sources
        gap["invalid_sources"] = invalid_sources
        gap["verified_sources"] = verified
        gap["confidence"] = confidence
        gap["verification"] = verification
        if novelty_key not in distribution:
            novelty_key = "unverified"
        distribution[novelty_key] += 1
    save_gaps(project, gaps)
    result = {"schema_version": SCHEMA_VERSION, "validated": len(gaps),
              "web_checked": do_web, "novelty_status": distribution}
    if getattr(args, "json", False):
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"  validated {len(gaps)} gap(s); confidence set per source-verification rules.")
        print("  novelty status distribution:", distribution)
    return 0


def run_rank(args) -> int:
    st = ensure_project(args)
    gaps = load_gaps(st["project"])
    min_total = int(args.min_total or 0)
    min_confidence = (args.min_confidence or "low").casefold()
    order = {"low": 0, "medium": 1, "high": 2}
    ranked = []
    for gap in gaps:
        importance = gap.get("importance") if isinstance(gap.get("importance"), dict) else {}
        total = scores_from_importance(importance)
        gap.setdefault("importance", {})["total"] = total
        confidence = clean_text(gap.get("confidence", "low")).casefold()
        if total >= min_total and order.get(confidence, 0) >= order.get(min_confidence, 0):
            ranked.append(gap)
    ranked.sort(key=lambda gap: (-scores_from_importance(gap.get("importance", {})),
                                 -order.get(clean_text(gap.get("confidence", "low")).casefold(), 0),
                                 clean_text(gap.get("id", ""))))
    selected = ranked[:max(0, int(args.top if args.top is not None else 10))]
    if getattr(args, "json", False):
        print(json.dumps({"schema_version": SCHEMA_VERSION, "count": len(selected),
                          "min_total": min_total, "min_confidence": min_confidence,
                          "gaps": selected}, ensure_ascii=False, sort_keys=True))
    else:
        print(f"  ranked {len(ranked)} gap(s) that clear score>= {min_total} and confidence>= {min_confidence}:")
        for index, gap in enumerate(selected, 1):
            print(f"   {index:>2}. [{gap.get('confidence', 'Low'):6s}] "
                  f"{scores_from_importance(gap.get('importance', {})):>2}/15 "
                  f"({gap.get('type', '?'):14s}) {clean_text(gap.get('statement', ''), 100)}")
    return 0


def formulate_question(gap: dict) -> str:
    statement = clean_text(gap.get("statement", ""), 220)
    return ("What study could test whether the reported limitation — " + statement +
            " — holds for a specified population, intervention/comparator, and outcome, "
            "and under what explicit assumptions?")


def _md(value, limit=1000):
    text = html.escape(clean_text(value, limit), quote=False)
    return text.replace("|", "\\|").replace("`", "&#96;").replace("[", "\\[").replace("]", "\\]")


def run_report(args) -> int:
    st = ensure_project(args)
    project, paths, cfg = st["project"], st["paths"], st["config"]
    gaps = load_gaps(project)
    top = max(0, int(args.top if args.top is not None else 8))
    confidence_order = {"low": 0, "medium": 1, "high": 2}
    ranked = sorted(gaps, key=lambda gap: (
        -scores_from_importance(gap.get("importance", {})),
        -confidence_order.get(clean_text(gap.get("confidence", "low")).casefold(), 0),
        clean_text(gap.get("id", ""))))
    include = ranked[:top]
    changed = False
    for gap in include:
        if not gap.get("research_question"):
            gap["research_question"] = formulate_question(gap)
            changed = True
    if changed:
        save_gaps(project, gaps)
    lines = [
        "# Research Gap Report", "",
        f"**Skill:** {APP} · **CLI:** {VERSION} · **Schema:** {SCHEMA_VERSION}",
        f"**Topic:** {_md(cfg.get('topic', '') or '(not set)')}",
        f"**Generated:** {utc()}", "",
        "> This is a candidate-gap report, not proof that an absence exists. A cue",
        "> sentence is evidence about what a source said, not evidence that the field",
        "> contains no other work. Re-run with broader sources and apply a PICOS/AHRQ",
        "> review before treating a candidate as a research gap.", "",
        "## Search provenance", "",
    ]
    queries = cfg.get("queries", [])
    if queries:
        for query in queries[-10:]:
            if isinstance(query, dict):
                lines.append(f"- **{_md(query.get('at', ''))}:** query=`{_md(query.get('query', ''), 500)}`; "
                             f"engines=`{_md(','.join(query.get('engines', []) or []), 300)}`; "
                             f"limit={query.get('limit')}; years={query.get('years')}")
    else:
        lines.append("- No automated search run is recorded in config.json.")
    lines += ["", "## Executive summary", "",
              f"Candidate gaps identified: **{len(gaps)}**; shown: **{len(include)}** (stable rank order).", "",
              "## PICO / search horizon", ""]
    if cfg.get("pico"):
        for key in sorted(cfg["pico"]):
            lines.append(f"- **{_md(key, 80).capitalize()}:** {_md(cfg['pico'][key], 2000)}")
    else:
        lines.append("- No PICO/PICOS object was supplied.")
    lines += ["", "## Candidate gaps", ""]
    for index, gap in enumerate(include, 1):
        importance = gap.get("importance") if isinstance(gap.get("importance"), dict) else {}
        secondary = ", ".join(str(x) for x in (gap.get("secondary_type") or []))
        identifiers = gap.get("sources") or []
        if identifiers:
            source_text = ", ".join(_md(x, 500) for x in identifiers)
        else:
            source_text = "no valid identifier (EXPLORATORY/HYPOTHETICAL)"
        verification = gap.get("verification", "not validated")
        lines += [
            f"### {index}. {_md(gap.get('statement', ''), 800)}", "",
            f"- **Gap type:** {_md(gap.get('type', 'unclassified'), 80)}" +
            (f" / secondary: {_md(secondary, 300)}" if secondary else ""),
            f"- **Importance (five dimensions, 0–3 each / max 15):** "
            f"theoretical={importance.get('theoretical', 0)}, practical={importance.get('practical', 0)}, "
            f"feasibility={importance.get('feasibility', 0)}, novelty={importance.get('novelty', 0)}, "
            f"coherence={importance.get('coherence', 0)} → **{importance.get('total', 0)}/15**" +
            (" *(estimated)*" if importance.get("estimated") else ""),
            f"- **Confidence:** {_md(gap.get('confidence', 'Low'), 50)}" +
            (" — **Exploratory/Hypothetical**" if gap.get("exploratory") else ""),
            f"- **Verification:** {_md(verification, 80)}",
            f"- **Source evidence:** {source_text}",
            f"- **Candidate research question:** {_md(gap.get('research_question', ''), 1200)}", "",
        ]
    lines += [
        "## Method and honesty constraints", "",
        "1. A gap statement is a source-linked **candidate**, not proof of absence.",
        "2. A valid DOI/accession is provenance; `--check-web` is required for web validation.",
        "3. High confidence requires at least two independent source labels and every identifier resolved in the check; otherwise confidence is capped at Medium or Low.",
        "4. Importance is separate from identification; baseline scores are estimates unless overridden with judged 0–3 values.",
        "5. Search results are bounded by the recorded query, engines, years, limits, and API availability; missing results may be a search artifact.",
        "6. Search text and API metadata are untrusted data; no retrieved text is executed.", "",
        "## Limitations", "",
        "- Metadata APIs do not replace a systematic review, citation-network review, grant/trial/preprint checks, or human appraisal.",
        "- An empty result set means that this bounded search found no records; it does not establish that no literature exists.", "",
    ]
    if not include:
        lines.append("*No candidate gaps found — run `search`, `extract`, `classify`, and `validate` first.*")
    output = _safe_project_path(project, args.out, "report output") if getattr(args, "out", None) else paths["report"]
    _atomic_write_text(output, "\n".join(lines) + "\n")
    print(f"  report written: {output}")
    return 0


def run_status(args) -> int:
    st = ensure_project(args)
    project, cfg = st["project"], st["config"]
    papers, gaps = load_papers(project), load_gaps(project)
    by_source = {}
    for paper in papers:
        source = paper.get("source", "?")
        by_source[source] = by_source.get(source, 0) + 1
    result = {"schema_version": SCHEMA_VERSION, "project": str(project),
              "topic": cfg.get("topic", ""), "evidence_records": len(papers),
              "gaps": len(gaps), "evidence_by_source": by_source,
              "engines": cfg.get("engines", []), "queries_recorded": len(cfg.get("queries", []))}
    if getattr(args, "json", False):
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"  project: {project}")
        print(f"  topic:   {cfg.get('topic', '(not set)')}")
        print(f"  evidence records: {len(papers)} ; gaps: {len(gaps)}")
        print("  evidence by source:", by_source)
    return 0


def run_selftest(args) -> int:
    import tempfile
    root = Path(args.dir or tempfile.mkdtemp(prefix="rgf-selftest-"))
    project = root / "proj"
    project.mkdir(parents=True, exist_ok=True)
    papers = [
        emit_paper("openalex", "W1", "Impact of X intervention on outcomes", ["A"], 2021,
                   "10.1000/x1", "https://example.invalid/w1",
                   "We found limited evidence that X is effective; however, small sample size and no control group limit conclusions. Future work should test in rural populations."),
        emit_paper("arxiv", "2401.12345", "An understudied mechanism of Y", ["B"], 2024, "",
                   "https://arxiv.org/abs/2401.12345",
                   "The mechanism remains unclear; more studies are needed in low-resource settings."),
    ]
    save_papers(project, papers)
    class Namespace:
        pass
    ns = Namespace(); ns.dir = str(project); ns.cuefile = None
    st = ensure_project(ns)
    candidates = bootstrap_extract(st, ns)
    save_gaps(project, candidates)
    for gap in load_gaps(project):
        gap["type"], gap["secondary_type"] = classify_type(gap.get("statement", ""))
        gap["importance"] = default_importance("unchecked", len(gap.get("sources", [])))
        gap["importance"]["total"] = scores_from_importance(gap["importance"])
    save_gaps(project, load_gaps(project))
    val = Namespace(); val.dir = str(project); val.check_web = False; val.json = False
    run_validate(val)
    report = Namespace(); report.dir = str(project); report.top = 8; report.out = str(project / "report.md")
    run_report(report)
    text = (project / "report.md").read_text(encoding="utf-8")
    ok = bool(load_papers(project)) and bool(load_gaps(project)) and "Candidate research question" in text and "EXPLORATORY" not in text
    print(f"  self-test: {len(load_gaps(project))} gap(s) generated; report ok={ok}")
    return 0 if ok else 1


# ── CLI ──────────────────────────────────────────────────────────────────────
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="research_gap_cli.py", description=__doc__)
    parser.add_argument("--version", action="version", version=VERSION)
    sub = parser.add_subparsers(dest="command", required=True)

    def add_dir(command):
        command.add_argument("--dir", required=True, help="Project directory")

    command = sub.add_parser("init", help="Create a research-gap project")
    add_dir(command); command.add_argument("--topic", required=True); command.add_argument("--pico", default="{}")
    command.add_argument("--json", action="store_true")

    command = sub.add_parser("search", help="Query bounded key-free scholarly APIs")
    add_dir(command); command.add_argument("--query"); command.add_argument("--engines")
    command.add_argument("--limit", type=int); command.add_argument("--years", nargs=2, type=int)
    command.add_argument("--json", action="store_true", help="Emit one machine-readable result object")

    command = sub.add_parser("extract", help="Extract source-linked candidate gap cues")
    add_dir(command); command.add_argument("--cuefile", help="Project-relative JSON list of cue phrases")

    command = sub.add_parser("classify", help="Assign taxonomy and transparent importance scores")
    add_dir(command); command.add_argument("--scores", help="Project-relative JSON score overrides")

    command = sub.add_parser("validate", help="Validate identifiers and optionally resolve them on the web")
    add_dir(command); command.add_argument("--check-web", action="store_true")
    command.add_argument("--json", action="store_true")

    command = sub.add_parser("rank", help="Rank gaps by importance and confidence")
    add_dir(command); command.add_argument("--min-total", type=int); command.add_argument("--top", type=int)
    command.add_argument("--min-confidence", choices=["low", "medium", "high"]); command.add_argument("--json", action="store_true")

    command = sub.add_parser("report", help="Emit the Markdown candidate-gap report")
    add_dir(command); command.add_argument("--top", type=int); command.add_argument("--out")

    command = sub.add_parser("status", help="Show project state")
    add_dir(command); command.add_argument("--json", action="store_true")

    command = sub.add_parser("selftest", help="Run an offline self-test")
    command.add_argument("--dir")
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    dispatch = {"init": _init_msg, "search": run_search, "extract": run_extract,
                "classify": run_classify, "validate": run_validate, "rank": run_rank,
                "report": run_report, "status": run_status, "selftest": run_selftest}
    try:
        return dispatch[args.command](args)
    except SystemExit:
        raise
    except Exception as exc:
        print(f"ERROR: {type(exc).__name__}: {clean_text(exc, 300)}", file=sys.stderr)
        return 1


def _init_msg(args) -> int:
    state = ensure_project(args)
    result = {"schema_version": SCHEMA_VERSION, "project": str(state["project"]),
              "topic": state["config"].get("topic", ""), "next": "search"}
    if getattr(args, "json", False):
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(f"  project initialised: {state['project']}")
        print(f"  topic: {state['config'].get('topic')}")
        print("  next: run `python3 scripts/research_gap_cli.py search --dir <proj> --query \"...\"`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
