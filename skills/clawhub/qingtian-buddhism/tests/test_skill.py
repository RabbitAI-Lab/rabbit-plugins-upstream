#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_skill.py — 青田·原始佛教修学助手 自动化回归（R2 新增；纯标准库，无需 pytest）

运行：python tests/test_skill.py            # 全部用例，退出码 0=全过
      python tests/test_skill.py -v        # 详细输出
      python tests/test_skill.py -k chunk  # 按名称过滤

覆盖：语料数量 / 索引条数与对齐 / 偏移口径 / 内容库标记 / 分类受控词表 /
      source 覆盖 / 脚本编译 / 版本一致性 / 语义检索上下文解析。
"""

import os
import re
import sys
import gzip
import json
import glob
import random

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

EXPECT_TXT = 217
EXPECT_CHUNKS = 101170
EXPECT_STORIES = 91
EXPECT_DHP = 423
EXPECT_DIR_COUNTS = {"teachings": 16, "pali": 62, "meditation": 5,
                     "figures": 12, "suttas": 20}
CATEGORY_VOCAB = {"无常", "无我", "慈悲", "智慧", "精进", "因果", "布施",
                  "持戒", "忍辱", "正念", "信心", "出家", "佛陀", "弟子",
                  "降魔", "菩萨行", "不放逸"}

_tests = []


def test(fn):
    _tests.append(fn)
    return fn


@test
def test_corpus_txt_count():
    n = 0
    for dp, _dn, fs in os.walk(os.path.join(ROOT, "data", "corpus")):
        for f in fs:
            if f.lower().endswith(".txt"):
                n += 1
    assert n == EXPECT_TXT, f"txt 数量 {n} != {EXPECT_TXT}"


@test
def test_index_files_exist():
    for name in ("pali_index.faiss", "chunks.jsonl.gz"):
        p = os.path.join(ROOT, "data", "index", name)
        assert os.path.exists(p), f"缺失 {p}"
        assert os.path.getsize(p) >= 1024 * 1024, f"{name} 过小"


@test
def test_chunk_ids_continuous():
    # 全量扫描 id 连续性
    n = 0
    with gzip.open(os.path.join(ROOT, "data", "index", "chunks.jsonl.gz"),
                   "rt", encoding="utf-8") as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            assert rec["id"] == i, f"id 不连续：行 {i} 实际 {rec['id']}"
            n += 1
    assert n == EXPECT_CHUNKS, f"chunk 数 {n} != {EXPECT_CHUNKS}"


@test
def test_chunk_offset_alignment_sample():
    """抽样 30 条：rel 可解析，且 start/end 在 LF 归一化文本上切片 == text（CRLF 口径修复）。"""
    random.seed(20260909)
    with gzip.open(os.path.join(ROOT, "data", "index", "chunks.jsonl.gz"),
                   "rt", encoding="utf-8") as f:
        lines = f.readlines()
    canon = os.path.join(ROOT, "data", "corpus",
                         "巴利三藏巴利-中文对照译本（2026-06-21） txt")
    for cid in random.sample(range(len(lines)), 30):
        rec = json.loads(lines[cid])
        p = os.path.join(canon, *rec["rel"].split(os.sep))
        assert os.path.exists(p), f"rel 无法解析：{rec['rel']}"
        with open(p, encoding="utf-8", errors="replace") as f:
            lf = f.read().replace("\r\n", "\n")
        s, e = rec["start"], rec["end"]
        assert isinstance(s, int) and isinstance(e, int) and s <= e and e <= len(lf), \
            f"偏移越界：{rec['rel']} {s}-{e}（文件 {len(lf)}）"
        assert lf[s:e] == rec["text"], f"偏移切片不符：id={cid} {rec['rel']}"


@test
def test_semantic_resolve_context():
    """resolve_context 应在 CRLF 文件上正确返回上下文（回归 P1 修复）。"""
    import semantic_search
    rec = semantic_search.get_chunk(0)
    ctx = semantic_search.resolve_context(rec["rel"], rec["start"], rec["end"], width=200)
    assert ctx is not None and len(ctx) > 0
    # 上下文必须包含 chunk 文本（LF 口径一致）
    assert rec["text"] in ctx, "上下文未包含原 chunk 文本（偏移口径错误）"


@test
def test_stories_markers():
    stories = open(os.path.join(ROOT, "references", "stories.md"), encoding="utf-8").read()
    idxs = re.findall(r"\(date_index:\s*(\d+)\)", stories)
    assert len(idxs) == EXPECT_STORIES, f"stories 标记 {len(idxs)} != {EXPECT_STORIES}"
    assert len(set(idxs)) == EXPECT_STORIES and set(idxs) == {str(i) for i in range(1, 92)}


@test
def test_stories_categories():
    stories = open(os.path.join(ROOT, "references", "stories.md"), encoding="utf-8").read()
    cats = re.findall(r"category:\s*(.+)", stories)
    assert len(cats) == EXPECT_STORIES, f"category 数 {len(cats)} != {EXPECT_STORIES}"
    bad = [c for c in cats if c not in CATEGORY_VOCAB]
    assert not bad, f"越界分类：{bad}"


@test
def test_dhammapada_markers():
    dhp = open(os.path.join(ROOT, "references", "dhammapada.md"), encoding="utf-8").read()
    idxs = re.findall(r"<!--\s*dhp:(\d+)\s*-->", dhp)
    assert len(idxs) == EXPECT_DHP, f"dhp 标记 {len(idxs)} != {EXPECT_DHP}"
    assert len(set(idxs)) == EXPECT_DHP and max(int(x) for x in idxs) == 423


@test
def test_reference_dir_counts():
    for sub, exp in EXPECT_DIR_COUNTS.items():
        d = os.path.join(ROOT, "references", sub)
        n = len([f for f in os.listdir(d) if f.endswith(".md") and f != "README.md"])
        assert n == exp, f"{sub} {n} != {exp}"


@test
def test_source_coverage():
    for sub in EXPECT_DIR_COUNTS:
        d = os.path.join(ROOT, "references", sub)
        for f in sorted(os.listdir(d)):
            if not f.endswith(".md") or f == "README.md":
                continue
            content = open(os.path.join(d, f), encoding="utf-8").read()
            head = content.split("---", 2)
            assert len(head) >= 2 and "source:" in head[1], f"{sub}/{f} 缺 source"


@test
def test_scripts_compile():
    import py_compile
    for p in sorted(glob.glob(os.path.join(ROOT, "scripts", "*.py"))):
        py_compile.compile(p, doraise=True)


@test
def test_version_consistency():
    """SKILL.md 与 README 版本号一致。"""
    skill = open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8").read()
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    sv = re.search(r"^version:\s*([\d.]+)", skill, re.M)
    rv = re.search(r"当前版本：\*\*v([\d.]+)\*\*", readme)
    assert sv and rv, "无法解析版本号"
    assert sv.group(1) == rv.group(1), f"版本不一致 SKILL {sv.group(1)} vs README {rv.group(1)}"


@test
def test_gitignore_hygiene():
    gi = open(os.path.join(ROOT, ".gitignore"), encoding="utf-8").read()
    assert "data/" in gi
    assert "__pycache__" in gi


def main():
    verbose = "-v" in sys.argv
    filt = None
    if "-k" in sys.argv:
        filt = sys.argv[sys.argv.index("-k") + 1]
    n_pass = n_fail = 0
    failed = []
    for fn in _tests:
        if filt and filt not in fn.__name__:
            continue
        try:
            fn()
            n_pass += 1
            if verbose:
                print(f"PASS  {fn.__name__}")
        except Exception as e:
            n_fail += 1
            failed.append((fn.__name__, e))
            print(f"FAIL  {fn.__name__}: {e}")
    print(f"\n通过 {n_pass} / {n_pass + n_fail}")
    if failed:
        for name, e in failed:
            print(f"  ✗ {name}: {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
