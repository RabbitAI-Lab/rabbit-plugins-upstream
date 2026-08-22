# md2pdf

📄 把 Markdown 文件以**渲染后的预览样式**导出为 PDF —— 中文友好，零外部依赖，离线可用。

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 这是什么

一个 OpenClaw/Claude Code Skill，把 `.md` 文件渲染成 GitHub 预览那种排版，再导出为 PDF。适合生成报告、文档归档、简历、周报等需要「漂亮打印」的场景。

**核心特性**
- 🎨 **所见即所得**：Markdown 先经 `marked.js` 渲染成 HTML，再用 Chrome headless `--print-to-pdf` 打印，输出即预览效果
- 🔌 **零外部依赖**：`marked.js`（MIT，35KB）已 vendored 进 `assets/`，全程离线不联网
- 🇨🇳 **中文友好**：内置 PingFang SC 优先字体栈 + GitHub 风格样式（标题/表格/代码块/引用/列表/加粗斜体/行内代码）
- 🚫 **无危险操作**：只读输入文件、写临时 HTML 到系统临时目录、用完即清，不做任何网络请求

## 快速开始

```bash
# 单文件：input.md → input.pdf（同名输出）
node scripts/md2pdf.js path/to/doc.md

# 直接传 Markdown 文本（stdin）
echo "# 标题" | node scripts/md2pdf.js --stdin -o out.pdf

# 自定义样式 + 纸张
node scripts/md2pdf.js doc.md --css custom.css --paper A4
```

## 前置条件

- Node ≥ 18
- Google Chrome（本机已装，脚本自动探测）

## 目录结构

```
md2pdf/
├── SKILL.md              # 技能说明
├── README.md             # 本文件
├── LICENSE               # MIT
├── VERSION               # 0.1.0
├── scripts/md2pdf.js     # 核心转换脚本（Node 单文件）
├── assets/
│   ├── marked.min.js     # vendored（MIT，离线）
│   └── style.css         # 中文友好 GitHub 预览风格
├── examples/demo.md      # 实测样例
└── references/chrome_flags.md  # Chrome headless 踩坑记录
```

## 安全说明

- 纯本地转换，无网络请求、无凭据读取、无外部命令注入
- 唯一的子进程调用是 Chrome headless 打印 PDF，参数为白名单硬编码
- 详见 `SKILL.md` 与安全自审清单
