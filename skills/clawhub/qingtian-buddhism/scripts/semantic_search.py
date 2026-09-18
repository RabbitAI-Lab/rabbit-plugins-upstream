#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
semantic_search.py — 青田·原始佛教修学助手 语义检索层（可选增强）

设计要点（与数据集 pali_index.faiss 严格对齐）：
  - 索引：pali_index.faiss（faiss.IndexScalarQuantizer，768 维，METRIC_INNER_PRODUCT，
    建库时已 L2 归一化 → IP 等价余弦相似度）。
  - 映射：chunks.jsonl.gz —— 每条 {id, rel, start, end, text}，id 即 FAISS 向量序号（0..101169），
    FAISS 返回的 top-k 序号直接定位原文片段。
  - 模型：BAAI/bge-base-zh（768 维，公开模型）。查询端用「同模型 + 同分词器 + 同归一化」，
    空间对齐，检索有效。模型由 sentence-transformers 首次调用时自动拉取并缓存。
  - 查询指令：bge 检索建议为中文查询加指令前缀「为这个句子生成表示以用于检索相关文章：」
    （对应数据集建库时的指令约定；可用 --no-instruct 关闭，对齐 search.py 行为）。

用法：
  python scripts/semantic_search.py "四圣谛"                 # 默认加指令
  python scripts/semantic_search.py "nibbāna" --no-instruct  # 不加指令
  python scripts/semantic_search.py "哪些经讲缘起" --topk 8

作为模块调用：
  from semantic_search import search
  hits = search("四圣谛", topk=5)   # -> [{"id","rel","start","end","text","score"}, ...]

环境变量：
  INDEX_DIR  语义索引目录（默认 <skill>/data/index）；本地测试可指向已下载目录
  BGE_MODEL  嵌入模型名/路径（默认 BAAI/bge-base-zh）
"""

import os
import sys
import json
import gzip
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, ".."))
INDEX_DIR = os.environ.get(
    "INDEX_DIR", os.path.join(SKILL_ROOT, "data", "index")
)
FAISS_FILE = os.path.join(INDEX_DIR, "pali_index.faiss")
CHUNKS_FILE = os.path.join(INDEX_DIR, "chunks.jsonl.gz")
# 默认：优先使用本技能预缓存的本地模型（离线可用），否则回退 HF 自动下载
_LOCAL_BGE = os.path.join(SKILL_ROOT, "data", "models", "bge-base-zh")
MODEL_NAME = os.environ.get(
    "BGE_MODEL", _LOCAL_BGE if os.path.isdir(_LOCAL_BGE) else "BAAI/bge-base-zh"
)

# bge 中文检索指令前缀（与数据集建库约定一致）
BGE_QUERY_INSTRUCTION_ZH = "为这个句子生成表示以用于检索相关文章："

# ---- 模块级缓存 ----
_index = None
_chunks = None
_model = None


def _load_index():
    global _index
    if _index is not None:
        return _index
    if not os.path.exists(FAISS_FILE):
        raise FileNotFoundError(
            f"未找到语义索引 {FAISS_FILE}\n"
            f"请先运行：python scripts/setup_corpus.py\n"
            f"（或设置环境变量 INDEX_DIR 指向含 pali_index.faiss 的目录）"
        )
    import faiss

    _index = faiss.read_index(FAISS_FILE)
    return _index


def _load_chunks():
    global _chunks
    if _chunks is not None:
        return _chunks
    if not os.path.exists(CHUNKS_FILE):
        raise FileNotFoundError(
            f"未找到映射文件 {CHUNKS_FILE}\n"
            f"请先运行：python scripts/setup_corpus.py"
        )
    # 顺序流式读取，按出现顺序存入列表（id 即列表下标；同时容错非连续 id）。
    recs = []
    with gzip.open(CHUNKS_FILE, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            recs.append(json.loads(line))
    # id 连续 0..N-1 时直接按下标；否则建 dict 兜底
    if recs and all(rec.get("id") == i for i, rec in enumerate(recs)):
        _chunks = recs
    else:
        _chunks = {rec["id"]: rec for rec in recs}
    return _chunks


def _load_model():
    global _model
    if _model is not None:
        return _model
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        raise RuntimeError(
            "未安装 sentence-transformers。请先：pip install sentence-transformers faiss-cpu"
        )
    _model = SentenceTransformer(MODEL_NAME)
    return _model


def embed_query(query, instruct=True):
    """编码查询：可选加 bge 中文指令前缀；L2 归一化（与索引对齐）。返回 (1,768) float32。"""
    model = _load_model()
    text = (BGE_QUERY_INSTRUCTION_ZH + query) if instruct else query
    emb = model.encode(
        [text],
        normalize_embeddings=True,   # L2 归一化 → 与索引一致，IP=余弦
        convert_to_numpy=True,
    )
    return emb.astype("float32")


def search(query, topk=5, instruct=True):
    """语义检索：返回 top-k 命中列表，每项为 dict。"""
    idx = _load_index()
    chunks = _chunks if _chunks is not None else _load_chunks()
    q = embed_query(query, instruct=instruct)
    D, I = idx.search(q, topk)
    hits = []
    for score, cid in zip(D[0], I[0]):
        if cid < 0:
            continue
        rec = chunks[cid] if isinstance(chunks, list) else chunks.get(cid)
        if rec is None:
            continue
        hits.append({
            "id": int(cid),
            "rel": rec.get("rel", ""),
            "start": rec.get("start"),
            "end": rec.get("end"),
            "text": rec.get("text", ""),
            "score": round(float(score), 4),
        })
    return hits


def _cli():
    ap = argparse.ArgumentParser(description="巴利三藏语义检索（bge-base-zh + FAISS）")
    ap.add_argument("query", help="自然语言查询 / 关键词")
    ap.add_argument("--topk", type=int, default=5, help="返回条数（默认 5）")
    ap.add_argument("--no-instruct", action="store_true", help="不加 bge 中文指令前缀")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出（便于程序调用）")
    args = ap.parse_args()

    try:
        hits = search(args.query, topk=args.topk, instruct=not args.no_instruct)
    except (FileNotFoundError, RuntimeError) as e:
        print(f"[semantic_search] {e}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
        return 0

    print(f"查询：「{args.query}」  指令前缀：{'开' if not args.no_instruct else '关'}\n")
    for i, h in enumerate(hits, 1):
        head = h["text"].replace("\n", " ").strip()
        if len(head) > 160:
            head = head[:160] + "…"
        print(f"[{i}] 分 {h['score']:.4f}  id={h['id']}  {h['rel']} ({h['start']}-{h['end']})")
        print(f"    {head}\n")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
