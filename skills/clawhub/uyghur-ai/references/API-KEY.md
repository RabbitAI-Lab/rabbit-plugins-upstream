# API 密钥配置


```bash
export UYGHUR_AI_SKILL_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选
```

请求根地址为 `${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}/api/v1`，
鉴权头为：

```text
Authorization: Bearer $UYGHUR_AI_SKILL_API_KEY
```

每个密钥只绑定一个 Skill，其他产品的密钥不能调用维吾尔语接口。密钥缺失时引导用户在
平台控制台创建；不要要求用户把完整密钥发到对话中，也不要把密钥写进代码、日志、
文件名或错误信息。

常见鉴权错误包括 `invalid_api_key`、`key_expired`、`key_revoked`、
`skill_not_active`、`user_skill_suspended` 和 `account_suspended`。
