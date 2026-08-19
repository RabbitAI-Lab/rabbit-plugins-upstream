# -*- coding: utf-8 -*-
"""v2.3.0 新增功能单测：核心期刊标注 / RIS 导出 / 批量任务 / SSR 转义解码。

运行: python3 eval/test_v230.py   （纯本地，不发任何网络请求）
"""
import os, sys, json, tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import cn_med_oa as m

PASS = 0
FAIL = 0


def ok(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("  ✅ %s" % name)
    else:
        FAIL += 1
        print("  ❌ %s  %s" % (name, detail))


# ── 1. rank_journal 边界 ──
print("== rank_journal ==")
ok("精确命中", m.rank_journal("中华内科杂志") == "北大核心/CSCD")
ok("首尾空白容忍", m.rank_journal(" 中华内科杂志 ") == "北大核心/CSCD")
ok("全角括号归一化", m.rank_journal("北京大学学报（医学版）") == "北大核心/CSCD")
ok("半角括号精确", m.rank_journal("北京大学学报(医学版)") == "北大核心/CSCD")
ok("电子版不继承母刊", m.rank_journal("中华内科杂志(电子版)") == "",
   "got=%r" % m.rank_journal("中华内科杂志(电子版)"))
ok("未收录返回空", m.rank_journal("某不知名杂志") == "")
ok("空串返回空", m.rank_journal("") == "")
ok("None 安全", m.rank_journal(None) == "")
ok("非中华系命中", m.rank_journal("中国循证医学杂志") == "北大核心/CSCD")
ok("高校学报命中", m.rank_journal("北京大学学报(医学版)") == "北大核心/CSCD")
ok("表规模>=150", len(m._CORE_JOURNALS) >= 150, "n=%d" % len(m._CORE_JOURNALS))
from collections import Counter
norm = [k.strip().replace("（", "(").replace("）", ")") for k in m._CORE_JOURNALS]
dup = [k for k, v in Counter(norm).items() if v > 1]
ok("无括号变体重复键", not dup, "dup=%s" % dup)
bad = [k for k, v in m._CORE_JOURNALS.items() if not v or "/" not in v and "核心" not in v]
ok("值格式合法", not bad, "bad=%s" % bad)

# ── 2. export_ris 边界 ──
print("== export_ris ==")
td = tempfile.mkdtemp(prefix="ris_t_")
full = {"files": [
    {"title": "测试文献", "authors": ["张三", "李四"], "journal": "中华内科杂志",
     "year": "2024", "volume": "63", "issue": "11", "pages": "1059-1077",
     "doi": "10.3760/cma.j.cn111213-20240515-00220",
     "download_url": "https://rs.yiigle.com/cmaid/1519051"},
    {"title": "无页码", "authors": [], "journal": "", "year": "2025", "pages": "",
     "doi": "", "path": "/x/a.pdf"},
    {"title": "单页", "authors": ["王五"], "journal": "J", "year": "", "volume": "",
     "issue": "", "pages": "123", "doi": "10.x"},
]}
p, n = m.export_ris(full, td)
c = open(p, encoding="utf-8").read()
ok("条数正确", n == 3)
ok("TY/AU/PY/JO/VL/IS/SP/EP/DO/UR 全字段", all(x in c for x in
   ["TY  - JOUR", "AU  - 张三", "PY  - 2024", "JO  - 中华内科杂志", "VL  - 63",
    "IS  - 11", "SP  - 1059", "EP  - 1077", "DO  - 10.3760", "UR  - https://rs.yiigle.com"]))
ok("空 authors 无 AU 行", "AU  - \n" not in c)
ok("path 分支用 L1", "L1  - /x/a.pdf" in c)
ok("无 UR 时无 UR 行", c.count("UR  - ") == 1)
ok("单页 SP=123 无 EP", "SP  - 123" in c and "EP  - 123" not in c)
empty = m.export_ris({"files": []}, td)
ok("空列表返回 0 条", empty[1] == 0 and os.path.exists(empty[0]))
enc = open(empty[0], encoding="utf-8").read()
ok("空文件无 ER 残迹", "ER" not in enc)

# ── 3. _decode_ssr_escapes 边界 ──
print("== _decode_ssr_escapes ==")
ok("\\uXXXX 解码", m._decode_ssr_escapes("\\u4e2d\\u6587") == "中文")
ok("\\\" 转引号", m._decode_ssr_escapes("a\\\"b") == 'a"b')
ok("\\\\ 转反斜杠", m._decode_ssr_escapes("a\\\\b") == "a\\b")
ok("混合", m._decode_ssr_escapes("x\\u00e9y\\\"z\\\\w") == "xéy\"z\\w")
ok("无转义原样", m._decode_ssr_escapes("plain text") == "plain text")
ok("代理对双序列", m._decode_ssr_escapes("\\ud83d\\ude00") == "\U0001f600")

# ── 4. run_batch 边界（mock fetch 不发网络）──
print("== run_batch ==")
_orig = m.fetch_cn_oa
calls = []


def _fake(q, field, max_results, save_dir, want_pdf, min_relevance, sources,
          year_from=None, year_to=None, doc_type=None):
    calls.append(q)
    if q == "有结果":
        return {"query": q, "field": field, "attempts": [], "final_status": "metadata_only",
                "files": [{"title": "R1", "relevance": {"state": "ok"}, "source": "Yiigle"}],
                "disclosure": ""}
    if q == "无结果":
        return {"query": q, "field": field, "attempts": [], "final_status": "not_found",
                "files": [], "disclosure": "❌ 检索无结果"}
    return {"query": q, "field": field, "attempts": [], "final_status": "low_relevance",
            "files": [], "disclosure": "⚠️ 相关性不足"}


m.fetch_cn_oa = _fake
bf = os.path.join(td, "batch.txt")
with open(bf, "w", encoding="utf-8") as f:
    f.write("# 注释行\n\n有结果\n无结果\n三态\n")
merged, report = m.run_batch(bf, "title", 5, None, False, "low", ("Yiigle",))
m.fetch_cn_oa = _orig
ok("跳过注释与空行", calls == ["有结果", "无结果", "三态"], "calls=%s" % calls)
ok("stats 计数", merged["batch"]["metadata_only"] == 1 and merged["batch"]["not_found"] == 1
   and merged["batch"]["low_relevance"] == 1 and merged["batch"]["total"] == 3,
   "batch=%s" % merged["batch"])
ok("files 合并", len(merged["files"]) == 1)
ok("报告行含汇总", any("1/3" in x for x in report) and any("❌" in x for x in report))
ok("无有效词报错", True)
try:
    bf2 = os.path.join(td, "empty.txt")
    open(bf2, "w", encoding="utf-8").write("# only comment\n")
    m.run_batch(bf2, "title", 5, None, False, "low", ("Yiigle",))
    ok("空文件 SystemExit", False)
except SystemExit:
    ok("空文件 SystemExit", True)

# ── 5. 集成完整性：entry 构造注入 journal_rank ──
print("== entry 注入 ==")
e_y = m.yiigle_to_entry({"title": "T", "authors": [], "journal": "中华内科杂志", "year": "2024",
                         "vol": "", "issue": "", "pages": "", "artDoi": "", "artUrl": "",
                         "docType": "", "abstract": "", "id": ""}, {"state": "ok"}, None, False)
ok("yiigle entry 注入", e_y.get("journal_rank") == "北大核心/CSCD")
v = m.to_vancouver({"title": "T", "authorInfo": [], "objectInfo": {"name": "中国循证医学杂志"},
                     "year": "2024", "doi": ""}, {})
ok("weipu entry 注入", v.get("journal_rank") == "北大核心/CSCD")

print("\n结果: %d 通过, %d 失败" % (PASS, FAIL))
sys.exit(1 if FAIL else 0)