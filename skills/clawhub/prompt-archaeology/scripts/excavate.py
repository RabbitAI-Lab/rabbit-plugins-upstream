#!/usr/bin/env python3
"""
excavate.py — Prompt Archaeology: excavate forgotten solutions from session logs.

A stdlib-only searcher + ranker for digging through conversation/session history.
Crawls directories of .md/.txt/.json/.jsonl files, scores them against a query
using a transparent composite ranker (density + recency + code + resolution),
and prints the buried artifacts.

Usage:
    python3 excavate.py dig <directory> --query "..." [options]
    python3 excavate.py index <directory> --out <file>
    python3 excavate.py query <index-file> --query "..." [options]

No third-party dependencies. Python 3.8+.

Author: Denis Voronin
License: MIT
"""

from __future__ import annotations

import argparse
import datetime as _dt
import functools
import hashlib
import json
import math
import os
import pickle
import re
import sys
from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

# ---------------------------------------------------------------------------
# Tunable scoring weights (see references/relevance-scoring.md)
# ---------------------------------------------------------------------------
WEIGHT_DENSITY: float = 0.25
WEIGHT_RECENCY: float = 0.15
WEIGHT_CODE: float = 0.25
WEIGHT_RESOLUTION: float = 0.35
assert abs(WEIGHT_DENSITY + WEIGHT_RECENCY + WEIGHT_CODE + WEIGHT_RESOLUTION - 1.0) < 1e-6

# Default Jaccard threshold for near-duplicate collapse.
DEDUP_THRESHOLD: float = 0.85

# Resolution marker lexicon (phrase -> strength multiplier).
_RESOLUTION_MARKERS: Dict[str, float] = {
    # Strong — explicit success.
    "that fixed it": 1.0,
    "that solved it": 1.0,
    "works now": 1.0,
    "working now": 1.0,
    "it works": 1.0,
    "this works": 1.0,
    "merged": 1.0,
    "deployed": 1.0,
    "shipped": 1.0,
    "problem solved": 1.0,
    "issue resolved": 1.0,
    "all green": 1.0,
    "tests pass": 1.0,
    "tests passed": 1.0,
    # Medium — past-tense success without emphatic confirmation.
    "fixed": 0.7,
    "resolved": 0.7,
    "solved": 0.7,
    "working": 0.7,
    "success": 0.7,
    # Weak — hedged success.
    "seems to work": 0.4,
    "might be it": 0.4,
    "i think that's it": 0.4,
    "looks good": 0.4,
    "appears to work": 0.4,
}

# A small English stopword list for normalization. Kept inline to stay stdlib-only
# and avoid importing a corpus that may be absent on minimal installs.
_STOPWORDS = frozenset(
    """a an the and or but if then else of to in on at by for with from into
    upon about as is are was were be been being this that these those it its
    i you he she we they me him her us them my your his our their what which
    who whom whose where when why how all any both each few more most other
    some such no nor not only own same so than too very can will just don
    should now do does did doing would could should""".split()
)


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class SessionDoc:
    """A single parsed session/log file held in the index."""

    path: str
    text: str  # normalized lowercase text used for matching
    raw: str  # original text (for extraction)
    mtime: float  # file modification time (epoch seconds)
    code_blocks: List[str] = field(default_factory=list)
    match_count: int = 0  # set during scoring
    resolution_hits: List[Tuple[str, float]] = field(default_factory=list)

    @property
    def length(self) -> int:
        return len(self.text)


@dataclass
class SearchHit:
    """A scored result returned from a search."""

    path: str
    score: float
    explanation: Optional[Dict[str, float]] = None
    extraction: str = ""
    matches: List[str] = field(default_factory=list)
    mtime: float = 0.0
    cluster_size: int = 1
    duplicates: List[str] = field(default_factory=list)
    # Raw per-signal values (always populated, used internally for scoring).
    density_raw: float = 0.0
    code_raw: float = 0.0
    resolution_raw: float = 0.0


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?\n)---\s*\n", re.DOTALL)
_FENCED_RE = re.compile(r"```[^\n]*\n(.*?)```", re.DOTALL)
_FRONTMATTER_DATE_RE = re.compile(
    r"(?:date|session_date|created|timestamp):\s*['\"]?(\d{4}-\d{2}-\d{2})", re.IGNORECASE
)


def _parse_frontmatter(raw: str) -> Tuple[Optional[str], str]:
    """Strip YAML frontmatter; return (date_iso_or_None, body)."""
    m = _FRONTMATTER_RE.match(raw)
    if not m:
        return None, raw
    fm = m.group(1)
    body = raw[m.end():]
    dm = _FRONTMATTER_DATE_RE.search(fm)
    return (dm.group(1) if dm else None), body


def _extract_code_blocks(body: str) -> List[str]:
    return [m.group(1) for m in _FENCED_RE.finditer(body)]


def _normalize(text: str) -> str:
    """Lowercase, strip punctuation, collapse whitespace."""
    text = text.lower()
    text = re.sub(r"[`*_~#>\-]", " ", text)  # markdown noise
    text = re.sub(r"[^\w\s]", " ", text)  # punctuation
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _parse_markdown(raw: str) -> Tuple[str, List[str], Optional[str]]:
    date, body = _parse_frontmatter(raw)
    code = _extract_code_blocks(body)
    return _normalize(body), code, date


def _parse_text(raw: str) -> Tuple[str, List[str], Optional[str]]:
    return _normalize(raw), _extract_code_blocks(raw), None


def _parse_json_messages(raw: str) -> str:
    """Concatenate content fields from a JSON session object/array."""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        return raw
    items = data if isinstance(data, list) else [data]
    out = []
    for item in items:
        if not isinstance(item, dict):
            continue
        for key in ("content", "text", "message", "body"):
            val = item.get(key)
            if isinstance(val, str):
                out.append(val)
            elif isinstance(val, dict) and isinstance(val.get("content"), str):
                out.append(val["content"])
    return "\n".join(out)


def _parse_file(path: str) -> Optional[SessionDoc]:
    """Parse a file into a SessionDoc. Returns None on failure."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        mtime = os.path.getmtime(path)
    except OSError:
        return None

    ext = os.path.splitext(path)[1].lower()
    if ext in (".md", ".markdown"):
        text, code, _date = _parse_markdown(raw)
    elif ext == ".json":
        body = _parse_json_messages(raw)
        text, code, _date = _parse_text(body)
    elif ext == ".jsonl":
        lines = []
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            lines.append(_parse_json_messages(line))
        body = "\n".join(lines)
        text, code, _date = _parse_text(body)
    else:  # .txt or unknown — treat as plain text
        text, code, _date = _parse_text(raw)

    return SessionDoc(path=path, text=text, raw=raw, mtime=mtime, code_blocks=code)


# ---------------------------------------------------------------------------
# Index
# ---------------------------------------------------------------------------


class ArchaeologyIndex:
    """Holds parsed SessionDocs and answers ranked searches over them."""

    FORMAT_VERSION = 1

    def __init__(self) -> None:
        self.docs: List[SessionDoc] = []

    # -- ingestion -------------------------------------------------------

    def scan(self, root: str) -> int:
        """Walk a directory recursively, parsing supported files."""
        count = 0
        for dirpath, _dirs, files in os.walk(root):
            for name in files:
                ext = os.path.splitext(name)[1].lower()
                if ext not in (".md", ".markdown", ".txt", ".json", ".jsonl"):
                    continue
                full = os.path.join(dirpath, name)
                doc = _parse_file(full)
                if doc is not None and doc.text:
                    self.docs.append(doc)
                    count += 1
        return count

    def add_file(self, path: str) -> bool:
        doc = _parse_file(path)
        if doc is None or not doc.text:
            return False
        self.docs.append(doc)
        return True

    # -- persistence -----------------------------------------------------

    def save(self, path: str) -> None:
        with open(path, "wb") as fh:
            pickle.dump(
                {"version": self.FORMAT_VERSION, "docs": self.docs}, fh, protocol=pickle.HIGHEST_PROTOCOL
            )

    @classmethod
    def load(cls, path: str) -> "ArchaeologyIndex":
        with open(path, "rb") as fh:
            data = pickle.load(fh)
        idx = cls()
        idx.docs = data.get("docs", [])
        return idx

    # -- search ----------------------------------------------------------

    def search(
        self,
        query: str,
        top: int = 5,
        explain: bool = False,
        exclude: Sequence[str] = (),
        after: Optional[_dt.date] = None,
        before: Optional[_dt.date] = None,
    ) -> List[SearchHit]:
        """Score all docs against `query` and return the top hits.

        Multiple terms in `query` are AND'd: all must appear in the doc.
        """
        terms = [t for t in _normalize(query).split() if t and t not in _STOPWORDS]
        if not terms:
            return []

        excl = [w.lower() for w in exclude]

        scored: List[SearchHit] = []
        for doc in self.docs:
            if not _all_terms_present(doc.text, terms):
                continue
            if excl and any(w in doc.text for w in excl):
                continue
            if after and _doc_date(doc) < after:
                continue
            if before and _doc_date(doc) > before:
                continue
            scored.append(_score_doc(doc, terms, explain))

        if not scored:
            return []

        # Normalize per-signal across the result set before combining.
        _normalize_signals(scored)

        scored.sort(key=lambda h: h.score, reverse=True)
        return scored[:top]

    # -- dedup -----------------------------------------------------------

    def dedup_hits(
        self, hits: List[SearchHit], threshold: float = DEDUP_THRESHOLD
    ) -> List[SearchHit]:
        """Collapse near-duplicate hits into clusters. Canonical = highest score."""
        if len(hits) <= 1:
            return hits

        by_path = {h.path: h for h in hits}
        docs = {d.path: d for d in self.docs}

        clusters: List[List[str]] = []
        assigned: Dict[str, int] = {}

        for i, hi in enumerate(hits):
            if hi.path in assigned:
                continue
            cluster = [hi.path]
            assigned[hi.path] = len(clusters)
            di = docs.get(hi.path)
            if di is None:
                clusters.append(cluster)
                continue
            ti = _masked_tokens(di.text)
            for hj in hits[i + 1:]:
                if hj.path in assigned:
                    continue
                dj = docs.get(hj.path)
                if dj is None:
                    continue
                tj = _masked_tokens(dj.text)
                sim = _jaccard(ti, tj)
                if sim >= threshold:
                    cluster.append(hj.path)
                    assigned[hj.path] = assigned[hi.path]
            clusters.append(cluster)

        out: List[SearchHit] = []
        for cluster in clusters:
            members = [by_path[p] for p in cluster]
            members.sort(key=lambda h: h.score, reverse=True)
            canonical = members[0]
            canonical.cluster_size = len(cluster)
            canonical.duplicates = [m.path for m in members[1:]]
            out.append(canonical)
        out.sort(key=lambda h: h.score, reverse=True)
        return out


# ---------------------------------------------------------------------------
# Scoring helpers
# ---------------------------------------------------------------------------


def _all_terms_present(text: str, terms: Sequence[str]) -> bool:
    return all(t in text for t in terms)


def _count_matches(text: str, terms: Sequence[str]) -> int:
    return sum(text.count(t) for t in terms)


def _count_resolution(text: str) -> List[Tuple[str, float]]:
    hits = []
    for phrase, strength in _RESOLUTION_MARKERS.items():
        if phrase in text:
            hits.append((phrase, strength))
    return hits


def _score_doc(doc: SessionDoc, terms: Sequence[str], explain: bool) -> SearchHit:
    raw_matches = _count_matches(doc.text, terms)
    doc.match_count = raw_matches
    doc.resolution_hits = _count_resolution(doc.text)

    matches = []
    for term in terms:
        idx = doc.text.find(term)
        if idx >= 0:
            start = max(0, idx - 40)
            end = min(len(doc.raw), idx + len(term) + 40)
            snippet = doc.raw[start:end].replace("\n", " ").strip()
            matches.append(snippet)

    extraction = ""
    if doc.code_blocks:
        # pick the code block with highest term density
        best = max(
            doc.code_blocks,
            key=lambda b: sum(b.lower().count(t) for t in terms),
        )
        if any(t in best.lower() for t in terms):
            extraction = best.strip()

    hit = SearchHit(
        path=doc.path,
        score=0.0,  # filled in by _normalize_signals
        explanation={} if explain else None,
        extraction=extraction,
        matches=matches[:3],
        mtime=doc.mtime,
    )
    # stash raw signals on the hit for later combination (always, regardless of --explain)
    hit.density_raw = float(raw_matches)
    hit.code_raw = float(min(1, len(doc.code_blocks)))
    hit.resolution_raw = float(sum(s for _, s in doc.resolution_hits))
    if explain:
        hit.explanation = {}  # filled in by _normalize_signals
    return hit


def _normalize_signals(hits: List[SearchHit]) -> None:
    """Normalize per-signal across the result set and combine into the composite score."""
    if not hits:
        return

    max_density = max((h.density_raw for h in hits), default=0.0) or 1.0
    max_mtime = max((h.mtime for h in hits), default=0.0)
    min_mtime = min((h.mtime for h in hits), default=0.0)
    mtime_span = (max_mtime - min_mtime) or 1.0
    max_resolution = max((h.resolution_raw for h in hits), default=0.0) or 1.0

    for h in hits:
        # log-saturated density
        density = math.log1p(h.density_raw) / math.log1p(max_density)
        recency = (h.mtime - min_mtime) / mtime_span
        code = min(1.0, h.code_raw)
        resolution = h.resolution_raw / max_resolution

        composite = (
            WEIGHT_DENSITY * density
            + WEIGHT_RECENCY * recency
            + WEIGHT_CODE * code
            + WEIGHT_RESOLUTION * resolution
        )
        h.score = composite
        # populate the explanation dict only if --explain was requested
        if h.explanation is not None:
            h.explanation = {
                "density": round(density, 3),
                "recency": round(recency, 3),
                "code": round(code, 3),
                "resolution": round(resolution, 3),
            }


# ---------------------------------------------------------------------------
# Dedup helpers
# ---------------------------------------------------------------------------


@functools.lru_cache(maxsize=4096)
def _normalized_token_set(text: str) -> frozenset:
    return frozenset(w for w in text.split() if w not in _STOPWORDS)


_VERSIONISH = re.compile(r"\b\d+\.\d+\.\d+\b")
_DATEISH = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
_PATHISH = re.compile(r"(?:/[\w.\-]+)+")


def _masked_tokens(text: str) -> frozenset:
    """Tokens with version/date/path-like strings masked, for variant detection."""
    text = _VERSIONISH.sub("VER", text)
    text = _DATEISH.sub("DATE", text)
    text = _PATHISH.sub("PATH", text)
    return _normalized_token_set(text)


def _jaccard(a: frozenset, b: frozenset) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    union = len(a | b)
    return inter / union if union else 0.0


def _doc_date(doc: SessionDoc) -> _dt.date:
    return _dt.date.fromtimestamp(doc.mtime)


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------


def _format_hit(hit: SearchHit, explain: bool, extract: str) -> str:
    lines: List[str] = []
    lines.append(f"{hit.path}")
    if hit.cluster_size > 1:
        lines.append(f"  cluster: {hit.cluster_size} sessions (canonical)")
        for d in hit.duplicates:
            lines.append(f"    ≈ {d}")
    lines.append(f"  score: {hit.score:.3f}")
    if explain and hit.explanation:
        e = hit.explanation
        lines.append(
            f"    density    {e['density']:.2f}"
            f"   recency {e['recency']:.2f}"
            f"   code {e['code']:.2f}"
            f"   resolution {e['resolution']:.2f}"
        )
    if hit.matches:
        lines.append("  matches:")
        for snip in hit.matches:
            lines.append(f"    > {snip}")
    if extract in ("code", "all") and hit.extraction:
        lines.append("  extraction:")
        for code_line in hit.extraction.splitlines():
            lines.append(f"    {code_line}")
    elif extract == "all" and hit.matches:
        pass  # matches already printed
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="excavate.py",
        description="Prompt Archaeology: excavate forgotten solutions from session logs.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # dig
    p_dig = sub.add_parser("dig", help="Search a directory of session files.")
    p_dig.add_argument("directory", help="Directory to search recursively.")
    p_dig.add_argument("--query", "-q", required=True, help="Search terms (AND'd within a file).")
    p_dig.add_argument("--top", "-n", type=int, default=5)
    p_dig.add_argument("--after", type=_date_arg, default=None, help="ISO date YYYY-MM-DD.")
    p_dig.add_argument("--before", type=_date_arg, default=None, help="ISO date YYYY-MM-DD.")
    p_dig.add_argument("--not", dest="exclude", action="append", default=[], help="Exclude files containing this term.")
    p_dig.add_argument("--explain", action="store_true")
    p_dig.add_argument("--extract", choices=["code", "all", "none"], default="none")
    p_dig.add_argument("--dedup", action="store_true")
    p_dig.add_argument("--dedup-threshold", type=float, default=DEDUP_THRESHOLD)
    p_dig.add_argument("--keep-variants", action="store_true")

    # index
    p_idx = sub.add_parser("index", help="Build a reusable index file.")
    p_idx.add_argument("directory")
    p_idx.add_argument("--out", "-o", required=True)
    p_idx.add_argument("--after", type=_date_arg, default=None)
    p_idx.add_argument("--before", type=_date_arg, default=None)

    # query
    p_q = sub.add_parser("query", help="Search an existing index file.")
    p_q.add_argument("index_file")
    p_q.add_argument("--query", "-q", required=True)
    p_q.add_argument("--top", "-n", type=int, default=5)
    p_q.add_argument("--not", dest="exclude", action="append", default=[])
    p_q.add_argument("--explain", action="store_true")
    p_q.add_argument("--extract", choices=["code", "all", "none"], default="none")
    p_q.add_argument("--dedup", action="store_true")
    p_q.add_argument("--dedup-threshold", type=float, default=DEDUP_THRESHOLD)
    p_q.add_argument("--keep-variants", action="store_true")

    return parser.parse_args(argv)


def _date_arg(s: str) -> _dt.date:
    try:
        return _dt.date.fromisoformat(s)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Bad date: {s} (use YYYY-MM-DD)")


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = _parse_args(argv if argv is not None else sys.argv[1:])

    if args.command == "dig":
        if not os.path.isdir(args.directory):
            print(f"error: not a directory: {args.directory}", file=sys.stderr)
            return 3
        idx = ArchaeologyIndex()
        n = idx.scan(args.directory)
        hits = idx.search(
            query=args.query,
            top=args.top,
            explain=args.explain,
            exclude=tuple(args.exclude),
            after=args.after,
            before=args.before,
        )
        if args.dedup:
            hits = idx.dedup_hits(hits, threshold=args.dedup_threshold)
        _print_results(hits, args, scanned=n)
        return 0

    if args.command == "index":
        if not os.path.isdir(args.directory):
            print(f"error: not a directory: {args.directory}", file=sys.stderr)
            return 3
        idx = ArchaeologyIndex()
        n = idx.scan(args.directory)
        # optional pre-filter by date (recorded at index time)
        if args.after or args.before:
            idx.docs = [
                d for d in idx.docs
                if (not args.after or _doc_date(d) >= args.after)
                and (not args.before or _doc_date(d) <= args.before)
            ]
        idx.save(args.out)
        print(f"indexed {len(idx.docs)} of {n} files -> {args.out}")
        return 0

    if args.command == "query":
        if not os.path.isfile(args.index_file):
            print(f"error: index not found: {args.index_file}", file=sys.stderr)
            return 3
        idx = ArchaeologyIndex.load(args.index_file)
        hits = idx.search(
            query=args.query,
            top=args.top,
            explain=args.explain,
            exclude=tuple(args.exclude),
        )
        if args.dedup:
            hits = idx.dedup_hits(hits, threshold=args.dedup_threshold)
        _print_results(hits, args, scanned=len(idx.docs))
        return 0

    return 2  # unreachable (subcommand required)


def _print_results(hits: List[SearchHit], args: argparse.Namespace, scanned: int) -> None:
    if not hits:
        print(f"no hits (scanned {scanned} files).")
        return
    print(f"=== top {len(hits)} of {scanned} files scanned ===")
    for hit in hits:
        print(_format_hit(hit, explain=args.explain, extract=args.extract))
        print()


if __name__ == "__main__":
    sys.exit(main())
