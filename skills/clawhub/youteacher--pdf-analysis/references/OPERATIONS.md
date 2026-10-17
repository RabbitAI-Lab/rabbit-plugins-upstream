# 操作说明

## PDF 内容分析

对应操作：`pdf.analyze`。提交一份 `document`，并选择 `analysis_type`：`summary`、`key_points` 或 `full`。可用 `instructions` 指定需要重点关注的内容。

## PDF 内容问答

对应操作：`pdf.question`。提交一份 `document` 和不超过 1000 字符的 `question`。回答必须只依据文档文字，并返回页码证据。

## PDF 多文档对比

对应操作：`pdf.compare`。提交 `documents` 数组，必须包含 2 至 3 份文档；全部文档总文字量不超过 180000 字符。`comparison_focus` 可指定价格、条款、版本变化或其他关注点。

## 导出 PDF 分析结果

对应操作：`pdf.export`。提交当前用户成功完成的 `pdf.analyze`、`pdf.question` 或 `pdf.compare` 的 `source_task_id`，生成 Markdown 和 JSON 私有文件。

分析结果统一包含：`title`、`summary`、`key_points`、`conclusions`、`evidence`、`limitations` 和 `documents`。`evidence` 每项包含 `document`、`page`、`quote` 和 `confidence`。
