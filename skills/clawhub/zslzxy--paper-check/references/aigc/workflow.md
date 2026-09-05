# AIGC 工作流

用户说“查 AI”但没有订单号时，先调用 `aigc-draft` 并把支付页交给用户。不要把普通维普查重订单当成 AIGC 订单。用户支付后，使用同一订单号和同一文件完成一次 source archive、一次供应商上传和一次 complete；网络超时只查询订单，不重新创建支付草稿。

结果状态以服务端为准：`PENDING`/`PROCESSING` 表示异步处理中，`SUCCEEDED`/`COMPLETE` 才能说检测完成；没有报告下载地址时只返回报告页。
