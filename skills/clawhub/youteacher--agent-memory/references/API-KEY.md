# API 密钥与站点根

推荐在平台创建通用 Key，并执行 `openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"` 和 `openclaw gateway restart`，全平台 Skill 只需配置一次。仍需开通目标产品。下列 `AGENT_MEMORY_API_KEY` 配置是兼容的产品专用覆盖项；调用优先使用该变量，为空时回退到 `AI_SKILLS_API_KEY`。两个变量均缺失时停止调用，不发送空 Bearer 请求。不要把旧请求换 Key 自动重试；幂等记录按 Key 隔离。



## 环境变量

要求：

```bash
: "${AGENT_MEMORY_API_KEY:-${AI_SKILLS_API_KEY:?请先设置 AI_SKILLS_API_KEY 或 AGENT_MEMORY_API_KEY}}"
```

默认 API 根为：

```text
https://ai-skills.open-idea.net/api/v1
```


```bash
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

## 鉴权

所有 POST 与任务 GET 都发送：

```http
Authorization: Bearer ${AGENT_MEMORY_API_KEY:-$AI_SKILLS_API_KEY}
Content-Type: application/json
```

仅通过环境变量读取密钥。不要把密钥放入 JSON、命令参数、日志、产物、记忆或回答。示例中的 `${AGENT_MEMORY_API_KEY:-$AI_SKILLS_API_KEY}` 是变量引用，不是真实凭证。

Agent Memory 使用平台本地服务提供方，不要求用户配置第三方连接。若平台仍返回 `provider_not_configured`（未配置服务提供方），把它当平台部署或产品绑定故障：停止写入，保留请求证据并联系平台管理员；不要尝试直连第三方服务。
