# API 密钥配置

推荐在平台创建通用 Key，并执行 `openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"` 和 `openclaw gateway restart`，全平台 Skill 只需配置一次。仍需开通目标产品。下列 `INVESTMENT_RESEARCH_API_KEY` 配置是兼容的产品专用覆盖项；调用优先使用该变量，为空时回退到 `AI_SKILLS_API_KEY`。两个变量均缺失时停止调用，不发送空 Bearer 请求。不要把旧请求换 Key 自动重试；幂等记录按 Key 隔离。



```bash
export INVESTMENT_RESEARCH_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选，仅站点根

SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

鉴权头：

```text
Authorization: Bearer ${INVESTMENT_RESEARCH_API_KEY:-$AI_SKILLS_API_KEY}
```

密钥只用于 Investment Research，权限能力为 `filing.search`、`company.facts`、
`risk.analyze`、`report.create`。上游身份由 AI Skills 平台配置；不要要求用户粘贴平台密钥、
服务提供方凭证或 User-Agent，也不要把 secret 写入 JSON、日志、引用或报告。
