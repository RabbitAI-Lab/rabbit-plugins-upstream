# 📋 Executive Briefing — 高管汇报内容工厂

[![Version](https://img.shields.io/badge/version-2.0.1-blue)](version.json)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Quality](https://img.shields.io/badge/quality-A%20级-4caf50)](SKILL.md)

> 输入详案 → 提炼 → 分层 → 转译 → 叙事 → 校验 → 输出面向高层的决策导向报告。

**业界唯一有自动化脚本链的高管报告 SKILL。** 竞品（Anthropic Executive Briefing 等）全是纯 Prompt 驱动，我们是 Prompt + 脚本 + 模板 + 校验四层体系。

---

## 🎯 一句话

把几十页的技术方案浓缩成一页纸的决策报告，让领导 30 秒看懂、3 分钟能拍板。

---

## ⚡ 5 步处理流水线

```
输入详案（md/doc/pdf）
    │
    ▼
[1] 信息提取 → 提取结论/数据/决策点，剔除过程描述
    │
    ▼
[2] 分层映射 → 按高管阅读习惯重排：结论→论据→背景（BLUF）
    │
    ▼
[3] 语态转译 → 技术术语→业务影响，段落→要点+表格
    │
    ▼
[4] 叙事构建 → 应用标准模板，一页纸强制产出
    │
    ▼
[5] 质量校验 → 7 项自动检查：BLUF/So What/数据/行动/篇幅/置信度/语态
    │
    ▼
  输出：高管报告（md + html）
```

---

## 📦 安装

**前置要求：** OpenClaw 平台 + Python 3.7+

```bash
# ClawHub 安装
clawhub install executive-briefing

# 或本地安装
git clone https://github.com/dark_night_sky/executive-briefing.git
cp -r executive-briefing ~/.openclaw/skills/report-builder/
```

---

## 🚀 快速开始

```bash
# 1. 初始化报告
python3 scripts/init.py --title "Q3 营收分析" --template executive-summary

# 2. 填充报告内容（基于 SKILL.md 流程）
# 输入你的详案/数据，SKILL 自动走 5 步流水线

# 3. 校验质量
python3 scripts/validate.py --file reports/my-report.md

# 4. 分析密度
python3 scripts/density.py --file reports/my-report.md

# 5. 升版发布
python3 scripts/bump.py --level minor
```

---

## 🛠️ 工具链

| 工具 | 用途 | 命令 |
|------|------|------|
| `init.py` | 一键脚手架：目录+模板+版本文件 | `python3 scripts/init.py --title "xxx"` |
| `validate.py` | 7 项质量校验 → A-D 评级 | `python3 scripts/validate.py --file xxx.md` |
| `density.py` | 内容密度分析：空洞词/数据密度/阅读时长 | `python3 scripts/density.py --file xxx.md` |
| `bump.py` | 语义化版本升级 | `python3 scripts/bump.py --level minor` |

---

## 📊 质量评分

| 等级 | 阈值 | 含义 |
|:----:|------|------|
| **A** | ≥85 | 可直接呈送高层 |
| **B** | 70-84 | 建议修正后使用 |
| **C** | 60-69 | 需大幅修改 |
| **D** | <60 | 不建议使用 |

当前预检评分：**A 级 100 分** ✅

---

## 📁 文件结构

```
report-builder/
├── SKILL.md                  # 核心逻辑（5步流水线+BLUF+铁律）
├── README.md                 # 本文件
├── LICENSE                   # MIT 协议
├── CHANGELOG.md              # 变更日志
├── version.json              # 版本元数据
├── scripts/
│   ├── init.py               # 脚手架
│   ├── validate.py           # 质量校验
│   ├── density.py            # 密度分析
│   └── bump.py               # 版本管理
├── templates/
│   ├── executive-summary.md  # 通用高管摘要
│   ├── decision-memo.md      # 决策备忘录
│   ├── one-pager.md          # 一页纸汇报
│   └── board-briefing.md     # 董事会汇报
├── references/
│   ├── style-guide.md        # 语态手册
│   ├── narrative-methodology.md  # 叙事方法论
│   ├── structure-validation.md   # 校验规则
│   ├── collaboration-workflow.md # 协作流程
│   └── edge-cases.md         # 边界场景
└── tests/
    ├── test_validate.py      # validate 测试
    ├── test_density.py       # density 测试
    ├── test_bump.py          # bump 测试
    └── fixtures/             # 测试数据
```

---

## 🔗 上下游协作

```
solution-architect / digital-research / plantuml-generator
                    ↓ (上游输入)
              report-builder
                    ↓ (输出 md)
           markdown-to-html (下游)
```

---

## 📚 理论基础

- **BLUF (Bottom Line Up Front)**：核心结论前置
- **So What 叙事**：每个数据点必须回答"所以呢？"
- **金字塔原理**：结论→论据→背景
- **30 秒电梯法则**：一句话说清"必须知道什么 + 需要什么决策"
- **基准框架：** [Anthropic Executive Briefing](https://github.com/anthropics/executive-briefing)（2.4k⭐/192 installs）

---

## 🤝 贡献

欢迎提交 Issue 和 PR。请确保通过 `scripts/validate.py` 检查后再提交。

---

## 📄 许可

MIT License — 详见 [LICENSE](LICENSE)

---

**Made with ❤️ by claude-learning-project 📚 | 2026**
