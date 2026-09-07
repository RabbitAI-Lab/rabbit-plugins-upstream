#!/usr/bin/env python3
"""selftest.py — cyberscope v2.0.0 离线自检（确定性、无网络）

运行：python3 scripts/selftest.py  （全部 PASS 才可交付）
组：G1 数据完整性 · G2 搜索语义 · G3 method/categories/stats · G4 导出确定性
    G5 校验和 · G6 verify-sources · G7 catalog-report · G8 退出码纪律
    G9 仅标准库 · G10 文档幻影
"""
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TOOL = os.path.join(HERE, "cyberscope.py")
CATALOG = os.path.join(ROOT, "data", "catalog.json")
T1 = tempfile.mkdtemp(prefix="cyself_")
RESULTS = []

# 数据保真锚点（由 v1.0.0 src/lib/seed-data.ts 移植时计算，见 references/catalog_schema.md）
METHODS_CANON = "32e47ddadd169a9af554f42fdd459fd658d64ec65f8294df23754c0c5b7e03ea"
RESOURCES_CANON = "62c22f3b51e27073b5ad6ef54d66c90cee7c28081203696fdb796a8eeb41001e"
N_CAT, N_METHOD, N_RES = 10, 62, 83
N_SOURCES = 45
SINGLE_SOURCE_COUNT = 43
DUP_URL = "https://freedomhouse.org/report/freedom-net"
COMMERCIAL_WARN_MNS = [9, 20, 24, 25, 36, 45, 46]
SLASH_WARN_MNS = [30, 48]


def check(group, name, ok, dbg=""):
    RESULTS.append((group, name, bool(ok), dbg))


def run(*args):
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True, timeout=120)


def jout(r):
    return json.loads(r.stdout) if r.stdout.strip() else None


def jerr(r):
    return json.loads(r.stderr) if r.stderr.strip() else None


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    cat = json.load(open(CATALOG, encoding="utf-8"))

    # ── G1 数据完整性 ────────────────────────────────────────────────────
    g = "G1-data-integrity"
    check(g, "10 类目", len(cat["categories"]) == N_CAT)
    check(g, "62 方法", len(cat["methods"]) == N_METHOD)
    check(g, "83 资源", len(cat["resources"]) == N_RES)
    nums = [m["methodNumber"] for m in cat["methods"]]
    check(g, "方法号 1..62 唯一有序", nums == list(range(1, 63)))
    slugs = [c["slug"] for c in cat["categories"]]
    check(g, "类目 slug 唯一", len(set(slugs)) == N_CAT)
    check(g, "资源外键全在 1..62", all(1 <= r["methodNumber"] <= 62 for r in cat["resources"]))
    check(g, "每方法 ≥1 资源", all(any(r["methodNumber"] == mn for r in cat["resources"]) for mn in nums))
    check(g, "全部 URL 为 https", all(r["url"].startswith("https://") for r in cat["resources"]))
    check(g, "45 个不同来源", len({r["source"] for r in cat["resources"]}) == N_SOURCES)

    def canon_methods(c):
        return sha("".join("%d|%s|%s|%s\n" % (m["methodNumber"], m["title"], m["description"],
                                              ",".join(sorted(m["keywords"]))) for m in c["methods"]).encode())

    def canon_resources(c):
        return sha("".join("%d|%s|%s|%s|%s\n" % (r["methodNumber"], r["title"], r["url"],
                                                 r["source"], r["resourceType"]) for r in c["resources"]).encode())
    check(g, "方法规范摘要=锚点", canon_methods(cat) == METHODS_CANON)
    check(g, "资源规范摘要=锚点", canon_resources(cat) == RESOURCES_CANON)
    check(g, "catalog 字段齐", all(set(m) == {"methodNumber", "categorySlug", "title", "description", "keywords"}
                                  for m in cat["methods"])
          and all(set(r) == {"methodNumber", "title", "url", "source", "resourceType", "description"}
                  for r in cat["resources"]))

    # ── G2 搜索语义 ──────────────────────────────────────────────────────
    g = "G2-search-semantics"
    d = jout(run("search", "ransomware"))
    check(g, "ransomware: top1=m50 score=2450, total=2",
          d["total"] == 2 and d["results"][0]["id"] == 50 and d["results"][0]["score"] == 2450
          and d["results"][1]["id"] == 27, json.dumps(d["results"])[:160])
    d = jout(run("search", "solarwinds"))
    check(g, "solarwinds: 仅 keywords 命中 m13（v1 召回缺失修复）",
          d["total"] == 1 and d["results"][0]["id"] == 13 and d["results"][0]["score"] == 500)
    d = jout(run("search", "pegasus"))
    check(g, "pegasus: keywords 命中 m47", d["total"] == 1 and d["results"][0]["id"] == 47)
    d = jout(run("search", "living off the land"))
    check(g, "living off the land: AND+短语, top1=m17", d["results"][0]["id"] == 17
          and d["results"][0]["score"] > 3000)
    d = jout(run("search", "zzzqqqxx"))
    check(g, "0 命中: rc0 空结果", d["total"] == 0 and d["results"] == [])
    d = jout(run("search", "vpn", "--category", "censorship-control"))
    check(g, "类目过滤: vpn@censorship = [36,35]", [r["id"] for r in d["results"]] == [36, 35])
    d = jout(run("search", "surveillance"))
    scores = [r["score"] for r in d["results"]]
    ids = [r["id"] for r in d["results"]]
    ok = all(scores[i] >= scores[i + 1] for i in range(len(scores) - 1))
    tie_ok = all((scores[i] > scores[i + 1]) or (scores[i] == scores[i + 1] and ids[i] < ids[i + 1])
                 for i in range(len(scores) - 1))
    check(g, "评分降序且平局按 id 升序（属性测试）", ok and tie_ok and d["total"] > 3)
    d = jout(run("search", "ransomware", "--fields", "all"))
    r0 = d["results"][0]
    check(g, "--fields all 带 description/keywords/resources",
          "description" in r0 and "keywords" in r0 and "resources" in r0 and len(r0["resources"]) >= 1)
    d = jout(run("search", "ransomware"))
    check(g, "--fields basic 默认不带回 description", "description" not in d["results"][0])
    d = jout(run("search", "ransomware", "--limit", "1"))
    check(g, "--limit 1: 截断但 total 保留", d["n_results"] == 1 and d["total"] == 2 and d["results"][0]["id"] == 50)
    d = jout(run("search", "dns", "poisoning", "--fields", "all"))
    check(g, "未加引号多词查询自动连接（LLM 常见误用）",
          d["query"] == "dns poisoning" and d["total"] == 1 and d["results"][0]["id"] == 30)
    d = jout(run("search", "ddos"))
    check(g, "大小写/缩写不敏感: ddos 命中 m25", any(r["id"] == 25 for r in d["results"]))

    # ── G3 method/categories/stats ───────────────────────────────────────
    g = "G3-method-categories-stats"
    d = jout(run("method", "1"))
    check(g, "method 1: 3 资源", d["method"]["id"] == 1 and len(d["method"]["resources"]) == 3
          and d["method"]["category"] == "mass-data-collection")
    d = jout(run("method", "wiper"))
    check(g, "method wiper: 唯一子串 → m27", d["method"]["id"] == 27)
    r = run("method", "supply chain")
    check(g, "method 'supply chain': 歧义 rc2 + candidates",
          r.returncode == 2 and jerr(r)["candidates"] == [12, 13] and r.stdout == "")
    r = run("method", "999")
    check(g, "method 999: rc2", r.returncode == 2 and jerr(r) is not None)
    r = run("method", "nonexistent-zzz")
    check(g, "method 无匹配子串: rc2", r.returncode == 2)
    d = jout(run("categories"))
    check(g, "categories: 10 条 count 和=62", d["n_categories"] == 10
          and sum(c["count"] for c in d["categories"]) == 62
          and [c["numeral"] for c in d["categories"]] == ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"])
    d = jout(run("stats"))
    check(g, "stats: 计数一致", d["n_methods"] == 62 and d["n_resources"] == 83
          and sum(d["methods_per_category"].values()) == 62
          and sum(d["resources_per_type"].values()) == 83
          and d["single_source_method_count"] == SINGLE_SOURCE_COUNT)

    # ── G4 导出确定性 ────────────────────────────────────────────────────
    g = "G4-export-determinism"
    r1 = run("export", "--format", "json", "--out", T1 + "/e1")
    r2 = run("export", "--format", "json", "--out", T1 + "/e2")
    b1 = open(T1 + "/e1/catalog.json", "rb").read()
    b2 = open(T1 + "/e2/catalog.json", "rb").read()
    check(g, "json 双跑字节一致", b1 == b2 and jout(r1)["bytes"] == len(b1))
    check(g, "json 导出=源文件字节", b1 == open(CATALOG, "rb").read())
    run("export", "--format", "csv", "--out", T1)
    rows = list(csv.reader(open(T1 + "/methods.csv", encoding="utf-8")))
    check(g, "csv: 63 行(表头+62), 列名固定",
          len(rows) == 63 and rows[0] == ["methodNumber", "title", "category_slug", "category_name",
                                          "description", "keywords", "resources"])
    check(g, "csv: 第 1 行 methodNumber=1 且 resources 非空",
          rows[1][0] == "1" and "https://" in rows[1][6])
    run("export", "--format", "md", "--out", T1)
    md = open(T1 + "/catalog.md", encoding="utf-8").read()
    check(g, "md: 10 个 ## 类目 + 62 个 ### 方法",
          len(re.findall(r"^## ", md, re.M)) == 10 and len(re.findall(r"^### \d+\. ", md, re.M)) == 62
          and md.count("https://") == N_RES)
    r = run("export", "--format", "csv")
    check(g, "export 无 --out: rc2", r.returncode == 2 and jerr(r) is not None)

    # ── G5 校验和 ────────────────────────────────────────────────────────
    g = "G5-checksums"
    d = jout(run("checksums"))
    check(g, "file_sha256 与文件一致", d["file_sha256"] == sha(open(CATALOG, "rb").read()))
    check(g, "方法规范摘要=锚点", d["methods_canon_sha256"] == METHODS_CANON)
    check(g, "资源规范摘要=锚点", d["resources_canon_sha256"] == RESOURCES_CANON)
    check(g, "计数 10/62/83", (d["n_categories"], d["n_methods"], d["n_resources"]) == (10, 62, 83))

    # ── G6 verify-sources ────────────────────────────────────────────────
    g = "G6-verify-sources"
    r = run("verify-sources")
    d = jout(r)
    check(g, "0 ERR（数据全 https/可解析）", d["n_errors"] == 0 and r.returncode == 0)
    check(g, "9 WARN = 7 商业 + 2 ATT&CK 斜杠",
          d["n_warnings"] == 9
          and sorted(i["methodNumber"] for i in d["issues"] if i["code"] == "COMMERCIAL_DOMAIN") == COMMERCIAL_WARN_MNS
          and sorted(i["methodNumber"] for i in d["issues"] if i["code"] == "ATTACK_SLASH_FORMAT") == SLASH_WARN_MNS)
    check(g, "limits 声明存在（诚实边界）", "不探测 HTTP" in d["limits"])
    # 结构违规 → rc3（构造坏 catalog）
    bad = json.loads(open(CATALOG, encoding="utf-8").read())
    bad["resources"][0] = dict(bad["resources"][0], url="http://insecure.example/")
    bp = T1 + "/bad_catalog"
    os.makedirs(bp, exist_ok=True)
    json.dump(bad, open(bp + "/catalog.json", "w", encoding="utf-8"))
    # 通过临时目录复制工具以指向坏 catalog：改路径不可行 → 用 env 覆盖
    r = subprocess.run([sys.executable, TOOL, "verify-sources"], capture_output=True, text=True,
                       timeout=120, env={**os.environ, "CYBERSCOPE_CATALOG": bp + "/catalog.json"})
    check(g, "非 https URL → ERR rc3", r.returncode == 3
          and any(i["code"] == "SCHEME" for i in jout(r)["issues"]))

    # ── G7 catalog-report ────────────────────────────────────────────────
    g = "G7-catalog-report"
    d = jout(run("catalog-report"))
    check(g, "单源方法 44 个", d["single_source_count"] == SINGLE_SOURCE_COUNT
          and len(d["single_source_methods"]) == SINGLE_SOURCE_COUNT)
    check(g, "重复 URL 恰 1 个 (freedomhouse: m33+m41)",
          d["duplicate_urls"] == {DUP_URL: [33, 41]})
    check(g, "ATT&CK 斜杠格式 [m30,m48]", [s["methodNumber"] for s in d["attack_slash_format"]] == SLASH_WARN_MNS)
    check(g, "分布和一致", sum(d["distribution"]["methods_per_category"].values()) == 62
          and sum(d["distribution"]["resources_per_type"].values()) == 83)
    check(g, "建议全部带 methodNumber+action+reason",
          all(set(x) == {"methodNumber", "action", "reason"} for x in d["recommendations"])
          and d["n_recommendations"] == len(d["recommendations"]))

    # ── G8 退出码纪律 ────────────────────────────────────────────────────
    g = "G8-exit-discipline"
    r = run("search", "x", "--category", "nope-slug")
    check(g, "未知类目: rc2 + stderr JSON + stdout 空",
          r.returncode == 2 and jerr(r) is not None and r.stdout == "")
    r = run("search", "x", "--limit", "999")
    check(g, "超范围 limit: rc2", r.returncode == 2)
    r = run("search", "")
    check(g, "空查询: rc2", r.returncode == 2)
    r = run("categories")
    check(g, "正常命令: rc0 且 stderr 空", r.returncode == 0 and r.stderr == "")
    e = jerr(run("search", "x", "--category", "nope-slug"))
    check(g, "错误 JSON 含 tool+error", "tool" in e and "error" in e and e["tool"].endswith("v2.0.0"))
    for cmd in (["categories"], ["stats"], ["checksums"], ["verify-sources"], ["catalog-report"],
                ["method", "1"], ["search", "dns"]):
        r = run(*cmd)
        try:
            d = json.loads(r.stdout)
            ok = d["tool"] == "cyberscope v2.0.0" and "command" in d
        except Exception:
            ok = False
        check(g, "单行 JSON + tool + command: " + cmd[0], ok)

    # ── G9 仅标准库 ──────────────────────────────────────────────────────
    g = "G9-stdlib-only"
    allowed = {"argparse", "csv", "hashlib", "io", "json", "os", "re", "sys",
               "urllib", "filecmp", "shutil", "subprocess", "tempfile"}
    for f in ("cyberscope.py", "selftest.py"):
        src = open(os.path.join(HERE, f)).read()
        bad = []
        for l in src.splitlines():
            m = re.match(r"^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_]*)", l)
            if m and m.group(1) not in allowed:
                bad.append(m.group(1))
        check(g, f + " 无第三方导入", not bad, str(bad))
    check(g, "无联网调用", not re.search(r"^\s*(?:import|from)\s+(?:requests|socket|http\.client)",
                                         open(TOOL).read(), re.M))

    # ── G10 文档幻影 ─────────────────────────────────────────────────────
    g = "G10-doc-phantoms"
    sk = open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8").read()
    help_txt = run("--help").stdout
    for cmd in ("search", "categories", "method", "stats", "export", "checksums",
                "verify-sources", "catalog-report"):
        check(g, "命令存在: " + cmd, cmd in sk and cmd in help_txt)
    for flag in ("--category", "--limit", "--fields", "--format", "--out"):
        check(g, "标志存在: " + flag, flag in sk and flag in help_txt)
    for ref in ("catalog_schema.md", "search_scoring.md", "source_verification.md"):
        p = os.path.join(ROOT, "references", ref)
        check(g, "参考存在: " + ref, os.path.exists(p) and "供参考" in open(p, encoding="utf-8").read())
    check(g, "SKILL 硬规则措辞", ("只读" in sk) and (("参考性" in sk) or ("reference" in sk.lower())))
    check(g, "版本一致 2.0.0", "2.0.0" in sk and "cyberscope v2.0.0" in open(TOOL).read())

    # ── 汇总 ─────────────────────────────────────────────────────────────
    total = len(RESULTS)
    fails = [x for x in RESULTS if not x[2]]
    for grp, name, ok, dbg in fails:
        print("FAIL %s :: %s %s" % (grp, name, dbg))
    print("selftest: %d/%d PASS" % (total - len(fails), total))
    shutil.rmtree(T1, ignore_errors=True)
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
