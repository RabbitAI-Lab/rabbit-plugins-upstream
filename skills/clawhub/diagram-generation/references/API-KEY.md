# API 密钥配置与价格

默认 API 根地址为 `https://ai-skills.open-idea.net/api/v1`；密钥环境变量为 `DIAGRAM_GENERATION_API_KEY`，可选覆盖 `AI_SKILLS_API_URL`。从 ClawHub 安装免费；无需购买或配置第三方服务账号，平台只对成功操作扣费。

- `diagram.plan`：输入 ¥0.006、输出 ¥0.012/千 tokens
- `diagram.render`：¥0.10/份

实际价格以[图表生成产品页面](https://ai-skills.open-idea.net/skills/diagram-generation)和响应头 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance` 为准。不要记录、回显或提交完整 API Key。
