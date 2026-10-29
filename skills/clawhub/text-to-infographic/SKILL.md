---
name: text-to-infographic
version: 1.2.2
description: 将对话或用户提供的内容组织成结构化信息图 plan（JSON），经布局语义与数值一致性校验后，用内置渲染器产出自包含静态 HTML 信息图。支持飞轮/鱼骨/桑基/金字塔/时间线/仪表盘六种 chart_family 布局。仅在用户明确请求信息图时调用。
allowed-tools: Read, Write, Bash
---

# Text to Infographic v1.2.2

把内容压缩为**可编辑的结构化 plan**，校验信息正确性，再渲染为**零依赖、零脚本、零外链**的静态 HTML 信息图。

## 与其他可视化工具的边界

- 主打「可编辑 plan + 信息正确校验 + 安全渲染」，不与海报型生成工具拼视觉；
- chart_family（flywheel / fishbone / sankey / pyramid / timeline / dashboard）是专用布局，通用图表请用图表类 skill。

## 何时使用

- 用户明确请求信息图（规格、HTML 或图片）；
- 用户提供了文章/笔记并希望可视化为单页信息图。

不要用于普通摘要、多页报告、幻灯片、照片编辑。

## 工作流（plan → validate → render）

1. **构建 plan**：把已提供内容整理为 `schemas/infographic-plan.schema.json` 结构的 JSON：
   - 按「关系本质」选布局：循环因果→flywheel；归因分析→fishbone；流量分解→sankey；层级递进→pyramid；时序→timeline；指标总览→dashboard；
   - 只用已提供的事实，缺失项标记而非补造；每条主张尽量带 `source_ref`。
2. **校验**：`python3 scripts/validate_infographic_plan.py plan.json [--source 原文.txt]`
   - 捕获布局语义错误：飞轮未闭环、鱼骨多头、桑基流量不守恒、仪表盘缺单位、时间线缺时标、并列内容被误写成流程；
   - 提供 `--source` 时额外做数值溯源（B 层）；ERROR 必须修复，WARN 需向用户说明。
3. **渲染**：`python3 scripts/render_infographic_html.py plan.json out.html`
   - 产出单文件静态 HTML：仅 HTML + 内联 CSS/SVG，**无 JavaScript、无外部请求、无第三方依赖**，可直接粘贴分享或打印。
4. 迭代 = 改 plan 再重跑两步，不推倒重来。

## 安全承诺（Safe Rendering）

- 渲染器仅用 Python 标准库，**不安装任何浏览器或依赖**；
- 产物**不包含脚本、不发起任何网络请求**，可离线打开、可打印、可安全分发；
- 不上传、不发布、不写入用户未指定的外部状态。

## 输入边界

- 只使用当前对话中用户提供的内容与文件；不联网抓取或核验；
- 缺失的事实、数值、引用保持未指定，并在 plan 中标注。

## 验证清单

- plan 通过 validate 脚本（0 ERROR）；
- HTML 以 `<!doctype html>` 开始、无 `<script>`、无 `http(s)://` 外链；
- 布局语义正确（飞轮闭环 / 鱼骨单头 / 桑基守恒 / 时间线含时标 / 仪表盘带单位）；
- 中文渲染无乱码、无溢出；仅依赖颜色传达信息的地方有文字冗余。
