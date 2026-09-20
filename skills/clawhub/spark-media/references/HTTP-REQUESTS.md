# HTTP 请求示例

```bash
API_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}/api/v1"

curl --fail-with-body "$API_ROOT/spark-media/image" \
  -H "Authorization: Bearer $SPARK_MEDIA_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: image-uuid-001" \
  -d '{"prompt":"雪山下的藏式村庄，电影感光线","width":1024,"height":1024,"count":1}'
```

```bash
curl --fail-with-body "$API_ROOT/spark-media/video" \
  -H "Authorization: Bearer $SPARK_MEDIA_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: video-uuid-001" \
  -d '{"prompt":"云层缓慢掠过雪山","duration":5,"resolution":"720p","ratio":"16:9","watermark":false}'
```

创建返回 HTTP 202 后：

```bash
curl --fail-with-body "$API_ROOT/spark-media/video/TASK_ID" \
  -H "Authorization: Bearer $SPARK_MEDIA_API_KEY"
```

图生图和图生视频将完整的 `data:image/png;base64,...` 放进 JSON 的 `image` 字段；不要
使用 multipart。生产中使用 UUID 等真正唯一的幂等键。

创建响应的计费头是 `X-AI-Skills-Billing-Currency`、
`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`。
