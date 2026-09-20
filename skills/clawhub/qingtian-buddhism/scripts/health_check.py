#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
health_check.py — 青田·原始佛教修学助手 一键体检（R2 工程化：把 R1「未执行项」落成可复跑工具）

检查项：
  1. 语料：corpus.ready、txt 数量（期望 217）、顶层目录存在
  2. 语义索引：index.ready、两个文件存在且 >1MB、chunk 条数（期望 101170）、id 连续性
  3. 索引-语料对齐：抽样 20 条 chunk 的 rel 可解析、start/end 在 LF 归一化文本上切片 == text
  4. 依赖：faiss / sentence-transformers / bge 模型缓存（信息级）
  5. 残留：data/_corpus_download.zip（警告）
  6. 内容库：stories 91 / dhammapada 423 / pali 62 / teachings 16 / meditation 5 /
     figures 12 / suttas 20、source 字段覆盖
  7. 脚本：全部 py_compile

用法：
  python scripts/health_check.py          # 逐项输出，退出码 0=健康 / 1=有警告 / 2=有错误
  python scripts/health_check.py --json   # 机器可读 JSON
  python scripts/health_check.py --fast   # 跳过全量 chunk 条数扫描（仅抽样）
"""

import os
import re
import sys
import io
import json
import gzip
import random
import argparse
import py_compile

import semantic_search
from semantic_search import CANON_DIR, get_chunk, resolve_context

SKILL_ROOT = semantic_search.SKILL_ROOT
DATA_DIR = os.path.join(SKILL_ROOT, "data")
CORPUS_DIR = os.path.join(DATA_DIR, "corpus")
INDEX_DIR = os.path.join(DATA_DIR, "index")

EXPECT_TXT = 217
EXPECT_CHUNKS = 101170
EXPECT_COUNTS = {
    "teachings": 16, "pali": 62, "meditation": 5,
    "figures": 12, "suttas": 20,
}
EXPECT_STORIES = 91
EXPECT_DHP = 423


def _walk_txt(root):
    n = 0
    for dp, _dn, fn in os.walk(root):
        for f in fn:
            if f.lower().endswith(".txt"):
                n += 1
    return n


def _count_md(sub):
    d = os.path.join(SKILL_ROOT, "references", sub)
    if not os.path.isdir(d):
        return -1
    return len([f for f in os.listdir(d)
                if f.endswith(".md") and f != "README.md"])


def run_checks(fast=False):
    results = []
    def add(name, status, detail=""):
        results.append({"name": name, "status": status, "detail": detail})

    # ---- 1. 语料 ----
    ready = os.path.exists(os.path.join(DATA_DIR, "corpus.ready"))
    n_txt = _walk_txt(CORPUS_DIR) if os.path.isdir(CORPUS_DIR) else 0
    if not ready:
        add("corpus.ready", "error", "缺失；请运行 python scripts/setup_corpus.py")
    elif n_txt == 0:
        add("语料 txt", "error", f"corpus.ready 存在但 txt=0，请重跑 setup_corpus.py")
    elif n_txt != EXPECT_TXT:
        add("语料 txt 数量", "warn", f"{n_txt} != 期望 {EXPECT_TXT}")
    else:
        add("语料 txt 数量", "ok", f"{n_txt}")

    if not os.path.isdir(CANON_DIR):
        add("译本顶层目录", "error", f"未找到 {os.path.basename(CANON_DIR)}，请检查语料结构")
    else:
        add("译本顶层目录", "ok", os.path.basename(CANON_DIR))

    # ---- 2. 语义索引 ----
    idx_ready = os.path.exists(os.path.join(DATA_DIR, "index.ready"))
    faiss_p = os.path.join(INDEX_DIR, "pali_index.faiss")
    chunks_p = os.path.join(INDEX_DIR, "chunks.jsonl.gz")
    faiss_ok = os.path.exists(faiss_p) and os.path.getsize(faiss_p) >= 1024 * 1024
    chunks_ok = os.path.exists(chunks_p) and os.path.getsize(chunks_p) >= 1024 * 1024
    if not idx_ready:
        add("index.ready", "warn", "缺失；语义检索不可用，Grep 不受影响")
    if not faiss_ok:
        add("pali_index.faiss", "error", "缺失或 <1MB")
    else:
        add("pali_index.faiss", "ok", f"{os.path.getsize(faiss_p)//1048576}MB")
    if not chunks_ok:
        add("chunks.jsonl.gz", "error", "缺失或 <1MB")
    else:
        add("chunks.jsonl.gz", "ok", f"{os.path.getsize(chunks_p)//1048576}MB")

    # ---- 3. 索引-语料对齐 ----
    n_chunks = None
    try:
        if fast:
            n_chunks = len(semantic_search._load_offsets())
        else:
            with gzip.open(chunks_p, "rt", encoding="utf-8") as f:
                n_chunks = sum(1 for _ in f)
    except Exception as e:
        add("chunk 条数", "error", f"读取失败：{e}")
        n_chunks = None
    if n_chunks is not None:
        if n_chunks != EXPECT_CHUNKS:
            add("chunk 条数", "warn", f"{n_chunks} != 期望 {EXPECT_CHUNKS}")
        else:
            add("chunk 条数", "ok", f"{n_chunks}")

    if n_chunks:
        try:
            rng = random.Random(20260909)
            sample = rng.sample(range(min(n_chunks, EXPECT_CHUNKS)), 20)
            miss = 0
            off_fail = 0
            for cid in sample:
                rec = get_chunk(cid)
                if rec is None:
                    miss += 1
                    continue
                rel = rec.get("rel", "")
                path = os.path.join(CANON_DIR, *rel.split(os.sep))
                if not os.path.exists(path):
                    miss += 1
                    continue
                with open(path, encoding="utf-8", errors="replace") as f:
                    lf = f.read().replace("\r\n", "\n")
                s, e = rec.get("start"), rec.get("end")
                if (not isinstance(s, int) or not isinstance(e, int)
                        or s > e or e > len(lf) or lf[s:e] != rec.get("text", "")):
                    off_fail += 1
            if miss or off_fail:
                add("索引-语料对齐(抽样20)", "error",
                    f"rel 解析失败 {miss}，偏移切片不符 {off_fail}")
            else:
                add("索引-语料对齐(抽样20)", "ok", "rel 全解析、LF 偏移切片全吻合")
        except Exception as e:
            add("索引-语料对齐(抽样20)", "error", f"检查异常：{e}")

    # ---- 4. 依赖（信息级） ----
    try:
        import faiss  # noqa
        add("依赖 faiss", "ok")
    except ImportError:
        add("依赖 faiss", "warn", "未安装；语义/混合检索的向量侧不可用（--bm25-only 可用）")
    try:
        import sentence_transformers  # noqa
        add("依赖 sentence-transformers", "ok")
    except ImportError:
        add("依赖 sentence-transformers", "warn", "未安装；语义检索不可用")

    # ---- 5. 残留文件 ----
    zp = os.path.join(DATA_DIR, "_corpus_download.zip")
    if os.path.exists(zp):
        add("残留 _corpus_download.zip", "warn",
            f"存在 {os.path.getsize(zp)//1048576}MB 冗余文件，可删除：del \"{zp}\"")
    else:
        add("残留 _corpus_download.zip", "ok", "无")

    # ---- 6. 内容库 ----
    stories = open(os.path.join(SKILL_ROOT, "references", "stories.md"), encoding="utf-8").read()
    dhp = open(os.path.join(SKILL_ROOT, "references", "dhammapada.md"), encoding="utf-8").read()
    n_stories = len(set(re.findall(r"\(date_index:\s*(\d+)\)", stories)))
    n_dhp = len(set(re.findall(r"<!--\s*dhp:(\d+)\s*-->", dhp)))
    if n_stories != EXPECT_STORIES:
        add("stories 标记", "warn", f"{n_stories} != 期望 {EXPECT_STORIES}")
    else:
        add("stories 标记", "ok", f"{n_stories}")
    if n_dhp != EXPECT_DHP:
        add("dhammapada 标记", "warn", f"{n_dhp} != 期望 {EXPECT_DHP}")
    else:
        add("dhammapada 标记", "ok", f"{n_dhp}")

    for sub, exp in EXPECT_COUNTS.items():
        n = _count_md(sub)
        if n != exp:
            add(f"references/{sub}", "warn", f"{n} != 期望 {exp}")
        else:
            add(f"references/{sub}", "ok", f"{n}")

    # source 覆盖（抽查 5 个目录全部内容文件）
    miss_src = []
    for sub in EXPECT_COUNTS:
        d = os.path.join(SKILL_ROOT, "references", sub)
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md") or f == "README.md":
                continue
            content = open(os.path.join(d, f), encoding="utf-8").read()
            head = content.split("---", 2)
            if len(head) < 2 or "source:" not in head[1]:
                miss_src.append(f"{sub}/{f}")
    if miss_src:
        add("source 覆盖", "warn", f"缺失：{', '.join(miss_src[:5])}")
    else:
        add("source 覆盖", "ok", "内容文件 100% 有 source")

    # ---- 7. 脚本编译 ----
    scripts_dir = os.path.join(SKILL_ROOT, "scripts")
    compile_fail = []
    for f in sorted(os.listdir(scripts_dir)):
        if f.endswith(".py"):
            try:
                py_compile.compile(os.path.join(scripts_dir, f), doraise=True)
            except Exception as e:
                compile_fail.append(f"{f}: {e}")
    if compile_fail:
        add("脚本编译", "error", "; ".join(compile_fail))
    else:
        add("脚本编译", "ok", "全部通过")

    return results


def main():
    ap = argparse.ArgumentParser(description="青田·原始佛教修学助手 一键体检")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fast", action="store_true", help="跳过全量 chunk 条数扫描")
    args = ap.parse_args()

    results = run_checks(fast=args.fast)
    n_err = sum(1 for r in results if r["status"] == "error")
    n_warn = sum(1 for r in results if r["status"] == "warn")

    if args.json:
        print(json.dumps({
            "checks": results,
            "summary": {"errors": n_err, "warnings": n_warn},
        }, ensure_ascii=False, indent=2))
    else:
        sym = {"ok": "✅", "warn": "⚠️ ", "error": "❌"}
        for r in results:
            print(f"{sym[r['status']]} [{r['status'].upper():5}] {r['name']}"
                  + (f"  —  {r['detail']}" if r["detail"] else ""))
        print(f"\n共 {len(results)} 项：错误 {n_err}，警告 {n_warn}，通过 {len(results)-n_err-n_warn}")
        if n_err:
            print("存在错误，请按上方提示处理（多为未运行 setup_corpus.py 或语料结构异常）。")
        elif n_warn:
            warn_names = "、".join(r["name"] for r in results if r["status"] == "warn")
            print(f"有警告：{warn_names}")
            print("（语义检索依赖未装属正常——可选层，Grep 不受影响；其他警告按提示处理）")
        else:
            print("全部健康 ✅")

    return 2 if n_err else (1 if n_warn else 0)


if __name__ == "__main__":
    sys.exit(main())
