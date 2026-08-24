---
version: "1.00.03.195"
name: fuxin-doc-qa
description: >
  福昕 Office 文档问答技能。对当前打开的文档（Word / Excel / PowerPoint）内容进行只读问答，
  不修改文档。通过 MCP 网关调用各产品的只读工具获取全文/大纲/单元格/幻灯片文本，
  再基于内容解答用户提问、做摘要、找位置、核对数据。
  Trigger: "问文档", "文档问答", "这篇文章讲了什么", "总结这份文档", "文档摘要",
  "大纲", "ask_current_document", "doc-qa", "阅读文档".
---

# fuxin-doc-qa — 福昕 Office 文档问答技能

> **产品分类**: Word / Excel / PowerPoint（按当前活动文档所属产品）
> **依赖**: FuxinAiService（端口见 `fuxin-office-bridge`「运行端口」，由 `MCPServerPort.ini` 读取）
> **只读**: 是（本技能**绝不修改**文档，仅读取与呈现）

---

## 功能概述

本技能对当前活动文档进行只读问答与内容检索。它不通过场景写工具修改文档，
而是调用各产品**只读工具**拉取全文/大纲/单元格/选区内容，再基于获取的内容
回答用户提问、生成摘要、定位内容位置或核对数据。

覆盖能力：
1. **全文问答** — 基于文档全文回答问题
2. **摘要/要点** — 生成内容摘要或大纲式要点
3. **定位内容** — 查找文档中特定内容的位置（章节/页/单元格）
4. **数据核对** — 读取单元格数值、选区内容进行核验

> ⚠️ **禁止写入**：本技能只调用只读工具，绝不调用任何写工具（write_report /
> highlight / organize_deck 等）。需要修改文档时交给对应的 `fuxin-word` / `fuxin-excel` / `fuxin-ppt`。

---

## 架构与预检

```
用户 → FuxinAiService（端口见 `fuxin-office-bridge`「运行端口」）→ 产品只读工具 → FuxinOfficeWord/FuxinOfficeExcel/FuxinOfficePPT App
```

执行前需预检（见 `fuxin-office-bridge`）：
- 调用 `{产品}_get_document_info` / `{产品}_get_path` 探活 → 就绪后按产品选择只读工具
- 无活动文档 → 按 `fuxin-office-bridge`「无活动文档」文案提示，禁止继续
- **空文档/空演示（0 页）也是活动文档**，按 `docId`/`GetId` 是否非空判定，不误判为无文档

> 预检全程只读。本技能所有操作均为只读，无写操作，因此**无需保存确认**。

---

## 只读工具速查

按当前产品类别选用（产品分类：Word / Excel / PowerPoint）：

| 产品 | 只读工具 | 用途 |
|------|----------|------|
| Word | `get_document_text`（全文）/ `get_document_info` | 全文、文档信息、大纲、段落文本 |
| Excel | `get_document_text`（全文）/ `get_sheet_summary` / `get_cell_value`(row/col 0基) / `get_selection_values` / `get_path` | 单元格、选区、工作表摘要、全文 |
| PowerPoint | `get_document_info` / `get_ppt_outline`（大纲）/ `get_slide_text`(slideIndex 1基) / `get_selected_text_range` | 大纲、每页文本与备注 |

> 覆盖行/列的索引注意：Excel 单元格索引为 0 基；PPT 页索引为 1 基（slideIndex）。

### 读取策略

1. 优先调用 `get_document_info` / `get_sheet_summary` / `get_ppt_outline` 了解总体结构
2. 按需调用 `get_document_text` / `get_cell_value` / `get_slide_text` 获取细节
3. 结合内容回答用户提问；涉及大量文本时分块读取后汇总

---

## 使用方式

agent 识别到本技能的 Trigger 关键词后：

1. 判断当前活动文档的产品类别（Word / Excel / PowerPoint）
2. 按 `fuxin-office-bridge` 预检链路确认就绪
3. 使用上表只读工具分步读取内容
4. 基于内容回答用户提问（问答/摘要/定位/核对）
5. 输出回答；如需写操作则建议交由对应产品技能

### 与其它技能协同

- 读取到的文档内容如需进一步编排（高亮/批注/建表等），交给 `fuxin-word` / `fuxin-excel` / `fuxin-ppt`
- 预检统一走 `fuxin-office-bridge`
- 跨文档多轮问答属于 `fuxin-office` 汇总层 E2E 编排的一部分
