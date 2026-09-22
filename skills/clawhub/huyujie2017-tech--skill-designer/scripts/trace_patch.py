"""
trace_patch.py — 把五维评分转成可执行补丁清单（双口径）

两套口径（与 references/trace-evaluation-guide.md 一致）：
  --mode design（设计期 BR-5）：评价对象是**设计蓝图**，输出「补哪一格」
  --mode ship  （发布期 TRACE，默认）：评价对象是**已落地的 skill**，输出「改哪个文件」

用法：
    # 设计期：蓝图 BR-5 自评后，生成补格清单
    python scripts/trace_patch.py <反馈.json> --mode design --output patches.md

    # 发布期：收到 SkillHub TRACE 返评后，生成补丁清单（默认）
    python scripts/trace_patch.py <反馈.json> [--threshold 4.5] [--output patches.md]
    python scripts/trace_patch.py '{"platform":"SkillHub TRACE","scores":{"T":4.8,"R":4.3,...}}' --json

输入格式（JSON）：
{
  "platform": "SkillHub TRACE",
  "skill_name": "skill-designer",
  "scores": {"T": 4.8, "R": 4.3, "A": 4.5, "C": 4.4, "E": 4.6},
  "comments": {
    "R": "缺少自动重试，网络问题需手动重来",
    "C": "FAQ 不好找"
  }
}

输出：
- Markdown：按 P0/P1/P2 排序的补丁清单，含维度、分数、评语、修复目标、动作、验收命令
- JSON：结构化数据，可被其他脚本或 skill 消费（含 mode 与 target 字段）
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8, fail  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

# ─── TRACE 维度定义 ───
DIMENSIONS: dict[str, dict[str, Any]] = {
    "T": {
        "name": "Trust（可信任度）",
        "threshold": 4.5,
        "keywords": ["密钥", "权限", "敏感", "隐私", "安全", "硬编码", "API key", "token", "secret", "password"],
        "patches": [
            ("P0", "运行 `scripts/validate_skill.py --self`，确保 §6 安全扫描通过（无 XML/保留词/疑似密钥）"),
            ("P0", "检查 scripts/ 与 references/ 是否明文写死 API key / token / password"),
            ("P1", "在 B06 输出文件约定中明确输出目录、命名、格式、错误输出"),
            ("P1", "确保 SKILL.md description 不索要超出任务需要的权限"),
        ],
    },
    "R": {
        "name": "Reliability（可靠性）",
        "threshold": 4.5,
        "keywords": ["重试", "网络", "手动重来", "失败", "卡死", "报错", "异常", "中断", "不稳定", "出错"],
        "patches": [
            ("P0", "为脚本统一接入 retry.py / sd_cli.py `--retries`，默认 3 次指数退避"),
            ("P0", "在 B05 边界字段补充空输入 / 超长 / 极少匹配 / 用户取消的处理"),
            ("P1", "在 B06 错误输出约定中明确失败时的用户提示与下一步动作"),
            ("P1", "检查 flow-recovery.md 断点续跑机制是否落地为 checkpoint 表 + 检查脚本"),
        ],
    },
    "A": {
        "name": "Adaptability（适用性）",
        "threshold": 4.5,
        "keywords": ["触发", "误触发", "漏触发", "边界", "什么时候", "该不该用", "适用范围", "场景"],
        "patches": [
            ("P0", "重写 SKILL.md description，确保含 WHEN（何时触发/典型说法）与 NEGATIVE（何时不使用）"),
            ("P0", "检查 capability-boundary.md 是否列出 10+ 正反例与分工"),
            ("P1", "为 description 增加 3–5 个具体触发词示例（中英同义）"),
            ("P2", "跑 trigger 测试：should / not / ambiguous 三类，记录召回率"),
        ],
    },
    "C": {
        "name": "Convention（规范性）",
        "threshold": 4.5,
        "keywords": ["FAQ", "找不到", "文档", "太长", "结构", "规范", "版本", "CHANGELOG", "索引", "导航"],
        "patches": [
            ("P0", "在 onboarding.md 顶部加 FAQ 快速导航锚点，并把 FAQ 提升为独立一级章节"),
            ("P0", "在 references/README.md 中把 FAQ / 发布前自查作为高亮标签"),
            ("P1", "确保 CHANGELOG.md 有版本号、日期、变更分类"),
            ("P1", "检查 references 索引机制：agent 应先读 README.md 再按需加载"),
        ],
    },
    "E": {
        "name": "Effectiveness（有效性）",
        "threshold": 4.5,
        "keywords": ["输出", "解决", "效果", "验证", "测试", "可用", "质量", "不走运", "整理"],
        "patches": [
            ("P0", "在 B08 行动积木补充真实场景验证 + 有/无 skill baseline 对比"),
            ("P0", "确保 B05 输出契约明确产物格式、可直接使用或少量检查即可发布"),
            ("P1", "让 B09 评分指向具体改进项，而不是只有一个数字"),
            ("P1", "用 export_brief.py 生成 SKETCH.md，验证产物可被 skill-creator 直接消费"),
        ],
    },
}


# ─── 设计期口径 BR-5：蓝图就绪度（问「约定了吗」，补丁指向「补哪一格」） ───
BR5_NAMES = {
    "T": "边界可信",
    "R": "失败可控",
    "A": "触发可辨",
    "C": "结构可解",
    "E": "验证可证",
}

BR5_DESIGN_PATCHES: dict[str, list[tuple[str, str, str]]] = {
    # (优先级, 补哪一格, 具体动作)
    "T": [
        ("P0", "01-条件.md", "写清准入四问结论与边界：这个 skill 做什么、不做什么"),
        ("P0", "06-决策.md", "输出四要素逐项填出：目录 / 命名 / 格式 / 错误输出"),
        ("P1", "05-分析.md", "列权限与敏感数据风险：需不需要密钥、碰到个人信息怎么处理"),
        ("P1", "06-决策.md", "allowed-tools 只列必需工具，说明权限最小化依据"),
    ],
    "R": [
        ("P0", "05-分析.md", "边界字段列全：空输入 / 超长 / 极少匹配 / 用户取消"),
        ("P0", "06-决策.md", "约定失败时的输出格式与用户提示（给可执行的下一步，不是 traceback）"),
        ("P1", "06-决策.md", "设计降级路径：依赖的脚本或兄弟 skill 不可用时怎么办"),
        ("P1", "index.md", "补断点续跑约定：产物落盘 + checkpoint 表 + 检查脚本（flow-recovery.md）"),
    ],
    "A": [
        ("P0", "02-事实.md", "补生态正交性检查：列出相邻 skill，说明为什么不重叠"),
        ("P0", "06-决策.md", "description 五件事填全：WHAT / WHEN / NEGATIVE / 触发词 / 边界归属"),
        ("P1", "06-决策.md", "触发词覆盖中英同义与省略表达，各给 3–5 个真实说法"),
        ("P2", "08-行动.md", "排触发测试计划：should / not / ambiguous 三类"),
    ],
    "C": [
        ("P0", "07-计划.md", "选定 archetype（6 选 1）并写出选型理由"),
        ("P0", "07-计划.md", "目录骨架要含**具体文件名**，不能只画层级"),
        ("P0", "07-计划.md", "SKILL.md 五段骨架逐段填出，不是只写五个标题"),
        ("P1", "07-计划.md", "定 references 索引策略：README.md 索引 + 每份文件的加载条件"),
        ("P2", "07-计划.md", "跑 `render_structure.py` 出结构图，自检「施工的人看得懂吗」"),
    ],
    "E": [
        ("P0", "05-分析.md", "输出契约写清产物格式，要求可直接交付"),
        ("P0", "08-行动.md", "指定真实验证场景（非空泛测试）+ 有/无 skill 对比计划"),
        ("P1", "08-行动.md", "安排独立审：人亲自审，AI 不当自己作业的唯一判官"),
        ("P1", "09-结果.md", "B09 评分必须指向具体改进项，而不是只有一个数字"),
    ],
}

# 发布期口径：每维的补丁落到哪些文件
SHIP_TARGETS = {
    "T": "SKILL.md frontmatter / scripts/",
    "R": "scripts/retry.py + B05 / B06",
    "A": "SKILL.md description / capability-boundary.md",
    "C": "quickstart.md / references/README.md / CHANGELOG.md",
    "E": "B05 输出契约 / B08 验证 / export_brief.py",
}


# ─── 通用修复动作（不绑定具体维度） ───
GENERAL_PATCHES = [
    ("P1", "把本补丁清单回填到 B09 结果积木 9.2 节，作为下一轮迭代的输入"),
    ("P1", "更新 CHANGELOG.md，记录本次针对外部评测的修复"),
    ("P2", "运行 `scripts/validate_skill.py --self` 与 `scripts/sd_cli.py validate --self` 验收"),
]

DESIGN_GENERAL_PATCHES = [
    ("P1", "把本清单回填到 `09-结果.md` 9.1 的 BR-5 自评表，作为下一轮迭代的输入"),
    ("P1", "修复顺序：先补**没填的格**（涨 IQS 见效快），再深化设计**填得浅的格**（涨 BR-5）"),
    ("P2", "运行 `scripts/check_blueprint.py <蓝图目录>` 验收集，确认缺口已清零"),
]


def parse_feedback(raw: str) -> dict[str, Any]:
    """解析反馈：支持 JSON 文件路径或 JSON 字符串。

    为什么显式判路径：直接 json.loads("./nope.json") 会抛 JSONDecodeError，
    用户看到的是「JSON 语法错误」——但真实问题是文件不存在，两个错误的
    下一步动作完全不同（改路径 vs 改内容），必须分开报。
    """
    p = Path(raw)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    if raw.endswith((".json", ".JSON")) or "/" in raw or "\\" in raw:
        raise FileNotFoundError(raw)
    return json.loads(raw)


def score_level(score: float, threshold: float) -> str:
    if score >= threshold + 0.3:
        return "ok"
    if score >= threshold:
        return "warn"
    return "critical"


def dim_patches(dim: str, score: float, comment: str | None, mode: str = "ship") -> list[dict[str, Any]]:
    """为某个维度生成补丁项。

    mode=design → 设计期 BR-5，target 指向「补哪一格」
    mode=ship   → 发布期 TRACE，target 指向「改哪个文件」
    """
    meta = DIMENSIONS[dim]
    level = score_level(score, meta["threshold"])
    result = []
    if mode == "design":
        items = [(prio, blk, act) for prio, blk, act in BR5_DESIGN_PATCHES.get(dim, [])]
        dim_name = f"{BR5_NAMES[dim]}（设计期）"
    else:
        items = [(prio, SHIP_TARGETS.get(dim, ""), act) for prio, act in meta["patches"]]
        dim_name = meta["name"]
    for prio, target, action in items:
        result.append({
            "priority": prio,
            "dimension": dim,
            "dimension_name": dim_name,
            "target": target,
            "action": action,
            "score": score,
            "level": level,
            "comment": comment or "",
        })
    return result


def build_patch_list(feedback: dict[str, Any], threshold: float | None = None, mode: str = "ship") -> dict[str, Any]:
    """构建完整补丁清单。mode: design（设计期 BR-5）| ship（发布期 TRACE，默认）。"""
    platform = feedback.get("platform", "外部评测")
    skill_name = feedback.get("skill_name", "")
    scores: dict[str, float] = feedback.get("scores", {})
    comments: dict[str, str] = feedback.get("comments", {})

    # 缺省维度补 0
    for dim in DIMENSIONS:
        scores.setdefault(dim, 0.0)

    effective_threshold = threshold or 4.5
    patches: list[dict[str, Any]] = []

    # 先处理有评语的维度（更具体）
    for dim in sorted(scores, key=lambda d: scores.get(d, 0.0)):
        score = float(scores[dim])
        if score >= effective_threshold + 0.3 and dim not in comments:
            continue  # 高分且无评语，跳过
        comment = comments.get(dim)
        patches.extend(dim_patches(dim, score, comment, mode))

    # 通用收尾
    general = DESIGN_GENERAL_PATCHES if mode == "design" else GENERAL_PATCHES
    for prio, action in general:
        patches.append({
            "priority": prio,
            "dimension": "ALL",
            "dimension_name": "通用收尾",
            "target": "09-结果.md" if mode == "design" else "B09 / CHANGELOG.md",
            "action": action,
            "score": 0.0,
            "level": "info",
            "comment": "",
        })

    # 排序：P0 > P1 > P2；同优先级按维度分数升序（最差的在前）
    priority_order = {"P0": 0, "P1": 1, "P2": 2}
    patches.sort(key=lambda x: (priority_order.get(x["priority"], 99), x["score"]))

    lowest_dim = min(scores, key=scores.get) if scores else None

    return {
        "mode": mode,
        "platform": platform,
        "skill_name": skill_name,
        "threshold": effective_threshold,
        "scores": scores,
        "comments": comments,
        "lowest_dimension": lowest_dim,
        "lowest_score": scores.get(lowest_dim, 0.0) if lowest_dim else 0.0,
        "patches": patches,
    }


def format_markdown(data: dict[str, Any]) -> str:
    mode = data.get("mode", "ship")
    design = mode == "design"
    title_suffix = "（设计期 BR-5 口径）" if design else "（发布期 TRACE 口径）"
    scope_hint = (
        "> 评价对象：**设计蓝图** ｜ 问的是「这一条**约定了吗**」 ｜ 补丁指向「补哪一格」"
        if design else
        "> 评价对象：**已落地的 skill** ｜ 问的是「这一条**做到了吗**」 ｜ 补丁指向「改哪个文件」"
    )

    header = ["| 维度 | 分数 | 阈值 | 状态 | 评语 |"]
    if design:
        header = ["| 维度 | 分数 | 阈值 | 状态 | 补哪一格 | 评语 |"]

    lines = [
        f"# {data['platform']} 反馈补丁清单{title_suffix}",
        "",
        f"> 目标 skill：`{data.get('skill_name') or '（未指定）'}` ｜ 分数阈值：{data['threshold']}",
        "",
        scope_hint,
        "",
        "## 五维评分",
        "",
        *header,
        "|------|------|------|------|------|" if not design else "|------|------|------|------|------|------|",
    ]
    for dim in ["T", "R", "A", "C", "E"]:
        score = data["scores"].get(dim, 0.0)
        meta = DIMENSIONS[dim]
        level = score_level(score, meta["threshold"])
        badge = {"ok": "✅ 达标", "warn": "⚠️ 临界", "critical": "❌ 低于阈值"}.get(level, "—")
        comment = data["comments"].get(dim, "—")
        if design:
            blocks = "/".join(sorted({blk for _, blk, _ in BR5_DESIGN_PATCHES.get(dim, [])}))
            lines.append(f"| {dim} {BR5_NAMES[dim]} | {score} | {meta['threshold']} | {badge} | {blocks} | {comment} |")
        else:
            lines.append(f"| {dim} {meta['name']} | {score} | {meta['threshold']} | {badge} | {comment} |")

    lowest = data["lowest_dimension"]
    lowest_name = BR5_NAMES.get(lowest, "") if design else DIMENSIONS.get(lowest, {}).get("name", lowest)
    lines.extend([
        "",
        f"## 最低分项：{lowest}（{data['lowest_score']} 分）",
        "",
        f"最低分维度：**{lowest_name}**",
        f"评语：{data['comments'].get(lowest, '（无）')}",
        "",
        "## 补丁清单（按优先级 P0 → P2）",
        "",
    ])

    current_prio = None
    for idx, p in enumerate(data["patches"], 1):
        if p["priority"] != current_prio:
            current_prio = p["priority"]
            lines.append(f"### {current_prio}")
            lines.append("")
        dim_label = f"[{p['dimension']}]" if p["dimension"] != "ALL" else "[通用]"
        target = p.get("target") or ""
        target_label = f"`{target}` → " if target else ""
        lines.append(f"{idx}. {dim_label} {target_label}{p['action']}")
    lines.append("")

    if design:
        lines.extend([
            "## 验收命令",
            "",
            "```bash",
            "# 1. 蓝图缺口检查（确认该补的格都补了）",
            "python scripts/check_blueprint.py <蓝图目录>",
            "",
            "# 2. 结构图自检：施工的人看得懂吗",
            "python scripts/render_structure.py <蓝图目录> --output structure.svg",
            "",
            "# 3. 重新评分并出摘要图",
            "python scripts/b09_summary.py <蓝图目录> --output b09-summary.svg",
            "```",
            "",
            "## 回填位置",
            "",
            "- 补丁清单摘要 → `09-结果.md` 9.1 BR-5 自评表（每维补证据）",
            "- 补格结果 → 对应积木格文件（`01-条件.md` … `08-行动.md`）",
            "- 归纳成通用规则 → `10-复盘.md`",
            "",
        ])
    else:
        lines.extend([
            "## 验收命令",
            "",
            "```bash",
            "# 1. 安全与静态检查",
            "python scripts/validate_skill.py --self",
            "",
            "# 2. 统一 CLI 自检验收",
            "python scripts/sd_cli.py validate --self",
            "",
            "# 3. 如修改后重新发布，把新反馈再次喂给 trace_patch.py 验证闭环",
            "python scripts/trace_patch.py feedback.json --output patches-v2.md",
            "```",
            "",
            "## 回填位置",
            "",
            "- 补丁清单摘要 → `09-结果.md` §9.2 外部平台评价回流",
            "- 失败/不足归纳成通用规则 → `10-复盘.md`",
            "- 版本记录 → `CHANGELOG.md`",
            "",
        ])
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(
        description="把外部平台评测反馈转成可执行补丁清单",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("feedback", help="反馈 JSON 文件路径或 JSON 字符串")
    ap.add_argument(
        "--mode", choices=("design", "ship"), default="ship",
        help="口径：design=设计期 BR-5（补哪一格，评蓝图）｜ship=发布期 TRACE（改哪个文件，评成品，默认）",
    )
    ap.add_argument("--threshold", type=float, default=4.5, help="低于此分数视为需修复（默认 4.5）")
    ap.add_argument("--output", "-o", help="输出文件路径（默认 stdout）")
    ap.add_argument("--json", action="store_true", help="输出 JSON 而非 Markdown")
    args = ap.parse_args()

    try:
        feedback = parse_feedback(args.feedback)
    except json.JSONDecodeError as e:
        # 英文原文降级为括号附注，主视觉给中文人话 + 一个可执行动作
        return fail("E002", detail=str(e), script="trace_patch")
    except (FileNotFoundError, OSError):
        return fail("E001", detail=args.feedback, script="trace_patch")

    data = build_patch_list(feedback, args.threshold, args.mode)

    if args.json:
        out = json.dumps(data, ensure_ascii=False, indent=2)
    else:
        out = format_markdown(data)

    if args.output:
        Path(args.output).write_text(out, encoding="utf-8")
        print(f"[trace_patch] 补丁清单已写入：{args.output}")
    else:
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
