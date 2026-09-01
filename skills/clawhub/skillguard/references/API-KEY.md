# API Key 配置


```bash
export SKILLGUARD_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选
```

请求根地址为 `${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}/api/v1`。

```text
Authorization: Bearer $SKILLGUARD_API_KEY
```

Key 只绑定 SkillGuard，不可跨 Skill 使用。不要要求用户在对话中粘贴完整 Key，不要把它
写进待审计源码、日志或审计报告。常见鉴权错误包括 `invalid_api_key`、`key_expired`、
`key_revoked`、`skill_not_active`、`user_skill_suspended` 和
`account_suspended`。
