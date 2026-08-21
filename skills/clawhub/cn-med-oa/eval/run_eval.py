#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cn-med-oa eval v2 —— 覆盖 v1 盲区：负例查询、多词语义、条目级相关性断言、卷期源断言。

指标：
  检索recall        : 命中数 ≥ min_results（正例）
  相关性精度        : relevance.state==ok 的条目占比 ≥ min_relevant/kept（正例硬断言）
  负例正确性        : 无关/多词查询的 final_status ∈ [low_relevance, not_found] 且 ok数==0
  卷期源正确性      : vol_source=="api"(权威) 占比（不再信任 DOI 正则猜测）
  下载成功率/内容匹配/页码率(信息性)
用法：
  python run_eval.py --quick          # 仅检索+元数据(快)
  python run_eval.py                  # 含下载+PDF校验(慢)
  python run_eval.py --limit 8
"""
import os, sys, json, argparse, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import cn_med_oa  # noqa: E402

GOLDEN = os.path.join(HERE, "golden.jsonl")
VANCOUVER_KEYS = ["title", "authors", "journal", "year", "doi"]


def load_golden(limit=None):
    items = []
    with open(GOLDEN, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                items.append(json.loads(line))
    return items[:limit] if limit else items


def vancouver_score(e):
    ok = 0
    for k in VANCOUVER_KEYS:
        v = e.get(k)
        if k == "authors":
            ok += 1 if v else 0
        else:
            ok += 1 if v else 0
    return ok / len(VANCOUVER_KEYS)


def pdf_contains_kw(path, kws):
    try:
        import fitz
        doc = fitz.open(path)
        txt = "".join(p.get_text() for p in doc[:5])
        doc.close()
    except Exception:
        return None
    return any(kw in txt for kw in kws)


_KW = {"类风湿": ["类风湿", "关节炎", "滑膜", "RA"], "default": None}


def run(quick=False, limit=None, out_dir=None):
    items = load_golden(limit)
    neg = [i for i in items if i.get("negative")]
    pos = [i for i in items if not i.get("negative")]
    print("=" * 74)
    print("cn-med-oa eval v2 | 模式: %s | 正例 %d + 负例 %d" %
          ("quick(仅元数据)" if quick else "full(含下载)", len(pos), len(neg)))
    print("=" * 74)

    dl_dir = out_dir or tempfile.mkdtemp(prefix="cnmed_eval_")
    fails = []
    agg = {"recall": 0, "rel_hard": 0, "neg": 0, "van": [], "dl_ok": 0, "dl_n": 0,
           "content_ok": 0, "content_n": 0, "vol_api": 0, "vol_n": 0, "pages": 0, "pages_n": 0}

    def handle(it, want_pdf):
        r = cn_med_oa.fetch_cn_oa(it["query"], it.get("field", "title"),
                                  max_results=3, save_dir=dl_dir, want_pdf=want_pdf)
        files = r["files"]
        n_ok_rel = sum(1 for e in files if e["relevance"]["state"] == "ok")
        label = it["query"][:14]
        if it.get("negative"):
            good = (r["final_status"] in it["expect_final"]) and \
                   (n_ok_rel == 0 if it.get("expect_no_ok") else True)
            agg["neg"] += good
            print("%s [负例] %-16s | status=%-13s ok=%d | %s" %
                  ("✅" if good else "❌", label, r["final_status"], n_ok_rel, r["disclosure"][:40]))
            if not good:
                fails.append(("负例未拦截", it["query"], r["final_status"], n_ok_rel))
            return
        # 正例
        rp = len(files) >= it.get("min_results", 2)
        hard = n_ok_rel >= it.get("min_relevant", 2)   # 条目级相关性硬断言
        fp = r["final_status"] in it["expect_final"]
        agg["recall"] += rp
        agg["rel_hard"] += hard
        if files:
            agg["van"].append(sum(vancouver_score(e) for e in files) / len(files))
        for e in files:
            if e.get("volume"):
                agg["vol_n"] += 1
                agg["vol_api"] += (e.get("vol_source") == "api" and e.get("vol_consistent", True))
            if e.get("path"):
                if e.get("pages"):
                    agg["pages"] += 1
                agg["pages_n"] += 1
            if e.get("path"):
                agg["dl_n"] += 1
                agg["dl_ok"] += 1
                cm = pdf_contains_kw(e["path"], _KW["类风湿"] if "类风湿" in it["query"] else
                                     [it["query"][:2]] if len(it["query"]) >= 2 else [])
                if cm is not None:
                    agg["content_n"] += 1
                    agg["content_ok"] += 1 if cm else 0
            elif e.get("download_error"):
                agg["dl_n"] += 1
        ok_all = rp and hard and fp
        print("%s %-18s | n=%d ok_rel=%d/%d status=%-13s van=%3.0f%% vol=api%s | %s" %
              ("✅" if ok_all else "❌", label, len(files), n_ok_rel, it.get("min_relevant", 2),
               r["final_status"], (agg["van"][-1] * 100) if agg["van"] else 0,
               "?" if not agg["vol_n"] else "", r["disclosure"][:30]))
        if not ok_all:
            fails.append(("正例断言失败", it["query"], len(files), n_ok_rel, r["final_status"]))

    for it in pos:
        handle(it, not quick)
    for it in neg:
        handle(it, False)  # 负例不下载

    n_pos, n_neg = len(pos), max(len(neg), 1)
    print("\n" + "=" * 74)
    print("汇总")
    print("=" * 74)
    print("  检索 recall(正例)        : %d/%d = %.0f%%" % (agg["recall"], n_pos, 100 * agg["recall"] / max(n_pos, 1)))
    print("  相关性精度硬断言(正例)   : %d/%d = %.0f%%   [v1盲区:已补]" % (agg["rel_hard"], n_pos, 100 * agg["rel_hard"] / max(n_pos, 1)))
    print("  负例拦截率               : %d/%d = %.0f%%   [v1盲区:已补]" % (agg["neg"], len(neg), 100 * agg["neg"] / n_neg))
    if agg["van"]:
        print("  Vancouver完整率(5字段)   : %.0f%%" % (100 * sum(agg["van"]) / len(agg["van"])))
    if agg["vol_n"]:
        print("  卷期权威源(api)占比      : %d/%d = %.0f%%   [P0-1修复验证]" % (agg["vol_api"], agg["vol_n"], 100 * agg["vol_api"] / agg["vol_n"]))
    if agg["pages_n"]:
        print("  页码提取率(信息性)       : %d/%d = %.0f%%" % (agg["pages"], agg["pages_n"], 100 * agg["pages"] / agg["pages_n"]))
    if not quick and agg["dl_n"]:
        print("  下载成功率               : %d/%d = %.0f%%" % (agg["dl_ok"], agg["dl_n"], 100 * agg["dl_ok"] / agg["dl_n"]))
    if agg["content_n"]:
        print("  内容匹配率               : %d/%d = %.0f%%" % (agg["content_ok"], agg["content_n"], 100 * agg["content_ok"] / agg["content_n"]))
    if fails:
        print("\n失败明细:")
        for f in fails:
            print("  -", f)
    print("\n下载目录: %s" % dl_dir)
    return 0 if not fails else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--out-dir", default=None)
    a = ap.parse_args()
    sys.exit(run(quick=a.quick, limit=a.limit, out_dir=a.out_dir))


if __name__ == "__main__":
    main()
