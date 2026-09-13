#!/usr/bin/env python3
"""selftest.py — persistent-skill-memory v2.0.0 离线自检（确定性、无网络、合成数据）

运行：python3 scripts/selftest.py  （全部 PASS 才可交付）
组：G1 夹具确定性 · G2 frontmatter 解析 · G3 去重/owner · G4 分类
    G5 prompt 块格式 · G6 注入幂等 · G7 verify 端到端 · G8 钩子
    G9 退出码纪律 · G10 仅标准库 + 文档幻影
"""
import filecmp
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
TOOL = os.path.join(HERE, "skill_memory.py")
T1 = tempfile.mkdtemp(prefix="pmself_")
RESULTS = []

BEGIN = "<<<SKILL_INDEX_BEGIN>>>"
END = "<<<SKILL_INDEX_END>>>"


def check(group, name, ok, dbg=""):
    RESULTS.append((group, name, bool(ok), dbg))


def run(*args):
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True, timeout=120)


def jout(r):
    return json.loads(r.stdout) if r.stdout.strip() else None


def jerr(r):
    return json.loads(r.stderr) if r.stderr.strip() else None


def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)


def build_fixture(root):
    """9 个合成 SKILL.md，覆盖解析边界。"""
    w(root + "/skills/alpha-tool/SKILL.md",
      "---\nname: alpha-tool\ndescription: Alpha parser for PDF and CSV files.\ntags: [x]\n---\n\n# Alpha Tool\n\nbody\n")
    w(root + "/skills/beta-folded/SKILL.md",
      "---\nname: beta-folded\ndescription: >\n  First folded line.\n  Second folded line.\nversion: 1.0.0\n---\n\nbody\n")
    w(root + "/skills/gamma-literal/SKILL.md",
      "---\nname: gamma-literal\ndescription: |\n  Line one\n  line two after blank\n\n  Line three\n---\n\n# Gamma\n")
    w(root + "/skills/beta-heading/SKILL.md", "# Beta Heading Skill\n\nplain body, no frontmatter\n")
    w(root + "/skills/@orion/dup-skill/SKILL.md",
      "---\nname: dup-skill\ndescription: Owned duplicate A.\n---\n\n# A\n")
    w(root + "/skills/@orion/copy/dup-skill/SKILL.md",
      "---\nname: dup-skill\ndescription: Owned duplicate B (should lose dedupe).\n---\n\n# B\n")
    w(root + "/skills/quotey/SKILL.md",
      '---\nname: "quotey, special"\ndescription: Handles "quotes": commas, and: colons # not a comment\n---\n\n# Q\n')
    w(root + "/skills/crlf-skill/SKILL.md",
      "---\r\nname: crlf-skill\r\ndescription: CRLF line endings skill.\r\n---\r\n\r\n# CRLF\r\n")
    w(root + "/skills/empty-skill/SKILL.md", "")
    w(root + "/skills/unnamed-dir/SKILL.md",
      "---\ndescription: No name field here.\n---\n\n# Fallback Heading\n")
    w(root + "/prompt.txt", "STABLE BASE DIRECTIVES ABOVE\n\n# Agent\n\nYou are a helpful agent.\n")


def main():
    build_fixture(T1)
    SK = T1 + "/skills"
    PR = T1 + "/prompt.txt"

    # ── G1 夹具确定性 ────────────────────────────────────────────────────
    g = "G1-fixture-determinism"
    r1 = run("index", "--root", SK)
    r2 = run("index", "--root", SK)
    check(g, "index 双跑字节一致", r1.stdout == r2.stdout and r1.returncode == 0)
    d = jout(r1)
    check(g, "9 SKILL.md → 8 skills（empty 跳过）", d["n_skills"] == 8 and d["n_skipped"] == 1,
          json.dumps(d, ensure_ascii=False)[:200])
    w(T1 + "/out1.md", "")
    run("index", "--root", SK, "--write", T1 + "/out1.md")
    run("index", "--root", SK, "--write", T1 + "/out2.md")
    check(g, "SKILLS_INDEX.md 双跑字节一致",
          open(T1 + "/out1.md", "rb").read() == open(T1 + "/out2.md", "rb").read())

    # ── G2 frontmatter 解析 ──────────────────────────────────────────────
    g = "G2-frontmatter"
    by_name = {s["name"]: s for c in d["categories"] for s in c["skills"]}
    check(g, "普通标量 + 忽略 tags", by_name["alpha-tool"]["description"] == "Alpha parser for PDF and CSV files.")
    check(g, "> 折叠块：单空格连接", by_name["beta-folded"]["description"] == "First folded line. Second folded line.")
    check(g, "| 字面块：保留换行、去缩进、去尾空行",
          by_name["gamma-literal"]["description"] == "Line one\nline two after blank\n\nLine three")
    check(g, "无 frontmatter：name=目录名, desc=首个 # 标题",
          by_name["beta-heading"]["description"] == "Beta Heading Skill")
    check(g, "引号 name 去引号；# 后文本保留（不剥行内注释）",
          by_name['quotey, special'] is not None
          and by_name['quotey, special']["description"] == 'Handles "quotes": commas, and: colons # not a comment')
    check(g, "CRLF 文件正常解析", by_name["crlf-skill"]["description"] == "CRLF line endings skill.")
    check(g, "无 name → 目录名回退（description 仍取 frontmatter）",
          by_name["unnamed-dir"]["description"] == "No name field here.")
    skip = {s["path"]: s["reason"] for s in d["skipped"]}
    check(g, "空文件 → skipped(empty)", any(v == "empty" for v in skip.values()))

    # ── G3 去重 / owner ─────────────────────────────────────────────────
    g = "G3-dedupe-owner"
    dups = [s for c in d["categories"] for s in c["skills"] if s["name"] == "dup-skill"]
    check(g, "(owner,slug) 去重：@orion 双路径保留字典序首路径",
          len(dups) == 1 and dups[0]["owner"] == "orion"
          and dups[0]["path"] == "@orion/copy/dup-skill/SKILL.md",
          json.dumps(dups, ensure_ascii=False))
    check(g, "owner 无 @ 段 → 空串", all(s["owner"] == "" for s in by_name.values()
                                          if s["name"] != "dup-skill"))

    # ── G4 分类 ──────────────────────────────────────────────────────────
    g = "G4-categorization"
    dom = {s["name"]: c["domain"] for c in d["categories"] for s in c["skills"]}
    check(g, "alpha-tool (parser/pdf/csv) → data-parsing", dom.get("alpha-tool") == "data-parsing")
    KNOWN_DOMAINS = {"agents-orchestration", "research-grounding", "data-parsing",
                     "security-redteam", "build-engineering", "content-writing",
                     "media-generation", "ops-sandbox", "education-learning",
                     "productivity-personal", "general"}
    check(g, "域值全部来自固定表", all(x in KNOWN_DOMAINS for x in dom.values()), str(dom))
    rp = run("index", "--root", SK)
    dp = jout(rp)
    names_in = {s["name"] for c in dp["categories"] for s in c["skills"]}
    check(g, "category 数组含 domain+count+skills", all(set(c) == {"domain", "count", "skills"} for c in dp["categories"]))
    check(g, "名字集合稳定（与双跑一致）", names_in == {s["name"] for c in d["categories"] for s in c["skills"]})

    # ── G5 prompt 块格式 ─────────────────────────────────────────────────
    g = "G5-prompt-block"
    d = jout(run("prompt", "--root", SK))
    lines = d["block"].rstrip("\n").split("\n")
    hdr_re = re.compile(r"^\[[a-z-]+\]$")
    hdr = [l for l in lines if hdr_re.match(l)]
    nm = [l for l in lines if not hdr_re.match(l)]
    check(g, "域头行=[domain] 独占行（本夹具 2 域）", hdr == ["[data-parsing]", "[general]"])
    check(g, "块内名字=8 且含逗号名可往返", sorted(nm) == sorted(names_in) and len(nm) == 8, str(nm))
    check(g, "bytes 与内容一致", d["bytes"] == len(d["block"].encode("utf-8")) and d["n_lines"] == len(lines))
    order = [h.strip("[]") for h in hdr]
    check(g, "域顺序=固定优先级序", order == sorted(order, key=["agents-orchestration", "research-grounding",
          "data-parsing", "security-redteam", "build-engineering", "content-writing",
          "media-generation", "ops-sandbox", "education-learning", "productivity-personal",
          "general"].index))
    gi = lines.index("[general]")
    gen = [l for l in lines[gi + 1:] if not hdr_re.match(l)]
    check(g, "域内名字升序", gen == sorted(gen), str(gen))

    # ── G6 注入幂等 ──────────────────────────────────────────────────────
    g = "G6-inject-idempotency"
    base = open(PR).read()
    r = run("inject", "--root", SK, "--prompt-file", PR)
    check(g, "无标记 → appended", jout(r)["status"] == "appended" and r.returncode == 0)
    first = open(PR).read()
    check(g, "标记块写入且哨兵行保留", BEGIN in first and END in first
          and first.startswith("STABLE BASE DIRECTIVES ABOVE") and first.index(BEGIN) > 0)
    r = run("inject", "--root", SK, "--prompt-file", PR)
    check(g, "再注入 → unchanged 且字节不变", jout(r)["status"] == "unchanged" and open(PR).read() == first)
    # 内容变化 → replaced，标记外字节保留
    w(SK + "/new-tool/SKILL.md", "---\nname: new-tool\ndescription: Brand new thing.\n---\n\n# N\n")
    r = run("inject", "--root", SK, "--prompt-file", PR)
    second = open(PR).read()
    check(g, "新增 skill → replaced 且哨兵仍保留", jout(r)["status"] == "replaced"
          and second.startswith("STABLE BASE DIRECTIVES ABOVE") and "new-tool" in second)
    check(g, "重复注入不产生重复标记（v1 失败模式）", second.count(BEGIN) == 1 and second.count(END) == 1)
    # 半开 / 多对 / 倒序 → rc2
    w(T1 + "/half.txt", "x\n" + BEGIN + "\nold\n")
    r = run("inject", "--root", SK, "--prompt-file", T1 + "/half.txt")
    check(g, "半开标记 → rc2 不改文件", r.returncode == 2 and jerr(r) is not None
          and open(T1 + "/half.txt").read() == "x\n" + BEGIN + "\nold\n")
    w(T1 + "/multi.txt", BEGIN + "\na\n" + END + "\n" + BEGIN + "\nb\n" + END + "\n")
    r = run("inject", "--root", SK, "--prompt-file", T1 + "/multi.txt")
    check(g, "多对标记 → rc2 不改文件", r.returncode == 2 and open(T1 + "/multi.txt").read().count(BEGIN) == 2)
    w(T1 + "/rev.txt", END + "\n" + BEGIN + "\n")
    r = run("inject", "--root", SK, "--prompt-file", T1 + "/rev.txt")
    check(g, "倒序标记 → rc2", r.returncode == 2 and jerr(r) is not None)
    r = run("inject", "--root", SK, "--prompt-file", T1 + "/nope.txt")
    check(g, "inject 不创建缺失文件（rc2）", r.returncode == 2 and not os.path.exists(T1 + "/nope.txt"))

    # ── G7 verify 端到端 ─────────────────────────────────────────────────
    g = "G7-verify-e2e"
    # 恢复 8-skill 状态（删 new-tool）
    os.remove(SK + "/new-tool/SKILL.md")
    run("inject", "--root", SK, "--prompt-file", PR)
    r = run("verify", "--root", SK, "--prompt-file", PR)
    check(g, "一致 → rc0 + ok:true", r.returncode == 0 and jout(r)["ok"] is True)
    # 磁盘删 skill → stale（在 prompt 但已不在磁盘）
    os.rename(SK + "/alpha-tool/SKILL.md", SK + "/alpha-tool/SKILL.md.bak")
    r = run("verify", "--root", SK, "--prompt-file", PR)
    d = jout(r)
    check(g, "删 skill → rc3 + stale=[alpha-tool]", r.returncode == 3
          and d["stale"] == ["alpha-tool"] and d["missing"] == [])
    os.rename(SK + "/alpha-tool/SKILL.md.bak", SK + "/alpha-tool/SKILL.md")
    # 磁盘加新 skill 未重注入 → missing（在磁盘但不在 prompt）
    w(SK + "/fresh-skill/SKILL.md", "---\nname: fresh-skill\ndescription: Fresh on disk.\n---\n\n# F\n")
    r = run("verify", "--root", SK, "--prompt-file", PR)
    d = jout(r)
    check(g, "新 skill 未注入 → rc3 + missing=[fresh-skill]", r.returncode == 3
          and d["missing"] == ["fresh-skill"] and d["stale"] == [])
    # prompt 多假名 → stale（与 missing 可共存）
    data = open(PR).read()
    assert "[data-parsing]\n" in data
    open(PR, "w").write(data.replace("[data-parsing]\n", "[data-parsing]\nghost-skill\n", 1))
    r = run("verify", "--root", SK, "--prompt-file", PR)
    d = jout(r)
    check(g, "假名 → rc3 + stale 含 ghost-skill（missing 并存）",
          r.returncode == 3 and "ghost-skill" in d["stale"] and d["missing"] == ["fresh-skill"])
    # 重注入修复 → rc0（自愈路径）
    r = run("inject", "--root", SK, "--prompt-file", PR)
    r = run("verify", "--root", SK, "--prompt-file", PR)
    check(g, "重注入后自愈 → rc0", r.returncode == 0)
    os.remove(SK + "/fresh-skill/SKILL.md")
    run("inject", "--root", SK, "--prompt-file", PR)
    # 无标记块 → rc2
    w(T1 + "/nomark.txt", "plain prompt\n")
    r = run("verify", "--root", SK, "--prompt-file", T1 + "/nomark.txt")
    check(g, "无标记块 → rc2", r.returncode == 2 and jerr(r) is not None)
    # 多对标记 → rc2（与 inject 同一不变式）
    r = run("verify", "--root", SK, "--prompt-file", T1 + "/multi.txt")
    check(g, "多对标记 → verify rc2（不误报 rc3）", r.returncode == 2 and jerr(r) is not None)

    # ── G8 钩子 ──────────────────────────────────────────────────────────
    g = "G8-hook"
    w(T1 + "/inst/real_installer.sh", "#!/bin/bash\necho INSTALLED $@\n")
    os.chmod(T1 + "/inst/real_installer.sh", 0o755)
    r = run("hook", "--root", SK, "--prompt-file", PR, "--out", T1 + "/inst/skill_add.sh")
    d = jout(r)
    hook = T1 + "/inst/skill_add.sh"
    check(g, "模板写盘+可执行位", d["executable"] is True and os.access(hook, os.X_OK)
          and open(hook).read().startswith("#!/bin/bash"))
    check(g, "模板含 index+inject+verify 三步与 set -euo pipefail",
          all(x in open(hook).read() for x in ("set -euo pipefail", "index", "inject", "verify")))
    # 成功路径：installer 成功 → 三步执行
    os.system("rm -rf %s/skills/zz-hook-check" % SK)
    w(SK + "/zz-hook-check/SKILL.md", "---\nname: zz-hook-check\ndescription: hook side effect.\n---\n\n# Z\n")
    r = subprocess.run([hook, T1 + "/inst/real_installer.sh", "arg1"],
                       capture_output=True, text=True, timeout=120, cwd=T1)
    data = open(PR).read()
    check(g, "钩子成功路径：重索引副作用入 prompt", r.returncode == 0 and "zz-hook-check" in data
          and "INSTALLED" in r.stdout)
    # 失败路径：installer 非零 → 透传退出码，不重索引
    w(T1 + "/inst/fail_installer.sh", "#!/bin/bash\necho FAILING\nexit 7\n")
    os.chmod(T1 + "/inst/fail_installer.sh", 0o755)
    r = subprocess.run([hook, T1 + "/inst/fail_installer.sh"], capture_output=True, text=True,
                       timeout=120, cwd=T1)
    check(g, "钩子失败路径：退出码 7 透传", r.returncode == 7 and "FAILING" in r.stdout)
    os.remove(SK + "/zz-hook-check/SKILL.md")
    run("inject", "--root", SK, "--prompt-file", PR)

    # ── G9 退出码纪律 ────────────────────────────────────────────────────
    g = "G9-exit-discipline"
    r = run("index", "--root", T1 + "/no-such-dir")
    check(g, "缺 root → rc2 + stderr JSON + stdout 空", r.returncode == 2 and jerr(r) is not None and r.stdout == "")
    r = run("index", "--root", SK)
    check(g, "正常命令 rc0 且 stderr 空", r.returncode == 0 and r.stderr == "")
    e = jerr(run("index", "--root", T1 + "/no-such-dir"))
    check(g, "错误 JSON 含 tool+error", "tool" in e and "error" in e and e["tool"].endswith("v2.0.0"))
    for cmd in (["index", "--root", SK], ["prompt", "--root", SK], ["verify", "--root", SK, "--prompt-file", PR],
                ["stats", "--root", SK, "--prompt-file", PR]):
        r = run(*cmd)
        try:
            d = json.loads(r.stdout)
            ok = d["tool"] == "skill-memory v2.0.0" and "command" in d
        except Exception:
            ok = False
        check(g, "单行 JSON + tool + command: " + cmd[0], ok)
    d = jout(run("stats", "--root", SK, "--prompt-file", PR))
    check(g, "stats 预算字段齐", all(k in d for k in
          ("n_skills", "n_domains", "domain_counts", "prompt_block_bytes",
           "skills_index_md_bytes", "description_total_bytes")))

    # ── G10 仅标准库 + 文档幻影 ──────────────────────────────────────────
    g = "G10-stdlib-docs"
    allowed = {"argparse", "hashlib", "json", "os", "re", "sys", "stat", "csv", "io",
               "tempfile", "subprocess", "filecmp", "shutil"}
    for f in ("skill_memory.py", "selftest.py"):
        src = open(os.path.join(HERE, f)).read()
        bad = []
        for l in src.splitlines():
            m = re.match(r"^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_]*)", l)
            if m and m.group(1) not in allowed:
                bad.append(m.group(1))
        check(g, f + " 无第三方导入", not bad, str(bad))
    sk = open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8").read()
    help_txt = run("--help").stdout
    for cmd in ("index", "prompt", "inject", "verify", "stats", "hook"):
        check(g, "命令存在: " + cmd, cmd in sk and cmd in help_txt)
    for flag in ("--root", "--write", "--prompt-file", "--out"):
        check(g, "标志存在: " + flag, flag in sk and flag in help_txt)
    for ref in ("frontmatter_parsing.md", "categorization.md", "injection_semantics.md"):
        p = os.path.join(ROOT, "references", ref)
        check(g, "参考存在: " + ref, os.path.exists(p) and "供参考" in open(p, encoding="utf-8").read())
    check(g, "版本一致 2.0.0", "2.0.0" in sk and "skill-memory v2.0.0" in open(TOOL).read())
    check(g, "SKILL 无幻影脚本引用（v1 失败模式）",
          "manage_system_prompt.py" not in sk and "skill_add.sh" not in sk)

    total = len(RESULTS)
    fails = [x for x in RESULTS if not x[2]]
    for grp, name, ok, dbg in fails:
        print("FAIL %s :: %s %s" % (grp, name, dbg))
    print("selftest: %d/%d PASS" % (total - len(fails), total))
    shutil.rmtree(T1, ignore_errors=True)
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
