# 视频生成与轮询

## 创建任务

- 文生视频：`POST /api/v1/spark-media/video`
- 图生视频：`POST /api/v1/spark-media/video/image`

JSON 参数：

| 字段 | 约束 |
|---|---|
| `prompt` | 必填，最多 8000 字符 |
| `duration` | 可选，`5` 或 `10` 秒 |
| `resolution` | 可选，`480p`、`720p` 或 `1080p` |
| `ratio` | 可选，`16:9`、`9:16` 或 `1:1` |
| `watermark` | 可选，布尔值 |
| `image` | 仅图生视频必填；PNG/JPEG/WebP `data:` URL，解码后最大 5 MB |

两个创建接口都要求 `Idempotency-Key`，成功返回 HTTP 202、`task_id` 和初始 `status`。
平台同一用户同一时刻只允许一个活跃视频任务；HTTP 409
`video_task_in_progress` 表示应继续查询已有任务，不要创建并行任务。

## 查询任务

`GET /api/v1/spark-media/video/{task_id}`

每 5–10 秒轮询一次并限制总时长。`pending`、`submitted`、`queued`、`running` 等状态
视为进行中；`succeeded` 为成功；`failed`、`error`、`cancelled`、`canceled` 为终态失败。
成功后读取响应中的 `video_url` 或 `result` 并立即保存需要的内容。

`refunded: true` 表示失败任务的本次费用已退回。不要仅凭失败文本自行宣称退款；以该字段
及账单记录为准。失败状态不能当作可无限重试的理由，新任务必须由用户意图或明确恢复策略
驱动。
