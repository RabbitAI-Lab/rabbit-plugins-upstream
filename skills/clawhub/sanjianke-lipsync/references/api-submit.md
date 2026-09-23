# 数字人对口型 · 提交任务

> a7w 插件 `lipsync` 的接口 `submit` · 官方文档

---

## 提交任务

`POST /api/v1/apps/lipsync/submit`

数字人对口型任务，提供数字人视频 URL、驱动音频 URL 和可选的数字人模型标识。xiaojiayu1.0 须配置弹性部署策略；xiaojiayu2.0/3.0 会先自动创建数字人，创建完成后提交视频生成任务。

返回示例：`{ "task_id": 123, "status": "pending" }`