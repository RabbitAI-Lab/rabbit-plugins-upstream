#!/usr/bin/env python3
"""
export_brief.py — 蓝图交接产物生成器（skill-designer）

把通过 check_blueprint.py 的施工蓝图，导出为 3 种标准化交接产物：
  1. summary.md      — 人类可读的项目小结与落地指南
  2. brief.json      — 机器可解析的完整蓝图摘要
  3. SKETCH.md       — 可直接交给 skill-creator 的精简需求规格书

用法：
    python scripts/export_brief.py <蓝图目录> --output <产物目录> [--format all|md|json|sketch] [--glossary]
    python scripts/export_brief.py <蓝图目录> --stdout --format json   # 直接输出 JSON 到 stdout

退出码：0 = 成功；1 = 蓝图未通过检查或参数错误。
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Optional
sys.path.insert(0, str(Path(__file__).resolve().parent))
from errors import enable_utf8  # noqa: E402

enable_utf8()  # Windows GBK 控制台下保证中文（含 stderr 报错）不乱码

# 相对 imports 在直接运行时不可用；脚本放在 scripts/ 中，通过根目录调用
ROOT = Path(__file__).resolve().parent.parent

BLOCK_FILES = {
    "B01": "01-条件.md", "B02": "02-事实.md", "B03": "03-观点.md",
    "B04": "04-问题.md", "B05": "05-分析.md", "B06": "06-决策.md",
    "B07": "07-计划.md", "B08": "08-行动.md", "B09": "09-结果.md",
    "B10": "10-复盘.md",
}

# 术语白话表（--glossary 用）：与 blueprint-methodology §十 口径一致，一词一句大白话。
GLOSSARY: list[tuple[str, str]] = [
    ("积木链 / B01–B10", "把一个 skill 从念头到落地拆成 10 步：条件→事实→观点→问题→分析→决策→计划→行动→结果→复盘，顺序走完蓝图就成型"),
    ("蓝图", "一份写清楚「做什么 / 不做什么 / 怎么触发 / 长什么样」的施工设计稿，落地施工照它来"),
    ("施工蓝图", "第四步产出的正式版蓝图，机器检查通过、可交给创建类 skill 直接开工"),
    ("IQS", "蓝图质量分（0–100，机器算）：看十格填得实不实，85+ 算扎实"),
    ("BR-5", "蓝图五维体检：好触发 / 跑得稳 / 好用 / 合规矩 / 有证据，每维找得到证据才给分"),
    ("强制阻塞", "触发词和 skill 名必须您自己定——AI 代填的名字上线后可能永远触发不了"),
    ("AUTO / REQUIRED", "AI 自动补全的事项（标注可改）vs 必须您拍板的事项（每次带建议+理由+备选）"),
    ("AI 建议三件套", "AI 提问的固定格式：建议值 + 理由 + 备选；回「按建议」即可批量采纳"),
    ("轻量 / 完整通道", "约 30 分钟出蓝图的最短路径 vs 约 2 小时多轮打磨的深度路径"),
    ("伴随守门", "已有 skill 在手、不想重走蓝图时，AI 只做逐格把关不替您写"),
    ("checkpoint / 续跑", "进度随时存盘，会话中断后新开一个，机器报缺口、从缺口继续"),
    ("有 / 无对比", "同一个真实任务，有蓝图和没蓝图各跑一遍——实证 skill 值不值的硬证据"),
]


def read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8-sig", errors="replace")
    except OSError:
        return ""


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---", text.lstrip(), re.DOTALL)
    if not m:
        return {}
    fm: dict[str, str] = {}
    for line in m.group(1).splitlines():
        kv = re.match(r'^([A-Za-z_][\w-]*)\s*:\s*"?(.*?)"?\s*$', line)
        if kv:
            fm[kv.group(1)] = kv.group(2).strip().strip('"')
    return fm


def parse_checkpoint(text: str) -> dict:
    cp: dict[str, str] = {}
    m = re.search(r"##\s*进度快照.*?\n((?:\|[^\n]*\n)+)", text, re.DOTALL)
    if not m:
        return cp
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and cells[0] not in ("字段", "---", "----", "------"):
            cp[cells[0]] = cells[1]
    return cp


def filled_lines(text: str) -> list[str]:
    """返回非空且非占位符（______ / ☐）的字段行。"""
    out = []
    for ln in text.splitlines():
        s = re.sub(r"^[\s>\-•]+", "", ln).strip()
        if not s or "______" in s or "☐" in s:
            continue
        if s.startswith("#") or s.startswith(">"):
            continue
        out.append(s)
    return out


def extract_key_value(text: str, keys: list[str]) -> dict[str, str]:
    """从「填空字段」区域内按 key: value 模式提取给定 keys；允许 key 后紧跟括号说明再跟冒号。"""
    # 只扫描 "## 填空字段" 到 "## 验收" 之间的内容，避免结构公式/标题误匹配
    m = re.search(r"##\s*填空字段.*?(?=##\s*验收|\Z)", text, re.DOTALL)
    field_area = m.group(0) if m else text
    found: dict[str, str] = {}
    for key in keys:
        # key 前须为行首 / 列表符号 / 表格分隔符；key 后可跟非冒号、非换行说明，再跟冒号
        pat = rf"(?:^|[\n\r]|[-|]\s+){re.escape(key)}[^:：\n\r]*[:：]\s*(.+?)(?:\n|\r|$)"
        for match in re.finditer(pat, field_area):
            val = match.group(1).strip()
            if "______" not in val:
                found[key] = val
                break
    return found


def run_check(bp_dir: Path, python: str) -> tuple[bool, dict]:
    cmd = [python, str(ROOT / "scripts" / "check_blueprint.py"), str(bp_dir), "--json"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", check=False)
    except Exception as e:
        return False, {"ok": False, "error": f"无法调用 check_blueprint.py: {e}"}
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return False, {"ok": False, "error": f"check_blueprint.py 输出非法 JSON: {proc.stdout[:200]}"}
    return bool(data.get("ok") and proc.returncode == 0), data


def summarize_block(bid: str, text: str) -> dict:
    """把单格内容压缩为摘要。"""
    lines = filled_lines(text)
    keys_of_interest = {
        "B01": ["结论", "非目标"],
        "B02": ["主体", "动作", "客体", "正交性"],
        "B03": ["判断", "依据"],
        "B04": ["待定项", "归属"],
        "B05": ["输入", "输出", "方法", "边界", "风险"],
        "B06": ["决策 1", "决策 2", "决策 3", "输出目录", "命名", "格式", "错误输出"],
        "B07": ["目标", "目录骨架", "实施步骤", "时间表"],
        "B08": ["验证场景", "有 / 无对比", "触发测试", "效果测试", "独立审"],
        "B09": ["内部质量分", "外部价值分", "综合评分", "指向的改进项"],
        "B10": ["失败/不足", "归纳为通用规则", "经验", "下一轮迭代点"],
    }
    highlights: dict[str, str] = extract_key_value(text, keys_of_interest.get(bid, []))
    # 如果关键 key 没命中，退而取前 3 条非空字段
    if not highlights and lines:
        highlights = {f"要点{i+1}": ln for i, ln in enumerate(lines[:3])}
    return {
        "bid": bid,
        "file": BLOCK_FILES[bid],
        "highlights": highlights,
        "raw_summary": "\n".join(lines[:6]),
    }


def block_marker_status(text: str) -> str:
    """按蓝图文件中残留标注判断该格决策类型（轻量启发式）。

    三档标记（v2.14.0 起取代旧的单一【草稿，待确认】）：
      【需用户拍板】→ 用户拍板项（必核）
      【AI 建议】   → AI 建议（待确认）
      【待回填】    → 待回填（时机未到）
    否则视为已确认。施工蓝图通常全为"已确认"，有残留说明还没收尾。

    优先级按"谁说了算"递减：必须人拍板 > 人有条件要补 > AI 有主张 > 全清。
    """
    if "【需用户拍板】" in text:
        return "用户拍板项（必核）"
    if "【待回填】" in text:
        return "待回填（时机未到）"
    if "【AI 建议】" in text:
        return "AI 建议（待确认）"
    return "已确认"


def build_provenance(data: dict, bp_dir: Path) -> list[dict]:
    """构建决策溯源表：关键决策 ↔ 来源格 ↔ 类型（用户拍板 / AI 建议 / 已确认）。

    轻量启发式：从各格已提取的 highlights 取关键决策值；
    类型由该格残留标注（【需用户拍板】/【草稿，待确认】）判定。
    """
    source_blocks = {
        "B01": ["结论", "非目标"],
        "B03": ["判断", "依据"],
        "B06": ["决策 1", "决策 2", "决策 3", "输出目录", "命名", "格式", "错误输出"],
        "B05": ["方法", "边界"],
        "B07": ["目标", "实施步骤"],
    }
    provenance: list[dict] = []
    for bid, keys in source_blocks.items():
        text = read_text(bp_dir / BLOCK_FILES[bid])
        status = block_marker_status(text)
        hl = data["blocks"].get(bid, {}).get("highlights", {})
        for k in keys:
            val = hl.get(k, "").strip()
            if val and "______" not in val:
                provenance.append({
                    "decision": k,
                    "value": val,
                    "source_block": bid,
                    "type": status,
                })
    return provenance


def load_blueprint(bp_dir: Path) -> dict:
    index_text = read_text(bp_dir / "index.md")
    fm = parse_frontmatter(index_text)
    cp = parse_checkpoint(index_text)

    blocks = {}
    for bid, fname in BLOCK_FILES.items():
        text = read_text(bp_dir / fname)
        blocks[bid] = summarize_block(bid, text)

    # 关键决策汇总
    decisions = {}
    for bid in ("B01", "B03", "B06"):
        if bid in blocks:
            decisions.update(blocks[bid]["highlights"])

    # 输出文件约定
    out_contract = {
        "输出目录": blocks.get("B06", {}).get("highlights", {}).get("输出目录", "未声明"),
        "命名": blocks.get("B06", {}).get("highlights", {}).get("命名", "未声明"),
        "格式": blocks.get("B06", {}).get("highlights", {}).get("格式", "未声明"),
        "错误输出": blocks.get("B06", {}).get("highlights", {}).get("错误输出", "未声明"),
    }
    # 若 B05 没声明涉及文件产出，则标记为 N/A
    # ⚠️ 不能写「"否" in b05_output」：B05 输出字段常含「是否需报告·日志」，
    # 其中「否」字会误触发，把正常有产出的 skill 判成无文件产出（P0 误判，已修）。
    b05_output = blocks.get("B05", {}).get("highlights", {}).get("输出", "")
    if not any(k in b05_output for k in ("文件", "file", "产出", "落盘", "写")):
        out_contract = {k: "N/A（未声明文件产出）" for k in out_contract}

    data = {
        "name": fm.get("title", cp.get("当前格", "未命名")),
        "platform": fm.get("platform", cp.get("平台", "未知")),
        "entry": fm.get("entry", cp.get("入口", "未知")),
        "channel": fm.get("channel", cp.get("通道", "未知")),
        "description_draft": fm.get("description", "<待补充 description>"),
        "status": fm.get("status", cp.get("当前格", "草稿")),
        "created": fm.get("created", date.today().isoformat()),
        "blocks": blocks,
        "decisions": decisions,
        "output_contract": out_contract,
        "test_strategy": blocks.get("B08", {}).get("highlights", {}),
        "checkpoint": cp,
    }
    data["provenance"] = build_provenance(data, bp_dir)
    return data


def render_gaps_md(gaps: dict) -> str:
    """把「带缺口导出」的遗留缺口渲染成 markdown 章节。

    没有缺口时返回空串，不污染产物。
    """
    if not gaps or not gaps.get("blocks"):
        return ""
    rows = []
    for b in gaps["blocks"]:
        miss = "；".join(
            [f"未勾：{', '.join(b['unchecked'])}" if b.get("unchecked") else "",
             f"未填：{', '.join(b['blanks'])}" if b.get("blanks") else "",
             b.get("note", "")]
        ).strip("；")
        rows.append(f"| {b['block']} | {b['file']} | {miss or '—'} |")
    return f"""

## ⚠️ 遗留缺口（带缺口导出）

本蓝图以 IQS **{gaps.get('iqs', '—')}/100** 导出，以下格子尚未收口。
其中 B08 类缺口属**运行期实证项**，需 skill 落地后真跑才能勾——不是遗漏，是时机未到。

| 格 | 文件 | 缺什么 |
|----|------|--------|
{chr(10).join(rows)}

- 下一步：{gaps.get('next_action', '—')}
- 缺口补齐后重跑 `sd_cli export <蓝图目录>` 即可覆盖本产物。
"""


def build_glossary_md() -> str:
    """术语白话附录（--glossary）：给读蓝图的下游（skill-creator 用户）零门槛对照。"""
    rows = "\n".join(f"| {term} | {plain} |" for term, plain in GLOSSARY)
    return f"""
## 术语白话附录（--glossary）

> 本蓝图涉及的专业术语一页对照；随问随答之外的首选自查表。口径与 blueprint-methodology §十 一致。

| 术语 | 白话解释 |
|------|----------|
{rows}
"""


def build_summary_md(data: dict, bp_dir: Path, gaps: dict | None = None,
                     glossary: bool = False) -> str:
    blocks = data["blocks"]
    oc = data["output_contract"]
    today = date.today().isoformat()

    b01_conclusion = blocks.get("B01", {}).get("highlights", {}).get("结论", "未提取")
    b02_profile = blocks.get("B02", {}).get("highlights", {})
    b03_mode = blocks.get("B03", {}).get("highlights", {}).get("判断", "未提取")
    b05_io = blocks.get("B05", {}).get("highlights", {})
    b09 = blocks.get("B09", {}).get("highlights", {})

    oc_rows = "\n".join(f"| {k} | {v} |" for k, v in oc.items())

    def _one_liner(b: dict) -> str:
        if b["highlights"]:
            return next(iter(b["highlights"].values()))
        if b["raw_summary"]:
            return b["raw_summary"].splitlines()[0]
        return "—"

    blocks_rows = "\n".join(
        f"| {bid} | {_one_liner(b)} |"
        for bid, b in blocks.items()
    )

    prov_rows = "\n".join(
        f"| {p['decision']} | {p['value']} | {p['source_block']} | {p['type']} |"
        for p in data.get("provenance", [])
    )
    prov_section = f"""
## 决策溯源表（每个关键决策能找到来源）

> "每个功能都能找到来源，每条规则都能解释为什么存在。" 关键决策 ↔ 来源格 ↔ 类型（用户拍板 / AI 建议 / 已确认）。

| 关键决策 | 取值 | 来源格 | 类型 |
|----------|------|--------|------|
{prov_rows}
""" if prov_rows else ""

    return f"""# {data['name']} — 蓝图交接小结

> 生成时间：{today} ｜ 来源蓝图：`{bp_dir}` ｜ 状态：{data['status']}

## 一句话定位

{data['description_draft']}

## 关键决策

| 维度 | 内容 |
|------|------|
| 平台 / 入口 / 通道 | {data['platform']} / {data['entry']} / {data['channel']} |
| B01 结论 | {b01_conclusion} |
| B03 设计模式 | {b03_mode} |
| 用户画像 | {b02_profile.get('主体', '—')} |
| 使用场景 | {b02_profile.get('动作', '—')}，{b02_profile.get('客体', '—')} |
{prov_section}
## 输入 / 输出契约

| 项 | 内容 |
|------|------|
| 输入 | {b05_io.get('输入', '—')} |
| 输出 | {b05_io.get('输出', '—')} |
| 方法 | {b05_io.get('方法', '—')} |
| 风险 | {b05_io.get('风险', '—')} |

## 输出文件约定

| 要素 | 内容 |
|------|------|
{oc_rows}

## 验收标准（B09 设计期自评）

- 内部质量分：{b09.get('内部质量分', '—')}
- 外部价值分：{b09.get('外部价值分', '—')}
- 综合评分：{b09.get('综合评分', '—')}
- 指向改进项：{b09.get('指向的改进项', '—')}

## 验证策略

{chr(10).join(f"- **{k}**：{v}" for k, v in data['test_strategy'].items()) or "- 未声明"}

## 回滚约定

- 蓝图是唯一事实源。若创建类 skill 产出偏离蓝图（设计模式、输出约定、触发词/name），回蓝图对照修正，不默许漂移。
- 用户不满意 → 回对应格修订蓝图 → 重新落地，形成“蓝图 ↔ 落地”闭环。

## 各格一句话摘要

| 格 | 核心结论 |
|----|----------|
{blocks_rows}

## 交付给创建类 skill 的下一步

1. 保持蓝图中的设计模式与输出文件约定；
2. 触发词 / name 以蓝图为准（已用户确认）；
3. 生成 SKILL.md 与目录骨架后，跑 `scripts/validate_skill.py` 静态检查；
4. 进入 test-playbook 触发测试 + 效果测试闭环打磨。
{render_gaps_md(gaps or {})}{build_glossary_md() if glossary else ''}"""


def build_brief_json(data: dict, gaps: dict | None = None,
                     glossary: bool = False) -> dict:
    """返回可直接序列化为 brief.json 的字典。"""
    out = {
        "schema_version": "2.5.0",
        "generated_at": date.today().isoformat(),
        "blueprint": {
            "name": data["name"],
            "platform": data["platform"],
            "entry": data["entry"],
            "channel": data["channel"],
            "status": data["status"],
            "created": data["created"],
        },
        "description_draft": data["description_draft"],
        "blocks_summary": {
            bid: {
                "file": b["file"],
                "highlights": b["highlights"],
            }
            for bid, b in data["blocks"].items()
        },
        "key_decisions": data["decisions"],
        "output_file_contract": data["output_contract"],
        "test_strategy": data["test_strategy"],
        "provenance": data.get("provenance", []),
        "handoff_notes": [
            "保持蓝图中的设计模式与输出文件约定",
            "触发词 / name 以蓝图为准（已用户确认）",
            "生成后跑 validate_skill.py 静态检查",
            "进入 test-playbook 触发测试 + 效果测试闭环",
        ],
    }
    if gaps:
        out["gaps"] = gaps
        out["handoff_notes"].append(
            f"带缺口导出（IQS {gaps.get('iqs', '—')}）：遗留 {len(gaps.get('blocks', []))} 格缺口，"
            f"见 gaps 字段，落地后补齐"
        )
    if glossary:
        out["glossary"] = [{"term": t, "plain": p} for t, p in GLOSSARY]
    return out


def build_sketch_md(data: dict, glossary: bool = False) -> str:
    """精简版需求规格书，给 skill-creator / builder 直接消费。"""
    blocks = data["blocks"]
    b01 = blocks.get("B01", {}).get("highlights", {})
    b02 = blocks.get("B02", {}).get("highlights", {})
    b03 = blocks.get("B03", {}).get("highlights", {})
    b05 = blocks.get("B05", {}).get("highlights", {})
    b06 = blocks.get("B06", {}).get("highlights", {})
    b07 = blocks.get("B07", {}).get("highlights", {})
    b08 = blocks.get("B08", {}).get("highlights", {})
    b09 = blocks.get("B09", {}).get("highlights", {})

    oc = data["output_contract"]
    oc_text = "\n".join(f"- {k}：{v}" for k, v in oc.items())

    prov_short = "\n".join(
        f"- {p['source_block']} {p['decision']}：{p['value'][:60]}（{p['type']}）"
        for p in data.get("provenance", [])
    ) or "- 未提取到关键决策"

    return f"""# SKETCH — {data['name']}

> 本文件由 skill-designer 蓝图自动生成，是交给创建类 skill 的精简需求规格书。
> 请勿修改触发词与 name（已由用户确认）；严格保持设计模式与输出文件约定。

## 0. 元数据

- **平台 / 入口 / 通道**：{data['platform']} / {data['entry']} / {data['channel']}
- **状态**：{data['status']}
- **生成日期**：{date.today().isoformat()}

## 1. 定位

{data['description_draft']}

## 2. 用户与场景

- **用户**：{b02.get('主体', '—')}
- **场景**：{b02.get('动作', '—')}，{b02.get('客体', '—')}
- **不做的事**：{b01.get('非目标', '—')}

## 3. 设计模式

{b03.get('判断', '—')}

依据：{b03.get('依据', '—')}

## 4. 输入 / 输出契约

- **输入**：{b05.get('输入', '—')}
- **输出**：{b05.get('输出', '—')}
- **方法**：{b05.get('方法', '—')}
- **边界**：{b05.get('边界', '—')}
- **风险**：{b05.get('风险', '—')}

## 5. 输出文件约定

{oc_text}

## 6. 目录骨架

{b07.get('目录骨架', '—')}

实施步骤：{b07.get('实施步骤', '—')}

## 7. 验收

- 内部质量分：{b09.get('内部质量分', '—')}
- 外部价值分：{b09.get('外部价值分', '—')}
- 综合评分：{b09.get('综合评分', '—')}
- 改进项：{b09.get('指向的改进项', '—')}

## 8. 验证策略

- 验证场景：{b08.get('验证场景', '—')}
- 有/无对比：{b08.get('有 / 无对比', '—')}
- 触发测试：{b08.get('触发测试', '—')}
- 效果测试：{b08.get('效果测试', '—')}

## 决策溯源

> 每个关键决策能找到来源（来源格 + 类型）。

{prov_short}

## 9. 回滚与事实源约定

- 蓝图是唯一事实源。创建 skill 产出若偏离本 SKETCH，回蓝图修正。
- 用户不满意 → 回对应格修订 → 重新落地。
{build_glossary_md() if glossary else ''}"""


# ─── L4 十格积木卡片（block-cards.svg）───
# 每格一张卡：格号 / 名称 / 决定什么 / 产物落点 / 最多 2 条要点摘录。
# 四段配色与 SKILL.md 拼装图同构：①想清楚(蓝) ②定下来(紫) ③画出来(绿) ④验一遍(橙)。
BLOCK_CARDS_META = {
    "B01": ("条件", "该不该做", "#2f6fb5"),
    "B02": ("事实", "给谁用、在哪儿用", "#2f6fb5"),
    "B03": ("观点", "做成什么样", "#7a4fb5"),
    "B04": ("问题", "口径谁定、缺信息怎么办", "#7a4fb5"),
    "B05": ("分析", "输入输出与出错代价", "#2f7a5b"),
    "B06": ("决策", "拆合、脚本边界与文件落点", "#2f7a5b"),
    "B07": ("计划", "目录怎么搭", "#2f7a5b"),
    "B08": ("行动", "拿什么证明它行", "#c07a12"),
    "B09": ("结果", "过不过质量门", "#c07a12"),
    "B10": ("复盘", "下一轮怎么变得更好", "#c07a12"),
}


def _xml_escape(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def _clip(s: str, n: int = 30) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def build_block_cards_svg(data: dict) -> str:
    """生成十格积木卡片 SVG 拼版（2 列 × 5 行，白底浅色卡片，可直接贴 SkillHub 介绍页）。"""
    bp_name = _xml_escape(str(data.get("name", "技能蓝图")))
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="700" height="760" '
        'viewBox="0 0 700 760" font-family="PingFang SC, Microsoft YaHei, sans-serif">',
        '<rect width="700" height="760" fill="#f6f7f9"/>',
        f'<text x="24" y="36" font-size="19" font-weight="700" fill="#1c2430">'
        f'🧩 十格积木卡片 · {bp_name}</text>',
        '<text x="24" y="56" font-size="12" fill="#7b8794">'
        '一条链 · 十块积木 · 四段拼装（每格一张卡：决定什么 → 产物落点）</text>',
    ]
    for i, bid in enumerate(BLOCK_FILES):
        name, decide, color = BLOCK_CARDS_META[bid]
        col, row = i % 2, i // 2
        x, y = 20 + col * 336, 72 + row * 134
        blk = (data.get("blocks") or {}).get(bid, {})
        hl = [v for v in (blk.get("highlights") or {}).values() if v and v != "N/A（未声明文件产出）"][:2]
        parts.append(f'<rect x="{x}" y="{y}" width="324" height="122" rx="10" fill="#ffffff" '
                     f'stroke="#e3e7ec"/>')
        parts.append(f'<rect x="{x}" y="{y}" width="6" height="122" rx="3" fill="{color}"/>')
        parts.append(f'<text x="{x + 18}" y="{y + 26}" font-size="14" font-weight="700" fill="#1c2430">'
                     f'{bid} · {_xml_escape(name)}</text>')
        parts.append(f'<text x="{x + 84}" y="{y + 26}" font-size="12" fill="{color}">'
                     f'决定：{_xml_escape(decide)}</text>')
        parts.append(f'<text x="{x + 18}" y="{y + 46}" font-size="11" fill="#7b8794">'
                     f'产物：{_xml_escape(BLOCK_FILES[bid])}</text>')
        if hl:
            for j, line in enumerate(hl):
                parts.append(f'<text x="{x + 18}" y="{y + 68 + j * 20}" font-size="11.5" fill="#4a5568">'
                             f'· {_xml_escape(_clip(str(line), 34))}</text>')
        else:
            parts.append(f'<text x="{x + 18}" y="{y + 68}" font-size="11.5" fill="#a8b2bd">（待填写）</text>')
    parts.append(
        '<text x="24" y="748" font-size="11" fill="#7b8794">'
        'Generated by skill-designer export_brief --block-cards · 蓝图是唯一事实源</text>')
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> int:
    ap = argparse.ArgumentParser(description="蓝图交接产物生成器（skill-designer）")
    ap.add_argument("blueprint", help="已完成 check_blueprint.py 的蓝图目录")
    ap.add_argument("--output", "-o", help="产物输出目录（默认：蓝图目录下的 brief/）")
    ap.add_argument("--format", choices=("all", "md", "json", "sketch"), default="all",
                    help="产物格式（默认 all）")
    ap.add_argument("--stdout", action="store_true", help="仅 --format json 时生效，直接输出 JSON 到 stdout")
    ap.add_argument("--allow-gap", action="store_true",
                    help="允许带缺口导出：IQS ≥ --min-iqs 时放行，剩余缺口写进产物的「遗留缺口」章节。"
                         "B08「真实场景跑过 / 有无对比」必须等 skill 落地后才填得出，"
                         "硬等 10/10 会让④施工蓝图在设计期永远导不出来。")
    ap.add_argument("--min-iqs", type=int, default=90,
                    help="--allow-gap 的放行阈值（默认 90；低于此值仍拒绝导出）")
    ap.add_argument("--glossary", action="store_true",
                    help="在产物中附「术语白话附录」（12 个核心术语一句大白话），"
                         "让读蓝图/brief 的下游用户同样零门槛对照")
    ap.add_argument("--block-cards", action="store_true",
                    help="额外产出 block-cards.svg：十格积木卡片拼版图（每格：格名 / 决定什么 / 产物 / 要点），"
                         "B10 复盘或给用户汇报蓝图全貌时用")
    args = ap.parse_args()

    bp_dir = Path(args.blueprint).resolve()
    if not bp_dir.is_dir() or not (bp_dir / "index.md").exists():
        print(f"[export_brief] 错误：不是有效蓝图目录（缺 index.md）：{bp_dir}", file=sys.stderr)
        return 1

    python = sys.executable
    ok, check_data = run_check(bp_dir, python)
    gaps: dict = {}
    if not ok:
        iqs = (check_data.get("iqs") or {}).get("score", 0)
        if not (args.allow_gap and iqs >= args.min_iqs):
            # F1（v3.19.0）：拒绝时**必须回显真正的拦截原因**。
            # 旧写法 `error or next_action` 有个致命盲区：C7/C8 属 warnings（不是 errors），
            # 此时 error 为空 → 落到 next_action。而 next_action 只在**十格全完成**时才会是
            # 「全部 10 格已完成——跑…进入交接落地」——也就是说，**恰好在这种被警告拦住的场合，
            # 用户看到的是一句鼓励语**，真实原因一次都没出现。既误导人，也埋下「绕过门禁」的动机。
            # 新序：error → warnings（警告未清即视为未通过）→ 才轮到 next_action。
            hint = ""
            if iqs >= args.min_iqs:
                hint = f"（IQS 已达 {iqs}，加 --allow-gap 可带缺口导出）"
            elif args.allow_gap:
                hint = f"（IQS {iqs} < 阈值 {args.min_iqs}，缺口太多，先补再导出）"
            warns = [str(w) for w in (check_data.get("warnings") or [])]
            hard = check_data.get("error")
            if hard or warns:
                listed = ([str(hard)] if hard else []) + warns
                kind = "错误" if hard else "警告"
                print(f"[export_brief] 蓝图未通过检查，无法导出交接产物："
                      f"拦下它的是{kind} {len(listed)} 项{hint}", file=sys.stderr)
                for item in listed:
                    print(f"    · {item}", file=sys.stderr)
                print("[export_brief] 先消掉上面这些再导出——警告未清即不交接，退出码语义不降级。",
                      file=sys.stderr)
            else:
                msg = check_data.get("next_action") or "蓝图完整性检查未通过"
                print(f"[export_brief] 蓝图未通过检查，无法导出交接产物：{msg}{hint}", file=sys.stderr)
            if not args.stdout:
                print(json.dumps(check_data, ensure_ascii=False, indent=2), file=sys.stderr)
            return 1
        gaps = {
            "iqs": iqs,
            "next_action": check_data.get("next_action", ""),
            "blocks": [
                {"block": b.get("block"), "file": b.get("file"), "note": b.get("iqs_note", ""),
                 "unchecked": b.get("unchecked", []), "blanks": b.get("blanks", [])}
                for b in (check_data.get("blocks") or [])
                if b.get("iqs_score", 10) < 10
            ],
        }
        print(f"[export_brief] ⚠️ 带缺口导出（--allow-gap）：IQS {iqs}/100，"
              f"遗留 {len(gaps['blocks'])} 格缺口，已写入产物「遗留缺口」章节。", file=sys.stderr)

    data = load_blueprint(bp_dir)

    if args.stdout and args.format == "json":
        print(json.dumps(build_brief_json(data, gaps, args.glossary), ensure_ascii=False, indent=2))
        return 0

    out_dir = Path(args.output).resolve() if args.output else bp_dir / "brief"
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[str] = []
    if args.format in ("all", "md"):
        md_path = out_dir / "summary.md"
        md_path.write_text(build_summary_md(data, bp_dir, gaps, args.glossary), encoding="utf-8")
        written.append(str(md_path))
    if args.format in ("all", "json"):
        json_path = out_dir / "brief.json"
        json_path.write_text(json.dumps(build_brief_json(data, gaps, args.glossary), ensure_ascii=False, indent=2), encoding="utf-8")
        written.append(str(json_path))
    if args.format in ("all", "sketch"):
        sketch_path = out_dir / "SKETCH.md"
        sketch_path.write_text(build_sketch_md(data, args.glossary), encoding="utf-8")
        written.append(str(sketch_path))
    if args.block_cards:
        cards_path = out_dir / "block-cards.svg"
        cards_path.write_text(build_block_cards_svg(data), encoding="utf-8")
        written.append(str(cards_path))

    print(f"[export_brief] 已生成 {len(written)} 个交接产物（格式={args.format}）：")
    for p in written:
        print(f"  - {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
