#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hybrid_search.py — 青田·原始佛教修学助手 混合检索（BM25 关键词 + FAISS 向量，RRF 融合）

设计要点（借鉴 tripitaka-mcp 的 search_hybrid 思路：keyword + semantic 经 Reciprocal
Rank Fusion 融合）：
  - BM25：对 chunks.jsonl.gz 的 text 字段做纯 Python 实现（零第三方依赖），
    巴利/拉丁词按整词、中文按单字分词，适合「巴利-中文对照」语料的混排；
    倒排索引用紧凑 array 存储并 pickle+gzip 缓存到 data/index/bm25.idx，
    避免每次进程重建（首次构建约 5–15 秒、峰值内存数百 MB）。
  - 向量：复用 semantic_search（bge-base-zh + FAISS，已 L2 归一化）。
  - RRF：score = Σ 1/(k + rank)，k=60；两种排序融合后输出，弱化单一检索的偏差。

何时用：自然语言模糊问（「哪些经讲缘起」「什么是苦的止息」）且 Grep 不易直接命中时，
推荐用本脚本替代纯语义检索；精确关键词/经号仍走 Grep。

用法：
  python scripts/hybrid_search.py "哪些经讲缘起"            # 默认 BM25+向量融合
  python scripts/hybrid_search.py "appamāda" --bm25-only   # 仅关键词（不需要 faiss/模型）
  python scripts/hybrid_search.py "慈心禅" --topk 8 --context 600
  python scripts/hybrid_search.py "缘起" --json

降级：faiss 或 bge 模型缺失时自动退化为 BM25-only 并提示（Grep 不受影响）。
环境变量同 semantic_search：INDEX_DIR / BGE_MODEL / CANON_TOP。
"""

import os
import re
import sys
import json
import math
import gzip
import pickle
import array
import argparse

from semantic_search import get_chunk, resolve_context, CHUNKS_FILE

# ---- 分词（巴利/拉丁整词 + 中文单字） ----
_LATIN_RE = re.compile(r"[A-Za-z\u00C0-\u024F\u1E00-\u1EFF]+|\d+")
_CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def tokenize(text):
    tokens = []
    for m in _LATIN_RE.finditer(text):
        tokens.append(m.group(0).lower())
    for ch in _CJK_RE.findall(text):
        tokens.append(ch)
    return tokens


class BM25:
    """Okapi BM25（k1=1.5, b=0.75）。倒排：term -> array('I') [doc_id, tf, doc_id, tf, ...]。"""

    def __init__(self, texts, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.n_docs = len(texts)
        self.doc_len = array.array("I", (len(tokenize(t)) for t in texts))
        self.avgdl = sum(self.doc_len) / max(1, self.n_docs)
        postings = {}
        for i, text in enumerate(texts):
            seen = {}
            for t in tokenize(text):
                seen[t] = seen.get(t, 0) + 1
            for t, c in seen.items():
                postings.setdefault(t, array.array("I")).extend((i, c))
        self.postings = postings
        self.idf = {}
        for t, arr in postings.items():
            df = len(arr) // 2
            self.idf[t] = math.log(1 + (self.n_docs - df + 0.5) / (df + 0.5))

    def search(self, query, topk=10):
        qtoks = set(tokenize(query))
        if not qtoks:
            return []
        scores = {}
        for t in qtoks:
            arr = self.postings.get(t)
            if not arr:
                continue
            idf = self.idf[t]
            n = len(arr) // 2
            for j in range(n):
                did = arr[j * 2]
                tf = arr[j * 2 + 1]
                dl = self.doc_len[did]
                denom = tf + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                if denom <= 0:
                    continue
                scores[did] = scores.get(did, 0.0) + idf * tf * (self.k1 + 1) / denom
        return sorted(scores.items(), key=lambda x: -x[1])[:topk]


# ---- BM25 缓存（进程级 + 磁盘级） ----
_BM25 = None
_BM25_STATE = {"n_docs": None}


def _bm25_cache_path():
    return os.path.join(os.path.dirname(CHUNKS_FILE), "bm25.idx")


def build_bm25(use_cache=True):
    """构建/复用 BM25 索引。优先加载 data/index/bm25.idx，其次现场构建并写缓存。"""
    global _BM25
    if _BM25 is not None:
        return _BM25
    if not os.path.exists(CHUNKS_FILE):
        raise FileNotFoundError(
            f"未找到映射文件 {CHUNKS_FILE}\n请先运行：python scripts/setup_corpus.py"
        )
    cache_path = _bm25_cache_path()
    if use_cache and os.path.exists(cache_path):
        try:
            if os.path.getmtime(cache_path) >= os.path.getmtime(CHUNKS_FILE):
                with gzip.open(cache_path, "rb") as f:
                    _BM25 = pickle.load(f)
                sys.stderr.write(f"[hybrid_search] 载入 BM25 缓存：{cache_path}\n")
                return _BM25
        except Exception as e:
            sys.stderr.write(f"[hybrid_search] BM25 缓存加载失败，重建（{e}）\n")

    sys.stderr.write("[hybrid_search] 构建 BM25 索引（约 5–15 秒，一次性）...\n")
    texts = []
    with gzip.open(CHUNKS_FILE, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            texts.append(json.loads(line).get("text", ""))
    _BM25 = BM25(texts)
    if use_cache:
        try:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            tmp = cache_path + ".tmp"
            with gzip.open(tmp, "wb") as f:
                pickle.dump(_BM25, f, protocol=4)
            os.replace(tmp, cache_path)
            sys.stderr.write(f"[hybrid_search] BM25 缓存已写入：{cache_path}\n")
        except Exception as e:
            sys.stderr.write(f"[hybrid_search] BM25 缓存写入失败（不影响本次检索）：{e}\n")
    return _BM25


def rrf_fuse(rankings, k=60):
    """Reciprocal Rank Fusion：rankings 为 [(doc_id, score), ...] 列表的列表。"""
    fused = {}
    for ranking in rankings:
        for rank, (doc_id, _score) in enumerate(ranking):
            fused[doc_id] = fused.get(doc_id, 0.0) + 1.0 / (k + rank + 1)
    return sorted(fused.items(), key=lambda x: -x[1])


def hybrid_search(query, topk=5, instruct=True, use_vector=True, bm25_top=200):
    """混合检索：返回 ({hits}, use_vector)；hits 每项含 id/rel/start/end/text/各分。"""
    bm = build_bm25()
    kw_rank = bm.search(query, topk=bm25_top)
    kw_map = {doc_id: score for doc_id, score in kw_rank}

    rankings = [kw_rank]
    vec_rank = []
    vec_map = {}
    if use_vector:
        try:
            from semantic_search import vector_search
            vhits = vector_search(query, topk=bm25_top, instruct=instruct)
            vec_rank = [(h["id"], h["score"]) for h in vhits]
            vec_map = dict(vec_rank)
            rankings.append(vec_rank)
        except (FileNotFoundError, RuntimeError) as e:
            sys.stderr.write(f"[hybrid_search] 向量检索不可用，降级为关键词：{e}\n")
            use_vector = False

    fused = rrf_fuse(rankings)
    results = []
    for doc_id, rrf_score in fused[:topk]:
        rec = get_chunk(int(doc_id))
        if rec is None:
            continue
        results.append({
            "id": int(doc_id),
            "rel": rec.get("rel", ""),
            "start": rec.get("start"),
            "end": rec.get("end"),
            "text": rec.get("text", ""),
            "score": round(rrf_score, 4),
            "keyword_score": round(kw_map.get(int(doc_id), 0.0), 4),
            "vector_score": round(vec_map.get(int(doc_id), 0.0), 4) if use_vector else None,
        })
    return results, use_vector


def _cli():
    ap = argparse.ArgumentParser(description="巴利三藏混合检索（BM25 + FAISS，RRF 融合）")
    ap.add_argument("query", help="自然语言查询 / 关键词")
    ap.add_argument("--topk", type=int, default=5, help="返回条数（默认 5）")
    ap.add_argument("--no-instruct", action="store_true", help="向量侧不加 bge 中文指令前缀")
    ap.add_argument("--bm25-only", action="store_true", help="仅关键词 BM25（无需 faiss/模型）")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出")
    ap.add_argument("--context", type=int, default=0, metavar="N",
                    help="附带每个命中左右各 N 字符的原文上下文")
    ap.add_argument("--bm25-top", type=int, default=200, help="融合前 BM25 候选数（默认 200）")
    ap.add_argument("--no-cache", action="store_true", help="不读写 BM25 磁盘缓存")
    args = ap.parse_args()

    try:
        results, use_vector = hybrid_search(
            args.query, topk=args.topk, instruct=not args.no_instruct,
            use_vector=not args.bm25_only, bm25_top=args.bm25_top,
        )
    except FileNotFoundError as e:
        print(f"[hybrid_search] {e}", file=sys.stderr)
        return 2

    if args.json:
        if args.context > 0:
            for h in results:
                h["context"] = resolve_context(h["rel"], h["start"], h["end"], args.context)
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0

    mode = "BM25+向量(RRF)" if use_vector else "BM25-only（向量不可用）"
    print(f"查询：「{args.query}」  模式：{mode}\n")
    for i, h in enumerate(results, 1):
        head = h["text"].replace("\n", " ").strip()
        if len(head) > 160:
            head = head[:160] + "…"
        vs = f"  向量 {h['vector_score']}" if h.get("vector_score") is not None else ""
        print(f"[{i}] RRF {h['score']:.4f}  关键词 {h['keyword_score']:.4f}{vs}  id={h['id']}")
        print(f"    {h['rel']} ({h['start']}-{h['end']})")
        print(f"    {head}")
        if args.context > 0:
            ctx = resolve_context(h["rel"], h["start"], h["end"], args.context)
            if ctx:
                c = ctx.replace("\n", " ").strip()
                if len(c) > 240:
                    c = c[:240] + "…"
                print(f"    [上下文 ±{args.context}] {c}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
