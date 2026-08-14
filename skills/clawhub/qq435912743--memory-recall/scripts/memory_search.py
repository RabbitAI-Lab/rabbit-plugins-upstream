#!/usr/bin/env python3
"""本地笔记/记忆检索：全文+时间加权，返回命中片段与来源。"""
import argparse, os, sys, time, math
from datetime import datetime


def iter_text_files(root):
    for dirpath, _, files in os.walk(root):
        for f in files:
            if f.lower().endswith((".md", ".txt", ".markdown")):
                yield os.path.join(dirpath, f)


def score_file(path, terms, use_or, after_ts, before_ts, half_life_days=30):
    try:
        mtime = os.path.getmtime(path)
    except OSError:
        mtime = 0
    # 时间加权：越近越高
    age_days = max(0, (time.time() - mtime) / 86400)
    recency = 0.5 ** (age_days / half_life_days)
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.read().splitlines()
    except Exception:
        return None
    low = [l.lower() for l in lines]
    hits = []
    matched = 0
    for i, l in enumerate(low):
        if any(t in l for t in terms):
            matched += 1
            ctx0 = max(0, i - 2)
            ctx1 = min(len(lines), i + 3)
            hits.append((i + 1, "\n".join(lines[ctx0:ctx1])))
    if not hits:
        return None
    ok = any(t in " ".join(low) for t in terms) if use_or else all(
        any(t in l for l in low) for t in terms)
    if not ok:
        return None
    # 关键词密度 + 时间
    kw = sum(l.count(t) for l in low for t in terms)
    score = (matched + kw) * (1 + recency)
    if after_ts and mtime < after_ts:
        return None
    if before_ts and mtime > before_ts:
        return None
    return {"path": path, "mtime": mtime, "hits": hits,
            "score": round(score, 3), "matched": matched}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--root", default=".")
    ap.add_argument("--tag", default=None, help="文件名含此字符串")
    ap.add_argument("--after", default=None, help="2026-07-01")
    ap.add_argument("--before", default=None)
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--ctx", type=int, default=2)
    ap.add_argument("--or", dest="use_or", action="store_true")
    args = ap.parse_args()
    terms = [t.lower() for t in args.query.split()]
    after_ts = datetime.strptime(args.after, "%Y-%m-%d").timestamp() if args.after else None
    before_ts = datetime.strptime(args.before, "%Y-%m-%d").timestamp() if args.before else None
    results = []
    for fp in iter_text_files(args.root):
        if args.tag and args.tag.lower() not in os.path.basename(fp).lower():
            continue
        r = score_file(fp, terms, args.use_or, after_ts, before_ts)
        if r:
            results.append(r)
    results.sort(key=lambda x: x["score"], reverse=True)
    if not results:
        print("⚠️ 无命中")
        sys.exit(0)
    for r in results[:args.top]:
        print(f"\n📄 {r['path']}  (score={r['score']}, 命中{r['matched']}行)")
        for ln, snippet in r["hits"][:5]:
            print(f"  L{ln}: {snippet[:160]}")


if __name__ == "__main__":
    main()
