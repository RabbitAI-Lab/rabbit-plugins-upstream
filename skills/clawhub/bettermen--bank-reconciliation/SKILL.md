---
name: bank-reconciliation
description: >-
  银行流水自动对账技能。导入银行流水（Excel/CSV）和账面记录，
  通过金额+日期精确匹配、模糊匹配、关联匹配三层引擎自动核销，
  生成交互式HTML可视化对账报告，标注待确认异常项。
  覆盖工商/建设/农业/中国/招商/兴业/浦发等主流银行流水格式。
  触发词：银行对账、流水对账、自动对账、导入银行流水、对账报告、
  银行流水匹配、账实核对、bank reconciliation。
agent_created: true
---

# 银行流水自动对账

四步对账流程，目标 90%+ 自动匹配率，财务只需处理少数异常项。

## 触发条件

当用户提到对账相关需求时使用此技能：
- "帮我对一下银行流水"
- "导入这个月的银行流水对账"
- "银行流水和账面记录对一下"
- 提供银行流水文件 + 账面记录文件

## 工作流程

### 1. 确认文件

向用户确认两个文件：
- **银行流水文件**：从网银导出的 Excel/CSV（含交易日期、借贷金额、摘要等）
- **账面记录文件**：ERP/财务系统导出的 Excel/CSV（含日期、凭证号、借贷金额、摘要等）

如果用户只有银行流水而没有账面记录，询问是否有标准格式的账目数据。

### 2. 运行对账引擎

执行 `scripts/reconcile.py`：

```bash
python scripts/reconcile.py \
  --bank <银行流水文件路径> \
  --books <账面记录文件路径> \
  --output reconciliation_result.json \
  --report reconciliation_report.html
```

可选参数（根据数据质量调整）：

| 参数 | 默认 | 说明 |
|------|------|------|
| `--date-tolerance` | 1 | 精确匹配日期容差天数 |
| `--amount-tolerance` | 0.01 | 精确匹配金额容差（元） |
| `--fuzzy-date-tolerance` | 3 | 模糊匹配日期容差天数 |
| `--fuzzy-amount-pct` | 0.05 | 模糊匹配金额百分比容差 |
| `--json-only` | - | 仅输出JSON，不生成HTML报告 |

**依赖**：需要 `pandas`, `openpyxl`, `rapidfuzz`。安装命令：

```bash
pip install pandas openpyxl rapidfuzz -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### 3. 展示结果

引擎完成后，使用 `present_files` 展示 HTML 报告给用户。报告中包含：

- **对账概览仪表盘**：总记录数、匹配数、待确认数、自动匹配率（环形图）
- **匹配明细表**：逐笔展示匹配对，标注匹配类型（精确/模糊/关联）和得分
- **待确认列表**：分 Tab 展示银行流水和账面记录中未能自动匹配的条目
- **导出功能**：支持导出待确认列表为 JSON

### 4. 解释结果

向用户解读报告关键指标：
- 匹配率 ≥ 90%：优秀，系统自动处理了绝大部分
- 匹配率 70-90%：良好，建议检查数据格式或调整容差
- 匹配率 < 70%：需排查，可能日期格式不一致或借/贷方列映射有问题

对"待确认"项给出处理建议：建议人工核对金额相近的或日期临近的未匹配项。

## 核心技术细节

### 列名自动识别

引擎内置 30+ 中文/英文列名别名，自动适配工商银行、建设银行、农业银行等主流格式。详细映射见 `references/matching_rules.md`。

### 借/贷方方向处理

银行流水和会计账面记录的借/贷方含义相反（银行视角 vs 企业视角），引擎自动处理此差异：
- 银行：贷方=收入(+)，借方=支出(-)
- 账面（资产类）：借方=收入(+)，贷方=支出(-)

### 三层匹配策略

1. **精确匹配**（金额+日期容差内）→ 自动核销
2. **模糊匹配**（金额百分比容差 + 日期放宽 + 摘要相似度）→ 自动核销
3. **关联匹配**（同户名批量匹配）→ 自动核销
4. **人工复核** → 标为待确认

## 典型使用示例

### 场景一：月度银行对账

```
用户："帮我对一下这个月的银行流水，银行流水是 6月流水.xlsx，账面是 6月账目.csv"
```

执行：
```bash
python scripts/reconcile.py --bank "6月流水.xlsx" --books "6月账目.csv" --output result.json --report report.html
```

### 场景二：调大容差

```
用户："有些金额差了几毛钱没匹配上，帮我把金额容差调大一点"
```

执行：
```bash
python scripts/reconcile.py --bank "流水.xlsx" --books "账目.csv" --amount-tolerance 0.5 --fuzzy-amount-pct 0.1
```

### 场景三：仅需结果数据

```
用户："帮我对账，只要结果数据就行，不用报告"
```

执行：
```bash
python scripts/reconcile.py --bank "流水.xlsx" --books "账目.csv" --json-only
```
然后向用户展示 JSON 中的 summary 和 unmatched 数据。
