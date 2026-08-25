# API Key 与站点根

## 环境变量

要求：

```bash
: "${AGENT_MEMORY_API_KEY:?请先设置 AGENT_MEMORY_API_KEY}"
```

默认 API 根为：

```text
https://ai-skills.open-idea.net/api/v1
```

`AI_SKILLS_API_URL` 只能覆盖站点根。例如值为 `https://example.internal` 时，实际 API 根是 `https://example.internal/api/v1`。不要把已含 `/api/v1` 的完整 API 根再次赋给它。

```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

## 鉴权

所有 POST 与任务 GET 都发送：

```http
Authorization: Bearer $AGENT_MEMORY_API_KEY
Content-Type: application/json
```

仅通过环境变量读取 Key。不要把 Key 放入 JSON、命令参数、日志、artifact、记忆或回答。示例中的 `$AGENT_MEMORY_API_KEY` 是变量引用，不是真实凭证。

Agent Memory 使用平台本地 Provider，不要求用户配置第三方连接。若平台仍返回 `provider_not_configured`，把它当平台部署或产品绑定故障：停止写入，保留请求证据并联系平台管理员；不要尝试直连第三方服务。
