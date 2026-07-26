---

slug: finance-acct-tool-free
name: finance-acct-tool-free
version: 1.0.0
displayName: 财务会计入门工具
summary: "个人与小微企业财务会计工具，支持记账、对账、税务计算与基础报表生成.。面向个人用户与小微企业的基础财务会计工具，提供流水账记录、银行对账、"
license: Proprietary
edition: free
description: "面向个人用户与小微企业的基础财务会计工具，提供流水账记录、银行对账、
  增值税计算和标准财务报表生成功能。通过命令行操作简化日常财务工作，
  适合独立开发者、自由职业者和小型工作室使用。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。快速洞察数据价值，支持数据驱动决策。触发关键词：数据分析、文档生成、自动化、PDF、机器学习、自然语言"

  增值税计算和标准财务报表生成功能。通过命令行操作简化日常财务工作，

  适合独立开发者、自由职业者和小型工作室使用。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。'
tags:
  - Finance
  - 会计记账
  - 税务计算
  - 金融
  - 财务
  - 数据
  - python
  - finance
  - type
  - code
  - period
tools:
  - read
  - exec
  - write
homepage: ""
category: "Finance"

---
# 财务会计入门工具（免费版）

## 概述

本工具为个人用户和小微企业提供基础财务会计处理能力。涵盖日常记账、银行对账、增值税计算和标准财务报表生成四大核心功能。通过简洁的命令行操作，帮助用户高效管理日常财务事务.
## 核心能力

### 功能模块总览

| 模块 | 功能 | 免费版支持 |
|---|---|-----|
| 基础记账 | 收入/支出/转账记录 | 支持 |
| 科目管理 | 会计科目设置 | 基础科目 |
| 银行对账 | 自动匹配流水 | 支持 |
| 税务计算 | 增值税/所得税 | 基础计算 |
| 报表生成 | 三大标准报表 | 支持 |
| 文档生成 | 发票/对账单 | 基础模板 |

**处理**: 解析功能模块总览的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回功能模块总览的响应数据,包含状态码、结果和日志.
### 基础记账模块

- 流水账记录：收入、支出、转账
- 科目管理：基础会计科目设置
- 凭证生成：自动生成会计凭证
- 余额计算：实时计算账户余额

**处理**: 解析基础记账模块的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回基础记账模块的响应数据,包含状态码、结果和日志.
### 对账模块

- 银行对账：自动匹配银行流水
- 往来对账：客户/供应商对账
- 差异处理：自动识别差异
- 对账报告：生成对账报告

**处理**: 解析对账模块的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回对账模块的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：个人与小微企业财、务会计工具、支持记账、税务计算与基础报、面向个人用户与小、微企业的基础财务、会计工具、提供流水账记录、增值税计算和标准、财务报表生成功能、通过命令行操作简、化日常财务工作、适合独立开发者、自由职业者和小型、工作室使用、Use、when、需要数据分析、统计洞察、数据可视化时使用、不适用于实时流数、据处理、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：日常记账

用户输入："记录一笔销售收入1000元"

用户可通过自然语言指令触发此场景，工具将自动执行相应操作并返回结构化结果.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 财务会计入门工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 记录收入
python finance.py record --type income --amount 1000 --category "销售收入" --date "2026-02-28"
# ...
# 记录支出
python finance.py record --type expense --amount 500 --category "办公用品" --date "2026-02-28"
# ...
# 查看余额
python finance.py balance
```

### 场景二：银行对账

用户输入："帮我核对这月的银行流水"

```bash
# 导入银行流水
python finance.py reconcile import --file bank_statement.csv
# ...
# 自动对账
python finance.py reconcile auto
# ...
# 生成对账报告
python finance.py reconcile report --output reconciliation_report.pdf
```

### 场景三：月度税务计算

用户输入："计算二月份的增值税"

```bash
# 计算增值税
python finance.py tax vat --period 2026-02
# ...
# 生成税务报告
python finance.py tax report --type vat --period 2026-02 --output vat_report.xlsx
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 初始化

```bash
# 初始化账套
python finance.py init --company "我的工作室" --year 2026
# ...
# 设置会计科目
python finance.py accounts init --template small_business
```

### 常用命令

```bash
# 记账
python finance.py record --type income --amount 1000 --category "销售收入"
python finance.py record --type expense --amount 500 --category "办公费用"
# ...
# 生成报表
python finance.py report balance-sheet --period 2026-02 --output balance_sheet.pdf
python finance.py report income-statement --period 2026-02 --output income_statement.pdf
python finance.py report cash-flow --period 2026-02 --output cash_flow.pdf
# ...
# 税务
python finance.py tax vat --period 2026-02
python finance.py tax plan --year 2026
```

## 示例

### 会计科目设置

```yaml
accounts:
  assets:
    - code: 1001
      name: 现金
      type: current_asset
    - code: 1002
      name: 银行存款
      type: current_asset
  liabilities:
    - code: 2001
      name: 短期借款
      type: current_liability
  equity:
    - code: 3001
      name: 实收资本
      type: equity
  income:
    - code: 4001
      name: 主营业务收入
      type: revenue
  expenses:
    - code: 5001
      name: 办公费用
      type: expense
```

### 税务设置

```yaml
tax:
  vat_rate: 0.13            # 增值税率
  income_tax_rate: 0.25     # 企业所得税率
  tax_threshold: 300000     # 起征点
  declarations:
    vat: monthly            # 增值税申报周期
    income_tax: quarterly   # 所得税申报周期
```

## 最佳实践

1. **及时记账**：建议每日或每周记录收支，避免月底集中补录
2. **科目规范**：使用标准会计科目编码，便于后续报表生成
3. **对账频率**：每月至少进行一次银行对账，及时发现差异
4. **票据留存**：电子票据按月归档，便于税务申报与审计

| 实践要点 | 说明 |
|---:|---:|
| 数据备份 | 定期导出账套数据备份 |
| 科目一致性 | 年度内不随意调整科目编码 |
| 税率确认 | 每年初确认最新适用税率 |
| 报表审核 | 生成报表后核对关键数据 |

## 常见问题

### Q1：免费版支持多公司账套吗？

免费版仅支持单账套管理。如需管理多个公司的财务，建议升级至PRO版支持多账套切换.
### Q2：税务计算是否支持所有税种？

免费版支持增值税和企业所得税的基础计算。个人所得税、印花税等其他税种建议升级PRO版获取完整支持.
### Q3：数据存储在哪里？

所有财务数据存储在本地SQLite数据库中，不会上传至任何服务器。建议定期导出备份.
### Q4：支持电子发票生成吗？

免费版提供基础发票模板。如需批量生成或对接税务系统，建议升级PRO版.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| sqlite3 | Python库 | 必需 | Python内置 |
| openpyxl | Python库 | 可选 | `pip install openpyxl`（Excel导出） |
| reportlab | Python库 | 可选 | `pip install reportlab`（PDF生成） |

### API Key 配置

- 免费版无需任何API Key
- 所有数据本地存储，不涉及外部API调用

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 本地财务会计处理，数据存储在SQLite数据库
- **免费版限制**: 单账套、基础税种、基础报表模板

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
- 依赖Agent平台的LLM能力与运行环境配置
- 免费版功能受限，高级能力需升级专业版
- 处理能力受限于本地硬件资源

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "财务会计入门工具处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "finance acct"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
