# 异步任务与浏览器交接

所有文件 lane 都遵循“创建订单 → 上传（必要时）→ 完成解析/计数 → 查询 → 页面支付/报告”的状态机：

1. 生成一次 `clientRequestId`，网络重试复用它；幂等重放不得再次创建订单。
2. `submit` 是便捷的一次性适配命令；内部仍按用户端的 presign → PUT → complete 顺序执行。
3. 上传票据是短时执行数据，只在进程或权限为 0600 的临时文件中使用；日志和回答不得展示 URL、签名头或对象键。
4. `status`/`report` 只接受服务端返回的 `orderNo`，按页面提示退避；超时查询不能重新提交。
5. 结果输出统一包含 `lane`、`order_no`（有则返回）、`status`、`browser_url`、`browser_urls`、`browser_action`、`next_action` 和原始业务字段。

## 浏览器地址优先级

`browser_url` 优先取服务端的 `resultUrl`/`officialUrl`/`entryUrl`。当服务端返回订单号时，工具可依据域名配置中已确认的页面模板返回 `browser_urls.payment`、`browser_urls.progress`、`browser_urls.report`；模板中的订单号只能来自服务端，不接受用户传入的 URL 或域名。

提交后通常打开 `payment` 或 `progress`；完成后打开 `report`。Skill 不代替用户付款，支付和下载按钮由现有用户端处理。
