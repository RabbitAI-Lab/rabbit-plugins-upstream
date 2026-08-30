# 计费说明

SQL 数据分析按人民币计费：

- 数据集导入 `dataset.ingest`：¥0.05/文件。
- 自然语言分析 `analysis.run`：¥0.20/次。
- 显式 SQL 查询 `query.execute`：¥0.08/次。
- 本地报告 `report.create`：¥2.90/份。

`doctor`、`dataset.inspect` 和 `dataset.delete` 在本地免费执行。

Runner 可展示计费币种、实扣金额和余额响应头，但这些信息仅用于计费遥测，不参与签名票据验证。
