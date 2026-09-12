#!/usr/bin/env python3
"""skill_memory.py — persistent-skill-memory v2.0.0（纯标准库、离线、确定性）

把 v1 散文机制代码化：index（解析+分类）→ prompt（压缩行）→ inject（标记间幂等注入）
→ verify（live prompt 端到端证明）→ stats（token 预算证据）→ hook（包装脚本模板）。
数据=磁盘上的 SKILL.md 文件（只读，绝不修改）；写盘只发生在 --write 与 hook --out 显式指定处。
契约：stdout 单行 JSON · stderr 单行 JSON（错误）· 退出码 0=ok · 2=输入错误 · 3=验证不一致。
"""
import argparse
import json
import os
import re
import stat
import sys

TOOL = "skill-memory v2.0.0"
BEGIN = "<<<SKILL_INDEX_BEGIN>>>"
END = "<<<SKILL_INDEX_END>>>"

# 分类表：固定优先级（先匹配先胜），关键词 = name+" "+description 小写子串；回退 general。
# 详见 references/categorization.md
DOMAINS = [
    ("agents-orchestration", ["agent", "orchestration", "swarm", "router", "playbook", "mcp", "tool-calling"]),
    ("research-grounding", ["research", "grounding", "evidence", "citation", "literature", "survey", "benchmark", "fact-check"]),
    ("data-parsing", ["parse", "parser", "dicom", "pdf", "csv", "json", "xml", "extract", "convert", "deid", "nifti", "imaging"]),
    ("security-redteam", ["security", "redteam", "red-team", "vuln", "vulnerability", "pentest", "threat", "exploit", "attack", "defense", "harden", "audit"]),
    ("build-engineering", ["build", "compile", "debug", "refactor", "deploy", "infra", "ci/cd", "test", "code"]),
    ("content-writing", ["write", "draft", "article", "copywriting", "marketing", "seo", "content", "blog", "newsletter"]),
    ("media-generation", ["image", "audio", "speech", "video", "tts", "render", "music", "illustration"]),
    ("ops-sandbox", ["sandbox", "snapshot", "docker", "kubernetes", "server", "monitoring", "cron", "async", "stall", "wipe", "restore", "deploy"]),
    ("education-learning", ["learn", "teach", "explain", "tutorial", "course", "quiz", "study", "education"]),
    ("productivity-personal", ["todo", "plan", "calendar", "email", "notes", "memory", "organize", "habit", "goal"]),
]
FALLBACK_DOMAIN = "general"


def emit(obj):
    sys.stdout.write(json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "\n")


def err(code, message, **extra):
    out = {"status": "error", "tool": TOOL, "error": message}
    out.update(extra)
    sys.stderr.write(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n")
    sys.exit(code)


def find_skill_files(root):
    hits = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort(key=str.lower)
        if "SKILL.md" in filenames:
            hits.append(os.path.join(dirpath, "SKILL.md"))
    return sorted(hits, key=str.lower)


# ── frontmatter 解析（简化 YAML 子集；规则见 references/frontmatter_parsing.md）──
def parse_frontmatter(text):
    """返回 (fields, body, had_frontmatter)。只解析 name/description（其余键忽略）。"""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text, False
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return {}, text, False
    fm_lines = lines[1:end]
    body = "\n".join(lines[end + 1:])
    fields = {}
    i = 0
    while i < len(fm_lines):
        ln = fm_lines[i]
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", ln)
        if not m:
            i += 1
            continue
        key, val = m.group(1), m.group(2).strip()
        i += 1
        if key not in ("name", "description"):
            # 跳过该键的值（含块/续行），直到下一个顶格键
            while i < len(fm_lines) and (not fm_lines[i].strip() or fm_lines[i].startswith((" ", "\t"))):
                i += 1
            continue
        if re.match(r"^[>|][+-]?$", val):
            block, i = _collect_block(fm_lines, i, folded=(val[0] == ">"))
            fields[key] = block
        elif val == "":
            block, i = _collect_block(fm_lines, i, folded=True)
            fields[key] = block
        else:
            fields[key] = _unquote(val)
    return fields, body, True


def _collect_block(fm_lines, i, folded=False):
    """收集缩进/空行块；folded(>) → 单空格连接；literal(|) → 保留换行。"""
    buf = []
    while i < len(fm_lines):
        ln = fm_lines[i]
        if ln.strip() == "" or ln.startswith((" ", "\t")):
            buf.append(ln)
            i += 1
        else:
            break
    # 去缩进：取最小缩进
    indents = [len(l) - len(l.lstrip()) for l in buf if l.strip()]
    pad = min(indents) if indents else 0
    ded = [l[pad:] if l.strip() else "" for l in buf]
    # 去尾部空行
    while ded and not ded[-1].strip():
        ded.pop()
    while ded and not ded[0].strip():
        ded.pop(0)
    if folded:
        text = " ".join(l.strip() for l in ded if l.strip())
    else:
        text = "\n".join(ded)
    return text.strip(), i


def _unquote(val):
    val = val.strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
        return val[1:-1]
    return val


def first_heading(body):
    for ln in body.split("\n"):
        m = re.match(r"^#{1,6}\s+(.+)$", ln.strip())
        if m:
            return m.group(1).strip()
    return ""


def categorize(name, description):
    text = (name + " " + description).lower()
    for domain, kws in DOMAINS:
        if any(kw in text for kw in kws):
            return domain
    return FALLBACK_DOMAIN


def build_index(root):
    skills, skipped = [], []
    seen = {}
    for path in find_skill_files(root):
        rel = os.path.relpath(path, root)
        try:
            raw = open(path, "rb").read()
        except OSError as e:
            skipped.append({"path": rel, "reason": "unreadable"})
            continue
        if not raw.strip():
            skipped.append({"path": rel, "reason": "empty"})
            continue
        text = raw.decode("utf-8-sig", errors="replace")
        text = text.replace("\r\n", "\n")
        fields, body, had = parse_frontmatter(text)
        ddir = os.path.dirname(rel)
        dirname = os.path.basename(ddir) if ddir not in (".", "") else ""
        owner = ""
        parts = rel.replace("\\", "/").split("/")
        for p in parts[:-1]:
            if p.startswith("@"):
                owner = p[1:]
                break
        name = fields.get("name") or dirname or ""
        description = fields.get("description") or first_heading(body) or ""
        if not name:
            skipped.append({"path": rel, "reason": "no-name"})
            continue
        key = (owner, name)
        entry = {"name": name, "owner": owner, "path": rel,
                 "description": description, "domain": categorize(name, description)}
        if key in seen:
            if rel < seen[key]["path"]:
                seen[key] = entry
        else:
            seen[key] = entry
    for entry in sorted(seen.values(), key=lambda e: (e["owner"], e["name"])):
        skills.append(entry)
    return skills, skipped


def group_by_domain(skills):
    groups = {}
    for s in skills:
        groups.setdefault(s["domain"], []).append(s)
    order = [d for d, _ in DOMAINS] + [FALLBACK_DOMAIN]
    out = []
    for d in order:
        if d in groups:
            out.append((d, sorted(groups[d], key=lambda e: e["name"])))
    return out


def prompt_block(skills):
    """行格式：域头行 [domain] + 其名下列名升序（一行一名，无分隔符歧义，任意名字可往返）。"""
    lines = []
    for d, items in group_by_domain(skills):
        lines.append("[%s]" % d)
        lines.extend(e["name"] for e in items)
    return "\n".join(lines) + "\n" if lines else ""


HEADER_RE = re.compile(r"^\[[a-z][a-z0-9-]*\]$")


def skills_index_md(skills, skipped):
    groups = group_by_domain(skills)
    L = ["# Skills Index — %d skills, %d domains" % (len(skills), len(groups)), ""]
    for d, items in groups:
        L.append("## %s (%d)" % (d, len(items)))
        L.append("")
        for e in items:
            who = (" (%s)" % e["owner"]) if e["owner"] else ""
            L.append("- **%s**%s — %s" % (e["name"], who, e["description"] or "(no description)"))
        L.append("")
    if skipped:
        L.append("## Skipped (%d)" % len(skipped))
        L.append("")
        for s in skipped:
            L.append("- `%s` — %s" % (s["path"], s["reason"]))
        L.append("")
    return "\n".join(L)


def cmd_index(args):
    root = args.root
    if not os.path.isdir(root):
        err(2, "skills 根目录不存在: %s" % os.path.abspath(root))
    skills, skipped = build_index(root)
    groups = group_by_domain(skills)
    out = {
        "command": "index", "tool": TOOL, "root": os.path.abspath(root),
        "n_skills": len(skills), "n_domains": len(groups), "n_skipped": len(skipped),
        "categories": [{"domain": d, "count": len(items),
                        "skills": [{"name": e["name"], "owner": e["owner"], "path": e["path"],
                                    "description": e["description"]}
                                   for e in items]} for d, items in groups],
        "skipped": skipped,
    }
    if args.write:
        os.makedirs(os.path.dirname(os.path.abspath(args.write)), exist_ok=True)
        md = skills_index_md(skills, skipped)
        with open(args.write, "w", encoding="utf-8", newline="") as f:
            f.write(md)
        out["index_file"] = os.path.abspath(args.write)
        out["index_bytes"] = len(md.encode("utf-8"))
    emit(out)
    sys.exit(0)


def cmd_prompt(args):
    root = args.root
    if not os.path.isdir(root):
        err(2, "skills 根目录不存在: %s" % os.path.abspath(root))
    skills, _ = build_index(root)
    block = prompt_block(skills)
    emit({"command": "prompt", "tool": TOOL, "n_skills": len(skills),
          "n_lines": block.count("\n"), "bytes": len(block.encode("utf-8")),
          "block": block})
    sys.exit(0)


# ── inject：标记间幂等（规则见 references/injection_semantics.md）────────────
def inject_block(prompt_file, block):
    """行级处理。返回 (status, new_content)。
    status: replaced | appended | unchanged | marker_error
    标记必须独占一行；BEGIN/END 恰好各一行且顺序正确才允许替换；
    其余情况（半开、多对、倒序、缩进标记）→ marker_error，不自动修。"""
    data = open(prompt_file, "rb").read().decode("utf-8", errors="replace")
    lines = data.split("\n")
    b_lines = [i for i, l in enumerate(lines) if l.strip() == BEGIN]
    e_lines = [i for i, l in enumerate(lines) if l.strip() == END]
    if len(b_lines) == 1 and len(e_lines) == 1 and b_lines[0] < e_lines[0]:
        body = block.rstrip("\n").split("\n") if block else [""]
        new_lines = lines[:b_lines[0]] + [BEGIN] + body + [END] + lines[e_lines[0] + 1:]
        new = "\n".join(new_lines)
        return ("unchanged" if new == data else "replaced"), new
    if not b_lines and not e_lines:
        suffix = "\n" if data and not data.endswith("\n") else ""
        return "appended", data + suffix + "\n" + BEGIN + "\n" + block + END + "\n"
    return "marker_error", data


def cmd_inject(args):
    if not os.path.isfile(args.prompt_file):
        err(2, "prompt 文件不存在（inject 不创建文件）: %s" % os.path.abspath(args.prompt_file))
    if not os.path.isdir(args.root):
        err(2, "skills 根目录不存在: %s" % os.path.abspath(args.root))
    skills, _ = build_index(args.root)
    block = prompt_block(skills)
    try:
        status, new = inject_block(args.prompt_file, block)
    except OSError as e:
        err(2, "prompt 文件不可读/写: %s" % e)
    if status == "marker_error":
        err(2, "标记异常（BEGIN/END 未成恰好一对：半开/多对/倒序）：请人工修复 prompt 文件",
            hint="不自动补全/清理，避免吞掉标记外内容")
    before = len(open(args.prompt_file, "rb").read())
    with open(args.prompt_file, "w", encoding="utf-8", newline="") as f:
        f.write(new)
    emit({"command": "inject", "tool": TOOL, "prompt_file": os.path.abspath(args.prompt_file),
          "status": status, "n_skills": len(skills),
          "block_bytes": len(block.encode("utf-8")),
          "prompt_bytes_before": before, "prompt_bytes_after": len(new.encode("utf-8"))})
    sys.exit(0)


def parse_prompt_names(data):
    """解析标记块 → 名字集合。域头行（匹配 HEADER_RE）忽略；其余非空行=名字。"""
    m = re.search(re.escape(BEGIN) + r"\n(.*?)\n" + re.escape(END), data, re.S)
    if not m:
        return None
    names = set()
    for ln in m.group(1).split("\n"):
        s = ln.strip()
        if not s or HEADER_RE.match(s):
            continue
        names.add(s)
    return names


def cmd_verify(args):
    if not os.path.isfile(args.prompt_file):
        err(2, "prompt 文件不存在: %s" % os.path.abspath(args.prompt_file))
    if not os.path.isdir(args.root):
        err(2, "skills 根目录不存在: %s" % os.path.abspath(args.root))
    data = open(args.prompt_file, "rb").read().decode("utf-8", errors="replace")
    b = [l for l in data.split("\n") if l.strip() == BEGIN]
    e = [l for l in data.split("\n") if l.strip() == END]
    if len(b) != 1 or len(e) != 1:
        err(2, "标记异常（BEGIN/END 未成恰好一对）：请人工修复 prompt 文件")
    prompt_names = parse_prompt_names(data)
    if prompt_names is None:
        err(2, "prompt 文件中无完整标记块（BEGIN 后缺 END 换行）")
    skills, _ = build_index(args.root)
    index_names = {s["name"] for s in skills}
    missing = sorted(index_names - prompt_names)
    stale = sorted(prompt_names - index_names)
    block = prompt_block(skills)
    emit({"command": "verify", "tool": TOOL,
          "n_index": len(index_names), "n_prompt": len(prompt_names),
          "missing": missing, "stale": stale,
          "block_bytes": len(block.encode("utf-8")),
          "ok": not missing and not stale})
    sys.exit(3 if (missing or stale) else 0)


def cmd_stats(args):
    if not os.path.isdir(args.root):
        err(2, "skills 根目录不存在: %s" % os.path.abspath(args.root))
    skills, skipped = build_index(args.root)
    groups = group_by_domain(skills)
    block = prompt_block(skills)
    md = skills_index_md(skills, skipped)
    out = {
        "command": "stats", "tool": TOOL,
        "n_skills": len(skills), "n_domains": len(groups),
        "domain_counts": {d: len(items) for d, items in groups},
        "prompt_block_bytes": len(block.encode("utf-8")),
        "skills_index_md_bytes": len(md.encode("utf-8")),
        "description_total_bytes": sum(len(s["description"].encode("utf-8")) for s in skills),
        "n_skipped": len(skipped),
    }
    if args.prompt_file:
        if not os.path.isfile(args.prompt_file):
            err(2, "prompt 文件不存在: %s" % os.path.abspath(args.prompt_file))
        data = open(args.prompt_file, "rb").read().decode("utf-8", errors="replace")
        names = parse_prompt_names(data)
        out["prompt_file_bytes"] = len(data.encode("utf-8"))
        out["prompt_indexed_names"] = len(names) if names is not None else None
    emit(out)
    sys.exit(0)


# ── hook：包装脚本模板（幂等重索引）──────────────────────────────────────────
HOOK_TEMPLATE = """#!/bin/bash
# 包装脚本：先执行原安装/变更命令，成功后重索引并注入，再 verify。
# 由 skill-memory v2.0.0 `hook` 命令生成（纯文本模板，无外部依赖）。
set -euo pipefail

# 1) 原始命令（透传参数，退出码由 set -e 传递）
"$@"

# 2) 重索引 → 注入 → 验证
SKILL_MEMORY=__TOOL_PATH__
SKILLS_ROOT=__SKILLS_ROOT__
PROMPT_FILE=__PROMPT_FILE__
python3 "$SKILL_MEMORY" index --root "$SKILLS_ROOT"
python3 "$SKILL_MEMORY" inject --root "$SKILLS_ROOT" --prompt-file "$PROMPT_FILE"
python3 "$SKILL_MEMORY" verify --root "$SKILLS_ROOT" --prompt-file "$PROMPT_FILE"
"""


def cmd_hook(args):
    if not os.path.isdir(args.root):
        err(2, "skills 根目录不存在: %s" % os.path.abspath(args.root))
    if not os.path.isfile(args.prompt_file):
        err(2, "prompt 文件不存在: %s" % os.path.abspath(args.prompt_file))
    if not args.out:
        err(2, "hook 需要 --out PATH（写盘位置必须显式）")
    tool_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "skill_memory.py"))
    content = (HOOK_TEMPLATE
               .replace("__TOOL_PATH__", tool_path)
               .replace("__SKILLS_ROOT__", os.path.abspath(args.root))
               .replace("__PROMPT_FILE__", os.path.abspath(args.prompt_file)))
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    with open(args.out, "w", encoding="utf-8", newline="") as f:
        f.write(content)
    os.chmod(args.out, os.stat(args.out).st_mode | stat.S_IXUSR | stat.S_IXGRP)
    emit({"command": "hook", "tool": TOOL, "file": os.path.abspath(args.out),
          "bytes": len(content.encode("utf-8")), "executable": True,
          "usage": "%s <原始安装命令...>" % os.path.abspath(args.out)})
    sys.exit(0)


def main():
    p = argparse.ArgumentParser(
        prog="skill_memory.py", description=TOOL + "（纯标准库、离线、确定性；只读 SKILL.md，写盘仅限 --write/--out/prompt 文件标记块）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="flags:\n"
               "  index  --root DIR [--write PATH]   # 解析+分类；--write 落 SKILLS_INDEX.md\n"
               "  prompt --root DIR                  # 压缩名字块（注入用）\n"
               "  inject --root DIR --prompt-file F  # 标记间幂等注入（不创建文件）\n"
               "  verify --root DIR --prompt-file F  # live prompt 证明（rc 3 = 缺失/过期）\n"
               "  stats  --root DIR [--prompt-file F]\n"
               "  hook   --root DIR --prompt-file F --out PATH   # 包装脚本模板\n"
               "exit: 0 ok | 2 输入错误(stderr 单行 JSON) | 3 验证不一致")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("index", help="解析全部 SKILL.md + 分类（确定性）")
    sp.add_argument("--root", required=True, help="skills 根目录")
    sp.add_argument("--write", default=None, help="写出 SKILLS_INDEX.md 路径")
    sp.set_defaults(fn=cmd_index)

    sp = sub.add_parser("prompt", help="压缩名字块（每域一行）")
    sp.add_argument("--root", required=True)
    sp.set_defaults(fn=cmd_prompt)

    sp = sub.add_parser("inject", help="标记间幂等注入（half-open → rc2 不自动补全）")
    sp.add_argument("--root", required=True)
    sp.add_argument("--prompt-file", required=True)
    sp.set_defaults(fn=cmd_inject)

    sp = sub.add_parser("verify", help="live prompt 端到端证明")
    sp.add_argument("--root", required=True)
    sp.add_argument("--prompt-file", required=True)
    sp.set_defaults(fn=cmd_verify)

    sp = sub.add_parser("stats", help="计数/域分布/字节预算")
    sp.add_argument("--root", required=True)
    sp.add_argument("--prompt-file", default=None)
    sp.set_defaults(fn=cmd_stats)

    sp = sub.add_parser("hook", help="生成安装后自动重索引的包装脚本")
    sp.add_argument("--root", required=True)
    sp.add_argument("--prompt-file", required=True)
    sp.add_argument("--out", default=None, help="包装脚本输出路径")
    sp.set_defaults(fn=cmd_hook)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
