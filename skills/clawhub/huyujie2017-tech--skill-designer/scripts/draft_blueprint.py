#!/usr/bin/env python3
"""
draft_blueprint.py — 四步施工流 Step ②「初步方案」生成器

用户说清 ①概念讨论的 A 组答案后，一键生成**有主张的设计稿**（不是空白骨架）：

  · 调 infer_design.py 把「六问信号 → 设计模式 → 结构框架」程序化推断一遍
  · 用推断结果填 B01–B10 每一格的空位（不是把用户原话拼进模板）
  · 所有 AI 给的字段标【AI 建议】，需用户拍板的标【需用户拍板】
  · 由 AI 已完成判定的 checklist 项预勾，标（AI 已判定·待复核）；
    需要真实执行或用户拍板的项**保持未勾**——不假勾换分

用法：
    python scripts/draft_blueprint.py <蓝图目录> --name "<skill名>" --answers answers.json
    python scripts/draft_blueprint.py <蓝图目录> --name "<skill名>" \
        --answers '{"problem":"...","audience":"...","platform":"...","entry":"...","priority":"..."}'
    python scripts/draft_blueprint.py <目录> --name x --answers a.json --design design.json  # 外部注入推断结果
    python scripts/draft_blueprint.py <目录> --name x --answers a.json --archetype knowledge  # 覆盖结构框架

参数：
    目标目录        蓝图 bundle 落盘位置
    --name    必填  skill 名
    --answers 必填  JSON 文件路径 或 JSON 字符串（problem 必填；scenario/audience 至少给一个）
    --design        外部注入的 infer_design 结果（不给则内部自动推断）
    --archetype     覆盖推断出的结构框架
    --channel       light（默认）| full
    --entry         create（默认）| improve
    --platform      运行平台（默认 workbuddy）
    --force         目标目录非空时先备份再重建（默认拒绝覆盖）
    --json          结构化输出

退出码：0 = 生成成功；1 = 参数/目录错误。
"""

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

from blocks import BLOCKS, CHANNELS, ENTRIES, build_index
from infer_design import infer_design
from retry import read_text_robust, write_text_robust

AI_TAG = "【AI 建议】"
DECIDE_TAG = "【需用户拍板】"
TODO_TAG = "【待回填】"
RECHECK = "（AI 已判定·待复核）"

TODAY = date.today().isoformat()

# 五类模式（B03「五类模式」字段要求填：思维/导航/哲学/流程/工具）
FIVE_KINDS = {
    "A 流程配方": "流程型（Process）——重步骤顺序与 checkpoint",
    "B 领域知识包": "思维型（Thinking）——重判断规则与知识调用",
    "C 工具编排": "工具型（Tool）——重调用纪律与失败路径",
    "D 模板渲染": "流程型（Process）+ 工具型（Tool）——重固定格式与校验",
    "E 带自检": "流程型（Process）——重检查清单与抽检回路",
    "F 技能组合": "导航型（Navigation）——重意图路由与仲裁",
}

# 由 AI 已完成判定、可诚实预勾的 checklist 项（子串匹配）。
# 未列入的项 = 需要真实执行（如 B08 跑真实场景）或用户拍板，保持 ☐。
PRECHECK: dict[str, tuple[str, ...]] = {
    "01": ("有明确结论",),
    "02": ("画像清晰", "生态位与正交性已检查"),
    "03": ("模式已选", "依据已给出"),
    "04": ("待定项已列出", "澄清协议四型已逐型判定", "已明确哪些要问用户"),
    "05": ("IPO+B 四象限已逐项填出", "P 象限已标出", "边界与风险已列出"),
    "06": ("输出文件约定已声明",),
    "07": ("结构框架 archetype 已选定", "目录骨架已画", "五段章节骨架已逐段填出",
           "Resource Routing 全为强路由句式"),
    "08": (),   # 必须真跑过才算，不预勾
    "09": ("BR-5 五维评分已出", "蓝图完备度（IQS）已出", "评分结果指向明确的改进项"),
    "10": ("下一轮迭代点已定",),
}


def parse_answers(raw: str) -> dict:
    """解析 --answers / --design：支持 JSON 文件路径或 JSON 字符串。"""
    p = Path(raw)
    if p.exists():
        return json.loads(read_text_robust(p))
    return json.loads(raw)


def _s(answers: dict, key: str, default: str = "") -> str:
    return str(answers.get(key, default)).strip()


def scenario_of(answers: dict) -> str:
    return _s(answers, "scenario") or _s(answers, "audience") or "（未说明使用场景）"


# ─── 逐格填充器：{block前缀: {行首前缀: 整行内容}} ───
def build_fillers(answers: dict, d: dict) -> dict[str, dict[str, str]]:
    task = d["task_short"]
    problem = _s(answers, "problem")
    scenario = scenario_of(answers)
    audience = _s(answers, "audience") or scenario
    platform = _s(answers, "platform", "workbuddy")
    entry = _s(answers, "entry", "create")
    example = _s(answers, "example")
    priority = _s(answers, "priority")
    pt, ar, tree, ipo = d["pattern"], d["archetype"], d["tree"], d["ipo"]
    dec, five, br5 = d["decisions"], d["five_sections"], d["br5"]
    entry_cn = "新建" if entry == "create" else "改进已有 skill"
    mat = _s(answers, "materials")

    # ── B01 条件 ──
    b01 = {
        "前提：": f"前提：{problem}；使用者为「{audience}」，使用场景为 {scenario} {AI_TAG}",
        "背景：": f"背景：运行在 {platform}（{entry_cn}）；按 skill-archetypes §一 决策表判为 "
                  f"{ar['id']}（{ar['name']}）——{ar['decided_by_rule']} {AI_TAG}",
        "资源约束：": f"资源约束：{tree['files']['note']}；"
                     f"外部依赖「{'有（见 B05 风险）' if 'API' in ipo['method'] or '调用' in ipo['method'] else '暂无'}」"
                     f"；凭据与密钥纪律按平台约定 {AI_TAG}",
        # ⚠️ 「准入四问」字段必须与「结论」里的 ✓/☐ 判定一致：
        # 此前字段行四项全是 ☐，而结论写「形态合规 ✓ /… /复用检验 ☐」，自相矛盾；
        # 且 check_blueprint 按「模板原文比对」会把整行判为未填，IQS 平白少 2 分。
        "准入四问：": "准入四问：☑ 形态合规 ☑ 非元信息 ☑ 可链接 ☐ 复用检验"
                     f"（前三项 AI 已判通过；复用检验待③深化设计确认生态位后勾） {AI_TAG}",
        "结论：": f"结论：做 {AI_TAG}（准入四问：形态合规 ✓ / 非元信息 ✓ / 可链接 ✓ / 复用检验 ☐ 待③深化设计确认）",
        "非目标清单：": f"非目标清单：{d['non_goals']} {AI_TAG}",
        # v3.3.0 实测补全（G1）：M3 只改了 init 路径模板，proto/draft 路径漏了此字段——
        # 又一次「文档定义了 ≠ 代码产出」。有材料 → 摘录前 60 字并提醒脱敏复核；
        # 无材料 → 如实声明推断只靠六问信号（实证项不代填）。
        "证据来源：": (
            f"证据来源：C10 历史资料（①提供，已进引擎信号扫描）：{mat[:60]}…"
            f"（落库前按 material-distill §四复核脱敏） {AI_TAG}" if mat else
            "证据来源：（无历史资料；推断仅凭六问信号，③深化设计须补真实场景验证）"
        ),
    }

    # ── B02 事实 ──
    b02 = {
        "时间：": f"时间：{TODAY}（设计期） | 主体：{audience} {AI_TAG}",
        "动作：": f"动作：目前在 {platform} 上靠手动或通用对话能力完成「{task}」，"
                  f"每次都要重新描述一遍要求 {AI_TAG}",
        "客体：": f"客体：{problem} {AI_TAG}",
        "结果：": f"结果：缺少结构化、可复现的 skill 支持——同样的活儿每次质量不稳定，"
                  f"且经验不沉淀 {AI_TAG}",
        "正交性：": f"正交性：{_s(answers, 'ecosystem') or f'与已有 skill 的边界待③深化设计确认；本 skill 只负责「{task}」，'
                                                        f'不承担上游数据生产与下游发布 {DECIDE_TAG}'}",
        "  - 真实案例 3–5 个（须覆盖：成功 / 失败 / 信息不足 / 边界）：":
            f"  - 真实案例 3–5 个（须覆盖：成功 / 失败 / 信息不足 / 边界）："
            f"{TODO_TAG}③深化设计首轮补齐；已知样例：{example or '（用户未提供，需补一个具体用法）'}",
    }

    # ── B03 观点（P0 修复点：不再是硬编码 Pipeline）──
    b03 = {
        "判断：": f"判断：采用 {pt['interaction']} × {pt['content']} {AI_TAG}",
        "内容：": f"内容：{pt['meaning']}"
                  f"{'；组合形态：' + pt['combination'] if pt['combination'] else ''} {AI_TAG}",
        "依据：": f"依据：{pt['reason']} {AI_TAG}",
        "五类模式：": f"五类模式：{FIVE_KINDS.get(pt['content_key'], pt['content_key'])} {AI_TAG}",
        "自由度：": f"自由度：{pt['freedom']} {AI_TAG}",
    }

    # ── B04 问题 ──
    pend = d["pending"]
    b04 = {
        "待定项清单：": "待定项清单：" + "；".join(
            f"{i}. {it}" for i, it in enumerate(pend[:3], 1)
        ) + f"（问谁：用户 / 何时问：③深化设计首轮 / 策略：一次性追问）{AI_TAG}",
        "  - 一次性追问（grouped checklist）→ 适用于：":
            f"  - 一次性追问（grouped checklist）→ 适用于：缺多个独立配置项时一次问齐"
            f"（如输出目录 / 命名 / 格式 / 阈值），避免逐项打断 {AI_TAG}",
        "  - 逐步澄清（one question at a time）→ 适用于：":
            f"  - 逐步澄清（one question at a time）→ 适用于：需求本身模糊、"
            f"需据首轮回答决定后续问法时（如「{task}」的范围界定）{AI_TAG}",
        "  - 选项式（2–4 个选项，每个注明影响）→ 适用于：":
            f"  - 选项式（2–4 个选项，每个注明影响）→ 适用于：2–4 个方案各有取舍需用户拍板"
            f"（如 {ar['alternatives']}）{AI_TAG}",
        "  - 关键假设确认（覆盖/删除/迁移/发布前复述动作并等确认）→ 适用于：":
            f"  - 关键假设确认（覆盖/删除/迁移/发布前复述动作并等确认）→ 适用于："
            f"覆盖 / 删除 / 批量 / 发布前，复述「即将对 {task} 做 X」并等确认 {AI_TAG}",
        "归属：": f"归属：必须用户拍板项 → {pend[0] if pend else '（无）'}；"
                  f"设计师可代答项 → 目录分层、失败分级、校验方式等工程惯例 {AI_TAG}",
    }

    # ── B05 分析 ──
    b05 = {
        "输入 I：": f"输入 I：{ipo['input']} {AI_TAG}",
        "处理 P：": f"处理 P：{ipo['process']} {AI_TAG}",
        "输出 O：": f"输出 O：{ipo['output']} {AI_TAG}",
        "边界 B：": f"边界 B：{ipo['boundary']} {AI_TAG}",
        "方法：": f"方法：{ipo['method']} ——决定 B06 决策 2 {AI_TAG}",
        "风险：": f"风险：{ipo['risk']} {AI_TAG}",
    }

    # ── B06 决策 ──
    b06 = {
        "决策者：": f"决策者：用户（AI 给建议与依据，取舍由用户拍板）{AI_TAG}",
        "决策 1：": f"决策 1：{dec['decision1']} {AI_TAG}",
        "决策 2：": f"决策 2：{dec['decision2']} {AI_TAG}",
        "决策 3：": f"决策 3：{dec['decision3']} {AI_TAG}",
        "  - 输出目录：": f"  - 输出目录：{dec['output_dir']} {AI_TAG}",
        "  - 命名：": f"  - 命名：{dec['naming']} {AI_TAG}",
        "  - 格式：": f"  - 格式：{dec['output_format']} {AI_TAG}",
        "  - 错误输出：": f"  - 错误输出：{dec['error_output']} {AI_TAG}",
        "ADR-1（重大选型记录）：": f"ADR-1（重大选型记录）：{dec['adr']} {AI_TAG}",
        "废弃方案：": f"{dec['abandoned']} {AI_TAG}",
    }

    # ── B07 计划（P0 修复点：archetype 与五段骨架不再留空）──
    b07 = {
        "目标：": f"目标：MVP 能稳定完成「{task}」的核心路径——"
                  f"{'产出符合约定格式的文件' if dec['produces_file'] else '在对话内给出可用的结论'}"
                  f"，且 {priority or '首要目标'} 达标 {AI_TAG}",
        "结构框架 archetype：": f"结构框架 archetype：{ar['id']}（{ar['name']}，选型见 references/skill-archetypes.md）{AI_TAG}",
        "模式→结构映射（B03 → B07，查 references/skill-archetypes.md §〇）：":
            f"模式→结构映射（B03 → B07，查 references/skill-archetypes.md §〇）："
            f"内容模式【{pt['content_key']}】→ 推荐 archetype【{ar['mapped_id']}】"
            f"→ 实际采用【{ar['id']}】（{ar['decided_by_rule']}）→ 侧重段【{ar['focus']}】{AI_TAG}",
        "① 目录骨架（文件层）：": f"① 目录骨架（文件层）：{tree['skeleton']} {AI_TAG}",
        "  - ## Workflow：": f"  - ## Workflow：{five['Workflow']} {AI_TAG}",
        "  - ## Clarification Protocol：": f"  - ## Clarification Protocol：{five['Clarification Protocol']} {AI_TAG}",
        "  - ## Resource Routing：": f"  - ## Resource Routing：{five['Resource Routing']} {AI_TAG}",
        "  - ## Failure Handling：": f"  - ## Failure Handling：{five['Failure Handling']} {AI_TAG}",
        "  - ## Validation：": f"  - ## Validation：{five['Validation']}（侧重：{ar['focus']}）{AI_TAG}",
        "③ 资源分配：": f"③ 资源分配：scripts={tree['files']['scripts']} / "
                        f"references={tree['files']['references']} / assets={tree['files']['assets']} {AI_TAG}",
        "实施步骤：": "实施步骤：1. 与用户敲定本稿的【AI 建议】项 2. 按 B07 目录骨架建 SKILL.md 五段 "
                     "3. 实现 scripts/ 确定性逻辑 4. 补 references/ 与 assets/ "
                     "5. 跑 check_blueprint.py + validate_skill.py 验收 {AI_TAG}".replace("{AI_TAG}", AI_TAG),
        "时间表：": f"时间表：轻量 MVP 1 轮（③深化设计 1–2 轮 + 落地 1 轮） | 负责人：用户拍板 + AI 执行 {AI_TAG}",
    }

    # ── B08 行动 ──
    b08 = {
        "验证场景：": f"验证场景：{example or f'用一次真实的「{task}」跑通全链路'}"
                      f"——必须真实场景，非空泛测试 {TODO_TAG}③深化设计后实跑",
        "有 / 无对比：": f"有 / 无对比：baseline = 无 skill 时靠通用对话做「{task}」；"
                         f"with-skill = 跑一次本 skill。对比口径：耗时 / 质量稳定性 / 是否需要返工 {TODO_TAG}",
        "触发测试：": f"触发测试：should（该触发）=「{dec['triggers'].split(' / ')[0]}」类请求必须命中；"
                      f"not（不该触发）= 与本 skill 无关的通用问答不得误召回；"
                      f"ambiguous（模糊）= 只说「{task}」但没给材料时应进入澄清而非硬跑 {TODO_TAG}",
        "效果测试：": f"效果测试：happy（材料齐全）/ complex（多来源或跨主题）/ edge（信息缺失或格式异常）"
                      f"/ negative（明确不属于本 skill 的请求）/ error（依赖失败或超时）五场景 {TODO_TAG}",
        "独立审：": f"独立审：用户亲自检查产出是否符合预期——AI 不能当唯一判官 {DECIDE_TAG}",
    }

    # ── B09 结果（BR-5 预估 + 待回填说明）──
    def br5_line(k: str, prefix: str) -> str:
        m = br5[k]
        return f"  - {prefix}：{m['score']} 分 — 证据：{m['evidence']} {AI_TAG}（③深化设计后重评）"

    b09 = {
        "BR-5 均分：": f"BR-5 均分：{br5['avg']}（T={br5['T']['score']} / R={br5['R']['score']} / "
                       f"A={br5['A']['score']} / C={br5['C']['score']} / E={br5['E']['score']}，五维各 1–5 分）"
                       f" {AI_TAG}（②阶段预估，③深化设计后重评）",
        "  - T 边界可信（B01/B05/B06）：": br5_line("T", "T 边界可信（B01/B05/B06）"),
        "  - R 失败可控（B05/B06）：": br5_line("R", "R 失败可控（B05/B06）"),
        "  - A 触发可辨（B02/B06）：": br5_line("A", "A 触发可辨（B02/B06）"),
        "  - C 结构可解（B07）：": br5_line("C", "C 结构可解（B07）"),
        "  - E 验证可证（B05/B08）：": br5_line("E", "E 验证可证（B05/B08）"),
        "外部价值分（EVS）：": f"外部价值分（EVS）：{br5['evs']}（= BR-5 均分 {br5['avg']} × 20）{AI_TAG}",
        "综合评分 = 内部 × 外部 / 100：": f"综合评分 = 内部 × 外部 / 100："
                                          f"待 IQS 回填后自动计算（IQS 由 check_blueprint.py --write-iqs 机器回填，"
                                          f"当前 EVS={br5['evs']}）{TODO_TAG}",
        "指向的改进项：": f"指向的改进项：五维中最低的是 {_lowest_dim(br5)}——③深化设计优先补它对应的积木格；"
                          f"其次补 B08 的真实场景验证（E 维只能靠实跑提分）{AI_TAG}",
        "平台名称（如 SkillHub TRACE / 内部评审）：": f"平台名称（如 SkillHub TRACE / 内部评审）："
                                                    f"{TODO_TAG}④施工蓝图 / 发布后回填",
        "外部评分：": f"外部评分：{TODO_TAG}拿到平台返评后回填（T / R / A / C / E 各 1–5 分）",
        "最低分项及文字评语：": f"最低分项及文字评语：{TODO_TAG}回填后即可用 "
                                f"`scripts/trace_patch.py <反馈.json> --mode design` 生成补丁清单",
        "按维度拆分的补丁清单（P0 必修 / P1 建议 / P2 可选）：":
            f"按维度拆分的补丁清单（P0 必修 / P1 建议 / P2 可选）：{TODO_TAG}由 trace_patch.py 生成，"
            f"或人工按 references/trace-evaluation-guide.md §六 定位",
        # ⚠️ 这三个字段此前完全没填，check_blueprint 按「模板原文比对」判为未填，
        # IQS 平白少 2 分。但它们本就是**执行记录型**字段：设计期无法"已跑"，
        # 正确写法是把「何时跑 / 跑什么命令」写清楚，而不是留一堆 ☐ 装没填。
        "机器验证：": "机器验证：☐ 已跑 scripts/check_blueprint.py（蓝图完整性——跑一次即由 "
                     f"--write-iqs 自动勾） ☐ 已跑 scripts/validate_skill.py（④施工蓝图落地后）"
                     f" {TODO_TAG}④施工蓝图阶段执行后勾选",
        "补丁生成命令：": "补丁生成命令：拿到外部平台返评后执行 "
                         f"`python scripts/trace_patch.py <反馈.json>`（设计期加 `--mode design`）；"
                         f"设计期无返评，保持未勾 {TODO_TAG}发布后执行",
        "补丁验证命令：": "补丁验证命令：每次改完补丁执行 `python scripts/validate_skill.py --self` "
                         f"/ `python scripts/sd_cli.py --self-check`，随补丁一并验证 "
                         f"{TODO_TAG}发布后执行",
    }

    # ── B10 复盘 ──
    b10 = {
        "失败/不足：": f"失败/不足：{TODO_TAG}MVP 首跑后回填——记录本 skill 实际翻车的具体场景"
                       f"（不是「效果一般」这种无效描述）",
        "归纳为通用规则：": f"归纳为通用规则：{TODO_TAG}把失败归成规则写回 SKILL.md，而非打特例补丁",
        "经验：": f"经验：{TODO_TAG}沉淀可复用做法（本稿 AI 建议部分也可作为对照基线）",
        "下一轮迭代点：": f"下一轮迭代点：1. 补 3–5 个真实案例（成功/失败/信息不足/边界）"
                          f" 2. 实跑 B08 五场景并回填 3. BR-5 五维重评，把最低维 "
                          f"{_lowest_dim(br5)} 拉到 4 分以上 {AI_TAG}",
        "版本记录：": f"版本记录：bump to 0.2.0 + CHANGELOG 更新（MVP 首跑通过后）{AI_TAG}",
    }

    return {"01": b01, "02": b02, "03": b03, "04": b04, "05": b05,
            "06": b06, "07": b07, "08": b08, "09": b09, "10": b10}


def _lowest_dim(br5: dict) -> str:
    dims = [k for k in ("T", "R", "A", "C", "E")]
    lo = min(dims, key=lambda k: br5[k]["score"])
    names = {"T": "T 边界可信", "R": "R 失败可控", "A": "A 触发可辨",
             "C": "C 结构可解", "E": "E 验证可证"}
    return f"{names[lo]}（{br5[lo]['score']} 分）"


_MD_STAR = re.compile(r"[*`]")


def _field_key(s: str) -> str:
    """取字段名：抹掉列表前缀与加粗符号后，截到第一个冒号之前。

    为什么必须归一化：模板字段名会加粗（`**非目标清单**：______`），还会挂括号限定语
    （`资源约束（**三件套，缺一不可**）：…`、`**证据来源**（仅留痕，**不进产物**）：…`），
    而填充器写的是裸键（`非目标清单：`）。按原文前缀匹配时这些字段会**静默漏填**——
    用户在①概念讨论给的 boundary 早已被引擎算进 non_goals，却落不进 01-条件.md，
    最后 check 只报「有个空位」，看上去像用户没填，实际是注入失败。
    """
    t = _MD_STAR.sub("", re.sub(r"^[\s>-]+", "", s)).strip()
    return re.match(r"^[^:：]*", t).group(0).strip()


def _key_matches(line: str, key: str) -> bool:
    """字段名相同，或字段名后紧跟括号限定语（`资源约束（三件套…）：`）。

    只放开「紧跟 `（`」这一种形态：若允许任意后缀，`输出目录（…）：` 会被
    `输出：` 误命中，把短键的填充内容灌进长键字段。
    """
    ln, kn = _field_key(line), _field_key(key)
    if not kn:
        return False
    if ln == kn:
        return True
    return ln.startswith(kn) and ln[len(kn):].startswith("（")


def fill_line(line: str, fillers: dict[str, str]) -> str:
    """用填充器替换该行；取最长匹配键，避免短键误命中。"""
    best_key, best_len = None, -1
    for key in fillers:
        k = _field_key(key)
        if _key_matches(line, key) and len(k) > best_len:
            best_key, best_len = key, len(k)
    return fillers[best_key] if best_key else line


def fmt_field(f: str, fm: dict) -> str:
    """与 blocks.build_block 同款排版：小节标题与缩进子项不加 `- ` 前缀。"""
    filled = fill_line(f, fm)
    if filled.lstrip().startswith("#"):
        return filled
    if filled[:1].isspace():
        return filled
    return f"- {filled}"


def build_draft_block(b: dict, fillers: dict) -> str:
    bid = b["file"][:2]
    fm = fillers.get(bid, {})
    fields = "\n".join(fmt_field(f, fm) for f in b["fields"])

    pre = PRECHECK.get(bid, ())
    checks = []
    for c in b["checklist"]:
        if any(k in c for k in pre):
            checks.append(f"- ☑ {c} {RECHECK}")
        else:
            checks.append(f"- ☐ {c}")
    checks = "\n".join(checks)

    return f"""# {b['title']}

> 结构公式：`{b['formula']}`

## 填空字段

{fields}

## 验收 checklist

{checks}

> 本格由 ②初步方案 自动生成：标 {AI_TAG} 的字段是 AI 按「六问信号 → 设计模式 → 结构框架」
> 推断出的**有主张建议**，回「按建议」即可批量采纳，也可只推翻某一格；
> 标 {DECIDE_TAG} 的必须由用户拍板；标 {TODO_TAG} 的是后续阶段才填得出来的项，
> 已写明触发时机。checklist 中带 {RECHECK} 的是 AI 已判定的项，**复核后请改勾**。
"""


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    ap = argparse.ArgumentParser(description="四步流 Step② 初步方案生成器（skill-designer）")
    ap.add_argument("target", help="蓝图 bundle 落盘目录")
    ap.add_argument("--name", required=True, help="skill 名（写入 index title）")
    ap.add_argument("--answers", required=True, help="JSON 文件路径 或 JSON 字符串")
    ap.add_argument("--design", help="外部注入的 infer_design 结果（JSON 路径/字符串）；不给则内部自动推断")
    ap.add_argument("--archetype", help="覆盖推断出的结构框架 id")
    ap.add_argument("--channel", default="light", choices=CHANNELS, help="通道：light（默认）/ full")
    ap.add_argument("--entry", default="create", choices=ENTRIES, help="入口：create（默认）/ improve")
    ap.add_argument("--platform", default="workbuddy", help="运行平台（默认 workbuddy）")
    ap.add_argument("--force", action="store_true", help="目标目录非空时先备份为 .bak-<时间戳> 再重建")
    ap.add_argument("--json", action="store_true", help="结构化输出")
    args = ap.parse_args()

    def fail(msg: str, code: int = 1) -> int:
        if args.json:
            print(json.dumps({"ok": False, "error": msg}, ensure_ascii=False))
        else:
            print(f"[draft_blueprint] 错误：{msg}", file=sys.stderr)
        return code

    try:
        answers = parse_answers(args.answers)
    except Exception as e:
        return fail(f"--answers 解析失败：{e}")

    if not str(answers.get("problem", "")).strip():
        return fail("--answers 缺少必填项：problem")
    if not (str(answers.get("scenario", "")).strip() or str(answers.get("audience", "")).strip()):
        return fail("--answers 缺少必填项：scenario 或 audience（至少给一个）")

    answers.setdefault("name", args.name)
    answers.setdefault("platform", args.platform)
    answers.setdefault("entry", args.entry)

    # 1. 推断设计（外部注入优先）
    if args.design:
        try:
            design = parse_answers(args.design)
        except Exception as e:
            return fail(f"--design 解析失败：{e}")
    else:
        try:
            design = infer_design(answers, args.archetype)
        except ValueError as e:
            return fail(str(e))

    target = Path(args.target)

    # 2. 幂等：已存在且非空 → 默认拒绝；--force 则先备份再重建
    if target.exists() and any(target.iterdir()):
        if not args.force:
            return fail(f"目标目录已存在且非空，拒绝覆盖：{target}（加 --force 可先备份再重建）")
        # ⚠️ 必须用 datetime 而非 date：date.today() 没有时分秒，%H%M%S 会全渲染成
        #    000000，同一秒内二次 --force 会因目标已存在而 rename 失败（WinError 183）。
        #    再补一层序号兜底，确保永不撞车。
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        bak = target.with_name(f"{target.name}.bak-{stamp}")
        n = 2
        while bak.exists():
            bak = target.with_name(f"{target.name}.bak-{stamp}-{n}")
            n += 1
        try:
            target.rename(bak)
        except Exception as e:
            return fail(f"备份旧目录失败：{e}")

    target.mkdir(parents=True, exist_ok=True)
    fillers = build_fillers(answers, design)
    created: list[str] = []

    # 3. index.md
    index_text = build_index(args.name, args.channel, args.entry, args.platform)
    index_text = index_text.replace(
        "蓝图骨架已生成，待逐格填充",
        f"②初步方案已生成：{design['pattern']['interaction']} × {design['pattern']['content']}"
        f" → {design['archetype']['id']}（{design['archetype']['name']}），待逐格确认"
    )
    # P0-③：description 五件事不再留空壳占位符，改为程序化生成草稿
    index_text = index_text.replace(
        "<五件事 description 初稿：做什么 / 何时用 / 何时不 / 触发词 / 语言>",
        design.get("description_five", "<五件事 description 初稿：做什么 / 何时用 / 何时不 / 触发词 / 语言>"),
    )
    # 快照表补上 AI 推断的设计模式与结构框架
    index_text = index_text.replace(
        "| 设计模式（交互×内容） | ______ × ______ |",
        f"| 设计模式（交互×内容） | {design['pattern']['interaction']} × {design['pattern']['content']} {AI_TAG} |",
    )
    index_text = index_text.replace(
        "| 输出文件约定 | ______（涉及文件产出时） |",
        f"| 输出文件约定 | {design['decisions']['output_dir']} / {design['decisions']['naming']}"
        f"{'（无文件产出）' if design['decisions']['output_dir'] == '无文件产出' else ''} {AI_TAG} |",
    )
    index_text = index_text.replace(
        "> 一句话定位：______（这个 skill 做什么）+ 为什么值得做（准入四问结论）",
        f"> 一句话定位：{design['task_short']}（{args.name}）——{design['archetype']['decided_by_rule']} {AI_TAG}",
    )
    write_text_robust(target / "index.md", index_text)
    created.append("index.md")

    # 4. 01–10 子积木
    for b in BLOCKS:
        write_text_robust(target / b["file"], build_draft_block(b, fillers))
        created.append(b["file"])

    result = {
        "ok": True, "target": str(target), "name": args.name,
        "channel": args.channel, "entry": args.entry, "platform": args.platform,
        "design": {
            "pattern": f"{design['pattern']['interaction']} × {design['pattern']['content']}",
            "archetype": design["archetype"]["id"],
            "archetype_name": design["archetype"]["name"],
            "focus": design["archetype"]["focus"],
            "br5_avg": design["br5"]["avg"],
            "evs": design["br5"]["evs"],
            "pending": design["pending"][:3],
        },
        "created": created,
        "next": f"进入③深化设计：逐格确认 AI 建议；回「按建议」可批量采纳；"
                f"标 {DECIDE_TAG} 的字段必须由用户拍板",
    }
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    d = design
    print(f"[draft_blueprint] 已生成②初步方案：{target}")
    print(f"  设计模式：{d['pattern']['interaction']} × {d['pattern']['content']} {AI_TAG}")
    print(f"  结构框架：{d['archetype']['id']}（{d['archetype']['name']}）{AI_TAG}")
    print(f"  侧重段：{d['archetype']['focus']}")
    print(f"  目录骨架：{d['tree']['skeleton']}")
    print(f"  BR-5 预估：{d['br5']['avg']} 分（EVS {d['br5']['evs']}），最低维 {_lowest_dim(d['br5'])}")
    print(f"  产出文件：index.md + " + " ".join(b["file"] for b in BLOCKS))
    print(f"→ 下一步：进入③深化设计；回「按建议」批量采纳 AI 建议，"
          f"或指定某一格推翻。标 {DECIDE_TAG} 的字段必须由用户拍板。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
