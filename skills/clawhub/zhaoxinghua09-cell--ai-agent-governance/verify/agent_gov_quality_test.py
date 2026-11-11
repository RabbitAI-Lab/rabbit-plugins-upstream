#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""agent_gov_quality_test.py — AI 智能体治理 质量与安全稳定性验证（本地闭环、零网络）"""

import json, os, re, subprocess, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILL_MD = os.path.join(BASE, "SKILL.md")
TOOL = os.path.join(BASE, "tools", "agent_gov_toolkit.py")
REFS = os.path.join(BASE, "references")
VERIFY = os.path.join(BASE, "verify")
PYTHON = sys.executable


def check_regulatory_timeliness():
    items = []
    try:
        cn = open(os.path.join(REFS, "05-Agent监管与合规.md"), encoding="utf-8").read()
        checks = [
            ("中国 2026-05 智能体政策", "2026-05" in cn and "智能体规范应用与创新发展实施意见" in cn),
            ("防越权/逃逸/滥用", all(k in cn for k in ["越权", "逃逸", "滥用"])),
            ("新加坡 Agentic AI 2026-05", "2026-05" in cn and "Agentic" in cn),
            ("NIST AI Agent 倡议 2026-01", "2026-01" in cn),
            ("欧盟 AI Act 延伸", "AI Act" in cn),
            ("核对基准日", "核对基准日" in cn),
        ]
        items = [{"name": n, "pass": p} for n, p in checks]
    except OSError as e:
        items = [{"name": f"读取失败: {e}", "pass": False}]
    return items


def check_coverage():
    items = []
    try:
        nav = open(SKILL_MD, encoding="utf-8").read()
        files = sorted(f for f in os.listdir(REFS) if f.endswith(".md"))
        items.append({"name": f"references 模块数=7（实际 {len(files)}）", "pass": len(files) == 7})
        for f in files:
            items.append({"name": f"导航表包含 {f}", "pass": f in nav})
        items.append({"name": "FAQ 专节存在", "pass": "FAQ" in nav})
        items.append({"name": "能力边界", "pass": "能力边界" in nav})
    except OSError as e:
        items = [{"name": f"读取失败: {e}", "pass": False}]
    return items


def check_tools():
    items = []
    try:
        r = subprocess.run([PYTHON, TOOL, "risk", "--agent", "客户服务Agent，可访问CRM、可发邮件、可下订单"],
                           capture_output=True, text=True, timeout=60)
        out = r.stdout or ""
        items.append({"name": "risk 命令执行", "pass": r.returncode == 0 and "风险等级" in out})
        r2 = subprocess.run([PYTHON, TOOL, "perm", "--tools", "CRM读写,邮件发送,订单下单", "--required", "CRM,邮件"],
                            capture_output=True, text=True, timeout=60)
        out2 = r2.stdout or ""
        items.append({"name": "perm 命令执行", "pass": r2.returncode == 0 and "多余权限" in out2 and "订单下单" in out2})
        r3 = subprocess.run([PYTHON, TOOL, "maturity", "--scores", "3,4,2,5,3,4"],
                            capture_output=True, text=True, timeout=60)
        items.append({"name": "maturity 命令执行", "pass": r3.returncode == 0 and "总分" in (r3.stdout or "")})
        r4 = subprocess.run([PYTHON, TOOL, "liability", "--scene", "Agent误发邮件给错误客户，含敏感信息"],
                            capture_output=True, text=True, timeout=60)
        out4 = r4.stdout or ""
        items.append({"name": "liability 命令执行", "pass": r4.returncode == 0 and "部署方担责" in out4 and "使用方担责" in out4})
        r5 = subprocess.run([PYTHON, TOOL, "regulation", "--region", "cn"], capture_output=True, text=True, timeout=60)
        items.append({"name": "regulation 命令执行", "pass": r5.returncode == 0 and "智能体" in (r5.stdout or "")})
    except Exception as e:
        items = [{"name": f"执行失败: {e}", "pass": False}]
    return items


def check_accuracy():
    cases = [
        ("客户服务Agent，可访问CRM、可发邮件、可下订单", ["高风险"]),
        ("文档整理Agent，只读公开资料，每步人工确认", ["低风险"]),
        ("客服Agent，只读查询，有人工确认", ["低风险"]),
    ]
    items = []
    for agent, expects in cases:
        try:
            r = subprocess.run([PYTHON, TOOL, "risk", "--agent", agent], capture_output=True, text=True, timeout=60)
            ok = r.returncode == 0 and any(e in (r.stdout or "") for e in expects)
            items.append({"name": f"risk「{agent[:14]}…」→{expects[0]}", "pass": ok})
        except Exception as e:
            items.append({"name": f"失败: {e}", "pass": False})
    return items


def check_structure():
    items = []
    try:
        sk = open(SKILL_MD, encoding="utf-8").read()
        fm = sk.split("---")[1] if sk.startswith("---") else ""
        for f in ["name:", "slug:", "display_name:", "displayName:", "title:", "version:", "category:",
                  "platforms:", "author:", "license:", "description:", "description_en:", "tags:"]:
            items.append({"name": f"frontmatter 含 {f}", "pass": f in fm})
        items.append({"name": "版权段", "pass": "版权与许可" in sk and "MIT" in sk})
        items.append({"name": "知识版权声明", "pass": "知识版权声明" in sk})
        items.append({"name": "免责声明 AS IS", "pass": "免责声明" in sk and "AS IS" in sk})
        items.append({"name": "LICENSE.md", "pass": os.path.exists(os.path.join(BASE, "LICENSE.md"))})
        ts = open(TOOL, encoding="utf-8").read()
        for c in ["risk", "perm", "maturity", "liability", "regulation", "--help"]:
            items.append({"name": f"工具实现 {c}", "pass": c in ts})
        for a in ["--agent", "--tools", "--required", "--scores", "--scene", "--region"]:
            items.append({"name": f"工具参数 {a}", "pass": a in ts})
    except OSError as e:
        items = [{"name": f"读取失败: {e}", "pass": False}]
    return items


def check_security():
    patterns = {
        "邮箱": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        "手机号": r"1[3-9][0-9]{9}",
        "本地路径(Win)": r"[A-Za-z]:\\\\Users\\\\",
        "本地路径(Unix)": r"[/\\]" + "Users" + r"[/\\][A-Za-z]",
        "密钥前缀": r"sk-[A-Za-z0-9]{16,}",
        "token 字样": r"(?i)api[_-]?key|access[_-]?token|secret[_-]?key",
        "私钥头": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    }
    items = []
    hits = []
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs if d not in {"verify", "__pycache__"}]
        for fn in files:
            if not fn.endswith((".md", ".py", ".json", ".svg", ".txt")):
                continue
            try:
                text = open(os.path.join(root, fn), encoding="utf-8").read()
            except UnicodeDecodeError:
                continue
            for name, pat in patterns.items():
                if re.search(pat, text):
                    hits.append(f"{os.path.relpath(os.path.join(root, fn), BASE)}: {name}")
    for name in patterns:
        items.append({"name": f"敏感模式「{name}」0 命中", "pass": not any(name in h for h in hits)})
    items.append({"name": "全包 0 命中", "pass": len(hits) == 0})
    return items


DIMS = [
    ("regulatory_timeliness", "法规时效性", check_regulatory_timeliness),
    ("coverage_completeness", "覆盖完整性", check_coverage),
    ("template_usability", "工具可用性", check_tools),
    ("risk_accuracy", "判定准确性", check_accuracy),
    ("structure_compliance", "结构规范性", check_structure),
    ("security_cleanliness", "安全净度", check_security),
]


def main():
    results = {"skill": "ai-agent-governance", "version": "1.0.0",
               "note": "本地闭环验证：零网络、零数据采集、可重复", "dimensions": [], "summary": {}}
    for key, label, fn in DIMS:
        items = fn()
        s = round(5.0 * sum(1 for i in items if i["pass"]) / len(items), 2) if items else 0.0
        results["dimensions"].append({"key": key, "label": label, "score": s, "checks": items})
        results["summary"][key] = s
        print(f"[{label}] {s:.2f}/5.00  ({sum(1 for i in items if i['pass'])}/{len(items)} 项)")
        for i in items:
            print(f"    {'PASS' if i['pass'] else 'FAIL'}  {i['name']}")
    results["benchmarks"] = {
        "industry_baseline": {"regulatory_timeliness": 2.5, "coverage_completeness": 3.0, "template_usability": 2.0,
                              "risk_accuracy": 2.5, "structure_compliance": 3.0, "security_cleanliness": 3.0},
        "enterprise_standard": {"regulatory_timeliness": 4.5, "coverage_completeness": 4.5, "template_usability": 4.0,
                                "risk_accuracy": 4.5, "structure_compliance": 5.0, "security_cleanliness": 5.0},
    }
    avg = round(sum(results["summary"].values()) / 6, 2)
    results["summary"]["average"] = avg
    os.makedirs(VERIFY, exist_ok=True)
    with open(os.path.join(VERIFY, "security_results.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n综合平均分：{avg:.2f} / 5.00")
    return 0


if __name__ == "__main__":
    sys.exit(main())
