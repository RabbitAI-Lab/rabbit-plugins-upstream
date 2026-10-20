# API 密钥与站点根

推荐在平台创建通用 Key，并执行 `openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"` 和 `openclaw gateway restart`，全平台 Skill 只需配置一次。仍需开通目标产品。下列 `KNOWLEDGE_GRAPH_API_KEY` 配置是兼容的产品专用覆盖项；调用优先使用该变量，为空时回退到 `AI_SKILLS_API_KEY`。两个变量均缺失时停止调用，不发送空 Bearer 请求。不要把旧请求换 Key 自动重试；幂等记录按 Key 隔离。



## 环境变量

```bash
: "${KNOWLEDGE_GRAPH_API_KEY:-${AI_SKILLS_API_KEY:?请先设置 AI_SKILLS_API_KEY 或 KNOWLEDGE_GRAPH_API_KEY}}"
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

默认 API 根为 `https://ai-skills.open-idea.net/api/v1`。

所有 POST 与任务 GET 使用：

```http
Authorization: Bearer ${KNOWLEDGE_GRAPH_API_KEY:-$AI_SKILLS_API_KEY}
Content-Type: application/json
```

只从环境变量读取密钥。不要将密钥放进 JSON、图谱字段、来源、日志、产物、命令参数或回答。

Knowledge Graph 使用平台本地服务提供方，无需第三方连接。若返回 `provider_not_configured`（未配置服务提供方），视为平台部署或产品绑定故障：停止操作并联系平台管理员，不要尝试直连图数据库或其他服务。
