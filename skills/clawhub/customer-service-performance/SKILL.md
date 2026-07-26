---
name: customer-service-performance-excel
slug: customer-service-performance-excel
displayName: 客服坐席绩效核算（Excel版）
description: 通过Python脚本读取Excel数据和规则文件，转换为文本后由大模型解析字段、阶梯规则与权重，自动完成逐行核算与排名输出。适用于直接使用Excel文件的绩效评分场景。反馈与定制联系:zenobiazizi.skills@foxmail.com
version: 1.1.0
inputs:
  - name: data_file
    type: File
    required: true
    description: "客服绩效数据文件，支持 .xlsx、.xls、.md、.txt、.csv 格式，包含坐席主键及各项指标数值。"
  - name: rule_file
    type: File
    required: true
    description: "绩效考核规则文件，支持 .xlsx、.xls、.md、.txt、.csv 格式，包含指标、权重、正反向属性、阶梯阈值和扣分项。"
outputs:
  - name: result_table
    type: String
    description: "核算完成的 Markdown 表格，包含主键、各项得分、绩效总分、排名。"
  - name: summary_markdown
    type: String
    description: "面向管理者的绩效诊断简报，包含总体结论、Top3/Bottom3 观察和改进建议。"
metadata:
  author: shibo
  category: data-analysis
  tags: ["performance", "customer-service", "analytics", "ranking", "excel"]
  compatibility: Requires Python 3.10+ and pandas with openpyxl/xlrd for Excel reading.
---

# 客服坐席绩效核算（Excel版）

通过Python脚本读取Excel数据和规则文件，转换为文本后由大模型解析字段、应用加权和阶梯规则，完成所有坐席的得分计算与排名。

## Quick Start

1. 准备客服绩效数据文件（支持 .xlsx、.xls、.md、.txt、.csv 格式）
2. 准备评分规则文件（支持 .xlsx、.xls、.md、.txt、.csv 格式）
3. 使用 scripts/read_file.py 脚本读取文件转为文本格式
4. 将转换后的文本数据和规则文本输入进行核算

## 资源

- `scripts/read_file.py` - 读取Excel、Markdown、文本、CSV文件并转换为文本格式

## When to Use

- 客服团队月度/季度绩效评估
- 坐席排名分析与梯队划分
- 生成绩效诊断报告
- 评估客服服务质量
- 直接使用Excel文件作为数据源的场景

## Workflow

1. **读取文件数据**：使用 `scripts/read_file.py` 将Excel/Markdown/CSV文件转换为文本格式
2. **规则理解**：仔细阅读规则文本，提取出需要计算的指标名称、计算公式、阶梯条件、权重以及正反向（例如：工作量是否为线性，出错率是否为反向扣分）。
3. **数据解析**：读取数据文本中的每一行，识别主键（如工号、姓名）。若有缺失值，默认视为 0。
4. **执行计算（核心）**：
   - 严格按照规则文件中的每一条规则执行计算，维度名称、权重、计分方式完全由规则文件决定。
   - 识别每条规则的阶梯条件（分段阈值）和正反向属性（加分/减分）。
   - 若数据中缺少规则引用的字段，将该指标得分记为 0，不阻断后续计算。
   - 绩效总分 = 各项指标得分之和。
5. **排名**：
   * 根据绩效总分由高到低对所有坐席进行降序排名。
6. **输出结果**：生成最终的计算结果表格以及诊断简报。

## 规则处理原则

- **必须逐行核算**：不能遗漏任何一个提供在数据源中的坐席。
- **数学严谨性**：确保加减乘除计算精确，注意除数不能为0。
- **排名口径**：分数相同时并列排名。
- **阶梯规则优先**：如果规则中存在阶梯分段（如：接起率>95%得10分，90%-95%得8分），必须优先根据阶梯匹配得分。

## 输出要求

请提供结构清晰的回答，必须包含以下两部分：

### 1. 📊 最终核算结果表
（请使用 Markdown 表格输出，列名需包含：主键/姓名、[各项指标得分]、总分、排名）

### 2. 📝 绩效诊断简报
（输出一段 Markdown 诊断摘要，包含 Top 3 优秀坐席表扬、Bottom 3 需要关注的坐席，以及基于数据的简要管理建议）

## 安全与数据规范

- **数据脱敏**：上传数据前建议去除真实姓名/工号等敏感信息，或使用示例数据测试。
- **文件大小**：建议单个文件不超过 10MB，避免内存溢出。
- **Python 依赖**：scripts/read_file.py 依赖 pandas、openpyxl，安装命令：`pip install pandas openpyxl`

## 约束

- **文件读取**：优先使用 `scripts/read_file.py` 脚本读取文件，确保数据格式统一。
- **不编写任何代码**：你必须直接输出计算结果。
- **结果导向**：不要长篇大论地展示每个人的中间计算过程，直接输出最终表格。