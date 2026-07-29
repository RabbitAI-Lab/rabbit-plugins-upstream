---
name: "report-builder"
description: "高管汇报内容工厂 V2.0 — 输入详案→提炼为决策导向的高管报告。BLUF一页纸+So What叙事+脚本化工具链(init/bump/validate/density)。"
author: claude-learning-project 📚
metadata:
  openclaw:
    cacheBoundary: on-demand
    emoji: "📋"
    requires:
      bins: [python3]
      env: []
      config: []
    dependencies:
      - markdown-to-html
  pattern: "Executive Report Builder"
  output-format: "md + html"
  upstream: solution-architect, digital-research
  downstream: markdown-to-html
triggers:
  - "高管汇报"
  - "executive briefing"
  - "executive summary"
  - "一页纸"
  - "one-pager"
  - "board report"
  - "决策摘要"
  - "向领导汇报"
  - "管理层报告"
  - "report builder"
  - "简报"
---

# Report Builder — 高管汇报内容工厂 V2.0

**定位：** 输入详细方案/参考资料 → 提炼→分层→转译→叙事→校验 → 输出面向高层的决策导向报告。

**核心差异化：** 业界唯一有自动化脚本链的高管报告 SKILL。竞品（Anthropic Executive Briefing 等）全是纯 Prompt 驱动，我们是 Prompt + 脚本 + 模板 + 校验四层体系。

---

## 5 步处理流水线

```
输入详案（md/doc/pdf）
    │
    ▼
[Step 1] 信息提取 → 提取结论/数据/决策点，剔除过程描述
    │
    ▼
[Step 2] 分层映射 → 按高管阅读习惯重排：结论→论据→背景（BLUF）
    │
    ▼
[Step 3] 语态转译 → 技术术语→业务影响，段落→要点+表格
    │
    ▼
[Step 4] 叙事构建 → 应用标准模板，一页纸强制产出
    │
    ▼
[Step 5] 质量校验 → 结论清晰度/数据支撑度/行动明确性自动检查
    │
    ▼
  输出：高管报告（md + html）
```

---

## 输出结构（Anthropic BLUF 格式）

```
═══════════════════════════════════════════════════════════
高层汇报：[主题]
日期：[日期] | 呈送：[受众]
═══════════════════════════════════════════════════════════

核心结论（BOTTOM LINE）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[2-3句：必须知道什么 + 需要做什么决策]

关键发现（KEY FINDINGS）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [发现1 — 附数据支撑]  [置信度：HIGH]
• [发现2 — 附数据支撑]  [置信度：MEDIUM]
• [发现3 — 附数据支撑]  [置信度：LOW]

业务影响（IMPLICATIONS）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[So What — 对收入/成本/风险/竞争的具体影响]

建议行动（RECOMMENDED ACTIONS）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
按 预期影响 ÷ 所需投入 排序：
1. [行动] — [负责人] — [时间线]
2. [行动] — [负责人] — [时间线]

需要您决策的事项（DECISION REQUIRED）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[明确列出需要高层拍板的事项]

风险与考量（RISKS & CONSIDERATIONS）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• [风险/考量]
• [不作为的后果]

═══════════════════════════════════════════════════════════
来源：[简要引用] | 联系人：[问题找谁]
═══════════════════════════════════════════════════════════
```

---

## 写作铁律

### ✅ 必须做

| 规则 | 来源 |
|------|------|
| **结论前置**：第一句就给出结论，不铺垫 | Anthropic / zhasty007 |
| **500 词硬上限**：全篇不超过 500 词 | zhasty007 |
| **用数字说话**：能用量化就不用形容词 | Anthropic |
| **建议含 Owner + Timeline**：不说"建议考虑"，说"XX 负责，Q3 前完成" | Anthropic |
| **标注置信度**：每项关键发现标注 HIGH/MEDIUM/LOW | Anthropic |
| **So What 检查**：每段读完能回答"所以呢？" | Recipe-060 |
| **受众先行**：开始前确认"谁读、做什么决策、已有多少上下文" | zhasty007 |

### ❌ 禁止做

| 规则 | 来源 |
|------|------|
| **不发明数字**：源材料没有的数据绝对不编 | zhasty007 |
| **不用被动语态**：不说"被建议"，说"我们建议" | Anthropic |
| **不用术语**：技术概念必须用业务语言翻译 | Anthropic |
| **不要过程描述**：不说"我们分析了 47 个品类"，说"采购成本可降 1200 万" | zhasty007 |
| **不要副词**：significantly/potentially/approximately 除非确有必要，一律删除 | zhasty007 |
| **不堆砌背景**：详细内容放附录，主体只放结论 | Anthropic |

---

## 数据呈现规则

| 规则 | 示例 |
|------|------|
| 数字四舍五入 | "$2.3M" 而非 "$2,347,892" |
| 对比基准 | "同比增长 15%" 而非 "增长 15%" |
| 用 relatable 比较 | "3 倍快" 而非 "200% 提升" |
| 突出 delta | "从 3.8% 升至 4.2%（↑0.4pp）" |

---

## 自动化工具链

| 脚本 | 用途 | 用法 |
|------|------|------|
| `scripts/init.py` | 新建报告脚手架 | `python3 init.py "报告名称" --template executive-summary` |
| `scripts/bump.py` | 版本升级+新文件生成+变更摘要 | `python3 bump.py --major\|--minor\|--patch` |
| `scripts/validate.py` | 内容质量校验（结论/数据/行动/篇幅/置信度） | `python3 validate.py <file> [-o report.json]` |
| `scripts/density.py` | 内容密度分析（段落长度/数据占比/空洞检测） | `python3 density.py <file>` |

---

## 模板体系

| 模板 | 适用场景 | 阅读时长 |
|------|---------|---------|
| `templates/executive-summary.md` | 通用高管摘要（BLUF 格式） | ≤3 分钟 |
| `templates/decision-memo.md` | 决策备忘录（需要拍板的事项） | ≤5 分钟 |
| `templates/one-pager.md` | 一页纸汇报（极简版） | ≤2 分钟 |
| `templates/board-briefing.md` | 董事会汇报 | ≤5 分钟 |

---

## 工作目录约定

```
reports/{报告名称}/
├── README.md                     # 版本索引
├── VERSION.md                    # 版本历史
├── 01-{报告名称}-v1.0.0.md       # 文件名三段式：序号-主题-版本
├── 01-{报告名称}-v1.0.0.html     # 定稿 HTML
├── 01-{报告名称}-v2.0.0.md
├── 01-{报告名称}-v2.0.0.html
└── appendix/                     # 附录（详细数据/方法论/技术细节）
```

---

## 与其他 SKILL 协作

| SKILL | 触发条件 | 协作方式 |
|-------|---------|---------|
| `solution-architect` | 详案来源 | 接收方案文档作为输入 |
| `digital-research` | 需要行业数据 | 委托调研，结果注入报告 |
| `markdown-to-html` | 报告定稿 | 输出 HTML 版本 |
| `plantuml-generator` | 需要架构图 | 生成图表嵌入报告 |

> 详见 `references/collaboration-workflow.md`

---

## 📂 参考文档索引

| 文档 | 内容 |
|------|------|
| `references/style-guide.md` | 高管语态手册（中英文写作规范） |
| `references/narrative-methodology.md` | 叙事方法论（BLUF/金字塔/So What框架） |
| `references/structure-validation.md` | 校验规则详解与 JSON 输出格式 |
| `references/edge-cases.md` | 边界情况处理策略 |
| `references/collaboration-workflow.md` | 与其他 SKILL 的协作流程 |
| `templates/executive-summary.md` | 通用高管摘要模板 |
| `templates/decision-memo.md` | 决策备忘录模板 |
| `templates/one-pager.md` | 一页纸汇报模板 |
| `templates/board-briefing.md` | 董事会汇报模板 |

---

## 约束

- ✅ 任何内容变更 = 升版 + 新文件
- ✅ 默认「注入」模式，旧内容不删不改
- ❌ 禁止覆盖旧版本文件
- ❌ 禁止手动修改版本号（统一通过 `scripts/bump.py`）
- ❌ 禁止 `pip install` / `npm install` / `apt install`
- ❌ 不要把 md→html 转换逻辑放进本 SKILL（用 markdown-to-html）
- ❌ 不要输出超过 500 词的报告主体（附录不计算在内）

---

*V2.0 — 由 claude-learning-project 📚 基于 Anthropic Executive Briefing 框架重构*
