#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""skill-registry — 技能注册表生成器（SSOT：扫描技能目录 → JSON+MD 清单）。
痛点：技能多了没有单一真源，状态/版本/评分/链接散落。理论根基：LGD 三律·有籍。
Usage: python registry.py <skills-dir> [--out registry.json] [--md registry.md]"""
import argparse, json, os, sys, datetime

def main():
    p = argparse.ArgumentParser()
    p.add_argument("skills_dir", help="directory containing skill folders (each with SKILL.md)")
    p.add_argument("--out", default="registry.json")
    p.add_argument("--md", default="registry.md")
    a = p.parse_args()
    entries = []
    for name in sorted(os.listdir(a.skills_dir)):
        d = os.path.join(a.skills_dir, name)
        if not os.path.isdir(d):
            continue
        sm = os.path.join(d, "SKILL.md")
        if not os.path.exists(sm):
            continue
        text = open(sm, encoding="utf-8", errors="replace").read()
        m = __import__("re").match(r"^---\n(.*?)\n---", text, __import__("re").S)
        fm = {}
        if m:
            for line in m.group(1).splitlines():
                mm = __import__("re").match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
                if mm:
                    fm[mm.group(1)] = mm.group(2).strip().strip('"')
        entries.append({
            "slug": name,
            "name": fm.get("name", name),
            "version": fm.get("version", "?"),
            "license": fm.get("license", "?"),
            "category": fm.get("category", "?"),
            "tags": fm.get("tags", ""),
            "risk_tier": fm.get("risk_tier", "?"),
            "path": d,
        })
    reg = {"generated": datetime.date.today().isoformat(), "count": len(entries), "skills": entries}
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(reg, f, ensure_ascii=False, indent=2, default=str)
    md = ["# Skill Registry / 技能注册表", "",
          "> Generated %s — %d skills. SSOT for skill lifecycle." % (reg["generated"], reg["count"]), "",
          "| slug | name | version | license | category | risk |", "|---|---|---|---|---|---|"]
    for e in entries:
        md.append("| %s | %s | %s | %s | %s | %s |" % (e["slug"], e["name"], e["version"], e["license"], e["category"], e["risk_tier"]))
    with open(a.md, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")
    print("registry:", a.out, "(%d skills)" % reg["count"])
    print("markdown:", a.md)
    return 0

if __name__ == "__main__":
    sys.exit(main())
