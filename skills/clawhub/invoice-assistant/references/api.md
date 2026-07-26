# 小河狸发票助手本机 Skill API

基础地址由软件运行端口决定，通常是 `http://127.0.0.1:8876/api/skill`，如端口被占用，软件会自动顺延到后续端口。优先使用 `scripts/invoice_assistant_client.py` 自动发现。

## GET /api/skill/info

返回软件名称、版本、当前 Skill API 地址、公司数量、发票数量、明细数量。

## GET /api/skill/companies

返回公司列表、税号、别名、发票数量和价税合计汇总。

## GET /api/skill/summary

参数：`company_id`、`start`、`end`、`direction`。

返回发票方向汇总、月度趋势、开具/取得/差额指标。该接口剔除状态包含“作废”的发票。

## GET /api/skill/invoices

参数：`company_id`、`start`、`end`、`direction`、`keyword`、`page`、`page_size`。

返回发票主表，包含公司、发票号码、日期、购销方名称与税号、金额、税额、价税合计、票种、状态、风险、备注、原始 JSON、电子发票附件摘要等字段。

## GET /api/skill/items

参数同 `/api/skill/invoices`。

返回发票明细，包含商品服务名称、规格、单位、数量、单价、金额、税率、税额、价税合计、电子发票附件摘要等字段。

## GET /api/skill/attachments

参数：`company_id`、`invoice_id`、`file_type`。

返回已扫描归档的 PDF/OFD/XML 附件清单，包含附件 ID、发票 ID、公司、发票号码、文件类型、文件名、导出时间、文件大小、是否仍存在、可调用的本机打开接口。该接口不返回本机绝对路径。

## POST /api/skill/attachments/{id}/open

在本机调用系统默认程序打开指定附件。若文件不存在，或电脑未安装可打开 PDF/OFD/XML 的程序，会返回错误提示。该接口不会上传文件内容。

## GET /api/skill/rankings

参数：`company_id`、`start`、`end`、`direction`、`limit`。

返回 Top 客户、Top 供应商、Top 商品服务。该接口剔除状态包含“作废”的发票。
