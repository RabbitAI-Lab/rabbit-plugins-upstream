# Happy Horse · 创建任务

> a7w 插件 `happy_horse` 的接口 `create` · 官方文档

---

## 创建任务（happyhorse 渠道）

`POST /api/v1/apps/happy_horse/create`

与 `submit` 入参完全一致，但锁死 happyhorse 渠道：内部走 aorizon `/api/v2/tasks` 流水线，
需要在应用配置里填入 `api_secret`（aorizon Bearer token），可选 `extra_config.happyhorse_base_url` 覆盖默认网关。

计费同 submit：**点数/秒 × 目标时长**，矩阵按输出分辨率 × 是否含视频输入分档（独立维护，可与 submit 不同）。