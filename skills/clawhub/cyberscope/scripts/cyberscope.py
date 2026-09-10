#!/usr/bin/env python3
"""cyberscope.py — CyberScope v2.0.0 参考目录 CLI（纯标准库、离线、确定性）

数据源：data/catalog.json（10 类目 / 62 方法 / 83 来源，唯一数据源）。
命令：search · categories · method · stats · export · checksums ·
      verify-sources · catalog-report
契约：stdout 单行 JSON（数据）· stderr 单行 JSON（错误）·
      退出码 0=ok · 2=输入错误 · 3=结构性数据违规。
"""
import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
from urllib.parse import urlparse

TOOL = "cyberscope v2.0.0"
HERE = os.path.dirname(os.path.abspath(__file__))
CATALOG_PATH = os.environ.get("CYBERSCOPE_CATALOG") or os.path.join(HERE, "..", "data", "catalog.json")

# 评分权重（整数、确定性；详见 references/search_scoring.md）
W_TITLE = 1000
W_KEYWORD = 500
W_DESC = 200
W_RES_TITLE = 100
W_RES_DESC = 50
PHRASE_BONUS_TITLE = 500
PHRASE_BONUS_RES_TITLE = 100

# 机构域名白名单（verify-sources 域分类用；其余按 TLD 启发式，商业域名仅 warn）
INSTITUTION_HOSTS = {
    "attack.mitre.org", "attackevals.mitre-engenuity.org", "cisa.gov", "csrc.nist.gov",
    "nvd.nist.gov", "www.nist.gov", "nist.gov", "eff.org", "owasp.org", "sans.org",
    "fcc.gov", "icann.org", "torproject.org", "freedomhouse.org", "privacyinternational.org",
    "amnesty.org", "netblocks.org", "accessnow.org", "citizenlab.ca", "opennet.net",
    "ooni.org", "explorer.ooni.org", "censoredplanet.org", "iclab.org", "ripe.net",
    "bgpstream.caida.org", "pulse.internetsociety.org", "internetsociety.org",
    "itu.int", "educause.edu", "sei.cmu.edu", "kb.cert.org", "first.org",
    "cisecurity.org", "manrs.org", "submarinecablemap.com", "schneier.com",
    "apwg.org", "securityscorecards.dev", "lolbas-project.github.io",
    "cyber.fsi.stanford.edu", "ccdcoe.org", "intgovforum.org",
}
EDU_TLDS = (".edu", ".edu.", ".ac.")


def emit(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n")


def err(code, message, **extra):
    out = {"status": "error", "tool": TOOL, "error": message}
    out.update(extra)
    sys.stderr.write(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n")
    sys.exit(code)


def load_catalog(path=None):
    p = path or CATALOG_PATH
    try:
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        err(2, "catalog 文件不存在: %s" % os.path.abspath(p))
    except json.JSONDecodeError as e:
        err(3, "catalog JSON 解析失败: %s" % e)


def norm(s):
    """归一化：小写；- _ & 视为空格；空白折叠。"""
    s = s.lower().replace("-", " ").replace("_", " ").replace("&", " ")
    return re.sub(r"\s+", " ", s).strip()


def tokens(s):
    return norm(s).split()


# ── search ────────────────────────────────────────────────────────────────
def build_index(cat):
    idx = []
    for m in cat["methods"]:
        res = method_resources(cat, m["methodNumber"])
        idx.append({
            "method": m,
            "n_title": norm(m["title"]),
            "n_kw": norm(" ".join(m["keywords"])),
            "n_desc": norm(m["description"]),
            "n_res_title": " ".join(norm(r["title"]) for r in res),
            "n_res_desc": " ".join(norm(r["description"]) for r in res),
        })
    return idx



def score_method(entry, toks, phrase):
    score = 0
    hit = {t: 0 for t in toks}
    for t in set(toks):
        if t in entry["n_title"]:
            hit[t] += W_TITLE
        if t in entry["n_kw"]:
            hit[t] += W_KEYWORD
        if t in entry["n_desc"]:
            hit[t] += W_DESC
        if t in entry["n_res_title"]:
            hit[t] += W_RES_TITLE
        if t in entry["n_res_desc"]:
            hit[t] += W_RES_DESC
    if any(v == 0 for v in hit.values()):
        return None  # AND 语义：每个 token 必须命中至少一个字段
    score = sum(hit.values())
    if phrase:
        if phrase in entry["n_title"]:
            score += PHRASE_BONUS_TITLE
        if phrase in entry["n_res_title"]:
            score += PHRASE_BONUS_RES_TITLE
    return score


def method_resources(cat, method_number):
    return [r for r in cat["resources"] if r["methodNumber"] == method_number]


def cmd_search(args):
    cat = load_catalog()
    by_slug = {c["slug"]: c for c in cat["categories"]}
    if args.category and args.category not in by_slug:
        err(2, "未知 category slug: %s（可用: %s）" % (args.category,
             ", ".join(c["slug"] for c in cat["categories"])))
    if not (1 <= args.limit <= 62):
        err(2, "--limit 必须在 1..62")
    if isinstance(args.q, list):
        args.q = " ".join(args.q)
    toks = tokens(args.q)
    if not toks:
        err(2, "查询为空")
    phrase = " ".join(toks)
    idx = build_index(cat)
    hits = []
    for e in idx:
        if args.category and e["method"]["categorySlug"] != args.category:
            continue
        s = score_method(e, toks, phrase)
        if s is not None:
            hits.append((s, e["method"]["methodNumber"], e["method"]))
    hits.sort(key=lambda x: (-x[0], x[1]))
    total = len(hits)
    hits = hits[: args.limit]
    results = []
    for s, mn, m in hits:
        c = by_slug[m["categorySlug"]]
        r = {"id": mn, "title": m["title"], "category": c["slug"],
             "category_name": c["name"], "score": s}
        if args.fields == "all":
            r["description"] = m["description"]
            r["keywords"] = m["keywords"]
            r["resources"] = method_resources(cat, mn)
        results.append(r)
    emit({"command": "search", "tool": TOOL, "query": args.q,
          "category": args.category or None, "n_results": len(results),
          "total": total, "limit": args.limit, "results": results})
    sys.exit(0)


def cmd_categories(args):
    cat = load_catalog()
    counts = {}
    for m in cat["methods"]:
        counts[m["categorySlug"]] = counts.get(m["categorySlug"], 0) + 1
    rows = [{"numeral": c["numeral"], "slug": c["slug"], "name": c["name"],
             "count": counts.get(c["slug"], 0)} for c in sorted(cat["categories"], key=lambda c: c["sortOrder"])]
    emit({"command": "categories", "tool": TOOL, "n_categories": len(rows),
          "n_methods": len(cat["methods"]), "categories": rows})
    sys.exit(0)


def cmd_method(args):
    cat = load_catalog()
    sel = args.ref.strip()
    matches = None
    if re.fullmatch(r"\d+", sel):
        n = int(sel)
        matches = [m for m in cat["methods"] if m["methodNumber"] == n]
        if not matches:
            err(2, "方法号 %d 不存在（范围 1..62）" % n)
    else:
        q = norm(sel)
        matches = [m for m in cat["methods"] if q in norm(m["title"])]
        if not matches:
            err(2, "标题子串无匹配: %s" % sel,
                hint="用数字方法号（1..62），见 `categories` / `search`")
        if len(matches) > 1:
            err(2, "标题子串歧义（%d 个匹配）" % len(matches),
                candidates=[m["methodNumber"] for m in matches],
                titles=[m["title"] for m in matches])
    m = matches[0]
    by_slug = {c["slug"]: c for c in cat["categories"]}
    c = by_slug[m["categorySlug"]]
    emit({"command": "method", "tool": TOOL,
          "method": {"id": m["methodNumber"], "title": m["title"],
                     "category": c["slug"], "category_name": c["name"],
                     "description": m["description"], "keywords": m["keywords"],
                     "resources": method_resources(cat, m["methodNumber"])}})
    sys.exit(0)


def cmd_stats(args):
    cat = load_catalog()
    per_cat = {}
    for m in cat["methods"]:
        per_cat[m["categorySlug"]] = per_cat.get(m["categorySlug"], 0) + 1
    per_type = {}
    for r in cat["resources"]:
        per_type[r["resourceType"]] = per_type.get(r["resourceType"], 0) + 1
    single = sum(1 for mn in {m["methodNumber"] for m in cat["methods"]}
                 if len(method_resources(cat, mn)) == 1)
    emit({"command": "stats", "tool": TOOL,
          "n_categories": len(cat["categories"]), "n_methods": len(cat["methods"]),
          "n_resources": len(cat["resources"]),
          "n_sources": len({r["source"] for r in cat["resources"]}),
          "methods_per_category": dict(sorted(per_cat.items())),
          "resources_per_type": dict(sorted(per_type.items())),
          "single_source_method_count": single})
    sys.exit(0)


# ── export ────────────────────────────────────────────────────────────────
def export_json(cat):
    return json.dumps(cat, ensure_ascii=False, indent=1, sort_keys=False) + "\n"


def export_csv(cat):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["methodNumber", "title", "category_slug", "category_name",
                "description", "keywords", "resources"])
    by_slug = {c["slug"]: c for c in cat["categories"]}
    for m in sorted(cat["methods"], key=lambda x: x["methodNumber"]):
        c = by_slug[m["categorySlug"]]
        urls = ";".join(r["url"] for r in method_resources(cat, m["methodNumber"]))
        w.writerow([m["methodNumber"], m["title"], c["slug"], c["name"],
                    m["description"], "|".join(m["keywords"]), urls])
    return buf.getvalue()


def export_md(cat):
    by_slug = {c["slug"]: c for c in cat["categories"]}
    L = ["# CyberScope Catalog — 62 methods / 10 categories", ""]
    for c in sorted(cat["categories"], key=lambda x: x["sortOrder"]):
        n = sum(1 for m in cat["methods"] if m["categorySlug"] == c["slug"])
        L.append("## %s. %s (%s, %d methods)" % (c["numeral"], c["name"], c["slug"], n))
        L.append("")
        for m in sorted((m for m in cat["methods"] if m["categorySlug"] == c["slug"]),
                        key=lambda x: x["methodNumber"]):
            L.append("### %d. %s" % (m["methodNumber"], m["title"]))
            L.append("")
            L.append(m["description"])
            L.append("")
            L.append("**Keywords:** %s" % ", ".join(m["keywords"]))
            L.append("")
            for r in method_resources(cat, m["methodNumber"]):
                L.append("- [%s](%s) — %s (%s)" % (r["title"], r["url"], r["source"], r["resourceType"]))
            L.append("")
    return "\n".join(L) + "\n"


def cmd_export(args):
    cat = load_catalog()
    if args.format == "json":
        name, content = "catalog.json", export_json(cat)
    elif args.format == "csv":
        name, content = "methods.csv", export_csv(cat)
    else:
        name, content = "catalog.md", export_md(cat)
    outdir = args.out
    if not outdir:
        err(2, "export 需要 --out DIR（保持 stdout=JSON 契约）")
    os.makedirs(outdir, exist_ok=True)
    p = os.path.join(outdir, name)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    emit({"command": "export", "tool": TOOL, "format": args.format,
          "file": p, "bytes": len(content.encode("utf-8"))})
    sys.exit(0)


# ── checksums ─────────────────────────────────────────────────────────────
def methods_canon(cat):
    s = "".join("%d|%s|%s|%s\n" % (m["methodNumber"], m["title"], m["description"],
                                   ",".join(sorted(m["keywords"]))) for m in cat["methods"])
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def resources_canon(cat):
    s = "".join("%d|%s|%s|%s|%s\n" % (r["methodNumber"], r["title"], r["url"],
                                      r["source"], r["resourceType"]) for r in cat["resources"])
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def cmd_checksums(args):
    p = os.path.abspath(CATALOG_PATH)
    raw = open(p, "rb").read()
    cat = json.loads(raw.decode("utf-8"))
    emit({"command": "checksums", "tool": TOOL,
          "file": os.path.relpath(p, HERE),
          "file_sha256": hashlib.sha256(raw).hexdigest(),
          "methods_canon_sha256": methods_canon(cat),
          "resources_canon_sha256": resources_canon(cat),
          "n_categories": len(cat["categories"]),
          "n_methods": len(cat["methods"]),
          "n_resources": len(cat["resources"])})
    sys.exit(0)


# ── verify-sources（纯静态，不联网）──────────────────────────────────────
ATTACK_TECH_RE = re.compile(r"attack\.mitre\.org/techniques/(T\d{4})([/\.])(\d{3})/")


def check_url(url):
    """返回 (severity, code, detail) 列表。ERR=结构性违规，WARN=建议项。"""
    issues = []
    if not url.startswith("https://"):
        issues.append(("ERR", "SCHEME", "非 https URL"))
        return issues
    u = urlparse(url)
    host = (u.hostname or "").lower()
    if not host:
        issues.append(("ERR", "HOST_EMPTY", "无主机名"))
        return issues
    if any(ch.isspace() for ch in host) or not host.isascii():
        issues.append(("ERR", "HOST_CHAR", "主机名含非法字符"))
    if u.port is not None:
        issues.append(("WARN", "PORT", "显式端口 :%d（规范 https 默认 443）" % u.port))
    path = u.path or "/"
    if "%00" in url.lower():
        issues.append(("WARN", "NULL_ENCODED", "路径含 %00"))
    if "//" in path:
        issues.append(("WARN", "DOUBLE_SLASH", "路径含连续 //"))
    if "\\" in url:
        issues.append(("WARN", "BACKSLASH", "URL 含反斜杠"))
    # 域分类（allowlist 按裸主机名匹配：www. 前缀不视为不同域）
    bare = host[4:] if host.startswith("www.") else host
    if bare in INSTITUTION_HOSTS or host.endswith((".gov", ".gov.uk", ".gov.au", ".edu", ".ac.", ".int")):
        cls = "institution"
    elif host.endswith(".org"):
        cls = "org"
    elif host.endswith((".com", ".net", ".io", ".dev", ".ca")):
        cls = "commercial"
        issues.append(("WARN", "COMMERCIAL_DOMAIN", "商业域名来源（信息性，非违规）"))
    else:
        cls = "other"
    # ATT&CK 子技术 URL 格式：规范为点号 T1234.005
    am = ATTACK_TECH_RE.search(url)
    if am and am.group(2) == "/":
        issues.append(("WARN", "ATTACK_SLASH_FORMAT",
                       "ATT&CK 子技术 URL 用斜杠（规范为 %s.%s 点号形式）" % (am.group(1), am.group(3))))
    return issues


def cmd_verify_sources(args):
    cat = load_catalog()
    n_error = n_warn = 0
    issues = []
    for r in cat["resources"]:
        for sev, code, detail in check_url(r["url"]):
            if sev == "ERR":
                n_error += 1
            else:
                n_warn += 1
            issues.append({"methodNumber": r["methodNumber"], "url": r["url"],
                           "code": code, "severity": sev, "detail": detail})
    emit({"command": "verify-sources", "tool": TOOL,
          "n_resources": len(cat["resources"]),
          "n_errors": n_error, "n_warnings": n_warn,
          "n_clean": len(cat["resources"]) - len({(i["methodNumber"], i["url"]) for i in issues}),
          "issues": issues,
          "limits": "纯静态检查（scheme/host/路径/域分类/ATT&CK 格式）；不探测 HTTP，不证明链接存活或内容正确"})
    sys.exit(3 if n_error else 0)


# ── catalog-report（自改进钩子）───────────────────────────────────────────
def cmd_report(args):
    cat = load_catalog()
    mns = sorted(m["methodNumber"] for m in cat["methods"])
    single = [mn for mn in mns if len(method_resources(cat, mn)) == 1]
    url_map = {}
    for r in cat["resources"]:
        url_map.setdefault(r["url"], []).append(r["methodNumber"])
    dups = {u: sorted(v) for u, v in sorted(url_map.items()) if len(v) > 1}
    slash = [{"methodNumber": r["methodNumber"], "url": r["url"]}
             for r in cat["resources"]
             if ATTACK_TECH_RE.search(r["url"]) and ATTACK_TECH_RE.search(r["url"]).group(2) == "/"]
    per_cat = {}
    for m in cat["methods"]:
        per_cat[m["categorySlug"]] = per_cat.get(m["categorySlug"], 0) + 1
    per_type = {}
    for r in cat["resources"]:
        per_type[r["resourceType"]] = per_type.get(r["resourceType"], 0) + 1
    n_commercial = sum(1 for r in cat["resources"]
                       if check_url(r["url"]) and any(c == "COMMERCIAL_DOMAIN" for _, c, _ in check_url(r["url"])))
    recs = ([{"methodNumber": mn, "action": "add_source",
              "reason": "仅 1 个来源，建议补充独立来源（另一机构或不同类型）"} for mn in single]
            + [{"methodNumber": mn, "action": "dedupe_or_keep",
                "reason": "URL 与方法 %s 重复使用；保留其一或改换更精确来源" % ", ".join(map(str, v))}
               for u, v in dups.items() for mn in v]
            + [{"methodNumber": s["methodNumber"], "action": "fix_attack_url_format",
                "reason": "ATT&CK 子技术 URL 应改为点号形式（如 T1195.002）"} for s in slash])
    emit({"command": "catalog-report", "tool": TOOL,
          "n_methods": len(mns), "n_resources": len(cat["resources"]),
          "single_source_methods": single,
          "single_source_count": len(single),
          "duplicate_urls": dups,
          "attack_slash_format": slash,
          "distribution": {"methods_per_category": dict(sorted(per_cat.items())),
                           "resources_per_type": dict(sorted(per_type.items())),
                           "commercial_sources": n_commercial},
          "n_recommendations": len(recs),
          "recommendations": recs})
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(
        prog="cyberscope.py", description=TOOL + "（纯标准库、离线、确定性；参考目录：10 类目 / 62 方法 / 83 来源）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="flags:\n"
               "  search Q... [--category SLUG] [--limit N] [--fields basic|all]  # Q 可多词免引号\n"
               "  method N|标题子串        categories\n"
               "  stats                   export --format json|csv|md [--out DIR]\n"
               "  checksums               verify-sources\n"
               "  catalog-report\n"
               "exit: 0 ok | 2 输入错误(stderr 单行 JSON) | 3 结构性数据违规")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("search", help="加权全文搜索（title>keywords>description>resources）")
    sp.add_argument("q", nargs="+", help="查询词（可多词免引号，空格连接）")
    sp.add_argument("--category", default=None, help="类目 slug 过滤")
    sp.add_argument("--limit", type=int, default=10)
    sp.add_argument("--fields", choices=["basic", "all"], default="basic")
    sp.set_defaults(fn=cmd_search)

    sp = sub.add_parser("categories", help="10 类目 + 计数")
    sp.set_defaults(fn=cmd_categories)

    sp = sub.add_parser("method", help="单条完整记录 + 全部资源")
    sp.add_argument("ref", help="方法号 1..62 或标题子串（歧义时 exit 2 + candidates）")
    sp.set_defaults(fn=cmd_method)

    sp = sub.add_parser("stats", help="计数/分布/覆盖")
    sp.set_defaults(fn=cmd_stats)

    sp = sub.add_parser("export", help="全量导出 json|csv|md（确定性字节）")
    sp.add_argument("--format", choices=["json", "csv", "md"], required=True)
    sp.add_argument("--out", default=None, help="输出目录；缺省时内容走 stdout")
    sp.set_defaults(fn=cmd_export)

    sp = sub.add_parser("checksums", help="数据完整性锚点（文件 sha + 规范摘要 sha）")
    sp.set_defaults(fn=cmd_checksums)

    sp = sub.add_parser("verify-sources", help="83 个来源 URL 的纯静态检查（不联网）")
    sp.set_defaults(fn=cmd_verify_sources)

    sp = sub.add_parser("catalog-report", help="目录质量报告 + 可执行建议（自改进钩子）")
    sp.set_defaults(fn=cmd_report)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
