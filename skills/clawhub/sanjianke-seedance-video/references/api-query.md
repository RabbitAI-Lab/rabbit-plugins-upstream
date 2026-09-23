# Seedance 2.0 · 查询任务

> a7w 插件 `seedance` 的接口 `query` · 官方文档

---

## 查询服务任务（可选）

`GET /api/v1/tasks/{task_id}`

直接查询 maplego 网关任务状态；不计费或按 0 点固定价。
常规集成更推荐使用开放平台统一任务接口：`GET /api/v1/tasks/{task_id}`（使用本平台的 task_id）。