---
slug: "csv-analyzer-free"
name: "csv-analyzer-free"
version: "1.0.0"
displayName: "CSV数据分析-免费版"
summary: "CSV数据分析免费版，提供快速统计与基础筛选，零外部依赖，适合轻量数据探索。。CSV数据分析器免费版提供快速统计与基础筛选能力. 仅依赖Python标准库（csv模块），无需pandas或重"
summary_zh: "CSV数据分析免费版，提供快速统计与基础筛选，零外部依赖，适合轻量数据探索。。CSV数据分析器免费版提供快速统计与基础筛选能力. 仅依赖Python标准库（csv模块），无需pandas或重"
license: "MIT"
description: "|-. 适用于需要csv analyzer相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  CSV数据分析器免费版提供快速统计与基础筛选能力.
  仅依赖Python标准库（csv模块），无需pandas或重型依赖.
  核心能力：
  - 快速统计：stats命令返回行数、列类型、数值列min/max/mean、文本列unique计数
  - 基础筛选：filter命令支持比较运算符，可导出筛选结果
  - 自动列类型检测：数值、日期、文本自动识别
  升级付费版专享：Top/Bottom N、异常检测（z-score 2σ）、分组聚合（sum/count）、结果导出.
  适用场景：轻量数据探索、基础统计、简单筛选.
  不适用于：超过100MB的大文件、加密文件破解.
tags:
  - 信息检索
  - csv
  - analyzer
  - automation
  - productivity
  - 数据分析
  - 工具
  - 效率
  - pandas
  - stats
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
pricing_tier: free
---
# Csv Analyzer — CSV数据分析器（免费版）

用简单命令分析CSV文件，即时获取统计与筛选结果——无需pandas或重型依赖.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | CSV数据分析-免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 核心能力

### 核心能力（免费版）

- 参考`核心能力（免费版）`的配置文档进行参数调优
### 1. 快速统计（stats）
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） stats data.csv
```

返回行数、列类型、数值列的min/max/mean、文本列的unique计数.

- 异常时参考错误处理章节进行恢复
- 关键参数: `快速统计（stats）` 选项

### 2. 基础筛选（filter）
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） 
# ...
**输入**: 用户提供核心能力（免费版）相关的配置参数、输入数据和处理选项.
# ...
### 为何不用pandas？
# ...
pandas很强大，但仅导入就占100MB+内存，对快速分析任务过于重型。本技能仅用Python标准库，在2GB内存服务器上运行无压力.
# ...
**输入**: 用户提供为何不用pandas？相关的配置参数、输入数据和处理选项.
- 参考`为何不用pandas？`的配置文档进行参数调优
### 付费版专享能力
# ...
> 升级付费版解锁以下高级能力：
# ...
- **Top/Bottom N**：`top`/`bottom` 命令按指定列取前N/后N行（如 `--column revenue --n 10`）.
- **异常检测**：`anomalies` 命令基于z-score检测超出2σ的值.
- **分组聚合**：`group` 命令按指定列分组，支持 `sum`/`count` 等多种聚合函数，可同时指定多个
# ...
**输入**: 用户提供付费版专享能力相关的配置参数、输入数据和处理选项.
# ...
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 核心能力（免费版）(补充)
# ...
### 1. 快速统计（stats）(补充)
# ...
```bash
```
# ...
# ...
### 2. 基础筛选（filter）(补充)
# ...
echo "操作完成"
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） filter data.csv --where "amount>1000" --output big_orders.csv
```
# ...
支持比较运算符（`>`、`<`、`>=`、`<=`、`==`、`!=`），可将筛选结果导出为CSV.
# ...
### 3. 自动列类型检测
# ...
自动识别列类型：数值（numeric）、日期（date）、文本（text）。数值列做统计计算，文本列做unique计数.
# ...
## 为何不用pandas？(补充)
# ...
# ...
## 使用流程
# ...
1. **确认环境**：检查 `python3` 可用（无需安装任何外部包）.
2. **快速统计**：用 `stats` 命令获取数据概况（行数、列类型、min/max/mean）.
3. **按需筛选**：用 `filter` 命令按条件筛选行，支持比较运算符.
4. **导出结果**：用 `--output` 参数将筛选结果导出为CSV.
5. **验证输出**：检查导出文件的行数与内容是否符合预期.
# ...
## 示例
# ...
### 示例1：快速统计
# ...
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） stats orders.csv
# 输出：
# 行数: 1500
# 列: order_id(text, 1500 unique), amount(numeric, min=10.5, max=9999.0, mean=456.78),
#     category(text, 12 unique), order_date(date)
```
# ...
### 示例2：筛选大额订单并导出
# ...
echo "操作完成"
```bash
python3 {baseDir}/（请参考skill目录中的脚本文件） filter orders.csv
# 输出：筛选出87行，已导出到 big_orders.csv
```
# ...
### 示例3：按条件筛选
# ...
echo "操作完成"
```bash
csv --where "category==electronics"
# 输出：筛选出category为electronics的行
```
# ...
## 付费版专享能力(补充)
# ...
> 升级付费版解锁以下高级能力：
# ...
- **分组聚合**：`group` 命令按指定列分组，支持 `sum`/`count` 等多种聚合函数，可同时指定多个.
- **多聚合组合**：`--agg "sum:amount" "count:id"` 一次指定多个聚合.
- **统计分析扩展**：mean之外的median/std/percentiles等统计量.
- **多条件组合**：`--where` 支持 AND/OR 组合条件（免费版仅支持单条件）.
# ...
## 错误处理
# ...
| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| `FileNotFoundError` | 文件路径错误或不存在 | 校验文件路径与扩展名（.csv） |
| `python3: command not found` | 系统未安装Python 3 | 安装Python 3.x并确保 `python3` 在PATH中 |
| `--column` 列名不存在 | 列名拼写错误或大小写不匹配 | 先用 `stats` 查看实际列名，再传入 |
| `--where` 表达式无效 | 比较运算符或列名错误 | 使用合法运算符（`>`/`<`/`>=`/`<=`/`==`/`!=`）与正确列名 |
| 数值列含非数值 | 数据中有空值或字符串 | 清洗数据或确认列类型识别正确 |
| 日期解析失败 | 非ISO格式 | 优先使用ISO 8601（`2024-01-15`），其他格式可能无法识别 |
| 文件过大导致内存不足 | 超过约100MB | 改用pandas流式处理，或拆分文件 |
| `--output` 路径不可写 | 目录权限不足 | 检查目标目录权限或更换输出路径 |
| 调用付费版专享命令 | 免费版仅支持stats/filter | 升级付费版解锁top/bottom/anomalies/group命令 |
# ...
## 常见问题
# ...
### Q1：免费版支持哪些命令？
免费版支持 `stats`（快速统计）与 `filter`（基础筛选）两个命令。`top`/`bottom`/`anomalies`/`group` 为付费版专享.
# ...
### Q2：为何不用pandas？
pandas仅导入就占100MB+内存，对快速分析任务过于重型。本技能仅用Python标准库（csv模块），在2GB内存服务器上运行无压力.
# ...
### Q3：支持多大的文件？
设计支持约100MB以内的文件（载入内存）。超过此规模建议安装pandas或使用流式处理.
# ...
### Q4：支持哪些比较运算符？
`filter` 的 `--where` 支持 `>`、`<`、`>=`、`<=`、`==`、`!=` 六种比较运算符。多条件组合（AND/OR）为付费版专享.
# ...
### Q5：能检测异常吗？
免费版不提供异常检测。付费版提供 `anomalies` 命令，基于z-score检测超出2σ的值.
# ...
### Q6：能分组聚合吗？
免费版不提供分组聚合。付费版提供 `group` 命令，支持 `sum`/`count` 等聚合函数.
# ...
### Q7：如何升级到付费版？
参考 `csv-analyzer` 付费版SKILL.md，解锁Top/Bottom N、异常检测、分组聚合、多条件组合等能力.
# ...
## 已知限制
# ...
- 仅支持 `stats` 与 `filter` 命令，不支持 top/bottom/anomalies/group（付费版专享）.
- 设计支持约100MB以内的文件（载入内存），更大文件需pandas流式处理.
- 日期解析为基础级，优先支持ISO 8601格式，其他格式可能无法识别.
- `--where` 仅支持单条件，不支持 AND/OR 组合（付费版专享）.
- 仅依赖Python标准库，无pandas的向量化加速，大文件分析较慢.
- 不支持加密CSV文件的破解.
- 不支持多表JOIN与跨文件关联分析.
# ...