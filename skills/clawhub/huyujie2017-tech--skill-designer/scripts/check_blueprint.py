#!/usr/bin/env python3
"""
check_blueprint.py — 蓝图完成度与一致性检查（skill-designer 的系统性错误提示）

读取 init_blueprint.py 生成的蓝图 bundle，逐格报告：
缺什么、哪里不一致、下一步建议。把"靠对话猜进度"升级为"机器结构化报错"。

检查分三层：
  [逐格完整性] 文件是否存在 / 填空字段（______）是否已填 / checklist（☐）是否已勾
  [IQS 蓝图完备度] 机器按 0/5/8/10 四档给每格打分，合计 0–100（B09 的 IQS 字段，见下）
  [跨格一致性]（机器可判硬规则）
    C1  checkpoint 当前格 ∈ {Phase 0, B01..B10}
    C2  checkpoint 已完成格 ⊆ 实际已填完的格（声明完成但仍有填空 → 警告）
    C3  B01 结论=不做 → 其余格仍在填充（警告：先定结论再继续）
    C4  B05 声明涉及文件产出 → B06 输出文件约定四要素必须已填
    C5  B09 综合评分已出 → 必须指向具体改进项
    C6  index 快照（platform/entry/channel）与 frontmatter 一致
    C7  边界密度门槛（v3.15.0 移植 v4.3）：十格填齐后，全部蓝图文件的边界条目
        <15 条 或「易混淆正例」=0 → 警告（对齐 outputs/baseline-vs-with-skill.md 实证口径）
    C8  教训回流门槛（v3.15.0 移植 v4.4）：B10 记了教训却 0 条标注「已落检查项 / 不适用」
        → 警告（lessons L10/L11 的机器侧：教训停在被记录那一层 = 下次照踩）
        配套 `--tick-reflow`：自动提取「LXX → 落点」标注并写回**权威源** `library/lessons.json`
        （v3.18.0 起；md 已是生成物，写 md 会被重编译覆盖，属静默丢失）

IQS 评分锚点（每格 10 分，10 格合计 100）：
    10 = 填全且可交接（无空位 + 验收已勾）
     8 = 已填但缺关键项（填了 ≥80%，或全填完但验收未勾）
     5 = 占位空壳（填了不到 80%）
     0 = 未填 / 文件缺失
  ⚠ B09 的「内部质量分」行由机器回填，统计时排除，否则会自己拉低自己。

用法：
    python scripts/check_blueprint.py <蓝图目录>
    python scripts/check_blueprint.py <蓝图目录> --json
    python scripts/check_blueprint.py <蓝图目录> --write-iqs   # 顺手把 IQS 回填进 09-结果.md
    python scripts/check_blueprint.py <蓝图目录> --tick-lesson L01,L03   # 手敲经验规则引用
    python scripts/check_blueprint.py <蓝图目录> --tick-reflow          # C8 自动登记（推荐）
    python scripts/check_blueprint.py --self-test                        # C8 判据自回归（不需蓝图）

退出码：0 = 全部 10 格完成且无警告；1 = 有缺失/未填（结构性缺口）；
        2 = 无缺失但有一致性警告。
  ★ IQS 只作为附加信息输出，不影响上述判据与退出码。
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Optional

from retry import read_text_robust, write_text_robust
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

BLOCKS = {
    "B01": "01-条件.md", "B02": "02-事实.md", "B03": "03-观点.md", "B04": "04-问题.md",
    "B05": "05-分析.md", "B06": "06-决策.md", "B07": "07-计划.md", "B08": "08-行动.md",
    "B09": "09-结果.md", "B10": "10-复盘.md",
}
VALID_CURRENT = {"Phase 0", *BLOCKS.keys()}
BLANK = "______"

GREEN, RED, YELLOW, RESET = "\033[92m", "\033[91m", "\033[93m", "\033[0m"

LESSONS_FILE = Path(__file__).resolve().parent.parent / "references" / "lessons.md"
LESSONS_JSON = Path(__file__).resolve().parent.parent / "library" / "lessons.json"


def tick_lessons(lesson_ids: list[str], bp_name: str = "", idempotent: bool = False,
                 reflow_target: Optional[dict] = None) -> list[dict]:
    """F6 机器钩子：把实际影响决策的经验规则写回**权威源** `library/lessons.json`
    （refs +1 / lastHit / reflow），随后重编译 `references/lessons.md`。

    闭环必须有机器写入点——凡是"用到了就记一笔"的规则，绑定到必然执行的 check_blueprint
    上，不再依赖 agent 口头执行 + 人手动 +1（靠"记得做"的闭环长期一定归零）。

    ⚠️ 阶段 1 修正（真 bug）：本函数原先直接正则改写 `references/lessons.md`。
    lessons.md 降级为**生成物**后，那条路径会：① 下次 `compile_library --write` 覆盖掉
    本次写入（**静默丢失**，正是 L11「实现完 ≠ 会生效」的同款）；② 让 C5 报 E013。
    现在写权威源 + 重编译——**写回点和渲染器共享单一事实源**（DP-209）。

    v3.15.0 增补两条（移植自姊妹分支 v4.4.0 的 C8 自动登记）：
      - reflow_target: {LID: 落点描述} → 同批写入回流落点，使每条教训的机器落点可反查。
      - idempotent: 同一天同一蓝图的同一条已登记则跳过，不重复 +1
        （--tick-reflow 是"每次跑 check 都可以跑"的操作，不幂等会把计数刷爆）。
    返回每条的 tick 结果：{"id", "ok", "refs", "detail"}。
    """
    from datetime import date

    results: list[dict] = []
    reflow_target = reflow_target or {}
    if not LESSONS_JSON.is_file():
        return [{"id": i, "ok": False, "refs": None,
                 "detail": f"权威源不存在：{LESSONS_JSON}（阶段1 起 lessons 的状态写在 library/lessons.json）"}
                for i in lesson_ids]
    try:
        data = json.loads(read_text_robust(LESSONS_JSON))
        items = {l["id"]: l for l in data["entries"]}
    except (ValueError, OSError, KeyError) as e:
        return [{"id": i, "ok": False, "refs": None,
                 "detail": f"library/lessons.json 不可解析（{type(e).__name__}: {e}）"}
                for i in lesson_ids]

    today = date.today().isoformat()
    changed = False
    for raw in lesson_ids:
        lid = re.sub(r"^L0*(?=\d)", "L", raw.strip().upper())  # L01/L001 → L1
        l = items.get(lid)
        if l is None:
            results.append({"id": lid, "ok": False, "refs": None, "detail": "条目不存在"})
            continue
        stamp = f"{today}（{bp_name}）" if bp_name else today
        l["lastHit"] = l.get("lastHit", "") or ""
        l["reflow"] = l.get("reflow", "") or ""
        target = reflow_target.get(lid, "").strip()
        # 幂等闸：同一天 + 同一蓝图已记一笔 → 视为重复登记，跳过计数但允许补写回流落点
        already = bool(idempotent and bp_name and today in l["lastHit"] and bp_name in l["lastHit"])
        if target:
            # 扁平戳（`2026-09-11 · bp`）而非 stamp 的 `2026-09-11（bp）`——
            # 外面已有一层括号，再套一层会出现「（2026-09-11（bp））」这种嵌套脏串。
            flat = f"{today} · {bp_name}" if bp_name else today
            l["reflow"] = f"{target}（{flat}）"
            changed = True
        if already:
            note = "本轮已登记，跳过重复计数"
            if target:
                note += "；回流落点已同步"
            results.append({"id": lid, "ok": True, "refs": int(l.get("refs", 0)), "detail": note})
            continue
        l["refs"] = int(l.get("refs", 0)) + 1
        l["lastHit"] = stamp
        changed = True
        results.append({"id": lid, "ok": True, "refs": l["refs"],
                        "detail": f"引用计数 +1 → {l['refs']}，最近命中 {stamp}"
                                  + (f"；回流落点：{target}" if target else "")})

    if changed:
        with open(LESSONS_JSON, "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        # 重编译：否则 md（生成物）落后于权威源 → knowledge verify 的 C5 会报 E013。
        # 失败不吞：把错误原样带进 detail，让上层看得见（DP-210 熔断不静默兜底）。
        rc, msg = recompile_views()
        if rc != 0:
            for r in results:
                if r["ok"]:
                    r["detail"] += f"；⚠️ 重编译失败（{msg}）→ md 已落后于权威源，须人工处理"
    return results


def recompile_views() -> tuple[int, str]:
    """把整条**派生链**刷成与权威源一致：md 视图 + 条目索引 manifest。

    为什么要连 manifest 一起刷：manifest 是从 md 解析出来的派生件（refs 也在里面）。
    只刷 md 会让 C1「索引↔权威源指纹」立刻报 E009——即一次**合法的运行态写回**
    反而把仓库带到不一致状态。写回点有责任让整条链闭合，而不是留给下次人工补救。

    返回 (退出码, 摘要)。**不吞异常**：失败原样上行，交由调用方决定是否熔断。
    """
    root = Path(__file__).resolve().parent.parent
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import compile_library  # 延迟导入：只在真正写回时才需要
        rc, written, issues, _notes = compile_library.write_all(root)
        if rc != 0:
            return rc, "；".join(issues[:3])
        import knowledge
        mf = knowledge.build_manifest(root)
        with open(knowledge.manifest_path(root), "w", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(mf, ensure_ascii=False, indent=2) + "\n")
        return 0, f"{len(written)} 份视图 + 索引（{mf['total']} 条 / {mf['libraryVersion']}）已刷新"
    except Exception as e:  # noqa: BLE001 —— 必须让任何失败都可见，不得静默
        return 1, f"{type(e).__name__}: {e}"


C8_SELF_TEST_CASES = [
    # (名称, B10 文本, 期望是否报警)
    ("有教训·无回流", "- 失败：dist 停在旧版\n- 教训：门禁验源不验包\n- 经验：要加 testzip", True),
    ("同行写落点", "- 教训 → 检查项：L10 → validate_skill 第 15 项", False),
    ("教训与豁免分两行", "- 教训：某坑\n- 不适用落检查项：属一次性环境问题", False),
    ("无教训", "- 经验：一切顺利", False),
    ("全是占位未填", "- 失败/不足：______\n- 教训 → 检查项（必答）：______", False),
    # 「门禁」这类泛词不能算回流——批评门禁 ≠ 已处理（姊妹分支 v4.4.1 修复的正是这条）
    ("教训内容含泛词「门禁」", "- 失败/不足：门禁全绿但发布包是旧的\n- 教训：门禁验源不验包", True),
]


# ── C7 边界密度**口径**自回归（v3.19.0，F2）───────────────────────────
# 为什么必要：v3.19.0 把口径收紧了（引用 / 提问 / 勾选 ≠ 声明边界）。这类判据最容易
# 「改完看着对、实则永远不响」——所以把正反边界样本固化成断言，改口径必须让它继续全绿。
# 每条都是**单行文本**，直接喂 boundary_stats，判据只此一处（DP-209）。
C7_SELF_TEST_CASES = [
    # (名称, 单行文本, 期望边界条目数, 期望易混淆正例数)
    ("陈述式声明 → 计入",         "- 不做与设计流程无关的通用文档排版", 1, 0),
    ("「不该」→ 计入",            "- 不该替代目标 skill 自身的业务判断", 1, 0),
    ("表格行命中 → 计入",         "| 2 | 不做行情与医学业务 | B01 |", 1, 0),
    ("引号**内不是**关键词 → 仍计入", "- 不做「PPT」类通用排版产物", 1, 0),
    ("疑问句 → 不计",             "- 它负责什么、不负责什么？", 0, 0),
    ("复选行（☑）→ 不计",         "- ☑ 有明确结论：做 / 不做 / 转向", 0, 0),
    ("引号引用 → 不计",           "- **④ 分发与安装（其余形态写「不适用」）**：已填示例", 0, 0),
    ("未填空位（______）→ 不计",   "- 不做______", 0, 0),
    ("未勾验收（☐）→ 不计",       "- ☐ 不接管发布上线流程", 0, 0),
    ("非列表 / 非表格行 → 不计",   "本节说明不做什么（说明性段落）", 0, 0),
    ("易混淆正例 → 剥引号后仍匹配", "- 易混淆正例：看似「通用文档排版」其实该本 skill 管", 0, 1),
]


def run_self_test() -> int:
    """C7 / C8 判定回归：内置样例跑一遍，确认门槛没退化。

    C8 部分——为什么必要：姊妹分支 C8 曾被三个缺陷同时废掉——① 被 gate 在 `errors==0` 里，逐格迭代时永不生效；
    ② 回流判据含「门禁」等泛词，导致批评门禁的反面描述被当成「已处理」；③ 要求同行共现，
    而模板里「教训」与「检查项」本就是两个字段。三者叠加的结果：功能**表面上实现完毕**，
    实则一次都没真正报过警（教训见 lessons L11）。所以把修复时的验收样本固化成命令——
    以后改判据必须让它继续全绿。

    C7 部分（v3.19.0 新增）——口径收紧了「引用 / 提问 / 勾选 ≠ 声明边界」三条，
    正反样本各若干，防止收紧后**误伤真实条目**或**噪音又溜回来**。
    """
    print("[check_blueprint] C8 教训回流门槛 —— 自回归测试\n")
    failures = 0
    for name, body, expect in C8_SELF_TEST_CASES:
        n_lesson, n_reflow = lesson_reflow_stats(body)
        actual = n_lesson >= 1 and n_reflow < LESSON_MIN_REFLOW
        ok = actual == expect
        failures += 0 if ok else 1
        mark = f"{GREEN}✔{RESET}" if ok else f"{YELLOW}✘{RESET}"
        print(f"  {mark} {name}：教训{n_lesson} 回流{n_reflow} → "
              f"{'报警' if actual else '不报'}（期望{'报警' if expect else '不报'}）")
    # 顺带验提取函数：同一份文本要能认出 L ID
    regs = reflow_registrations("- 教训 → 检查项：L10 → validate_skill 第 15 项")
    ok_ext = regs == [("L10", "validate_skill 第 15 项")]
    failures += 0 if ok_ext else 1
    print(f"  {GREEN + '✔' + RESET if ok_ext else YELLOW + '✘' + RESET} "
          f"回流提取：{regs}（期望 [('L10', 'validate_skill 第 15 项')]）")
    # ── C7 边界密度**口径**自回归（v3.19.0，F2）─────────────────────
    # v3.19.0 把口径收紧了（引用 / 提问 / 勾选 ≠ 声明边界）。这类判据最容易
    # 「改完看着对、实则永远不响」——正反样本都固定在这里，改口径必须让它继续全绿。
    print("\n[check_blueprint] C7 边界密度口径 —— 自回归测试\n")
    for name, text, exp_items, exp_conf in C7_SELF_TEST_CASES:
        i, p = boundary_stats(text)
        ok = (i == exp_items and p == exp_conf)
        failures += 0 if ok else 1
        mark = f"{GREEN}✔{RESET}" if ok else f"{YELLOW}✘{RESET}"
        print(f"  {mark} {name}：边界{i}/易混淆{p}（期望 {exp_items}/{exp_conf}）")

    print(f"\n{'✅ C7+C8 自回归全过' if failures == 0 else f'❌ {failures} 档不符预期，判据已退化'}")
    return 0 if failures == 0 else 1


# ── C7 边界密度门槛（v3.15.0 移植自姊妹分支 v4.3）─────────────────────
# 背景：有/无 skill 对比实证（outputs/baseline-vs-with-skill.md）显示，
# 自动出稿的边界条目密度（11 条）显著低于深度人工设计（18 条），且对照组
# 有「易混淆正例」防误伤设计而实验组没有——这是平台评审两次点名的已知短板。
# 统计口径与该实证文档一致，可手工复现；把「边界补全」从靠人记变成机器守。
BOUNDARY_KEYWORDS = ("不做", "不该", "排除", "拒绝", "非目标", "不适用",
                     "不接管", "不负责", "停用", "降级为", "不属于", "不处理")
BOUNDARY_MIN = 15          # 边界条目门槛（实证对照组 18 条，取保守值 15）
BOUNDARY_CONFUSABLE_MIN = 1  # 易混淆正例至少 1 条（防误伤设计）
CONFUSABLE_RE = re.compile(r"易混淆|防误伤|看似.{0,14}其实|以为是.{0,18}其实")
_LIST_ITEM_RE = re.compile(r"^\s*[-*]\s+")
_TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:\-|]+\|?\s*$")  # 表头分隔行 |---|---|
# ── v3.19.0（F2 收紧）：把「声明了一条边界」与「在讲怎么写 / 在提问 / 在勾验收」分开 ──
_CHECKBOX_LINE_RE = re.compile(r"^\s*(?:[-*]\s+)?[☑☐]")          # 复选行 = 验收勾选，不是边界声明
_QUESTION_TAIL_RE = re.compile(r"[？?]\s*$")                      # 疑问句：提问 ≠ 声明
_QUOTED_SPAN_RE = re.compile(r"[「『“\"'][^」』”\"']*[」』”\"']")   # 引号引用：引 ≠ 声明


def _declares_boundary(ln: str) -> bool:
    """这一行是否**自己声明**了一条边界（而不是在讲怎么写 / 提问 / 勾验收）。

    为什么必须区分（v3.19.0，F2 实测）：模板里三行引导语在蓝图**填完后**会被计入边界条目——
      · B01「☑ 有明确结论：做 / 不做 / 转向」
      · B07「…其余形态写「不适用」」
      · B10「…写明「不适用」及理由…」
    空填蓝图时它们被 `☐` 过滤器掩盖（模板里是未勾状态），**一旦用户勾了验收就冒出来**。
    实测夹具 20 条里 3 条是这么来的——真实条目只有 17 条（门槛 15），
    等于门槛的 1/5 是噪音，表面余量 5 条、真实余量仅 2 条。排掉后门槛口径**更严**（I4：只增不减）。

    ⚠ 剥离引号**只作用于关键词匹配**。易混淆正例的判据（`看似「X」其实`）恰恰靠引号，
    所以 `boundary_stats` 里 CONFUSABLE_RE 仍然匹配**原始行**，不走这条路径。
    """
    if _CHECKBOX_LINE_RE.match(ln):
        return False
    if _QUESTION_TAIL_RE.search(ln):
        return False
    return any(k in _QUOTED_SPAN_RE.sub("", ln) for k in BOUNDARY_KEYWORDS)


def boundary_stats(text: str) -> tuple[int, int]:
    """统计一段蓝图文本的（边界条目数, 易混淆正例数）。

    口径（与 outputs/baseline-vs-with-skill.md 一致）：
      边界条目 = 列表项（- / * 开头）或表格行（含 | 且非分隔行），
                 且命中 BOUNDARY_KEYWORDS 之一，且**是自己声明的**（见 _declares_boundary）；
      未填字段（含 ______）与未勾验收（含 ☐）不算证据；
      易混淆正例 = 命中「易混淆 / 防误伤 / 看似…其实 / 以为是…其实」的行。
    """
    items = pos = 0
    for ln in text.splitlines():
        if "______" in ln or "☐" in ln:
            continue
        is_item = bool(_LIST_ITEM_RE.match(ln)) or ("|" in ln and not _TABLE_SEP_RE.match(ln))
        if is_item and _declares_boundary(ln):
            items += 1
        if CONFUSABLE_RE.search(ln):   # ⚠ 用**原始行**：正例判据本身就靠引号
            pos += 1
    return items, pos


# ── C8 教训回流门槛（v3.15.0 移植自姊妹分支 v4.4.0）────────────────────
# 背景：姊妹分支 v4.4.0 吸收官方元技能时「回照自己」连抓三个 bug，**全部同源**——
# 有「记录」机制，缺「回流」机制：① 条目入了库却漏三处索引；② 英文冒号坑只做个案修复、
# 未沉淀检查项；③ prepare_release 有 --sync-dist 而 sd_cli package 从未调用（门禁验源不验包）。
# 教训进了 CHANGELOG 就算完事、能力写了没人接进主流程 = 下次照踩。
# 对应 lessons L10/L11；C8 把它从「靠人记」升级为「机器拦」（元设计一：约束机器化）。
LESSON_RE = re.compile(r"教训|踩坑|失败|根因|返工|复发|踩过的坑")
# ⚠ 这里必须是「动作/落点」，不能是泛名词。姊妹分支初版把 `门禁`/`validate`/`check_blueprint`
# 列进关键词，结果「教训：门禁验源不验包」这种**反面描述**也被判成「已回流」——
# C8 从此再没报过一次警（教训内容是批评门禁，却被当成已经处理）。
# 判据收紧为四选一：①明确的落成动作 ②「检查项：」后真有内容 ③明确豁免词 ④写明了落点箭头。
REFLOW_RE = re.compile(
    r"已(?:落|加|补|建)[^，。；\n]{0,12}(?:检查项|检查|正则|枚举|门槛|钩子)|"  # ① 已落检查项 / 已加检查项
    r"检查项\s*[：:]\s*\S+|"                                                  # ② 检查项：有内容
    r"不适用|无需(?:落|加)|不可机器(?:化|判定)|无法机器判定|判不了|"             # ③ 明确豁免
    r"→\s*\S+"                                                                # ④ 写明落点
)
LESSON_MIN_REFLOW = 1   # 凡记录了教训，至少一条要标「已落检查项」或「不适用（理由）」


def reflow_registrations(text: str) -> list[tuple[str, str]]:
    """从 B10 文本提取「已回流」标注里的 (lessons ID, 落点描述)，供 --tick-reflow 自动登记。

    识别形态（人与 AI 的常见写法都收）：
      - 教训 → 检查项：L10 → validate_skill 第 15 项（机器查裸冒号）
      - 已落检查项：L10 —— check_blueprint C8
      - 不适用落检查项：L11（理由：属一次性环境问题，无法机器判定）
    口径与 C8 一致：只认列表项与表格行；一行含多个 ID 时逐个登记，落点共用。
    """
    out: list[tuple[str, str]] = []
    for ln in text.splitlines():
        if "______" in ln or "☐" in ln:
            continue
        is_item = bool(_LIST_ITEM_RE.match(ln)) or ("|" in ln and not _TABLE_SEP_RE.match(ln))
        if not is_item:
            continue
        ids = re.findall(r"L0*(\d+)\b", ln)
        if not ids:
            continue
        # 判定为「回流标注行」：含回流关键词，或用了箭头（箭头本身就是在写流向）。
        # 只认关键词会漏掉表格行写法（如 `| 教训 | L10 → sd_cli ... |` 无关键词却有明确流向）。
        if not (REFLOW_RE.search(ln) or "→" in ln or "->" in ln):
            continue
        for i in ids:
            out.append((f"L{i}", _reflow_target_of(ln, i)))
    # 同一 ID 多次出现取最长描述（信息更全）；保持首次出现顺序
    merged: dict = {}
    for lid, tgt in out:
        if lid not in merged or len(tgt) > len(merged[lid]):
            merged[lid] = tgt
    return list(merged.items())


def _reflow_target_of(line: str, lid: str) -> str:
    """从一行标注里剥出「落点」描述——三种常见写法都要能读：
    「L10 → validate_skill 第 15 项」/「L10 —— check_blueprint C8」/「不适用：L11（理由）」。
    """
    for sep in ("→", "->"):
        if sep in line:
            tail = line.split(sep)[-1]
            break
    else:
        tail = re.split(r"[：:]", line, maxsplit=1)[-1] if re.search(r"[：:]", line) else line
    tail = tail.strip().strip("|-—–*").strip()
    # 去掉行首冗余的自身 ID（破折号写法里落点常以「L10 ——」开头）
    tail = re.sub(rf"^L0*{re.escape(lid)}\b\s*[—–\-:：]*\s*", "", tail)
    # 剥掉不成对的收尾括号（源于原文被截断）
    while tail.endswith(("）", ")")) and (tail.count("）") + tail.count(")")
                                          > tail.count("（") + tail.count("(")):
        tail = tail[:-1]
    return tail.strip() or line.strip()[:60]


def lesson_reflow_stats(text: str) -> tuple[int, int]:
    """统计（教训条数, 已回流条数）。口径与 C7 一致：只认列表项与表格行。

    ⚠ 两个计数**按「文件」而非「同行」统计**：
    初版要求「教训」与「回流关键词」出现在同一行，但真实模板里它们是两个字段——
    「失败/不足：xxx」一行、「教训 → 检查项：不适用（理由）」另一行，于是写了豁免照样报警。
    C8 问的是「B10 有没有答过这道必答题」，那就该看整份文件是否出现过回答，而不是行内共现。
    """
    lessons = reflowed = 0
    for ln in text.splitlines():
        if "______" in ln or "☐" in ln:
            continue
        is_item = bool(_LIST_ITEM_RE.match(ln)) or ("|" in ln and not _TABLE_SEP_RE.match(ln))
        if not is_item:
            continue
        if LESSON_RE.search(ln):
            lessons += 1
        if REFLOW_RE.search(ln):
            reflowed += 1
    return lessons, reflowed


def read(p: Path) -> str:
    """带重试的蓝图文件读取；IO 失败时返回空字符串，不阻塞检查流程。"""
    try:
        return read_text_robust(p)
    except OSError:
        return ""


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---", text.lstrip(), re.DOTALL)
    fm: dict[str, str] = {}
    if not m:
        return fm
    for line in m.group(1).splitlines():
        kv = re.match(r'^([A-Za-z_][\w-]*)\s*:\s*"?(.*?)"?\s*$', line)
        if kv:
            fm[kv.group(1)] = kv.group(2)
    return fm


def parse_checkpoint(text: str) -> dict:
    """从 index.md 的 checkpoint 表提取五字段。"""
    cp: dict[str, str] = {}
    m = re.search(r"##\s*进度快照.*?\n((?:\|[^\n]*\n)+)", text, re.DOTALL)
    if not m:
        return cp
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2 and cells[0] not in ("字段", "----", "------", "---"):
            cp[cells[0]] = cells[1]
    return cp


def field_lines(text: str) -> list[str]:
    """提取仍含填空位的字段行（去掉 markdown 前缀）。"""
    return [re.sub(r"^[\s>-]+", "", ln).strip()
            for ln in text.splitlines() if BLANK in ln]


def unchecked(text: str) -> list[str]:
    """收集「验收 checklist」段落下仍未勾的项（☐）。

    ⚠️ 不能全文扫 ☐——B01 的「准入四问：☐ 形态合规 ☐ 非元信息…」是**字段**，
    结论字段的括号里也常出现 ☐（如「复用检验 ☐ 待③深化设计确认」），
    它们都不是 checklist 项。全文扫会把这两行误算成未勾，IQS 永远卡在 94。

    找不到「验收 checklist」标题时回退全文扫描，保证旧蓝图/手写蓝图不被漏判。
    """
    out: list[str] = []
    in_sec = False
    for ln in text.splitlines():
        s = ln.strip()
        if re.match(r"^#{1,6}\s*验收", ln) or s.startswith("验收 checklist"):
            in_sec = True
            continue
        if in_sec and re.match(r"^#{1,6}\s", ln):
            break  # 进入下一节 → checklist 段落结束
        if in_sec and "☐" in ln:
            out.append(re.sub(r"^[\s>-]*☐\s*", "", ln).strip())
    if in_sec:  # 找得到该段落就以段落为准（哪怕 0 项未勾）
        return out
    return [re.sub(r"^[\s>-]*☐\s*", "", ln).strip()
            for ln in text.splitlines() if "☐" in ln]


# B09 的「内部质量分」由机器回填，统计完成度时排除，避免自拉自低
MACHINE_FILLED = {"B09": r"内部质量分"}

# IQS 四档锚点：填够这个比例算「已填但缺关键项(8)」，否则算「空壳(5)」
FILLED_RATIO_OK = 0.8

# 模板字段原文（用于识别「选择题未选」这类无空位但也没填的字段）
# 导入失败时退化为空集——不影响主流程，只是少判一类未填项
try:
    from blocks import BLOCKS as _BLOCK_DEFS, dims_for_block
    _DEFS_BY_FILE = {b["file"]: b for b in _BLOCK_DEFS}
except Exception:  # pragma: no cover - blocks.py 缺失时的兜底
    _DEFS_BY_FILE = {}

    def dims_for_block(bid: str) -> list[str]:  # type: ignore[misc]
        return []


# 四步术语改名（投料/出稿/深化/定稿 → 概念讨论/初步方案/深化设计/施工蓝图）后，
# blocks.py 模板里的措辞变了，但磁盘上已有的旧蓝图还是旧措辞。
# 若不做归一，旧蓝图里那一行会被判成「模板行不存在 = 已填」，IQS 虚高。
# 归一方向：新术语 → 旧术语（统一到一个 canonical 形式即可，方向本身不重要）。
_TERM_EQUIV = (
    ("施工蓝图", "定稿"),
    ("概念讨论", "投料"),
    ("初步方案", "出稿"),
    ("深化设计", "深化"),
)


def _canon(line: str) -> str:
    """四步术语归一，使新旧措辞可比。"""
    for new, old in _TERM_EQUIV:
        line = line.replace(new, old)
    return line


def _norm(line: str) -> str:
    """归一化字段行：剥掉 markdown 列表前缀与首尾空白，使模板项与文件行可比。"""
    return _canon(re.sub(r"^[\s>-]+", "", line).strip())


_CHOICE_PAREN = re.compile(r"[（(][^）)]*[）)]")
_CHOICE_BLANK = re.compile(r"^[_\s　]+$")


def selected_choice(value: str) -> str:
    """从选择题取值里取「已选中的那一项」；模板原样（候选仍在多个）时返回 ''。

    B01 结论这类选择题行，模板原文天然含有「不做」二字
    （`结论：**创建** / **继续蒸馏**… / **不做**（…）/ 转向（______）`）。
    若只做「包含不做」的子串判断，未选时整行原样就会被误判成结论=不做，
    让一个满分蓝图永远退不出 C3 警告态。
    判定口径：剥掉加粗与括号注释后仍剩 ≥2 个候选 → 未选；只剩 1 个 → 那就是结论。
    """
    v = _CHOICE_PAREN.sub("", value.replace("**", ""))
    opts = [o.strip() for o in v.split("/")]
    opts = [o for o in opts if o and not _CHOICE_BLANK.match(o)]
    return opts[0] if len(opts) == 1 else ""


def template_fields(bid: str, fname: str) -> set[str]:
    """该格在 blocks.py 里的模板字段原文集合（已归一化，与文件行同一口径）。"""
    blk = _DEFS_BY_FILE.get(fname)
    if not blk:
        return set()
    return {_norm(f) for f in blk.get("fields", []) if f.strip()}


# 选择题型：冒号后出现「 / 」分隔的候选项，如「结论：做 / 不做 / 转向」
_CHOICE_HINT = re.compile(r"[:：][^/:：]*\s/\s")
# 分组标题：冒号就是行尾，如「输出文件约定（…必填四要素）：」
_SECTION_TITLE = re.compile(r"[:：]\s*$")


def is_fillable(item: str) -> bool:
    """模板项是否为「可机器判定的待填字段」。

    只统计能判的，判不了的不扣分——否则像「错误台账：把本轮失败按…append 进 MISTAKES.md」
    这类纯说明型字段会被永远判为未填，把分数压死。

    属于待填字段的三类：
      1. 含填空位 `______`；
      2. 含 checkbox `☐`；
      3. 选择题型（冒号后出现 " / " 分隔候选项）。
    明确排除：冒号结尾的分组标题、以及无填空标记的说明行。
    """
    if BLANK in item or "☐" in item:
        return True
    if _SECTION_TITLE.search(item):
        return False
    return bool(_CHOICE_HINT.search(item))


def field_stats(fname: str, text: str, exclude: str | None = None) -> tuple[int, int]:
    """统计 (应填字段总数, 已填字段数)。

    判据：**拿 blocks.py 的模板字段逐条去文件里匹配——原样还在 = 未填，被改写或删除 = 已填。**

    这样一次解决两类「看起来填了其实没填」的情形：
      1. 仍含填空位 `______`；
      2. 无空位的**选择题**未选，如「结论：做 / 不做 / 转向」——只数空位会把它误判为已填。
    同时天然排除了「结构公式：…」这类说明行与 `☐` checklist 项（它们不在模板 fields 里）。
    """
    tmpl = template_fields(fname, fname)
    items = [f for f in tmpl if is_fillable(f)]
    if exclude:
        items = [f for f in items if not re.search(exclude, f)]
    if not items:  # 非本模板生成的蓝图：退化为空位统计
        lines = [_norm(ln) for ln in text.splitlines()]
        field_lines = [s for s in lines if ("：" in s or ":" in s) and "☐" not in s]
        blanks = [s for s in field_lines if BLANK in s]
        return len(field_lines) or 1, len(field_lines) - len(blanks)

    present = {_norm(ln) for ln in text.splitlines()}
    filled = sum(1 for f in items if f not in present)
    return len(items), filled


def block_iqs(bid: str, fname: str, exists: bool, text: str, boxes: list[str]) -> tuple[int, str]:
    """按 0/5/8/10 四档给一格打分，返回 (分数, 说明)。"""
    if not exists or not text.strip():
        return 0, "文件缺失"
    total, filled = field_stats(fname, text, MACHINE_FILLED.get(bid))
    if filled == 0:
        return 0, "未填"
    ratio = filled / total
    if ratio >= 1.0:
        if boxes:
            return 8, f"字段填全，但 {len(boxes)} 项验收未勾"
        return 10, "填全且可交接"
    if ratio >= FILLED_RATIO_OK:
        return 8, f"已填 {filled}/{total}，缺 {total - filled} 项"
    return 5, f"仅填 {filled}/{total}，仍属空壳"


def _block_labels(blocks: list[dict]) -> list[str]:
    """待补格的展示标签：能涨 BR-5 维度的格标出来，如「B06(涨T/R/A)」。"""
    labels = []
    for b in blocks:
        if b["iqs_score"] >= 10:
            continue
        labels.append(f"{b['block']}(涨{'/'.join(b['dims'])})" if b["dims"] else b["block"])
    return labels


def write_iqs(bp: Path, score: int) -> bool:
    """把机器算出的 IQS 回填进 09-结果.md 的「内部质量分」字段。已填数字则覆盖。

    顺带把「机器验证」里的「☐ 已跑 check_blueprint.py」勾成 ☑——本函数被调到，
    就说明 check_blueprint 确实跑过了。与 B07「已跑 visualize_blueprint.py」
    按实际产出勾选是同一个道理，不假勾没跑过的项（validate_skill.py 那项不动）。
    """
    p = bp / "09-结果.md"
    text = read(p)
    if not text:
        return False
    # 值部分 = 冒号后到「行尾 / 半角( / 全角(」之前的一切。
    # 不能只认 ______ 或数字——用户可能先手填了「待定」「85分」这类非数字值，那些也要能被机器覆盖。
    new, n = re.subn(
        r"(内部质量分[^:：\n]*[:：]\s*)[^（(\n]*",
        rf"\g<1>{score}",
        text, count=1,
    )
    if n == 0:
        return False
    # 只勾 check_blueprint 那一项：精确匹配到「（蓝图完整性」为止，避免误勾后面的项
    new = new.replace("☐ 已跑 scripts/check_blueprint.py（蓝图完整性",
                      "☑ 已跑 scripts/check_blueprint.py（蓝图完整性")
    write_text_robust(p, new)
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description="蓝图完成度检查（skill-designer）")
    ap.add_argument("blueprint", nargs="?", default="",
                    help="蓝图 bundle 目录（含 index.md 与 01–10 子积木）")
    ap.add_argument("--json", action="store_true", help="结构化输出")
    ap.add_argument("--write-iqs", action="store_true",
                    help="把机器算出的 IQS 回填进 09-结果.md 的「内部质量分」字段（已填则覆盖）")
    ap.add_argument("--tick-lesson", default="",
                    help="F6 机器钩子：本任务实际用到的经验规则 ID（逗号分隔，如 --tick-lesson L01,L03），"
                         "写回 references/lessons.md 引用计数 +1 与最近命中日期（不需要蓝图目录）")
    ap.add_argument("--tick-reflow", action="store_true",
                    help="C8 自动登记（v3.15.0）：从 B10 的「已落检查项：LXX → 落点」标注自动提取 lessons ID，"
                         "写回引用计数 / 最近命中 / 回流落点——勾选即登记，无需手敲 --tick-lesson；"
                         "幂等：同一天同一蓝图不重复 +1")
    ap.add_argument("--self-test", action="store_true",
                    help="C7+C8 判据自回归：跑内置样例，确认门槛口径没退化（不需要蓝图目录）")
    args = ap.parse_args()

    # --self-test 不需要蓝图，先于一切校验执行
    if args.self_test:
        return run_self_test()

    # F6：经验规则引用计数机器写回（先于主检查执行，结果随主输出一并汇报）
    # 放在缺参检查之前——手动 tick 不需要蓝图目录（bp_name 取空即只记日期）。
    tick_results: list[dict] = []
    if args.tick_lesson.strip():
        ids = [x for x in re.split(r"[,，\s]+", args.tick_lesson.strip()) if x]
        tick_results = tick_lessons(ids, bp_name=Path(args.blueprint).name)
        for t in tick_results:
            mark = GREEN if t["ok"] else YELLOW
            print(f"  {mark}{'✔' if t['ok'] else '✘'}{RESET} {t['id']}：{t['detail']}")
        if not args.blueprint:
            return 0 if all(t["ok"] for t in tick_results) else 1

    if not args.blueprint:
        print("[check_blueprint] 错误：缺蓝图目录参数（或改用 --self-test 跑 C8 自回归）", file=sys.stderr)
        return 1

    bp = Path(args.blueprint)
    if not bp.is_dir() or not (bp / "index.md").exists():
        msg = f"不是有效蓝图目录（缺 index.md）：{bp}"
        if args.json:
            print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
        else:
            print(f"[check_blueprint] 错误：{msg}", file=sys.stderr)
        return 1

    # C8 自动登记（v3.15.0）：B10 只要写了「已落检查项：LXX → 落点」，就在本次检查里
    # 自动写回 lessons.md 的引用计数与回流落点——把「勾选」变成有持久化后果的动作。
    # 绑定在必然执行的 check_blueprint 上，而不是"别忘了跑一条命令"。
    if getattr(args, "tick_reflow", False):
        b10 = bp / BLOCKS["B10"]
        regs = reflow_registrations(read(b10)) if b10.is_file() else []
        if regs:
            tick_results += tick_lessons([lid for lid, _ in regs], bp_name=bp.name,
                                         idempotent=True, reflow_target=dict(regs))
        else:
            tick_results.append({"id": "-", "ok": True, "refs": None,
                                 "detail": "B10 未检出「LXX → 落点」形式的回流标注，本次无登记"
                                           "（应写：`教训 → 检查项：L10 → validate_skill 第 15 项`）"})

    index_text = read(bp / "index.md")
    fm = parse_frontmatter(index_text)
    cp = parse_checkpoint(index_text)

    # ─── 逐格完整性 + IQS 完备度打分 ───
    blocks, errors, done_set = [], 0, set()
    for bid, fname in BLOCKS.items():
        p = bp / fname
        text = read(p)
        if not text:
            # ⚠ 键必须与下面「完成/未填完」两条分支保持一致，尤其 `dims`——
            # 汇总处 `b["dims"]` 无条件取值，缺键会让**任一格文件缺失**时整个脚本 KeyError 崩溃
            # （移植自查实证：新建蓝图只放了 index.md 和 10-复盘.md → 直接 traceback 退出）。
            blocks.append({"block": bid, "file": fname, "status": "缺失",
                           "blanks": [], "unchecked": [], "hint": "文件不存在——用 init_blueprint.py 重新生成该格",
                           "iqs_score": 0, "iqs_note": "文件缺失",
                           "dims": dims_for_block(bid)})
            errors += 1
            continue
        blanks, boxes = field_lines(text), unchecked(text)
        # 机器回填项（如 B09 的 IQS）不算「待填空位」——它由 --write-iqs 自动填，
        # 提示用户去手填只会造成困惑（与实际判分口径不一致）。
        if bid in MACHINE_FILLED:
            blanks = [b for b in blanks if not re.search(MACHINE_FILLED[bid], b)]
        iqs_score, iqs_note = block_iqs(bid, fname, True, text, boxes)
        if blanks or boxes:
            status = "未填完" if blanks else "未勾验"
            errors += 1
            hint = f"先填 {len(blanks)} 个空" if blanks else f"勾完 {len(boxes)} 项验收"
            entry = {"block": bid, "file": fname, "status": status,
                     "blanks": blanks, "unchecked": boxes, "hint": hint,
                     "iqs_score": iqs_score, "iqs_note": iqs_note}
        else:
            entry = {"block": bid, "file": fname, "status": "完成",
                     "blanks": [], "unchecked": [], "hint": "",
                     "iqs_score": iqs_score, "iqs_note": iqs_note}
            done_set.add(bid)
        # IQS × BR-5 联动：这一格填好能涨哪些维度
        entry["dims"] = dims_for_block(bid)
        blocks.append(entry)

    # ─── IQS 蓝图完备度汇总（满分 100） ───
    iqs_total = sum(b["iqs_score"] for b in blocks)
    iqs_detail = {b["block"]: {"score": b["iqs_score"], "note": b["iqs_note"],
                               "dims": b["dims"]} for b in blocks}
    weakest = [b["block"] for b in blocks if b["iqs_score"] < 10]

    # ─── 跨格一致性 ───
    warnings: list[str] = []

    # C1 checkpoint 当前格有效（终态兼容新旧写法：施工蓝图 / 定稿 / 完成 / 交接）
    current = cp.get("当前格", "")
    if current and not re.match(r"^(Phase 0|B\d{2}|施工蓝图|定稿|完成|交接)\b", current):
        warnings.append(
            f"C1 checkpoint「当前格」无效：{current}"
            f"（应为 Phase 0、B01–B10 或终态：施工蓝图/完成/交接；旧稿写「定稿」仍兼容）"
        )

    # C2 已完成格 ⊆ 实际填完的格
    finished = {s.strip()[:3] for s in re.split(r"[，,\s]+", cp.get("已完成", "")) if s.strip()}
    for bid in sorted(finished & set(BLOCKS) - done_set):
        warnings.append(f"C2 checkpoint 声明 {bid} 已完成，但该格仍有未填字段/未勾验收")

    # C3 B01 结论=不做 → 其余格仍在填
    b01 = read(bp / "01-条件.md")
    concl_line = next((ln for ln in b01.splitlines() if re.search(r"结论[:：]", ln)), "")
    m = re.search(r"结论[:：]\s*(.*)", concl_line)
    if m and len(done_set - {"B01"}) > 0:
        # 只认「明确单选为不做」：模板原样（多个候选都还在）视为未选，不告警。
        # 同理也放过「不做 / 转向」这类仍含多个候选的半成品。
        if selected_choice(m.group(1)) == "不做":
            warnings.append("C3 B01 结论为「不做」，但后续格仍在填充——先确认结论，避免无效施工")

    # C4 B05 涉及文件产出 → B06 四要素
    b05 = read(bp / "05-分析.md")
    out_line = next((ln for ln in b05.splitlines() if "输出：" in ln), "")
    b06 = read(bp / "06-决策.md")
    if out_line and ("是" in out_line or "文件" in out_line) and BLANK not in out_line:
        missing = [k for k, pat in
                   {"输出目录": r"输出目录[:：]\s*__+", "命名": r"命名[:：]\s*__+",
                    "格式": r"格式[:：]\s*__+", "错误输出": r"错误输出[:：]\s*__+"}.items()
                   if re.search(pat, b06)]
        if missing:
            warnings.append(f"C4 B05 声明涉及文件产出，但 B06 输出文件约定缺：{'、'.join(missing)}")

    # C5 B09 评分 → 改进项（仅当综合评分已填成数字时才检查）
    b09 = read(bp / "09-结果.md")
    score = re.search(r"综合评分[^:\n]*[:：]\s*(\d+(?:\.\d+)?)", b09)
    if score and re.search(r"改进项[:：]\s*__+", b09):
        warnings.append("C5 B09 已有综合评分，但「指向的改进项」仍为空——评分必须指向具体改进")

    # C6 index 快照与 frontmatter 一致
    for key, fm_key in (("平台", "platform"), ("入口", "entry"), ("通道", "channel")):
        snap = re.search(rf"\|\s*{key}\s*\|\s*([^\|]+)\|", index_text)
        if snap and fm.get(fm_key) and snap.group(1).strip() != fm[fm_key].strip():
            warnings.append(f"C6 index 快照「{key}={snap.group(1).strip()}」与 frontmatter「{fm_key}={fm[fm_key]}」不一致")

    # C8 教训回流门槛（v3.15.0）：教训不落检查项 = 下次照踩。
    # ⚠ 必须放在 `if errors == 0:` 之外——C7 关在里面是对的（十格没填齐时谈边界密度是自扰），
    # 但 C8 关心的是「B10 已经写了教训却没回流」，而这恰恰发生在逐格迭代、十格远未填齐的时候。
    # 关进 errors==0 会让它在最常见的用法（填一格跑一次）里永久失效，等到全齐才一次性抛出，
    # 那时教训已凉、也错过了「当天加检查项」的窗口——正是它要防的病（教训见 lessons L11）。
    # 判据只需 B10 存在且有内容（与 C5 同级：单文件级门控）。
    b10_text = read(bp / BLOCKS["B10"])
    if b10_text.strip():
        n_lesson, n_reflow = lesson_reflow_stats(b10_text)
        if n_lesson >= 1 and n_reflow < LESSON_MIN_REFLOW:
            warnings.append(
                f"C8 复盘记了 {n_lesson} 条教训，但 0 条标注「已落检查项 / 不适用」——"
                f"教训停在被记录那一层，下次照踩（见 lessons L10/L11）。"
                f"在 10-复盘.md 的「教训 → 检查项（必答）」补一行：能落机器检查就写落到哪，"
                f"不能就写「不适用 + 理由」；按「LXX → 落点」格式写（如 L10 → validate_skill 第 15 项），"
                f"即可被 --tick-reflow 自动登记进 lessons.md 引用计数"
            )

    # C7 边界密度门槛（v3.15.0）：仅当无结构性缺口时才报——十格都没填齐时，
    # 边界少是缺项的自然结果，先补格再谈密度，避免两类警告互相淹没。
    if errors == 0:
        n_items = n_conf = 0
        for fname in BLOCKS.values():
            i, p = boundary_stats(read(bp / fname))
            n_items += i
            n_conf += p
        if n_items < BOUNDARY_MIN:
            warnings.append(
                f"C7 边界条目共 {n_items} 条，低于门槛 {BOUNDARY_MIN} 条"
                f"（实证口径：自动出稿 11 条 vs 深度人工 18 条，见 outputs/baseline-vs-with-skill.md）——"
                f"建议按 capability-boundary.md 4 问决策树做一轮「边界补全」（③固定步骤）再出蓝图"
            )
        if n_conf < BOUNDARY_CONFUSABLE_MIN:
            warnings.append(
                "C7 缺「易混淆正例」——听起来超界、其实该本 skill 管的场景（防误伤设计），"
                "至少补 1 条，参考 capability-boundary.md 20 场景正反例表"
            )

    # ─── 下一步建议（IQS × BR-5 联动：优先补「能涨最多维度」的格）───
    pending = [b for b in blocks if b["status"] != "完成"]
    if pending:
        nxt = max(pending, key=lambda b: (len(b["dims"]), -int(b["block"][1:])))
        dim_hint = f"，可涨 {'/'.join(nxt['dims'])}" if nxt["dims"] else ""
        next_action = f"下一步：{nxt['block']}（{nxt['hint']}{dim_hint}）"
    else:
        next_action = "全部 10 格已完成——跑 09-结果.md 的机器验证并进入交接落地"

    ok = errors == 0 and not warnings
    exit_code = 0 if ok else (1 if errors else 2)

    iqs_written = False
    if args.write_iqs:
        iqs_written = write_iqs(bp, iqs_total)

    if args.json:
        print(json.dumps({
            "ok": ok, "blueprint": str(bp), "exit_code": exit_code,
            "completed": len(done_set), "total": 10,
            "iqs": {"score": iqs_total, "max": 100, "detail": iqs_detail,
                    "weakest": weakest, "weakest_dims": {b["block"]: b["dims"] for b in blocks if b["dims"]},
                    "written": iqs_written},
            "blocks": blocks, "warnings": warnings,
            "lessons_tick": tick_results,
            "checkpoint": cp, "next_action": next_action,
        }, ensure_ascii=False, indent=2))
    else:
        print(f"[check_blueprint] 蓝图：{bp}（完成 {len(done_set)}/10）\n")
        print(f"{'格':<5}{'状态':<6}{'IQS':<6}缺什么 / 建议")
        print("-" * 76)
        for b in blocks:
            color = GREEN if b["status"] == "完成" else RED
            detail = b["hint"] or b["iqs_note"] or "—"
            if b["blanks"]:
                detail += "；空位：" + "；".join(b["blanks"][:3]) + ("…" if len(b["blanks"]) > 3 else "")
            print(f"{b['block']:<5}{color}{b['status']:<4}{RESET}{b['iqs_score']:>3}/10  {detail}")
        if warnings:
            print("\n一致性警告：")
            for w in warnings:
                print(f"  {YELLOW}⚠{RESET} {w}")
        iqs_line = f"\nIQS 蓝图完备度：{iqs_total}/100"
        iqs_line += "（满分，十格均可交接）" if not weakest else f"（待补：{'、'.join(_block_labels(blocks))}）"
        print(iqs_line)
        if iqs_written:
            print(f"  已回填：09-结果.md「内部质量分（IQS，蓝图完备度）」= {iqs_total}")
        elif args.write_iqs:
            print("  ⚠ 回填失败：09-结果.md 不存在或找不到「内部质量分」字段")
        if tick_results:
            print("\n经验规则引用回写（F6 机器钩子）：")
            for t in tick_results:
                mark = "✔" if t["ok"] else "✘"
                print(f"  {mark} {t['id']}：{t['detail']}")
        print(f"\n{next_action}")
        verdict = "✅ 通过" if exit_code == 0 else ("❌ 有缺口" if exit_code == 1 else "⚠ 仅警告")
        print(f"结论：{verdict}（退出码 {exit_code}）")
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
