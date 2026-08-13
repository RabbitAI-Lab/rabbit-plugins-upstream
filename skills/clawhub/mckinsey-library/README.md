# mckinsey-library

> 麦肯锡风格咨询交付 Skill（中文名「麦肯锡资料库顾问」）

一个**带方法论内核、带质量闸门、可端到端自主编排**的咨询交付工作流。它把零散的客户材料（文档 / 数据 / 笔记 / 会议记录）结构化成一页页「有结论、有论证、有数据来源」的咨询交付物，并在内部材料不足时**自主搜集外部资料**、在确认后**自主产出 PPT 与演讲稿**。

本 Skill 的方法论不是通用知识，而是直接来自用户提供的 **44 份真实麦肯锡风格资料库**（已全量吸收、逐份落位，并已做脱敏处理）。

## 核心能力

- **四段 + 闸门工作流**：提问锁定 → 外部资料搜集与评估 → 生成故事线 →（确认闸门）→ 生成 PPT + 演讲稿。
- **纪律约束**：客户未确认故事线之前，绝不进入 PPT 生成（麦肯锡「先画鬼图、后写故事、再整理文件」）。
- **外部证据引擎**：内置 WebSearch / WebFetch 搜集策略，以及三角验证、来源分级、口径透明等可信度准则。
- **可视化布局目录**：50+ 布局模式库 + 可解释选型流程 + python-pptx 复用绘图引擎（`assets/pptx_primitives.py`，含 Treemap / 矩阵 / 瀑布 / 漏斗 / 仪表盘等面积类图）。
- **Critic 视觉质量门**：交付前强制逐页巡检（重叠 / 溢出 / 图表 / 对齐 / 字体等 12 项清单）。

## 目录结构

```
mckinsey-library/
├── SKILL.md                      # 工作流总纲与方法论文档
├── assets/
│   ├── pptx_primitives.py        # python-pptx 复用绘图引擎
│   └── __primitives_selftest__.pptx
└── references/                   # 11 份方法论文档（索引 / 守则 / 框架 / 模板等）
    ├── materials_index.md        # 资料路由索引（需求类型 → 对应资料 → 是否已用）
    ├── functional_playbooks.md   # 44 份全量逐份应用账本与主题 playbook
    ├── rulebook.md               # 速查守则（每条标注来源）
    ├── methodology.md            # 框架与方法论细则
    ├── intake_questions.md       # 提问锁定话术与映射表
    ├── storyline_template.md     # 故事线 + 演讲稿模板
    ├── external_research.md      # 外部资料搜集与可信度评估
    ├── strategy_playbook.md      # 战略规划专题 playbook
    ├── visualization_layouts.md  # 50+ 可视化布局模式库
    ├── layout_selection.md       # 布局可解释选型流程
    └── critic_checklist.md       # 视觉质量门巡检清单
```

## 使用方法

1. 将本目录整体放入 WorkBuddy 的技能目录（用户级 `~/.workbuddy/skills/` 或项目级 `.workbuddy/skills/`）。
2. 在对话中描述你的咨询需求，例如「帮我用麦肯锡方法梳理这个故事线并出 PPT」。
3. Skill 会先锁定问题、按需搜集外部资料、产出故事线 md 供你确认，确认后再生成 PPT + 演讲稿三件套。

## 内容与隐私说明

- 本仓库内容已做**脱敏处理**：不包含任何真实姓名、雇主名称或可识别个人身份的信息；资料中涉及的机构名称均已泛化。
- 方法论框架与术语均摘录自公开的麦肯锡风格资料，仅用于方法与交付流程参考。
- 本仓库以 MIT 协议开源，可自由使用、修改与再分发（见 [LICENSE](./LICENSE)）。

## 许可

[MIT](./LICENSE) © 2026 forrestneo
