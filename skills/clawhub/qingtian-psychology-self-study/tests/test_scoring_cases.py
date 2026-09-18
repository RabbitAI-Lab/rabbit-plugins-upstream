# -*- coding: utf-8 -*-
"""计分引擎定向用例（R9 起固化，替代一次性验证脚本）。

覆盖：反向计分、危机触发（item 与总分两条路径）、SAS/SDS 标准分换算、
ASRS 官方计数计分、PHQ-2/GAD-2 快速筛查、全量表结构/冒烟/位置键、报告渲染。

用法：python tests/test_scoring_cases.py   （0=全部通过；非 0=存在失败）
"""
import glob
import os
import sys
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "assessment", "scripts"))
from scoring_engine import load_scale, score  # noqa: E402
from report_generator import render, save  # noqa: E402

FAILURES = []


def check(name, cond, detail=""):
    if not cond:
        FAILURES.append(f"{name}：{detail}")
        print(f"  ✗ {name} {detail}")
    else:
        print(f"  ✓ {name}")


def test_reverse():
    print("[1] 反向计分（PSS-10）")
    s = load_scale("PSS-10")
    rev = [it["id"] for it in s["items"] if it.get("reverse")]
    check("PSS-10 有 4 题反向", len(rev) == 4, f"实际 {len(rev)}")
    r0 = score(s, {it["id"]: 0 for it in s["items"]})["dimension_scores"]["压力总分"]
    r4 = score(s, {it["id"]: 4 for it in s["items"]})["dimension_scores"]["压力总分"]
    check("全选0时反向题贡献满分", r0 == 4 * len(rev), f"r0={r0}")
    check("全选4时反向题贡献0分", r4 == 4 * (len(s["items"]) - len(rev)), f"r4={r4}")


def test_crisis():
    print("[2] 危机触发（PHQ-9）")
    s = load_scale("PHQ-9")
    ans = {it["id"]: 0 for it in s["items"]}
    ans["q9"] = 1
    r = score(s, ans)
    check("q9=1 触发 crisis", r["crisis_flag"] is True, str(r["crisis_notes"]))
    ans2 = {"q1": 3, "q2": 3, "q3": 3, "q4": 3, "q5": 3, "q6": 0, "q7": 0, "q8": 0, "q9": 0}
    r2 = score(s, ans2)
    check("总分15无q9 触发 high_risk", r2["crisis_flag"] is True,
          f"总分={r2['dimension_scores']}")
    ans3 = {"q1": 3, "q2": 3, "q3": 0, "q4": 0, "q5": 0, "q6": 0, "q7": 0, "q8": 0, "q9": 0}
    r3 = score(s, ans3)
    check("总分6无q9 不触发", r3["crisis_flag"] is False, str(r3["crisis_notes"]))


def test_standard():
    print("[3] 标准分换算（SAS/SDS）")
    for sid in ("SAS", "SDS"):
        s = load_scale(sid)
        ans = {it["id"]: 2 for it in s["items"]}
        r = score(s, ans)
        d = r["dimension_scores"]["原始总分"]
        std = r["standard_scores"]["原始总分"]
        check(f"{sid} 标准分=原始×1.25", abs(std - d * 1.25) < 0.01, f"d={d} std={std}")


def test_asrs_count():
    print("[4] ASRS 官方计数计分")
    s = load_scale("ASRS")
    # 3 题得 4 分（经常）→ 阳性题数 3 < 4 → 阴性（官方口径）
    r1 = score(s, {"q1": 4, "q2": 4, "q3": 4, "q4": 0, "q5": 0, "q6": 0})
    n1 = r1["dimension_scores"]["筛查总分"]
    check("3 题高分计 3 项阳性", n1 == 3, f"n={n1}")
    check("3 项阳性判阴性", r1["bands"]["筛查总分"] == "阴性（低风险）", str(r1["bands"]))
    # 6 题各得 2 分（有时）→ 6 项阳性 → 阳性提示（官方口径）
    r2 = score(s, {"q1": 2, "q2": 2, "q3": 2, "q4": 2, "q5": 2, "q6": 2})
    n2 = r2["dimension_scores"]["筛查总分"]
    check("6 题各 2 分计 6 项阳性", n2 == 6, f"n={n2}")
    check("6 项阳性判阳性提示", r2["bands"]["筛查总分"] == "阳性提示", str(r2["bands"]))


def test_quick_screen():
    print("[5] 快速筛查（PHQ-2/GAD-2）")
    for sid in ("PHQ-2", "GAD-2"):
        s = load_scale(sid)
        r_neg = score(s, {"q1": 0, "q2": 1})
        r_pos = score(s, {"q1": 2, "q2": 1})
        check(f"{sid} 总分3判阳性提示", r_pos["bands"]["筛查总分"] == "阳性提示", str(r_pos["bands"]))
        check(f"{sid} 总分1判阴性", "阴性" in r_neg["bands"]["筛查总分"], str(r_neg["bands"]))


def test_all_scales():
    print("[6] 全量表结构/冒烟/位置键")
    paths = sorted(glob.glob(os.path.join(ROOT, "assessment", "scales", "*.json")))
    check("量表数量=21", len(paths) == 21, f"实际 {len(paths)}")
    for p in paths:
        sid = os.path.splitext(os.path.basename(p))[0]
        s = load_scale(sid)
        items = s["items"]
        iids = {it["id"] for it in items}
        for d in s.get("dimensions", []):
            for iid in d.get("items", []):
                check(f"{sid} 维度引用存在", iid in iids, f"{d.get('name')}->{iid}")
        for b in s.get("interpretation", {}).get("bands", []):
            check(f"{sid} bands 区间完整", b.get("min") is not None and b.get("max") is not None, str(b))
        for ci in s.get("safety", {}).get("crisis_items", []):
            check(f"{sid} 危机题存在", ci in iids, ci)
        # item_id 作答
        r = score(s, {it["id"]: len(it["options"]) // 2 for it in items})
        check(f"{sid} item_id 冒烟完成", r["complete"] is True, str(r.get("missing_items")))
        # 位置键作答
        r2 = score(s, {"q%d" % (i + 1): len(items[i]["options"]) // 2 for i in range(len(items))})
        check(f"{sid} 位置键冒烟完成", r2["complete"] is True, str(r2.get("missing_items")))


def test_report():
    print("[7] 报告渲染与危机单源")
    s = load_scale("PHQ-9")
    ans = {it["id"]: 1 for it in s["items"]}
    r = score(s, ans)
    html = render(s, r)
    check("报告含量表名", s["name"] in html)
    check("报告含危机单源热线(12356)", "12356" in html)
    check("报告含 PDF 导出提示", "另存为 PDF" in html)
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        path = save(s, r, out_dir=td)
        check("报告落盘", os.path.exists(path) and os.path.getsize(path) > 500, path)


def main():
    test_reverse()
    test_crisis()
    test_standard()
    test_asrs_count()
    test_quick_screen()
    test_all_scales()
    test_report()
    if FAILURES:
        print(f"\n失败 {len(FAILURES)} 项：")
        for f in FAILURES:
            print("  -", f)
        sys.exit(1)
    print("\ntest_scoring_cases 全部通过 ✓")


if __name__ == "__main__":
    main()
