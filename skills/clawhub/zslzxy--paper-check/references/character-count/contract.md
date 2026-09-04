# character-count lane 合约

- 固定走维普用户端：`POST /api/paper/check/public/pwp/order/create-draft`，再调用 `POST /api/paper/check/public/upload/presign`、OSS PUT 和 `POST /api/paper/check/public/upload/complete`。
- `GET /api/paper/check/public/order/{orderNo}`：查询解析状态与字符数。

结果重点字段：`orderNo`、`status`、`wordCount`/`actualWordCount`、`payAmount`。主结果只能称“字符数（不计空格）”；不把它当重复率或订单计费字数。

禁止字段：provider、employeeId、url、pay、detect、用户自定义域名。
