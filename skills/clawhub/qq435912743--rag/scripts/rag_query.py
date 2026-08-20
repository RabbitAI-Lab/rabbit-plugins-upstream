#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rag_query —— 检索 top-k 相关分块（带出处与引用片段）。

用法：
  python rag_query.py --index <index.json> --question "..." [--topk 5] [--out res.json]
"""
import os, sys, json, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from raglib import tokenize, tfidf_vector, cosine


def load_index(path):
    d = json.load(open(path, encoding="utf-8"))
    chunks = d["chunks"]
    vecs = d.get("vectors", [])
    for c, v in zip(chunks, vecs):
        c["vec"] = v
    return d, chunks


def snippet(text, span=120):
    t = text.strip().replace("\n", " ")
    return t[:span] + ("…" if len(t) > span else "")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", required=True)
    ap.add_argument("--question", required=True)
    ap.add_argument("--topk", type=int, default=5)
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    d, chunks = load_index(args.index)
    idf = d["idf"]
    qvec = tfidf_vector(tokenize(args.question), idf)
    scored = []
    for c in chunks:
        s = cosine(qvec, c.get("vec", {}))
        if s > 0:
            scored.append((s, c))
    scored.sort(key=lambda x: x[0], reverse=True)
    top = scored[: args.topk]

    results = []
    for rank, (score, c) in enumerate(top, 1):
        results.append({
            "rank": rank,
            "doc": c["doc"],
            "score": round(score, 4),
            "chunk_id": c["id"],
            "snippet": snippet(c["text"]),
            "text": c["text"],
        })
    out = {"question": args.question, "topk": args.topk, "hits": len(results), "results": results}
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
        print(f"✅ 检索到 {len(results)} 条，写入 {args.out}")
    else:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    for r in results:
        print(f"[{r['rank']}] {r['doc']}  score={r['score']}  {r['snippet']}")


if __name__ == "__main__":
    main()
