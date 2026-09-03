# 知网页面

入口：`https://cnki.cqccjy.cn/pzw`。订单页模板为支付 `/pzw?orderNo={order_no}&stage=payment`，进度/报告 `/pzw/check?orderNo={order_no}&stage=progress` 或 `/pzw/check?orderNo={order_no}`。不向用户暴露内部 API 前缀。
