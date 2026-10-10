# API 密钥配置与价格

默认 API 根地址为 `https://ai-skills.open-idea.net/api/v1`；密钥环境变量为 `DATA_CLEANING_API_KEY`，可选覆盖 `AI_SKILLS_API_URL`。从 ClawHub 安装免费；平台只对成功操作扣费。

- `clean.inspect`：免费
- `clean.preview`：¥0.08/千单元格
- `clean.execute`：¥0.18/千单元格

实际价格以[数据清洗产品页面](https://ai-skills.open-idea.net/skills/data-cleaning)和响应头 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance` 为准。不要记录、回显或提交完整 API Key。
