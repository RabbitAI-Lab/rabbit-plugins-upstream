# API 密钥配置


```bash
export INVESTMENT_RESEARCH_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选，仅站点根

SITE_ROOT="${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}"
API_ROOT="${SITE_ROOT%/}/api/v1"
```

鉴权头：

```text
Authorization: Bearer $INVESTMENT_RESEARCH_API_KEY
```

密钥只用于 Investment Research，权限能力为 `filing.search`、`company.facts`、
`risk.analyze`、`report.create`。上游身份由 AI Skills 平台配置；不要要求用户粘贴平台密钥、
服务提供方凭证或 User-Agent，也不要把 secret 写入 JSON、日志、引用或报告。
