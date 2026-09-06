# reduction lane 合约

- `GET /api/paper/reduction/public/config`：实时降重/降 AIGC 产品目录。
- `POST /api/paper/reduction/public/order/create-draft`：创建草稿；原文/报告分别调用 presign 后 PUT。
- `POST /api/paper/reduction/public/order/{orderNo}/count/file`：触发字符计数和报价；`GET .../order/{orderNo}` 查询。

降重是改写服务，不等于查重；计字和报价以降重解析字段为准，不冒充通用字符数。禁止自动支付或保证降重比例。
