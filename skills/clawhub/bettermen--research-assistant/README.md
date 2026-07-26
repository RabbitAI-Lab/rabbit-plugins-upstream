# 🧪 AI 科研全流程助理 (Research Assistant)

> 覆盖从 idea 到 publication 的科研全生命周期。一个 WorkBuddy 技能，12 大模块，交互式 HTML 可视化报告。

## 🌟 功能概览

| # | 模块 | 核心能力 |
|---|------|---------|
| 🔍 | 文献检索与发现 | 多渠道语义搜索、研究趋势图、引用网络 |
| 📖 | 文献阅读与理解 | 结构化摘要、方法论评分、TL;DR |
| 📝 | 文献综述 | 自动生成综述框架、识别研究空白 |
| 💡 | 研究选题 | 六维创新评估、多方向对比 |
| 🧪 | 研究设计 | 变量定义、实验范式、统计方案 |
| 📊 | 数据分析 | 统计方法推荐、Python/R 代码生成 |
| ✍️ | 论文写作 | IMRaD 结构分节撰写 |
| 🔧 | 润色校对 | 原文 vs 润色版对比、学术风格检查 |
| 📎 | 引用管理 | 7 种格式转换（APA/MLA/IEEE/GB等） |
| 🎯 | 投稿选刊 | 冲-稳-保期刊推荐、Cover Letter |
| 💰 | 基金申请 | 国自然全结构、预算编制 |
| 🎤 | 学术汇报 | PPT 大纲、讲稿、预判 Q&A |

## 🚀 快速使用

在 WorkBuddy 中触发：

```
科研助手，帮我做以下工作：
1. 搜索近3年"大语言模型安全对齐"论文
2. 对核心论文做结构化阅读
3. 生成文献综述并识别研究空白
```

## 🏗️ 技术架构

- **驱动方式**: LLM + WebSearch 纯文本驱动（无外部 API 依赖）
- **输出格式**: 交互式 HTML 报告（Chart.js 可视化，Tab 导航）
- **报告生成**: `scripts/generate_report.py`

## 📂 目录结构

```
research-assistant/
├── SKILL.md                    # 技能定义（12模块完整工作流）
├── README.md
├── scripts/
│   └── generate_report.py      # HTML 报告生成器
└── references/
    ├── search_strategies.md     # 检索策略指南
    ├── academic_terms.md        # 学术术语词典
    ├── citation_styles.md       # 引用格式规范
    └── funding_guide.md         # 基金申请指南
```

## 📄 许可

MIT License

---

Made with ❤️ for researchers by WorkBuddy
