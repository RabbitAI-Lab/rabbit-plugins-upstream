#!/usr/bin/env python3
"""penguin-guard v3 — PreToolUse 硬闸（penguin-oss-suite 运行时强制层）

拦截 GitHub 写操作，按两类分级：
  A 类（发布）：git push / gh pr create
    要求 ① .oss-task/*/CHECKLIST.md 存在
        ② 某清单中 R14/放行 行为 [x] 且带证据指针（m\d{4,}|URL|引号原文|时间戳）
        ③ 勾选行声明的 证据:/落盘: 文件路径槽真实存在（路径状 token 才校验；
          m-ref/引号原话等指针型证据不校验文件系统）（v3：技能产物证据闸）
  B 类（评论/issue 写）：gh pr comment/edit/review/merge/close、gh issue comment/create/close/edit
    仅要求 ① 存在性（评论预览等门禁由 oss-workflow s2.md 文本规则承担）。

退出码（双模式，见 deny()）：
  - 桥接模式（stdin 载荷 hook_event_name=PreToolUse，dsh-hooks-claude-code 投喂形态）：
    拦截 = stdout JSON {"decision":"block","reason":...} + 退出码 0；
    放行 = 无输出 + 退出码 0。宿主 ctx.shell 包装会改写非零退出码（实测 2→1），
    dsh-hook-protocol 只认 exitCode===2（block）或 exitCode===0+stdout JSON，
    故拦截语义只能走 JSON 路径。
  - CLI 直调（本地测试/手工跑）：拦截 = stderr 消息 + 退出码 2；放行 = 退出码 0。
设计依据：
  - 2026-09-29 #752 实战——零清单裸奔 320s、评论未经预览直发（v1：存在性门禁）。
  - 2026-09-29 三场实战合成（TRIPLE-BATTLE-SYNTHESIS U4）——勾选滞后 40-138s、
    "勾了没做"：真实性优先于时序，发布类命令必须先见 R14 勾+证据（v2：时序门禁）。
  - 2026-09-29 headless 探针 probe2——退出码路径被包装层吃掉（exitCode 2→1、
    decision=pass），拦截不生效（v2.1：JSON 双模式）。
  - 2026-09-29 五场实战技能利用率审计——套件 29 能力触达 3（council 0/5、
    ocr 探测后弃用 2/5）；模型自称「已执行」而无落盘产物 = 未执行（v3：证据槽闸）。
"""
import json
import os
import re
import sys

CLASS_A = re.compile(
    r"\b(?:git\s+push|gh\s+pr\s+create)\b"
)
CLASS_B = re.compile(
    r"\b(?:"
    r"gh\s+pr\s+(?:comment|edit|review|merge|close)"
    r"|gh\s+issue\s+(?:comment|create|close|edit)"
    r")\b"
)

R14_LINE = re.compile(r"(?:R14|放行|release)", re.IGNORECASE)
CHECKED = re.compile(r"\[[xX]\]")
EVIDENCE = re.compile(
    r"(?:\bm\d{4,}\b|https?://|[“”「」『』]|“|\d{1,2}:\d{2}:\d{2})"
)
SLOT = re.compile(r"(?:证据|落盘)[：:]\s*(\S+)")
PATHLIKE = re.compile(r"(?:[\\/]|(?:\.md|\.json|\.txt|\.log|\.ya?ml|\.csv)$)")


def find_checklists(project):
    root = os.path.join(project, ".oss-task")
    out = []
    try:
        for name in os.listdir(root):
            path = os.path.join(root, name, "CHECKLIST.md")
            if os.path.isfile(path):
                out.append(path)
    except OSError:
        pass
    return out


def r14_state(paths):
    """返回 (有勾, 有带证据的勾)。"""
    checked = evidenced = False
    for path in paths:
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    if R14_LINE.search(line) and CHECKED.search(line):
                        checked = True
                        if EVIDENCE.search(line):
                            evidenced = True
        except OSError:
            continue
    return checked, evidenced


def missing_slots(paths, project):
    """扫描已勾选条目里的 证据:/落盘: 路径槽，返回不存在的文件 token 列表。

    条目 = 以 `- [` 开头的行；其后的缩进行（如 `  证据: <路径>`）属于同一
    条目，勾选状态继承。只校验路径状 token（含斜杠或以 .md/.json 等结尾）；
    m-ref、引号原话等指针型证据不触发文件系统校验。路径按项目根和清单所在
    目录两处解析。未勾选条目的槽不校验（步骤未声明执行）。
    """
    missing = []
    seen = set()
    item_start = re.compile(r"\s*-\s+\[")
    for path in paths:
        base = os.path.dirname(path)
        active = False
        try:
            with open(path, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    if item_start.match(line):
                        active = bool(CHECKED.search(line))
                    if not active:
                        continue
                    for m in SLOT.finditer(line):
                        tok = m.group(1).strip("「」『』“”\"'()（）,，。；;`")
                        if not tok or not PATHLIKE.search(tok) or tok in seen:
                            continue
                        seen.add(tok)
                        if not any(
                            os.path.isfile(os.path.join(root, tok))
                            for root in (project, base)
                        ):
                            missing.append(tok)
        except OSError:
            continue
    return missing


def deny(msg, payload):
    """拦截输出。双模式：
    - 桥接模式（stdin 载荷 hook_event_name=PreToolUse）：stdout 输出
      {"decision":"block","reason":...} 并退出 0。dsh-hook-protocol 只在
      exitCode===0 时解析 stdout JSON、exitCode===2 时认 block；实测宿主
      ctx.shell 包装会把 2 改写成 1（2026-09-29 headless 探针 probe2：
      stderr 消息完整送达但 exitCode=1、decision=pass），退出码路径不可靠，
      JSON 路径不经过包装层改写。
    - CLI 直调（本地测试/手工跑）：stderr 消息 + 退出码 2。
    reason 传给模型，承载解除方式说明。
    """
    if isinstance(payload, dict) and payload.get("hook_event_name") == "PreToolUse":
        sys.stdout.write(
            json.dumps({"decision": "block", "reason": "[penguin-guard] " + msg})
            + "\n"
        )
        return 0
    sys.stderr.write("[penguin-guard] " + msg + "\n")
    return 2


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0  # 载荷不可解析 → 不拦截（fail-open，避免桥接协议变化卡死会话）

    if not isinstance(payload, dict):
        return 0

    tool_input = payload.get("tool_input")
    cmd = ""
    if isinstance(tool_input, dict):
        cmd = str(tool_input.get("command") or tool_input.get("script") or "")

    is_a = CLASS_A.search(cmd)
    is_b = CLASS_B.search(cmd)
    if not (is_a or is_b):
        return 0

    project = (
        os.environ.get("CLAUDE_PROJECT_DIR")
        or payload.get("cwd")
        or os.getcwd()
    )
    hit = (is_a or is_b).group(0)
    paths = find_checklists(project)

    if not paths:
        return deny(
            "已拦截 GitHub 写操作：{op}\n"
            "原因：项目内不存在 .oss-task/*/CHECKLIST.md——penguin-oss-suite 规则要求 "
            "GitHub 写操作必须先经 oss-workflow 实例化任务清单（含 R14 放行与评论预览门禁）。\n"
            "解除方式：加载 oss-workflow → 按 §1 识别场景并创建 .oss-task/<任务ID>/CHECKLIST.md "
            "→ 按清单执行到对应 Gate。\n"
            "（依据：2026-09-29 #752 实战——零清单裸奔导致 61% 时间损耗）".format(op=hit),
            payload,
        )

    if is_a:
        checked, evidenced = r14_state(paths)
        if not checked:
            return deny(
                "已拦截发布类操作：{op}\n"
                "原因：清单存在但 R14/放行 未勾选——发布（push/建 PR）前必须先拿到用户放行原话 "
                "并勾选 R14、附证据指针（用户原话引用 / m-ref / URL / 时间戳）。"
                "三场实战（#758、dsh-pua#2、PR#49）勾选全部滞后于 push 40-138s，"
                "本闸把该顺序强制反转：先勾后推。\n"
                "解除方式：取得用户放行原话 → 在 .oss-task/*/CHECKLIST.md 勾选 R14 行并附证据 → 重新执行。"
                .format(op=hit),
                payload,
            )
        if not evidenced:
            return deny(
                "已拦截发布类操作：{op}\n"
                "原因：R14 已勾但勾选行没有证据指针（用户放行原话引用 / m-ref / URL / 时间戳）——"
                "空勾等同未勾（TRIPLE-BATTLE-SYNTHESIS U4：真实性优先于时序，"
                "实战曾出现「勾了没做」）。\n"
                "解除方式：在 R14 勾选行补上放行原话或证据指针后重新执行。".format(op=hit),
                payload,
            )
        missing = missing_slots(paths, project)
        if missing:
            return deny(
                "已拦截发布类操作：{op}\n"
                "原因：清单勾选行声明了产物证据文件但文件不存在：{files}——"
                "勾了但落盘物缺失 = 未执行（2026-09-29 五场实战审计：套件 29 能力触达 3，"
                "council 0/5、ocr 探测后弃用 2/5；模型自称已执行而无落盘即未执行）。\n"
                "解除方式：真正执行技能派发序列（ocr review 输出落盘 ocr.json、"
                "council 视角结论落盘 council.md），或修正证据路径后重新执行。".format(
                    op=hit, files=", ".join(missing)
                ),
                payload,
            )

    return 0


if __name__ == "__main__":
    sys.exit(main())
