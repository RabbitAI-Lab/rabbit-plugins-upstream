#!/usr/bin/env python3
"""retrieval.py — local BM25 retrieval over your own corpus (v2.2.0).

The highest-leverage anti-hallucination move is putting facts in front of the
model instead of trusting its weights (RAG). This tool builds a stdlib-only
index (sqlite3 FTS5, BM25-ranked) from your JSON docs and queries it.
No network, no embeddings, no GPU.

  build --db IDX --docs DOCS.json [--reset]   # DOCS: [{id?, text, meta?}] or ["text", ...]
  query --db IDX --q "..." [--top 5]
  stats --db IDX

The index may contain your private corpus: the file is chmodded 0600 on build
and repaired to 0600 on every query.
"""
import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import clean_errors

_SCHEMA = (
    "CREATE TABLE IF NOT EXISTS docs(id TEXT PRIMARY KEY, text TEXT, meta TEXT);"
    "CREATE VIRTUAL TABLE IF NOT EXISTS fts USING fts5(id, text);"
)


def _perm(db):
    try:
        if os.stat(db).st_mode & 0o777 != 0o600:
            os.chmod(db, 0o600)
    except OSError:
        pass


def _has_index(con):
    n = con.execute(
        "SELECT COUNT(*) FROM sqlite_master WHERE type='table' AND name IN ('docs','fts')"
    ).fetchone()[0]
    return n == 2


def _build(a):
    try:
        with open(a.docs, encoding="utf-8") as f:
            docs = json.load(f)
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": f"cannot read docs JSON: {exc}"}))
        return 2
    if not isinstance(docs, list) or not docs:
        print(json.dumps({"error": "docs must be a non-empty JSON array"}))
        return 2
    rows = []
    for i, d in enumerate(docs):
        if isinstance(d, str):
            d = {"text": d}
        if not isinstance(d, dict) or not isinstance(d.get("text"), str) or not d["text"]:
            print(json.dumps({"error": f"doc {i} lacks a 'text' field"}))
            return 2
        did = str(d.get("id") or hashlib.sha1(d["text"].encode("utf-8")).hexdigest()[:8])
        rows.append((did, d["text"], json.dumps(d.get("meta")) if d.get("meta") is not None else None))
    seen = {}
    for r in rows:
        seen[r[0]] = r
    rows = list(seen.values())
    os.makedirs(os.path.dirname(a.db) or ".", exist_ok=True)
    fd = os.open(a.db, os.O_CREAT | os.O_RDWR, 0o600)  # 0600 from creation (no window)
    os.close(fd)
    con = sqlite3.connect(a.db)
    if a.reset:
        con.execute("DROP TABLE IF EXISTS docs")
        con.execute("DROP TABLE IF EXISTS fts")
    elif _has_index(con) and con.execute("SELECT COUNT(*) FROM docs").fetchone()[0]:
        print(json.dumps({"error": "index exists and is non-empty (use --reset to rebuild)"}))
        con.close()
        return 2
    con.executescript(_SCHEMA)
    con.execute("DELETE FROM fts")
    con.executemany("INSERT OR REPLACE INTO docs(id, text, meta) VALUES (?,?,?)", rows)
    con.executemany("INSERT INTO fts(id, text) VALUES (?,?)",
                    [(did, t) for did, t, _ in rows])
    con.commit()
    n = con.execute("SELECT COUNT(*) FROM docs").fetchone()[0]
    con.close()
    _perm(a.db)
    print(json.dumps({"built": True, "docs": n,
                      "bytes": os.path.getsize(a.db), "db": a.db}))
    return 0


def _match_expr(q):
    toks = re.findall(r"[^\W_]{2,}", q.lower())  # unicode word chars (non-English queries work)
    seen, uniq = set(), []
    for t in toks:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return " OR ".join(f'"{t}"' for t in uniq[:12])


def _query(a):
    if not os.path.exists(a.db):
        print(json.dumps({"error": f"no index at {a.db} (run build first)"}))
        return 2
    con = sqlite3.connect(a.db)
    if not _has_index(con):
        print(json.dumps({"error": "not a retrieval index (run build first)"}))
        con.close()
        return 2
    if a.top < 1:
        print(json.dumps({"error": "--top must be >= 1"}))
        con.close()
        return 2
    expr = _match_expr(a.q or "")
    if not expr:
        print(json.dumps({"error": "query has no searchable tokens"}))
        con.close()
        return 2
    try:
        cur = con.execute(
            "SELECT id, bm25(fts), snippet(fts, 1, '', '', ' ... ', 24) FROM fts "
            "WHERE fts MATCH ? ORDER BY rank LIMIT ?", (expr, a.top))
        hits = [{"id": i, "bm25": round(-float(b), 3), "snippet": s}  # negated: higher = more relevant
                for i, b, s in cur.fetchall()]
    except sqlite3.Error as exc:
        print(json.dumps({"error": f"query failed: {exc}"}))
        con.close()
        return 2
    con.close()
    _perm(a.db)
    print(json.dumps({"q": a.q, "match": expr, "hits": hits}, indent=2))
    return 0


def _stats(a):
    if not os.path.exists(a.db):
        print(json.dumps({"error": f"no index at {a.db}"}))
        return 2
    con = sqlite3.connect(a.db)
    n = con.execute("SELECT COUNT(*) FROM docs").fetchone()[0] if _has_index(con) else 0
    con.close()
    _perm(a.db)
    print(json.dumps({"docs": n, "bytes": os.path.getsize(a.db), "db": a.db}))
    return 0


@clean_errors
def main(argv=None):
    ap = argparse.ArgumentParser(prog="retrieval.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="index JSON docs into an FTS5/BM25 file")
    b.add_argument("--db", required=True)
    b.add_argument("--docs", required=True, help="JSON array [{id?, text, meta?}]")
    b.add_argument("--reset", action="store_true")
    b.set_defaults(func=_build)
    q = sub.add_parser("query", help="BM25-ranked search with snippets")
    q.add_argument("--db", required=True)
    q.add_argument("--q", required=True)
    q.add_argument("--top", type=int, default=5)
    q.set_defaults(func=_query)
    s = sub.add_parser("stats", help="index size stats")
    s.add_argument("--db", required=True)
    s.set_defaults(func=_stats)
    a = ap.parse_args(argv)
    return a.func(a)


if __name__ == "__main__":
    sys.exit(main())
