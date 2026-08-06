---
name: littlebeaver-invoice-assistant
description: 读取并分析本机小河狸发票助手中的数据。当用户要求连接小河狸发票助手、查询发票台账或明细、选择公司、统计进销项、分析客户/供应商/商品排行、查看月度开票趋势、汇总税额，或查询已归档电子发票附件时使用。通过应用的 localhost Skill API 在本机处理数据。
---

# 小河狸发票助手 Skill

许可证：MIT

通过用户本机运行的“小河狸发票助手”桌面应用读取发票数据。确保应用与智能体运行在同一台电脑上。仅调用本机 API，不通过本 Skill 上传发票数据。

默认使用简体中文回答。金额默认按人民币格式显示并保留两位小数；使用“开具”“取得”“进项”“销项”“价税合计”“作废”等中国财税常用术语。除非用户明确要求，否则不要把台账计算结果表述为最终应纳税额或纳税申报结论。

## 连接应用

1. 优先使用 `scripts/invoice_assistant_client.py`。
2. 用户提供地址时，传入 `--base-url http://127.0.0.1:<port>`。
3. 用户未提供地址时，扫描 `http://127.0.0.1:8876` 至 `http://127.0.0.1:8895`，并通过 `/api/metadata` 自动发现应用。
4. 自动发现失败时，请用户先打开“小河狸发票助手”，然后重试。

可选环境变量：

- `INVOICE_ASSISTANT_BASE_URL`：指定应用地址，例如 `http://127.0.0.1:8876`。
- `INVOICE_ASSISTANT_PORTS`：指定逗号分隔的端口或端口范围，例如 `8876-8895,9000`。

## 常用查询

在 Skill 目录中运行：

```bash
python scripts/invoice_assistant_client.py info
python scripts/invoice_assistant_client.py companies
python scripts/invoice_assistant_client.py summary --company-id 1 --start 2026-01-01 --end 2026-06-30
python scripts/invoice_assistant_client.py invoices --company-id 1 --keyword 作废 --page-size 100
python scripts/invoice_assistant_client.py items --company-id 1 --keyword 咨询服务
python scripts/invoice_assistant_client.py attachments --company-id 1
python scripts/invoice_assistant_client.py open-attachment --attachment-id 123
python scripts/invoice_assistant_client.py rankings --company-id 1 --limit 10
```

处理自然语言分析请求时，先获取满足问题所需的最小数据集：

- 选择公司：运行 `companies`。
- 汇总金额和月度趋势：运行 `summary`。
- 分析客户、供应商和商品排行：运行 `rankings`。
- 核查具体发票：运行 `invoices`，按需设置 `keyword`、`start`、`end`、`direction` 和分页参数。
- 分析商品或服务明细：运行 `items`。
- 查询已归档电子发票：运行 `attachments`，读取匹配的 PDF/OFD/XML 元数据。仅在用户明确要求打开本机文件时运行 `open-attachment`。

## API 规则

使用以下本机 Skill API：

- `/api/skill/health`
- `/api/skill/info`
- `/api/skill/companies`
- `/api/skill/summary`
- `/api/skill/invoices`
- `/api/skill/items`
- `/api/skill/attachments`
- `/api/skill/attachments/<id>/open`
- `/api/skill/rankings`

各接口支持的筛选参数不同：

- `company_id`：可重复传入。
- `start` 和 `end`：使用 `yyyy-mm-dd` 格式。
- `direction`：使用 `开具` 或 `取得`。
- `keyword`：对发票和明细执行模糊搜索。
- `page` 和 `page_size`：控制明细分页。
- `limit`：控制排行数量。
- `invoice_id`：按发票主表 ID 筛选附件。
- `file_type`：使用 `PDF`、`OFD` 或 `XML`。

`summary` 和 `rankings` 接口排除状态中包含“作废”的发票；明细接口保留所有状态，以便核查作废或异常发票。

附件响应包含文件类型、文件名、发票号码、公司、导出时间、文件大小、文件是否存在以及 `open_api` 路径，不暴露本机绝对路径。打开附件只调用用户本机的默认应用，不上传文件内容。

需要完整字段说明时，读取 `references/api.md`。

## 分析要求

回答财务问题时，明确说明所选公司、日期范围以及是否排除作废发票。

分析“哪些客户开票下降明显”等问题时，先读取汇总或排行数据；需要精确计算降幅时，再按月读取发票明细并比较相邻期间。区分发票台账测算与正式纳税申报结果。
