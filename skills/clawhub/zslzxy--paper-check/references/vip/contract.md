# vip lane 合约

- `GET /api/paper/check/public/pwp/config`：实时维普产品目录，必须使用返回的 `productType`。
- `POST /api/paper/check/public/pwp/order/create-draft`：创建未支付草稿。
- `POST /api/paper/check/public/upload/presign` → OSS PUT → `POST /api/paper/check/public/upload/complete`：完成文件解析前置。
- `GET /api/paper/check/public/order/{orderNo}`：复用订单号查询；正式检测由用户在支付页完成。

创建任务代表解析/未支付前置流程，不代表付款、正式检测或报告已生成。只传本模块声明的字段。
