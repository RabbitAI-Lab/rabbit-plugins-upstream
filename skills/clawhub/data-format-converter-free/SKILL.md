---
slug: "data-format-converter-free"
name: "data-format-converter-free"
version: "1.0.0"
displayName: "数据格式转换(免费版)"
summary: "CSV与JSON、JSON与YAML基础互转，支持单文件转换与中文输出。数据格式转换器免费版，提供基础的数据格式互转能力. 核心能力包括： - CSV转JSON（csv.DictReader"
summary_zh: "CSV与JSON、JSON与YAML基础互转，支持单文件转换与中文输出。数据格式转换器免费版，提供基础的数据格式互转能力. 核心能力包括： - CSV转JSON（csv.DictReader"
license: "MIT"
description: "|-. 适用于需要data format converter相关能力的开发场景,包含结构化的工作流程和可复用的模板,帮助用户快速完成任务并保持代码质量.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性.该技能适用于相关开发场景,包含结构化的工作流程和配置指引.经过深度差异化处置,针对用户反馈和使用痛点进行了改进,提升了实用性和可操作性."
  数据格式转换器免费版，提供基础的数据格式互转能力.
  核心能力包括：
  - CSV转JSON（csv.DictReader读取，json.dumps输出）
  - JSON转CSV（csv.DictWriter写入，utf-8-sig编码）
  - JSON转YAML（yaml.safe_dump块样式输出）
  - YAML转JSON（yaml.safe_load安全解析）
  - 中文输出（ensure_ascii=False，allow_unicode=True）
  高级功能（XML互转、TOML互转、批量转换、嵌套结构处理）为付费版专享.
tags:
  - 信息检索
  - format
  - converter
  - automation
  - data-format
  - 数据处理
  - 数据分析
  - 工具
  - json
  - csv
tools:
  - read
  - exec
  - write
  - glob
homepage: ""
category: "Research"
pricing_tier: free
---
# 数据格式转换器（免费版）

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 数据格式转换(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 概述

在CSV、JSON、YAML等常用数据格式间进行基础转换，支持中文输出与UTF-8编码处理.
## 核心能力
### CSV转JSON
使用 `csv.DictReader()` 逐行读取为字典，通过 `json.dumps(ensure_ascii=False, indent=2)` 输出UTF-8中文JSON.
```python
import csv, json
# ...
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
# ...
json_str = json.dumps(rows, ensure_ascii=False, indent=2)
```

### JSON转CSV
使用 `csv.DictWriter()` 写入，需指定 `fieldnames`，`encoding='utf-8-sig'` 确保Excel兼容.
```python
import csv, json
# ...
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# ...
fieldnames = list(data[0].keys())
with open('output.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
```

### JSON转YAML
使用 `yaml.safe_dump()` 输出，`default_flow_style=False` 使用块样式，`allow_unicode=True` 保留中文.
```python
import yaml, json
# ...
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
# ...
yaml_str = yaml.safe_dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False)
```

### YAML转JSON
使用 `yaml.safe_load()` 安全解析（不执行任意Python对象）.
```python
import yaml, json
# ...
with open('data.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)
# ...
json_str = json.dumps(data, ensure_ascii=False, indent=2)
```

> **升级提示**：XML与JSON互转（`xmltodict.parse`/`unparse`）、TOML与JSON互转（`toml.load`/`dumps`）、批量目录级转换、嵌套结构自动扁平化为付费版专享功能.

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

1. **识别源格式**：根据文件扩展名（`.csv`/`.json`/`.yaml`）确定输入格式
2. **选择目标格式**：确认需要转换为何种格式（免费版支持CSV/JSON/YAML）
3. **加载源数据**：使用对应解析器读取文件（注意 `encoding='utf-8'`）
4. **执行转换**：通过JSON作为中间格式进行转换
5. **输出结果**：写入目标文件，注意 `ensure_ascii=False` 保留中文

## 示例

### 示例1：CSV转JSON

```text
输入 (CSV):
name,age,city
张三,30,北京
李四,25,上海
# ...
输出 (JSON):
[
  {"name": "张三", "age": "30", "city": "北京"},
  {"name": "李四", "age": "25", "city": "上海"}
]
```

### 示例2：JSON转YAML

```text
输入 (JSON):
{"database": {"host": "localhost", "port": 5432}, "debug": true}
# ...
输出 (YAML):
database:
  host: localhost
  port: 5432
debug: true
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| `json.JSONDecodeError` | JSON格式错误（尾随逗号、单引号） | 使用 `json.loads()` 严格解析，报告出错行号 |
| CSV含嵌套数据无法扁平化 | CSV单元格内含JSON字符串 | 免费版需手动扁平化，升级付费版获取自动处理 |
| `UnicodeDecodeError` 编码错误 | 文件非UTF-8编码 | 尝试 `encoding='gbk'` 或 `encoding='latin-1'` 读取 |
| JSON转CSV时值含逗号或换行 | CSV字段需引号包裹 | `csv.DictWriter` 自动处理引号转义，确保 `newline=''` |
| YAML含特殊字符未加引号 | 值含 `:` `#` `&` 等保留字符 | 输出时用 `default_style='"'` 强制引号包裹 |

## 常见问题

### Q1: 转换后中文变成 `\u5f20\u4e09` 怎么办？
A: 输出JSON时设置 `ensure_ascii=False`，如 `json.dumps(data, ensure_ascii=False, indent=2)`。YAML设置 `allow_unicode=True`.
### Q2: JSON转CSV时，JSON值是数组或对象怎么办？
A: CSV是扁平格式，无法直接表示嵌套结构。免费版需手动将嵌套值扁平化（如 `{"a": {"b": 1}}` → `{"a.b": 1}`），或转为JSON字符串存入单元格。付费版支持自动扁平化.
### Q3: 如何转换XML或TOML格式？
A: XML与JSON互转、TOML与JSON互转为付费版专享功能。免费版支持CSV、JSON、YAML三种格式互转.
### Q4: 如何批量转换多个文件？
A: 批量目录级转换为付费版专享功能。免费版需逐个文件手动执行转换.
### Q5: YAML转JSON时遇到 `!!python/object` 标签怎么办？
A: 这是非安全YAML标签。务必使用 `yaml.safe_load()` 而非 `yaml.safe_load()`，`safe_load` 会拒绝执行任意Python对象.
## 已知限制

- 免费版不支持XML与TOML格式转换
- 免费版不支持批量目录级转换
- 免费版不支持嵌套结构自动扁平化
- CSV是扁平格式，无法无损表示JSON的嵌套结构
- 升级至付费版可解锁全部高级功能
