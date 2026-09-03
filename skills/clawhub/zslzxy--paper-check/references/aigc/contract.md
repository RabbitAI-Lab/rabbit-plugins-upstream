# AIGC 检测接口合约

当前 AIGC 用户端使用 `/api/paper/aigc/public/*`，与维普 PWP 查重是独立产品。先执行 `aigc-draft` 创建支付草稿；用户在 `/paper-aigc` 页面完成支付后，才能拿订单号执行文件提交。

## 顺序

1. `POST /order/pay/draft`：只建支付草稿，不自动扣款。
2. `POST /order/prepare-submit`：领取本次订单的 source OSS 票据和供应商票据。
3. 按票据 PUT 原文，再 `POST /order/complete-source-archive`。
4. `POST /order/mark-upload-attempted`：只有服务端声明 `shouldUpload=true` 时才向供应商上传一次。
5. 供应商 multipart 成功后 `POST /order/complete-direct-submit`。
6. `GET /order/{orderNo}`：查询异步状态；报告页使用 `/paper-aigc/check?orderNo=`。

任何票据不完整、订单未支付或供应商要求人工验证码时，停止自动提交并返回原页面，不暴露 token、timespan、uploadUrl 或文件内容。
