# cnki lane 合约

- `GET /api/paper/cnki/public/config`：实时知网产品目录，使用返回的 `productCode`。
- `POST /api/paper/cnki/public/upload/presign` → signed PUT → `POST /api/paper/cnki/public/order/create`。
- `GET /api/paper/cnki/public/order/{orderNo}`：复用订单号查询；正式检测和支付在原页面完成。

知网检测、AIGC 或按篇产品都必须由目录返回的代码确认，不将知网代码复用到万方。
