# 音效生成、视频配音 · 提交任务

> a7w 插件 `mmaudio` 的接口 `submit` · 官方文档

---

## 提交弹性任务

`POST /api/v1/apps/mmaudio/submit`

音效生成、视频配音任务，提供视频 URL、可选 duration 视频时长和可选 prompt 音频生成提示词，平台将自动生成匹配的音频配音。可选提供参考音频 URL。

返回示例：`{ "task_id": 123, "status": "pending" }`（task_id 为弹性任务主键）