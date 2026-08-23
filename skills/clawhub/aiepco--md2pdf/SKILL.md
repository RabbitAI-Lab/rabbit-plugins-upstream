---
name: md2pdf
description: Convert Markdown files to rendered, print-ready PDFs with Chinese-friendly typography — fully offline, zero external dependencies. Use when exporting reports, docs, resumes, or meeting notes from .md to polished PDF.
---

# Markdown → PDF 转换技能

> 把 `.md` 文件以**渲染后的预览样式**导出为 PDF（不是原始源码），中文友好，零外部依赖。

## 核心理念

- **所见即所得**：Markdown 先经 `marked.js` 渲染成 HTML，再用 Chrome headless `--print-to-pdf` 打印成 PDF，输出的就是 GitHub 预览那种渲染效果。
- **零外部依赖**：Chrome 本机就有，`marked.js`（MIT，35KB）已 vendored 进 `assets/`，全程离线，不联网。
- **中文友好**：内置 PingFang SC 优先的字体栈 + GitHub 风格样式（标题/表格/代码块/引用/列表/加粗斜体/行内代码）。

## 技术栈

| 环节 | 实现 | 说明 |
|:---|:---|:---|
| Markdown 渲染 | `assets/marked.min.js` | MIT，vendored 离线 |
| PDF 生成 | Chrome headless `--print-to-pdf` | 本机 `/Applications/Google Chrome.app` |
| 编排 | `scripts/md2pdf.js` | Node 单脚本，无 npm 依赖 |

## 目录结构

```
md2pdf/
├── SKILL.md              # 本文件
├── scripts/
│   └── md2pdf.js          # 核心转换脚本（Node）
├── assets/
│   ├── marked.min.js      # vendored（MIT，离线）
│   └── style.css          # 内置中文友好样式（GitHub 预览风格）
└── references/
    └── chrome_flags.md    # Chrome headless 踩坑记录
```

## 快速开始

### 前置条件
- Node ≥ 18（`node -v`）
- Google Chrome（本机已装）

### 基本用法
```bash
# 单文件：input.md → input.pdf（同名输出）
node scripts/md2pdf.js path/to/doc.md

# 直接传 Markdown 文本（stdin）
echo "# 标题" | node scripts/md2pdf.js --stdin -o out.pdf

# 自定义样式覆盖
node scripts/md2pdf.js doc.md --css custom.css

# 纸张 + 页眉页脚
node scripts/md2pdf.js doc.md --paper A4          # A4（默认）/ Letter
node scripts/md2pdf.js doc.md --no-pdf-header-footer  # 关闭 Chrome 默认页眉页脚
```

### 参数说明

| 参数 | 说明 | 默认 |
|:---|:---|:---|
| `<input.md>` | 输入 Markdown 文件路径（位置参数） | 必填（或用 `--stdin`） |
| `--stdin` | 从标准输入读 Markdown 文本 | 关闭 |
| `-o, --output` | 输出 PDF 路径 | 与输入同名 `.pdf` |
| `--css` | 额外 CSS 文件（覆盖内置样式） | 无 |
| `--paper` | 纸张尺寸 `A4` / `Letter` | `A4` |
| `--no-pdf-header-footer` | 关闭 Chrome 默认页眉页脚 | 开启页眉页脚 |

## 架构

```
.md 文件 / stdin 文本
        │
        ▼
[marked.js 渲染成 HTML]  + 内置 style.css + 自定义 --css
        │
        ▼
[写临时 HTML 文件]
        │
        ▼
[Chrome headless --print-to-pdf]  --paper --no-pdf-header-footer
        │
        ▼
[输出同名 .pdf]
```

## 踩坑记录

- **Chrome headless 的噪音日志不是失败**：`ERROR:base/process/process_mac.cc` / `task_policy_set` 是 macOS 无害噪音，以「PDF 文件成功生成且非空」为准（详见 `references/chrome_flags.md`）。
- **必须 `--no-sandbox` 或 `--headless=new` 之一**：新版 Chrome 在部分环境需要，脚本已内置。
- **临时 HTML 用完即清**：写到系统临时目录，退出时删除，不留垃圾。

## 状态

- [x] marked.js vendored 离线
- [x] 中文友好 CSS 模板
- [x] Node 转换脚本（文件 + stdin 两种输入）
- [x] `--css` / `--paper` / `--no-pdf-header-footer` 选项
- [x] 实测样例验证（中文/表格/代码块渲染正常）
- [x] 安全自审通过（无网络请求/无凭据读取/参数白名单硬编码）
- [x] 上架元数据齐备（VERSION / LICENSE / README）
