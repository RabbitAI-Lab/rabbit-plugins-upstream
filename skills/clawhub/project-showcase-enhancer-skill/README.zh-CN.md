<p align="center">
  <img src="./images/logo.svg" width="120" alt="个人项目包装与面试备战" />
</p>

<h1 align="center">个人项目包装与面试备战 · Project Showcase Enhancer</h1>

<p align="center">
  <b>把 Demo 级个人项目推演为商用级完整产品，一键生成项目展示文档与面试备考手册。脚本做确定性扫描，大模型做深度语义理解，四阶段闭环从读代码直通面试准备。</b>
</p>

<p align="center">
  🌐 <a href="./README.md">双语版</a> &nbsp;·&nbsp; 🇬🇧 <a href="./README.en.md">English</a>
</p>

<p align="center">
  <img alt="WorkBuddy" src="https://img.shields.io/badge/WorkBuddy-Skill-00b4d8" />
  <img alt="Stages" src="https://img.shields.io/badge/stages-4%20phases-8b5cf6" />
  <img alt="Architecture" src="https://img.shields.io/badge/architecture-hybrid-10b981" />
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen" />
  <img alt="Models" src="https://img.shields.io/badge/models-Opus%204.6%20%7C%20DeepSeek%20v4%20Pro%20%7C%20GPT--5.6-ff6b35" />
</p>

---

## 简介

> 夫良玉韫椟，待良工而后彰其华；宝剑藏匣，遇识者而始显其锋。今之开发者，多能运斤成风，俄顷立一项目；然藏器于身而莫之能言，怀璧在握而难自陈其价。是以码虽精而人未之知，Demo 虽巧而市未之售。善作者不必善述，此古今之通患也。

**个人项目展示增强器（Project Showcase Enhancer）** 正为此患而生：先读懂你的代码与原始意图，再与你共创，把能跑的 Demo 推演成商用级产品方案，最终产出两份可直接使用的文档——**项目展示文档**与**面试备考手册**。融合脚本确定性扫描与 LLM 深度语义理解，打通「分析代码 → 推演商用 → 生成展示文档 → 预测面试题」的全链路。

## 这是什么？

> **个人项目包装与面试备战** 是一个 WorkBuddy 技能（Skill）。它不是「扫一遍代码吐模板」的工具，而是一套**人机协作的工作流**：先读懂你的代码与原始意图，再和你一起把 Demo 推演成商用级产品方案，最后产出两份可直接使用的文档——**项目展示文档**和**面试备考手册**。

它融合了两个不同的源头：

- 源自 **code-project-analyzer** —— 代码扫描与项目文档生成的原始脚本与思路；
- 源自 **JD + 简历 → 面试题预测助手** —— JD + 简历 → 面试题的 STAR 框架与结构化分析方法。

真实痛点：你有一个能跑的个人项目 / Demo，但不知道怎么把它**讲清楚、写专业、准备面试**。代码能跑，项目说明却只会写「基于 React + Node 做的博客」，提炼不出亮点；Demo 离商用差得远却说不清差在哪；面试官一追问技术选型理由就露怯。

这个技能把这三件事一次性解决：**分析代码 → 推演商用 → 生成展示文档 → 预测面试题**。

## 亮点

> **扫描脚本提供确定性地图，大模型在地图上做深度推理——两者结合，才既快又准。** —— 本技能的核心设计

- **真实读懂代码**：先用脚本做确定性扫描，再由大模型阅读关键源文件，理解业务逻辑、模块划分、数据流，而不是靠文件名猜。
- **Demo 到商用的推演**：结合你的产品愿景，列出功能 / 工程化 / 运维三方面的差距，给出分阶段演进路线图（MVP → 完善 → 商用）。
- **项目展示文档**：按模板生成亮点、功能模块、技术栈选型理由、架构设计、部署说明，排版精良，直接可放简历网站或作为 README。
- **面试备考手册**：结合 JD 和简历，预测 15 道项目相关面试题（必问 / 针对性 / 追问三类），每题给考察点、答题策略和 STAR 框架。
- **混合架构**：脚本做快而稳的扫描，大模型做深而准的推理，兼顾速度与质量，也不浪费 token。

## 上手

### 前提

```bash
# 1. 已安装 WorkBuddy 客户端（本技能为 WorkBuddy 用户级技能）
# 2. 建议在「高推理模型」下使用（见「配置」）
#    推荐：Claude Opus 4.6 / DeepSeek v4 Pro / GPT-5.6

# 3.（可选）如需解析简历文件，安装 Python 依赖
pip install pdfplumber python-docx pypdf
```

### 安装技能

```bash
# 方式一：从 GitHub 克隆到用户级技能目录
git clone https://github.com/whishi47/project-showcase-enhancer-skill.git \
  "$HOME/.workbuddy/skills/project-showcase-enhancer"

# 方式二：从压缩包解压
#   下载 project-showcase-enhancer.zip，解压到 $HOME/.workbuddy/skills/project-showcase-enhancer/
#   确保目录下直接包含 SKILL.md

# 方式三：SkillHub 市场安装
#   在 SkillHub 搜索 project-showcase-enhancer-skill 并安装
```

> `$HOME` 在 Windows 上通常是 `C:\Users\你的用户名`。技能目录也可能是 `.codebuddy\skills`，以你使用的客户端为准。安装后无需编译或安装依赖，在 WorkBuddy 对话中直接用自然语言触发即可。

### 使用

| 触发方式 | 操作 | 效果 |
|---|---|---|
| 💬 自然语言 | "分析一下我的项目" | 启动技能，进入阶段 0 收集信息 |
| 💬 自然语言 | "帮我把这个项目推演到商用" | 直接进入阶段 2 商用推演 |
| 💬 自然语言 | "生成一份项目展示文档" | 跳过推演，直接产出展示文档 |
| 💬 自然语言 | "结合我的 JD 准备这个项目的面试" | 进入阶段 4 面试备考 |
| 📎 简历文件 | 上传 PDF / DOCX / TXT | 解析为纯文本，供面试准备阶段使用 |

首次触发时，技能会一次性问你四件事（不用逐条回答）：**项目路径**、**使用场景**（简历 / 面试 / GitHub / 作品集）、**目标岗位方向**（可选）、**特别说明**（你的原始想法、想突出的点）。

## 工作原理

```
┌──────────────────────────────────────────────────────────┐
│             project-showcase-enhancer-skill                      │
│   输入：项目目录 +（可选）JD 文件 + 简历文件                  │
└───────────────────────────┬──────────────────────────────┘
                            ▼
   ┌──────────────────────────────────────────────┐
   │ ① 深度代码理解                                  │
   │   scripts/scan_project.js（字典扫描 → JSON）    │
   │   + 大模型语义阅读关键源文件                     │
   │   → 代码现状画像（含 8 维质量评分）             │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ ② 商用级推演（对话）                           │
   │   愿景澄清 → 差距分析(P0/P1/P2) → 演进路线图    │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ ③ 项目展示文档                                 │
   │   assets/showcase-template.md 填充             │
   │   → {项目}-展示文档.md                         │
   └──────────────────────┬───────────────────────┘
                           ▼
   ┌──────────────────────────────────────────────┐
   │ ④ 面试视角审视                                 │
   │   JD + 简历 → 15 道项目面试题 + STAR           │
   │   → {项目}-面试备考手册.md                     │
   └──────────────────────────────────────────────┘
```

**阶段 ① 深度代码理解**：脚本 `scan_project.js` 秒级输出结构化 JSON（技术栈、依赖、带职责标注的目录树、入口/配置文件、README 原文）；大模型再基于该「地图」阅读关键源文件，分析模块划分、数据流、启动流程、配置里的第三方服务，并从 README 提取产品原始意图；最后对 8 个维度（代码组织、类型安全、安全性、可部署性、错误处理、测试覆盖、性能设计、文档完整度）按 1–10 打分，附文件名 + 行号证据。

**阶段 ② 商用推演对话**：通过对话澄清目标用户、核心卖点、商业模式（可选）、MVP 范围；列出三类差距（功能 / 工程化 / 运维，每项标 P0/P1/P2 优先级）；给出三阶段演进路线图（MVP → 完善 → 商用）。

**阶段 ③ 生成交付物**：读取 `assets/showcase-template.md` 填充亮点、功能模块、技术栈选型理由、架构设计、部署说明；读取 `assets/interview-prep-template.md` 生成 15 道面试题。

**阶段 ④ 面试视角审视**：结合 JD 与简历，预判面试官看到该项目会追问的技术题 / 项目题，每题输出「考察点 → 答题策略 → STAR 框架」。

## 四阶段详解

| 阶段 | 名称 | 输入 | 关键动作 | 产出 |
|---|---|---|---|---|
| ① | 深度代码理解 | 项目目录 | 脚本扫描 + 大模型语义阅读 + 8 维质量评分 | 代码现状画像（JSON + 评分） |
| ② | 商用推演对话 | 现状画像 + 你的愿景 | 差距分析(P0/P1/P2) + 演进路线图 | 演进方案 |
| ③ | 项目展示文档 | 现状 + 演进方案 | 按模板填充亮点 / 模块 / 技术栈 / 架构 | {项目}-展示文档.md |
| ④ | 面试视角审视 | 展示文档 + JD + 简历 | 预测 15 题（必问/针对性/追问）+ STAR | {项目}-面试备考手册.md |

## 配置

技能要求**高推理能力**的大模型。**推荐模型**：

- Claude Opus 4.6
- DeepSeek v4 Pro
- GPT-5.6（或同等级别）

低推理模型仍能用，但会导致：代码理解肤浅、商用推演模板化、面试题预测质量差。技能在阶段 0 会提示你确认当前模型，若不满足建议切换后再用。

> 💡 建议：把常用的高推理模型设为 WorkBuddy 默认，或在触发技能前手动切换，以获得最佳推演与文档质量。

## 为什么不用其他方案？

| 维度 | 本技能 | 纯 code-analyzer | 手写 README | 纯 interview-prep |
|---|---|---|---|---|
| 代码理解 | ✅ 脚本 + 大模型深度 | ⚠️ 仅文件名字典 | ❌ 手动 | ❌ 不涉及 |
| Demo→商用推演 | ✅ 对话共创路线图 | ❌ | ❌ | ❌ |
| 展示文档质量 | ✅ 专人专案、有证据 | ⚠️ 模板化、泛化 | ⚠️ 取决于写作水平 | ❌ |
| 面试预测 | ✅ 紧扣本项目代码 | ❌ | ❌ | ⚠️ 仅通用 JD 题 |
| 混合架构省 token | ✅ | ❌ | — | ❌ |

**本技能的定位**：你不是「替换」code-project-analyzer 或 interview-prep，而是把「读代码 → 推演商用 → 写展示 → 备面试」四步一次性跑通。扫描脚本提供确定性地图，大模型在地图上做深度推理，最终产出两份拿得出手的文档。

## 内置脚本

### `scripts/scan_project.js`

硬编码字典扫描项目，输出结构化 JSON。不调用大模型，速度快、确定性强。

```bash
# 用法
node scripts/scan_project.js <项目目录>

# 示例：分析当前目录
node scripts/scan_project.js ./my-project
```

输出 JSON 字段：

| 字段 | 内容 |
|------|------|
| `techStack` | 按 runtime / framework / build / css / test / orm / deploy 分类的技术栈 |
| `dependencies` | 完整依赖列表 |
| `directoryStructure` | 带职责标注的目录树 |
| `entryFiles` | 检测到的入口文件 |
| `configFiles` | 配置文件清单 |
| `readmeContent` | README 原文（最多 5000 字符） |
| `packageJson` | 项目元信息 |
| `fileStats` | 文件统计 |

### `scripts/parse_file.py`

把简历 PDF / DOCX / TXT 解析为纯文本，供面试准备阶段使用。

```bash
# 用法
python scripts/parse_file.py <简历文件路径>

# 示例
python scripts/parse_file.py ./resume.pdf
```

依赖：`pdfplumber` 或 `pypdf`（PDF）、`python-docx`（DOCX）。未安装时脚本会提示安装命令。

## 开发

```bash
# 克隆项目
git clone https://github.com/whishi47/project-showcase-enhancer-skill.git
cd project-showcase-enhancer-skill

# 仅修改 SKILL.md 与 assets 模板即可调整工作流，无需编译
# 若要调扫描逻辑，编辑 scripts/scan_project.js
# 若要调简历解析，编辑 scripts/parse_file.py
```

技能目录结构：

```
project-showcase-enhancer/
├── SKILL.md                          # 技能主文件（工作流定义）
├── README.md                         # 双语版
├── README.en.md                      # 英文版
├── README.zh-CN.md                   # 本文档（中文版）
├── images/
│   └── logo.svg                      # 文档用 logo
├── scripts/
│   ├── scan_project.js               # 项目扫描器：字典匹配 → JSON
│   └── parse_file.py                 # 简历解析器：PDF/DOCX/TXT → 文本
└── assets/
    ├── showcase-template.md          # 项目展示文档模板
    └── interview-prep-template.md    # 面试备考手册模板
```

## 发布

```bash
# 方式一：SkillHub 网页发布
#   进入 https://skillhub.cn ，上传打包好的 project-showcase-enhancer.zip
#   Slug: project-showcase-enhancer，显示名称：个人项目包装与面试备战

# 方式二：SkillHub CLI 发布
#   登录后执行 skillhub publish ./project-showcase-enhancer-skill

# 重新打包（需 skill-creator 的 package_skill.py）
python package_skill.py ./project-showcase-enhancer-skill ./dist
```

> 发布前记得同步更新 SKILL.md 中的 `version` 字段。

## 协议

MIT © 2026
