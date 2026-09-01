# 操作、字段与结果

请求 JSON 总大小不超过 128 KiB；单据最多 100 条 items。所有未知字段都应省略。

## `document.create`

必填：`document_type`、`document_number`、`issue_date`、`issuer`、`recipient`。`document_type` 为 `quote`、`receipt`、`delivery_note`。

- issuer、recipient：`name` 必填；可选 `address`、`phone`、`email`、`tax_id`。
- quote、delivery_note 至少一条 items；每项含 `name`、`quantity`、`unit`，quote 还必须含 `unit_price`。
- receipt 必须含 `amount_received`；可选 `payment_method`。
- 可选 `currency`、`discount_rate`、`tax_rate`、`notes`。quantity 最多 3 位小数，金额最多 2 位小数，比例为 0 至 100 的十进制字符串。

结果 `document` 始终含 `document_id`、`document_number`、`document_type`、`version`、totals、`item_count` 和最多 10 项的 items 预览；`items_truncated:true` 表示完整明细应以私有 `business-document-pdf` artifact 为准。创建同时返回该 PDF。

## `document.read`

请求仅含 `document_id`。读取免费，返回最新 document，不创建 replacement。

## `document.update`

请求含 `document_id`、`expected_version`、非空 `changes`。changes 只可替换创建字段，不能改变 document_type。平台将变更合并为完整 replacement、重新计算 totals、将 version 加一，并返回新的 `business-document-pdf`。

## `document.export`

请求仅含 `document_id`、`expected_version`，不能夹带 changes。返回当前版本的 `business-document-pdf` artifact。
