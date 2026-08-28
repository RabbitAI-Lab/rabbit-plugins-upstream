# API Key 与站点根


## 环境变量

```bash
: "${KNOWLEDGE_GRAPH_API_KEY:?请先设置 KNOWLEDGE_GRAPH_API_KEY}"
SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

默认 API 根为 `https://ai-skills.open-idea.net/api/v1`。

所有 POST 与任务 GET 使用：

```http
Authorization: Bearer $KNOWLEDGE_GRAPH_API_KEY
Content-Type: application/json
```

只从环境变量读取 Key。不要将 Key 放进 JSON、图谱字段、来源、日志、artifact、命令参数或回答。

Knowledge Graph 使用平台本地 Provider，无需第三方连接。若返回 `provider_not_configured`，视为平台部署或产品绑定故障：停止操作并联系平台管理员，不要尝试直连图数据库或其他服务。
