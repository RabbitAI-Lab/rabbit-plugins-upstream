---
slug: "csv-handler-free"
name: "csv-handler-free"
version: "1.0.0"
displayName: "CSV文件处理(免费版)"
summary: "自动检测编码与分隔符，读取并清洗CSV数据，支持基础合并与导出。CSV文件处理免费版，提供基础的CSV读写与清洗能力. 核心能力包括： - 编码自动检测（utf-8、utf-8-sig、la"
summary_zh: "自动检测编码与分隔符，读取并清洗CSV数据，支持基础合并与导出。CSV文件处理免费版，提供基础的CSV读写与清洗能力. 核心能力包括： - 编码自动检测（utf-8、utf-8-sig、la"
license: "MIT"
description: "|-. 适用于需要csv handler相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  CSV文件处理免费版，提供基础的CSV读写与清洗能力.
  核心能力包括：
  - 编码自动检测（utf-8、utf-8-sig、latin-1）
  - 分隔符自动识别（逗号、分号、制表符）
  - CSV文件画像分析（行数、列数、表头判定）
  - 基础数据清洗（列名标准化、空行删除）
  - CSV导出（utf-8-sig编码）
  高级功能（多文件合并、按列拆分、类型转换、进度计划解析、成本解析）为付费版专享.
tags:
  - 研发工具
  - csv
  - handler
  - automation
  - productivity
  - data-processing
  - 工具
  - 效率
  - utf-8-sig
  - 编码
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
pricing_tier: free
---
# CSV文件处理（免费版）

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | CSV文件处理(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 概述

CSV是工程与财务领域最通用的数据交换格式。本免费版提供基础的CSV读取、编码检测与数据清洗能力，满足日常单文件处理需求.
## 核心能力
### 编码自动检测
通过 `chardet.detect()` 读取文件前 10000 字节进行编码推断，支持以下编码：

- `utf-8`：标准Unicode编码
- `utf-8-sig`：带BOM头的UTF-8（Excel导出常见）
- `latin-1`：西欧语言编码

检测失败时回退至 `utf-8`，避免抛出 `UnicodeDecodeError`.

### 分隔符自动识别
读取文件前 5000 字符，统计 `COMMON_DELIMITERS = [',', ';', '\t', '|']` 各分隔符出现频次，选取频次最高者作为分隔符.

- 参考`分隔符自动识别`的配置文档进行参数调优
### CSV文件画像分析
调用 `profile_csv()` 生成 `CSVProfile` 对象，包含 `encoding`、`delimiter`、`has_header`、`row_count`、`column_count`、`columns` 字段。表头判定逻辑：检查首列是否为纯数字（去除 `.` 和 `-`），若非数字则判定有表头.

### 数据读取与清洗
`read_csv()` 方法封装 `pd.read_csv()`，默认参数 `on_bad_lines='skip'`、`low_memory=False`。清洗流程包括列名标准化（转小写、空格转下划线）、删除全空行 `df.dropna(how='all')`、字符串列空白裁剪.
- 参考`数据读取与清洗`的配置文档进行参数调优
### CSV导出

`export_csv()` 默认使用 `utf-8-sig` 编码导出（带BOM，确保Excel正确显示中文），`index=False` 不写入行索引.
> **升级提示**：多文件合并（`merge_csvs`）、按列拆分（`split_csv`）、智能类型转换（`convert_types`）、进度计划专用解析（`ScheduleCSVHandler`）、成本数据专用解析（`CostCSVHandler`）为付费版专享功能.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY=${API_KEY:?请设置环境变量}
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 使用流程

1. **画像分析**：调用 `profile_csv("export.csv")` 获取文件编码、分隔符、行列数
2. **读取清洗**：调用 `read_csv("export.csv", clean=True)` 加载并自动清洗数据
3. **结果导出**：调用 `export_csv(df, "output.csv")` 以 `utf-8-sig` 编码写出

## 示例

### 示例1：文件画像与基础读取

```python
handler = ConstructionCSVHandler()
# ...
profile = handler.profile_csv("p6_export.csv")
# 输出: Encoding: utf-8-sig, Delimiter: ',', Rows: 1542, Cols: 7
# ...
df = handler.read_csv("p6_export.csv")
print(f"加载 {len(df)} 行, {len(df.columns)} 列")
# 输出: 加载 1542 行, 7 列
```

### 示例2：导出清洗后的数据

```python
handler.export_csv(df, "cleaned_output.csv", encoding='utf-8-sig')
# 生成带BOM的UTF-8文件，Excel可正确显示中文
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| `UnicodeDecodeError` | 文件包含非声明编码字符 | 使用 `errors='replace'` 替换非法字符，或手动指定 `latin-1` 编码 |
| BOM残留导致列名首字符异常 | `utf-8` 读取带BOM文件 | 改用 `utf-8-sig` 编码读取，BOM会被自动移除 |
| `ParserError: Error tokenizing data` | 行内字段数不一致 | 已通过 `on_bad_lines='skip'` 自动跳过，检查原始文件引号配对 |
| 分隔符误判 | 文件内逗号出现在文本字段中 | 手动指定 `delimiter='\t'` |
| `MemoryError` 大文件溢出 | 文件超过可用内存 | 使用 `nrows` 分批读取或 `chunksize=10000` 流式处理 |

## 常见问题

### Q1: Excel打开CSV中文乱码怎么办？
A: 导出时使用 `utf-8-sig` 编码（`export_csv(df, "output.csv", encoding='utf-8-sig')`），BOM头会让Excel正确识别UTF-8编码.
### Q2: 如何判断CSV是否有表头行？
A: `profile_csv()` 返回的 `has_header` 字段会自动判定——检查首列是否为纯数字，非数字则判定有表头.
### Q3: 欧式CSV用分号分隔，如何正确读取？
A: `detect_delimiter()` 会自动识别分号。也可手动指定：`handler.read_csv("data.csv", delimiter=';')`.
### Q4: 如何合并多个CSV文件？
A: 多文件合并为付费版专享功能。免费版建议手动使用 `pd.concat()` 处理少量文件，或升级至付费版使用 `merge_csvs()` 一键合并.
### Q5: 成本列含 `$` 符号如何处理？
A: 成本数据专用解析（`CostCSVHandler`）为付费版专享。免费版可手动执行 `df['col'].replace(r'[\$,]', '', regex=True)` 清洗.
## 已知限制

- 免费版不支持多文件合并、按列拆分、智能类型转换
- 免费版不包含进度计划与成本数据专用解析器
- 编码检测基于前 10000 字节采样，极少情况下可能误判混合编码文件
- `on_bad_lines='skip'` 会静默丢弃格式错误行，建议检查丢弃行数
- 升级至付费版可解锁全部高级功能

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "CSV文件处理(免费版)处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "csv-handler"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
