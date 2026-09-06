# 字符统计页面

CQCCJY 用户端入口是 `https://vpcs.cqccjy.cn/pwp`。如果服务端同时返回 `orderNo`，工具会按已确认的前端路由提供：

- 中间/进度页：`/pwp?orderNo={order_no}&stage=progress`
- 支付确认页：`/pwp?orderNo={order_no}&stage=payment`（仅用户自主操作）
- 报告/结果查询页：`/reports?orderNo={order_no}`

没有订单号时不拼接订单页面，使用服务端 `resultUrl` 或入口地址。
