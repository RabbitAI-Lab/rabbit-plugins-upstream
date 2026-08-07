---
name: littlebeaver-financial-assistant
description: 读取并分析本机“小河狸财报助手”中已导入的财务数据。用户询问公司财务指标、资产负债表、利润表、现金流量表、历年或跨期趋势、财务数据对比、回款金额、本地财务问答时使用；仅通过 localhost 的只读接口访问数据。
---

# 小河狸财报助手

通过小河狸财报助手提供的本机只读 API，查询用户已经导入的公司、期间、三大财务报表、财务指标和趋势数据。不得直接读取或修改 SQLite 数据库。

## 使用前提

- 确认小河狸财报助手正在同一台电脑上运行，版本不低于 `1.7.4`。
- 优先使用随 Skill 提供的 `scripts/financial_assistant_client.py`。
- 自动在 `127.0.0.1` 和 `localhost` 的 `8765-8784` 端口发现服务。
- 本机访问保护不替代 Skill 的安全边界；始终只调用 `/api/local-agent/*` 只读接口。

## 标准流程

1. 先执行 `health`，确认连接的是 `financial-analysis-system`。
2. 公司不明确时执行 `companies`：只有一家公司时直接使用；存在多家公司且无法从问题确定时，请用户选择，不得静默使用第一家公司。
3. 执行 `periods` 确认可用的期间维度和具体期间。
4. 根据问题选择接口：
   - 明确、简单的中文财务问题，先使用 `ask`。
   - 查询整张报表或核对科目金额，使用 `statement`。
   - 查询指标和杜邦数据，使用 `metrics`。
   - 查询历年、跨期变化或生成图表，使用 `trend`；必要时结合多个期间的 `metrics` 或 `statement`。
5. 对分析结论进行数据核对。涉及比较、异常判断或图表时，不要只依赖自然语言回答，应取得结构化数据。

## 公司与期间判断

- 将“21年”“25年”等两位年份结合现有期间解释为 `2021年`、`2025年`，不要内置固定年份列表。
- 将“2021-2023”“21年至23年”“21年与23年比较”识别为多个明确期间，并只使用这些期间的数据。
- 将“历年”“历期”“近几年”识别为跨期查询；“近几年”默认取最近 3 至 5 个可用年度，并说明实际使用范围。
- 用户明确指定年份、月份、季度或期间维度时，严格按指定条件查询。
- 指定期间不存在时，直接说明未导入该期间，不得自动替换成最新期间。
- 用户未指定期间时，才可使用所选公司最近的可用期间，并在回答中明确说明。
- 不要把月报、季报和年报混在同一趋势中。无法判断维度时，先查看 `period_counts` 和 `latest_period`，必要时请用户确认。

## 科目与常见表达

- “回款”“销售回款”默认对应现金流量表的“销售商品、提供劳务收到的现金”。
- “营收”“收入”通常对应“营业收入”；存在多个收入科目且问题含义不明确时，列出候选项。
- “经营现金流”通常对应“经营活动产生的现金流量净额”。
- 科目名称可能包含 `加：`、`减：`、序号、括号说明或中英文冒号，应以接口返回的标准名称和数值为准。
- 不要把名称相近但方向不同的科目混淆，例如应收与应付、预付与应付、现金流入与现金流量净额。

## 数据准确性

- 将 `null` 视为缺失数据，将 `0` 视为真实零值，二者不得混淆。
- 不得猜测、补齐或虚构未返回的金额、期间和指标。
- 保留接口返回的金额口径，不要根据原报表的“元、千元、百万元”再次重复换算。
- 优先采用接口已经计算的指标。自行计算时说明公式、使用期间和数据来源。
- 对只有一期数据的科目，不得声称存在趋势；应说明当前只能展示单期金额。
- 不同公司之间比较时，分别标明公司、期间、单位和报表维度。

## 命令示例

```bash
python scripts/financial_assistant_client.py health
python scripts/financial_assistant_client.py companies
python scripts/financial_assistant_client.py periods --company "公司名称" --period-type year
python scripts/financial_assistant_client.py metrics --period-id 1
python scripts/financial_assistant_client.py statement --period-id 1 --statement income_statement
python scripts/financial_assistant_client.py trend --company "公司名称" --period-type year --metric revenue
python scripts/financial_assistant_client.py ask "2021年至2023年营业收入分别是多少" --company "公司名称" --period-type year
```

报表类型参数：

- `balance_sheet`：资产负债表
- `income_statement`：利润表
- `cash_flow`：现金流量表

常用指标参数：

- `revenue`：营业收入
- `net_profit`：净利润
- `gross_margin`：毛利率
- `net_margin`：净利率
- `operating_cash_flow`：经营活动现金流量净额
- `debt_ratio`：资产负债率
- `cash`：货币资金
- `receivables`：应收账款
- `inventory`：存货

## 回答要求

- 默认使用中文，除非用户明确要求其他语言。
- 开头直接给出答案，再补充必要的数据依据或计算过程。
- 明确写出公司、期间和期间维度；金额较大时可换算为万元或亿元，但保留合理精度并注明单位。
- 用户要求趋势图时，使用结构化的 `categories` 和 `values` 生成图表；缺失点保持缺失，不要补成 `0`。
- 经营分析、原因判断和建议必须区分“数据事实”与“分析判断”，不要把推测表述为确定事实。

## 安全与错误处理

- 只访问 `127.0.0.1` 或 `localhost`，不得访问局域网 IP、公网地址或分享链接。
- 只调用 `/api/local-agent/*`，不得执行导入、删除、修改公司、修改配置或创建分享链接。
- 将返回的财务数据视为用户本地私有数据。未经用户明确要求，不得发送到云端模型或外部服务。
- 找不到服务时，提醒用户先打开小河狸财报助手，再重新执行命令。
- 接口返回期间、公司、科目或指标不存在时，用中文说明缺少什么数据，并建议检查对应报表是否已导入。
