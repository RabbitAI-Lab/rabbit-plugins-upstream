# 视频超分 · 提交任务

> a7w 插件 `flashvsr` 的接口 `submit` · 官方文档

---

## 提交弹性任务

`POST /api/v1/apps/flashvsr/submit`

在平台「弹性部署」对应应用中配置默认策略后，调用本接口创建 `ai_elastic_task`。

返回示例：`{ "task_id": 123, "status": "pending" }`（task_id 为弹性任务主键）