# Happy Horse · 查询任务

> a7w 插件 `happy_horse` 的接口 `query` · 官方文档

---

## 查询任务

`POST /api/v1/apps/happy_horse/query`

按平台 `task_id` 拉取处理状态与结果。接口 **同步调用**，可与异步 submit 配合。
**内测期未放通时，会返回与 submit 一致的内测提示。**