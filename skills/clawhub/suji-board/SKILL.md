---
name: suji-board
description: 速记板——一个零依赖、纯前端的「碎片化文字收集 + 整理 + 导出 Word」单文件网页应用。当用户需要：收集/摘录散落各处的文字、自动编号整理要点、按主题用文件夹归档文档、把零散文字一键导出成标准 .docx 文件，或要求"做个文字收集板/速记工具/剪贴板整理器/资料归档页"时使用。也适用于"把一段 HTML 做成可安装的 skill"这类交付需求。
---

# 速记板（Suji Board）

一个单文件 HTML 应用（无构建、无后端、纯本地存储），把零散文字收集成结构化文档，一键导出 Word。

核心产物：`assets/word-doc.html`。直接用浏览器打开即可使用，无需安装任何依赖。

## 何时使用本 skill

- 用户要"做个文字收集/速记/摘录/剪贴板整理工具"
- 用户想把复制来的零散文字自动编号、归类、导出成文档
- 用户需要一个本地优先、不登录不上传的资料暂存与归档页
- 用户要把这个 HTML 包装成可安装、可分发的能力（skill）

## 核心能力

1. **粘贴即记录**：Ctrl+V 直接贴，或敲回车逐条添加，每条自动编号；复制内容时序号不随行。
2. **每条可整理**：折叠收起过长内容；存草稿箱（不参与编号与导出）；删除进回收站（可恢复、可彻底清除）。
3. **文件夹归档**：建文件夹分主题；上传/拖拽 txt·doc·docx·md·rtf·json·csv·log·xml·html 等文档；列表显示文件名/大小/上传时间；点开看正文、复制、删除。
4. **一键成稿**：导出标准 .docx（用内置 ZIP 打包，非 base64 伪装），可直接在 Word/WPS 打开。
5. **本地保存**：localStorage 存储，关页不丢；不联网、不登录、不上传。
6. **快捷键**：Ctrl+S / Cmd+S 保存，Ctrl+V 粘贴新增。

## 交付与分发

- 直接把 `assets/word-doc.html` 发给用户，或部署到任意静态托管。
- 要导出为可安装 skill 包：运行 `python -X utf8 <skill-creator>/scripts/package_skill.py <本目录>`。
- 产品命名与面向客户的功能介绍见 [references/product-intro.md](references/product-intro.md)。

## 实现说明（给维护者）

- 导出 docx 走原生 `Blob` + 手写 STORE 模式 ZIP（crc32 见脚本内 `makeZip`），不依赖任何库。
- 文件夹模块用标准 HTML5 拖放 API；`.doc/.docx` 为二进制附件，仅保存元信息、不解析正文；`.txt/.md` 等纯文本类可预览与复制正文。
- 全部状态存于 localStorage 三个键：`wordpad_entries`、`wordpad_trash`、`wordpad_drafts`、`wordpad_folders`。
