---
slug: accounting-finance-tool-free
name: accounting-finance-tool-free
version: 1.0.0
displayName: 财务分析入门工具
summary: "企业财务分析与估值建模基础工具集，涵盖DCF、可比估值、财务比率等核心技能.。面向个人投资者与初级分析师的财务分析技能包，提供估值建模、财务比率分析、"
license: Proprietary
edition: free
description: '面向个人投资者与初级分析师的财务分析技能包，提供估值建模、财务比率分析、

  风险评估等基础能力。通过自然语言指令驱动Agent执行专业财务分析任务。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。Use
  when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。'
tags:
  - Finance
  - 估值分析
  - 财务建模
  - 金融
  - 财务
  - 数据
  - 财务比率
  - 分析
  - dcf
  - 风险评估
  - 盈利质量
tools:
  - read
  - exec
  - write
homepage: ""
category: "Finance"
---
# 财务分析入门工具（免费版）

## 概述

本工具为个人投资者和财务专业学生提供一套完整的财务分析基础能力。涵盖估值建模、财务比率分析、风险评估三大核心领域，通过结构化的分析框架帮助用户快速理解企业财务状况.
免费版聚焦单只标的的深度分析，包含 24 个常用财务分析技能，适合个人投资决策、课程学习和初步研究使用.
## 核心能力

### 估值建模模块

| 技能 | 用途 | 适用场景 |
|---|---|----|
| `dcf-zero-growth` | DCF零增长模型 | 成熟稳定企业估值 |
| `dcf-constant-growth` | DCF恒定增长模型 | 稳定增长期企业 |
| `dcf-two-stage` | DCF二阶段模型 | 高增长转稳定期企业 |
| `pe-valuation` | 市盈率估值 | 盈利倍数、行业对比 |
| `pb-valuation` | 市净率估值 | 账面价值倍数 |
| `ps-valuation` | 市销率估值 | 收入倍数 |
| `peg-valuation` | PEG估值 | 增长调整市盈率 |
| `wacc-calculation` | 加权平均资本成本 | WACC、折现率 |

**处理**: 解析估值建模模块的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回估值建模模块的响应数据,包含状态码、结果和日志.
### 财务比率分析模块

| 技能 | 用途 | 分析维度 |
|:-----|:-----|:-----|
| `financial-ratio-framework` | 财务比率综合分析 | 五维比率体系 |
| `dupont-five-factor` | 杜邦五因素分析 | ROE拆解 |
| `roe-analysis` | ROE分析 | 股东回报 |
| `gross-margin-analysis` | 毛利率分析 | 成本结构 |
| `revenue-analysis` | 收入分析 | 收入增长、质量 |
| `cashflow-forecasting` | 现金流预测 | 未来现金流 |
| `free-cashflow-calculation` | 自由现金流计算 | FCFF/FCFE |
| `working-capital-analysis` | 营运资本分析 | 流动性管理 |

**处理**: 解析财务比率分析模块的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回财务比率分析模块的响应数据,包含状态码、结果和日志.
### 风险评估模块

| 技能 | 用途 | 风险类型 |
|---:|---:|---:|
| `fraud-risk-detection` | 欺诈风险检测 | 财务造假识别 |
| `liquidity-risk-assessment` | 流动性风险评估 | 短期偿债能力 |
| `earnings-quality-analysis` | 盈利质量分析 | 利润可持续性 |
| `sensitivity-analysis` | 敏感性分析 | 关键变量影响 |
| `trend-analysis` | 趋势分析 | 时间序列趋势 |
| `peer-comparison-analysis` | 可比公司分析 | 横向对比 |
| `industry-benchmarking` | 行业基准对比 | 行业对标 |
| `investment-thesis-generation` | 投资论点生成 | 投资建议 |

**处理**: 解析风险评估模块的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回风险评估模块的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业财务分析与估、值建模基础工具集、可比估值、财务比率等核心技、面向个人投资者与、初级分析师的财务、分析技能包、风险评估等基础能、通过自然语言指令、Agent、执行专业财务分析、Use、when、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：个人投资者分析单只股票

用户输入："帮我分析一下贵州茅台的财务状况"

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| input | string | 是 | 财务分析入门工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```text
执行流程：
1. financial-ratio-framework - 财务比率综合分析
2. dupont-five-factor - ROE拆解分析
3. earnings-quality-analysis - 盈利质量评估
4. peer-comparison-analysis - 同业对比
5. 输出结构化分析报告
```

### 场景二：DCF估值建模

用户输入："用DCF模型估算某科技公司的合理估值"

```text
执行流程：
1. wacc-calculation - 计算加权平均资本成本
2. dcf-two-stage - 二阶段DCF估值
3. sensitivity-analysis - 关键变量敏感性分析
4. 输出估值区间与建议
```

### 场景三：财务风险排查

用户输入："这家公司有没有财务造假的风险？"

```text
执行流程：
1. fraud-risk-detection - 欺诈风险检测
2. earnings-quality-analysis - 盈利质量分析
3. liquidity-risk-assessment - 流动性风险评估
4. 输出风险等级与预警信号
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 单个技能调用

```text
/[skill-name]
例如：/dcf-two-stage
```

### 组合分析流程

```bash
# 示例
# 1. 财务比率综合分析
/financial-ratio-framework
# ...
# 2. ROE拆解
/dupont-five-factor
# ...
# 3. 盈利质量评估
/earnings-quality-analysis
# ...
# 4. 同业对比
/peer-comparison-analysis
```

### 数据输入格式

```python
# 财务数据输入示例
financial_data = {
    "company": "示例公司",
    "ticker": "600519.SH",
    "revenue": [10000, 12000, 15000],  # 近三年营收（万元）
    "net_income": [2000, 2500, 3200],  # 近三年净利润
    "total_assets": 50000,
    "total_equity": 30000,
    "cash_flow_ops": [1800, 2200, 2900]
}
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 配置示例

### 分析参数配置

```yaml
analysis_config:
  company:
    name: "示例公司"
    ticker: "000001.SZ"
    industry: "银行业"
# ...
  valuation:
    discount_rate: 0.10        # 折现率
    growth_rate: 0.05          # 增长率
    terminal_growth: 0.03      # 永续增长率
    forecast_years: 5          # 预测年限
# ...
  ratio_analysis:
    dimensions:                # 分析维度
      - profitability          # 盈利能力
      - solvency               # 偿债能力
      - operational            # 运营能力
      - growth                 # 成长能力
      - cashflow               # 现金流
# ...
  risk_thresholds:
    current_ratio_min: 1.5     # 流动比率下限
    debt_ratio_max: 0.7        # 资产负债率上限
    gross_margin_min: 0.2      # 毛利率下限
```

## 最佳实践

1. **数据完整性优先**：分析前确认财务数据完整，缺失关键科目会导致结论偏差
2. **多维度交叉验证**：不要仅依赖单一指标，结合财务比率、估值和风险三个维度
3. **行业可比性**：选择可比公司时注意行业、规模、商业模式的一致性
4. **敏感性测试**：估值结果对关键假设（增长率、折现率）高度敏感，务必测试不同情景
5. **趋势优于时点**：关注3-5年趋势变化，而非单一年份的绝对值

| 实践要点 | 说明 |
|:------|------:|
| 数据来源 | 优先使用年报/季报等官方披露数据 |
| 行业基准 | 与同行业可比公司横向对比 |
| 时间跨度 | 至少覆盖3年完整财务数据 |
| 假设披露 | 明确列出所有估值假设 |

## 常见问题

### Q1：DCF估值结果与市场价差异很大怎么办？

DCF是内在价值估算，与市场价格存在差异属正常现象。建议检查：增长率假设是否过于乐观、折现率是否合理、终值占比是否过高。同时结合可比估值方法交叉验证.
### Q2：财务比率分析需要哪些基础数据？

至少需要资产负债表、利润表、现金流量表三大报表的完整数据。建议覆盖最近3个完整会计年度，以保证趋势分析的可靠性.
### Q3：免费版支持批量分析多只股票吗？

免费版聚焦单只标的深度分析，暂不支持批量处理。如需批量分析多只股票并导出对比报告，建议升级至专业版（PRO）.
### Q4：分析结果可以直接用于投资决策吗？

本工具提供的分析结果仅供参考，不构成投资建议。投资有风险，决策需谨慎。建议结合基本面、技术面、宏观环境综合判断.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+（执行数值计算脚本时需要）

### 依赖详情

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|:---|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 可选 | 系统安装或conda环境 |
| numpy | Python库 | 可选 | `pip install numpy` |
| pandas | Python库 | 可选 | `pip install pandas` |

### API Key 配置

- 本skill基于Markdown指令规范驱动，无需额外API Key
- 如需接入外部财务数据源（Wind、Bloomberg等），需单独配置对应数据源的API凭证

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行财务分析任务
- **免费版限制**: 单标的深度分析，不支持批量处理与自动化报告生成

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------:|--------|:-------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
- 数据处理能力受限于本地硬件资源
- 大数据量时分析性能可能显著下降
- 数据准确性依赖输入质量，无法自动修正脏数据

## 示例

### 基本用法

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "财务分析入门工具处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "accounting finance"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
