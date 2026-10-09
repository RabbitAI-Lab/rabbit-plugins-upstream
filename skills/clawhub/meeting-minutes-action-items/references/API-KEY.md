# API 密钥配置与价格

默认 API 根地址为 `https://ai-skills.open-idea.net/api/v1`；密钥环境变量为 `MEETING_MINUTES_ACTION_ITEMS_API_KEY`，可选覆盖 `AI_SKILLS_API_URL`。从 ClawHub 安装免费；平台只对成功操作扣费。

- `meeting.analyze`：输入 ¥0.006、输出 ¥0.012/千 tokens
- `meeting.export`：¥0.10/份

实际价格以[会议纪要与行动项产品页面](https://ai-skills.open-idea.net/skills/meeting-minutes-action-items)和响应头 `X-AI-Skills-Billing-Currency`、`X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance` 为准。不要记录、回显或提交完整 API Key。
