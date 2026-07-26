# 图片与视频 HTTP 请求参考

## 生成图片

```bash
curl -X POST https://media.open-idea.net/api/v1/image \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Idempotency-Key: <stable-request-id>" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "一幅宁静的草原风景",
    "width": 2048,
    "height": 2048,
    "style": "写实摄影，电影级光影",
    "image_count": 1
  }'
```

**响应（成功 201）：**

```json
{
    "success": true,
    "data": {
        "images": ["<base64 PNG data>"],
        "width": 2048,
        "height": 2048,
        "style": "写实摄影，电影级光影",
        "image_count": 1,
        "points_used": 56
    },
    "billing": {
        "charged": 0.56,
        "balance": 0.44,
        "currency": "CNY"
    }
}
```

**响应头：**

- `X-Mengguyu-Billing-Currency: CNY`
- `X-Mengguyu-Billing-Charged: 0.560000`
- `X-Mengguyu-Billing-Balance: 0.440000`

同一次用户生成请求请使用同一个 `Idempotency-Key`，新的生成请求要换新的 key。如果请求超时或需要重新读取结果，重复提交相同 key 和相同请求体会返回已生成结果，`billing.charged` 为 `0`，不会重复扣费。图片生成成功后应立即把 `data.images[]` 保存到文件；后续展示、下载或移动文件时不要再次调用生成接口。

把同一个 key 用于不同请求体时返回 `409`：

```json
{
  "error": {
    "message": "同一个 Idempotency-Key 不能用于不同的图片生成请求。",
    "type": "idempotency_conflict",
    "code": "idempotency_key_reused"
  }
}
```

## 根据文字和图片生成图片

```bash
curl -X POST https://media.open-idea.net/api/v1/image/edit \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Idempotency-Key: <stable-request-id>" \
  -F "prompt=基于参考商品图生成一张夏季清爽风格广告图，保留商品外观，预留标题区域" \
  -F "reference_image=@product.png" \
  -F "width=2048" \
  -F "height=2048" \
  -F "style=商业广告，干净排版，高级感" \
  -F "image_count=1"
```

也可以传 `image_url`，但 `reference_image` 和 `image_url` 只能提供一个。控制台推荐直接上传参考图片。这个 multipart 示例是客户端调用 Spark Media 的请求格式；Spark Media 服务端会再用 JSON 调用火山图片接口。

注意：火山上游图生图接口使用 JSON，请求体中的 `image` 是一个字符串 URL，例如 `"image": "https://..."`，不是 multipart 字段。上传后的参考图会以 URL 形式交给火山模型下载，因此该 URL 必须是公网可访问地址，不能是 `127.0.0.1`、`localhost` 或内网 IP。线上可配置 `IMAGE_REFERENCES_DISK=s3`，把上传参考图保存到 AWS S3，再通过公开 S3 URL、CloudFront 或 `IMAGE_REFERENCES_PUBLIC_URL` 交给火山读取；本地调试时请配置 `IMAGE_REFERENCES_PUBLIC_URL` 为 ngrok、Cloudflare Tunnel、CDN 或对象存储公开地址。

**响应（成功 201）：**

```json
{
    "success": true,
    "data": {
        "mode": "image_to_image",
        "images": ["<base64 PNG data or image URL>"],
        "width": 2048,
        "height": 2048,
        "style": "商业广告，干净排版，高级感",
        "image_count": 1,
        "reference_image_type": "upload",
        "points_used": 56
    },
    "billing": {
        "charged": 0.56,
        "balance": 0.44,
        "currency": "CNY"
    }
}
```

## 创建视频任务

```bash
curl -X POST https://media.open-idea.net/api/v1/video \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "雨夜城市街头，镜头缓慢推进，霓虹倒影，电影感",
    "duration": 5,
    "resolution": "720p",
    "ratio": "16:9"
  }'
```

**响应（成功 201）：**

```json
{
    "success": true,
    "data": {
        "task_id": "video_task_xxx",
        "status": "submitted",
        "duration": 5,
        "resolution": "720p",
        "ratio": "16:9",
        "video_url": null,
        "cover_url": null
    },
    "billing": {
        "charged": 6.46,
        "balance": 3.54,
        "currency": "CNY"
    }
}
```

## 根据图片创建视频任务

```bash
curl -X POST https://media.open-idea.net/api/v1/video/image \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -F "prompt=让参考图中的商品缓慢旋转，镜头轻微推进，背景光线从左向右扫过" \
  -F "reference_image=@product.png" \
  -F "duration=5" \
  -F "resolution=720p" \
  -F "ratio=16:9"
```

也可以传 `image_url`，但 `reference_image` 和 `image_url` 只能提供一个。上传后的参考图会以 URL 形式交给火山视频模型读取，因此该 URL 必须公网可访问。

**响应（成功 201）：**

```json
{
    "success": true,
    "data": {
        "task_id": "video_task_xxx",
        "status": "submitted",
        "generation_type": "image_video",
        "reference_image_type": "upload",
        "reference_image_url": "https://example.com/reference.png",
        "duration": 5,
        "resolution": "720p",
        "ratio": "16:9",
        "video_url": null,
        "cover_url": null
    },
    "billing": {
        "charged": 6.46,
        "balance": 3.54,
        "currency": "CNY"
    }
}
```

## 查询视频任务

```bash
curl -X GET https://media.open-idea.net/api/v1/video/<TASK_ID> \
  -H "Authorization: Bearer <YOUR_API_KEY>"
```

**响应（成功 200）：**

```json
{
    "success": true,
    "data": {
        "task_id": "video_task_xxx",
        "status": "succeeded",
        "video_url": "https://example.com/video.mp4",
        "cover_url": "https://example.com/cover.jpg"
    },
    "billing": {
        "charged": 0.0,
        "balance": 3.54,
        "currency": "CNY"
    }
}
```

## 错误响应

| HTTP 状态码 | 说明                                       |
| ----------- | ------------------------------------------ |
| 400         | 参数错误（如 prompt 为空）                 |
| 401         | 未授权（API Key 无效）                     |
| 403         | API Key 权限不足                           |
| 402         | 余额不足                                   |
| 409         | 当前已有视频任务进行中，需等待完成后再创建；或同一个 `Idempotency-Key` 被用于不同请求体 |
| 422         | 参数值不在支持列表中；或 `Idempotency-Key` 超过 191 个字符 |
| 429         | 超出每日消费限额（`daily_limit_exceeded`）；或触发每分钟请求限制 |
| 502         | 上游服务错误                               |

## 429 的两种情况

**429 有两个来源，处理方式完全相反，必须先看 `error.code` 区分。**

每日消费限额：响应体带 `error.code = daily_limit_exceeded`。

```json
{
  "error": {
    "message": "今日消费已达限额（¥100），请明日再试。",
    "type": "daily_limit_exceeded",
    "code": "daily_limit_exceeded"
  }
}
```

这种情况**当天重试都会失败**，应告知用户明日再试，不要重发请求。图片、图生图、视频、图生视频四个接口都会检查。

每分钟请求限制：Laravel 标准响应，**没有** `error.code`，`message` 为 `Too Many Attempts.`，并带 `Retry-After` 头。等待后重试即可成功。

## 尺寸错误响应

当图片尺寸不在支持列表中时，接口返回 `422`：

```json
{
    "error": {
        "message": "当前模型仅支持 2K 及以上的推荐尺寸组合，例如 2048x2048、2304x1728、2848x1600。",
        "type": "invalid_request_error",
        "code": "invalid_image_size"
    }
}
```

## 参考图错误响应

当 `reference_image` 和 `image_url` 均未提供，或二者同时提供时，接口返回 `422`：

```json
{
    "error": {
        "message": "请提供 image_url 或 reference_image，且二者只能提供一个。",
        "type": "invalid_request_error",
        "code": "invalid_reference_image"
    }
}
```

当参考图 URL 不是公网可访问地址时，接口返回 `422`：

```json
{
    "error": {
        "message": "图生图参考图地址必须是火山服务可访问的公网 URL...",
        "type": "invalid_request_error",
        "code": "reference_image_url_not_public"
    }
}
```

## 视频任务冲突响应

当同一账号已有视频任务进行中时，接口返回 `409`：

```json
{
    "error": {
        "message": "当前已有视频任务进行中，请等待成功或失败后再创建新任务。",
        "type": "conflict_error",
        "code": "video_task_in_progress"
    },
    "data": {
        "task_id": "video_task_xxx",
        "status": "processing"
    },
    "billing": {
        "charged": 0.0,
        "balance": 0.44,
        "currency": "CNY"
    }
}
```

## 计费说明

- 图片接口和图生图接口按实际点数结算，`billing.charged` 为本次实际费用
- 视频创建成功时按预计费用预扣，`billing.charged` 为本次预扣金额
- 视频任务失败后会退款；查询到失败状态时 `billing.charged` 可能为负数，表示本次退回金额
- 如需统一展示余额，优先使用 JSON body 中的 `billing.balance`，并可结合响应头交叉校验
