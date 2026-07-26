---
name: spark-media
version: 1.0.3
description: 提供图片与视频任务能力：输入文本生成图片，基于文字和参考图生成新图片，创建文生视频或图生视频任务，并查询视频结果。图片同步返回结果；视频采用 task_id 任务制。使用同一 SPARK_MEDIA_API_KEY 调用。
triggers: 生成图片, 画一张图, text to image, 文生图, 图生图, 图片改图, 参考图生成, 根据图片生成图片, 广告图, 商品海报, AI绘图, 油画风格, 水彩画, 动漫风, 国画, 科幻风, 唯美风格, 制作图片, 画图, 生成图片, 生成视频, 做个视频, 文生视频, 图生视频, 根据图片生成视频, image to video, text to video, AI视频, 短视频原型, 视频分镜, 视频任务
metadata:
    {
        "openclaw":
            {
                "emoji": "🎨",
                "homepage": "https://media.open-idea.net",
                "primaryEnv": "SPARK_MEDIA_API_KEY",
                "requires": { "env": ["SPARK_MEDIA_API_KEY"] },
            },
    }
---

# Spark Media Skill 图片与视频生成技能

文本生成图片、图文生成图片、文生视频与图生视频服务，基于 Spark Media 中转服务调用火山引擎媒体生成 API。Base URL: **https://media.open-idea.net/api/v1**，`Authorization: Bearer <Key>`。

## Install

```bash
openclaw skills install @youteacherasia/spark-media
```

## Setup

- **`SPARK_MEDIA_API_KEY`**：[media.open-idea.net](https://media.open-idea.net) 登录后在「API Key」页创建。同一个 Key 可用于图片、图生图与视频接口。[API-KEY.md](./references/API-KEY.md)

## Privacy

生成图片或视频时，提示词文本与参考图片将发送至 **media.open-idea.net**，并由服务转发给上游火山引擎 API。请勿上传敏感或保密内容。

## Output

成功响应后，对用户展示业务结果 + 状态说明 + 计费行。

### 图片结果

- 根据 `data.images[]` 渲染 1-4 张图片
- 如果 `data.mode` 为 `image_to_image`，说明结果来自文字 + 参考图生成
- 成功响应后必须立即把 `data.images[]` 中的图片保存到本地临时文件或目标文件，再用该文件展示、下载或移动
- 保存、展示、移动、重命名图片时，必须复用本次响应里的图片数据，**不要**再次调用 `/image` 或 `/image/edit`
- 使用 `<img src="data:image/png;base64,...">`、本地文件或下载链接展示
- **不要**直接贴出完整 base64 字符串

### 视频任务结果

- 创建视频任务时，展示 `task_id` 与 `status`
- 创建或查询成功后，如响应包含 `video_url`、`cover_url`，展示可播放视频链接与封面
- 如果状态仍为 `submitted` / `processing`，明确提示这是异步任务，需要稍后继续查询

### 计费行

```text
本次扣费: {charged} CNY, 余额: {balance} CNY
```

HTTP 头字段：`X-Mengguyu-Billing-Charged` · `X-Mengguyu-Billing-Balance` · `X-Mengguyu-Billing-Currency`

说明：

- 图片接口和图生图接口中的 `billing.charged` 表示本次实际扣费
- 视频创建成功时 `billing.charged` 表示本次预扣费用；失败任务退款时，查询响应里的 `billing.charged` 可能为负数，表示本次退回金额

**禁止**对用户输出：完整 JSON、完整 base64、路由说明、模型名、token、Key 等内部信息。

## Usage

### 生成图片

```text
POST /image
Header: Idempotency-Key: <同一次用户生成请求的稳定唯一值>
Body: { "prompt": "描述文字", "width": 2048, "height": 2048, "style": "油画风格，厚涂笔触", "image_count": 1 }
```

响应：`data.images[]`（1-4 张 base64 PNG）+ `data.points_used`。收到响应后先保存图片；如果用户只是询问“图片放哪里了”或要求保存到桌面，使用已保存文件或本次响应数据，不要重新生成。

### 根据文字和图片生成图片

```text
POST /image/edit
Header: Idempotency-Key: <同一次用户生成请求的稳定唯一值>
Multipart Body: prompt="基于参考产品图生成夏季广告图", reference_image=@product.png, width=2048, height=2048, style="商业广告，清爽高级", image_count=1
```

参考图优先使用上传字段 `reference_image`；接口也支持 `image_url`。`reference_image` 和 `image_url` 二选一。multipart 是调用 Spark Media 的上传格式；Spark Media 服务端会以 JSON 调用火山，上游 `image` 字段为字符串 URL。参考图 URL 必须可被公网访问，不能使用 `127.0.0.1`、`localhost` 或内网地址。响应：`data.mode = image_to_image` + `data.images[]`（1-4 张图片数据或 URL）+ `data.points_used`。

### 创建文生视频任务

```text
POST /video
Body: { "prompt": "描述文字", "duration": 5, "resolution": "720p", "ratio": "16:9" }
```

响应：`data.task_id` + `data.status` + 本次任务参数；部分上游响应可能同时包含 `data.video_url` / `data.cover_url`

### 创建图生视频任务

```text
POST /video/image
Multipart Body: prompt="让参考图中的商品缓慢旋转，镜头轻微推进", reference_image=@product.png, duration=5, resolution="720p", ratio="16:9"
```

也可以传 `image_url`，但 `reference_image` 和 `image_url` 只能提供一个。响应：`data.task_id` + `data.status` + `data.generation_type = image_video`。

### 查询视频任务

```text
GET /video/{taskId}
```

响应：`data.status` + `data.video_url` + `data.cover_url`

### Idempotency-Key 规则

仅图片接口（`/image`、`/image/edit`）支持，视频接口不支持。

- **每一次新的生成请求都要用新的 key**；只有在超时或网络中断后重发**完全相同**的请求体时才复用同一个 key
- 同一个 key 配相同请求体重发：返回首次已生成的结果，`billing.charged` 为 `0`，不会重复扣费
- 同一个 key 配**不同**请求体：返回 `409` `idempotency_key_reused`，此时应换一个新 key 重新请求
- key 超过 191 个字符：返回 `422` `invalid_idempotency_key`

### 429 的两种情况

**处理方式完全相反，必须先看 `error.code` 区分。**

- `error.code = daily_limit_exceeded`：**每日消费限额**。当天重试都会失败，告知用户明日再试，**不要重发**
- 没有 `error.code`（`Too Many Attempts.`）：**每分钟请求限制**。等待几十秒后重试即可

说明：

- 图片接口是同步返回结果
- 图生图接口也是同步返回结果，适合参考图改图、商品广告图、海报延展等场景
- 视频接口是异步任务制，文生视频和图生视频都需要先创建再查询
- 当前每个用户同一时间只允许一个进行中的视频任务；若已有任务进行中，再次创建会返回 `409`

详见 [IMAGE-GENERATION.md](./references/IMAGE-GENERATION.md)、[VIDEO-GENERATION.md](./references/VIDEO-GENERATION.md) 和 [HTTP-REQUESTS.md](./references/HTTP-REQUESTS.md)。

## references/

| 文件                                                    | 用途                            |
| ------------------------------------------------------- | ------------------------------- |
| [HTTP-REQUESTS.md](./references/HTTP-REQUESTS.md)       | 图片 / 视频接口 curl 与响应示例 |
| [IMAGE-GENERATION.md](./references/IMAGE-GENERATION.md) | 图片生成详细说明                |
| [VIDEO-GENERATION.md](./references/VIDEO-GENERATION.md) | 视频任务详细说明                |
| [BEHAVIOR-RULES.md](./references/BEHAVIOR-RULES.md)     | 行为规范、确认、轮询与重试      |
| [API-KEY.md](./references/API-KEY.md)                   | Key 配置                        |
