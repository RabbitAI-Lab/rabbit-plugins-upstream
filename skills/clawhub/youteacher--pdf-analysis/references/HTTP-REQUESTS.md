# HTTP 请求

下面以分析接口为例。把本地脚本生成的 `document` 对象放入请求体：

```sh
curl -sS -X POST "${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}/api/v1/pdf-analysis/pdf.analyze" \
  -H "Authorization: Bearer ${PDF_ANALYSIS_API_KEY}" \
  -H "Idempotency-Key: $(python3 -c 'import uuid; print(uuid.uuid4())')" \
  -H "Content-Type: application/json" \
  --data-binary @request.json
```

`pdf.analyze`、`pdf.question` 和 `pdf.compare` 是异步任务，创建后通常返回 `202`。使用响应中的 `task_id` 查询同一 operation：

```sh
curl -sS "${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}/api/v1/pdf-analysis/pdf.analyze/tasks/任务ID" \
  -H "Authorization: Bearer ${PDF_ANALYSIS_API_KEY}"
```

状态为 `queued` 或 `processing` 时采用递增间隔轮询；到达 `succeeded`、`partial`、`failed` 或 `cancelled` 后停止。不要用新的 Idempotency-Key 重复提交同一分析。
