# wanfang lane 合约

- `GET /api/paper/wanfang/public/config`：实时万方产品目录，使用返回的 `productCode`。
- `POST /api/paper/wanfang/public/upload/presign` → signed PUT → `POST /api/paper/wanfang/public/order/create`。
- `GET /api/paper/wanfang/public/order/{orderNo}`：复用订单号查询；正式检测和支付在原页面完成。

万方解析字数、报价和报告字段只按万方返回展示，不能冒充维普字符统计。
