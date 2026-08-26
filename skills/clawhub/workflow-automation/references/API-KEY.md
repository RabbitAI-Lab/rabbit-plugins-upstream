# API Key 配置

```bash
export WORKFLOW_AUTOMATION_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选，仅站点根

SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

鉴权头：

```text
Authorization: Bearer $WORKFLOW_AUTOMATION_API_KEY
```

Key 只用于 Workflow Automation，abilities 为 `workflow.validate`、`workflow.trigger`、
`execution.read`、`execution.history`。Provider 连接、允许列表、固定 Production Webhook 和
认证 secret 必须预先在 AI Skills 平台配置；不要要求用户在对话中粘贴平台 Key、Provider Key
或 webhook secret，也不要把 secret 写入 JSON、日志、input 或结果。
