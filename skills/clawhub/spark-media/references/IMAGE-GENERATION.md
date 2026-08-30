# 图片生成与编辑

## 文生图

`POST /api/v1/spark-media/image`

| 字段 | 约束 |
|---|---|
| `prompt` | 必填，最多 8000 字符 |
| `width`、`height` | 可选，各 512–4096 |
| `count` | 可选，1–4 |

## 图生图

`POST /api/v1/spark-media/image/edit`

除 `prompt`、`width`、`height` 外，必须提供 JSON 字段 `image`。其值是完整的 PNG、
JPEG 或 WebP `data:` URL，例如 `data:image/png;base64,...`；不是 multipart 文件。
解码后的图片不得超过 5 MB。

两个接口都要求：

```text
Authorization: Bearer ...
Idempotency-Key: 每个新逻辑请求的唯一值
Content-Type: application/json
```

保持用户要求的主体、构图、文字和风格。编辑图片时以用户提供的原图为事实来源；不要为了
下载、改名、移动或再次展示结果而重新调用生成接口。响应中的媒体字段由上游模型决定，
应解析并持久化实际返回内容；不要假设始终是某一种 URL 结构，也不要在聊天中输出完整
base64。
