#!/usr/bin/env python3
"""
infer_design.py — ②初步方案的「有主张」推断引擎

把两份人工参考表程序化，让 ②初步方案从「模板填空」升级为「有主张的设计稿」：

  1. references/designer-guide.md §二 —— 六问信号 → 设计模式翻译表
  2. references/skill-archetypes.md §〇 —— 设计模式 → 结构框架映射矩阵
     与 §一 选型决策表（命中即停）

输入：①概念讨论的 answers（problem / audience / platform / entry /
      priority / flow / example / boundary / ecosystem）
输出：design dict —— 设计模式(B03)、结构框架(B07)、目录骨架、SKILL.md
      五段骨架、IPO+B(B05)、决策(B06)、待定项(B04) 等全部给出建议值。

所有建议值统一带 AI_TAG 标记；用户回「按建议」即可批量采纳，
也可以只推翻其中一格。

用法：
    python scripts/infer_design.py --answers '<JSON>' [--json]
    python scripts/infer_design.py --answers answers.json --archetype knowledge

退出码：0 = 推断成功；1 = answers 解析失败。
"""

import argparse
import json
import re
import sys
from pathlib import Path

from retry import read_text_robust

sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8, fail  # noqa: E402

enable_utf8()  # stdout + stderr 双流兜底（原先只配了 stdout，报错仍会乱码）

AI_TAG = "【AI 建议】"
PENDING_TAG = "【待确认】"

ARCHETYPE_IDS = ("minimal", "pipeline", "tool", "knowledge", "template", "full", "suite")

# ─── ① 六问信号 → 设计模式翻译表（数据源：designer-guide.md §二）───
SIGNAL_RULES = {
    "Q1_pipeline": {
        "q": "Q1",
        "interaction": "Pipeline", "content": "A 流程配方",
        "meaning": "多步骤带 checkpoint",
    },
    "Q2_tool": {
        "q": "Q2",
        "interaction": "Tool Wrapper", "content": "C 工具编排",
        "meaning": "编排外部能力 + 失败路径",
    },
    "Q3_template": {
        "q": "Q3",
        "interaction": "Generator", "content": "D 模板渲染",
        "meaning": "标准化格式产出",
    },
    "Q_knowledge": {
        "q": "Q4*",
        "interaction": "Inversion", "content": "B 领域知识包",
        "meaning": "LLM 不知的领域规则，知识主体下沉 references",
    },
    "Q4_inversion": {
        "q": "Q4",
        "interaction": "Inversion", "content": "B 领域知识包",
        "meaning": "先澄清再行动（咨询/诊断/陪练）",
    },
    "Q5_review": {
        "q": "Q5",
        "interaction": "Reviewer", "content": "E 带自检",
        "meaning": "评审 / 检查类",
    },
}

# 强信号词典（权重 2）：命中即强指示任务性质
KEYWORDS_STRONG: dict[str, tuple[str, ...]] = {
    "Q2_tool": (
        "API", "api", "接口", "调用", "抓取", "爬取", "查询数据库", "数据库", "DB", "CLI",
        "命令行", "MCP", "连接器", "webhook", "上传", "下载", "第三方", "HTTP", "请求",
        "SDK", "sdk", "服务端", "爬虫", "同步数据", "实时数据", "行情", "行情数据",
    ),
    "Q3_template": (
        "模板", "固定格式", "生成文件", "导出", "报告", "周报", "月报", "日报", "卡片",
        "PPT", "ppt", "pptx", "docx", "DOCX", "pdf", "PDF", "xlsx", "表格", "封面",
        "排版", "海报", "清单", "台账", "合同", "简历", "图表", "可视化", "HTML", "html",
        "结构化", "统一格式", "规范化", "一键生成", "出图", "长图",
    ),
    "Q_knowledge": (
        "领域知识", "法规", "法条", "规范", "手册", "专家经验", "行业标准", "政策",
        "术语", "指南", "判例", "条文", "规章制度", "会计准则", "税法", "诊疗", "药典",
    ),
    "Q4_inversion": (
        "先问", "澄清", "访谈", "咨询", "问诊", "确认需求", "追问", "了解情况", "先聊", "调研",
    ),
    "Q1_pipeline": (
        "多步", "流程", "分步", "步骤", "然后", "工作流", "SOP", "sop",
        "流水线", "阶段", "checkpoint", "逐步", "一步一步",
    ),
    "Q5_review": (
        "检查", "评审", "审查", "审计", "体检", "评估", "诊断", "校对", "批改",
        "风险排查", "合规", "验收", "打分", "评分", "质检", "巡检",
    ),
    "suite": (
        "套件", "多子域", "多个子技能", "一站式", "全家桶", "矩阵", "多个领域",
    ),
}

# 弱信号词典（权重 1）：多为「输出目的地 / 手段」，不能直接判定任务性质。
# 例：「沉淀到 Obsidian 知识库」是输出去向，不等于 skill 本身是知识密集型。
KEYWORDS_WEAK: dict[str, tuple[str, ...]] = {
    "Q_knowledge": ("知识库", "资料库", "归档", "沉淀", "笔记", "素材库", "整理", "收录"),
}

# ─── ② 设计模式 → 结构框架映射矩阵（数据源：skill-archetypes.md §〇）───
PATTERN_TO_ARCH: dict[tuple[str, str], dict[str, str]] = {
    ("A 流程配方", "Pipeline"):     {"id": "pipeline", "alt": "full",      "focus": "Workflow 写决策树 + checkpoint（分支明确、步骤带中间确认）"},
    ("B 领域知识包", "Inversion"):  {"id": "knowledge", "alt": "full",     "focus": "Resource Routing 写强路由表（If…load…before…）"},
    ("C 工具编排", "Tool Wrapper"): {"id": "tool",      "alt": "full",     "focus": "Failure Handling 写四状态 + 重试/降级"},
    ("D 模板渲染", "Generator"):    {"id": "template",  "alt": "full",     "focus": "Validation 写 schema 校验 + 错误输出"},
    ("E 带自检", "Reviewer"):       {"id": "pipeline",  "alt": "minimal",  "focus": "Validation 写 golden checklist + 抽检回路"},
    ("F 技能组合", "Pipeline"):     {"id": "full",      "alt": "suite",    "focus": "Workflow 写意图路由表 + 多 skill 仲裁"},
}

# ─── ③ 各 archetype 的施工图素材 ───
ARCH_SPEC: dict[str, dict[str, object]] = {
    "minimal": {
        "name": "极简型 Single-file",
        "tree": "SKILL.md（唯一入口 = 元数据 + 全部指令）",
        "scripts": "不建（无确定性逻辑）",
        "references": "不建（SKILL.md ≤ 500 行装得下）",
        "assets": "不建",
        "method": "LLM 推理（无脚本、无外部依赖）",
        "non_goals": "不引入 scripts/ 与 references/；不做外部调用与文件产出——装不下时再扩容",
        "triggers_hint": "原则 / 判断规则 / 咨询类问句",
        "workflow": [
            "识别意图：判断请求是否落在触发范围内（不在则一句话说明不做什么）",
            "调用核心判断规则给出结论",
            "补一句「为什么这么判断」的依据",
            "提示需用户确认的分支或缺失信息",
            "收尾：复述结论与下一步",
        ],
        "routing": "无（单文件，全部指令常驻上下文，不需要路由）",
        "failure": "升级条件：请求超出本 skill 范围 → 明确说明并建议替代路径；回退方式：退回通用对话",
        "validation": "自检清单：结论是否落在声明范围内 / 是否给出了依据 / 是否误引用未声明的能力",
    },
    "pipeline": {
        "name": "流程型 Pipeline",
        "tree": "SKILL.md + references/（README.md 索引 + step-guide.md 逐步细则 + edge-cases.md 例外）+ scripts/（仅当某步必须 100% 确定）",
        "scripts": "仅当某步「LLM 会出错、脚本能 100% 确定」才建（如校验器）",
        "references": "README.md（agent 索引）+ step-guide.md（逐步细则）+ edge-cases.md（症状→原因→修复）",
        "assets": "不建（无模板产物）",
        "method": "混合（流程编排由 LLM，确定性校验/状态记录由脚本）",
        "non_goals": "不做跨 skill 编排；不隐藏中间状态——每步必须可回退、可重跑",
        "triggers_hint": "「一步步 / 帮我走完 / 分阶段」类问句",
        "workflow": [
            "收集输入并做准入校验（缺项用一次性追问补齐，不逐项打断）",
            "阶段一：拆解输入 → 产出阶段产物并记录状态",
            "checkpoint：向用户确认阶段产物，允许回退修改后再继续",
            "阶段二：按顺序执行剩余步骤，每步结束更新进度快照",
            "汇总交付 + 跑 Validation（产物存在 / 格式 / 退出码）",
        ],
        "routing": "If 进入第 N 步 → load references/step-guide.md#step-N before 执行；If 命中例外症状 → load references/edge-cases.md",
        "failure": "四状态（Not started / In progress / Partial success / Failed safely）；升级条件：某步产物校验不通过 → 停在该步并回退；回退方式：从上一 checkpoint 重跑，已处理项不重复",
        "validation": "每步 checkpoint 通过 + 最终产物齐全 + 进度快照与实际一致",
    },
    "tool": {
        "name": "工具编排型 Tool Wrapper",
        "tree": "SKILL.md + scripts/（调用与预检）+ references/（api-contract.md 接口契约）",
        "scripts": "预检脚本 + 调用脚本（参数说明 / 清晰错误 / 退出码 / 重试退避）",
        "references": "api-contract.md（接口契约：入参 / 返回 / 错误码 / 限流）",
        "assets": "不建",
        "method": "脚本为主（确定性调用、重试、鉴权），LLM 负责参数澄清与结果解读",
        "non_goals": "不静默重试；不只写成功路径——超时/限流/鉴权失效/部分成功四种失败必须各有动作",
        "triggers_hint": "「调用 / 拉取 / 同步 / 上传」类动作句",
        "workflow": [
            "预检：参数 / 凭据 / 依赖可用性（任一缺失立即报清晰错误，不静默失败）",
            "发起调用（脚本负责超时与指数退避重试）",
            "解析返回并做 schema 校验（识别部分成功）",
            "失败分级处理：超时 / 限流 / 鉴权失效 / 部分成功 各有明确动作",
            "交付结果；失败时写可读错误输出（不写敏感路径）",
        ],
        "routing": "If 需要调用外部接口 → load references/api-contract.md + scripts/<caller>.py before 发起请求",
        "failure": "四状态；升级条件：鉴权失效或连续重试失败 → 停止并给出人工介入指引；回退方式：返回上一次成功缓存或明确告知无数据",
        "validation": "预检通过 + 返回通过 schema 校验 + 错误路径已实测（断网/超时/错误码）",
    },
    "knowledge": {
        "name": "知识密集型 Reference-heavy",
        "tree": "SKILL.md（路由器 + 核心判断规则）+ references/（知识主体，一主题一文件）",
        "scripts": "不建或仅建索引校验脚本（知识查阅无需确定性计算）",
        "references": "知识主体：一主题一文件 + README.md 索引（>300 行须加目录）",
        "assets": "不建",
        "method": "LLM 推理 + 强路由加载（知识在 references，不进上下文）",
        "non_goals": "不把知识正文搬进 SKILL.md；不做实时数据抓取——本型只负责领域判断规则与知识检索",
        "triggers_hint": "领域术语 / 「XX 怎么规定 / 怎么判断」类问句",
        "workflow": [
            "识别用户问的是哪个知识主题（意图路由）",
            "强路由加载对应 references 文件（If… load … before 判断）",
            "按核心判断规则给答案，注明出处文件与章节",
            "命中边界 / 例外时转对应例外条目并说明",
            "交付 + 自检（是否引用了未加载的文件 / 是否超出声明范围）",
        ],
        "routing": "If 用户问到【主题/术语/规则】→ load references/<topic>.md before 给判断（避免 see xxx.md 式弱路由）",
        "failure": "四状态；升级条件：references 无命中 → 明说「不在知识范围内」而非臆造；回退方式：给出最接近的条目并标注不确定",
        "validation": "答案可溯源到具体 references 文件 + 无臆造条目 + 边界情况已声明",
    },
    "template": {
        "name": "模板产出型 Generator",
        "tree": "SKILL.md + assets/（模板）+ scripts/（渲染与校验）",
        "scripts": "渲染脚本 + 校验脚本（schema 校验 / 格式校验）",
        "references": "style-rules.md（排版与写作规范，可选）",
        "assets": "输出模板（.html / .md / .docx 等，不进上下文）",
        "method": "脚本为主（渲染与校验确定性），LLM 负责内容要素整理",
        "non_goals": "不让 LLM 手搓格式；不静默失败——失败也必须产出错误文件并写清原因",
        "triggers_hint": "「生成 / 导出 / 做一份 / 排版成」类产出句",
        "workflow": [
            "收集内容要素（缺项一次性追问，不逐项打断）",
            "要素完整性校验（必填 schema 校验，缺则一次性列全）",
            "从 assets/ 取模板 + 脚本渲染（不靠 LLM 拼格式）",
            "输出校验：格式 / 命名 / 落盘路径 三查",
            "成功交付；失败时写错误输出到约定路径（不静默）",
        ],
        "routing": "If 需要产出文件 → load assets/<template> + scripts/render.py before 渲染",
        "failure": "四状态；升级条件：要素缺失且无法默认 → 一次性列出全部缺失项后停；回退方式：产出半成品 + 缺口清单",
        "validation": "产物存在 + 格式通过 schema 校验 + 命名/路径符合输出文件约定 + 错误路径已实测",
    },
    "full": {
        "name": "全栈工程型 Full-stack",
        "tree": "SKILL.md（路由器 ≤500 行）+ scripts/（cli.py 统一入口）+ references/ + assets/ + 治理台账（CHANGELOG / MISTAKES，不进上下文）",
        "scripts": "cli.py 聚合各脚本（参数说明 / 清晰错误 / 退出码 / 重试）",
        "references": "一主题一文件 + README.md 索引",
        "assets": "模板与示例",
        "method": "混合（确定性逻辑脚本化，澄清/创意由 LLM）",
        "non_goals": "治理文件（MISTAKES/REQUIREMENTS/SOLUTIONS/CHANGELOG）不得被 SKILL.md 正文引用，只由人或工具按需读取",
        "triggers_hint": "发布级 / 高风险 / 多模块场景",
        "workflow": [
            "意图路由（命中路由表对应模块）",
            "预检与参数校验（统一走 scripts/cli.py）",
            "执行核心逻辑（脚本管确定性，LLM 管澄清与创意）",
            "治理台账更新（CHANGELOG / 错误台账按需，不进上下文）",
            "交付 + 完整 Validation（产物 / 退出码 / 格式 / 验证命令）",
        ],
        "routing": "If 命中【模块/意图】→ load references/<module>.md before 执行；治理文件不路由",
        "failure": "四状态 + 模块级隔离（单模块失败不拖垮全局）；升级条件：高风险操作前复述动作并等确认；回退方式：模块级回滚 + 台账记录",
        "validation": "模块级单测 + 端到端一次真实场景 + 退出码与产物双查",
    },
    "suite": {
        "name": "套件型 Skill Suite",
        "tree": "SKILL.md（顶层路由器：场景路由契约 + 全局护栏 + 工程宪法）+ references/ 下 N 个自治子 skill",
        "scripts": "顶层不建脚本（下沉到各子 skill），仅保留工程宪法校验脚本",
        "references": "N 个自治子 skill（各自 SKILL.md，可独立使用/发布）",
        "assets": "下沉到各子 skill",
        "method": "路由为主（顶层只做场景判定与护栏，执行下沉）",
        "non_goals": "顶层不写子域细节（防路由器膨胀）；子域间不互相引用实现细节",
        "triggers_hint": "「某个子域的具体任务」类问句",
        "workflow": [
            "场景识别：按结构化路由契约判定属于哪个子域",
            "加载该子 skill 的 SKILL.md（首读），禁读无关子域",
            "执行该子域动作前检查（动作前检查清单）",
            "跨子域需求走仲裁（冲突仲裁五序）",
            "交付 + 回归（顶层护栏是否被守住）",
        ],
        "routing": "If 命中【子域信号】→ load references/<sub-skill>/SKILL.md before 执行；顶层只留路由 + 护栏",
        "failure": "四状态；升级条件：场景模糊无法路由 → 用选项式让用户选子域；回退方式：退回顶层并列出候选子域",
        "validation": "路由准确率（should/not/ambiguous 三类触发测试）+ 子 skill 各自回归 + 护栏未破",
    },
}

# ─── 各 archetype 的具体文件名建议（B07 ①目录骨架要「写具体文件名」）───
ARCH_FILES: dict[str, dict[str, str]] = {
    "minimal": {
        "scripts": "不建",
        "references": "不建",
        "assets": "不建",
        "note": "单文件起步；装不下时按 references/ → scripts/ → assets/ 顺序扩容",
    },
    "pipeline": {
        "scripts": "check_step.py（步骤产物校验，仅当某步必须 100% 确定才建）",
        "references": "README.md（agent 索引）+ step-guide.md（逐步细则）+ edge-cases.md（症状→原因→修复）",
        "assets": "不建",
        "note": "细则全部下沉 references，SKILL.md 只留路由与 checkpoint",
    },
    "tool": {
        "scripts": "precheck.py（参数/凭据预检）+ call.py（调用 + 超时重试）",
        "references": "api-contract.md（入参 / 返回 / 错误码 / 限流）",
        "assets": "不建",
        "note": "脚本四项要求：参数说明 / 清晰错误 / 退出码 / 重试退避",
    },
    "knowledge": {
        "scripts": "不建（或 index_check.py 校验索引与文件一一对应）",
        "references": "README.md（agent 索引）+ 一主题一文件（按知识主题拆分）",
        "assets": "不建",
        "note": "知识主体全在 references，>300 行的文件须加目录",
    },
    "template": {
        "scripts": "render.py（取模板渲染）+ validate.py（schema / 格式校验）",
        "references": "style-rules.md（排版与写作规范）",
        "assets": "template.md（输出模板，不进上下文）",
        "note": "输出文件约定四要素必须齐全，含错误输出",
    },
    "full": {
        "scripts": "cli.py（统一入口聚合各脚本）+ 各模块脚本",
        "references": "README.md（索引）+ 一模块一文件",
        "assets": "模板与示例",
        "note": "治理台账（CHANGELOG / MISTAKES）不进上下文，不被 SKILL.md 引用",
    },
    "suite": {
        "scripts": "顶层不建（下沉到各子 skill）",
        "references": "N 个自治子 skill（每个自带 SKILL.md，可独立使用/发布）",
        "assets": "下沉到各子 skill",
        "note": "顶层只留路由契约 + 全局护栏，防路由器膨胀",
    },
}

# ─── 各 archetype 的五段骨架侧重（决策表覆盖查表时用它，而非沿用被覆盖的 focus）───
ARCH_FOCUS: dict[str, str] = {
    "minimal": "Workflow 写核心判断规则 + 边界声明（单文件也要写清「不归我管」）",
    "pipeline": "Workflow 写决策树 + checkpoint（分支明确、步骤带中间确认）",
    "tool": "Failure Handling 写四状态 + 重试/降级（超时、限流、鉴权、部分成功）",
    "knowledge": "Resource Routing 写强路由表（If…load…before…）",
    "template": "Validation 写 schema 校验 + 错误输出（失败也产文件）",
    "full": "Workflow 写意图路由表 + 模块级隔离",
    "suite": "SKILL.md 写结构化场景路由契约（信号 / 首读 / 禁读 / 动作前检查 / 常见错误）",
}

# ─── 各 archetype 的待定项（B04）───
ARCH_PENDING: dict[str, list[str]] = {
    "minimal": ["核心判断规则的边界（什么情况明确说「不归我管」）", "是否需要对外部引用做溯源"],
    "pipeline": ["步骤总数与每步的 checkpoint 粒度", "中断后从哪个 checkpoint 续跑", "例外情形的兜底动作"],
    "tool": ["接口凭据与鉴权方式", "限流阈值与重试策略", "超限/部分成功时的降级动作"],
    "knowledge": ["知识主题的拆分粒度（一主题一文件的边界）", "知识过期时的更新机制", "无命中时如何回应"],
    "template": ["输出目录 / 命名 / 格式 / 错误输出 四要素", "模板可变项与固定项的划分", "要素缺失时的默认值策略"],
    "full": ["模块边界与路由表条目", "治理台账的更新时机", "发布级验证清单"],
    "suite": ["子域划分与路由契约信号词", "跨子域需求的仲裁顺序", "子 skill 的独立发布策略"],
}


def _text(answers: dict) -> str:
    """把 answers 拼成一段待扫描文本。

    v3.3.0：materials（C10 历史资料）进扫描列表——此前它属 C 组加分项、
    被排除在推断链之外（收而不化）。信号按「词存在性」计分（非频次），
    塞入长原文不会放大既有信号，只可能引入新命中，爆炸半径可控。
    """
    parts = [str(answers.get(k, "")) for k in
             ("problem", "audience", "example", "priority", "flow", "boundary", "ecosystem", "name", "materials")]
    return " ".join(p for p in parts if p)


def _task_short(problem: str, limit: int = 18) -> str:
    """从 problem 提取一句短任务描述（去掉句首虚词、截断）。

    v3.3.0（G3，真实测发现）：截断符补中文冒号「：」——此前
    「把XX流程标准化：从收集…」会把冒号后半句带进 task_short，
    污染 description 五件事与触发词草稿。
    """
    s = re.sub(r"^(帮|帮我|我想|我要|我想做|我想要|希望|需要|做一个|做个|创建|创建一个)+", "", str(problem).strip())
    s = re.sub(r"[，,。；;：:].*$", "", s).strip()
    if not s:
        s = str(problem).strip()
    if len(s) <= limit:
        return s
    # 语义边界截断：在 limit 内回退到最近的标点/空格，避免把中文词拦腰截断
    head = s[:limit]
    m = re.search(r"[，,。；;：:、\s][^，,。；;：:、\s]*$", head)
    if m and m.start() > limit // 2:
        head = head[:m.start()].rstrip("，,。；;：:、 ")
    return head + "…"


def detect_signals(answers: dict) -> dict[str, int]:
    """扫描 answers 文本 + flow/priority 字段，返回各信号加权得分。

    权重设计：
      - 强关键词（任务性质）  ×2
      - 弱关键词（输出目的地） ×1
      - flow 字段（显式声明）  +2
      - priority 字段（最在意项）按语义加权 +2
    """
    text = _text(answers)
    hits: dict[str, int] = {}
    for sig, words in KEYWORDS_STRONG.items():
        n = sum(2 for w in words if w in text)
        if n:
            hits[sig] = n
    for sig, words in KEYWORDS_WEAK.items():
        n = sum(1 for w in words if w in text)
        if n:
            hits[sig] = hits.get(sig, 0) + n

    # flow 字段：用户对流程节奏的显式声明
    flow = str(answers.get("flow", "")).strip()
    if flow:
        if re.search(r"分步|分几步|确认|多轮|多步|逐步", flow):
            hits["Q1_pipeline"] = hits.get("Q1_pipeline", 0) + 2
        if re.search(r"一次|一次干完|直接|一气呵成|单步", flow):
            hits["_single_shot"] = hits.get("_single_shot", 0) + 2
        if re.search(r"标准化|固定|统一格式|规范", flow):
            hits["Q3_template"] = hits.get("Q3_template", 0) + 2
        if re.search(r"灵活|自由|不确定|看情况", flow):
            hits["_flexible"] = hits.get("_flexible", 0) + 2

    # priority 字段：最在意做对哪一点，直接暴露任务性质
    pr = str(answers.get("priority", "")).strip()
    if pr:
        if re.search(r"格式|统一|一致|规范|标准|排版|不失真", pr):
            hits["Q3_template"] = hits.get("Q3_template", 0) + 2
        if re.search(r"准|可靠|不出错|不能错|稳定|可控|安全", pr):
            hits["Q5_review"] = hits.get("Q5_review", 0) + 2
        if re.search(r"快|简单|一步|省事", pr):
            hits["_single_shot"] = hits.get("_single_shot", 0) + 1
    return hits


def infer_pattern(signals: dict, answers: dict) -> dict:
    """六问信号 → 设计模式（B03）。

    修正规则（实战踩坑）：
      「产出型优先」——文件产出信号不弱于纯知识信号时，模式取 Generator×D。
      理由：用户说「沉淀到 XX 知识库」只是输出去向，不等于 skill 本身是知识密集型；
      而「整理成卡片」决定了它必须走模板产出。这条修正把 archetype 从 knowledge
      拉回 template，避免给出「路由器 + 一堆 references」的错误处方。
    """
    q3 = signals.get("Q3_template", 0)
    qk = signals.get("Q_knowledge", 0)
    override_note = ""
    if q3 > 0 and q3 >= qk:
        ranked_head = "Q3_template"
        if qk > 0:
            override_note = f"（Q3 产出信号 {q3} ≥ Q_knowledge 知识信号 {qk}，按产出型优先）"
    else:
        ranked_head = None

    ranked = sorted(
        (k for k in signals if k in SIGNAL_RULES),
        key=lambda k: (-signals[k], list(SIGNAL_RULES).index(k)),
    )
    if ranked_head and ranked_head in ranked:
        ranked.remove(ranked_head)
        ranked.insert(0, ranked_head)
    primary = ranked[0] if ranked else "Q1_pipeline"

    inter = SIGNAL_RULES[primary]["interaction"]
    content = SIGNAL_RULES[primary]["content"]
    meaning = SIGNAL_RULES[primary]["meaning"]

    # 组合信号（designer-guide §二 结论行）
    # 顺序是有讲究的：产出型（Generator）优先于澄清型（Inversion），
    # 否则「整理成卡片 + 分步确认」会被误判成 Inversion + Pipeline。
    combo = ""
    if q3 > 0 and qk > 0:
        combo = "Generator + 知识路由（模板产出，知识按需加载）"
    elif q3 > 0 and signals.get("Q1_pipeline"):
        combo = "Generator + Pipeline（分步产出，每步可确认）"
    elif signals.get("Q1_pipeline") and signals.get("Q5_review"):
        combo = "Pipeline + Reviewer（边走边检）"
    elif signals.get("Q2_tool") and signals.get("Q5_review"):
        combo = "Tool Wrapper + Reviewer（调用后校验）"
    elif signals.get("Q4_inversion", 0) + signals.get("Q_knowledge", 0) > 0 and signals.get("Q1_pipeline"):
        combo = "Inversion + Pipeline（先澄清再分步执行）"

    # 自由度：单步直达 + 无固定格式 → 高；多步 + 评审/模板 → 低
    if signals.get("_single_shot") and not signals.get("Q5_review") and not signals.get("Q3_template"):
        freedom = "高（单步直达，允许自由发挥）"
    elif signals.get("Q5_review") or signals.get("Q3_template"):
        freedom = "低（输出须可校验 / 格式须固定，收紧自由度）"
    else:
        freedom = "中（关键步骤严格，表述与创意部分自由）"

    alt_pool = [k for k in ranked[1:] if k in SIGNAL_RULES]
    alternatives = " / ".join(
        f"{SIGNAL_RULES[k]['interaction']} × {SIGNAL_RULES[k]['content']}" for k in alt_pool[:2]
    ) or "Inversion × B 领域知识包（若以知识查阅为主）"

    reason_bits = [f"命中 {SIGNAL_RULES[primary]['q']} 信号：{meaning}"]
    if override_note:
        reason_bits.append(override_note.strip("（）"))
    if combo:
        reason_bits.append(f"组合信号 → {combo}")
    if answers.get("priority"):
        reason_bits.append(f"最在意「{answers['priority']}」，与该模式的强项一致")
    if answers.get("flow"):
        reason_bits.append(f"流程性质为「{answers['flow']}」")
    if str(answers.get("materials", "")).strip():
        reason_bits.append("C10 历史资料已纳入信号扫描（v3.3.0）")

    return {
        "interaction": combo.split("（")[0].strip() if combo else inter,
        "content": content,
        "content_key": content,
        "combination": combo,
        "meaning": meaning,
        "freedom": freedom,
        "alternatives": alternatives,
        "reason": "；".join(reason_bits),
        "signals": {k: v for k, v in signals.items() if not k.startswith("_")},
    }


def infer_archetype(pattern: dict, signals: dict, answers: dict, override: str | None) -> dict:
    """模式 → 结构框架（B07）。

    两路合并：
      A. 查 §〇 映射矩阵（B03 模式 → 推荐 archetype）
      B. 走 §一 选型决策表（命中即停的硬规则，优先级高于查表）
    两者不一致时以决策表为准，并把不一致写进 reason 让用户看见。
    """
    # A. 查表
    mapped = PATTERN_TO_ARCH.get((pattern["content_key"], inter_head(pattern)))
    if mapped is None:
        for (c, _i), v in PATTERN_TO_ARCH.items():
            if c == pattern["content_key"]:
                mapped = v
                break
    if mapped is None:
        mapped = {"id": "pipeline", "alt": "full", "focus": "Workflow 写决策树 + checkpoint"}
    mapped_id = mapped["id"]

    # B. 决策表（命中即停）
    has_external = signals.get("Q2_tool", 0) > 0
    has_file = signals.get("Q3_template", 0) > 0
    knowledge_heavy = signals.get("Q_knowledge", 0) >= 4 or (
        signals.get("Q_knowledge", 0) > signals.get("Q3_template", 0)
    )
    multi_step = signals.get("Q1_pipeline", 0) > 0
    review = signals.get("Q5_review", 0) > 0

    if signals.get("suite"):
        decided, why = "suite", "覆盖多个正交子域，单 SKILL.md 装不下"
    elif has_external:
        decided, why = "tool", "存在外部 API / 工具调用，失败路径是头号风险"
    elif has_file:
        decided, why = "template", "有文件产出且格式固定，模板 + 渲染脚本最稳"
    elif knowledge_heavy:
        decided, why = "knowledge", "知识量大且需拆分查阅，references 是主体"
    elif multi_step:
        decided, why = "pipeline", "多步骤带 checkpoint，细则下沉"
    elif review:
        decided, why = "pipeline", "评审类需要 golden checklist + 抽检回路"
    elif not has_file and not has_external and not knowledge_heavy:
        decided, why = "minimal", "无文件产出、无外部调用、知识量小"
    else:
        decided, why = "pipeline", "默认"

    aid = override or decided
    spec = ARCH_SPEC[aid]

    if override and override != decided:
        reason = (f"显式指定 {override}（{spec['name']}）；按决策表推断应为 {decided}"
                  f"（{why}），按 §〇 查表建议为 {mapped_id}——如有冲突以显式指定为准")
        consistent = (override == mapped_id)
    elif decided != mapped_id:
        reason = (f"§一 决策表命中：{why} → {aid}（{spec['name']}）；"
                  f"按 B03「{pattern['interaction']} × {pattern['content_key']}」查 §〇 矩阵得 {mapped_id}，"
                  f"两路不一致时以决策表为准（结构由「产出什么」决定，而非「装什么知识」）")
        consistent = False
    else:
        reason = (f"B03 定了 {pattern['interaction']} × {pattern['content_key']} → "
                  f"§〇 矩阵得 {aid}（{spec['name']}）；决策表复核一致（{why}）")
        consistent = True

    # 备选去重：查表给的 alt 可能与「更轻量方案」撞车
    alts = [mapped["alt"], _lighter_alt(aid).split("（")[0]]
    seen_alt, uniq_alt = set(), []
    for a in alts:
        if a and a != aid and a not in seen_alt:
            seen_alt.add(a)
            uniq_alt.append(a)
    alt_text = " / ".join(
        f"{a}（{'更全但偏重' if a == mapped['alt'] else '更轻但可能装不下'}）" for a in uniq_alt
    ) or "（无更优替代）"

    return {
        "id": aid,
        "name": spec["name"],
        "reason": reason,
        "consistent_with_pattern": consistent,
        "mapped_id": mapped_id,
        "decided_by_rule": why,
        "alternatives": alt_text,
        # focus 跟随最终 archetype：决策表覆盖查表时，侧重段也要跟着换
        "focus": ARCH_FOCUS[aid] if not consistent else mapped["focus"],
    }


def inter_head(pattern: dict) -> str:
    """取交互模式的主类（组合信号取第一段）。"""
    return pattern["interaction"].split(" + ")[0].strip()


def _lighter_alt(aid: str) -> str:
    return {
        "minimal": "pipeline（需要多步时）",
        "pipeline": "minimal（步骤能压到 1–2 步时）",
        "tool": "pipeline（外部调用能去掉时）",
        "knowledge": "minimal（知识量 < 5K 时）",
        "template": "knowledge（若以知识查阅为主、无固定格式）",
        "full": "pipeline（不需要治理台账时）",
        "suite": "full（子域能收敛为一个时）",
    }[aid]


def build_tree(arch: dict, answers: dict) -> dict:
    spec = ARCH_SPEC[arch["id"]]
    files = ARCH_FILES[arch["id"]]
    return {
        "scripts": spec["scripts"],
        "references": spec["references"],
        "assets": spec["assets"],
        "summary": spec["tree"],
        "files": files,
        # B07 ①目录骨架一行（已写具体文件名，结构图会画成子节点）
        "skeleton": (
            f"SKILL.md + scripts/（{files['scripts']}）+ references/（{files['references']}）"
            f"+ assets/（{files['assets']}）+ [CHANGELOG.md 仅发布级]"
        ),
    }


def estimate_br5(design: dict, answers: dict) -> dict[str, dict[str, object]]:
    """BR-5 五维预估分（②初步方案阶段的 AI 预估，③深化设计后重评）。

    打分口径（设计期）：每维 1–5 分，**找不到证据的维度最高给 2 分**。
    证据指向具体积木格，不是拍脑袋的数字。
    """
    aid = design["archetype"]["id"]
    has_example = bool(str(answers.get("example", "")).strip())
    has_flow = bool(str(answers.get("flow", "")).strip())
    has_boundary = bool(str(answers.get("boundary", "")).strip())
    has_materials = bool(str(answers.get("materials", "")).strip())

    # T 边界可信（B01/B05/B06）：IPO+B 四象限已填 + 非目标清单已给
    t = 4 if has_boundary else 3
    # R 失败可控（B05/B06）：Failure Handling 段已给四状态；tool/full 更强
    r = 4 if aid in ("tool", "full") else 3
    # A 触发可辨（B02/B06）：触发词已给五维；有具体样例再 +1；
    # 有真实历史材料（C10）视为触发场景存在性的锚定证据，再加 1（封顶 5）
    a = 4 if (has_example and has_flow) else 3
    if has_materials and a < 5:
        a += 1
    # C 结构可解（B07）：archetype + 目录骨架 + 五段骨架齐备
    c = 4 if design["archetype"]["consistent_with_pattern"] else 3
    # E 验证可证（B05/B08）：Validation 段已给但未实测
    e = 3

    scores = {"T": t, "R": r, "A": a, "C": c, "E": e}
    evidence = {
        "T": "B01 非目标清单 + B05 边界 B 象限（见 01-条件.md / 05-分析.md）",
        "R": "B05 风险 + B07 Failure Handling 段（见 05-分析.md / 07-计划.md）",
        "A": "B02 主体画像 + B06 决策 3 触发策略（见 02-事实.md / 06-决策.md）",
        "C": "B07 结构框架 + 目录骨架 + 五段骨架（见 07-计划.md）",
        "E": "B05 输出 O + B08 验证场景（见 05-分析.md / 08-行动.md）",
    }
    if has_materials:
        evidence["A"] += "；C10 历史材料（真实触发场景的锚定证据）"
    dims = {}
    for k, v in scores.items():
        dims[k] = {"score": v, "evidence": evidence[k]}
    dims["avg"] = round(sum(scores.values()) / 5, 1)
    dims["evs"] = round(sum(scores.values()) / 5 * 20)
    return dims


def build_workflow(arch: dict, answers: dict) -> list[str]:
    spec = ARCH_SPEC[arch["id"]]
    task = _task_short(answers.get("problem", "本任务"))
    out = []
    for step in spec["workflow"]:
        out.append(step.replace("{task_short}", task))
    return out


def build_five_sections(arch: dict, pattern: dict, answers: dict) -> dict:
    """SKILL.md 五段章节骨架（B07 ②）。"""
    spec = ARCH_SPEC[arch["id"]]
    task = _task_short(answers.get("problem", "本任务"))
    wf = build_workflow(arch, answers)
    return {
        "Workflow": "；".join(f"{i}. {s}" for i, s in enumerate(wf, 1)),
        "Clarification Protocol": (
            "一次性追问=缺多个独立配置项（输出目录/命名/格式/阈值）时一次问齐；"
            "逐步澄清=需求本身模糊、需据首轮回答决定后续问法；"
            "选项式=2–4 个方案各有取舍需用户拍板；"
            f"关键假设确认=覆盖/删除/批量/发布前复述「即将对 {task} 做 X」并等确认"
        ),
        "Resource Routing": spec["routing"],
        "Failure Handling": spec["failure"],
        "Validation": spec["validation"],
    }


def build_ipo(arch: dict, pattern: dict, answers: dict) -> dict:
    """B05 IPO+B 四象限。"""
    spec = ARCH_SPEC[arch["id"]]
    task = _task_short(answers.get("problem", "本任务"))
    problem = str(answers.get("problem", "")).strip()
    by_arch = {
        "minimal": dict(
            i=f"用户必须提供 具体情境或待判断对象；Agent 可主动读取 无（单文件无外部依赖）；"
              f"缺失即不能开始 判断对象不明；可默认 输出语言（中文）vs 必须确认 判断所依据的规则边界",
            p=f"标准执行顺序 意图判定 → 匹配判断规则 → 给结论+依据 → 声明边界；"
              f"分支判断点 是否落在声明范围内；必须严格执行 范围判定与边界声明；允许自由发挥 表述与举例",
            o=f"最终交付物 一段结论 + 依据（无文件产出）；格式 对话内 Markdown；"
              f"落盘路径 无；是否需报告·日志 否（对话即记录）",
            b=f"不属于本 skill 需外部数据或多步执行的任务；必须暂停并询问 判断对象超出声明范围时；"
              f"应交由其他 skill 或工具 需要实时数据 / 文件产出的场景",
        ),
        "pipeline": dict(
            i=f"用户必须提供 {task} 的原始输入；Agent 可主动读取 工作区已有上下文；"
              f"缺失即不能开始 原始输入；可默认 每步的输出格式 vs 必须确认 checkpoint 的通过标准",
            p=f"标准执行顺序 见 B07 Workflow 五步；分支判断点 每步 checkpoint 是否通过；"
              f"必须严格执行 checkpoint 校验与状态记录；允许自由发挥 每步内部的措辞与细化建议",
            o=f"最终交付物 走完全流程的成品 + 进度快照；格式 对话内 + 必要的中间产物；"
              f"落盘路径 待 B06 约定；是否需报告·日志 是（每步状态需可见）",
            b=f"不属于本 skill 单步直达的简单请求；必须暂停并询问 checkpoint 不通过时；"
              f"应交由其他 skill 或工具 需要外部 API 的步骤（转 tool 型子能力）",
        ),
        "tool": dict(
            i=f"用户必须提供 调用目标与关键参数；Agent 可主动读取 凭据配置与接口契约；"
              f"缺失即不能开始 凭据或必填参数；可默认 重试次数与退避 vs 必须确认 影响外部状态的操作",
            p=f"标准执行顺序 预检 → 调用 → 校验 → 失败分级 → 交付；分支判断点 返回码与部分成功识别；"
              f"必须严格执行 预检、重试、错误分级（全部脚本化）；允许自由发挥 结果解读与建议",
            o=f"最终交付物 调用结果 + 解读；格式 结构化（JSON/表格）+ 自然语言摘要；"
              f"落盘路径 待 B06 约定；是否需报告·日志 是（调用日志与错误输出）",
            b=f"不属于本 skill 纯推理无外部依赖的任务；必须暂停并询问 写操作/删除操作前；"
              f"应交由其他 skill 或工具 鉴权失效需人工介入时",
        ),
        "knowledge": dict(
            i=f"用户必须提供 待查主题或术语；Agent 可主动读取 references/ 索引与主题文件；"
              f"缺失即不能开始 查询主题；可默认 输出详略 vs 必须确认 知识版本／适用范围",
            p=f"标准执行顺序 意图路由 → 加载对应 references → 按判断规则组织答案 → 溯源标注 → 自检；"
              f"分支判断点 是否有命中条目；必须严格执行 先加载后回答（防臆造）；允许自由发挥 表述与举例",
            o=f"最终交付物 带出处的知识答案；格式 Markdown + 出处标注；"
              f"落盘路径 无（对话内）；是否需报告·日志 否",
            b=f"不属于本 skill 需要实时数据或执行动作的任务；必须暂停并询问 无命中条目时（明说而非臆造）；"
              f"应交由其他 skill 或工具 需落地成文件或流程的场景",
        ),
        "template": dict(
            i=f"用户必须提供 {task} 的内容要素；Agent 可主动读取 assets/ 模板与 style-rules；"
              f"缺失即不能开始 必填要素；可默认 排版细节 vs 必须确认 输出目录与命名",
            p=f"标准执行顺序 收要素 → schema 校验 → 取模板渲染 → 三查 → 交付；"
              f"分支判断点 必填要素是否齐全；必须严格执行 渲染与格式校验（脚本化）；允许自由发挥 内容润色",
            o=f"最终交付物 一份符合固定格式的文件；格式 待 B06 约定；"
              f"落盘路径 待 B06 约定；是否需报告·日志 是（失败也要写错误输出）",
            b=f"不属于本 skill 无固定格式的自由文本；必须暂停并询问 要素缺失且无法默认时；"
              f"应交由其他 skill 或工具 格式渲染引擎不支持时",
        ),
        "full": dict(
            i=f"用户必须提供 意图与关键参数；Agent 可主动读取 模块路由表与治理台账；"
              f"缺失即不能开始 意图不明且无法路由；可默认 模块内部默认值 vs 必须确认 高风险操作",
            p=f"标准执行顺序 路由 → 预检 → 执行 → 台账更新 → 验证；分支判断点 路由命中哪个模块；"
              f"必须严格执行 预检、校验、退出码（脚本化）；允许自由发挥 模块内的创意与澄清",
            o=f"最终交付物 模块产出 + 验证结果；格式 按模块约定；"
              f"落盘路径 待 B06 约定；是否需报告·日志 是（验证命令与结果）",
            b=f"不属于本 skill 超出模块边界的请求；必须暂停并询问 高风险/不可逆操作前；"
              f"应交由其他 skill 或工具 单模块能力不足时",
        ),
        "suite": dict(
            i=f"用户必须提供 具体任务描述；Agent 可主动读取 顶层路由契约与子 skill 索引；"
              f"缺失即不能开始 任务描述；可默认 子域内默认值 vs 必须确认 场景模糊时的子域归属",
            p=f"标准执行顺序 场景识别 → 加载子 skill → 动作前检查 → 仲裁 → 交付；"
              f"分支判断点 命中哪个子域；必须严格执行 路由与护栏检查；允许自由发挥 子 skill 内部",
            o=f"最终交付物 子 skill 的产出；格式 按子 skill 约定；"
              f"落盘路径 按子 skill 约定；是否需报告·日志 是（路由命中记录）",
            b=f"不属于本 skill 顶层不执行具体任务（只路由）；必须暂停并询问 场景模糊无法路由时；"
              f"应交由其他 skill 或工具 子域外请求",
        ),
    }
    d = by_arch[arch["id"]]
    return {
        "input": d["i"], "process": d["p"], "output": d["o"], "boundary": d["b"],
        "method": spec["method"],
        "risk": _infer_risk(arch, answers, problem),
    }


def _infer_risk(arch: dict, answers: dict, problem: str) -> str:
    bits = []
    pr = str(answers.get("priority", "")).strip()
    if pr:
        bits.append(f"最怕出错的环节：{pr}（未满足则 skill 价值归零）")
    by_arch = {
        "tool": "依赖失败（超时/限流/鉴权）是头号风险",
        "template": "格式偏差与要素缺失会导致产出不可用",
        "knowledge": "知识过期或无命中时臆造答案",
        "pipeline": "中间状态丢失导致无法续跑",
        "suite": "路由错判导致加载错误子域",
        "full": "模块间耦合导致单点失败扩散",
        "minimal": "范围声明不清导致被误用在超出能力的场景",
    }
    bits.append(by_arch[arch["id"]])
    bits.append("触发词覆盖不足会导致召回失败")
    return "；".join(bits)


def build_decisions(arch: dict, pattern: dict, ipo: dict, answers: dict) -> dict:
    """B06 三项决策 + 输出文件约定。"""
    aid = arch["id"]
    if aid == "suite":
        d1 = f"拆分（顶层路由器 + N 个自治子 skill）——理由：覆盖多个正交子域，单 SKILL.md 装不下且需分别维护"
    elif aid in ("full",):
        d1 = f"组合但内部分模块（单一 skill，模块边界靠路由表隔离）——理由：领域内聚，拆分会增加调用成本"
    else:
        d1 = "不拆分（单一 skill 覆盖）——理由：任务链路短、目标聚焦，拆分收益小于维护成本"

    scripted = ipo["method"].startswith("脚本") or "混合" in ipo["method"]
    if scripted:
        d2 = f"{ipo['method']} ——理由：确定性部分（校验/渲染/调用/状态）必须 100% 可复现，交给脚本；澄清与创意交给 LLM"
    else:
        d2 = "纯引导（LLM 推理）——理由：本 skill 无确定性计算与外部依赖，脚本化收益低于维护成本"

    triggers = _infer_triggers(answers, arch)
    d3 = f"触发词覆盖中英五维（对象/动作/场景/产出/别名）：{triggers} ——理由：单一名词召回率低，五维覆盖能把 should 类请求接住"

    produces_file = aid in ("template", "full", "tool") or "文件" in ipo["output"]
    if produces_file:
        outdir = "./output/"
        naming = "{日期}-{类型}-{主题}.{ext}"
        fmt = "由 B07 五段骨架 Validation 段声明的格式（模板型以 assets/ 模板为准）"
        erroutf = "同目录写 `{原名}.error.md`，含失败阶段 / 原因 / 已完成的中间产物；不写敏感路径"
    else:
        outdir, naming, fmt, erroutf = "无文件产出", "无", "对话内 Markdown", "对话内返回可读错误提示，不落盘"

    return {
        "decision1": d1,
        "decision2": d2,
        "decision3": d3,
        "output_dir": outdir, "naming": naming, "output_format": fmt, "error_output": erroutf,
        "produces_file": produces_file,
        "triggers": triggers,
        "adr": f"决策 采用 {aid}（{arch['name']}） / 置信度 75% / 依据 {arch['reason']} / 替代方案 {arch['alternatives']}",
        "abandoned": f"废弃方案：{arch['alternatives'].split('（')[0]} / 原因：与「{answers.get('priority', '首要目标') or '首要目标'}」相比性价比更低",
    }


def _infer_triggers(answers: dict, arch: dict) -> str:
    """从 problem / name / 关键词反推触发词候选。"""
    task = _task_short(answers.get("problem", ""), limit=20).strip("…")
    name = str(answers.get("name", "")).strip()
    text = _text(answers)
    verbs = [w for w in ("整理", "生成", "检查", "分析", "导出", "总结", "梳理", "评估", "翻译", "转写", "归档", "检索")
             if w in text]
    objs = [w for w in ("笔记", "报告", "卡片", "清单", "知识库", "文档", "数据", "表格", "材料", "流程", "代码", "论文")
            if w in text]
    parts = []
    # name 是用户确认过的 skill 名，优先作为首要触发词；task 短句作补充
    if name:
        parts.append(name)
    if task and task not in parts:
        parts.append(task)
    for v in verbs[:2]:
        parts.append(v)
    for o in objs[:2]:
        parts.append(o)
    parts.append(ARCH_SPEC[arch["id"]]["triggers_hint"])
    seen, out = set(), []
    for p in parts:
        if p and p not in seen:
            seen.add(p)
            out.append(p)
    return " / ".join(out[:8])


def build_pending(arch: dict, answers: dict) -> list[str]:
    """B04 待定项清单（archetype 固有 + B 组缺失字段）。"""
    items = list(ARCH_PENDING[arch["id"]])
    for key, label in (("priority", "最在意做对哪一点（B5）"),
                       ("flow", "流程性质：一次干完 / 分步确认（B6）"),
                       ("example", "一个具体样例（B7）"),
                       ("boundary", "明确不做什么（C8）"),
                       ("ecosystem", "生态位：与哪些已有 skill 相邻（C9）")):
        if not str(answers.get(key, "")).strip():
            items.insert(0, f"{label} —— 缺失，需用户补")
    return items[:5]


def build_non_goals(arch: dict, answers: dict) -> str:
    base = ARCH_SPEC[arch["id"]]["non_goals"]
    if answers.get("boundary"):
        return f"{base}；用户补充：{answers['boundary']}"
    return base


def build_description_five(arch: dict, pattern: dict, answers: dict) -> str:
    """生成 description 五件事草稿（WHAT / WHEN / NEGATIVE / 触发词 / 语言），
    单行文本，供 index.md frontmatter 与 export SKETCH「1. 定位」使用。

    五件事对应 validate_skill 与 trace_patch 的 description 五件事口径：
    WHAT（做什么）/ WHEN（何时用）/ NEGATIVE（何时不用）/ 触发词 / 语言。
    """
    task = _task_short(answers.get("problem", "本任务"), limit=24)
    triggers = _infer_triggers(answers, arch)
    neg = build_non_goals(arch, answers).split("；")[0] if build_non_goals(arch, answers) else "一次性脚本、无复用价值的单点任务"
    what = f"做什么：把「{task}」做成可复用的 skill"
    when = f"何时用：创建 / 设计 / 改进 skill，或说「{triggers.split(' / ')[0]}」等"
    neg_s = f"何时不用：{neg}"
    trig = f"触发词：{triggers}"
    lang = "语言：中文主语言，技术术语保留英文"
    return "；".join([what, when, neg_s, trig, lang])


def infer_design(answers: dict, archetype: str | None = None) -> dict:
    """主入口：①概念讨论的 answers → 整套设计建议。"""
    if archetype and archetype not in ARCHETYPE_IDS:
        raise ValueError(f"未知 archetype：{archetype}（可选：{'/'.join(ARCHETYPE_IDS)}）")

    signals = detect_signals(answers)
    pattern = infer_pattern(signals, answers)
    arch = infer_archetype(pattern, signals, answers, archetype)
    tree = build_tree(arch, answers)
    five = build_five_sections(arch, pattern, answers)
    ipo = build_ipo(arch, pattern, answers)
    decisions = build_decisions(arch, pattern, ipo, answers)
    pending = build_pending(arch, answers)

    d = {
        "pattern": pattern,
        "archetype": arch,
        "tree": tree,
        "workflow": build_workflow(arch, answers),
        "five_sections": five,
        "ipo": ipo,
        "decisions": decisions,
        "pending": pending,
        "non_goals": build_non_goals(arch, answers),
        "description_five": build_description_five(arch, pattern, answers),
        "task_short": _task_short(answers.get("problem", "本任务")),
        "ai_tag": AI_TAG,
        "pending_tag": PENDING_TAG,
    }
    d["br5"] = estimate_br5(d, answers)
    return d


def main() -> int:
    # UTF-8 兜底已由模块级 enable_utf8() 统一处理（含 stderr，见 errors.py）
    ap = argparse.ArgumentParser(
        description="②初步方案推断引擎：六问信号 → 设计模式 → 结构框架 → 五段骨架",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="数据源：references/designer-guide.md §二 与 references/skill-archetypes.md §〇/§一",
    )
    ap.add_argument("--answers", required=True, help="JSON 文件路径 或 JSON 字符串")
    ap.add_argument("--archetype", "-a", choices=ARCHETYPE_IDS, help="显式指定结构框架（覆盖推断）")
    ap.add_argument("--json", action="store_true", help="输出完整 JSON（默认输出可读摘要）")
    args = ap.parse_args()

    p = Path(args.answers)
    try:
        if p.exists():
            answers = json.loads(read_text_robust(p))
        elif args.answers.endswith(".json") or "/" in args.answers or "\\" in args.answers:
            # 看着像路径却找不到 → 报路径错误，别误报成 JSON 语法错误
            raise FileNotFoundError(args.answers)
        else:
            answers = json.loads(args.answers)
    except json.JSONDecodeError as e:
        return fail("E002", detail=str(e), script="infer_design")
    except (FileNotFoundError, OSError):
        return fail("E001", detail=args.answers, script="infer_design")

    try:
        d = infer_design(answers, args.archetype)
    except ValueError as e:
        print(f"[infer_design] {e}")
        return 1

    if args.json:
        print(json.dumps(d, ensure_ascii=False, indent=2))
        return 0

    pt, ar = d["pattern"], d["archetype"]
    print(f"任务摘要：{d['task_short']}")
    print(f"命中信号：{', '.join(f'{k}×{v}' for k, v in pt['signals'].items()) or '（无，走默认）'}")
    print()
    print(f"[B03 设计模式] {pt['interaction']} × {pt['content']}  自由度：{pt['freedom']}")
    print(f"  理由：{pt['reason']}")
    print(f"  备选：{pt['alternatives']}")
    print()
    print(f"[B07 结构框架] {ar['id']}（{ar['name']}）")
    print(f"  理由：{ar['reason']}")
    print(f"  侧重段：{ar['focus']}")
    print(f"  备选：{ar['alternatives']}")
    print(f"  目录骨架：{d['tree']['summary']}")
    print()
    print("[SKILL.md 五步 Workflow]")
    for i, s in enumerate(d["workflow"], 1):
        print(f"  {i}. {s}")
    print()
    print(f"[B05 方法] {d['ipo']['method']}")
    print(f"[B06 决策] 拆分={d['decisions']['decision1'][:24]}… | 脚本化={d['decisions']['decision2'][:24]}…")
    print(f"[B06 触发词] {d['decisions']['triggers']}")
    print()
    print("[B04 待定项]")
    for i, it in enumerate(d["pending"], 1):
        print(f"  {i}. {it}")
    print()
    print(f"→ 以上均为 {AI_TAG}，用户回「按建议」即可批量采纳；只推翻某一格也支持。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
