#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_index.py — 青田·原始佛教修学助手 本地重建语义索引（段落感知分块 + bge 嵌入 + FAISS）

背景（R2 改进，借鉴 SuttaCentral 的 segment 组织理念）：
  官方索引 chunks.jsonl.gz 是「固定 1500 字符窗口」分块，会切开巴利行/中文行的配对与
  句子边界。本脚本改为「段落感知分块」：按空行/标题切段落、相邻段落合并到上限，
  **绝不在段落中间切开**，从而保证「巴利行 + 中文行」对（译本中相邻行）始终在同一 chunk。

输出格式与官方完全一致（可被 semantic_search / hybrid_search / resolve_context 直接使用）：
  - chunks.jsonl.gz：{id, rel, start, end, text}，start/end 为 **LF 归一化文本**的字符偏移
  - pali_index.faiss：bge-base-zh 嵌入 + L2 归一化 + IP（= 余弦）；默认 SQ8 量化（与官方同规格，
    101170×768 ≈ 74MB），可选 --index flat（全精度，约 311MB）

用法：
  # 只重建文本分块（不写 faiss；无需模型）：
  python scripts/build_index.py --dry-run --out-dir <临时目录>
  # 完整重建（需先 pip install sentence-transformers faiss-cpu，首次拉取 bge-base-zh）：
  python scripts/build_index.py --yes
  # 自定义分块大小：
  python scripts/build_index.py --dry-run --max-chars 1200 --out-dir <临时目录>

注意：
  - 覆盖官方索引属有风险操作：默认 out-dir 为 data/index 且已有 index.ready 时需 --yes 确认。
  - 重建后建议运行 scripts/health_check.py 复核；chunks.offsets / bm25.idx 会自动重建。
  - 嵌入耗时与文本量成正比（本语料约 220MB，CPU 上可能数十分钟）。
环境变量同 semantic_search：CANON_TOP / BGE_MODEL / INDEX_DIR。
"""

import os
import re
import sys
import json
import gzip
import random
import argparse

import semantic_search
from semantic_search import CANON_DIR, CANON_TOP, INDEX_DIR

_TEXT_EXT = ".txt"
_WS_SPLIT = re.compile(r"\n\s*\n")


def iter_txt_files(root):
    """返回 (rel, abs_path)，rel 相对 CANON_DIR，分隔符与官方索引一致（os.sep）。"""
    for dp, _dn, fn in sorted(os.walk(root)):
        for f in sorted(fn):
            if not f.lower().endswith(_TEXT_EXT):
                continue
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, CANON_DIR)
            yield rel, full


def chunk_text(text, max_chars):
    """段落感知分块：按空行切段，相邻段合并至上限；返回 [(chunk_text, start, end)]。

    start/end 为 LF 归一化文本的字符偏移，且保证 text[start:end] == chunk_text。
    """
    paras = []
    cursor = 0
    for para in _WS_SPLIT.split(text):
        idx = text.find(para, cursor)
        if idx < 0:
            idx = cursor
        paras.append((idx, idx + len(para)))
        cursor = idx + len(para)
    chunks = []
    s0 = e0 = None
    for s, e in paras:
        if text[s:e].strip() == "":
            continue
        if s0 is None:
            s0, e0 = s, e
        elif (e - s0) <= max_chars:
            e0 = e
        else:
            chunks.append((s0, e0))
            s0, e0 = s, e
    if s0 is not None:
        chunks.append((s0, e0))
    return [(text[s:e], s, e) for s, e in chunks]


def build_chunks(out_dir, max_chars, quiet=False):
    """扫描全部语料，生成段落感知分块并写 chunks.jsonl.gz。返回 chunk 数。"""
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "chunks.jsonl.gz")
    n_files = 0
    n_chunks = 0
    total_chars = 0
    with gzip.open(out_path, "wt", encoding="utf-8") as out:
        for rel, full in iter_txt_files(CANON_DIR):
            with open(full, encoding="utf-8", errors="replace") as f:
                text = f.read().replace("\r\n", "\n")
            for chunk, s, e in chunk_text(text, max_chars):
                rec = {
                    "id": n_chunks,
                    "rel": rel,
                    "start": s,
                    "end": e,
                    "text": chunk,
                }
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")
                n_chunks += 1
                total_chars += len(chunk)
            n_files += 1
            if not quiet and n_files % 40 == 0:
                sys.stderr.write(f"[build_index] 已处理 {n_files} 文件，{n_chunks} chunk\n")
    sys.stderr.write(f"[build_index] 完成：{n_files} 文件 → {n_chunks} chunk"
                     f"（avg {total_chars // max(1, n_chunks)} 字符）→ {out_path}\n")
    return n_chunks


def verify_chunks(out_dir, sample_n=20):
    """自检：抽样 chunk 的 rel 可解析、LF 偏移切片与 text 一致。"""
    path = os.path.join(out_dir, "chunks.jsonl.gz")
    with gzip.open(path, "rt", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        raise RuntimeError("chunks.jsonl.gz 为空")
    rng = random.Random(20260909)
    sample = rng.sample(range(len(lines)), min(sample_n, len(lines)))
    for cid in sample:
        rec = json.loads(lines[cid])
        full = os.path.join(CANON_DIR, *rec["rel"].split(os.sep))
        if not os.path.exists(full):
            raise RuntimeError(f"rel 无法解析：{rec['rel']}")
        with open(full, encoding="utf-8", errors="replace") as f:
            lf = f.read().replace("\r\n", "\n")
        s, e = rec["start"], rec["end"]
        if s > e or e > len(lf) or lf[s:e] != rec["text"]:
            raise RuntimeError(f"偏移切片不符：id={cid} {rec['rel']} {s}-{e}")
    sys.stderr.write(f"[build_index] 自检通过：抽样 {len(sample)} 条 rel 与偏移全部吻合\n")


def build_faiss(chunks_path, out_path, index_type="sq", model_name=None, quiet=False):
    """嵌入全部 chunk 文本并写 FAISS 索引（需要 sentence-transformers + faiss）。"""
    import numpy as np
    try:
        from sentence_transformers import SentenceTransformer
    except ImportError:
        raise RuntimeError(
            "未安装 sentence-transformers。请先：pip install sentence-transformers faiss-cpu"
        )
    try:
        import faiss
    except ImportError:
        raise RuntimeError("未安装 faiss-cpu。请先：pip install faiss-cpu")

    texts = []
    with gzip.open(chunks_path, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                texts.append(json.loads(line)["text"])
    if not quiet:
        sys.stderr.write(f"[build_index] 开始嵌入 {len(texts)} 段（模型 {model_name}，"
                         f"CPU 上可能较慢）...\n")
    model = SentenceTransformer(model_name)
    embs = model.encode(
        texts,
        normalize_embeddings=True,
        convert_to_numpy=True,
        batch_size=64,
        show_progress_bar=not quiet,
    ).astype("float32")
    if index_type == "sq":
        idx = faiss.IndexScalarQuantizer(embs.shape[1], faiss.METRIC_INNER_PRODUCT)
    else:
        idx = faiss.IndexFlatIP(embs.shape[1])
    idx.add(embs)
    faiss.write_index(idx, out_path)
    sys.stderr.write(f"[build_index] FAISS 索引已写入：{out_path}"
                     f"（{embs.shape[0]}×{embs.shape[1]}，{index_type}）\n")


def _cli():
    ap = argparse.ArgumentParser(description="本地重建语义索引（段落感知分块）")
    ap.add_argument("--out-dir", default=INDEX_DIR, help="输出目录（默认 data/index）")
    ap.add_argument("--max-chars", type=int, default=1500, help="chunk 字符上限（默认 1500）")
    ap.add_argument("--dry-run", action="store_true",
                    help="只重建文本分块，不写 FAISS（无需模型）")
    ap.add_argument("--index", choices=["sq", "flat"], default="sq",
                    help="FAISS 索引类型：sq=SQ8 量化(官方同规格,约74MB)，flat=全精度(约311MB)")
    ap.add_argument("--model", default=None, help=f"嵌入模型（默认 bge-base-zh）")
    ap.add_argument("--yes", action="store_true",
                    help="确认覆盖 data/index 下的官方索引（有 index.ready 时必需）")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    if not os.path.isdir(CANON_DIR):
        print(f"[build_index] 未找到语料目录 {CANON_DIR}，请先运行 setup_corpus.py",
              file=sys.stderr)
        return 2

    # 覆盖确认
    index_ready = os.path.exists(os.path.join(INDEX_DIR, "index.ready"))
    overwriting_official = (
        os.path.normpath(args.out_dir) == os.path.normpath(INDEX_DIR) and index_ready
    )
    if overwriting_official and not args.yes:
        print(
            "[build_index] 警告：输出目录是官方索引所在 data/index 且 index.ready 存在，"
            "覆盖会替换官方索引。\n"
            "  确认请加 --yes；或先试 --dry-run --out-dir <临时目录> 查看分块效果。",
            file=sys.stderr,
        )
        return 2

    try:
        n = build_chunks(args.out_dir, args.max_chars, quiet=args.quiet)
        verify_chunks(args.out_dir)
        if args.dry_run:
            print(f"[build_index] dry-run 完成：{n} chunk（未写 FAISS）。"
                  f"文本分块在 {os.path.join(args.out_dir, 'chunks.jsonl.gz')}")
            return 0
        build_faiss(
            os.path.join(args.out_dir, "chunks.jsonl.gz"),
            os.path.join(args.out_dir, "pali_index.faiss"),
            index_type=args.index,
            model_name=args.model or "BAAI/bge-base-zh",
            quiet=args.quiet,
        )
    except Exception as e:
        print(f"[build_index] 失败：{e}", file=sys.stderr)
        return 1
    print(f"[build_index] 完成：段落感知分块 {n} 条 + FAISS 索引已写入 {args.out_dir}")
    print("[build_index] 提示：请运行 scripts/health_check.py 复核；chunks.offsets/bm25.idx 会自动重建。")
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
