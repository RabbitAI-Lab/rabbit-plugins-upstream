# API 密钥配置


```bash
export SPARK_MEDIA_API_KEY="ais_..."
export AI_SKILLS_API_URL="https://ai-skills.open-idea.net" # 可选
```

请求根地址为 `${AI_SKILLS_API_URL:-https://ai-skills.open-idea.net}/api/v1`。

```text
Authorization: Bearer $SPARK_MEDIA_API_KEY
```

密钥仅绑定 Spark Media，不能跨 Skill 使用。不要要求用户在聊天中粘贴完整密钥，也不要
将密钥写入代码、提示词、日志或生成文件。常见鉴权错误包括 `invalid_api_key`、
`key_expired`、`key_revoked`、`skill_not_active`、`user_skill_suspended` 和
`account_suspended`。
