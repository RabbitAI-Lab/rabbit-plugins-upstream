# API Key 配置

```bash
export SEO_AUDITOR_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选，仅站点根

SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

鉴权头：

```text
Authorization: Bearer $SEO_AUDITOR_API_KEY
```

Key 仅用于 SEO Auditor，abilities 为 `keyword.research`、`page.audit`、`competitor.gap`、
`report.create`。不要要求用户在对话中粘贴完整 Key，不把它写入 JSON、日志、证据或报告。
