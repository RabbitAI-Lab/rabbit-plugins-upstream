#!/usr/bin/env python3
"""career_selftest.py — ai-era-career-planner v2.0.0 安装自检（离线、纯标准库）

用法: python3 tools/career_selftest.py
输出: 每组 PASS/FAIL + 摘要行；全部通过 → ALL CHECKS PASSED (exit 0)，否则 exit 1。
"""
import json
import os
import re
import subprocess
import sys
import tempfile

B = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
SCRIPT = os.path.join(B, "scripts", "career_planner.py")
GEN = os.path.join(B, "scripts", "generate_salary_db.py")
REPG = os.path.join(B, "scripts", "report_generator.py")
DB = os.path.join(B, "data", "salary_database.json")

RESULTS = []


def check(group, name, cond, detail=""):
    RESULTS.append((group, name, bool(cond), detail))


def sh(args, **kw):
    return subprocess.run([PY] + args, capture_output=True, text=True, **kw)


def run_cp(*args):
    return sh([SCRIPT] + list(args))


def g1_frontmatter():
    g = "1-frontmatter"
    txt = open(os.path.join(B, "SKILL.md"), encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    check(g, "frontmatter exists", bool(m))
    fm = m.group(1) if m else ""
    for field in ("name: ai-era-career-planner", "version: 2.0.0", "author: orionshaowswmw",
                  "license: MIT-0"):
        check(g, f"field {field.split(':')[0]}", field in fm)
    check(g, "tags is a list", re.search(r"^tags:\n(\s+- .+\n)+", fm, re.M) is not None)
    dm = re.search(r"description: >\n((?:\s+.+\n)+)", fm)
    desc = re.sub(r"\s+", " ", dm.group(1)).strip() if dm else ""
    check(g, "description non-empty", len(desc) > 40, f"len={len(desc)}")
    check(g, "description <= 1024", len(desc) <= 1024, f"len={len(desc)}")
    check(g, "no fake verification_hash", "verification_hash" not in fm)
    check(g, "no comma-string tags", not re.search(r"^tags:\s*\".*,.+\"", fm, re.M))


def g2_no_phantoms():
    g = "2-no-phantoms"
    txt = open(os.path.join(B, "SKILL.md"), encoding="utf-8").read()
    check(g, "no i18n/en.md phantom", "i18n/en.md" not in txt)
    for f in ("references/integrations.md", "references/assessment.md", "references/mbti.md",
              "references/job_demand.md", "references/salary_data.md", "references/ai_career_impact.md",
              "references/overseas_jobs.md", "references/career_anchor.md", "references/education_paths.md",
              "references/flow_engine.md", "references/industry_trends.md", "references/tracker_system.md",
              "references/integrations.md", "data/salary_database.json",
              "data/scrape_samples.json", "data/insurance_broker_companies.json"):
        check(g, f"exists: {f}", os.path.exists(os.path.join(B, f)))
    # CHANGELOG.md is the version-history record: it *describes* v1's removed
    # flaws (the author /Users/... path, the fabricated source claim) so the
    # rebuild stays traceable, and quoting them there is intentional history,
    # not a live claim. The selftest quotes them too. Both are excluded from
    # these specific string-claim scans; EVERY other shipped file — including
    # README.md and all of references/ data/ scripts/ SKILL.md — must stay
    # clean (and does).
    alltxt = ""
    self_path = os.path.abspath(__file__)
    excluded_paths = {
        self_path,
        os.path.abspath(os.path.join(B, "CHANGELOG.md")),
    }
    for root, _, files in os.walk(B):
        if ".git" in root:
            continue
        for f in files:
            p = os.path.join(root, f)
            if os.path.getsize(p) < 3_000_000 and os.path.abspath(p) not in excluded_paths:
                alltxt += open(p, encoding="utf-8", errors="ignore").read()
    check(g, "no /Users/ author paths", "/Users/" not in alltxt)
    check(g, "no 智联招聘2024年度薪酬报告 (fabricated)", "智联招聘2024年度薪酬报告" not in alltxt)
    check(g, "no 国家统计局 claim", "国家统计局" not in alltxt)


def g3_holland():
    g = "3-holland"
    combos = [
        ({"q1": "安静", "q2": "事实", "q3": "规则"}, "R"),
        ({"q1": "安静", "q2": "事实", "q3": "自由"}, "R"),
        ({"q1": "安静", "q2": "概念", "q3": "规则"}, "I"),
        ({"q1": "安静", "q2": "概念", "q3": "自由"}, "I/A"),
        ({"q1": "一起", "q2": "事实", "q3": "规则"}, "C"),
        ({"q1": "一起", "q2": "事实", "q3": "自由"}, "E"),
        ({"q1": "一起", "q2": "概念", "q3": "规则"}, "S"),
        ({"q1": "一起", "q2": "概念", "q3": "自由"}, "S"),
    ]
    for a, want in combos:
        r = run_cp("holland", "--answers", json.dumps(a, ensure_ascii=False))
        ok = r.returncode == 0
        code = None
        if ok:
            d = json.loads(r.stdout)
            code = d.get("code")
            ok = code == want and d.get("assessment_type") == "screening"
        check(g, f"{a['q1']}+{a['q2']}+{a['q3']} -> {want}", ok, f"got={code} rc={r.returncode}")
    r = run_cp("holland", "--answers", json.dumps({"q1": "安静"}, ensure_ascii=False))
    check(g, "missing answers -> exit 2", r.returncode == 2)
    try:
        e = json.loads(r.stderr)
        check(g, "error is JSON with questions", "questions" in e)
    except Exception:
        check(g, "error is JSON with questions", False, r.stderr[:80])


def g4_match():
    g = "4-match"
    full = json.dumps({"holland": "R", "values": ["成就感", "自主性"], "anchor": "自主/独立型"},
                      ensure_ascii=False)
    r = run_cp("match", "--answers", full, "--city", "北京", "--industry", "互联网/IT")
    ok = r.returncode == 0
    d = json.loads(r.stdout) if ok else {}
    check(g, "match runs", ok)
    check(g, "screening type", d.get("assessment_type") == "screening")
    check(g, "heuristic note", "启发式" in d.get("scoring_note", "") and "非预测" in d.get("scoring_note", ""))
    check(g, "not_assessed empty", d.get("not_assessed") == [])
    recs = d.get("recommendations", [])
    check(g, "top rec 后端开发 fit=4 salary 13500-24200",
          bool(recs) and recs[0]["title"] == "后端开发" and recs[0]["score"] == 4
          and "13500-24200" in recs[0]["salary"], str(recs[:1]))
    check(g, "体制内 salary null (full_ranking) + note (recommendations)",
          any(x["name"] == "体制内" and x["salary"] is None for x in d.get("full_ranking", []))
          and all((r["salary_note"] or "暂无参考区间" in r["salary"]) for r in recs))
    # tie-break determinism: two equal-fit names sorted; run twice
    r2 = run_cp("match", "--answers", full, "--city", "北京", "--industry", "互联网/IT")
    check(g, "deterministic (two runs identical)", r.stdout == r2.stdout)
    # partial: values only
    r3 = run_cp("match", "--answers", json.dumps({"values": ["稳定性", "人际关系"]}, ensure_ascii=False))
    ok3 = r3.returncode == 0
    d3 = json.loads(r3.stdout) if ok3 else {}
    check(g, "partial -> not_assessed + renorm weights",
          ok3 and d3.get("not_assessed") == ["holland", "anchor"] and d3.get("weights_used", {}).get("values") == 1.0)
    # empty
    r4 = run_cp("match", "--answers", "{}")
    check(g, "empty answers -> exit 2", r4.returncode == 2)
    # bad value
    r5 = run_cp("match", "--answers", json.dumps({"values": ["钱"]}, ensure_ascii=False))
    check(g, "invalid value -> exit 2", r5.returncode == 2)
    # holland_answers raw
    r6 = run_cp("match", "--answers", json.dumps(
        {"holland_answers": {"q1": "安静", "q2": "概念", "q3": "自由"}}, ensure_ascii=False))
    ok6 = r6.returncode == 0
    d6 = json.loads(r6.stdout) if ok6 else {}
    check(g, "holland_answers raw -> I/A", ok6 and d6.get("inputs", {}).get("holland") == "I/A")


def g5_salary():
    g = "5-salary"
    r = run_cp("salary", "--city", "北京", "--industry", "互联网/IT",
               "--occupation", "后端开发工程师", "--level", "entry")
    ok = r.returncode == 0
    d = json.loads(r.stdout) if ok else {}
    check(g, "known value 13500-24200",
          ok and d.get("salary_min") == 13500 and d.get("salary_max") == 24200)
    check(g, "provenance is factor model", "因子模型" in d.get("provenance", ""))
    r2 = run_cp("salary", "--city", "纽约", "--industry", "互联网/IT",
                "--occupation", "后端开发工程师", "--level", "entry")
    ok2 = r2.returncode == 2
    e = {}
    try:
        e = json.loads(r2.stderr)
    except Exception:
        pass
    check(g, "invalid city -> exit 2 + valid list", ok2 and "city" in e.get("valid_options", {}))
    r3 = run_cp("salary", "--list", "levels")
    ok3 = r3.returncode == 0
    d3 = json.loads(r3.stdout) if ok3 else {}
    check(g, "--list levels", ok3 and d3.get("levels") == ["entry", "mid", "senior", "expert"])
    r4 = run_cp("salary", "--city", "北京", "--industry", "不存在的行业",
                "--occupation", "后端开发工程师", "--level", "entry")
    check(g, "invalid industry -> exit 2", r4.returncode == 2)
    r5 = run_cp("salary", "--list", "bogus")
    ok5 = r5.returncode == 2
    e5 = {}
    try:
        e5 = json.loads(r5.stderr)
    except Exception:
        pass
    check(g, "invalid --list -> exit 2 + valid keys",
          ok5 and "valid_options" in e5 and set(e5.get("valid_options", [])) ==
          {"cities", "industries", "occupations", "levels"})


def g6_report():
    g = "6-report"
    full = json.dumps({"holland": "R", "values": ["成就感", "自主性"], "anchor": "自主/独立型"},
                      ensure_ascii=False)
    m = json.loads(run_cp("match", "--answers", full, "--city", "北京",
                          "--industry", "互联网/IT").stdout)
    data = {"nickname": "自检", "stage": "测试", "holland": "R", "values": ["成就感", "自主性"],
            "recommendations": m["recommendations"],
            "ai_guide": {"skills": "x", "tools": "y", "cert": "z"},
            "actions": {"today": "t", "1month": "m", "3months": "q", "1year": "y"}}
    with tempfile.TemporaryDirectory() as td:
        df = os.path.join(td, "d.json")
        json.dump(data, open(df, "w"), ensure_ascii=False)
        r = sh([SCRIPT, "report", "--data-file", df])
        ok = r.returncode == 0 and "个性化职业规划报告" in r.stdout
        check(g, "report roundtrip stdout", ok)
        check(g, "footer v2.0.0", "ai-era-career-planner v2.0.0" in r.stdout)
        check(g, "disclaimer present", "筛查性参考" in r.stdout and "非预测" in r.stdout)
        r2 = sh([REPG, "--data-file", df, "--out", os.path.join(td, "r.md")])
        outp = os.path.join(td, "r.md")
        ok2 = r2.returncode == 0 and os.path.exists(outp)
        check(g, "report_generator --out", ok2)
        check(g, "report_generator footer", ok2 and "v2.0.0" in open(outp, encoding="utf-8").read())
        bad = os.path.join(td, "bad.json")
        open(bad, "w").write("{not json")
        r3 = sh([REPG, "--data-file", bad])
        check(g, "malformed JSON -> exit 2", r3.returncode == 2)
        empty = os.path.join(td, "empty.json")
        json.dump({"recommendations": []}, open(empty, "w"))
        r4 = sh([REPG, "--data-file", empty])
        ok4 = r4.returncode == 2
        check(g, "empty recommendations -> exit 2 + actionable", ok4 and "recommendations" in r4.stderr)


def g7_db_integrity():
    g = "7-db-integrity"
    d = json.load(open(DB, encoding="utf-8"))
    recs = d["records"]
    check(g, "5376 records", len(recs) == 5376, f"got={len(recs)}")
    check(g, "no 2024 fabricated source in records",
          all("2024" not in r.get("data_source", "") for r in recs))
    # arithmetic reproduction
    sys.path.insert(0, os.path.dirname(GEN))
    import importlib.util
    spec = importlib.util.spec_from_file_location("gsdb", GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    bad = 0
    for r in recs:
        lo, hi = mod.modeled_range(r["city"], r["industry"], r["occupation"], r["level"])
        if (lo, hi) != (r["salary_min"], r["salary_max"]):
            bad += 1
    check(g, "all records match factor arithmetic", bad == 0, f"mismatch={bad}")
    check(g, "meta provenance_statement", "不是招聘平台抓取数据" in d["meta"]["provenance_statement"])
    check(g, "meta calibration_anchors >= 3", len(d["meta"]["calibration_anchors"]) >= 3)
    # regenerate determinism (date fixed)
    with tempfile.TemporaryDirectory() as td:
        out = os.path.join(td, "db.json")
        r = sh([GEN, "--out", out, "--date", "2026-09-06"])
        ok = r.returncode == 0
        d2 = json.load(open(out, encoding="utf-8"))
        check(g, "regeneration ok", ok)
        check(g, "regeneration deterministic (records identical)",
              d2["records"] == recs and d2["scrape_samples"] == d["scrape_samples"])


def g8_scrape_samples():
    g = "8-scrape-samples"
    d = json.load(open(DB, encoding="utf-8"))
    s = d["scrape_samples"]
    check(g, "74 samples", len(s) == 74, f"got={len(s)}")
    check(g, "no verification fields",
          all(not any(k in x for k in ("verification_status", "verified_by", "verification_source")) for x in s))
    summ = d["meta"]["scrape_sample_summary"]
    check(g, "summary honest breakdown 32/29/13",
          summ.get("identical_to_model") == 32 and summ.get("genuine_scrapes_comparable") == 29
          and summ.get("nonmodelable") == 13, json.dumps(summ, ensure_ascii=False)[:120])
    check(g, "genuine drift range recorded",
          summ.get("genuine_drift_range_pct") == [-80.2, 431.9], str(summ.get("genuine_drift_range_pct")))
    raw = json.load(open(os.path.join(B, "data", "scrape_samples.json"), encoding="utf-8"))
    check(g, "raw scrape file has 74 + _meta", len(raw.get("samples", [])) == 74 and "_meta" in raw)


def g9_insurance():
    g = "9-insurance"
    d = json.load(open(os.path.join(B, "data", "insurance_broker_companies.json"), encoding="utf-8"))
    check(g, "28 companies", len(d.get("companies", [])) == 28)
    check(g, "meta provenance note", "核实" in d["_meta"].get("data_provenance", ""))
    check(g, "no raw_answer/snippets junk",
          all("raw_answer" not in c and "snippets" not in c for c in d["companies"]))
    check(g, "every entry has provenance", all("provenance" in c for c in d["companies"]))


def g10_references():
    g = "10-references"
    for f in ("industries/creative.md", "industries/education.md", "industries/finance.md",
              "industries/healthcare.md", "industries/manufacturing.md", "industries/tech_career.md",
              "ai_career_impact.md", "industry_trends.md"):
        t = open(os.path.join(B, "references", f), encoding="utf-8").read()
        check(g, f"label in {f}", ("供参考" in t) and ("定性" in t))
    j = open(os.path.join(B, "references", "job_demand.md"), encoding="utf-8").read()
    check(g, "job_demand dated sources", all(x in j for x in
          ("2026-07-21", "2025-03-26", "2026-03-31", "2026-07-03", "+244%", "+87.7%")))
    o = open(os.path.join(B, "references", "overseas_jobs.md"), encoding="utf-8").read()
    check(g, "overseas provenance line", "Tavily" in o and "2026-07-26" in o)
    a = open(os.path.join(B, "references", "assessment.md"), encoding="utf-8").read()
    check(g, "assessment validity evidence", "50-65%" in a and ".91" in a and "8 组合" in a)
    m = open(os.path.join(B, "references", "mbti.md"), encoding="utf-8").read()
    check(g, "mbti 16-row crosswalk complete", m.count("| S |") + m.count("| R |") + m.count("| I |")
          + m.count("| A |") + m.count("| E |") + m.count("| C |") >= 16)
    s = open(os.path.join(B, "references", "salary_data.md"), encoding="utf-8").read()
    check(g, "salary_data honesty", "因子模型" in s and "不是" in s and "200000" in s)


def g11_cli_contract():
    g = "11-cli-contract"
    r = sh([SCRIPT, "holland", "--answers", "{bad"])
    ok = r.returncode == 2
    try:
        json.loads(r.stderr)
        jok = True
    except Exception:
        jok = False
    check(g, "bad JSON -> exit 2 + JSON error", ok and jok, r.stderr[:60])
    r2 = sh([SCRIPT, "nonexistent"])
    check(g, "unknown subcommand -> non-zero", r2.returncode != 0)
    r3 = sh([SCRIPT, "--help"])
    check(g, "--help works", r3.returncode == 0 and "holland" in r3.stdout and "match" in r3.stdout)


def main():
    for fn in (g1_frontmatter, g2_no_phantoms, g3_holland, g4_match, g5_salary,
               g6_report, g7_db_integrity, g8_scrape_samples, g9_insurance,
               g10_references, g11_cli_contract):
        fn()
    total = len(RESULTS)
    fails = [r for r in RESULTS if not r[2]]
    groups = {}
    for gr, name, ok, det in RESULTS:
        groups.setdefault(gr, [0, 0])
        groups[gr][0] += 1
        groups[gr][1] += 0 if ok else 1
    for gr in sorted(groups):
        n, f = groups[gr]
        print(f"[{'PASS' if f == 0 else 'FAIL'}] {gr}: {n - f}/{n}")
        for g2, name, ok, det in RESULTS:
            if g2 == gr and not ok:
                print(f"    ✗ {name} {('— ' + det) if det else ''}")
    print(f"\n{total - len(fails)}/{total} checks passed")
    if fails:
        print("SELFTEST FAILED")
        sys.exit(1)
    print("ALL CHECKS PASSED")
    sys.exit(0)


if __name__ == "__main__":
    main()
