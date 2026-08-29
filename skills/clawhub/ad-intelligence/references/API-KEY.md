# API Key 配置


```bash
export AD_INTELLIGENCE_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选，仅站点根

SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

鉴权头为：

```text
Authorization: Bearer $AD_INTELLIGENCE_API_KEY
```

Key 仅用于 Ad Intelligence，abilities 为 `creative.search`、`advertiser.analyze`、
`trend.report`。不要要求用户在对话中粘贴完整 Key，不要把它写进 JSON、日志、结果或产物。
