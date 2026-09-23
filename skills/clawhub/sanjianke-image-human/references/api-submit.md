# 全驱动数字人 · 提交任务

> a7w 插件 `image_human` 的接口 `submit` · 官方文档

---

## 提交任务

`POST /api/v1/apps/image_human/submit`

全驱动数字人任务，提供人物图片、驱动音频、可选用户提示词和生成模式。mode 支持 fast、standard、2k、4k；resolution 仅作为兼容别名；submit 按输入音频时长计费。

返回示例：`{ "task_id": 123, "status": "pending" }`