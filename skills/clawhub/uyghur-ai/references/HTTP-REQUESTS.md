# HTTP 请求示例

```bash
API_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}/api/v1"

curl --fail-with-body "$API_ROOT/uyghur-ai/translation" \
  -H "Authorization: Bearer $UYGHUR_AI_SKILL_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: uyghur-translate-001" \
  -d '{"from":"zh","to":"ug","content":"你好，世界。"}'
```

```bash
curl --fail-with-body "$API_ROOT/uyghur-ai/chat/completions" \
  -H "Authorization: Bearer $UYGHUR_AI_SKILL_API_KEY" \
  -H "Content-Type: application/json" \
  -H "Idempotency-Key: uyghur-chat-001" \
  -d '{"messages":[{"role":"user","content":"请用维吾尔语写一句欢迎语。"}],"temperature":0.4}'
```

```bash
curl --fail-with-body "$API_ROOT/uyghur-ai/pdf/translation" \
  -H "Authorization: Bearer $UYGHUR_AI_SKILL_API_KEY" \
  -H "Idempotency-Key: uyghur-pdf-001" \
  -F "file=@document.pdf" -F "from=ug" -F "to=zh" -F "mode=all_text"
```

成功计费头为 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、
`X-AI-Skills-Billing-Balance`。固定幂等键仅为示例；生产调用应使用 UUID 等唯一值。
