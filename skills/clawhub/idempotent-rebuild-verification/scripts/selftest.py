#!/usr/bin/env python3
"""selftest.py — rebuild-verify v2.0.0 离线自检（确定性、无网络、合成数据）

运行：python3 scripts/selftest.py  （全部 PASS 才可交付）
组：G1 夹具确定性 · G2 提取器 · G3 verify 分类 · G4 manifest · G5 pins
    G6 wipe-audit · G7 退出码纪律 · G8 尾部换行边界 · G9 夹具内容
    G10 仅标准库 · G11 文档幻影 · G12 跨模型 JSON 契约
"""
import filecmp
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TOOL = os.path.join(HERE, "rebuild_verify.py")
T1 = tempfile.mkdtemp(prefix="rvself_")
T2 = tempfile.mkdtemp(prefix="rvself2_")
RESULTS = []


def check(group, name, ok, dbg=""):
    RESULTS.append((group, name, bool(ok), dbg))


def run(*args, env_extra=None):
    env = {**os.environ}
    if env_extra:
        env.update(env_extra)
    return subprocess.run([sys.executable, TOOL, *args], capture_output=True, text=True,
                          timeout=120, env=env)


def jout(r):
    return json.loads(r.stdout) if r.stdout.strip() else None


def jerr(r):
    return json.loads(r.stderr) if r.stderr.strip() else None


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rd(p):
    return open(p, "rb").read()


def main():
    run("gen-fixtures", T1)
    run("gen-fixtures", T2)
    files = ["canonical.txt", "drift_no_nl.txt", "drift_3nl.txt", "truncated.txt",
             "html404.txt", "same_size_diff.txt", "crlf.txt", "manifest.txt", "runbook.md"]
    canon = rd(T1 + "/canonical.txt")
    want = sha(canon)

    # ── G1 夹具确定性 ─────────────────────────────────────────────────────
    g = "G1-fixtures-determinism"
    dc = filecmp.dircmp(T1, T2)
    check(g, "两次生成目录完全一致", dc.diff_files == [] and dc.left_only == [] and dc.right_only == [],
          str((dc.diff_files, dc.left_only, dc.right_only)))
    check(g, "canonical=1116B 单尾 \\n", len(canon) == 1116 and canon.endswith(b"\n") and not canon.endswith(b"\n\n"))
    check(g, "drift_no_nl=1115B", len(rd(T1 + "/drift_no_nl.txt")) == 1115)
    check(g, "drift_3nl=1118B", len(rd(T1 + "/drift_3nl.txt")) == 1118)
    trunc = rd(T1 + "/truncated.txt")
    check(g, "truncated=500B 止于词中", len(trunc) == 500 and not trunc.endswith(b"\n"))
    h404 = rd(T1 + "/html404.txt")
    check(g, "html404 <4096 且含 404", len(h404) < 4096 and b"404" in h404)
    ssd = rd(T1 + "/same_size_diff.txt")
    diffpos = [i for i in range(len(canon)) if ssd[i] != canon[i]]
    check(g, "same_size_diff 仅 1 字节差异(offset 100)", len(ssd) == len(canon) and diffpos == [100])
    crlf = rd(T1 + "/crlf.txt")
    check(g, "crlf 行数一致", crlf.replace(b"\r\n", b"\n") == canon and crlf.count(b"\r\n") == canon.count(b"\n"))

    # ── G2 提取器 ─────────────────────────────────────────────────────────
    g = "G2-extractor"
    r = run("extract-steps", T1 + "/runbook.md", "--write-steps", T1 + "/steps")
    d = jout(r)
    check(g, "6 个步骤", d["n_steps"] == 6)
    check(g, "suspect 恰为 [3,4]", d["suspect"] == [3, 4], str(d["suspect"]))
    s2 = d["steps"][1]
    check(g, "step2 heredoc EOF 终止且 ok", s2["status"] == "ok"
          and s2["heredocs"] == [{"label": "EOF", "at_line": 2, "terminated": True, "dash": False}]
          or (s2["status"] == "ok" and s2["heredocs"] and s2["heredocs"][0]["terminated"]))
    s3 = d["steps"][2]
    check(g, "step3 内嵌围栏 => suspect(SHIM_EOF 未终止)",
          s3["status"] == "suspect" and s3["heredocs"][0]["label"] == "SHIM_EOF" and not s3["heredocs"][0]["terminated"])
    step3_bytes = rd(T1 + "/steps/step_03.sh")
    check(g, "step3 字节含内嵌围栏行", b"```bash" in step3_bytes and b"# inner fence line" in step3_bytes
          and step3_bytes.endswith(b"# inner fence line: an example inside the heredoc\n"))
    expect3 = (b"cat > ~/.shim/claude << 'SHIM_EOF'\n#!/bin/sh\necho 'usage: see runbook'\n"
               b"```bash\n# inner fence line: an example inside the heredoc\n")
    check(g, "step3 完整字节精确（独立期望值）", step3_bytes == expect3)
    open(T1 + "/tab.md", "w").write("# t\n\n```bash\nx\n\t```\nend\n```\n")
    rt = run("extract-steps", T1 + "/tab.md", "--write-steps", T1 + "/tabsteps")
    dt = jout(rt)
    check(g, "Tab 缩进围栏行不视为闭栏(CommonMark)",
          dt["n_steps"] == 1 and dt["steps"][0]["status"] == "ok"
          and rd(T1 + "/tabsteps/step_01.sh") == b"x\n\t```\nend\n")
    open(T1 + "/tab2.md", "w").write("# t2\n\n```bash\nx\n\t\t```\ny\n```\n")
    rt2 = run("extract-steps", T1 + "/tab2.md", "--write-steps", T1 + "/tab2steps")
    dt2 = jout(rt2)
    check(g, "连续 Tab 缩进(=8 列)围栏行不视为闭栏",
          dt2["n_steps"] == 1 and rd(T1 + "/tab2steps/step_01.sh") == b"x\n\t\t```\ny\n")
    open(T1 + "/hd.md", "w").write("```bash\ncat > /tmp/out.txt << 'MY-LABEL'\nbody line\nMY-LABEL\necho done\n```\n")
    rh = run("extract-steps", T1 + "/hd.md")
    dh = jout(rh)
    check(g, "连字符 heredoc 标签识别且终止",
          dh["n_steps"] == 1 and dh["steps"][0]["status"] == "ok"
          and dh["steps"][0]["heredocs"] == [{"label": "MY-LABEL", "at_line": 1,
                                              "terminated": True, "dash": False}])
    s4 = d["steps"][3]
    check(g, "step4 孤儿块 => suspect(OPEN_LABEL)", s4["status"] == "suspect"
          and s4["heredocs"][0]["label"] == "OPEN_LABEL" and not s4["heredocs"][0]["terminated"])
    s5 = d["steps"][4]
    check(g, "step5 波浪围栏 lang=sh", s5["lang"] == "sh" and s5["status"] == "ok")
    man = json.load(open(T1 + "/steps/steps.json"))
    okh = all(sha(rd(T1 + "/steps/" + s["file"])) == s["sha256"] for s in man)
    check(g, "steps.json sha256 与写盘一致", okh and len(man) == 6)
    check(g, "step1 字节精确", rd(T1 + "/steps/step_01.sh") ==
          b"apt-get update && apt-get install -y cmake g++ make\n")
    r2 = run("extract-steps", T1 + "/runbook.md", "--lang", "sh")
    d2 = jout(r2)
    check(g, "--lang sh 精确过滤", d2["n_steps"] == 1 and d2["steps"][0]["lang"] == "sh")
    r3 = run("extract-steps", T1 + "/runbook.md", "--lang", "text")
    d3 = jout(r3)
    check(g, "--lang text = 未标注块", d3["n_steps"] == 1 and d3["steps"][0]["status"] == "suspect")

    # ── G3 verify 分类 ────────────────────────────────────────────────────
    g = "G3-verify-classes"
    cases = [
        ("canonical.txt", "ok", "ok"), ("drift_no_nl.txt", "trailing_newline_drift", "benign"),
        ("drift_3nl.txt", "trailing_newline_drift", "benign"), ("truncated.txt", "truncated_paste", "error"),
        ("html404.txt", "html_error_page", "error"), ("same_size_diff.txt", "content_change", "error"),
        ("crlf.txt", "crlf_drift", "benign"),
    ]
    for f, klass, status in cases:
        r = run("verify", T1 + "/" + f, "--want", want, "--want-size", "1116")
        d = jout(r)
        check(g, "%s -> %s" % (f, klass), d["class"] == klass and d["status"] == status
              and r.returncode == (0 if status == "ok" else 3), json.dumps(d, ensure_ascii=False)[:160])
    r = run("verify", T1 + "/canonical.txt", "--want", want)
    check(g, "无 want-size 时 ok", jout(r)["class"] == "ok")
    r = run("verify", T1 + "/drift_no_nl.txt", "--want-size", "1116")
    d = jout(r)
    check(g, "仅尺寸：1115!=1116 -> size_mismatch", d["class"] == "size_mismatch" and r.returncode == 3)
    r = run("verify", T1 + "/canonical.txt", "--want-size", "1116")
    d = jout(r)
    check(g, "仅尺寸匹配 -> size_ok 并给出哈希", d["class"] == "size_ok" and d["detail"]["got_sha256"] == want)
    # 无尾换行钉扎（钉扎 strip_all 形式）
    core = canon.rstrip(b"\n")
    r = run("verify", T1 + "/canonical.txt", "--want", sha(core))
    d = jout(r)
    check(g, "钉扎无换行形式: 1\\n 文件 -> trailing_newline_drift(strip_all)",
          d["class"] == "trailing_newline_drift" and d["detail"]["normalized_match"] == "strip_all")
    r = run("verify", T1 + "/drift_3nl.txt", "--want", want)
    check(g, "3 尾换行: n=3 且 normalized_match=single_nl",
          jout(r)["detail"]["trailing_newlines"] == 3 and jout(r)["detail"]["normalized_match"] == "single_nl")

    # ── G4 manifest ───────────────────────────────────────────────────────
    g = "G4-manifest"
    r = run("manifest", T1 + "/manifest.txt", "--root", T1)
    d = jout(r)
    check(g, "钉扎 manifest: 1 ok / 6 drift", d["n_ok"] == 1 and d["n_drifted"] == 6 and r.returncode == 3)
    cls = {x["rel"]: x["class"] for x in d["drifted"]}
    check(g, "drift 分类齐全", cls == {"drift_no_nl.txt": "trailing_newline_drift",
                                       "drift_3nl.txt": "trailing_newline_drift",
                                       "truncated.txt": "truncated_paste",
                                       "html404.txt": "html_error_page",
                                       "same_size_diff.txt": "content_change",
                                       "crlf.txt": "crlf_drift"}, str(cls))
    good = T1 + "/good.txt"
    lines = ["# good"]
    for f in files:
        if f in ("manifest.txt", "runbook.md", "good.txt"):
            continue
        p = rd(T1 + "/" + f)
        lines.append("%s %s %d" % (f, sha(p), len(p)))
    open(good, "w").write("\n".join(lines) + "\n")
    r = run("manifest", good, "--root", T1)
    check(g, "全 ok manifest exit 0", r.returncode == 0 and jout(r)["status"] == "ok")
    open(T1 + "/miss.txt", "w").write("nope.txt %s\n" % sha(b"x"))
    r = run("manifest", T1 + "/miss.txt", "--root", T1)
    d = jout(r)
    check(g, "缺失文件入 missing 且 stderr 干净", d["missing"] == [{"rel": "nope.txt", "line": 1}]
          and r.returncode == 3 and r.stderr == "")
    open(T1 + "/bad1.txt", "w").write("onlyonearg\n")
    r = run("manifest", T1 + "/bad1.txt", "--root", T1)
    check(g, "坏行 -> exit 2 + stderr JSON", r.returncode == 2 and jerr(r) is not None and "格式错误" in jerr(r)["error"])
    open(T1 + "/bad2.txt", "w").write("f.txt zz\n")
    r = run("manifest", T1 + "/bad2.txt", "--root", T1)
    check(g, "坏哈希 -> exit 2", r.returncode == 2 and "哈希非法" in jerr(r)["error"])

    # ── G5 pins ───────────────────────────────────────────────────────────
    g = "G5-pins"
    r = run("pins", T1 + "/runbook.md")
    d = jout(r)
    check(g, "2 个钉扎", d["n_pins"] == 2)
    check(g, "均为 64 hex", all(re.fullmatch(r"[0-9a-f]{64}", p["sha256"]) for p in d["pins"]))
    check(g, "heading 不被围栏内 # 污染", all(p["heading"] == "Mini Rebuild Runbook (synthetic test)" for p in d["pins"]),
          str([p["heading"] for p in d["pins"]]))
    check(g, "referenced_file 均解析", all(p["referenced_file"] == "~/dynamic_system_prompt.txt" for p in d["pins"]),
          str([p["referenced_file"] for p in d["pins"]]))
    check(g, "in_code_fence 标记", all(p["in_code_fence"] for p in d["pins"]))

    # ── G6 wipe-audit ─────────────────────────────────────────────────────
    g = "G6-wipe-audit"
    ws = T1 + "/ws"
    os.makedirs(ws + "/build/bin", exist_ok=True)
    os.makedirs(ws + "/node_modules/.bin", exist_ok=True)
    open(ws + "/setup.sh", "w").write("x\n")
    open(ws + "/model.gguf", "w").write("x" * 100)
    open(ws + "/build/bin/tool", "w").write("x\n")
    r = run("wipe-audit", ws)
    check(g, "擦除前 -> pre_wipe_or_full", jout(r)["verdict"] == "pre_wipe_or_full" and r.returncode == 0)
    shutil.rmtree(ws + "/build"); os.remove(ws + "/model.gguf"); shutil.rmtree(ws + "/node_modules")
    r = run("wipe-audit", ws)
    d = jout(r)
    check(g, "擦除后 -> normal_post_wipe", d["verdict"] == "normal_post_wipe")
    check(g, "next_actions 含 compile/model/shim",
          any("compile" in a for a in d["next_actions"]) and any("model" in a for a in d["next_actions"])
          and any("shim" in a for a in d["next_actions"]), str(d["next_actions"]))
    os.remove(ws + "/setup.sh")
    r = run("wipe-audit", ws)
    check(g, "全空 -> clean", jout(r)["verdict"] == "clean" and r.returncode == 0)
    os.makedirs(ws + "/build/bin", exist_ok=True)
    open(ws + "/build/bin/tool", "w").write("x\n")
    r = run("wipe-audit", ws)
    d = jout(r)
    check(g, "产物在脚本无 -> scripts_missing_too exit 3", d["verdict"] == "scripts_missing_too" and r.returncode == 3)
    ws2 = T1 + "/ws2"
    os.makedirs(ws2 + "/custom_artifacts")
    open(ws2 + "/custom_artifacts/x", "w").write("x")
    r = run("wipe-audit", ws2)
    check(g, "自定义目录默认不算产物 -> clean", jout(r)["verdict"] == "clean" and r.returncode == 0)
    r = run("wipe-audit", ws2, env_extra={"RV_SNAPSHOT_EXCLUDED": "custom_artifacts"})
    d = jout(r)
    check(g, "RV_SNAPSHOT_EXCLUDED 覆盖 -> scripts_missing_too", d["verdict"] == "scripts_missing_too" and r.returncode == 3)

    # ── G7 退出码纪律 ─────────────────────────────────────────────────────
    g = "G7-exit-discipline"
    r = run("verify", T1 + "/nope.txt", "--want", want)
    check(g, "缺文件 exit 2 + stderr JSON", r.returncode == 2 and jerr(r) is not None and r.stdout == "")
    r = run("verify", T1 + "/canonical.txt", "--want", "zz")
    check(g, "坏 hex exit 2", r.returncode == 2 and "64 位" in jerr(r)["error"])
    r = run("verify", T1 + "/canonical.txt", "--want", want)
    check(g, "ok exit 0", r.returncode == 0)
    r = run("verify", T1 + "/truncated.txt", "--want", want, "--want-size", "1116")
    check(g, "drift exit 3 且 stdout 有数据 JSON", r.returncode == 3 and jout(r) is not None)
    e = jerr(run("verify", T1 + "/nope.txt", "--want", want))
    check(g, "错误 JSON 含 tool+error", "tool" in e and "error" in e and e["tool"].endswith("v2.0.0"))

    # ── G8 尾部换行边界 ────────────────────────────────────────────────────
    g = "G8-newline-edges"
    open(T1 + "/e1.txt", "wb").write(b"abc")
    r = run("verify", T1 + "/e1.txt", "--want", sha(b"abc"))
    check(g, "无尾换行 vs 无尾换行钉扎 = ok", jout(r)["class"] == "ok")
    open(T1 + "/e2.txt", "wb").write(b"abc\n")
    r = run("verify", T1 + "/e2.txt", "--want", sha(b"abc"))
    check(g, "1 尾换行 vs 无尾换行钉扎 = drift", jout(r)["class"] == "trailing_newline_drift")
    r = run("verify", T1 + "/e2.txt", "--want", sha(b"abc\n"))
    check(g, "1 尾换行 vs 同形式钉扎 = ok", jout(r)["class"] == "ok")
    open(T1 + "/e3.txt", "wb").write(b"")
    r = run("verify", T1 + "/e3.txt", "--want", sha(b"abc"), "--want-size", "3")
    check(g, "空文件 vs 非空钉扎 = truncated_paste", jout(r)["class"] == "truncated_paste")
    open(T1 + "/e4.txt", "wb").write(b"abc")
    r = run("verify", T1 + "/e4.txt", "--want", sha(b"abd"))
    check(g, "同尺寸无 want-size = unknown(带 magic)", jout(r)["class"] == "unknown"
          and "magic" in jout(r)["detail"])
    open(T1 + "/e5.txt", "wb").write(b"abc\r\ndef\r\n")
    r = run("verify", T1 + "/e5.txt", "--want", sha(b"abc\ndef\n"))
    check(g, "CRLF vs LF 钉扎 = crlf_drift(benign)", jout(r)["class"] == "crlf_drift"
          and jout(r)["status"] == "benign" and jout(r)["detail"]["crlf_count"] == 2)
    r = run("verify", T1 + "/e5.txt", "--want", sha(b"abc\ndef\n"), "--want-size", "7")
    check(g, "CRLF + LF 字节数钉扎 -> crlf_drift 优先于尺寸类", jout(r)["class"] == "crlf_drift")
    open(T1 + "/e7.txt", "wb").write(b"error: file not found\n")  # 纯文本含 error，无标签
    r = run("verify", T1 + "/e7.txt", "--want", sha(b"ERROR: FILE NOT FOUND\n"), "--want-size", "24")
    check(g, "纯文本含 'error' 不误判 html_error_page", jout(r)["class"] != "html_error_page")
    open(T1 + "/e8.txt", "wb").write(b"<html><body><h1>404</h1></body></html>\n")
    r = run("verify", T1 + "/e8.txt", "--want", sha(b"x" * 38), "--want-size", "38")
    check(g, "真 HTML 404 页仍判 html_error_page", jout(r)["class"] == "html_error_page")

    # ── G9 夹具内容 ────────────────────────────────────────────────────────
    g = "G9-fixture-content"
    man_lines = [l for l in open(T1 + "/manifest.txt").read().splitlines() if l.strip() and not l.startswith("#")]
    check(g, "manifest 7 行", len(man_lines) == 7)
    # 夹具 manifest 故意把 7 个文件全部钉在 canonical 哈希上（drift 演示用）
    check(g, "manifest 全行钉 canonical 哈希+1116",
          all(l.split()[1] == want and l.split()[2] == "1116" for l in man_lines)
          and sha(rd(T1 + "/canonical.txt")) == want)
    check(g, "runbook 含内嵌围栏与坏 heredoc",
          b"```bash\n# inner fence line" in rd(T1 + "/runbook.md") and b"OPEN_LABEL" in rd(T1 + "/runbook.md"))
    check(g, "gen 输出声明确定性", "deterministic" in run("gen-fixtures", T1 + "/again").stdout)

    # ── G10 仅标准库 ───────────────────────────────────────────────────────
    g = "G10-stdlib-only"
    allowed = {"argparse", "hashlib", "json", "os", "re", "sys", "filecmp", "shutil",
               "subprocess", "tempfile", "importlib"}
    for f in ("rebuild_verify.py", "selftest.py"):
        src = open(os.path.join(HERE, f)).read()
        bad = []
        for l in src.splitlines():
            m = re.match(r"^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_]*)", l)
            if m and m.group(1) not in allowed:
                bad.append(m.group(1))
        check(g, f + " 无第三方导入", not bad, str(bad))

    # ── G11 文档幻影 ──────────────────────────────────────────────────────
    g = "G11-doc-phantoms"
    sk = open(os.path.join(ROOT, "SKILL.md")).read()
    help_txt = run("--help").stdout
    for cmd in ("verify", "manifest", "pins", "extract-steps", "wipe-audit", "gen-fixtures"):
        check(g, "SKILL 命令存在: " + cmd, cmd in sk and cmd in help_txt)
    for flag in ("--want", "--want-size", "--root", "--lang", "--write-steps"):
        check(g, "SKILL 标志存在: " + flag, flag in sk and flag in help_txt)
    for ref in ("drift_classes.md", "runbook_extraction.md", "snapshot_semantics.md"):
        p = os.path.join(ROOT, "references", ref)
        check(g, "参考存在: " + ref, os.path.exists(p) and "供参考" in open(p).read())
    check(g, "SKILL 含硬规则", "勿盲目重贴" in sk and "不修改" in sk or "只读" in sk)

    # ── G12 跨模型 JSON 契约 ──────────────────────────────────────────────
    g = "G12-json-contract"
    for args in (["verify", T1 + "/canonical.txt", "--want", want],
                 ["manifest", T1 + "/manifest.txt", "--root", T1],
                 ["pins", T1 + "/runbook.md"],
                 ["extract-steps", T1 + "/runbook.md"],
                 ["wipe-audit", T1 + "/ws"],
                 ["gen-fixtures", T1 + "/again"]):
        r = run(*args)
        try:
            d = json.loads(r.stdout)
            ok = d["tool"] == "rebuild-verify v2.0.0" and "command" in d
        except Exception:
            ok = False
        check(g, "单行 JSON + tool + command: " + args[0], ok)
    r = run("verify", T1 + "/drift_no_nl.txt", "--want", want)
    d = jout(r)
    check(g, "next_action 恒在且为字符串", isinstance(d.get("next_action"), str) and len(d["next_action"]) > 5)
    check(g, "detail 含 got/want 哈希", d["detail"]["got_sha256"] != d["detail"]["want_sha256"]
          and len(d["detail"]["got_sha256"]) == 64)

    # ── 汇总 ──────────────────────────────────────────────────────────────
    total = len(RESULTS)
    fails = [x for x in RESULTS if not x[2]]
    for grp, name, ok, dbg in fails:
        print("FAIL %s :: %s %s" % (grp, name, dbg))
    print("selftest: %d/%d PASS" % (total - len(fails), total))
    shutil.rmtree(T1, ignore_errors=True)
    shutil.rmtree(T2, ignore_errors=True)
    sys.exit(0 if not fails else 1)


if __name__ == "__main__":
    main()
