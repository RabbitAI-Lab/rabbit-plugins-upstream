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
    （对应数据集建库时的指令约定；可用 --no-instruct 关闭）。

⚠️ 偏移口径（重要，v1.5.4 修复）：
  chunks.jsonl.gz 的 start/end 是「LF 归一化文本（\\r\\n→\\n）」的字符偏移，而 data/corpus/
  下的 txt 文件是 CRLF 行尾。因此【不要】直接按 start/end 对原文件字节/字符切片——会错位。
  请使用本模块的 resolve_context()（或 CLI --context）读取上下文：内部会自动做 CRLF→LF
  归一化后再按字符偏移切片。

用法：
  python scripts/semantic_search.py "四圣谛"                  # 默认加指令
  python scripts/semantic_search.py "nibbāna" --no-instruct   # 不加指令
  python scripts/semantic_search.py "哪些经讲缘起" --topk 8
  python scripts/semantic_search.py "四圣谛" --context 800    # 附带每个命中的上下文窗口

作为模块调用：
  from semantic_search import search, resolve_context, get_chunk
  hits = search("四圣谛", topk=5)      # -> [{"id","rel","start","end","text","score"}, ...]
  ctx  = resolve_context(hits[0]["rel"], hits[0]["start"], hits[0]["end"], width=800)

环境变量：
  INDEX_DIR  语义索引目录（默认 <skill>/data/index）；本地测试可指向已下载目录
  BGE_MODEL  嵌入模型名/路径（默认 BAAI/bge-base-zh）
  CANON_TOP  语料顶层目录名（默认「巴利三藏巴利-中文对照译本（2026-06-21） txt」）
"""

import os
import sys
import json
import gzip
import struct
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, ".."))
INDEX_DIR = os.environ.get(
    "INDEX_DIR", os.path.join(SKILL_ROOT, "data", "index")
)
FAISS_FILE = os.path.join(INDEX_DIR, "pali_index.faiss")
CHUNKS_FILE = os.path.join(INDEX_DIR, "chunks.jsonl.gz")
CHUNKS_OFFSETS_FILE = os.path.join(INDEX_DIR, "chunks.offsets")
MODEL_NAME = os.environ.get("BGE_MODEL", "BAAI/bge-base-zh")

# 语料顶层目录（chunks 的 rel 路径相对于此目录）
CANON_TOP = os.environ.get(
    "CANON_TOP", "巴利三藏巴利-中文对照译本（2026-06-21） txt"
)
CANON_DIR = os.path.join(SKILL_ROOT, "data", "corpus", CANON_TOP)

# bge 中文检索指令前缀（与数据集建库约定一致）
BGE_QUERY_INSTRUCTION_ZH = "为这个句子生成表示以用于检索相关文章："

# ---- 模块级缓存 ----
_index = None
_model = None
_offsets = None          # list[int]：每条 chunk 在 gzip 未压缩流中的起始字节偏移
_offsets_checked = False
_chunk_cache = {}        # 最近读取的 chunk 行缓存（有界）
_CHUNK_CACHE_MAX = 512


def _load_index():
    """加载 FAISS 索引；faiss 缺失时给出友好提示（v1.5.4 修复 R1-D6）。"""
    global _index
    if _index is not None:
        return _index
    if not os.path.exists(FAISS_FILE):
        raise FileNotFoundError(
            f"未找到语义索引 {FAISS_FILE}\n"
            f"请先运行：python scripts/setup_corpus.py\n"
            f"（或设置环境变量 INDEX_DIR 指向含 pali_index.faiss 的目录）"
        )
    try:
        import faiss
    except ImportError:
        raise RuntimeError(
            "未安装 faiss-cpu，无法进行向量检索。请先安装：\n"
            "  pip install faiss-cpu\n"
            "（若只想用关键词/混合检索，可运行 scripts/hybrid_search.py --bm25-only，"
            " 不需要 faiss；Grep 检索也不受影响。）"
        )
    _index = faiss.read_index(FAISS_FILE)
    return _index


def _load_offsets():
    """构建/复用 chunks.offsets（gzip 未压缩流逐行起始偏移），支持随机访问。"""
    global _offsets, _offsets_checked
    if _offsets is not None:
        return _offsets
    if not os.path.exists(CHUNKS_FILE):
        raise FileNotFoundError(
            f"未找到映射文件 {CHUNKS_FILE}\n"
            f"请先运行：python scripts/setup_corpus.py"
        )
    # 偏移文件缺失或比 chunks 旧 → 重建
    need_build = True
    if os.path.exists(CHUNKS_OFFSETS_FILE):
        try:
            if os.path.getmtime(CHUNKS_OFFSETS_FILE) >= os.path.getmtime(CHUNKS_FILE):
                with open(CHUNKS_OFFSETS_FILE, "rb") as f:
                    (n,) = struct.unpack("<Q", f.read(8))
                    offs = list(struct.unpack(f"<{n}Q", f.read(8 * n)))
                # 简单校验：条数与首条偏移 0 一致
                if n > 0 and offs and offs[0] == 0:
                    _offsets = offs
                    need_build = False
        except Exception:
            need_build = True
    if need_build:
        offs = []
        with gzip.open(CHUNKS_FILE, "rb") as f:
            pos = 0
            for line in f:
                offs.append(pos)
                pos += len(line)
        if not offs:
            raise RuntimeError(f"{CHUNKS_FILE} 为空，请重新运行 setup_corpus.py")
        _offsets = offs
        try:
            with open(CHUNKS_OFFSETS_FILE, "wb") as f:
                f.write(struct.pack("<Q", len(offs)))
                f.write(struct.pack(f"<{len(offs)}Q", *offs))
        except OSError as e:
            sys.stderr.write(f"[semantic_search] 提示：写入 {CHUNKS_OFFSETS_FILE} 失败（{e}），"
                             f"本次仍可检索，下次将重建。\n")
    _offsets_checked = True
    return _offsets


def get_chunk(cid):
    """按 id 读取单条 chunk（随机访问 + 有界缓存，避免全量载入内存）。"""
    offs = _load_offsets()
    if cid < 0 or cid >= len(offs):
        return None
    if cid in _chunk_cache:
        return _chunk_cache[cid]
    with gzip.open(CHUNKS_FILE, "rb") as f:
        f.seek(offs[cid])
        line = f.readline()
    try:
        rec = json.loads(line)
    except json.JSONDecodeError:
        return None
    if len(_chunk_cache) >= _CHUNK_CACHE_MAX:
        _chunk_cache.clear()
    _chunk_cache[cid] = rec
    return rec


def iter_chunks(ids):
    """按 id 顺序批量读取（id 列表会先排序以利用流式读取；小批量用 get_chunk 更快）。"""
    if len(ids) <= 16:
        return [get_chunk(c) for c in ids]
    offs = _load_offsets()
    wanted = {c for c in ids if 0 <= c < len(offs)}
    out = {}
    with gzip.open(CHUNKS_FILE, "rb") as f:
        for i, line in enumerate(f):
            if i not in wanted:
                continue
            try:
                out[i] = json.loads(line)
            except json.JSONDecodeError:
                out[i] = None
            wanted.discard(i)
            if not wanted:
                break
    # 写回缓存
    for k, v in out.items():
        if len(_chunk_cache) >= _CHUNK_CACHE_MAX:
            _chunk_cache.clear()
        _chunk_cache[k] = v
    return [out.get(c) for c in ids]


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


def resolve_context(rel, start, end, width=600):
    """按 rel + start/end 读取原文上下文（CRLF→LF 归一化后再按字符偏移切片）。

    返回 rel 指向文件中 [start-width, end+width] 的文本；文件缺失或偏移越界返回 None。
    """
    path = os.path.join(CANON_DIR, *rel.split(os.sep))
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read().replace("\r\n", "\n")
    s = max(0, int(start) - width)
    e = min(len(text), int(end) + width)
    if s > e or s >= len(text):
        return None
    return text[s:e]


def vector_search(query, topk=5, instruct=True):
    """向量检索：返回 top-k 命中列表，每项为 dict（含 id/rel/start/end/text/score）。"""
    idx = _load_index()
    q = embed_query(query, instruct=instruct)
    D, I = idx.search(q, topk)
    hits = []
    for score, cid in zip(D[0], I[0]):
        if cid < 0:
            continue
        rec = get_chunk(int(cid))
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


def search(query, topk=5, instruct=True):
    """语义检索（与 vector_search 等价，保留旧接口兼容）。"""
    return vector_search(query, topk=topk, instruct=instruct)


def _print_context(rel, start, end, width):
    ctx = resolve_context(rel, start, end, width)
    if ctx is None:
        print(f"      [上下文]（无法读取 {rel}，跳过）")
        return
    head = ctx.replace("\n", " ").strip()
    if len(head) > 240:
        head = head[:240] + "…"
    print(f"      [上下文 ±{width}] {head}")


def _cli():
    ap = argparse.ArgumentParser(description="巴利三藏语义检索（bge-base-zh + FAISS）")
    ap.add_argument("query", help="自然语言查询 / 关键词")
    ap.add_argument("--topk", type=int, default=5, help="返回条数（默认 5）")
    ap.add_argument("--no-instruct", action="store_true", help="不加 bge 中文指令前缀")
    ap.add_argument("--json", action="store_true", help="以 JSON 输出（便于程序调用）")
    ap.add_argument("--context", type=int, default=0, metavar="N",
                    help="附带每个命中左右各 N 字符的原文上下文（自动 CRLF→LF 后按偏移切片）")
    args = ap.parse_args()

    try:
        hits = vector_search(args.query, topk=args.topk, instruct=not args.no_instruct)
    except (FileNotFoundError, RuntimeError) as e:
        print(f"[semantic_search] {e}", file=sys.stderr)
        return 2

    if args.json:
        if args.context > 0:
            for h in hits:
                h["context"] = resolve_context(h["rel"], h["start"], h["end"], args.context)
        print(json.dumps(hits, ensure_ascii=False, indent=2))
        return 0

    print(f"查询：「{args.query}」  指令前缀：{'开' if not args.no_instruct else '关'}\n")
    for i, h in enumerate(hits, 1):
        head = h["text"].replace("\n", " ").strip()
        if len(head) > 160:
            head = head[:160] + "…"
        print(f"[{i}] 分 {h['score']:.4f}  id={h['id']}  {h['rel']} ({h['start']}-{h['end']})")
        print(f"    {head}")
        if args.context > 0:
            _print_context(h["rel"], h["start"], h["end"], args.context)
        print()
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
