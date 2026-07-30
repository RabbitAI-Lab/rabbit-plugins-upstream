# AHKB-CPS v0.1.0 — 阿色全息知识库建产系统

> Arthur's Holographic Knowledge Base Construction & Production System

**AHKB-CPS** 是一套基于大模型的本地知识库建产系统。将任意文档构建为全息知识库，再消费为幻灯片、文章、全息脑图等多种产出。由【大系统观开放论坛】提供，MIT 开源。

---

## 🧭 系统架构

```
文档 → [知识库构建] → 知识库 → [智能路由] → 幻灯片 / 文章 / 全息脑图
        kb模块                   guide模块       ppt     write    mm
```

**一个入口，五大模块：**

| 模块 | 功能 | 说明 |
|------|------|------|
| 🧭 **技能向导** | 统一入口，意图理解，智能路由 | 不确定时先问我 |
| 📦 **知识库构建** | 扫描文档、提取知识元、建立链接、生成地图 | 支持 pptx/docx/xlsx/pdf/md/html/txt |
| ✍️ **文章生成** | 10种输出格式（Word/PDF/Markdown/HTML/Excel/公众号等） | KB驱动 / 基于文档 / 独立创作 |
| 📊 **幻灯片生成** | 36主题 × 15模板 × 31布局 × 48动画，HTML自包含 | KB驱动 / 文档转换 / 独立创作 |
| 🧠 **全息脑图生成** | 按大系统观原理生成升维全息思维导图 | KB驱动 / 基于文档 / 独立创作 |

## 🚀 快速开始

**Claude Code 用户：**
```bash
npx skills add https://github.com/arthurqwang/ahkb-cps
# 在 Claude Code 中调用：
# /ahkb-cps   — 统一入口，一个命令搞定所有！
```

**WorkBuddy 用户：**
将技能包放置在 `~/.workbuddy/skills/ahkb-cps/` 目录下，WorkBuddy 会自动识别并加载。
或通过 WorkBuddy 技能市场搜索 `AHKB-CPS` 一键安装。

直接说"帮我"进入技能向导，或者说"写文章"/"做PPT"/"画脑图"/"入库"直达对应模块。

## 📖 使用建议

1. 先说"帮我"进入技能向导，了解系统能力
2. 用「知识库构建」构建知识库与知识地图
3. 用「文章生成」生成各种格式的文档
4. 用「幻灯片生成」生成幻灯片
5. 用「全息脑图生成」生成阿色全息脑图

> ⚠️ **重要提醒**：工作空间/Vault 必须是您的知识库目录（如 Obsidian Vault），**永远不要将本 Skill 的安装目录作为工作空间**。

## 🎯 核心特性

- **全本地运行** — 知识库存储于本地 Obsidian Vault，数据完全自主可控
- **格式全覆盖** — Word、PPT、PDF、Markdown、HTML、Excel、TXT、公众号、小红书、论文等
- **自创算法·大量节省 Tokens** — 全工作流采用自创算法，大幅节省 Token 消耗；惰性环境检测，全对话只检测一次
- **知识库驱动** — 从文档入库到知识消费，全链路AI辅助
- **自包含交付** — 幻灯片/文章/脑图均为独立文件，可直接拷贝、发送
- **智能路由** — 自然语言理解意图，自动加载对应模块
- **统一体验** — 一个入口，5大模块，无缝切换
- **版本自检** — 启动时自动比对 GitHub 最新版本

## 🏗 系统版本

> 🔖 AHKB-CPS v0.1.0

## 📂 项目结构

```
ahkb-cps/
├── SKILL.md                   统一入口（路由+菜单+环境检测）
├── README.md                  本文件
├── LICENSE                    MIT 许可证
├── core/
│   └── kb2slides.py           共享知识库检索脚本
├── guide/                     技能向导模块
│   ├── guide.md               向导工作流
│   └── scripts/                知识库检索引擎
├── kb/                        知识库构建模块
│   ├── kb.md                  构建工作流
│   └── scripts/                文档扫描、提取、关联等
├── write/                     文章生成模块
│   ├── write.md               文章生成工作流
│   └── scripts/                md2docx 转换工具
├── ppt/                       幻灯片生成模块
│   ├── ppt.md                 幻灯片生成工作流
│   ├── scripts/                build-ppt.py 等
│   ├── templates/              master.html + 36主题 + 15模板
│   └── references/             主题/布局/动画参考文档
└── mm/                        全息脑图生成模块
    ├── mm.md                  脑图生成工作流
    ├── ahmm.html              脑图渲染引擎
    └── ahmm_launcher.html     启动器
```

## 📄 License

MIT © 2026 王权（Arthur Q. Wang，阿色树新风，Arthur Tree New Bee）
> 幻灯片生成组件基于 lewis 的 MIT 许可成果开发（github.com/lewislulu/html-ppt-skill），特此致谢。

---

> 🌐 www.holomind.com.cn · [github.com/arthurqwang/ahkb-cps](https://github.com/arthurqwang/ahkb-cps)

---

# AHKB-CPS v0.1.0 — Arthur's Holographic Knowledge Base Construction & Production System

> AHKB-CPS · powered by the Open Forum of Big Systems View (OFBSV)

**AHKB-CPS** is a local, LLM-powered knowledge base construction and production system. Turn any document into a holographic knowledge base, then consume it as presentations, articles, holographic mind maps, and more. Provided by the Open Forum of Big Systems View (OFBSV). MIT licensed.

---

## 🧭 System Architecture

```
Documents → [KB Builder] → Knowledge Base → [Guide] → Slides / Articles / Mind Maps
              kb module                   guide module   ppt     write     mm
```

**One entry, five modules:**

| Module | Function | Description |
|--------|----------|-------------|
| 🧭 **Skill Guide** | Unified entry, intent routing | Start here if unsure |
| 📦 **KB Builder** | Scan docs, extract knowledge units, build links & maps | 7 formats supported |
| ✍️ **Article Writer** | 10 output formats (Word/PDF/MD/HTML/Excel/etc.) | KB-driven / doc-based / standalone |
| 📊 **Slide Studio** | 36 themes × 15 templates × 31 layouts × 48 animations | KB-driven / convert / standalone |
| 🧠 **Mind Map Generator** | Holographic mind maps based on BSV principles | KB-driven / doc-based / standalone |

## 🚀 Quick Start

**Claude Code users:**
```bash
npx skills add https://github.com/arthurqwang/ahkb-cps
# In Claude Code:
# /ahkb-cps   — one command for everything!
```

**WorkBuddy users:**
Place the skill package in `~/.workbuddy/skills/ahkb-cps/` and WorkBuddy will auto-detect and load it.
Or search `AHKB-CPS` in the WorkBuddy Skill Marketplace for one-click installation.

Just say "help" for the guide, or "write article" / "make PPT" / "mind map" / "import docs" to jump directly.

## 📖 Recommended Workflow

1. Say "help" to enter the skill guide
2. Use KB Builder to construct your knowledge base
3. Use Article Writer to generate documents
4. Use Slide Studio to create presentations
5. Use Mind Map Generator for holographic mind maps

## 🎯 Key Features

- **Fully Local** — Knowledge base stored in your local Obsidian Vault
- **Format Coverage** — Word, PDF, Markdown, HTML, Excel, WeChat, Xiaohongshu, papers
- **KB-Driven** — End-to-end AI assistance from ingestion to production
- **Self-Contained** — Slides, articles, mind maps are standalone files
- **Smart Routing** — Natural language intent recognition, auto module loading
- **Unified Experience** — One entry, 5 modules, seamless switching
- **Version Auto-Check** — Compares against GitHub latest release

## 🏗 System Version

> 🔖 AHKB-CPS v0.1.0

## 📂 Project Structure

```
ahkb-cps/
├── SKILL.md                   Unified entry (routing + menu + env detection)
├── README.md                  This file
├── LICENSE                    MIT License
├── core/
│   └── kb2slides.py           Shared KB search script
├── guide/                     Skill Guide module
├── kb/                        KB Builder module
├── write/                     Article Writer module
├── ppt/                       Slide Studio module
└── mm/                        Mind Map Generator module
```

## 📄 License

MIT © 2026 Arthur Q. Wang (WANG Quan)
> The slide-generation component is built upon MIT-licensed work by lewis (github.com/lewislulu/html-ppt-skill).

---

> 🌐 www.holomind.com.cn · [github.com/arthurqwang/ahkb-cps](https://github.com/arthurqwang/ahkb-cps)
