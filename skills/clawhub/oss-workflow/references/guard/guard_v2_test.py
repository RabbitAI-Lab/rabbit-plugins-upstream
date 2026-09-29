# -*- coding: utf-8 -*-
"""guard v3 双模式八例×2 冒烟测试。

两种载荷形态：
- CLI 模式（无 hook_event_name）：拦截 = stderr 消息 + 退出码 2。
- 桥接模式（hook_event_name=PreToolUse，dsh-hooks-claude-code 实际投喂形态）：
  拦截 = stdout JSON {"decision":"block","reason":...} + 退出码 0。
  依据 2026-09-29 探针 probe2：宿主 ctx.shell 包装会把退出码 2 改写成 1，
  dsh-hook-protocol 对非 0 非 2 不产出 decision（记 pass），故桥接模式必须走
  stdout JSON 路径（仅 exitCode===0 时被解析）。
测试对象 = 同目录 guard.py（真源与 repo 副本各测各的）。
"""
import json, os, subprocess, sys, tempfile

GUARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guard.py")

def run_guard(project, command, bridge=False):
    payload = {"tool_input": {"command": command}, "cwd": project}
    if bridge:
        payload["hook_event_name"] = "PreToolUse"
    p = subprocess.run([sys.executable, GUARD], input=json.dumps(payload).encode("utf-8"),
                       capture_output=True)
    return p.returncode, p.stderr.decode("utf-8", "replace"), p.stdout.decode("utf-8", "replace")

def mk(tmp, name, checklist=None):
    proj = os.path.join(tmp, name)
    os.makedirs(proj, exist_ok=True)
    if checklist is not None:
        os.makedirs(os.path.join(proj, ".oss-task", "t1"), exist_ok=True)
        with open(os.path.join(proj, ".oss-task", "t1", "CHECKLIST.md"), "w", encoding="utf-8") as fh:
            fh.write(checklist)
    return proj

def bridge_blocks(out):
    try:
        doc = json.loads(out.strip().splitlines()[-1])
        return doc.get("decision") == "block" and "[penguin-guard]" in doc.get("reason", "")
    except Exception:
        return False

cases = []
with tempfile.TemporaryDirectory() as tmp:
    p1 = mk(tmp, "c1")                                                    # 无清单
    p2 = mk(tmp, "c2", "# CHECKLIST\n- [ ] R14 放行：等待用户\n- [x] P0 场景闸门：已建 m00401\n")  # R14 未勾
    p3 = mk(tmp, "c3", "# CHECKLIST\n- [x] R14 放行：用户原话“放行”（m00477）\n")  # 勾+证据
    p6 = mk(tmp, "c6", "# CHECKLIST\n- [x] R14 放行\n")                    # 空勾
    p7 = mk(tmp, "c7", "# CHECKLIST\n- [x] R14 放行：用户原话“放行”（m00477）\n"
                       "- [x] 技能派发序列三产物齐备\n  证据: .oss-task/t1/council.md\n")  # 槽文件缺
    p8 = mk(tmp, "c8", "# CHECKLIST\n- [x] R14 放行：用户原话“放行”（m00477）\n"
                       "- [x] 技能派发序列三产物齐备\n  证据: .oss-task/t1/council.md\n"
                       "- [x] ocr 缺陷检查\n  证据: ocr.json\n")            # 槽文件在（相对清单目录）
    os.makedirs(os.path.join(p8, ".oss-task", "t1"), exist_ok=True)
    for fname in ("council.md", "ocr.json"):
        with open(os.path.join(p8, ".oss-task", "t1", fname), "w", encoding="utf-8") as fh:
            fh.write("ok\n")

    spec = [
        ("T1 无清单+push", p1, "git push origin master", "deny"),
        ("T2 R14未勾+push", p2, "git push origin master", "deny"),
        ("T3 R14勾+证据+push", p3, "git push origin master", "pass"),
        ("T4 B类存在性即放", p2, "gh issue comment 1 --body hi", "pass"),
        ("T5 安全命令", p3, "git status", "pass"),
        ("T6 空勾无证据+gh pr create", p6, "gh pr create --title x", "deny"),
        ("T7 槽文件缺+push", p7, "git push origin master", "deny"),
        ("T8 槽文件在+push", p8, "git push origin master", "pass"),
    ]
    for label, proj, cmd, want in spec:
        # CLI 模式
        code, err, _ = run_guard(proj, cmd)
        want_code = 2 if want == "deny" else 0
        cases.append((f"{label} [CLI→exit{want_code}]", code == want_code,
                      f"exit={code} want={want_code} stderr={err.strip()[:120]}"))
        # 桥接模式
        code, err, out = run_guard(proj, cmd, bridge=True)
        if want == "deny":
            good = (code == 0) and bridge_blocks(out)
            cases.append((f"{label} [桥接→JSON block]", good,
                          f"exit={code} stdout={out.strip()[:120]}"))
        else:
            good = (code == 0) and not out.strip()
            cases.append((f"{label} [桥接→静默放行]", good,
                          f"exit={code} stdout={out.strip()[:120]}"))

ok = True
for label, good, detail in cases:
    print(f"[{'PASS' if good else 'FAIL'}] {label}  {detail if not good else ''}")
    ok = ok and good
print("ALL PASS" if ok else "HAS FAILURES")
sys.exit(0 if ok else 1)
