#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rag_index —— 构建本地检索索引（RAG 的"检索"底座）。

把一组文档（.md/.txt/.json/.csv 的文本内容）切成分块，做 TF-IDF 向量化，
保存为索引文件，供 rag_query / rag_synthesize 使用。纯 Python，无外部依赖。

用法：
  python rag_index.py --docs <文档目录> --out <index.json> [--chunk 400] [--overlap 80]
"""
import os, sys, json, glob, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from raglib import tokenize, build_idf, tfidf_vector, chunk_text

EXTS = ("*.md", "*.txt", "*.json", "*.csv", "*.log")


def read_text(path):
    try:
        with open(path, encoding="utf-8", errors="ignore") as f:
            return f.read()
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", required=True, help="文档目录（递归扫描）")
    ap.add_argument("--out", required=True, help="输出索引 json 路径")
    ap.add_argument("--chunk", type=int, default=400)
    ap.add_argument("--overlap", type=int, default=80)
    args = ap.parse_args()

    files = []
    for ext in EXTS:
        files += glob.glob(os.path.join(args.docs, "**", ext), recursive=True)
    files = sorted(set(files))
    if not files:
        print(f"⚠️ 在 {args.docs} 未找到任何文档")
        sys.exit(1)

    chunks = []          # {id, doc, text}
    all_tokens = []      # 每个 chunk 的 token，用于 idf
    for fp in files:
        text = read_text(fp)
        if not text.strip():
            continue
        for ci, piece in enumerate(chunk_text(text, args.chunk, args.overlap)):
            chunks.append({
                "id": f"{len(chunks)}",
                "doc": os.path.relpath(fp, args.docs),
                "text": piece,
            })
            all_tokens.append(tokenize(piece))

    idf = build_idf(all_tokens)
    for c, toks in zip(chunks, all_tokens):
        c["vec"] = tfidf_vector(toks, idf)

    index = {
        "version": 1,
        "source": os.path.abspath(args.docs),
        "chunk_size": args.chunk,
        "overlap": args.overlap,
        "n_docs": len(files),
        "n_chunks": len(chunks),
        "idf": idf,
        "chunks": [{k: v for k, v in c.items() if k != "vec"} for c in chunks],
        # 向量体积大，单独存一份；运行时按需合并
        "vectors": [c["vec"] for c in chunks],
    }
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False)
    print(f"✅ 索引完成：{len(files)} 文档 → {len(chunks)} 分块，写入 {args.out}")


if __name__ == "__main__":
    main()
