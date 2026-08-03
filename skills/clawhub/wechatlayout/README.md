# WeChatLayout

> **约束优于自由** — 微信公众号排版引擎。把 Markdown 文章转换为可直接粘贴进公众号编辑器、粘贴后样式不丢失的 HTML（样式内联 + `<span leaf="">` 包裹）。也从任意公众号文章 URL 提取视觉风格，生成匹配的组件库。

[![Version](https://img.shields.io/badge/Version-v1.1-green.svg)](./SKILL.md#changelog) [![Author](https://img.shields.io/badge/Author-Qomob.AI-blue.svg)](#版权与授权) [![License](https://img.shields.io/badge/License-Commercial_Use_Requires_Authorization-red.svg)](#版权与授权) [![Modes](https://img.shields.io/badge/Modes-A_+_B-orange.svg)](#两种工作模式) [![Themes](https://img.shields.io/badge/Themes-5_+_Custom-9cf.svg)](#主题系统)

---

## 一句话

给它一篇 Markdown，返还一段可直接粘贴到公众号编辑器的 `<section>` HTML 片段——样式不丢失、平台合规、视觉克制。

```
"把这篇 Markdown 排成公众号文章，用翡翠绿主题"
  → 输入归一化 → 选主题 → 读组件库 → 解析结构
    → 装配 HTML → validate_output.py 校验 → 输出
```

---

## 两种工作模式

| 模式 | 触发词 | 产物 |
|------|--------|------|
| **Mode A: 排版** | 公众号排版 / 微信排版 / gzh / 排成公众号 / 粘到公众号 | 纯 `<section>` 正文片段 + 预览页 |
| **Mode B: 风格提取** | 提取风格 / 分析排版 / 模仿公众号 / 风格提取 / 主题提取 | `references/theme-{name}.md` 组件库 + 主题注册登记 |

路由后锁定模式，不混合。Mode A 产出的 HTML 可被 Mode B 提取的主题直接使用。

---

## 主题系统

| 主题 | 主色 | 适用场景 |
|------|------|---------|
| 翡翠绿 emerald | `#059669` | 教程/测评/清单（信息密度高） |
| 石墨灰 graphite | `#374151` | 设计/科技评论/高端品牌（极简留白） |
| 暖橙 sunset | `#EA580C` | 美食/生活/旅行（暖色调亲切感） |
| 海蓝 ocean | `#2563EB` | 企业/科技/金融（专业权威） |
| 胭红 rose | `#E11D48` | 时尚/美妆/节庆（热情活力） |
| 自定义 | — | 由 Mode B 提取或用 `theme-generator.md` 创建 |

---

## 平台红线

公众号编辑器是极度受限的富文本粘贴器。核心限制：

- **禁止**：`<style>` / `<script>` / `<div>` / `class` / `id` / 事件处理器 / `position` / `float` / `grid` / `@media` / CSS 变量
- **必须**：样式全部内联；文字节点用 `<span leaf="">` 包裹
- **可用**：`<section>` / `<span>` / `<p>` / `<img>` / `<table>` 等基础标签 + 内联 style 属性

完整红线表 → [`references/mode-a-format.md`](./references/mode-a-format.md)

---

## 双关卡可验证循环

| 关卡 | 脚本 | 作用 |
|------|------|------|
| **源头关** | `scripts/component_lint.py` | 扫描主题组件库源头的反模式 |
| **产物关** | `scripts/validate_output.py` | 扫描最终 HTML 是否符合平台限制 |

**两关全绿才交付。即使用户要求跳过，校验也不可绕过。**

```bash
# 排版校验（严重问题必须为 0）
python3 scripts/validate_output.py <output.html>
python3 scripts/validate_output.py <output.html> --ops   # 额外运营维度检查

# 组件库源头检查
python3 scripts/component_lint.py <skill-base>

# 风格提取
python3 scripts/style_extractor.py <url> [--output <name>]
python3 scripts/style_extractor.py --html <file.html> --output <name>

# 统一 CLI
./scripts/wechat validate <input.html>
./scripts/wechat lint
./scripts/wechat extract <url> [--output <name>]
```

---

## 内容智能处理（Mode A 核心特色）

| 处理项 | 说明 |
|--------|------|
| 章节自动编号 | `##` → 01/02/03，末章结语用 `∞` |
| 英文标签 | 据中文标题生成（实测→TEST、教程→TUTORIAL…） |
| 关键词下划线 | 每段主动标 1-3 个核心短语（即使原文没加粗） |
| 引言关键词高亮 | 识别开头金句核心词 |
| 目录提取 | 前 3 个 `##` 作为导读 |
| 全角标点 | 正文自动规范中文全角（代码块内保持原样） |
| 签名区 | 末尾一处，默认 `{{作者名}}` 占位 |

---

## 3 层视觉层级（克制三原则）

**锚点层**（全文 ≤5 处，主色加粗/深底白字）→ **标记层**（每段 1-3 处，下划线）→ **容器层**（按需，浅底引用/荧光笔/徽章）

克制三原则：① 主色只在锚点出现；② 大面积白底+灰阶；③ 一段内高亮 ≤2 种。

---

## 运行时回退策略

| 失败场景 | 回退 |
|---------|------|
| URL 抓取失败 | 提示用户提供本地 HTML 文件 |
| 颜色提取过少（<3 种） | 使用默认调色板填充 |
| 排版信息不足 | 使用标准值（字号 16px，行高 1.9） |
| 主题 CSS 未找到 | 回退 emerald 主题 |

---

## 目录结构

```
WeChatLayout/
├── SKILL.md                       # 入口文件（Intent Router + 工作流摘要）
├── README.md                      # 本文件
├── references/
│   ├── mode-a-format.md           # Mode A 排版工作流完整定义
│   ├── mode-b-extract.md          # Mode B 风格提取工作流完整定义
│   ├── common-components.md       # 通用组件库
│   ├── format-normalize.md        # 输入归一化规则
│   ├── theme-index.md             # 主题注册表（SSOT）
│   ├── theme-emerald.md           # 翡翠绿组件库
│   ├── theme-graphite.md          # 石墨灰组件库
│   ├── theme-sunset.md            # 暖橙组件库
│   ├── theme-ocean.md             # 海蓝组件库
│   ├── theme-rose.md              # 胭红组件库
│   ├── theme-generator.md         # 自定义主题生成器
│   └── paste-test-checklist.md    # 粘贴测试清单
├── scripts/
│   ├── validate_output.py         # 产物关校验
│   ├── component_lint.py          # 源头关扫描
│   ├── style_extractor.py         # 风格提取脚本
│   ├── validation_config.json     # 校验规则外化
│   └── wechat                     # 统一 CLI 入口
└── evals/
    ├── evals.json                 # 评测用例
    └── trigger-queries.json       # 触发词测试
```

---

## 完成判据

| Mode | 完成判据 |
|------|----------|
| **Mode A 排版** | HTML 不含 `<div>`/`class`/`id`；所有样式内联；文字节点用 `<span leaf="">` 包裹；`validate_output.py` 严重问题=0 |
| **Mode B 风格提取** | 生成 `references/theme-{name}.md`；在 `theme-index.md` 登记；提取颜色/排版/间距；域名白名单校验通过 |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-07 | 从 XDesign v2.8 提取公众号排版（Mode 4）和风格提取（Mode 5）为独立 skill |
| v1.1 | 2026-07 | ARE 评测后改进：P0 修复「不可跳过校验」硬指令 + 事件处理器 XSS 检查；P1 消除 SKILL.md 重复内容 + 新增 3 套主题（sunset/ocean/rose）+ 内容质量可验证规则；P2 校验规则外化为 validation_config.json + 运营维度可选检查（--ops） |

完整 Changelog → [`SKILL.md#changelog`](./SKILL.md#changelog)

---

## 版权与授权

**作者**：Qomob.AI

**版权声明**：本作品版权归 **Qomob.AI** 所有。

### 第三方素材声明

- **主题色板**：5 套预设主题（emerald / graphite / sunset / ocean / rose）的色阶色值参考自 [Tailwind CSS](https://tailwindcss.com) 调色板。Tailwind CSS 采用 [MIT 许可证](https://github.com/tailwindlabs/tailwindcss/blob/master/LICENSE)， Copyright (c) Adam Wathan, Jonathan Reinink, David Hemphill, Steve Schoger。本项目按 MIT 许可条款保留其版权声明，仅使用色值数字，未复制其源代码或样式表。
- **Python 依赖**：`requests`（Apache License 2.0）、`beautifulsoup4`（MIT License），按各自许可使用。

### 授权条款

- ✅ **个人学习与评估**：可免费使用、阅读、研究本 skill
- ✅ **内部非商业项目**：在署名 Qomob.AI 的前提下可使用
- ❌ **商业用途**：必须事先获得 Qomob.AI 书面授权
  - 包括但不限于：商业产品集成、付费 SaaS 服务、对外交付的项目、培训课程收费
- ❌ **再分发**：不得去除或修改版权声明与作者信息

如需商业授权，请联系 **Qomob.AI**。

> 未经授权而将本 skill 用于商业用途的，视为侵权行为，Qomob.AI 保留追究法律责任的权利。

