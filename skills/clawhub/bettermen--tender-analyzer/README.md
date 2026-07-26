# Tender Analyzer — 投标文件全流程智能分析技能

> WorkBuddy Skill: 解析招标文件 → MECE多维需求拆解 → 自动生成专业图表 → 模拟评审专家打分 → 逐条自动修订 → 版本管理与迭代追踪

[![Skill Type](https://img.shields.io/badge/Skill-WorkBuddy-2563EB)](https://www.codebuddy.cn)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## 核心能力

| 能力 | 说明 |
|------|------|
| 📄 文档智能解析 | 解析 PDF/DOCX/XLSX 招标文件，提取结构化需求清单 |
| 🧩 MECE多维分析 | 6大维度（技术/商务/资质/管理/合规/实施）×24+子维度，相互独立完全穷尽 |
| 📊 专业图表生成 | 架构图/流程图/ER图/甘特图/雷达图，SVG内嵌HTML |
| 🎯 评审专家模拟 | 5角色（技术/商务/法律/项目管理/质量）独立打分，扣分明细追踪 |
| ✏️ 自动修订引擎 | 4种修订类型（enhance/add/fix/remove），评审意见驱动逐条修改 |
| 📝 版本管理 | Git式版本快照、Diff对比、回滚、版本演化树 |

## 8阶段工作流

```
文档解析 → 需求清单 → MECE展开 → 图表生成 → 评审模拟 → 自动修订 → 版本快照 → 报告生成
```

## 技能结构

```
tender-analyzer/
├── SKILL.md                          # 核心定义（8阶段工作流 + 触发词）
├── scripts/
│   ├── tender_parser.py              # PDF/DOCX/XLSX 解析引擎
│   ├── mece_analyzer.py              # MECE 6维需求展开引擎
│   ├── expert_reviewer.py            # 5角色评审模拟 + 扣分追踪
│   ├── auto_reviser.py               # 评审意见驱动自动修订
│   ├── version_manager.py            # Git式版本管理（快照/Diff/回滚/树）
│   ├── report_builder.py             # 交互式HTML报告组装
│   └── requirements.txt              # 依赖清单
├── references/
│   ├── mece_framework.md             # MECE 6维×24子维度完整定义
│   ├── bid_scoring_standards.md      # 4种评标办法 + 扣分对照表
│   └── bid_terminology.md            # 招投标术语词典（50+术语）
└── assets/
    └── report_template.html          # 完整HTML模板（CSS+JS交互框架）
```

## 快速开始

### 安装为 WorkBuddy 技能

将 `tender-analyzer/` 放置在 `~/.workbuddy/skills/` 目录下，重启 WorkBuddy 即可自动加载。

### 触发词

- "分析这份招标文件"
- "MECE多维拆解"
- "模拟评审打分"
- "生成架构图"
- "根据评审意见修改"
- "保存版本" / "版本对比"

### Python 依赖

```bash
pip install pymupdf python-docx openpyxl pandas numpy
```

### 运行脚本验证

```bash
python scripts/mece_analyzer.py --demo
python scripts/expert_reviewer.py --demo
python scripts/auto_reviser.py --demo
python scripts/version_manager.py
```

## MECE 六大维度

| 维度 | 权重建议 | 二级维度 |
|------|----------|----------|
| 技术 | 25-40% | 方案完整性、先进性、参数符合度、创新性、成熟度 |
| 商务 | 25-40% | 报价合理性、付款条件、质保售后、培训、交付周期 |
| 资质 | 10-20% | 企业资质、人员资质、业绩案例、财务、信誉 |
| 管理 | 10-15% | 组织架构、进度计划、质量管理、风险管理、沟通 |
| 合规 | 10-15% | 实质性条款、知识产权、免责、违约、废标项检测 |
| 实施 | 10-15% | 交付计划、资源配置、验收标准、运维保障、应急预案 |

## 评审专家角色

| 角色 | 权重 | 关注维度 | 评分风格 |
|------|------|----------|----------|
| 技术专家 | 30% | 技术 | 严格 |
| 商务专家 | 25% | 商务 | 性价比 |
| 法律专家 | 20% | 合规 | 风险规避 |
| 项目管理专家 | 15% | 管理+实施 | 可落地性 |
| 质量专家 | 10% | 技术+管理+实施 | 标准合规 |

## License

MIT
